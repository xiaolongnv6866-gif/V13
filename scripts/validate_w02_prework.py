#!/usr/bin/env python3
"""Check W02 preregistered fiction evidence mechanically, without literary certification."""
from pathlib import Path
import csv
import hashlib
import re

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/"v13_w/w02/prework_20261012"
CONTRACT=BASE/"FROZEN_WM_TX_01_CONTRACT.md"
EXPECTED_CONTRACT_BLOB="4e151ba33f75b7e9fcb80118b8bd975eb5aaa47b"

def git_blob(path):
    data=path.read_bytes()
    return hashlib.sha1(b"blob "+str(len(data)).encode()+b"\0"+data).hexdigest()

assert git_blob(CONTRACT)==EXPECTED_CONTRACT_BLOB,"frozen W02 preregistration unexpectedly changed"
mapping={r["old_task_id"]:r for r in csv.DictReader(
    (ROOT/"V13_3_STAGE0_20_TO_ROUNDS.tsv").read_text(encoding="utf-8").splitlines(),delimiter="\t")}
assert len(mapping)==20
required={"WM-T01":("WM_T01_3_SCENES.md",["田栀","彭槐","孟济","候补工","状态差值"]),
          "TX-T01":("TX_T01_3_SCENES.md",["黄述","赵姑","范四","林末","四方关系"])}
for key,(filename,words) in required.items():
    assert mapping[key]["truly_independent_C"]=="NOT_RUN",key
    body=(BASE/filename).read_text(encoding="utf-8")
    assert sum("\u4e00"<=c<="\u9fff" for c in body)>=1700,key
    for heading in ("## 第一场","## 第二场","## 第三场"):
        assert body.count(heading)==1,(key,heading)
    for word in words: assert word in body,(key,word)
    assert "DIAGNOSTIC_ONLY" in body
    assert "独立C创作/评审均未执行" in body
status=(BASE/"W02_PREWORK_STATUS.tsv").read_text(encoding="utf-8")
entries=list(csv.DictReader(status.splitlines(),delimiter="\t"))
assert len(entries)==2 and set(r["task_id"] for r in entries)==set(required)
for e in entries:
    assert e["status"]=="WRITTEN_DIAGNOSTIC_ONLY"
    assert e["independent_creator"]=="NOT_RUN"
    assert e["independent_judges"]=="NOT_RUN"
print("STRUCTURE_ONLY_PASS: frozen before writing; 2/20 prework texts, 0/20 independent C; W01 BLOCKED and W02 NOT_STARTED")
