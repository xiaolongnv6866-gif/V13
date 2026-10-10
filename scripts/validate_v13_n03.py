#!/usr/bin/env python3
"""V13.3 N03 18+1 source integrity. No independent literary or method certification."""
import json,re,csv
from pathlib import Path
P=Path(__file__).resolve().parents[1]
def read(path):
 with (P/path).open(encoding="utf8",newline="") as f:return list(csv.DictReader(f,delimiter="\t"))
cursor=json.loads((P/"V13_CURRENT_V4.json").read_text(encoding="utf8"))
ledger=read("V13_LEDGER_V4.tsv")
assert ledger[0]["status"]==ledger[1]["status"]=="PASSED"
if cursor["completed_new_rounds"]==2:
 assert cursor["current_round"]=="N03" and cursor["current_round_status"] in ("IN_PROGRESS","BLOCKED","FAILED")
 assert ledger[2]["status"]==cursor["current_round_status"]
else: assert cursor["completed_new_rounds"]>=3 and ledger[2]["status"]=="PASSED"
issues=read("V13_3_ISSUES_426_TO_ROUNDS.tsv")
expected={x["issue_id"]:x for x in issues if x["new_primary_round"]=="N03" and x["issue_type"]=="STAGE0_B_CLAIM"}
rows=read("v13_3/n03/N03_LITERARY_B_18.tsv")
assert len(expected)==len(rows)==18 and {x["issue_id"] for x in rows}==set(expected)
assert sum(x["B_adjudication"].startswith("REJECT_") for x in rows)==5
assert len({x["counter_or_competing_explanation"] for x in rows})==18
assert len({x["narrative_alternative_loss"] for x in rows})==18
cache={}
for x in rows:
 ref=expected[x["issue_id"]]
 assert x["original_claim_id"]==ref["origin_id"] and x["original_source_round"]=="R013"
 assert x["stage1_permission"]=="B_RESEARCH_ONLY_NO_V1_V2_V3_NO_INDEPENDENT_C"
 for field in ("observed_action","subject_and_view_limit","actual_vs_unsettled_result","counter_or_competing_explanation","narrative_alternative_loss","boundary"):
  assert len(x[field])>=27,(x["issue_id"],field)
 p=ref["source"]
 if p not in cache:cache[p]={int(k["narrative_ordinal"]):k for k in [json.loads(s) for s in (P/p).read_text(encoding="utf8").splitlines() if s.strip()]}
 n=int(re.match(r"n(\d+)/",x["reviewed_loci"]).group(1))
 doc=cache[p][n]
 assert doc["source_epub_sha256"]=="a8f3b43dcd496822cd384ac8e9aa85f7dc374f8430f06c6f8321c26825093082"
 assert doc["chapter_sha256"]==x["chapter_sha256"] and doc["epub_path"]==x["original_epub_path"]
 mechanism=doc["mechanism_claims"][0]
 assert mechanism["claim_id"]==x["original_claim_id"] and mechanism["claim_text"]==x["original_claim"]
 assert mechanism["support_anchor_ids"]==x["old_support"].split(";")
 assert set(mechanism["support_anchor_ids"])<={a["anchor_id"] for a in doc["anchors"]}
 assert x["reviewed_loci"].startswith("n"+str(n)+"/")
 for part in x["reviewed_loci"].split("/",1)[1].split(","):
  m=re.fullmatch(r"(?:n\d+/)?p(\d+)(?:-(\d+))?",part)
  assert m,(n,part)
  if "n148/" in part:continue
  assert 1<=int(m.group(1))<=int(m.group(2) or m.group(1))<=int(doc["body_paragraph_count"]),(n,part)
proof=read("v13_3/n03/N03_ORIGINAL_PARAGRAPH_SHA_36.tsv")
assert len(proof)==36 and len({(e["issue_id"],e["paragraph_index"]) for e in proof})==36
assert {e["issue_id"] for e in proof}==set(expected)
from collections import Counter
assert set(Counter(e["issue_id"] for e in proof).values())=={2}
for sample in proof:
 case=next(z for z in rows if z["issue_id"]==sample["issue_id"])
 assert sample["claim_id"]==case["original_claim_id"] and sample["epub_path"]==case["original_epub_path"]
 assert sample["ordinal"]==re.match(r"n(\d+)/",case["reviewed_loci"]).group(1)
 assert re.fullmatch(r"[0-9a-f]{64}",sample["paragraph_sha256"])
 assert sample["source_hash_status"]=="DIRECT_PRIVATE_EPUB_SHA256_MATCH"
 assert sample["locus_role"] in ("OLD_OR_SCENE_LOCUS","CORRECTIVE_OR_CONTRARY_CONTEXT")
 assert 1<=int(sample["paragraph_index"])<=int(cache["cangjie/reading/R013/wanming_receipts.jsonl"][int(sample["ordinal"])]["body_paragraph_count"])
q=read("v13_3/n03/N03_LEGACY_R042.tsv")
assert len(q)==1 and q[0]["legacy_issue_id"]=="LEGACY:wanming-R013-143-narrative-candidate"
assert "OPEN_QUARANTINED" in q[0]["quarantine_after_N03"] and "NO_DIRECT_PROMOTION" in q[0]["promotion_permission"]
report=(P/"v13_3/n03/N03_SOURCE_REVIEW.md").read_text(encoding="utf8")
assert len(report)>14000 and all(x["issue_id"] in report for x in rows)
assert len((P/"runs/N03_V4.md").read_text(encoding="utf8"))>500
print("PASS N03 18/18 old B cases + 1/1 R042 legacy reviewed & isolated. CI is structural only.")
