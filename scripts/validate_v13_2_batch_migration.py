#!/usr/bin/env python3
"""V13.2 migration audit and rolling cursor integrity: preserve 44 contracts, 47 IDs."""
import csv,hashlib,json,re
from pathlib import Path
P=Path(__file__).resolve().parents[1]
def blob(path):
 b=(P/path).read_bytes()
 return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()
def tab(path):
 with (P/path).open(encoding="utf-8",newline="") as f:
  return list(csv.DictReader(f,delimiter="\t"))
def csvs(path):
 with (P/path).open(encoding="utf-8",newline="") as f:return list(csv.DictReader(f))
s=json.loads((P/"V13_CURRENT_V3.json").read_text(encoding="utf-8"))
h=json.loads((P/"V13_CURRENT_V2.json").read_text(encoding="utf-8"))
assert s["plan_version"]=="v13.2-consolidated-96" and s["batch_status"] in {"NOT_STARTED","IN_PROGRESS","BLOCKED","BLOCKED_PENDING_USER_CONFIRM","FAILED","PASSED"}
assert s["overall_management_units_total"]==96 and s["overall_management_units_completed"]==66+s["v13_2_new_batches_completed"]
assert s["v13_2_new_batches_total"]==30 and 0<=s["v13_2_new_batches_completed"]<=30
assert h["rounds_completed"]==66 and h["current_round"]=="R067" and h["round_status"]=="NOT_STARTED"
assert blob("V13_CURRENT_V2.json")==s["frozen_v13_1_state_blob"]=="0b782d604a2217fcc5e1c73a69e4108373e4fe42"
assert blob("V13_LEDGER_V2.csv")==s["frozen_v13_1_ledger_blob"]=="3c5e7a34e752e45a089de926cd7280256e554bdc"
assert blob("V13_REVISED_110_ROUNDS.md")=="55256653a7f9359339a5f7a8924e4210ee25203a"
L=csvs("V13_LEDGER_V3.csv")
assert len(L)==30 and [x["batch_id"] for x in L]==["B%03d"%i for i in range(67,97)]
assert all(x["status"] in {"NOT_STARTED","IN_PROGRESS","FAILED","BLOCKED","BLOCKED_PENDING_USER_CONFIRM","PASSED"} for x in L)
n=s["v13_2_new_batches_completed"]
assert [x["status"] for x in L[:n]]==["PASSED"]*n
assert all(x["status"]!="PASSED" for x in L[n:])
if n<30:
 assert (s["current_batch"],s["batch_status"])==(L[n]["batch_id"],L[n]["status"])
else:
 assert (s["current_batch"],s["batch_status"])==("B096","PASSED")
assert s["last_passed_batch"]==("B%03d"%(66+n) if n else None)
C=tab("V13_LEGACY_TO_BATCH_V3.tsv")
assert len(C)==44 and [x["legacy_round"] for x in C]==["R%03d"%i for i in range(67,111)]
batches={x["batch_id"]:x for x in L}
original=(P/"V13_REVISED_110_ROUNDS.md").read_text(encoding="utf-8").splitlines()
for x in C:
 rid=x["legacy_round"];i=next(i for i,t in enumerate(original) if t.startswith("### "+rid+" · "))
 end=next((j for j in range(i+1,len(original)) if original[j].startswith("### R")),len(original))
 section=original[i:end]
 def field(k):return next(t.split("：",1)[1] for t in section if t.startswith("- **"+k+"**："))
 assert x["legacy_title"]==original[i].split(" · ",1)[1]
 assert x["mandatory_operation_unabridged"]==field("必须操作")
 assert x["required_artifacts_unabridged"]==field("必须产物")
 assert x["original_acceptance_unabridged"]==field("验收标准")
 assert x["legacy_user_or_auto_gate"]==field("硬门/状态")
 bs=x["new_batches"].split(";")
 assert all(rid in batches[b]["legacy_rounds"].split(";") for b in bs)
 assert len(bs)==(2 if rid in ("R069","R072","R073") else 1)
for b,row in batches.items():
 original_for_batch=[x["legacy_round"] for x in C if b in x["new_batches"].split(";")]
 assert row["legacy_rounds"].split(";")==original_for_batch
gates={x["legacy_round"] for x in C if x["legacy_user_or_auto_gate"]=="MANDATORY_USER_CONFIRM"}
assert gates=={"R078","R098","R101","R104","R107","R110"}
assert {x["batch_id"] for x in L if x["gate"]=="MANDATORY_USER_CONFIRM"}==set(s["user_confirm_batches"])=={"B076","B087","B088","B090","B093","B096"}
A=tab("V13_V3_47_METHOD_ALLOCATION_V3.tsv")
orig=tab("gates/R057_REPAIR_V3_47_TEST_QUEUE.tsv")
assert len(A)==len(orig)==47 and len({x["candidate_id"] for x in A})==47
old={x["candidate_id"]:x for x in orig}
distribution={}
for x in A:
 src=old[x["candidate_id"]];b=x["new_v13_2_batch"]
 assert x["book"]==src["book"] and x["original_V1"]==src["prior_V1"] and x["original_V2"]==src["prior_V2"]
 assert x["original_V3"]==src["prior_V3"] and x["original_task_ids"]==src["stage0_task_ids"]
 assert x["original_v13_1_round"] in batches[b]["legacy_rounds"].split(";")
 assert x["freeze_contract_batch"]=="B067" and x["arm_parity"]=="SAME_INPUT_SAME_CONSTRAINTS_ONLY_METHOD_CARD_DIFF"
 distribution[b]=distribution.get(b,0)+1
assert distribution=={"B068":11,"B069":10,"B070":9,"B071":9,"B072":8}
assert sum(x["book"]=="wanming" for x in A)==21 and sum(x["book"]=="tiexuecanming" for x in A)==26
assert 0<=s["v3_original_47_completed"]<=47 and s["skill_certified_count"]>=0 and s["heldout_bank_status"] in ("SEALED_NOT_RUN","AUTHORIZED_OPENED","COMPLETED")
print("V13.2 MIGRATION PASS: 44/44 inherited contracts, 30 batches, 47/47 exact V3 IDs, six original user gates, v13.1 frozen.")
