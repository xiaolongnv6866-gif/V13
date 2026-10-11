#!/usr/bin/env python3
"""Check W01 public calibration freeze and eligibility; NOT real blind literary evaluation."""
from pathlib import Path
from collections import Counter
import csv,json,hashlib,re
P=Path(__file__).resolve().parents[1]
def read(path):return (P/path).read_text(encoding="utf-8")
def tab(path):return list(csv.DictReader(read(path).splitlines(),delimiter="\t"))
def gitblob(data):
    b=data.encode("utf-8")
    return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()
c=json.loads(read("v13_w/w01/W01_PUBLIC_CALIBRATION_CONTRACT.json"))
assert c["status"]=="INPUT_FROZEN_OUTPUT_NOT_RUN"
assert c["benchmark_generated"]=="NO" and c["actual_outputs"]=="NOT_RUN"
assert c["blind_scores"]=="NOT_RUN" and c["independent_certification"]=="NO"
assert c["public_task_blob"]==gitblob(read(c["public_task_file"]))=="afa17988178de20c9304f0078babb409bf808e6b"
cases=tab(c["public_task_file"])
ex=tab(c["excluded_case_file"])
e=tab("v13_w/w01/V3_69_ELIGIBILITY_PREFLIGHT.tsv")
assert len(cases)==56 and len(ex)==13 and len(e)==69
assert Counter(x["preliminary_gate"] for x in e)=={"READY":56,"PARTIAL":5,"INELIGIBLE":8}
ready={x["repeat_id"]:x for x in e if x["preliminary_gate"]=="READY"}
no={x["repeat_id"]:x for x in e if x["preliminary_gate"]!="READY"}
assert set(x["repeat_id"] for x in cases)==set(ready)
assert set(x["repeat_id"] for x in ex)==set(no)
assert len({x["candidate_id"] for x in cases})==56
assert len({x["new_task_id"] for x in cases})==56
assert len({x["clean_blind_task"] for x in cases})==56
assert all(x["status"]=="PUBLIC_CALIBRATION_FROZEN_BEFORE_ANY_W01_OUTPUT" for x in cases)
assert all("method_card" not in x["clean_blind_task"] and "original" not in x["clean_blind_task"] for x in cases)
assert all(len(x["method_card"])>60 and len(x["measurable_hypothesis"])>12 for x in cases)
assert all("450—650" in x["clean_blind_task"] and "背景：" in x["clean_blind_task"] for x in cases)
assert all(x["allowed_independent_V3_now"]=="NO" for x in ex)
for x in cases:
    z=ready[x["repeat_id"]]
    assert x["candidate_id"]==z["candidate_id"] and x["book"]==z["book"]
for x in ex:
    z=no[x["repeat_id"]]
    assert x["candidate_id"]==z["candidate_id"] and x["gate"]==z["preliminary_gate"]
    assert x["disposition"]==("V2_PARTIAL_NO_V3" if z["preliminary_gate"]=="PARTIAL" else "NO_V1_METHOD_ELIGIBILITY")
assert {x["repeat_id"] for x in cases}.isdisjoint(x["repeat_id"] for x in ex)
assert len(tab("V13_3_V3_69_TO_ROUNDS.tsv"))==69
assert "GitHub Models" in read("v13_w/w01/W01_EVAL_PROTOCOL.md")
print("PASS W01 input-only freeze: 56 distinct public calibration prompts; 5 partial + 8 V1-ineligible excluded; 0 independent V3 claims")
