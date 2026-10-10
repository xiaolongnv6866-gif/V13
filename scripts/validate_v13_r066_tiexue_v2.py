#!/usr/bin/env python3
import csv,json,hashlib
from pathlib import Path
P=Path(__file__).resolve().parents[1]
def read(path):
 with (P/path).open(encoding="utf8",newline="") as h:return list(csv.DictReader(h,delimiter="\t"))
b=(P/"v2/v2/TIEXUE_FROZEN_INPUTS.json").read_bytes()
sha=hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()
assert sha=="78308e7acbe4863c76cd09a148727c526aeca795"
tests=json.loads(b)["cases"];rows=read("v2/v2/TIEXUE_RESULTS.tsv")
assert len(tests)==len(rows)==12
old={x["candidate_id"]:x for x in read("gates/R057_REPAIR_V2_11_TEST_DESIGNS.tsv") if x["book"]=="tiexuecanming"}
new={x["candidate_id"]:x for x in read("v2/v1/TIEXUE_16_RESULTS.tsv") if x["R064_V1_result"]=="PASS_NARROW"}
assert len(old)==len(new)==6
for i,(t,r) in enumerate(zip(tests,rows)):
 key=t["candidate_id"]
 assert t["case_id"]==r["case_id"] and key==r["candidate_id"]
 assert t["source_group"]==r["candidate_origin"]==("OLD" if i<6 else "NEW")
 assert key in (old if i<6 else new)
 assert r["V1_precondition"]==("PASS" if i<6 else "PASS_NARROW")
 assert r["frozen_blob_sha"]==sha and r["frozen_commit"]=="36443c18448c1caf89d9fc9d1706b714a09c4716"
 path="v2/v2/results/"+t["case_id"]+".json"
 assert r["result_path"]==path
 o=json.loads((P/path).read_text(encoding="utf8"))
 assert o["id"]==t["case_id"] and o["candidate"]==key
 assert 200<=len(o["scene"])<=390 and int(r["scene_chars"])==len(o["scene"])
 assert len(o["state"])>=3 and int(r["state_rows"])==len(o["state"])
 assert len(t["checks"])==len(o["evidence"])==4
 assert o["phase"]=="V2_PAPER_WALKTHROUGH_NONBLIND" and o["unknowns_preserved"] is True
 for k in range(1,5):
  ev=r["evidence"+str(k)]
  assert r["criterion"+str(k)]=="PASS" and ev==o["evidence"][k-1] and len(ev)>=2 and ev in o["scene"]
 assert r["passed_of_4"]=="4" and r["V2_disposition"]=="PASS_LIMITED_PAPER_WALKTHROUGH"
 assert r["evaluated_by"]=="SAME_AGENT_NONBLIND_SELF_ASSESSMENT"
 assert r["V3"]==r["independent_C"]=="NOT_RUN" and r["skill_certified"]=="NO"
s=json.loads((P/"V13_CURRENT_V2.json").read_text(encoding="utf8"))
assert s["rounds_completed"]>=65 and s["v3_full47_completed"]==s["skill_certified_count"]==0
assert s["heldout_bank_status"]=="SEALED_NOT_RUN"
print("R066 PASS: frozen twelve original V2 scenes, forty-eight gates; no V3 or Skill.")
