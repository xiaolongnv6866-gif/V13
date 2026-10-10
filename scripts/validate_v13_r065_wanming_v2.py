#!/usr/bin/env python3
"""R065: reproducible structural checks, not independent literary or V3 judgment."""
import csv,hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def ts(path):
 with (ROOT/path).open(encoding="utf8",newline="") as f:return list(csv.DictReader(f,delimiter="\t"))
fpath=ROOT/"v2/v2/WANMING_FROZEN_INPUTS.json"
raw=fpath.read_bytes()
git_sha=hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()
assert git_sha=="a45eae29075595c68d6d23fe2f5455a89182eaa5",git_sha
fixed=json.loads(raw)
cases=fixed["tests"]
assert len(cases)==10 and all(len(t["criteria"])==4 for t in cases)
R=ts("v2/v2/WANMING_RESULTS.tsv")
assert len(R)==10 and [r["case_id"] for r in R]==[t["case_id"] for t in cases]
assert len(set(t["candidate_id"] for t in cases))==10
old={t["candidate_id"]:t for t in ts("gates/R057_REPAIR_V2_11_TEST_DESIGNS.tsv") if t["book"]=="wanming"}
new={t["candidate_id"]:t for t in ts("v2/v1/WANMING_23_RESULTS.tsv")}
assert len(old)==5
ncriteria=0
for i,(c,r) in enumerate(zip(cases,R)):
 assert c["candidate_id"]==r["candidate_id"]
 assert r["source_V1_basis"]==c["candidate_origin"]
 if i<5:
  assert c["candidate_id"] in old and old[c["candidate_id"]]["V1_past"]=="PASS"
  assert old[c["candidate_id"]]["execution_status"]=="DESIGN_ONLY_NO_OUTPUT"
 else:
  assert c["candidate_id"] in new and new[c["candidate_id"]]["R063_V1_result"]=="PASS_NARROW"
 assert r["input_freeze_commit"]=="f34508deb6aa7e3c50df99c6bf7fd13f509d459c"
 assert r["input_freeze_blob_sha"]==git_sha
 outpath=ROOT/r["walkthrough_artifact"]
 assert outpath.is_relative_to(ROOT/"v2/v2/results")
 o=json.loads(outpath.read_text(encoding="utf8"))
 assert o["id"]==c["case_id"] and o["candidate"]==c["candidate_id"]
 assert o["phase"]=="V2_PAPER_WALKTHROUGH_NONBLIND"
 assert o["unknowns_preserved"] is True and len(o["checks"])==4
 assert 160<=len(o["scene"])<=380 and len(o["scene"])==int(r["scene_chars"])
 assert len(o["state"])>=3 and len(o["state"])==int(r["state_rows"])
 assert "SAME_AGENT_SELF_RATED_NONBLIND"==r["evaluator"]
 for j in range(1,5):
  assert r[f"C{j}_pass"]=="PASS",c["case_id"]
  q=r[f"C{j}_evidence"]
  assert 2<=len(q)<70 and q in o["scene"],(c["case_id"],j,q)
  ncriteria+=1
 assert r["V2_result"]=="PASS_LIMITED_PAPER_WALKTHROUGH"
 assert int(r["total_gates_passed"])==4
 assert r["V3_status"]=="NOT_RUN" and r["independent_creative_utility"]=="NOT_RUN"
 assert r["skill_certified"]=="NO"
 assert len(r["failure_or_limit"])>=20
assert ncriteria==40
cur=json.loads((ROOT/"V13_CURRENT_V2.json").read_text(encoding="utf8"))
assert cur["rounds_completed"]>=64 and cur["v3_full47_completed"]==0 and cur["skill_certified_count"]==0
assert cur["heldout_bank_status"]=="SEALED_NOT_RUN"
receipt=(ROOT/"runs/R065_V2.md").read_text(encoding="utf8")
assert all(term in receipt for term in ["10/10","40/40","NONBLIND","NO_V3"])
print("R065 CI source/contract structure PASS: frozen blob unchanged; 10 actual scenes, 40 original criteria, 10 paper V2 only; no V3/C/Skill.")
