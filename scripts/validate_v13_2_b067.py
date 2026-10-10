#!/usr/bin/env python3
"""V13.2 B067 preregistration structural gate; NOT literary-quality certification."""
from __future__ import annotations
import csv
import hashlib
import json
from collections import Counter
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
def j(p): return json.loads((ROOT/p).read_text(encoding="utf-8"))
def tsv(p): return list(csv.DictReader((ROOT/p).open(encoding="utf-8",newline=""),delimiter="\t"))
def assert_ok(test,message):
    if not test: raise AssertionError(message)

d=j("v2/v3/FROZEN_TEST_CONTRACT.json")
a=tsv("v2/v3/V3_TASK_ALLOCATIONS.tsv")
hist=tsv("V13_V3_47_METHOD_ALLOCATION_V3.tsv")
extra=tsv("v2/v3/ADDITIONAL_V2_22_ROUTE.tsv")
state=j("V13_CURRENT_V3.json")
v2=j("V13_CURRENT_V2.json")
cases=d["cases"]
expected={"B068":11,"B069":10,"B070":9,"B071":9,"B072":8}
assert_ok(len(cases)==len(a)==len(hist)==47,"47 total exact")
assert_ok(len({x["candidate_id"] for x in cases})==47,"duplicates in tests")
assert_ok(set(x["candidate_id"] for x in cases)==set(x["candidate_id"] for x in hist)==set(x["candidate_id"] for x in a),"original IDs must match")
assert_ok(Counter(x["allocated_batch"] for x in cases)==expected,"11+10+9+9+8")
assert_ok(Counter(x["book"] for x in cases)=={"wanming":21,"tiexuecanming":26},"WM21 TX26")
assert_ok(len(extra)==len({x["candidate_id"] for x in extra})==22,"22 exact extra")
assert_ok(Counter(x["route_batch"] for x in extra)=={"B073":10,"B074":12},"10+12 extras")
assert_ok(set(x["candidate_id"] for x in extra).isdisjoint(x["candidate_id"] for x in cases),"additional must be separate")
assert_ok(d["preregistered_not_results"] and 0 <= state["v3_original_47_completed"] <= 47,"frozen V3 prereg preserved with bounded progress")
assert_ok(state["current_batch"] in tuple(f'B{i:03d}' for i in range(67,97)),"V13.2 execution batch valid")
assert_ok(66 <= state["overall_management_units_completed"] <= 96,"administrative range valid")
assert_ok(v2["rounds_completed"]==66,"historical 66 unchanged")
for x in cases:
    id=x["candidate_id"]
    assert_ok(x["prior_evidence"]["v1_status"]=="PASS" and x["prior_evidence"]["v2_status"]=="V2_WALKTHROUGH_PASS_LIMITED",id+" origin")
    assert_ok(x["source_epub_sha256"] in (
        "a8f3b43dcd496822cd384ac8e9aa85f7dc374f8430f06c6f8321c26825093082",
        "9100bbcdb9f52bcd5458cbda92e16b646489efbc00df5161ed568ebac83ffbaf"),id+" source hash")
    assert_ok(len(x["source_paragraph_sha256"])==64,id+" paragraph sha")
    assert_ok(len(x["test_input"]["situation"])>=18 and len(x["test_input"]["fixed_facts"])>=18,id+" genuine fixed scenario")
    assert_ok(len(x["method_card"]["steps"])>=3 and x["method_card"]["single_candidate_only"],id+" isolated method")
    assert_ok(x["arm_parity"]["baseline"].startswith("仅收到test_input") and "baseline全部同一材料" in x["arm_parity"]["method"],id+" matched parity")
    assert_ok(len(x["scoring"]["shared_rubric"])==5 and len(x["scoring"]["specialized_checks"])==2,id+" rubric")
    assert_ok(x["evaluation"]["outcome"]=="NOT_TESTED" and x["evaluation"]["arm_outputs"]=="NOT_CREATED",id+" no future outputs")
    assert_ok(x["evaluation"]["independent_judge_available"]=="NOT_ESTABLISHED",id+" no fake judges")
    assert_ok(x["test_id"] and x["candidate_title"] and x["hypothesis"],id+" test completeness")
if state["current_batch"] == "B067":
    assert_ok(not (ROOT/"v2/v3/outputs").exists() and not (ROOT/"v2/v3/results").exists(),"only B067 pre-registration phase requires no V3 outputs")
print("B067 PREREG INVARIANTS PASS: frozen 47/47 contracts, WM21 TX26, 11+10+9+9+8, extras22. Rolling V3 outputs are checked by their own batch workflows; this is not literary certification.")
