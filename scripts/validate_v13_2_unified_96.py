#!/usr/bin/env python3
"""96-round consolidation integrity. Structural routing only; not V1/V3 literary approval."""
import csv,json
from pathlib import Path
from collections import Counter
P=Path(__file__).resolve().parents[1]
def rd(p,delim="\t"):
 with (P/p).open(encoding="utf-8",newline="") as f:return list(csv.DictReader(f,delimiter=delim))
a=rd("gates/V13_96_ISSUE_426_ROUTING.tsv")
f=rd("v2/ISSUE_REGISTRY.tsv")
assert len(a)==len(f)==426 and [x["issue_id"] for x in a]==[x["issue_id"] for x in f]
assert len({x["issue_id"] for x in a})==426
assert set(x["current_batch"] for x in a)=={"B076"}
assert Counter(x["frozen_type"] for x in a)=={"STAGE0_B_CLAIM":296,"LEGACY_R042_QUARANTINE":14,"V1_SOURCE_REVIEW":39,"V2_EXECUTABILITY_NOT_TESTED":11,"V3_NO_GAIN_PROVEN":47,"STAGE0_TASK_COVERAGE":19}
count=Counter(x["actual_evidence_status"] for x in a)
expected={"UNREVIEWED_B_OPEN":192,"SCOPED_B_REVIEW_NOT_VERIFIED":104,"OPEN_QUARANTINED":14,"ROUTED_REFERENCE":18,"NEW_LIMITED_V1":3,"V1_REMAINING_OPEN":7,"EARLIER_LIMITED_V1":11,"LEGACY_V2_LIMITED_NOT_REAL_V3":11,"NONBLIND_OLD_OUTPUT_INDEPENDENT_NOT_RUN":47,"R057_TOPIC_LINK_ONLY_FULL_C_NOT_RUN":19}
assert dict(count)==expected
b=rd("gates/V13_96_BATCH_MASTER_30.tsv")
l=rd("V13_LEDGER_V3.csv",",")
assert len(b)==len(l)==30
ids=["B"+str(i).zfill(3) for i in range(67,97)]
assert [x["batch_id"] for x in b]==[x["batch_id"] for x in l]==ids
assert sum(x["official_status"]=="PASSED" for x in b)==9
assert next(x for x in b if x["batch_id"]=="B076")["official_status"]=="BLOCKED"
assert all(x["official_status"]=="NOT_STARTED" for x in b if x["batch_id"]>="B077")
legacy=rd("V13_LEGACY_TO_BATCH_V3.tsv")
assert len(legacy)==44 and {x["legacy_round"] for x in legacy}=={"R"+str(i).zfill(3) for i in range(67,111)}
for x in legacy:
 for oldbatch in x["new_batches"].split(";"):
  assert x["legacy_round"] in next(r for r in b if r["batch_id"]==oldbatch)["source_contract_ids"].split(";")
c=rd("gates/V13_96_CANDIDATES_187_ROUTING.tsv")
assert len(c)==len({x["candidate_id"] for x in c})==187
assert Counter(x["current_decision"] for x in c)=={"reference":108,"needs_review":79}
v=rd("gates/V13_96_V3_69_ROUTING.tsv")
assert len(v)==len({x["candidate_id"] for x in v})==69
assert Counter(x["cohort"] for x in v)=={"ORIGINAL47":47,"EXTRA22":22}
assert {x["candidate_id"] for x in v}<={x["candidate_id"] for x in c}
assert all(x["real_independent_V3"]=="NOT_RUN" for x in v)
t=rd("gates/V13_96_ORIGINAL_STAGE0_20_ROUTING.tsv")
assert len(t)==len({x["old_task_id"] for x in t})==20
assert Counter(x["book"] for x in t)=={"wanming":10,"tiexuecanming":10}
assert {"WM-T05","WM-T09"} <= {x["old_task_id"] for x in t}
assert all(x["full_independent_acceptance"]=="NOT_RUN" for x in t)
s=json.loads((P/"V13_CURRENT_V3.json").read_text(encoding="utf-8"))
assert s["overall_management_units_total"]==96 and s["overall_management_units_completed"]==75
assert s["current_batch"]=="B076" and s["batch_status"]=="BLOCKED" and s["last_passed_batch"]=="B075"
assert s["b076_decisions"]["verified"]==s["skill_certified_count"]==0
assert s["b076_decisions"]["reference"]==108 and s["b076_decisions"]["needs_review"]==79
assert s["b076_unified_scheduling_only_no_new_round"] is True
print("PASS 96 original administrative rounds, 44 original contracts, full issue 426, candidate 187, V3 69, Stage0 20: no promotion")
