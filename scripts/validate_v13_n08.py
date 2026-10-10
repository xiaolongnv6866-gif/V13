#!/usr/bin/env python3
"""N08 original literary B + historical quarantine structural verification; NOT independent literary test."""
import csv,json,re
from collections import Counter
from pathlib import Path
P=Path(__file__).resolve().parents[1]
def rd(p):
 with (P/p).open(encoding="utf8",newline="") as f:return list(csv.DictReader(f,delimiter="\t"))
cur=json.loads((P/"V13_CURRENT_V4.json").read_text(encoding="utf8"))
ledger=rd("V13_LEDGER_V4.tsv")
assert all(x["status"]=="PASSED" for x in ledger[:7])
if cur["completed_new_rounds"]==7:
 assert cur["current_round"]=="N08" and cur["current_round_status"] in ("IN_PROGRESS","BLOCKED","FAILED")
 assert ledger[7]["status"]==cur["current_round_status"]
else:assert cur["completed_new_rounds"]>=8 and ledger[6]["status"]=="PASSED"
issues=rd("V13_3_ISSUES_426_TO_ROUNDS.tsv")
B={x["issue_id"]:x for x in issues if x["new_primary_round"]=="N08" and x["issue_type"]=="STAGE0_B_CLAIM"}
Q=[x for x in issues if x["new_primary_round"]=="N08" and x["issue_type"]=="LEGACY_R042_QUARANTINE"]
C=rd("v13_3/n08/N08_LITERARY_B_20.tsv")
assert len(C)==len(B)==20 and set(B)=={x["issue_id"] for x in C}
assert len(Q)==1 and Q[0]["issue_id"]=="LEGACY:v13-r023-wanming-339-candidate"
assert sum(x["literary_B_disposition"].startswith("REJECT_") for x in C)==6
assert len({x["counterexample_or_old_error"] for x in C})==20
assert len({x["alternative_narrative_loss"] for x in C})==20
cache={}
for x in C:
 issue=B[x["issue_id"]]
 assert x["original_claim_id"]==issue["origin_id"] and x["original_round"]=="R023"
 assert x["method_status"]=="STAGE0_B_ONLY_NO_V1_V2_TRUE_INDEPENDENT_V3_C_OR_SKILL"
 for k in ("visible_action","different_voices_knowledge_limit","actual_and_pending_result","counterexample_or_old_error","alternative_narrative_loss","applicability_and_failure_boundary"):
  assert len(x[k])>=24,(x["issue_id"],k)
 src=issue["source"]
 if src not in cache:cache[src]={int(y["narrative_ordinal"]):y for y in (json.loads(v) for v in (P/src).read_text(encoding="utf8").splitlines() if v.strip())}
 n=int(re.match(r"n(\d+)/",x["reviewed_loci"]).group(1));doc=cache[src][n]
 assert doc["epub_path"]==x["epub_path"] and doc["chapter_sha256"]==x["chapter_sha256"]
 assert doc["source_epub_sha256"]=="a8f3b43dcd496822cd384ac8e9aa85f7dc374f8430f06c6f8321c26825093082"
 old=doc["mechanism_claims"][0]
 assert old["claim_id"]==x["original_claim_id"] and old["claim_text"]==x["original_claim"]
 assert x["old_support"].split(";")==old["support_anchor_ids"]
 assert set(old["support_anchor_ids"])<={y["anchor_id"] for y in doc["anchors"]}
 for p in x["reviewed_loci"].split("/",1)[1].split(","):
  m=re.fullmatch(r"p(\d+)(?:-(\d+))?",p)
  assert m and 1<=int(m.group(1))<=int(m.group(2) or m.group(1))<=int(doc["body_paragraph_count"]),(n,p)
S=rd("v13_3/n08/N08_ORIGINAL_PARAGRAPH_SHA_40.tsv")
assert len(S)==40 and set(x["issue_id"] for x in S)==set(B)
assert set(Counter(x["issue_id"] for x in S).values())=={2}
for x in S:
 claim=next(y for y in C if y["issue_id"]==x["issue_id"])
 assert x["claim_id"]==claim["original_claim_id"] and x["epub_path"]==claim["epub_path"]
 assert x["narrative_ordinal"]==re.match(r"n(\d+)/",claim["reviewed_loci"]).group(1)
 assert re.fullmatch(r"[0-9a-f]{64}",x["paragraph_sha256"])
 assert x["verification"]=="DIRECT_RECOMPUTED_USER_PRIVATE_EPUB_SHA256"
 assert x["location_role"] in ("FROZEN_OLD_SUPPORT","REVISED_OR_COUNTER")
 assert 1<=int(x["paragraph_index"])<=int(cache["cangjie/reading/R023/wanming_receipts.jsonl"][int(x["narrative_ordinal"])]["body_paragraph_count"])
L=rd("v13_3/n08/N08_LEGACY_R042.tsv")
assert len(L)==1 and L[0]["legacy_issue_id"]=="LEGACY:v13-r023-wanming-339-candidate"
assert "OPEN_QUARANTINED" in L[0]["historical_quarantine_status"]
assert "NO_DIRECT_PROMOTION" in L[0]["method_promotion_permission"]
md=(P/"v13_3/n08/N08_SOURCE_REVIEW.md").read_text(encoding="utf8")
assert len(md)>14000 and all(x["issue_id"] in md for x in C)
if cur["completed_new_rounds"]>=8: assert len((P/"runs/N08_V4.md").read_text(encoding="utf8"))>600
print("PASS N08 20/20 B source analyses, 40 paragraph hashes and 1 separately quarantined R042 historical ID; structural only")
