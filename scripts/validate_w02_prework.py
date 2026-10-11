#!/usr/bin/env python3
"""W02 public/preregistered original-fiction prework, STRUCTURE ONLY.

Never treat this script as an independent literary C assessment.
"""
from pathlib import Path
import csv
import hashlib

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/"v13_w/w02/prework_20261012"
LOCKED={
"FROZEN_WM_TX_01_CONTRACT.md":"4e151ba33f75b7e9fcb80118b8bd975eb5aaa47b",
"FROZEN_WM02_WM03_TX02_TX03.md":"067c35d7e8199086af25eb55cc2fc027a945a590"
}
def blob_sha(p):
    b=p.read_bytes()
    return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()
for name,sha in LOCKED.items():
    assert blob_sha(BASE/name)==sha, f"Unfrozen or modified preregistration: {name}"

with (ROOT/"V13_3_STAGE0_20_TO_ROUNDS.tsv").open(encoding="utf-8") as f:
    tasks={v["old_task_id"]:v for v in csv.DictReader(f,delimiter="\t")}
assert len(tasks)==20
checks={
"WM-T01":("WM_T01_3_SCENES.md",3,["田栀","彭槐","孟济","候补工","状态差值"]),
"TX-T01":("TX_T01_3_SCENES.md",3,["黄述","赵姑","范四","林末","四方关系"]),
"WM-T02":("WM_T02_3_SCENES.md",3,["白荷","周椿","八根","六根","两根","双视角"]),
"WM-T03":("WM_T03_FIVE_LEDGERS.md",3,["温绍","祝闻舟","五账","八两","四人","两人"]),
"TX-T02":("TX_T02_APPLICATION_STATES.md",2,["蔡宁","何顺","宁振","五状态","授权","追责"]),
"TX-T03":("TX_T03_AUTONOMOUS_STAFF.md",2,["叶监","陈豆","庄嫂","职责依赖图","西滩","东棚"])
}
with (BASE/"W02_PREWORK_STATUS.tsv").open(encoding="utf-8") as f:
    rows={v["task_id"]:v for v in csv.DictReader(f,delimiter="\t")}
assert len(rows)==6 and set(rows)==set(checks)
for task,(name,n,words) in checks.items():
    assert tasks[task]["truly_independent_C"]=="NOT_RUN"
    body=(BASE/name).read_text(encoding="utf-8")
    assert sum("\u4e00"<=c<="\u9fff" for c in body)>=1700,(task,"short output")
    for i in range(1,n+1):
        mark="## "+["第一场","第二场","第三场"][i-1]
        assert body.count(mark)==1,(task,mark)
    for w in words: assert w in body,(task,w)
    assert "DIAGNOSTIC_ONLY" in body
    assert "独立C创作/评审均未执行" in body
    row=rows[task]
    assert row["output_file"]==name
    assert row["status"]=="WRITTEN_DIAGNOSTIC_ONLY"
    assert row["independent_creator"]=="NOT_RUN"
    assert row["independent_judges"]=="NOT_RUN"
    assert row["official_w02_status"]=="NOT_STARTED"
    required_commit="60d503feb8697433557c1287c97e42d0d4509324" if task.endswith("01") else "1e040f9dfb88bcc08922bbdc89f69e84dacb42d8"
    assert row["input_commit"]==required_commit
cur=(ROOT/"V13_W_CURRENT_V5.json").read_text(encoding="utf-8")
assert '"current_package": "W01"' in cur
assert '"current_package_status": "BLOCKED"' in cur
assert '"completed_packages": 0' in cur
print("STRUCTURE_ONLY_PASS: 6/20 frozen prework outputs; 0/20 independent C. W01 BLOCKED, 0/11 packages.")
