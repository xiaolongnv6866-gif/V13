#!/usr/bin/env python3
"""R057 source and routing structural check, not a literary or independent utility judge."""
import csv,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def read(path):
 with (ROOT/path).open(encoding="utf8",newline="") as f:return list(csv.DictReader(f,delimiter="\t"))
def ensure(ok,message):
 if not ok:raise AssertionError(message)
orig=read("books/wanming/R053_CANDIDATE_MATRIX.tsv")+read("books/tiexuecanming/R053_CANDIDATE_MATRIX.tsv")
v1=read("books/wanming/validation/V1_EVIDENCE.tsv")+read("books/tiexuecanming/validation/V1_EVIDENCE.tsv")
v2=read("tests/v2/R055_CANDIDATE_OUTCOMES.tsv");v3=read("tests/v3/R056_CANDIDATE_OUTCOMES.tsv")
result=read("books/wanming/R057_DECISION_MATRIX.tsv")+read("books/tiexuecanming/R057_DECISION_MATRIX.tsv")
by=lambda entries:{x["candidate_id"]:x for x in entries}
ensure(len(orig)==len(v1)==len(v2)==len(v3)==len(result)==187,"187 candidate lineage")
O,A,B,C,D=map(by,(orig,v1,v2,v3,result))
ensure(len(D)==187 and set(O)==set(A)==set(B)==set(C)==set(D),"original ID uniqueness or loss")
rules={"V2_WALKTHROUGH_PASS_LIMITED":("needs_review","PASS","NO_INCREMENTAL_GAIN_DEMONSTRATED_NONBLIND"),
"V1_PASS_V2_NOT_TESTED":("needs_review","PASS","V2_NOT_TESTED_NO_V3"),
"BLOCKED_BY_V1_NEEDS_SOURCE_REPAIR":("needs_review","REVIEW","BLOCKED_V1_NO_V3"),
"REFERENCE_ONLY_NOT_EXECUTABLE_METHOD":("reference","PASS","REFERENCE_NO_INDEPENDENT_V3")}
totals={};obstacles={}
for key,row in D.items():
 o,a,b,c=O[key],A[key],B[key],C[key]
 ensure(row["original_id"]==o["original_id"]==a["original_id"],key+" original ID")
 ensure(row["candidate_source_file"]==o["candidate_source_file"] and row["original_source_loci"]==o["original_source_loci"],key+" provenance")
 ensure(row["task_ids"]==o["task_ids"] and row["title"]==o["title"],key+" source metadata")
 ensure(row["V1"]==a["V1"]==b["V1"]==c["V1"],key+" V1 drift")
 ensure(row["V2"]==b["V2"]==c["V2"] and row["V3"]==c["V3"],key+" V2/V3 drift")
 ensure(row["V2_output_files"]==b["actual_output_files"] and row["V2_input_ids"]==b["actual_input_ids"],key+" actual execution trace")
 ensure(row["V3_primary_pair"]==c["primary_comparison_result"],key+" paired trace")
 ensure(row["V2"] in rules,key+" unexpected V2")
 expected,v1_expected,v3_expected=rules[row["V2"]]
 ensure((row["decision"],row["V1"],row["V3"])==(expected,v1_expected,v3_expected),key+" false promotion")
 ensure(row["decision_reason"] and row["evidence_responsibility"],key+" empty responsibility")
 ensure(row["current_actual_destination"].startswith("books/"+row["book"]+"/"),key+" no current delivery")
 if expected=="reference":ensure(row["future_planned_destination"].endswith("/overview.md") or row["future_planned_destination"].endswith("/glossary.md"),key+" missing future reference destination")
 else:ensure(row["future_planned_destination"]=="NONE_BLOCKED",key+" review active leak")
 totals[expected]=totals.get(expected,0)+1
 obstacles[row["V2"]]=obstacles.get(row["V2"],0)+1
ensure(totals=={"reference":90,"needs_review":97},"four-way totals mismatch")
ensure([obstacles.get(k) for k in rules]==[47,11,39,90],"47/11/39/90 source breakdown")
old=read("cangjie/reading/R042_OLD_CLAIM_QUARANTINE.tsv");qu=read("gates/R057_LEGACY_QUARANTINE.tsv")
ensure(len(old)==len(qu)==14,"14 history quarantine")
ensure({r["legacy_claim_id"] for r in old}=={r["legacy_claim_id"] for r in qu},"missing old ID")
for x in qu:
 ensure(x["decision"]=="needs_review" and x["stage1_permission"]=="NO_DIRECT_PROMOTION_RECONSTRUCT_FROM_SOURCE","old claim accidentally promoted")
 ensure(x["source_boundary"] and x["next_evidence_responsibility"],"legacy source obligation omitted")
cov=read("gates/R057_TASK_COVERAGE.tsv")
ensure(len(cov)==19 and len({x["task_id"] for x in cov})==19,"task count or identity")
scores=json.loads((ROOT/"tests/v3/R056_MATCHED_PAIRED_RATINGS.json").read_text(encoding="utf8"))
by_score={x["id"]:str(x["delta"]) for x in scores["records"]}
for x in cov:
 tid=x["task_id"];expected={k for k,v in O.items() if tid in v["task_ids"].split(",")}
 ensure(bool(expected) and set(x["all_candidates"].split(";"))==expected,tid+" RAW map incomplete")
 for name,route in (("needs_review","needs_review"),("reference","reference")):
  expected_route={k for k in expected if D[k]["decision"]==route}
  ensure(set(x[name].split(";"))==expected_route,tid+" "+name+" mapping")
 ensure(x["verified"]=="" and tid in by_score and x["R056_delta"]==by_score[tid],tid+" false verified or wrong score")
 ensure(x["original_loci"] and x["stage0_missing"],tid+" ungrounded Stage0 task")
ensure({x["task_id"] for x in cov}=={f"WM-{n:02d}" for n in range(1,10)}|{f"TX-{n:02d}" for n in range(1,11)},"task identity")
for slug,refc,reviewc in (("wanming",42,49),("tiexuecanming",48,48)):
 chosen=[x for x in D.values() if x["book"]==slug]
 ensure(sum(x["decision"]=="reference" for x in chosen)==refc and sum(x["decision"]=="needs_review" for x in chosen)==reviewc,slug+" counts")
 for file in ("verified.md","references.md","needs-review.md","coverage-audit.md","rejected/README.md"):
  ensure((ROOT/"books"/slug/file).exists(),slug+" missing delivery "+file)
cur=json.loads((ROOT/"CURRENT_ROUND.json").read_text(encoding="utf8"))
ensure(cur["current_round"]=="R057" and cur["round_status"]=="BLOCKED" and cur["rounds_completed"]==56 and cur["last_passed_round"]=="R056","unapproved round advanced")
ensure(cur.get("cangjie_stage1_5_user_confirm")=="PENDING_R057_USER_APPROVAL","user consent falsified")
with (ROOT/"ROUND_LEDGER.csv").open(encoding="utf8",newline="") as f:ledger={x["id"]:x for x in csv.DictReader(f)}
ensure(ledger["R056"]["status"]=="PASSED" and ledger["R057"]["status"]=="BLOCKED","ledger approval gate")
print("R057 STRUCTURE PASS: 187 exact candidate origins; verified0 reference90 needs_review97 rejected0; 14 old quarantines, 19 RAW/0 verified tasks; cursor BLOCKED.")
