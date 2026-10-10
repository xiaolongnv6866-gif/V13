#!/usr/bin/env python3
"""R060 archived ID + locator integrity. Not independent literary validation."""
import csv,json,re
from pathlib import Path
P=Path(__file__).resolve().parents[1]
def load(path):
 with (P/path).open(encoding="utf-8",newline="") as f:return list(csv.DictReader(f,delimiter="\t"))
r=load("v2/legacy/WANMING_7_DECISIONS.tsv")
q=[x for x in load("gates/R057_LEGACY_QUARANTINE.tsv") if x["book_slug"]=="wanming"]
assert len(r)==len(q)==7 and {x["legacy_claim_id"] for x in r}=={x["legacy_claim_id"] for x in q}
assert len({x["new_candidate_id"] for x in r})==7
for x in r:
 assert x["book_slug"]=="wanming" and x["source_round"] in ("R009","R011","R013","R017","R019","R021","R023")
 data=[json.loads(y) for y in (P/"cangjie"/"reading"/x["source_round"]/"wanming_receipts.jsonl").read_text(encoding="utf-8").splitlines() if y.strip()]
 found=[(i,c) for i in data for c in i["mechanism_claims"] if c["claim_id"]==x["legacy_claim_id"]]
 assert len(found)==1
 i,c=found[0]
 assert str(i["narrative_ordinal"])==x["narrative_ordinal"] and i["epub_path"]==x["original_epub_path"] and i["chapter_sha256"]==x["chapter_sha256"]
 assert x["old_anchor"] in c["support_anchor_ids"]
 assert len(x["rechecked_loci"].split(";"))>=3
 for z in x["private_paragraph_sha256_samples"].split(";"):
  m=re.fullmatch(r"p(\d+):[0-9a-f]{64}",z)
  assert m and 1<=int(m[1])<=i["body_paragraph_count"]
 assert x["old_status"]=="OPEN_QUARANTINED" and x["new_status"]=="B_PROVISIONAL"
 assert all(x[k]=="NOT_RUN" for k in ("v1","v2","v3","independent_c"))
 assert all(x[k] for k in ("narrow_scene_mechanism","competing_explanation_or_counterexample","old_error_disposition"))
state=json.loads((P/"V13_CURRENT_V2.json").read_text(encoding="utf-8"))
assert state["rounds_completed"]>=59 and state["skill_certified_count"]==0 and state["heldout_bank_status"]=="SEALED_NOT_RUN" and state["v3_full47_completed"]==0
print("R060 STRUCTURE PASS 7/7 (content judgement based on private EPUB is not certified by CI)")
