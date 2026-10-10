#!/usr/bin/env python3
"""B075 evidence-only audit; never equate GitHub green with literary verification."""
import csv, json, pathlib, subprocess
P=pathlib.Path(__file__).resolve().parents[1]
def sha(path):return subprocess.check_output(["git","hash-object",str(path)],cwd=P,text=True).strip()
def tab(path):
 with (P/path).open("r",encoding="utf-8",newline="") as h:return list(csv.DictReader(h,delimiter="\t"))
def file(path):return json.loads((P/path).read_text(encoding="utf-8"))
o=tab("v2/v3/FINAL_47_EVIDENCE_AUDIT.tsv")
a=tab("v2/v3/FINAL_22_ADDITIONAL_AUDIT.tsv")
tasks=tab("v2/v3/B075_STAGE0_19_COVERAGE_AUDIT.tsv")
original=file("v2/v3/FROZEN_TEST_CONTRACT.json")["cases"]
assert sha(P/"v2/v3/FROZEN_TEST_CONTRACT.json")=="4e24d782632210c1e1637eba4954bde3d8f3846f"
assert sha(P/"v2/v3/B073_WM_PREREGISTERED_INPUTS.json")=="a62d1ade7017fca01e405edbcb93368489c9122f"
assert sha(P/"v2/v3/B074_TX_PREREGISTERED_INPUTS.json")=="b44928f5728e771127dacdeefb0ad61a12ad8c28"
assert len(o)==47 and len(a)==22 and len(tasks)==19 and len(original)==47
assert len(set(x["candidate_id"] for x in o+a))==69
assert {x["candidate_id"] for x in o}=={x["candidate_id"] for x in original}
assert sum(x["book"]=="wanming" for x in o)==21 and sum(x["book"]=="tiexuecanming" for x in o)==26
assert sum(x["book"]=="wanming" for x in a)==10 and sum(x["book"]=="tiexuecanming" for x in a)==12
for r in o:
 assert all(r[k]=="PASS" for k in ["frozen_contract_valid","id_match","han_length_match","score_arithmetic_match","evidence_quote_exists","state_and_counterexample"])
 assert r["creator_and_judge"]=="SAME_AGENT_NONBLIND"
 assert r["actual_prompt_arm_separation"]==r["independent_judge"]=="NOT_ESTABLISHED"
 assert r["V3_utility"]=="NOT_VERIFIED"
 assert sha(P/r["raw_path"])==r["raw_git_blob_sha1"]
 assert file(r["raw_path"])["candidate_id"]==r["candidate_id"]
for r in a:
 assert all(r[k]=="PASS" for k in ["freeze_valid","id_match","length_valid","score_valid","state_ledger_and_negative"])
 assert r["baseline_and_method_same_scene_one"]=="YES"
 assert r["actual_prompt_arm_separation"]==r["evaluator_independent"]=="NOT_ESTABLISHED"
 assert r["V3_outcome"]=="DIAGNOSTIC_ONLY_NOT_VERIFIED"
 assert sha(P/r["raw_path"])==r["raw_git_blob_sha1"]
 assert file(r["raw_path"])["candidate_id"]==r["candidate_id"]
assert sum(int(x["observed_self_rating_delta"])==0 for x in o)==35
assert sum(int(x["observed_self_rating_delta"])==1 for x in o)==12
assert sum(int(x["self_rated_delta"])==0 for x in a)==15
assert sum(int(x["self_rated_delta"])==1 for x in a)==7
all_ids={r["candidate_id"] for r in o+a}
legacy=tab("gates/R057_TASK_COVERAGE.tsv")
assert len(legacy)==19
assert {x["task_id"] for x in legacy}=={x["task_id"] for x in tasks}
for r in tasks:
 assert r["candidate_link_status"]=="SOURCE_CANDIDATE_LINK_PRESENT"
 assert r["Stage0_full_task_output"]=="NOT_ASSESSED_AS_FULL_STAGE0_TASK"
 assert r["independent_C"]=="NOT_RUN"
 ids=set(filter(None,r["tested_candidate_ids"].split(";")))
 assert ids and ids<=all_ids
 old=next(x for x in legacy if x["task_id"]==r["task_id"])
 assert ids==set(filter(None,old["all_candidates"].split(";")))&all_ids
 assert int(r["original47_associated_count"])==len(ids&{x["candidate_id"] for x in o})
 assert int(r["additional22_associated_count"])==len(ids&{x["candidate_id"] for x in a})
assert sum(x["task_id"].startswith("WM-") for x in tasks)==9
assert sum(x["task_id"].startswith("TX-") for x in tasks)==10
q=tab("v2/stage0/STAGE0_B_AUDIT_STATUS_V2.tsv")
assert len(q)==296 and sum(x["review_state"]=="B_PROVISIONAL_NOT_REAUDITED" for x in q)==192
# Distinguish original 20 Stage0 tasks from R057's 19. This is a reported mapping debt.
w=(P/"books/wanming/adler/TASKS.md").read_text(encoding="utf-8")
t=(P/"books/tiexuecanming/adler/TASKS.md").read_text(encoding="utf-8")
assert sum(x.startswith("| T") and x[3:5].isdigit() for x in w.splitlines())==10
assert sum(x.startswith("| TX-T") for x in t.splitlines())==10
state=file("V13_CURRENT_V3.json")
assert state["v3_original_47_completed"]==47 and state["skill_certified_count"]==0
assert int(state["current_batch"][1:])>=75
print("B075 PASS evidence only: original47/47; additional22/22; 69 unverified, 19 candidate-linked tasks only, 192 Stage0 unreviewed; independent C NOT_RUN")
