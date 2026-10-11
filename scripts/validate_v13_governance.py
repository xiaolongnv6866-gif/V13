#!/usr/bin/env python3
"""Non-literary V13.3 governance guard: frozen plan, source pins, one-round cursor.
This is deterministic administrative defense, NOT V1/V2/V3/novel quality proof.
"""
from __future__ import annotations
import csv
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def read(name):
    return (ROOT / name).read_text(encoding="utf-8")

def table(name):
    return list(csv.DictReader(read(name).splitlines(), delimiter="\t"))

def git_blob_sha(data):
    raw = data.encode("utf-8")
    return hashlib.sha1(b"blob " + str(len(raw)).encode("ascii") + b"\0" + raw).hexdigest()

lock = json.loads(read("V13_3_GOVERNANCE_LOCK.json"))
state = json.loads(read("V13_CURRENT_V4.json"))
led = table("V13_LEDGER_V4.tsv")
assert lock["schema"] == "V13.3_GOVERNANCE_LOCK_1"
assert lock["authoritative_cursor"] == "V13_CURRENT_V4.json"
assert lock["authoritative_ledger"] == "V13_LEDGER_V4.tsv"
assert lock["original_approved_plan"] == "V13_3_FIXED_48_ROUNDS.md"
assert git_blob_sha(read(lock["original_approved_plan"])) == lock["frozen_plan_git_blob_sha"], "FROZEN 48-ROUND PLAN CHANGED WITHOUT RELOCK/APPROVAL"
assert state["version"] == "V13.3" and state["total_new_rounds"] == lock["frozen_counts"]["rounds"] == 48
assert state["plan"] == lock["original_approved_plan"] and state["ledger"] == lock["authoritative_ledger"]
assert state["pinned_cangjie"] == lock["original_skills"]["cangjie"]
assert state["pinned_nuwa"] == lock["original_skills"]["nuwa"]
assert state["original_user_source_WM_SHA256"] == lock["original_private_epub_sha256"]["wanming"]
assert state["original_user_source_TX_SHA256"] == lock["original_private_epub_sha256"]["tiexuecanming"]
for ref in (state["pinned_cangjie"], state["pinned_nuwa"]):
    assert ref in read("V13_CURRENT_V4.json")
for sha in (state["pinned_cangjie"].split("@")[1], state["pinned_nuwa"].split("@")[1]):
    assert sha in read("SKILL_SOURCES.md"), "SKILL_SOURCES has diverged from original pinned SHA"
assert state["original_426_issues"] == lock["frozen_counts"]["original_issues"] == 426
assert state["old_stage0_B_total"] == lock["frozen_counts"]["literary_B"] == 296
assert state["old_R042_quarantined"] == lock["frozen_counts"]["R042_quarantined"] == 14
assert state["historical_75_completed_preserved"] is True
assert state["R057_19_topics_not_equivalent_to_old20"] is True
assert len(led) == 48 and [r["round_id"] for r in led] == [f"N{i:02d}" for i in range(1, 49)]
k = state["completed_new_rounds"]
assert isinstance(k, int) and 0 <= k <= 48
assert all(x["status"] == "PASSED" for x in led[:k])
assert all(x["status"] != "PASSED" for x in led[k:])
assert all(x["status"] == "NOT_STARTED" for x in led[k+1:])
if k < 48:
    assert state["current_round"] == f"N{k+1:02d}"
    assert state["current_round_status"] == led[k]["status"]
    assert state["current_round_status"] in {"NOT_STARTED", "IN_PROGRESS", "BLOCKED", "FAILED"}
else:
    assert all(x["status"] == "PASSED" for x in led)
for i in range(1, k+1):
    receipt = read(f"runs/N{i:02d}_V4.md")
    assert re.search(rf"(?m)^round:\s*N{i:02d}\s*$", receipt)
    assert re.search(r"(?m)^status:\s*PASSED\s*$", receipt)
assert state["v13_3_stage0_B_disposed_this_plan"] <= 296
assert state["v13_3_from_old_192_unreviewed_done"] <= 192
assert 0 <= state["v13_3_R042_quarantines_still_not_promoted"] <= 14
if k < 27:  # Before N28 can be closed, no R042 quarantine release is authorized.
    assert state["v13_3_R042_quarantines_still_not_promoted"] == 14
assert sum(state[x] for x in ("verified", "reference", "needs_review", "rejected")) == lock["frozen_counts"]["method_candidates"] == 187
if k < 21:
    assert state["verified"] == 0, "No verified skill methods before actual independent V3"
if k < 36:
    assert state["certified_skills"] == 0, "No compiled and tested Cangjie skill before Stage5"
assert lock["frozen_counts"]["original_stage0_tasks"] == 20
assert lock["frozen_counts"]["topic_mappings"] == 19
assert len(table("V13_3_STAGE0_20_TO_ROUNDS.tsv")) == 20
assert len(table("V13_3_ORIGINAL_44_CONTRACTS_MAP.tsv")) == 44
assert len(table("V13_3_V3_69_TO_ROUNDS.tsv")) == 69
assert len(table("V13_3_CANDIDATES_187_TO_ROUNDS.tsv")) == 187
for name in ("START_HERE.md", "ROUND_EXECUTION_RULES.md"):
    assert "V13_3_RECOVERY_GUARD.md" in read(name), name
if k == 15:
    assert "N16" in read("NEXT_ACTION.md")
print(f"PASS V13.3 governance (administrative only): fixed plan and original SHA pins; {k}/48; "
      f"cursor={state['current_round']} {state['current_round_status']}; 20 Stage0 tasks; 187 candidates")
