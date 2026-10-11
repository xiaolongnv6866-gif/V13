#!/usr/bin/env python3
"""N19 Cangjie Stage1.5 V2 new-input walkthrough completeness check.
This is a STRUCTURAL TEST; it does not prove prose quality or independent V3.
"""
from __future__ import annotations
import csv
import hashlib
import re
from collections import Counter
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
PREFIX = ROOT / "v13_3/n19"
SRC = ROOT / "v13_3/n17/N17_WM_V1_91.tsv"
PREG_COMMIT = "4f1d6e6f07bc3276671f322b7a9a5b27e5b4ba02"
FROZEN = {
  "N19_WM_V2_PREREG_32.tsv":"4243c0914369509e861617f4d2b449402c6a627d",
  "N19_V2_PREREG_CONTRACT.md":"78adf4d00e6be1c258f639adc3046321e9c58c99",
  "N19_SYNTHETIC_WORLD_FACTS.md":"45d2b1e0ac62da5dbb93b67f0d9def16dc072b6b",
}
def blob(text):
    b=text.encode("utf-8")
    return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()
for name,expected in FROZEN.items():
    actual=blob((PREFIX/name).read_text(encoding="utf-8"))
    assert actual==expected,("PRE-REGISTRATION CHANGED AFTER WRITING OUTPUT",name,actual)
def get(name):
    with (ROOT/name).open(encoding="utf-8",newline="") as fh:
        return list(csv.DictReader(fh,delimiter="\t"))
v1=get("v13_3/n17/N17_WM_V1_91.tsv")
qualified={row["candidate_id"] for row in v1 if row["V1_source_decision"]=="V1_SOURCE_SUPPORTED_SCOPED_V2_PENDING"}
assert len(qualified)==32
preregistered=get("v13_3/n19/N19_WM_V2_PREREG_32.tsv")
outputs=get("v13_3/n19/N19_WM_V2_RESULTS_32.tsv")
negative=get("v13_3/n19/N19_V2_ABLATION_32.tsv")
for arr in (preregistered,outputs,negative):
    ids=[x["candidate_id"] for x in arr]
    assert len(ids)==len(set(ids))==32 and set(ids)==qualified
prmap={x["candidate_id"]:x for x in preregistered}
resmap={x["candidate_id"]:x for x in outputs}
negmap={x["candidate_id"]:x for x in negative}
assert all(x["evaluation_scope"]=="STAGE1_5_V2_WALKTHROUGH_ONLY" for x in preregistered)
assert all("STAGE1_5" not in x["new_input_pre_registered"] for x in preregistered)
assert all(len(x["new_input_pre_registered"])>=30 and len(x["mandatory_verifiable_observation"])>=14 and len(x["forbidden_inference_or_failure"])>=14 for x in preregistered)
counts=Counter(x["V2_outcome"] for x in outputs)
assert counts=={"V2_WALKTHROUGH_PASS_SCOPED":28,"V2_PARTIAL_NEEDS_FOLLOWUP":4},counts
partial={x["candidate_id"] for x in outputs if x["V2_outcome"]=="V2_PARTIAL_NEEDS_FOLLOWUP"}
assert partial=={"f03","f05","f10","f17"}
used=set()
for letter in "ABCD":
    p=f"v13_3/n19/N19_V2_OUTPUTS_{letter}.md"
    txt=(ROOT/p).read_text(encoding="utf-8")
    assert PREG_COMMIT in txt,(letter,"prereg SHA")
    blocks=re.split(r"(?m)^## (f\d{2}|p\d{2})\s*$",txt)
    assert (len(blocks)-1)//2==8,(letter,len(blocks))
    for i in range(1,len(blocks),2):
        cid=blocks[i];section=blocks[i+1]
        assert cid not in used,cid
        used.add(cid)
        row=resmap[cid]
        assert row["frozen_prereg_commit"]==PREG_COMMIT
        assert row["source_V1"]=="V1_SOURCE_SUPPORTED_SCOPED_V2_PENDING"
        assert row["output_file"]==p
        assert row["scene_section"]=="## "+cid
        for col in ("walkthrough_steps_executed","original_scene_written","state_change_recorded","missing_input_branch_executed"):
            assert row[col].startswith("YES"),(cid,col)
        assert row["independent_V3_evidence"]=="NOT_RUN" and row["actual_host_Stage4_evidence"]=="NOT_RUN"
        assert row["method_verified_status"]=="NO_PROMOTION"
        for part in ("**操作步骤**：","**原创场景输出**：","**结果/前后状态账**：","**缺输入回退/边界负例**：","**V2执行初判**："):
            assert part in section,(cid,part)
        scene=re.search(r"\*\*原创场景输出\*\*：\s*\n> (.+?)\n\n",section,re.S)
        assert scene and len(scene.group(1))>=120,(cid,"scene not actual")
        assert row["V2_outcome"]=="V2_WALKTHROUGH_PASS_SCOPED" or row["V2_outcome"]=="V2_PARTIAL_NEEDS_FOLLOWUP"
        if row["V2_outcome"]=="V2_PARTIAL_NEEDS_FOLLOWUP":
            assert len(row["reason_for_limit_or_success"])>=33
        neg=negmap[cid]
        assert neg["branch_result"]=="STOP_WITH_BOUNDARY_NO_INVENTED_FACT"
        assert len(neg["ablation_input_without_crucial_fact"])>=14
        assert len(neg["actual_stop_or_refusal_output"])>=23
assert used==qualified
import json
s=json.loads((ROOT/"V13_CURRENT_V4.json").read_text(encoding="utf-8"))
assert s["completed_new_rounds"]>=18
if s["completed_new_rounds"]==18: assert s["current_round"]=="N19"
else: assert get("V13_LEDGER_V4.tsv")[18]["status"]=="PASSED"
if s["completed_new_rounds"]<28:
    assert (s["verified"],s["reference"],s["needs_review"],s["rejected"])==(0,108,79,0)
    assert s["v13_3_R042_quarantines_still_not_promoted"]==14
if s["completed_new_rounds"]<37: assert s["certified_skills"]==0
assert (PREFIX/"N19_V2_SOURCE_AND_QUALITY_AUDIT.md").is_file()
print("PASS N19 32 preregistered/new creative walkthroughs + 32 concrete ablation refusals: scoped V2 pass28, partial4. NO independent V3 or novel SKILL certification.")
