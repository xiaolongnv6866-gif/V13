#!/usr/bin/env python3
"""B076 Stage1.5 honest triage integrity. Passing does NOT grant user confirmation."""
import csv, json, pathlib, subprocess
P=pathlib.Path(__file__).resolve().parents[1]
def rows(path):
 with (P/path).open("r",encoding="utf-8",newline="") as f:return list(csv.DictReader(f,delimiter="\t"))
def sha(path):return subprocess.check_output(["git","hash-object",str(P/path)],text=True).strip()
counts={"wanming":(91,42,49,31),"tiexuecanming":(96,48,48,38)}
allids=[]
for book,(total,refs,needs,tested) in counts.items():
 old=rows(f"books/{book}/R057_DECISION_MATRIX.tsv")
 new=rows(f"books/{book}/R078_V2_DECISION_MATRIX.tsv")
 assert len(old)==len(new)==total
 assert [r["candidate_id"] for r in old]==[r["candidate_id"] for r in new]
 assert sum(x["B076_final_decision"]=="reference" for x in new)==refs
 assert sum(x["B076_final_decision"]=="needs_review" for x in new)==needs
 assert sum(x["B076_final_decision"] in ("verified","rejected") for x in new)==0
 assert sum(x["raw_pair_git_sha"]!="NONE" for x in new)==tested
 for a,b in zip(old,new):
  assert a["decision"]==b["B076_final_decision"]
  assert a["original_source_loci"]==b["source_loci"]
  assert a["candidate_id"]==b["candidate_id"]
  if b["raw_pair_git_sha"]!="NONE":
   assert sha(b["evidence_path"])==b["raw_pair_git_sha"]
   assert b["B076_current_V3"].startswith("NONBLIND_PAIRED_DIAGNOSTIC_DELTA_")
   assert b["B076_final_decision"]=="needs_review"
  elif b["B076_final_decision"]=="reference":
   assert b["stage3_planned_destination"]!="NONE_UNTIL_VERIFIED"
   assert b["stage3_materialized"]=="PLANNED_ONLY_NOT_CREATED"
   assert (P/b["actual_destination"].split("#")[0]).is_file()
 assert "count: 0" in (P/f"books/{book}/verified.md").read_text()
 assert "count: 0" in (P/f"books/{book}/rejected/README.md").read_text()
 allids.extend(x["candidate_id"] for x in new)
assert len(allids)==len(set(allids))==187
original=rows("v2/v3/FINAL_47_EVIDENCE_AUDIT.tsv")
additional=rows("v2/v3/FINAL_22_ADDITIONAL_AUDIT.tsv")
assert len(original)==47 and len(additional)==22
assert {x["candidate_id"] for x in original+additional} <= set(allids)
assert len(set(x["candidate_id"] for x in original+additional))==69
assert sha("v2/v3/FROZEN_TEST_CONTRACT.json")=="4e24d782632210c1e1637eba4954bde3d8f3846f"
assert len(rows("gates/R078_OLD14_QUARANTINE_ROUTE.tsv"))==14
cross=rows("gates/R078_STAGE0_ORIGINAL20_TO_R057_19_CROSSWALK.tsv")
tasks=rows("v2/v3/B075_STAGE0_19_COVERAGE_AUDIT.tsv")
assert len(cross)==20 and len(tasks)==19
assert len(set(r["old_Stage0_id"] for r in cross))==20
assert all(r["independent_full_task_acceptance"]=="NOT_RUN" for r in cross)
assert all(r["independent_C"]=="NOT_RUN" for r in tasks)
state=json.loads((P/"V13_CURRENT_V3.json").read_text())
assert state["current_batch"]=="B076"
assert state["last_passed_batch"]=="B075"
assert state["skill_certified_count"]==0
assert state["batch_status"] in ("NOT_STARTED","BLOCKED_PENDING_USER_CONFIRM")
gate=(P/"gates/CANGJIE_STAGE15_V2.md").read_text()
assert "BLOCKED_PENDING_EXPLICIT_USER_CONFIRM" in gate
assert "user_confirmation: NOT_YET_GRANTED" in gate
assert "187" in gate and "97" in gate and "90" in gate
print("B076 TRIAGE_EVIDENCE_OK: 187 unique, 90 reference, 97 needs review, 0 verified, 14 historic; user confirmation absent, B076 BLOCKED")
