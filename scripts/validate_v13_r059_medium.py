#!/usr/bin/env python3
"""R059 source provenance + bounded quality-debt routing, not a literary or Skill certification."""
import csv,json,re
from pathlib import Path
P=Path(__file__).resolve().parents[1]
def require(c,m):
 if not c:raise AssertionError(m)
def rows(p):
 with (P/p).open(encoding="utf-8",newline="") as f:return list(csv.DictReader(f,delimiter="\t"))
def obj(p):return json.loads((P/p).read_text(encoding="utf-8"))
rounds=[7,16,18,19,20,21,22,23,24]
claims={}
by_round={}
for n in rounds:
 r=f"R{n:03d}"
 path=P/"cangjie"/"reading"/r/(("wanming" if n%2 else "tiexue")+"_receipts.jsonl")
 original=[json.loads(s) for s in path.read_text(encoding="utf-8").splitlines() if s.strip()]
 require(len(original)==40,r+" archived reading receipts incomplete")
 key=[]
 for item in original:
  for claim in item.get("mechanism_claims",[]):
   id_="STAGE0:"+r+":"+claim["claim_id"]
   require(id_ not in claims,"duplicate original claim "+id_)
   claims[id_]=(item,claim)
   key.append(id_)
 by_round[r]=set(key)
require(len(claims)==166,"old medium/repaired rounds total must be 166")
require([len(by_round[f"R{n:03d}"]) for n in rounds]==[6,20,20,20,20,20,20,20,20],"old claims source counts wrong")
wm=rows("v2/stage0/R059_WANMING_21_REVIEW.tsv")
tx=rows("v2/stage0/R059_TIEXUE_40_REVIEW.tsv")
exam=wm+tx
actual_ids={x["issue_id"] for x in exam}
require(len(wm)==21 and len(tx)==40 and len(exam)==len(actual_ids)==61,"61 actual review receipts absent or duplicate")
frozen=[x for x in rows("v2/ISSUE_REGISTRY.tsv") if x["issue_type"]=="STAGE0_B_CLAIM" and x["assigned_round"]=="R059" and x["audit_sampling"]=="PRESELECTED_FOR_R058_R059"]
frozen_ids={x["issue_id"] for x in frozen}
require(len(frozen_ids)==34 and frozen_ids<=actual_ids,"R057 frozen 34 missing from R059")
require(all(x["review_class"]=="R057_FROZEN_SAMPLE" for x in exam if x["issue_id"] in frozen_ids),"pre-registered reviews mislabeled")
require(actual_ids>=by_round["R007"] and actual_ids>=by_round["R024"],"all previously repaired 6+20 original IDs required")
extra_ids=actual_ids-frozen_ids
require(len(extra_ids)==27,"must be 34 prereg + 27 extra = 61")
require(len((by_round["R007"]|by_round["R024"])-frozen_ids)==20,"fixed R007/R024 extra repair coverage")
for n in [16,18,19,20,21,22,23]:
 r=f"R{n:03d}"
 subset=extra_ids&by_round[r]
 require(len(subset)==1,"must expand one sample in "+r)
for x in exam:
 id_=x["issue_id"]
 require(id_ in claims,id_+" is not an original claim")
 orig,c=claims[id_]
 require(x["source_round"] in by_round and id_ in by_round[x["source_round"]],id_+" source-round identity wrong")
 require(x["claim_id"]==c["claim_id"] and str(orig["narrative_ordinal"])==str(x["narrative_ordinal"]),id_+" claim ID or narrative ordinal drift")
 require(x["book"]==orig["book_slug"] and x["original_source_path"]==orig["epub_path"],id_+" source EPUB chapter wrong")
 require(x["source_chapter_sha256"]==orig["chapter_sha256"],id_+" archived chapter SHA wrong")
 require(set(filter(None,x["original_support_ids"].split(";")))==set(c["support_anchor_ids"]),id_+" old support SHA locator IDs wrong")
 require(bool(x["scene_specific_finding"] and x["counterexample_or_limit"] and x["result_status"] and x["next_gate"]),id_+" missing substantive review")
 require(x["next_gate"].startswith("R06"),id_+" not routed to existing R060-R062")
 for region in x["reviewed_loci"].split(";"):
  m=re.fullmatch(r"(\d+)(?:-(\d+))?",region)
  require(m is not None,id_+" malformed scene locus "+region)
  a=int(m[1]);b=int(m[2] or m[1])
  require(1<=a<=b<=orig["body_paragraph_count"],id_+" locus outside XHTML text")
 require("VERIFIED" not in x["result_status"] and "V1_PASS" not in x["result_status"],id_+" B audit cannot promote")
oldq={x["legacy_claim_id"] for x in rows("gates/R057_LEGACY_QUARANTINE.tsv")}
overlaps=[x for x in exam if x["claim_id"] in oldq]
require(len(overlaps)==7,"7 R042-medium legacy claims absent")
require(all("LEGACY" in x["result_status"] and ("R060" in x["next_gate"] or "R061" in x["next_gate"]) for x in overlaps),"old quarantine wrongly removed")
sha=rows("v2/stage0/R059_PREVIOUS_REPAIRS_26_PRIVATE_SHA.tsv")
require(len(sha)==26 and len({(x["book"],x["narrative_ordinal"]) for x in sha})==26,"prior repairs need 26 distinct paragraph SHA")
r007={str(claims[id_][0]["narrative_ordinal"]) for id_ in by_round["R007"]}
r024={str(claims[id_][0]["narrative_ordinal"]) for id_ in by_round["R024"]}
require({x["narrative_ordinal"] for x in sha if x["book"]=="wanming"}==r007,"six R007 repairs not reanchored")
require({x["narrative_ordinal"] for x in sha if x["book"]=="tiexuecanming"}==r024,"twenty R024 repairs not reanchored")
for x in sha:
 require(re.fullmatch("[0-9a-f]{64}",x["private_source_paragraph_sha256"]),"bad rechecked SHA")
 matched=[c for (r,c) in claims.values() if r["book_slug"]==x["book"] and str(r["narrative_ordinal"])==x["narrative_ordinal"]]
 require(len(matched)==1,"new SHA has no original claim")
 # CI does not have user private EPUB bytes; hashes are not independent source-content proof.
 require(1<=int(x["paragraph_index"])<=next(r["body_paragraph_count"] for (r,c) in claims.values() if r["book_slug"]==x["book"] and str(r["narrative_ordinal"])==x["narrative_ordinal"]),"alternate hash paragraph outside original chapter")
 require(x["status"]=="SUPPORT_LOCUS_CANDIDATE_REVIEW_ONLY_NOT_CERTIFIED","SHA incorrectly promoted")
live=rows("v2/stage0/STAGE0_B_AUDIT_STATUS_V2.tsv")
asserted=rows("v2/ISSUE_REGISTRY.tsv")
all_b={x["issue_id"] for x in asserted if x["issue_type"]=="STAGE0_B_CLAIM"}
require(len(all_b)==296 and len(live)==296 and len({x["issue_id"] for x in live})==296,"296 current literary B statuses exact")
require({x["issue_id"] for x in live}==all_b,"living B audit index differs from R057 frozen source registry")
all_r058={x["issue_id"] for x in rows("v2/stage0/R058_WM_24_DECISIONS.tsv")+rows("v2/stage0/R058_TX_19_DECISIONS.tsv")}
require(len(all_r058)==43 and all_r058.isdisjoint(actual_ids),"R058 and R059 must remain disjoint")
require({x["issue_id"] for x in live if x["review_state"]=="REVIEWED_R058"}==all_r058,"R058 living record drift")
require({x["issue_id"] for x in live if x["review_state"]=="REVIEWED_R059"}==actual_ids,"R059 living record drift")
require(sum(x["review_state"]=="B_PROVISIONAL_NOT_REAUDITED" for x in live)==192,"must explicitly retain 192 untouched B claims")
require({x["origin_id"] for x in live if x["R042_quarantine"].startswith("NO_DIRECT_PROMOTION")}==oldq,"14 quarantined original claims lost")
require(all(x["execution_truth"]=="NO_B_VERIFIED_NO_C_OR_SKILL" for x in live),"historical B or C certification fabricated")
doc=(P/"v2/stage0/MEDIUM_REPAIRED_SOURCE_AUDIT.md").read_text(encoding="utf-8")
rec=(P/"runs/R059_V2.md").read_text(encoding="utf-8")
require("61/166" in doc and "105/166" in doc and "61/166" in rec,"must disclose 105 unreviewed B records")
cur=obj("V13_CURRENT_V2.json")
require(cur["rounds_total"]==110 and cur["rounds_completed"]>=58,"V2 cursor wrong")
if cur["rounds_completed"]==58:
 require(cur["current_round"]=="R059" and cur["round_status"]=="NOT_STARTED","R059 has not actually passed")
elif cur["rounds_completed"]>=59:
 require(cur["last_passed_round"]>="R059","R059 PASS status missing")
if cur["rounds_completed"]<=59:
 require(cur["skill_certified_count"]==0 and cur["heldout_bank_status"]=="SEALED_NOT_RUN" and cur["v3_full47_completed"]==0,"R059 did not certify Skills or open heldout")
print("R059 STRUCTURAL PASS: source 9 old rounds / 166 old claims, 34 prereg + 27 new=61 audits, all R007 six + R024 twenty rechecked, seven quarantine preserved, 105 B unresolved.")
