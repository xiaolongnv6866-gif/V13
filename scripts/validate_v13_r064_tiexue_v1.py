#!/usr/bin/env python3
import csv,re,json
from pathlib import Path
P=Path(__file__).resolve().parents[1]
def read(p):
 with (P/p).open(encoding="utf8",newline="") as f:return list(csv.DictReader(f,delimiter="\t"))
q=[x for x in read("gates/R057_REPAIR_V1_39_QUEUE.tsv") if x["book"]=="tiexuecanming"]
v={x["candidate_id"]:x for x in read("books/tiexuecanming/validation/V1_EVIDENCE.tsv")}
a=read("v2/v1/TIEXUE_16_RESULTS.tsv")
assert len(q)==len(a)==16
counts={}
for src,x in zip(q,a):
 k=src["candidate_id"];old=v[k]
 assert x["candidate_id"]==k and x["old_V1"]==old["V1"]=="REVIEW"
 assert x["book"]==src["book"] and x["original_loci"]==src["original_source_loci"]
 assert x["old_R054_reason"]==src["R054_V1_reason"]
 assert x["old_primary_paragraph_SHA256"]==old["primary_paragraph_sha256"]
 assert x["epub_sha256"]==old["source_epub_sha256"]
 m=re.fullmatch(r"n(\d{3})/p(\d+):([a-f0-9]{64})",x["R064_second_paragraph_SHA256"])
 assert m and any(t.startswith("n"+m[1]+"/") for t in x["original_loci"].split(";")),k
 assert len(x["scene_facts_observed"])>10 and len(x["counterexample_or_limit"])>10
 assert x["V2_status"]==x["V3_status"]=="NOT_TESTED" and x["independent_C_status"]=="NOT_RUN"
 counts[x["R064_V1_result"]]=counts.get(x["R064_V1_result"],0)+1
assert counts=={"PASS_NARROW":6,"REFERENCE":9,"REVIEW":1},counts
z=read("v2/v1/V1_39_COMBINED_ROUTE.tsv")
w={x["candidate_id"]:x for x in read("v2/v1/WANMING_23_RESULTS.tsv")}
t={x["candidate_id"]:x for x in a}
full=read("gates/R057_REPAIR_V1_39_QUEUE.tsv")
assert len(z)==len(full)==39
for x,y in zip(z,full):
 assert x["candidate_id"]==y["candidate_id"] and x["book"]==y["book"]
 d=w[x["candidate_id"]]["R063_V1_result"] if x["book"]=="wanming" else t[x["candidate_id"]]["R064_V1_result"]
 assert x["latest_V1_disposition"]==d and x["Skill_verified"]=="NO"
assert sum(x["latest_V1_disposition"]=="PASS_NARROW" for x in z)==11
assert sum(x["latest_V1_disposition"]=="REFERENCE" for x in z)==19
assert sum(x["latest_V1_disposition"]=="REVIEW" for x in z)==9
c=json.loads((P/"V13_CURRENT_V2.json").read_text(encoding="utf8"))
assert c["rounds_completed"]>=63 and c["skill_certified_count"]==c["v3_full47_completed"]==0
print("R064 structural PASS: 16 TX and 39 combined; V1 only; no V2, V3, C or Skill")
