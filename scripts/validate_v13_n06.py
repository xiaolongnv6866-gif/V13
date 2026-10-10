#!/usr/bin/env python3
"""N06 source and historical quarantine gate, structural; NOT a literary skill certification."""
import csv,json,re
from pathlib import Path
from collections import Counter
P=Path(__file__).resolve().parents[1]
def rd(p):
 with (P/p).open(encoding="utf-8",newline="") as f:return list(csv.DictReader(f,delimiter="\t"))
state=json.loads((P/"V13_CURRENT_V4.json").read_text(encoding="utf-8"))
ledger=rd("V13_LEDGER_V4.tsv")
assert all(x["status"]=="PASSED" for x in ledger[:5])
if state["completed_new_rounds"]==5:
 assert state["current_round"]=="N06" and state["current_round_status"] in ("IN_PROGRESS","BLOCKED","FAILED")
 assert ledger[5]["status"]==state["current_round_status"]
else:assert state["completed_new_rounds"]>=6 and ledger[5]["status"]=="PASSED"
all_issues=rd("V13_3_ISSUES_426_TO_ROUNDS.tsv")
mapped={x["issue_id"]:x for x in all_issues if x["new_primary_round"]=="N06" and x["issue_type"]=="STAGE0_B_CLAIM"}
legacyIDs=[x for x in all_issues if x["new_primary_round"]=="N06" and x["issue_type"]=="LEGACY_R042_QUARANTINE"]
r=rd("v13_3/n06/N06_LITERARY_B_20.tsv")
assert len(r)==len(mapped)==20 and set(mapped)=={x["issue_id"] for x in r}
assert len(legacyIDs)==1 and legacyIDs[0]["issue_id"]=="LEGACY:v13-r019-wanming-265-candidate"
assert sum(x["B_decision"].startswith("REJECT_") for x in r)==2
assert len({x["counterexample"] for x in r})==20 and len({x["narrative_alternative_loss"] for x in r})==20
cache={}
for row in r:
 i=mapped[row["issue_id"]]
 assert row["claim_id"]==i["origin_id"] and row["source_round"]=="R019"
 assert row["method_status"]=="STAGE0_B_ONLY_NO_V1_V2_V3_C_OR_SKILL"
 for k in ("observable_action","character_view_and_knowledge","result_and_pending","counterexample","narrative_alternative_loss","failure_boundary"):
  assert len(row[k])>=20,(row["issue_id"],k)
 src=i["source"]
 if src not in cache:cache[src]={int(x["narrative_ordinal"]):x for x in (json.loads(z) for z in (P/src).read_text(encoding="utf-8").splitlines() if z.strip())}
 n=int(re.match(r"n(\d+)/",row["reviewed_loci"]).group(1));doc=cache[src][n]
 assert doc["source_epub_sha256"]=="a8f3b43dcd496822cd384ac8e9aa85f7dc374f8430f06c6f8321c26825093082"
 assert doc["epub_path"]==row["epub_path"] and doc["chapter_sha256"]==row["chapter_sha256"]
 m=doc["mechanism_claims"][0]
 assert m["claim_id"]==row["claim_id"] and m["claim_text"]==row["old_claim"]
 assert m["support_anchor_ids"]==row["old_anchor_ids"].split(";")
 assert set(m["support_anchor_ids"])<={x["anchor_id"] for x in doc["anchors"]}
 for part in row["reviewed_loci"].split("/",1)[1].split(","):
  v=re.fullmatch(r"p(\d+)(?:-(\d+))?",part)
  assert v and 1<=int(v.group(1))<=int(v.group(2) or v.group(1))<=int(doc["body_paragraph_count"]),(n,part)
sha=rd("v13_3/n06/N06_ORIGINAL_PARAGRAPH_SHA_40.tsv")
assert len(sha)==40 and set(x["issue_id"] for x in sha)==set(mapped)
assert set(Counter(x["issue_id"] for x in sha).values())=={2}
for x in sha:
 row=next(y for y in r if y["issue_id"]==x["issue_id"])
 assert x["claim_id"]==row["claim_id"] and x["epub_path"]==row["epub_path"]
 assert x["narrative_ordinal"]==re.match(r"n(\d+)/",row["reviewed_loci"]).group(1)
 assert re.fullmatch(r"[a-f0-9]{64}",x["paragraph_sha256"])
 assert x["source_check"]=="RECOMPUTED_FROM_PRIVATE_EPUB"
 assert x["paragraph_role"] in ("FROZEN_OLD","REVISED_OR_COUNTER")
 assert 1<=int(x["paragraph_index"])<=int(cache["cangjie/reading/R019/wanming_receipts.jsonl"][int(x["narrative_ordinal"])]["body_paragraph_count"])
q=rd("v13_3/n06/N06_LEGACY_R042.tsv")
assert len(q)==1 and q[0]["legacy_issue_id"]=="LEGACY:v13-r019-wanming-265-candidate"
assert "OPEN_QUARANTINED" in q[0]["historical_status"] and "NO_DIRECT_PROMOTION" in q[0]["direct_promotion"]
report=(P/"v13_3/n06/N06_SOURCE_REVIEW.md").read_text(encoding="utf-8")
assert len(report)>10000 and all(x["issue_id"] in report for x in r)
print("PASS N06 20 original B literary source contracts, 40 SHA positions, 1 independent R042 historical quarantine; structural only.")
