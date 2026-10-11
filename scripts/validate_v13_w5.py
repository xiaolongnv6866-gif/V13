#!/usr/bin/env python3
"""V13 approved W5 11-package governance. STRUCTURE ONLY, not literary or blind-review certification."""
from pathlib import Path
import csv, json, hashlib, re
from collections import Counter
P=Path(__file__).resolve().parents[1]
def read(p): return (P/p).read_text(encoding="utf-8")
def ts(p): return list(csv.DictReader(read(p).splitlines(),delimiter="\t"))
def blob(s):
    b=s.encode("utf-8")
    return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()
s=json.loads(read("V13_W_CURRENT_V5.json"))
l=json.loads(read("V13_W_GOVERNANCE_LOCK.json"))
old=json.loads(read("V13_CURRENT_V4.json"))
old_lock=json.loads(read("V13_3_GOVERNANCE_LOCK.json"))
assert l["new_plan_blob_sha"]==blob(read("V13_APPROVED_11_WORKPACKAGES.md")), "W plan changed without new approval"
assert l["legacy_plan_blob_sha"]==blob(read("V13_3_FIXED_48_ROUNDS.md"))==old_lock["frozen_plan_git_blob_sha"]
assert s["schema"]=="V13-W-V5" and s["total_packages"]==11 and s["legacy_v4_read_only"]
assert old["completed_new_rounds"]==20 and old["current_round"]=="N21" and old["current_round_status"]=="NOT_STARTED"
assert s["legacy_rounds_passed"]==20 and s["legacy_rounds_total"]==48
assert s["pinned_cangjie"]==old["pinned_cangjie"]==l["original_skill_pins"]["cangjie"]
assert s["pinned_nuwa"]==old["pinned_nuwa"]==l["original_skill_pins"]["nuwa"]
assert s["wanming_sha256"]==old["original_user_source_WM_SHA256"]==l["original_epub_sha256"]["wanming"]
assert s["tiexue_sha256"]==old["original_user_source_TX_SHA256"]==l["original_epub_sha256"]["tiexuecanming"]
assert (s["original_issues"],s["old_methods"],s["old_V3"],s["old_C"],s["old_contracts"],s["quarantined_R042"])==(426,187,69,20,44,14)
assert s["extra_paid_approved"] is False
ledger=ts("V13_W_LEDGER_V5.tsv")
assert len(ledger)==11 and [x["work_package"] for x in ledger]==[f"W{i:02d}" for i in range(1,12)]
done=s["completed_packages"]
assert isinstance(done,int) and 0<=done<=11
assert all(x["status"]=="PASSED" for x in ledger[:done])
assert all(x["status"]=="NOT_STARTED" for x in ledger[done+1:])
if done<11:
    assert ledger[done]["status"] in {"NOT_STARTED","IN_PROGRESS","BLOCKED","FAILED"}
    assert (s["current_package"],s["current_package_status"])==(ledger[done]["work_package"],ledger[done]["status"])
else: assert (s["current_package"],s["current_package_status"])==("W11","PASSED")
legacy=ts("V13_LEDGER_V4.tsv")
assert len(legacy)==48 and all(x["status"]=="PASSED" for x in legacy[:20])
assert all(x["status"]=="NOT_STARTED" for x in legacy[20:])
m=ts("V13_W_MIGRATION_MAP_V5.tsv")
assert len(m)==28 and len({x["old_round"] for x in m})==28
assert {x["old_round"] for x in m}=={f"N{i:02d}" for i in range(21,49)}
groups={x["work_package"]:x for x in ledger}
for row in m:
    assert row["old_status"]=="NOT_STARTED"
    assert row["old_round"] in groups[row["work_package"]]["original_n_rounds"].split(";")
for p in ledger:
    expected={x["old_round"] for x in m if x["work_package"]==p["work_package"]}
    assert expected==set(p["original_n_rounds"].split(";")),p["work_package"]
contracts=ts("V13_3_ORIGINAL_44_CONTRACTS_MAP.tsv")
assert len(contracts)==44
seen=set()
for c in contracts:
    owners={x["work_package"] for x in m if x["old_round"] in c["new_rounds"].split(";")}
    assert len(owners)>=1,c["original_contract"]
    for w in owners:
        assert c["original_contract"] in groups[w]["original_r_contracts"].split(";")
    seen.add(c["original_contract"])
assert len(seen)==44
for p in ledger:
    assert all(c in seen for c in p["original_r_contracts"].split(";"))
checks={"W02":"N28 Stage1.5","W06":"N37 Stage5","W07":"N41 Phase1.5","W08":"N42 Phase2.5","W09":"N44 Phase4","W10":"N45 Phase5","W11":"N48 Final"}
assert l["original_user_gates"]==checks
for w,gate in checks.items():
    assert groups[w]["user_gate"]=="MANDATORY_USER_CONFIRM" and groups[w]["user_confirmation"]
    if groups[w]["status"]=="PASSED": assert groups[w]["user_confirmation"] not in ("PENDING","NOT_APPLICABLE")
for i in range(done):
    p=ledger[i]["work_package"];receipt=read("runs/"+p+"_V5.md")
    assert re.search(r"(?m)^package:\s*"+p+r"\s*$",receipt)
    assert re.search(r"(?m)^status:\s*PASSED\s*$",receipt)
if s["certified_skill"]:
    assert done==11 and s["current_package_status"]=="PASSED"
assert len(ts("V13_3_CANDIDATES_187_TO_ROUNDS.tsv"))==187
assert len(ts("V13_3_STAGE0_20_TO_ROUNDS.tsv"))==20
assert len(ts("V13_3_V3_69_TO_ROUNDS.tsv"))==69
assert len(ts("V13_3_FULL_SKILL_REQUIREMENTS.tsv"))==35
assert len(ts("V13_3_ISSUES_426_TO_ROUNDS.tsv"))==426
pre=ts("v13_w/w01/V3_69_ELIGIBILITY_PREFLIGHT.tsv")
assert len(pre)==69 and Counter(x["preliminary_gate"] for x in pre)=={"READY":56,"PARTIAL":5,"INELIGIBLE":8}
v3=ts("V13_3_V3_69_TO_ROUNDS.tsv")
assert {x["repeat_id"] for x in pre}=={x["repeat_id"] for x in v3}
for x in pre:
    assert x["independent_result"]=="NOT_RUN" and x["creator"]=="UNASSIGNED"
    assert x["blind_judge_one"]=="UNASSIGNED" and x["blind_judge_two"]=="UNASSIGNED"
for x in v3:
    if x["actual_independent_result"]!="NOT_RUN":
        assert all(x[k]!="UNASSIGNED" and x[k] for k in ("creator","blind_judge_one","blind_judge_two"))
for name in ("README.md","START_HERE.md","NEXT_ACTION.md","PROGRESS.md","ROUND_EXECUTION_RULES.md","NEW_CHAT_START.md"):
    assert "V13_W_CURRENT_V5.json" in read(name),name
print("PASS W5 GOVERNANCE (STRUCTURE ONLY): 11 packages, 28 legacy N, 44 contracts, 35 duties, 69 preflight; completed",done)
