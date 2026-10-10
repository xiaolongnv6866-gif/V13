#!/usr/bin/env python3
"""V13 v13.1 R057 forensic inventory validator (STRUCTURAL; not semantic B/C certification)."""
import csv,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def ensure(cond,message):
    if not cond: raise AssertionError(message)
def rows(path,delim="\t"):
    with (ROOT/path).open(encoding="utf-8",newline="") as f:
        return list(csv.DictReader(f,delimiter=delim))
def j(path):return json.loads((ROOT/path).read_text(encoding="utf-8"))
claims=[]
for n in range(7,25):
    id_="R%03d"%n
    kind="wanming" if n%2 else "tiexue"
    path="cangjie/reading/"+id_+"/"+kind+"_receipts.jsonl"
    objects=[json.loads(s) for s in (ROOT/path).read_text(encoding="utf-8").splitlines() if s.strip()]
    ensure(len(objects)==40,id_+" chapter receipts incomplete")
    for obj in objects:
        for c in obj.get("mechanism_claims",[]):
            claims.append((id_,obj,c,path))
ensure(len(claims)==296,"actual R007-R024 claims must be 296")
ensure(len({(r,c["claim_id"]) for r,o,c,p in claims})==296,"duplicate original claim ID")
ensure(all(c["counterexample_status"]=="SEARCHED_NONE" for r,o,c,p in claims),"counterexample status must be read honestly")
src_wm="a8f3b43dcd496822cd384ac8e9aa85f7dc374f8430f06c6f8321c26825093082"
src_tx="9100bbcdb9f52bcd5458cbda92e16b646489efbc00df5161ed568ebac83ffbaf"
for r,o,c,p in claims:
    ensure(o["source_epub_sha256"]==(src_wm if o["book_slug"]=="wanming" else src_tx),r+" original source hash mismatch")
    ensure(bool(c.get("support_anchor_ids")),r+" claim lacks any support anchor")
    anchors={v["anchor_id"] for v in o["anchors"]}
    ensure(set(c["support_anchor_ids"]).issubset(anchors),r+" support IDs not found")
historical=rows("v2/stage0/LEGACY_R007_CLAIMS.tsv")+rows("v2/stage0/LEGACY_WM_R009_R023_144.tsv")+rows("v2/stage0/LEGACY_TX_R008_R024_146.tsv")
ensure(len(historical)==296,"frozen claims count mismatch")
hmap={}
for x in historical:
    item=x.get("issue_id") or x.get("record_id")
    ensure(item not in hmap,"duplicate frozen item")
    hmap[item]=x
for round_,o,c,path in claims:
    name="STAGE0:"+round_+":"+c["claim_id"]
    ensure(name in hmap,name+" missing")
    frozen=hmap[name]
    ensure((frozen.get("source_round") or "")==round_,name+" wrong round")
    ensure(frozen["claim_id"]==c["claim_id"],name+" wrong claim ID")
    ensure(str(frozen.get("narrative_ordinal") or frozen.get("ordinal"))==str(o["narrative_ordinal"]),name+" ordinal drift")
    ensure(frozen["epub_path"]==o["epub_path"] if "epub_path" in frozen else frozen.get("original_epub_path")==o["epub_path"],name+" source path drift")
    if frozen.get("chapter_sha256"):
        ensure(frozen["chapter_sha256"]==o["chapter_sha256"],name+" original chapter SHA drift")
    if frozen.get("original_epub_sha256"):
        ensure(frozen["original_epub_sha256"]==o["source_epub_sha256"],name+" original book SHA drift")
    loc=frozen.get("support_anchor_ids") or frozen.get("anchor_ids")
    ensure(set(loc.split(";"))==set(c["support_anchor_ids"]),name+" support anchor drift")
    ensure(frozen["counterexample_status"]==c["counterexample_status"],name+" counterexample misread")
v1=rows("gates/R057_REPAIR_V1_39_QUEUE.tsv")
v2=rows("gates/R057_REPAIR_V2_11_TEST_DESIGNS.tsv")
v3=rows("gates/R057_REPAIR_V3_47_TEST_QUEUE.tsv")
q=rows("gates/R057_LEGACY_QUARANTINE.tsv")
t=rows("gates/R057_TASK_COVERAGE.tsv")
batches=rows("V13_V3_47_BATCH_MAP.tsv")
registry=rows("v2/ISSUE_REGISTRY.tsv")
baseline=j("v2/BASELINE_LOCK.json")
counts={"STAGE0_B_CLAIM":296,"LEGACY_R042_QUARANTINE":14,"V1_SOURCE_REVIEW":39,"V2_EXECUTABILITY_NOT_TESTED":11,"V3_NO_GAIN_PROVEN":47,"STAGE0_TASK_COVERAGE":19}
ensure(len(registry)==426 and len({x["issue_id"] for x in registry})==426,"426 issue IDs not unique")
ensure({k:sum(x["issue_type"]==k for x in registry) for k in counts}==counts,"issue type counts wrong")
ensure({x["issue_id"] for x in registry if x["issue_type"]=="STAGE0_B_CLAIM"}==set(hmap),"Stage0 claims not all routed")
ensure({x["origin_id"] for x in registry if x["issue_type"]=="LEGACY_R042_QUARANTINE"}=={x["legacy_claim_id"] for x in q},"14 legacy IDs missing")
ensure({x["origin_id"] for x in registry if x["issue_type"]=="V1_SOURCE_REVIEW"}=={x["candidate_id"] for x in v1},"39 V1 IDs missing")
ensure({x["origin_id"] for x in registry if x["issue_type"]=="V2_EXECUTABILITY_NOT_TESTED"}=={x["candidate_id"] for x in v2},"11 V2 IDs missing")
ensure({x["origin_id"] for x in registry if x["issue_type"]=="V3_NO_GAIN_PROVEN"}=={x["candidate_id"] for x in v3},"47 V3 IDs missing")
ensure({x["origin_id"] for x in registry if x["issue_type"]=="STAGE0_TASK_COVERAGE"}=={x["task_id"] for x in t},"19 tasks missing")
ensure(len(v1)==39 and sum(x["book"]=="wanming" for x in v1)==23 and sum(x["book"]=="tiexuecanming" for x in v1)==16,"V1 split")
ensure(len(v2)==11 and sum(x["book"]=="wanming" for x in v2)==5 and sum(x["book"]=="tiexuecanming" for x in v2)==6,"V2 split")
ensure(len(v3)==47 and sum(x["book"]=="wanming" for x in v3)==21 and sum(x["book"]=="tiexuecanming" for x in v3)==26,"V3 split")
ensure(len(q)==14 and sum(x["book_slug"]=="wanming" for x in q)==7 and sum(x["book_slug"]=="tiexuecanming" for x in q)==7,"legacy split")
ensure(len(t)==19 and len({x["task_id"] for x in t})==19,"Stage0 19")
ensure(len(batches)==47 and {x["candidate_id"] for x in batches}=={x["candidate_id"] for x in v3},"V3 mapping")
bcounts={r:sum(x["round"]==r for x in batches) for r in ("R068","R069","R070","R071","R072","R073","R074")}
ensure(list(bcounts.values())==[7,7,7,7,7,6,6],"V3 batches not full")
ensure(all(x["execution_state"]=="FROZEN_NOT_EXECUTED" and x["decision"]=="PENDING_EVIDENCE" for x in registry),"incorrectly passed an unresolved issue")
chosen=[x for x in registry if x["issue_type"]=="STAGE0_B_CLAIM" and x["audit_sampling"]=="PRESELECTED_FOR_R058_R059"]
ensure(len(chosen)==68 and sum(x["assigned_round"]=="R058" for x in chosen)==34 and sum(x["assigned_round"]=="R059" for x in chosen)==34,"68 prereg samples not fixed")
old_ranges={n:[(r,o,c) for r,o,c,p in claims if r==n] for n in ("R%03d"%i for i in range(7,25))}
selected={x["issue_id"] for x in chosen}
for n,items in old_ranges.items():
    for i in {0,(len(items)-1)//2,len(items)-1}:
        ensure("STAGE0:"+n+":"+items[i][2]["claim_id"] in selected,n+" missing first/middle/last")
for x in q:
    overlap=[z for z in claims if z[2]["claim_id"]==x["legacy_claim_id"]]
    ensure(len(overlap)==1,x["legacy_claim_id"]+" legacy old receipt missing")
    r,o,c,p=overlap[0]
    ensure("STAGE0:"+r+":"+c["claim_id"] in selected,"legacy special sampling absent")
ensure(baseline["issues"]["total"]==426 and baseline["issues"]["old_stage0"]["total"]==296,"baseline counts")
ensure(baseline["sampling_contract"]["preselected_unique_claims"]==68,"baseline selection drift")
ensure(baseline["v3_evaluation_contract"]["scope_count"]==47 and set(baseline["v3_evaluation_contract"]["scope"])=={x["candidate_id"] for x in v3},"baseline V3 scope")
ensure(baseline["v3_evaluation_contract"]["actual_new_tests_complete"]==0,"fabricated V3 result")
cur=j("V13_CURRENT_V2.json")
ledger=rows("V13_LEDGER_V2.csv",",")
ensure(len(ledger)==110,"new plan ledger")
ensure(cur["rounds_total"]==110,"plan cursor total drift")
if cur["rounds_completed"]<=57:
    ensure(cur["skill_certified_count"]==0 and cur["heldout_bank_status"]=="SEALED_NOT_RUN","R057 must not claim certified skill or released tests")
if cur["rounds_completed"]==56:
    ensure(cur["current_round"]=="R057" and cur["round_status"]=="NOT_STARTED" and ledger[56]["status"]=="NOT_STARTED","unexpected prereg state")
elif cur["rounds_completed"]>=57:
    ensure(ledger[56]["status"]=="PASSED" and cur["last_passed_round"]>="R057","R057 not passed but cursor advanced")
else:raise AssertionError("completion rolled back")
print("V13 R057 STRUCTURAL FREEZE PASS: original 296 claims matched to JSONL; 426 issues, 68 preselected; 14+39+11+47+19 intact, R057 source-only scope, 0 certified.")
