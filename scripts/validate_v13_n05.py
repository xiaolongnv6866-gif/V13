#!/usr/bin/env python3
"""N05 source-location and 20+1 original ID gate; never independent literary test."""
import csv,json,re
from pathlib import Path
from collections import Counter
P=Path(__file__).resolve().parents[1]
def read(p):
 with (P/p).open(encoding="utf8",newline="") as f:return list(csv.DictReader(f,delimiter="\t"))
s=json.loads((P/"V13_CURRENT_V4.json").read_text(encoding="utf8"))
ledger=read("V13_LEDGER_V4.tsv")
assert all(x["status"]=="PASSED" for x in ledger[:4])
if s["completed_new_rounds"]==4:
 assert s["current_round"]=="N05" and s["current_round_status"] in ("IN_PROGRESS","BLOCKED","FAILED")
 assert ledger[4]["status"]==s["current_round_status"]
else:assert s["completed_new_rounds"]>=5 and ledger[4]["status"]=="PASSED"
issues=read("V13_3_ISSUES_426_TO_ROUNDS.tsv")
claim_mapping={x["issue_id"]:x for x in issues if x["new_primary_round"]=="N05" and x["issue_type"]=="STAGE0_B_CLAIM"}
quarantines=[x for x in issues if x["new_primary_round"]=="N05" and x["issue_type"]=="LEGACY_R042_QUARANTINE"]
assert len(claim_mapping)==20 and len(quarantines)==1
assert quarantines[0]["issue_id"]=="LEGACY:wanming-R017-220-candidate"
cases=read("v13_3/n05/N05_LITERARY_B_20.tsv")
assert len(cases)==20 and {x["issue_id"] for x in cases}==set(claim_mapping)
assert sum(x["literary_B_disposition"].startswith("REJECT_") for x in cases)==4
assert len({x["contrary_evidence_or_old_error"] for x in cases})==20
assert len({x["replacement_narrative_loss"] for x in cases})==20
cache={}
for x in cases:
 ref=claim_mapping[x["issue_id"]]
 assert x["original_claim_id"]==ref["origin_id"] and x["original_round"]=="R017"
 assert x["method_gate"]=="B_SOURCE_REVIEW_ONLY_NO_V1_V2_INDEPENDENT_V3_C_SKILL"
 for field in ("observable_action","character_views","actual_and_unsettled_result","contrary_evidence_or_old_error","replacement_narrative_loss","failure_boundary"):
  assert len(x[field])>=30,(x["issue_id"],field)
 src=ref["source"]
 if src not in cache:cache[src]={int(y["narrative_ordinal"]):y for y in (json.loads(ln) for ln in (P/src).read_text(encoding="utf8").splitlines() if ln.strip())}
 n=int(re.match(r"n(\d+)/",x["reread_loci"]).group(1))
 chapter=cache[src][n]
 assert chapter["epub_path"]==x["epub_path"] and chapter["chapter_sha256"]==x["chapter_sha256"]
 assert chapter["source_epub_sha256"]=="a8f3b43dcd496822cd384ac8e9aa85f7dc374f8430f06c6f8321c26825093082"
 m=chapter["mechanism_claims"][0]
 assert m["claim_id"]==x["original_claim_id"] and m["claim_text"]==x["old_claim"]
 assert x["old_support"]==";".join(m["support_anchor_ids"])
 assert set(m["support_anchor_ids"])<={a["anchor_id"] for a in chapter["anchors"]}
 for v in x["reread_loci"].split("/",1)[1].split(","):
  p=re.fullmatch(r"p(\d+)(?:-(\d+))?",v)
  assert p,(x["original_claim_id"],v)
  assert 1<=int(p.group(1))<=int(p.group(2) or p.group(1))<=int(chapter["body_paragraph_count"]),(n,v)
sha=read("v13_3/n05/N05_ORIGINAL_PARAGRAPH_SHA_40.tsv")
assert len(sha)==40 and {x["issue_id"] for x in sha}==set(claim_mapping)
assert set(Counter(x["issue_id"] for x in sha).values())=={2}
for x in sha:
 row=next(z for z in cases if z["issue_id"]==x["issue_id"])
 assert x["original_claim_id"]==row["original_claim_id"] and x["epub_path"]==row["epub_path"]
 assert x["ordinal"]==re.match(r"n(\d+)/",row["reread_loci"]).group(1)
 assert re.fullmatch(r"[a-f0-9]{64}",x["paragraph_sha256"])
 assert x["locus_type"] in ("FROZEN_SINGLE_ANCHOR","CONTRARY_OR_CORRECTIVE_CONTEXT")
 assert x["verification"]=="DIRECT_PRIVATE_EPUB_SHA256_RECALCULATED"
 assert 1<=int(x["paragraph_index"])<=int(cache["cangjie/reading/R017/wanming_receipts.jsonl"][int(x["ordinal"])]["body_paragraph_count"])
legacy=read("v13_3/n05/N05_LEGACY_R042.tsv")
assert len(legacy)==1 and legacy[0]["legacy_issue_id"]=="LEGACY:wanming-R017-220-candidate"
assert "OPEN_QUARANTINED" in legacy[0]["historical_quarantine_status"]
assert "NO_DIRECT_PROMOTION" in legacy[0]["promotion_rule"]
md=(P/"v13_3/n05/N05_SOURCE_REVIEW.md").read_text(encoding="utf8")
assert len(md)>14000 and all(x["issue_id"] in md for x in cases)
assert len((P/"runs/N05_V4.md").read_text(encoding="utf8"))>500
print("PASS N05 20 R017 B claims, 40 original paragraph hash records and 1 quarantined historical ID; structural only.")
