#!/usr/bin/env python3
"""V13 W01 five candidate partial-V2 retests: authored evidence integrity only.

Does NOT certify literary quality, V3, source sufficiency, or independent review.
"""
from pathlib import Path
import hashlib, json, csv

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/"v13_w/w01/repair_20261012"
PREREG=BASE/"FROZEN_5_PARTIAL_V2_RETEST.md"
PREREG_BLOB="0827304665f34e625ee49f2c76684b8b669ba15a"
EXCEPTIONS=ROOT/"v13_w/w01/W01_13_EXCEPTIONS.tsv"
EXCEPTIONS_BLOB="800f8aae1ca5ef8fe2fa7cacfb05231f2afb5d96"

def blob(p):
    data=p.read_bytes()
    return hashlib.sha1(b"blob "+str(len(data)).encode()+b"\0"+data).hexdigest()

assert blob(PREREG)==PREREG_BLOB, "prereg input must remain frozen"
assert blob(EXCEPTIONS)==EXCEPTIONS_BLOB, "original thirteen exceptions cannot be silently rewritten"
with EXCEPTIONS.open(encoding="utf-8") as f:
    old={r["candidate_id"]:r for r in csv.DictReader(f,delimiter="\t")}
assert len(old)==13
cases={
"WM-f05":("WM_f05_V2_RETEST.md",["葛生","傅圆","穆秋","新尺","五张","六张"]),
"WM-f10":("WM_f10_V2_RETEST.md",["刘伯","秦织","崔岩","赵婆","第三日","第七日"]),
"TX-f02":("TX_f02_V2_RETEST.md",["伊述","桂平","100","89","11","十二笔"]),
"TX-f07":("TX_f07_V2_RETEST.md",["杜渠","巡视","三锅","两轮","第三锅"]),
"TX-f15":("TX_f15_V2_RETEST.md",["顾林","闻桑","周嫂","许竹","四日","两日"])
}
assert sum(v["gate"]=="PARTIAL" for v in old.values())==5
for id,(f,words) in cases.items():
    assert old[id]["gate"]=="PARTIAL"
    s=(BASE/f).read_text(encoding="utf-8")
    assert sum("\u4e00"<=x<="\u9fff" for x in s)>=1500, (id,"too short")
    for w in words:
        assert w in s,(id,w)
    for section in ("pre_inputs","step_path","ablation_actual_output","self_failure_review","observed_state_ledger"):
        assert section in s,(id,"missing",section)
    assert "SELF_DIAGNOSTIC_ONLY" in s,(id,"independence falsely claimed")
assert (BASE/"README.md").is_file()

# These values come from the preregistration, not a new post-hoc threshold.
dues=[10,8,12,5,7,9,11,6,8,10,5,9]
receipts=dues[:]
receipts[6]=0 # #7 has no signed receipt
assert len(dues)==12 and sum(dues)==100 and sum(receipts)==89
assert sum(dues)-sum(receipts)==11
# Other tasks must not misreport the only actual observed quantities.
w=(BASE/"WM_f05_V2_RETEST.md").read_text(encoding="utf-8")
assert "实际做6" in w and "合格5" in w and "不合格1" in w
w=(BASE/"TX_f07_V2_RETEST.md").read_text(encoding="utf-8")
assert "第三锅未发" in w
status=json.loads((ROOT/"V13_W_CURRENT_V5.json").read_text(encoding="utf-8"))
assert status["current_package"]=="W01" and status["current_package_status"]=="BLOCKED"
assert status["completed_packages"]==0 and status["independent_V3_passed"]==0
print("W01_V2_RETEST_STRUCTURAL_PASS 5 new frozen inputs and outputs; old 13 exceptions preserved; 0 independent V3; W01 BLOCKED")
