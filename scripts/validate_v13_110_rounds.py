#!/usr/bin/env python3
"""V13 v13.1 plan integrity only. No literary/source/skill utility certification."""
import csv,json,re
from pathlib import Path
P=Path(__file__).resolve().parents[1]
def check(test,message):
 if not test:raise AssertionError(message)
def read_tsv(filename):
 with (P/filename).open(encoding="utf-8",newline="") as f:return list(csv.DictReader(f,delimiter="\t"))
def read_csv(filename):
 with (P/filename).open(encoding="utf-8",newline="") as f:return list(csv.DictReader(f))
cur=json.loads((P/"V13_CURRENT_V2.json").read_text(encoding="utf-8"))
plan=json.loads((P/"V13_REVISED_110_ROUNDS.json").read_text(encoding="utf-8"))
rows=read_csv("V13_LEDGER_V2.csv")
old=read_csv("ROUND_LEDGER.csv")
oldcur=json.loads((P/"CURRENT_ROUND.json").read_text(encoding="utf-8"))
remap=read_tsv("V13_ROUND_REMAP_V2.tsv")
scope=read_tsv("V13_WORK_ITEM_ROUTING_V2.tsv")
v1=read_tsv("gates/R057_REPAIR_V1_39_QUEUE.tsv")
v2=read_tsv("gates/R057_REPAIR_V2_11_TEST_DESIGNS.tsv")
v3=read_tsv("gates/R057_REPAIR_V3_47_TEST_QUEUE.tsv")
legacy=read_tsv("gates/R057_LEGACY_QUARANTINE.tsv")
tasks=read_tsv("gates/R057_TASK_COVERAGE.tsv")
batches=read_tsv("V13_V3_47_BATCH_MAP.tsv")
IDs=["R%03d"%i for i in range(1,111)]
check(plan["version"]==cur["plan_version"]=="v13.1-rebased-110","version")
check(plan["total_rounds"]==cur["rounds_total"]==110,"total")
check(len(plan["rounds"])==len(rows)==110 and [x["id"] for x in plan["rounds"]]==[x["id"] for x in rows]==IDs,"unique ordered rounds")
check(cur["current_round"]=="R057" and cur["round_status"]=="NOT_STARTED" and cur["rounds_completed"]==56 and cur["last_passed_round"]=="R056","new cursor incorrectly changed")
check([x["status"] for x in rows]==["PASSED"]*56+["NOT_STARTED"]*54,"new ledger fake PASS")
check(all(x["status"]=="PASSED" for x in old[:56]) and len(old)==89 and old[56]["id"]=="R057" and old[56]["status"]=="BLOCKED","historic 89 immutable pass ledger")
check(oldcur["current_round"]=="R057" and oldcur["rounds_completed"]==56 and oldcur["round_status"]=="BLOCKED" and oldcur.get("superseded_by_cursor")=="V13_CURRENT_V2.json","old snapshot not correctly archived")
check(cur["skill_certified_count"]==0 and cur["heldout_bank_status"]=="SEALED_NOT_RUN" and cur["v3_full47_completed"]==0,"fabricated cert")
for n in range(1,57):
 check(plan["rounds"][n-1]["old_id"]==IDs[n-1] and rows[n-1]["legacy_round"]==IDs[n-1],"historic mapping")
for n in range(57,78):
 check(plan["rounds"][n-1]["old_id"]=="NEW" and rows[n-1]["legacy_round"]=="NEW","added round mapping")
for n in range(78,111):
 original="R%03d"%(n-21)
 check(plan["rounds"][n-1]["old_id"]==original and rows[n-1]["legacy_round"]==original,"future remap")
check(len(remap)==110 and len(set(x["new_id"] for x in remap))==110,"remap lost/duplicated")
check({x["old_id"] for x in remap if x["old_id"]!="NEW"}=={"R%03d"%i for i in range(1,90)},"old rounds missing")
check(len(v1)==39 and sum(x["book"]=="wanming" for x in v1)==23 and sum(x["book"]=="tiexuecanming" for x in v1)==16,"V1 review coverage")
check(len(v2)==11 and sum(x["book"]=="wanming" for x in v2)==5 and sum(x["book"]=="tiexuecanming" for x in v2)==6,"V2 not tested coverage")
check(len(v3)==47 and sum(x["book"]=="wanming" for x in v3)==21 and sum(x["book"]=="tiexuecanming" for x in v3)==26,"V3 eligible coverage")
check(len(legacy)==14 and sum(x["book_slug"]=="wanming" for x in legacy)==7 and sum(x["book_slug"]=="tiexuecanming" for x in legacy)==7,"old quarantines")
check(len(tasks)==19,"Stage0 task count")
keys={kind:{x["original_id"] for x in scope if x["work_id"].startswith(kind+":")} for kind in ("LEGACY","V1","V2","V3","TASK","STAGE0")}
check(len(scope)==148 and len({x["work_id"] for x in scope})==148,"work items 18+14+39+11+47+19")
check(keys["STAGE0"]=={"R%03d"%i for i in range(7,25)},"Stage0 risk rounds not covered")
check(keys["LEGACY"]=={x["legacy_claim_id"] for x in legacy},"legacy ID lost")
check(keys["V1"]=={x["candidate_id"] for x in v1},"V1 ID lost")
check(keys["V2"]=={x["candidate_id"] for x in v2},"V2 ID lost")
check(keys["V3"]=={x["candidate_id"] for x in v3},"V3 ID lost")
check(keys["TASK"]=={x["task_id"] for x in tasks},"Stage0 task lost")
check(len(batches)==47 and {x["candidate_id"] for x in batches}==keys["V3"],"47 V3 batches not exact")
counts={roundid:sum(x["round"]==roundid for x in batches) for roundid in ("R068","R069","R070","R071","R072","R073","R074")}
check([counts[x] for x in counts]==[7,7,7,7,7,6,6],"V3 47 batches count")
check(all(x["status"]=="NOT_RUN_NEW_TEST" for x in batches),"V3 false execution")
for x in plan["rounds"][56:]:
 check(x.get("actions") and x.get("pass_condition") and x.get("deliverable"),"missing per-round full contract "+x["id"])
check((P/"V13_REVISED_110_ROUNDS.md").exists(),"human readable plan missing")
print("V13 v13.1 PLAN STRUCTURE PASS: 110 ordered; old 56 PASSED; 21 inserted; 33 remapped; 148 routed items incl 47 individual V3; zero false pass.")
