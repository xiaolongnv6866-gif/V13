#!/usr/bin/env python3
"""V13.3 source-of-truth integrity: identities and contracts only, not literary pass."""
import csv,json,re
from pathlib import Path
from collections import Counter
P=Path(__file__).resolve().parents[1]
def rd(f):
 with (P/f).open(encoding="utf-8",newline="") as h:return list(csv.DictReader(h,delimiter="\t"))
s=json.loads((P/"V13_CURRENT_V4.json").read_text(encoding="utf-8"))
assert (s["current_round"],s["current_round_status"],s["completed_new_rounds"],s["total_new_rounds"])==("N01","NOT_STARTED",0,48)
assert s["actual_N01_work_started"] is False and s["historical_completed_admin"]==75
b=json.loads((P/"V13_CURRENT_V3.json").read_text(encoding="utf-8"))
assert b["overall_management_units_completed"]==75 and b["current_batch"]=="B076"
n=rd("V13_LEDGER_V4.tsv")
assert len(n)==48 and [x["round_id"] for x in n]==["N"+str(i).zfill(2) for i in range(1,49)]
assert all(x["status"]=="NOT_STARTED" and x["acceptance"] for x in n)
assert sum(int(x["required_objects"]) for x in n[:15])==296
assert sum(int(x["old_unreviewed_count"]) for x in n[:15])==192
assert sum(int(x["old_R042_quarantine_count"]) for x in n[:15])==14
a=rd("V13_3_ISSUES_426_TO_ROUNDS.tsv"); f=rd("v2/ISSUE_REGISTRY.tsv")
assert len(a)==len(f)==426 and [x["issue_id"] for x in a]==[x["issue_id"] for x in f]
assert Counter(x["issue_type"] for x in a)=={"STAGE0_B_CLAIM":296,"LEGACY_R042_QUARANTINE":14,"V1_SOURCE_REVIEW":39,"V2_EXECUTABILITY_NOT_TESTED":11,"V3_NO_GAIN_PROVEN":47,"STAGE0_TASK_COVERAGE":19}
for row in n[:15]:
 bunch=[x for x in a if x["new_primary_round"]==row["round_id"]]
 assert sum(x["issue_type"]=="STAGE0_B_CLAIM" for x in bunch)==int(row["required_objects"])
 assert sum(x["issue_type"]=="LEGACY_R042_QUARANTINE" for x in bunch)==int(row["old_R042_quarantine_count"])
 assert sum(x["at_migration_status"]=="B_PROVISIONAL_NOT_REAUDITED" for x in bunch)==int(row["old_unreviewed_count"])
assert len([x for x in a if x["issue_type"]=="LEGACY_R042_QUARANTINE"])==14
old=rd("v2/stage0/STAGE0_B_AUDIT_STATUS_V2.tsv")
assert Counter(x["review_state"] for x in old)=={"REVIEWED_R058":43,"REVIEWED_R059":61,"B_PROVISIONAL_NOT_REAUDITED":192}
c=rd("V13_3_CANDIDATES_187_TO_ROUNDS.tsv")
assert len(c)==len({x["candidate_id"] for x in c})==187
assert Counter(x["old_four_way"] for x in c)=={"reference":108,"needs_review":79}
assert Counter(x["book"] for x in c)=={"wanming":91,"tiexuecanming":96}
v=rd("V13_3_V3_69_TO_ROUNDS.tsv")
assert len(v)==len({x["candidate_id"] for x in v})==69
assert Counter(x["cohort"] for x in v)=={"ORIGINAL47":47,"EXTRA22":22}
assert Counter(x["real_V3_round"] for x in v)=={"N22":21,"N23":26,"N24":10,"N25":12}
assert all(x["actual_independent_result"]=="NOT_RUN" and x["creator"]=="UNASSIGNED" for x in v)
assert {x["candidate_id"] for x in v} <= {x["candidate_id"] for x in c}
o=rd("V13_3_STAGE0_20_TO_ROUNDS.tsv")
assert len(o)==20 and len({x["old_task_id"] for x in o})==20
assert Counter(x["original_full_C_round"] for x in o)=={"N26":10,"N27":10}
assert {"WM-T05","WM-T09"} <= {x["old_task_id"] for x in o}
assert all(x["truly_independent_C"]=="NOT_RUN" for x in o)
m=rd("V13_3_ORIGINAL_44_CONTRACTS_MAP.tsv")
assert len(m)==44 and {x["original_contract"] for x in m}=={"R"+str(i).zfill(3) for i in range(67,111)}
assert all(x["original_required_actions"] and x["original_required_files"] and x["original_acceptance"] and x["do_not_delete"]=="TRUE" for x in m)
assert all(q in {x["round_id"] for x in n} for x in m for q in x["new_rounds"].split(";"))
assert s["verified"]==s["certified_skills"]==0 and s["reference"]==108 and s["needs_review"]==79
print("PASS V13.3 48 round migration, 426 frozen issues, 296 B, 192 unreviewed, 14 quarantine, 187 candidates, 69 V3 and 20 original Stage0; 44 uncut original contracts")
