#!/usr/bin/env python3
"""B076 Stage1.5 honest triage integrity. Passing does NOT grant user confirmation."""
import csv, json, pathlib, subprocess
P=pathlib.Path(__file__).resolve().parents[1]
def rows(path):
 with (P/path).open("r",encoding="utf-8",newline="") as f:return list(csv.DictReader(f,delimiter="\t"))
def sha(path):return subprocess.check_output(["git","hash-object",str(P/path)],text=True).strip()
counts={"wanming":(91,51,40,31),"tiexuecanming":(96,57,39,38)}
allids=[]
all_new=[]
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
  assert a["decision"]==b["B076_final_decision"] or (a["decision"]=="needs_review" and b["B076_final_decision"]=="reference" and b["candidate_id"] in {x["candidate_id"] for x in rows("gates/B076_18_SOURCE_ONLY_REFERENCE_ROUTE.tsv")})
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
 all_new.extend(new)
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
assert state["batch_status"]=="BLOCKED"
gate=(P/"gates/CANGJIE_STAGE15_V2.md").read_text()
assert "BLOCKED_ZERO_VERIFIED_APPROVAL_A_RECORDED" in gate
assert "user_confirmation: APPROVED_A_2026_10_10_PLANNING_ONLY" in gate
assert "187" in gate and "97" in gate and "90" in gate
assert state["overall_management_units_completed"]==75
assert state["b076_user_approval"]=="APPROVED_A_2026_10_10_PLANNING_ONLY"
assert "user_selection: A" in (P/"gates/R078_USER_APPROVAL_A_20261010.md").read_text()
q28=rows("gates/B076_APPROVED_A_V1_28_REPAIR_QUEUE.tsv")
q69=rows("gates/B076_APPROVED_A_V3_69_REPLICATION_QUEUE.tsv")
q20=rows("gates/B076_APPROVED_A_STAGE0_20_CONTRACT_GAP_PLAN.tsv")
assert len(q28)==28 and len(q69)==69 and len(q20)==20
assert sum(x["book"]=="wanming" for x in q28)==18
assert sum(x["book"]=="tiexuecanming" for x in q28)==10
assert {x["candidate_id"] for x in q69}=={x["candidate_id"] for x in original+additional}
assert len(set(x["repeat_id"] for x in q69))==69
assert all(x["independent_author"]==x["blind_judge"]=="UNASSIGNED" and x["real_independent_test"]=="NOT_RUN" for x in q69)
raw={x["candidate_id"]:(x["raw_path"],x["raw_git_blob_sha1"]) for x in original+additional}
assert all((x["source_raw_path"],x["source_git_sha"])==raw[x["candidate_id"]] for x in q69)
assert {x["candidate_id"] for x in q28}==({x["candidate_id"] for x in all_new if x["B076_final_decision"]=="needs_review" and x["raw_pair_git_sha"]=="NONE"} | {x["candidate_id"] for x in rows("gates/B076_18_SOURCE_ONLY_REFERENCE_ROUTE.tsv")})
assert len({x["old_task_id"] for x in q20})==20
assert all(x["original_required_output"] and x["original_success_and_failure"] and x["independent_full_task_acceptance"]=="NOT_RUN" for x in q20)
assert {x["old_task_id"] for x in q20}=={x["old_Stage0_id"] for x in cross}
assert "approved" in (P/"gates/B076_APPROVED_A_EVIDENCE_PROTOCOL.md").read_text().lower()
audit=rows("gates/B076_V1_28_ACTUAL_SOURCE_RECHECK.tsv")
assert len(audit)==28
audit_by_id={x["candidate_id"]:x for x in audit}
assert set(audit_by_id)=={x["candidate_id"] for x in q28}
assert sum(x["book"]=="wanming" for x in audit)==18
assert sum(x["book"]=="tiexuecanming" for x in audit)==10
assert sum(len(x["source_loci"].split(";")) for x in audit)==89
assert len(set((x["book"],y) for x in audit for y in x["source_loci"].split(";")))==76
assert all(x["V1_result"]=="REVIEW_SOURCE_RECHECKED_NOT_PASSED" and x["independent_v3"]=="NOT_RUN" for x in audit)
assert all(len(x["paragraph_digest_sha256"])==64 for x in audit)
for x in q28:
 y=audit_by_id[x["candidate_id"]]
 assert x["book"]==y["book"] and x["source_loci"]==y["source_loci"]
 assert x["evidence_digest_sha256"]==y["paragraph_digest_sha256"]
 assert x["actual_source_recheck_file"]=="gates/B076_V1_28_ACTUAL_SOURCE_RECHECK.tsv"
 assert x["status"] in ("B076_REFERENCE_ROUTED","B076_V1_NARROW_PASS","B076_V1_SOURCE_GAP_REMAINS","B076_V1_PASS_NARROW_V2_WALKTHROUGH_ONLY_V3_NOT_RUN")
 assert x["B076_V1"] in ("REVIEW","PASS_NARROW","REFERENCE_SOURCE_ONLY")
 assert x["reviewer"]=="SAME_AGENT_EPUB_CONTEXT_REVIEW_NOT_INDEPENDENT"
assert "89" in (P/"gates/B076_V1_28_SOURCE_RECHECK_REPORT.md").read_text()
assert "source_paths" in (P/"scripts/verify_b076_v1_private_epub_receipts.py").read_text()
print("B076 evidence: original 28 source receipts retained; 3 narrowed V1 passes, 3 limited V2 walkthroughs; V3 NOT_RUN; B076 BLOCKED")


# Incremental B076 literary-claim scope and Stage0 contract preservation (not a V1/V3 certification).
fix=rows("gates/B076_V1_28_CLAIM_SCOPE_ADJUDICATION.tsv")
assert len(fix)==28 and {x["candidate_id"] for x in fix}==set(audit_by_id)
assert sum(x["V1_scope_adjudication"]=="NARROW_SOURCE_SUPPORT" for x in fix)==4
assert sum(x["V1_scope_adjudication"]=="REVIEW_COMPOSITE" for x in fix)==6
assert sum(x["V1_scope_adjudication"]=="SOURCE_ONLY_REFERENCE" for x in fix)==18
assert all(x["formal_v1_method_pass"]=="NO_FORMAL_PASS_PRESERVE_BLOCK" and x["independent_V3"]=="NOT_RUN" and x["formal_four_way_unchanged"]=="needs_review" for x in fix)
assert all(x["source_loci"]==audit_by_id[x["candidate_id"]]["source_loci"] and x["paragraph_digest_sha256"]==audit_by_id[x["candidate_id"]]["paragraph_digest_sha256"] for x in fix)
audit20=rows("gates/B076_STAGE0_20_EXACT_DELIVERABLE_REAUDIT.tsv")
assert len(audit20)==20 and {x["old_task_id"] for x in audit20}=={x["old_task_id"] for x in q20}
assert all(x["contract_execution"]=="CONTRACT_RESTORED_NOT_RUN" and x["independent_acceptance"]=="NOT_RUN" for x in audit20)
assert all(x["old_required_output"]==next(y["original_required_output"] for y in q20 if y["old_task_id"]==x["old_task_id"]) for x in audit20)
for oldid in ("WM-T05","WM-T09"):
 assert next(x for x in audit20 if x["old_task_id"]==oldid)["exact_gap_adjudication"].startswith("SPECIAL_RESTORED")
assert state["b076_v1_claim_scope_reviewed"]==28 and state["b076_new_v1_pass"]==3
assert "Original immutable requirement" in (P/"gates/B076_STAGE0_WM_T05_T09_RESTORED_CONTRACTS.md").read_text()
print("B076 incremental: 28 claim scopes adjudicated (4/6/18); 20 original Stage0 outputs retained, T05/T09 executable test contracts restored; no V1/V3 promotion")

# The 18 source-only references are real markdown destinations, not skill methods.
new18=rows("gates/B076_18_SOURCE_ONLY_REFERENCE_ROUTE.tsv")
new4=rows("gates/B076_V1_4_NARROW_FINAL_ADJUDICATION.tsv")
assert len(new18)==18 and len({x["candidate_id"] for x in new18})==18
assert len(new4)==4 and {x["candidate_id"] for x in new4 if x["V1"]=="PASS_NARROW"}=={"WM-f15","WM-p09","WM-p17"}
assert all(x["V3"]=="NOT_RUN" for x in new4)
assert sum(x["V2"]=="WALKTHROUGH_PASS_LIMITED" for x in new4)==3
assert next(x for x in new4 if x["candidate_id"]=="WM-p02")["V2"]=="NOT_RUN"
assert sum(x["book"]=="wanming" for x in new18)==sum(x["book"]=="tiexuecanming" for x in new18)==9
for x in new18:
 r=next(y for y in all_new if y["candidate_id"]==x["candidate_id"])
 assert r["B076_final_decision"]=="reference" and r["actual_destination"]==x["destination"]
 assert r["stage3_materialized"]=="PLANNED_ONLY_NOT_CREATED"
 assert r["raw_pair_git_sha"]=="NONE"
 assert x["digest"]==audit_by_id[x["candidate_id"]]["paragraph_digest_sha256"]
 path,anchor=x["destination"].split("#")
 assert ("### "+x["candidate_id"]) in (P/path).read_text()
assert state["b076_decisions"]["reference"]==108 and state["b076_decisions"]["needs_review"]==79
assert state["b076_reference_routing_new"]==18 and state["overall_management_units_completed"]==75
print("B076 refreshed: 18 references, 3 V1 narrow and 3 V2 walkthrough only, 0 independent V3, block unchanged")
