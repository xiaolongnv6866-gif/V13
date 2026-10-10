#!/usr/bin/env python3
"""R063 archival ID, source anchor and conservative V1-only gate validation.
Public CI cannot see copyright EPUB or judge literary quality; hashes can be privately recalculated.
"""
import csv,json,re
from pathlib import Path
P=Path(__file__).resolve().parents[1]
def tab(p):
 with (P/p).open(encoding="utf-8",newline="") as f:return list(csv.DictReader(f,delimiter="\t"))
frozen=[x for x in tab("gates/R057_REPAIR_V1_39_QUEUE.tsv") if x["book"]=="wanming"]
arch={x["candidate_id"]:x for x in tab("books/wanming/validation/V1_EVIDENCE.tsv")}
r=tab("v2/v1/WANMING_23_RESULTS.tsv")
assert len(r)==len(frozen)==23 and [x["candidate_id"] for x in r]==[x["candidate_id"] for x in frozen]
assert len({x["candidate_id"] for x in r})==23
count={}
for x,old in zip(r,frozen):
 k=x["candidate_id"];prev=arch[k]
 assert x["original_id"]==old["original_id"] and x["extractor_type"]==old["extractor_type"]
 assert x["original_loci"]==old["original_source_loci"] and x["old_V1_reason"]==old["R054_V1_reason"]
 assert x["old_V1"]==prev["V1"]=="REVIEW" and x["primary_original_paragraph_sha256"]==prev["primary_paragraph_sha256"]
 sample=x["R063_new_secondary_paragraph_SHA256"];m=re.fullmatch(r"n(\d{3})/p(\d+):([0-9a-f]{64})",sample)
 assert m and f"n{m[1]}/p{m[2]}" in x["original_loci"],(k,sample)
 assert len(x["reviewed_original_scene"])>=12 and len(x["limiting_counterexample"])>=10 and len(x["bounded_V1_scope"])>=10
 assert x["source_status_A"]=="EPUB_SHA_ZIPCRC_AND_71_LOCATOR_PRIVATE_REAUDIT"
 assert x["V2"]==x["V3"]=="NOT_TESTED" and x["independent_C"]=="NOT_RUN"
 assert x["R063_V1_result"] in ("PASS_NARROW","REFERENCE","REVIEW")
 if x["R063_V1_result"]=="PASS_NARROW": assert x["next_gate"]=="R065_NEW_V1_SCOPED_ELIGIBLE"
 else:assert x["next_gate"]=="R078_REFERENCE_OR_NEEDS_REVIEW"
 count[x["R063_V1_result"]]=count.get(x["R063_V1_result"],0)+1
assert count=={"PASS_NARROW":5,"REFERENCE":10,"REVIEW":8},count
cur=json.loads((P/"V13_CURRENT_V2.json").read_text(encoding="utf-8"))
assert cur["rounds_completed"]>=62 and cur["skill_certified_count"]==0 and cur["v3_full47_completed"]==0 and cur["heldout_bank_status"]=="SEALED_NOT_RUN"
print("R063 SOURCE-STRUCTURE PASS: 23/23 original V1 REVIEW; 5 narrow V1-only, 10 reference, 8 REVIEW. No false Skill/V2/V3/C promotion.")
