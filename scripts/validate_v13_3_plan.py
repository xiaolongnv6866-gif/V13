#!/usr/bin/env python3
"""V13.3 source-of-truth integrity: identities and contracts only, not literary pass."""
import csv,json,re,hashlib
from pathlib import Path
from collections import Counter
P=Path(__file__).resolve().parents[1]
def rd(f):
 with (P/f).open(encoding="utf-8",newline="") as h:return list(csv.DictReader(h,delimiter="\t"))
s=json.loads((P/"V13_CURRENT_V4.json").read_text(encoding="utf-8"))
assert s["total_new_rounds"]==48 and s["historical_completed_admin"]==75
assert isinstance(s["completed_new_rounds"],int) and 0<=s["completed_new_rounds"]<=48
b=json.loads((P/"V13_CURRENT_V3.json").read_text(encoding="utf-8"))
assert b["overall_management_units_completed"]==75 and b["current_batch"]=="B076"
n=rd("V13_LEDGER_V4.tsv")
assert len(n)==48 and [x["round_id"] for x in n]==["N"+str(i).zfill(2) for i in range(1,49)]
assert all(x["acceptance"] and x["status"] in {"NOT_STARTED","IN_PROGRESS","BLOCKED","FAILED","PASSED"} for x in n)
done=s["completed_new_rounds"]
assert all(x["status"]=="PASSED" for x in n[:done])
assert all(x["status"]=="NOT_STARTED" for x in n[done+1:])
if done<48: assert n[done]["status"]!="PASSED"
current_idx=min(done,47)
assert (s["current_round"],s["current_round_status"])==(n[current_idx]["round_id"],n[current_idx]["status"])
if done==0 and n[0]["status"]=="NOT_STARTED":
 assert s["actual_N01_work_started"] is False
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
if current_idx<20:
 assert all(x["actual_independent_result"]=="NOT_RUN" and x["creator"]=="UNASSIGNED" for x in v)
assert {x["candidate_id"] for x in v} <= {x["candidate_id"] for x in c}
o=rd("V13_3_STAGE0_20_TO_ROUNDS.tsv")
assert len(o)==20 and len({x["old_task_id"] for x in o})==20
assert Counter(x["original_full_C_round"] for x in o)=={"N26":10,"N27":10}
assert {"WM-T05","WM-T09"} <= {x["old_task_id"] for x in o}
if current_idx<25:
 assert all(x["truly_independent_C"]=="NOT_RUN" for x in o)
m=rd("V13_3_ORIGINAL_44_CONTRACTS_MAP.tsv")
assert len(m)==44 and {x["original_contract"] for x in m}=={"R"+str(i).zfill(3) for i in range(67,111)}
assert all(x["original_required_actions"] and x["original_required_files"] and x["original_acceptance"] and x["do_not_delete"]=="TRUE" for x in m)
assert all(q in {x["round_id"] for x in n} for x in m for q in x["new_rounds"].split(";"))
assert all(isinstance(s[k],int) and s[k]>=0 for k in ("verified","reference","needs_review","rejected","certified_skills"))
assert sum(s[k] for k in ("verified","reference","needs_review","rejected"))==187

# Active source correction, preserving frozen historical registries unchanged.
z=rd("V13_3_SOURCE_RESOLUTION_296.tsv")
assert len(z)==296 and len({x["issue_id"] for x in z})==296
by_legacy={x["issue_id"]:x for x in f}
by_resolution={x["issue_id"]:x for x in z}
receipt_cache={}
for claim in (row for row in a if row["issue_type"]=="STAGE0_B_CLAIM"):
 round_code=claim["original_source_round"]
 is_wm=int(round_code[1:])%2==1
 book="wanming" if is_wm else "tiexuecanming"
 filename="wanming_receipts.jsonl" if is_wm else "tiexue_receipts.jsonl"
 expected="cangjie/reading/"+round_code+"/"+filename
 assert claim["source"]==expected,claim["issue_id"]
 r=by_resolution[claim["issue_id"]]
 assert r["original_source_round"]==round_code and r["book"]==book
 assert r["corrected_receipt_source"]==expected
 assert r["frozen_registry_source"]==by_legacy[claim["issue_id"]]["original_source"]
 assert r["frozen_registry_anchor"]==by_legacy[claim["issue_id"]]["source_anchor"]
 assert r["verification_scope"]=="LOCATOR_VERIFIED_ONLY_B_PROVISIONAL"
 if expected not in receipt_cache:
  blob=(P/expected).read_bytes()
  object_sha=hashlib.sha1(("blob "+str(len(blob))+"\\0").encode().replace(b"\\0",b"\\x00")+blob).hexdigest()
  lines=[json.loads(line) for line in blob.decode("utf-8").splitlines() if line.strip()]
  receipt_cache[expected]=(object_sha,{int(p["narrative_ordinal"]):p for p in lines})
 sha,chapters=receipt_cache[expected]
 assert r["receipt_git_blob_sha"]==sha
 chapter=chapters.get(int(r["resolved_ordinal"]))
 assert chapter and chapter["book_slug"]==book
 recorded={t["anchor_id"] for t in chapter["anchors"]}
 assert all(t in recorded for t in r["resolved_anchor_ids"].split(";"))
 assert r["resolved_locator"]=="n"+r["resolved_ordinal"]+"/"+r["resolved_anchor_ids"]

# Candidate Markdown anchors must exist, not just their destination file.
for candidate in c:
 p,anchor=candidate["old_reference_path"].split("#",1)
 doc=(P/p).read_text(encoding="utf-8")
 assert any(line.startswith("##") and line.lstrip("# ").split(" ")[0].casefold()==anchor.casefold()
            for line in doc.splitlines()),candidate["candidate_id"]
print("PASS V13.3 sequential 48-round progress, 426 original issues, 296 source+anchors, 187 candidate links, 69 V3, 20 tasks, 44 contracts. Not literary or independent-method PASS.")
