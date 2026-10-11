#!/usr/bin/env python3
"""Event-sourced resource/permission/knowledge checker for V13 alpha.

This is deterministic consistency checking ONLY, not historical verification,
not literary review, and not independent V3 testing.
"""
from __future__ import annotations
import argparse
import json
from collections import defaultdict
from decimal import Decimal, InvalidOperation
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FIXTURE = ROOT / "fixtures" / "chaoxun_ch03.json"
ALLOWED_FACT_STATUS = {"UNKNOWN", "HEARSAY", "REPORTED", "INFERRED", "CONFIRMED"}
REQUIRE_PERMISSION = {"stock.dry", "cash.public"}


class LedgerError(ValueError):
    pass


def need(test, message):
    if not test:
        raise LedgerError(message)


def integer(value, name):
    need(type(value) is int and not isinstance(value, bool), name + " must be integer")
    return value


def validate(data):
    need(isinstance(data, dict), "top-level must be an object")
    need(data.get("schema") == "v13-novel-alpha-ledger-1", "wrong schema")
    need(bool(data.get("project")), "missing project")
    initial = data.get("initial_accounts")
    expected = data.get("expected_balances")
    need(isinstance(initial, dict) and bool(initial), "initial_accounts missing")
    need(isinstance(expected, dict), "expected_balances missing")
    need(set(initial) == set(expected), "expected_balances account keys mismatch")
    for account, amount in initial.items():
        need(account.strip() and "." in account, "invalid account: " + str(account))
        need(integer(amount, "initial." + account) >= 0, "negative initial account " + account)
    balance = dict(initial)

    facts = {}
    for f in data.get("facts", []):
        fid = f.get("fact_id")
        need(bool(fid) and fid not in facts, "duplicate or missing fact id")
        need(f.get("status") in ALLOWED_FACT_STATUS, "invalid fact status: " + str(fid))
        if f["status"] == "CONFIRMED":
            need(bool(f.get("source")), "confirmed fact requires evidence: " + str(fid))
        facts[fid] = dict(f)

    permissions = {}
    for p in data.get("permissions", []):
        pid = p.get("id")
        need(bool(pid) and pid not in permissions, "duplicate permission ID")
        need(p.get("resource_account") in initial, "unknown permission account: " + str(pid))
        integer(p.get("grant_chapter"), "grant_chapter")
        integer(p.get("first_valid_chapter"), "first_valid_chapter")
        integer(p.get("last_valid_chapter"), "last_valid_chapter")
        need(p["grant_chapter"] <= p["first_valid_chapter"] <= p["last_valid_chapter"],
             "permission effective before grant or reversed time: " + str(pid))
        need(integer(p.get("max_debit"), "max_debit") >= 0, "permission max_debit <0")
        need(bool(p.get("issuer") and p.get("grant_event_id")),
             "permission missing issuer/grant event: " + str(pid))
        permissions[pid] = p

    used = defaultdict(int)
    seen = {}
    previous_chapter = 0
    for event in data.get("events", []):
        eid = event.get("id")
        need(bool(eid) and eid not in seen, "duplicate event ID: " + str(eid))
        chapter = integer(event.get("chapter"), "event.chapter")
        need(chapter >= previous_chapter and chapter >= 1, "event chapter order regressed")
        previous_chapter = chapter
        need(bool(event.get("evidence_ref")), "event has no observable source: " + str(eid))
        seen[eid] = event

        # A permission ID never silently disappears from an otherwise unprotected event.
        ids = event.get("permission_ids", [])
        need(isinstance(ids, list) and len(ids) == len(set(ids)),
             "invalid or duplicate permission IDs: " + str(eid))
        need(all(pid in permissions for pid in ids),
             "unknown permission ID: " + str(eid))

        for item in event.get("changes", []):
            account = item.get("account")
            need(account in balance, "untracked account: " + str(account))
            delta = integer(item.get("delta"), "change.delta")
            if account in REQUIRE_PERMISSION and delta < 0:
                matching = [permissions[p] for p in event.get("permission_ids", [])
                            if p in permissions and permissions[p]["resource_account"] == account]
                need(len(matching) == 1, "debit without exactly one suitable permission: " + str(eid))
                permit = matching[0]
                need(permit["grant_event_id"] in seen and permit["grant_event_id"] != eid,
                     "permission grant not observed before action: " + str(eid))
                need(permit["first_valid_chapter"] <= chapter <= permit["last_valid_chapter"],
                     "permission outside valid time: " + str(eid))
                used[permit["id"]] += -delta
                need(used[permit["id"]] <= permit["max_debit"],
                     "debit exceeds permission capacity: " + str(eid))
            if account == "stock.promised_not_arrived" and delta < 0:
                need(event.get("kind") == "RECEIPT" and
                     bool(event.get("receipt_evidence_ref")),
                     "cannot turn promised goods into physical stock without witnessed receipt: " + str(eid))
            balance[account] += delta
            need(balance[account] >= 0, "negative balance " + account + " at " + str(eid))

        # Receiving an old promise requires an equal physical-stock credit.
        # A paper receipt alone cannot evaporate a promise or double the inventory.
        promise_debit = -sum(c["delta"] for c in event.get("changes", [])
                             if c.get("account") == "stock.promised_not_arrived"
                             and c.get("delta", 0) < 0)
        if promise_debit:
            physical_credit = sum(c["delta"] for c in event.get("changes", [])
                                  if c.get("account") in {"stock.dry", "stock.wet"}
                                  and c.get("delta", 0) > 0)
            need(physical_credit == promise_debit,
                 "receipt transfer must conserve physical stock: " + str(eid))

        if any(x.get("account") == "debt.wages" and x.get("delta", 0) < 0
               for x in event.get("changes", [])):
            wage = sum(-x["delta"] for x in event["changes"]
                       if x.get("account") == "debt.wages")
            cash = sum(-x["delta"] for x in event["changes"]
                       if x.get("account") == "cash.public" and x.get("delta", 0) < 0)
            need(wage == cash, "wage debt cannot disappear without corresponding cash payment: " + str(eid))

        for change in event.get("facts_updates", []):
            fid = change.get("fact_id")
            need(fid in facts, "update of unknown fact: " + str(fid))
            next_status = change.get("status")
            need(next_status in ALLOWED_FACT_STATUS, "invalid status update: " + str(eid))
            if next_status == "CONFIRMED" and facts[fid]["status"] != "CONFIRMED":
                need(bool(change.get("proof_ref")) and
                     change.get("proof_type") in {"WITNESSED", "DOCUMENT_VERIFIED"},
                     "rumor promoted to confirmed without explicit verifiable evidence: " + str(fid))
            facts[fid]["status"] = next_status
            if next_status == "CONFIRMED":
                facts[fid]["source"] = change.get("proof_ref") or facts[fid].get("source")

    for pid, p in permissions.items():
        need(p["grant_event_id"] in seen, "dangling permission grant event: " + pid)
        need(seen[p["grant_event_id"]].get("kind") == "PERMISSION_GRANTED",
             "permission grant event is not an authorization: " + pid)
        need(seen[p["grant_event_id"]]["chapter"] == p["grant_chapter"],
             "permission chapter does not match grant event: " + pid)

    for account, target in expected.items():
        need(integer(target, "expected." + account) == balance[account],
             "expected balance differs for " + account +
             ": expected " + str(target) + ", actual " + str(balance[account]))

    need(data.get("independent_review") in {"NOT_RUN", "DIAGNOSTIC_ONLY", "INDEPENDENT_DOCUMENTED"},
         "invalid review status")
    for person in data.get("characters", []):
        need(person.get("name") and isinstance(person.get("knows"), list) and
             isinstance(person.get("heard"), list), "character lacks knowledge partitions")
    need(isinstance(data.get("open_loops"), list), "missing open loops")
    return {"project": data["project"], "events": len(seen),
            "balances": balance, "facts": {k: x["status"] for k, x in facts.items()},
            "independent_review": data["independent_review"]}


def main():
    a = argparse.ArgumentParser(description="Check V13 alpha state constraints")
    a.add_argument("state", nargs="?", default=str(FIXTURE),
                   help="JSON event state (default: original sandbox example)")
    args = a.parse_args()
    try:
        result = validate(json.loads(Path(args.state).read_text(encoding="utf-8")))
    except (LedgerError, json.JSONDecodeError, OSError) as e:
        print("FAIL STATE:", e)
        raise SystemExit(1)
    print(json.dumps({"status": "STRUCTURE_ONLY_PASS", **result}, ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
