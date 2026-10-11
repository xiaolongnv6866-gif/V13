#!/usr/bin/env python3
"""V13.3 N20: source-to-output integrity for 32 Cangjie Stage1.5 V2 walkthroughs.
STRUCTURAL audit only. Does NOT evaluate literary quality or independent V3 gain.
"""
from __future__ import annotations
import csv, hashlib, re, json
from collections import Counter
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
DIR=ROOT/"v13_3/n20"
PREREG_SHA="937a9dbe240ad12e6e56ccdeb56ea5e7747bf6c7"
FROZEN={
 "N20_TX_V2_PREREG_32.tsv":"fb71bc50ba59d90270f0b4e71aadb9d34439fa8c",
 "N20_V2_PREREG_CONTRACT.md":"17d110898f53cc512c3103721b0fad7ce5066c20",
}
def blob(path:Path)->str:
 b=path.read_bytes()
 return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()
for fname,ref in FROZEN.items():
 assert blob(DIR/fname)==ref, ("FROZEN_PRE_REGISTRATION_CHANGED",fname)
def read_tsv(p:Path):
 with p.open(encoding="utf-8",newline="") as f: return list(csv.DictReader(f,delimiter="\t"))
v1=read_tsv(ROOT/"v13_3/n18/N18_TX_V1_96.tsv")
qualified=[x for x in v1 if x["V1_decision"]=="V1_SOURCE_SUPPORTED_SCOPED_V2_PENDING"]
assert len(qualified)==32 and len({r["candidate_id"] for r in qualified})==32
ids=[x["candidate_id"] for x in qualified]
pr=read_tsv(DIR/"N20_TX_V2_PREREG_32.tsv")
results=read_tsv(DIR/"N20_TX_V2_RESULTS_32.tsv")
ablate=read_tsv(DIR/"N20_V2_ABLATION_32.tsv")
for label,arr in (("prereg",pr),("results",results),("ablation",ablate)):
 assert len(arr)==32,(label,len(arr))
 assert [x["candidate_id"] for x in arr]==ids,(label,"missing/reordered ids")
for i,item in enumerate(pr):
 assert item["evaluation_status"]=="CANGJIE_STAGE1_5_V2_ONLY"
 assert all(item[x] for x in ("task_frozen","must_observe","disqualifying_overreach","missing_input_stop","required_delivery"))
 assert item["task_frozen"]!=v1[i]["title"],(item["candidate_id"],"new input was not independently written")
counts=Counter(r["v2_outcome"] for r in results)
assert counts=={"V2_WALKTHROUGH_PASS_SCOPED":29,"V2_PARTIAL_NEEDS_FOLLOWUP":3},counts
assert {r["candidate_id"] for r in results if r["v2_outcome"]=="V2_PARTIAL_NEEDS_FOLLOWUP"}=={"f02","f07","f15"}
used=set()
for letter in "ABCD":
 fn=f"v13_3/n20/N20_V2_OUTPUTS_{letter}.md"
 txt=(ROOT/fn).read_text(encoding="utf-8")
 assert PREREG_SHA in txt,(letter,"missing freeze link")
 chunks=re.split(r"(?m)^## ([fp]\d{2})\s*$",txt)
 assert (len(chunks)-1)//2==8,(letter,"8 blocks required")
 for i in range(1,len(chunks),2):
  cid=chunks[i];s=chunks[i+1]
  assert cid not in used;used.add(cid)
  rr=next(x for x in results if x["candidate_id"]==cid)
  src=next(x for x in qualified if x["candidate_id"]==cid)
  assert rr["frozen_prereg_commit"]==PREREG_SHA
  assert rr["source_v1"]==src["V1_decision"]
  assert rr["source_first_locus"]==src["source_first_locus"]
  assert rr["original_chapter"]==src["source_epub_path"]
  assert rr["chapter_sha256"]==src["chapter_sha256"]
  assert rr["source_paragraph_sha256"]==src["paragraph_sha256"]
  assert rr["actual_output_file"]==fn and rr["actual_output_section"]=="## "+cid
  assert all(rr[k]=="YES" for k in ("steps_executed","original_scene_written","state_change_recorded","missing_input_ablation_output","self_review_recorded"))
  assert rr["genuine_independent_v3"]=="NOT_RUN"
  assert rr["stage4_real_host_test"]=="NOT_RUN"
  assert rr["method_verified_or_promoted"]=="NO_PROMOTION"
  assert rr["v2_outcome"] in s,(cid,"outcome not in original scene")
  assert re.search(r"(?m)^\*\*(?:识别与操作分支|输入.*操作|输入.*分支|操作步骤|输入识别.*)\*\*：",s) or ("**步骤" in s),cid
  found=re.search(r"\*\*原创现场(?:演练|场景|输出)\*\*：\s*(.*?)\n\n\*\*",s,re.S)
  assert found and len(found.group(1).strip())>=90,(cid,"actual scene missing")
  assert "状态" in s and "自审" in s or "自我审查" in s
  assert re.search(r"(?m)^\*\*.*(?:答复|回退)\*\*：",s),(cid,"ablation branch missing")
assert used==set(ids)
for r in ablate:
 cid=r["candidate_id"]
 assert r["preregistered_commit"]==PREREG_SHA
 assert r["branch_result"]=="STOP_WITH_BOUNDARY_NO_INVENTED_FACT"
 assert len(r["actual_removed_fact_input"])>=5
 assert len(r["actual_stop_or_refusal_output"])>=10
 assert r["output_section"]=="## "+cid
assert (DIR/"N20_V2_SOURCE_AND_QUALITY_AUDIT.md").is_file()
state=json.loads((ROOT/"V13_CURRENT_V4.json").read_text(encoding="utf-8"))
ledger=read_tsv(ROOT/"V13_LEDGER_V4.tsv")
row=next(x for x in ledger if x["round_id"]=="N20")
if state["completed_new_rounds"]==19:
 assert state["current_round"]=="N20" and row["status"] in ("NOT_STARTED","IN_PROGRESS")
elif state["completed_new_rounds"]==20:
 assert state["current_round"]=="N21" and row["status"]=="PASSED"
else:
 raise AssertionError("unexpected V13 N20 status")
assert (state["verified"],state["reference"],state["needs_review"],state["rejected"])==(0,108,79,0)
assert state["certified_skills"]==0
assert state["v13_3_R042_quarantines_still_not_promoted"]==14
print("PASS N20: 32 frozen/source-qualified IDs, original scenes, state ledgers, ablation outputs, 29 limited V2 + 3 partial. V3/Stage4/Skill certification NOT RUN.")
