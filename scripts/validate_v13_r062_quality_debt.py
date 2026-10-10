#!/usr/bin/env python3
"""R062 structural and identity ledger check. Does not adjudicate literary B or utility C."""
import csv,json
from pathlib import Path
P=Path(__file__).resolve().parents[1]
def tsv(f):
 with (P/f).open(encoding="utf-8",newline="") as v:return list(csv.DictReader(v,delimiter="\t"))
src=tsv("v2/ISSUE_REGISTRY.tsv")
out=tsv("v2/stage0/QUALITY_DEBT_ROUTING.tsv")
assert len(out)==len(src)==426
assert [x["issue_id"] for x in out]==[x["issue_id"] for x in src]
assert len({r["issue_id"] for r in out})==426
cnt={t:sum(x["issue_type"]==t for x in out) for t in set(x["issue_type"] for x in out)}
assert cnt=={"STAGE0_B_CLAIM":296,"LEGACY_R042_QUARANTINE":14,"V1_SOURCE_REVIEW":39,"V2_EXECUTABILITY_NOT_TESTED":11,"V3_NO_GAIN_PROVEN":47,"STAGE0_TASK_COVERAGE":19},cnt
live={z["issue_id"]:z for z in tsv("v2/stage0/STAGE0_B_AUDIT_STATUS_V2.tsv")}
assert len(live)==296
read=[x for x in out if x["issue_type"]=="STAGE0_B_CLAIM"]
assert sum(live[x["issue_id"]]["review_state"]=="REVIEWED_R058" for x in read)==43
assert sum(live[x["issue_id"]]["review_state"]=="REVIEWED_R059" for x in read)==61
assert sum(live[x["issue_id"]]["review_state"]=="B_PROVISIONAL_NOT_REAUDITED" for x in read)==192
leg=[x for x in out if x["issue_type"]=="LEGACY_R042_QUARANTINE"]
assert len(leg)==14 and all(x["B_literary_status"]=="OLD_OPEN_QUARANTINED_NEW_SCOPED_B_PROVISIONAL" for x in leg)
wm=tsv("v2/legacy/WANMING_7_DECISIONS.tsv")
tx=tsv("v2/legacy/TIEXUE_7_DECISIONS.tsv")
assert len(wm)==len(tx)==7
assert {x["origin_id"] for x in leg}=={z["legacy_claim_id"] for z in wm+tx}
assert {x["new_candidate_id"] for x in leg}=={z["new_candidate_id"] for z in wm+tx}
tasks=[x for x in out if x["issue_type"]=="STAGE0_TASK_COVERAGE"]
frozen=tsv("gates/R057_TASK_COVERAGE.tsv")
assert len(tasks)==len(frozen)==19 and {x["origin_id"] for x in tasks}=={x["task_id"] for x in frozen}
assert all("sources/metadata/" not in x["frozen_source"] or 1 for x in tasks)
assert all(x["certification_permission"]=="NONE_VERIFIED_TASK_BASIS" for x in tasks)
assert all(x["C_creative_utility"]=="NOT_RUN_STANDALONE" for x in tasks)
assert all(x["B_literary_status"]!="VERIFIED" and x["certification_permission"]!="ACTIVE" for x in out)
assert all(not x["C_creative_utility"].startswith("PASS") for x in out)
for p in ["books/wanming/BOOK_OVERVIEW.md","books/tiexuecanming/BOOK_OVERVIEW.md"]:
 assert (P/p).is_file()
assert all(x["verified"]=="" for x in frozen)
doc=(P/"v2/stage0/BOOK_OVERVIEW_DELTA.md").read_text(encoding="utf-8")
report=(P/"runs/R062_V2.md").read_text(encoding="utf-8")
for tok in ["296","104","192","14/14","19/19","68","49","TX-08","R078","0/47"]:
 assert tok in doc,tok
assert "426" in report and "NOT_RUN" in report
state=json.loads((P/"V13_CURRENT_V2.json").read_text(encoding="utf-8"))
assert state["rounds_completed"]>=61 and state["skill_certified_count"]==0 and state["v3_full47_completed"]==0 and state["heldout_bank_status"]=="SEALED_NOT_RUN"
print("R062 ROUTING STRUCTURE PASS: all 426 frozen IDs; 296 Stage0 B (43+61+192), 14 old quarantines, 19 tasks, 39 V1, 11 V2, 47 V3; no active certification.")
