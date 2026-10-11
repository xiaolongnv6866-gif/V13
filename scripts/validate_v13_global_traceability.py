#!/usr/bin/env python3
"""Entire historical V13 evidence crosswalk. STRUCTURE ONLY, not independent literary certification."""
import csv, json, re
from collections import Counter
from pathlib import Path
P=Path(__file__).resolve().parents[1]
def tsv(path):
    with (P/path).open(encoding="utf-8", newline="") as f:return list(csv.DictReader(f, delimiter="\t"))
data=tsv("V13_GLOBAL_TRACEABILITY_1058.tsv")
want={"89_PLAN":89,"110_PLAN":110,"96_BATCH":30,"48_PLAN":48,"ISSUE_426":426,"CANDIDATE_187":187,"V3_69":69,"STAGE0_C20":20,"CONTRACT_44":44,"SKILL_DUTY_35":35}
got=Counter(x["family"] for x in data)
assert len(data)==1058 and got==want,(len(data),got)
assert len({(x["family"],x["version_scoped_id"]) for x in data})==1058
def by(group):return {x["version_scoped_id"]:x for x in data if x["family"]==group}
def require_same(g,key,ids):
    actual=set(by(g))
    assert actual==set(ids),(g,"missing",sorted(set(ids)-actual)[:5],"unexpected",sorted(actual-set(ids))[:5])
for x in data:
    assert x["canonical_source"] and x["remaining_package"] and x["mandatory_disposition"]
    for part in x["remaining_package"].split("+"):
        assert part=="HISTORY" or part in {f"W{i:02d}" for i in range(1,12)},(x["version_scoped_id"],part)
r89=by("89_PLAN");r110=by("110_PLAN");b=by("96_BATCH");n=by("48_PLAN")
require_same("89_PLAN",None,[f"R{i:03d}@v13.0" for i in range(1,90)])
require_same("110_PLAN",None,[f"R{i:03d}@v13.1" for i in range(1,111)])
require_same("96_BATCH",None,[f"B{i:03d}@v13.2" for i in range(67,97)])
require_same("48_PLAN",None,[f"N{i:02d}@v13.3" for i in range(1,49)])
renumbered=0
for oid,x in r89.items():
    m=re.search(r"semantic_to_v13.1=(R\d{3});(.*)",x["trace_note"])
    assert m,oid
    new_id,title=m.groups()
    newer=r110.get(new_id+"@v13.1")
    assert newer is not None,(oid,new_id)
    # historical titles shifted; one old R057 wording differs from revised R078
    assert title==newer["trace_note"] or oid=="R057@v13.0",(oid,new_id)
    if oid.split("@")[0]!=new_id:renumbered+=1
assert renumbered==32,renumbered
assert sum(x["observed_status"]=="PASSED" for x in r89.values())==56
assert r89["R057@v13.0"]["observed_status"]=="BLOCKED"
assert sum(x["observed_status"]=="PASSED" for x in b.values())==9
assert b["B076@v13.2"]["observed_status"]=="BLOCKED"
assert sum(x["observed_status"]=="PASSED" for x in n.values())==20
assert n["N21@v13.3"]["observed_status"]=="NOT_STARTED"
root=json.loads((P/"V13_CURRENT_V4.json").read_text(encoding="utf-8"))
assert root["current_round"]=="N21" and root["completed_new_rounds"]==20
plan=(P/"V13_REVISED_110_ROUNDS.md").read_text(encoding="utf-8")
p110=re.findall(r"(?m)^\|R(\d{3})\|",plan)
assert len(p110)==110 and p110==[f"{i:03d}" for i in range(1,111)]
ledger=tsv("V13_LEDGER_V4.tsv")
assert len(ledger)==48
assert {x["round_id"]+"@v13.3" for x in ledger}==set(n)
for x in ledger:
    assert n[x["round_id"]+"@v13.3"]["observed_status"]==x["status"]
original=tsv("V13_3_ISSUES_426_TO_ROUNDS.tsv")
require_same("ISSUE_426",None,[x["issue_id"] for x in original])
src=tsv("v13_3/n16/N16_LITERARY_B_296_MASTER.tsv")
assert Counter(x["disposition_class"] for x in src)=={"SCOPED_LITERARY_B_ONLY":243,"REJECT_OLD_STRONG_CLAIM":53}
source_by_id={x["issue_id"]:x for x in src}
for x in original:
    if x["issue_type"]=="STAGE0_B_CLAIM":
        assert by("ISSUE_426")[x["issue_id"]]["observed_status"]==source_by_id[x["issue_id"]]["disposition_class"]
assert sum(x["issue_type"]=="LEGACY_R042_QUARANTINE" for x in original)==14
cand=tsv("V13_3_CANDIDATES_187_TO_ROUNDS.tsv")
require_same("CANDIDATE_187",None,[x["candidate_id"] for x in cand])
assert Counter(x["book"] for x in cand)=={"wanming":91,"tiexuecanming":96}
cmap=by("CANDIDATE_187")
status=Counter(x["trace_note"].split(";")[-1] for x in cmap.values())
assert status=={"READY_V3":57,"V2_PARTIAL":7,"NOT_V1_METHOD":123},status
v3=tsv("V13_3_V3_69_TO_ROUNDS.tsv")
require_same("V3_69",None,[x["repeat_id"] for x in v3])
vg=Counter(x["trace_note"].split(";")[-1] for x in by("V3_69").values())
assert vg=={"PRE_V3_ELIGIBLE":56,"V2_PARTIAL":5,"V1_INELIGIBLE":8},vg
assert all(x["actual_independent_result"]=="NOT_RUN" for x in v3)
c20=tsv("V13_3_STAGE0_20_TO_ROUNDS.tsv")
require_same("STAGE0_C20",None,[x["old_task_id"] for x in c20])
assert all(x["truly_independent_C"]=="NOT_RUN" for x in c20)
co=tsv("V13_3_ORIGINAL_44_CONTRACTS_MAP.tsv")
require_same("CONTRACT_44",None,[x["original_contract"]+"@v13.1" for x in co])
assert all(x["original_required_actions"] and x["original_acceptance"] and x["do_not_delete"]=="TRUE" for x in co)
duties=tsv("V13_3_FULL_SKILL_REQUIREMENTS.tsv")
require_same("SKILL_DUTY_35",None,[x["id"] for x in duties])
manifest=tsv("PROJECT_FILE_REGISTER_1101.tsv")
assert len(manifest)==1101 and Counter(x["action"] for x in manifest)=={"RETAIN_MAIN":931,"PRESERVE_BACKUP_ONLY":170}
assert (P/"V13_GLOBAL_REMAINING_WORK_V1.md").is_file()
print("PASS global traceability STRUCTURE ONLY: 1058 task records; 89->110 collision 32, manual R057; 426/187/69/20/44/35; 1101 source files; zero independent V3 or certified SKILL claimed.")
