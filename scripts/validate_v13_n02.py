#!/usr/bin/env python3
"""Structural N02 source and 17+1 ID checks, NOT independent literary evaluation."""
import csv,json,re
from pathlib import Path
P=Path(__file__).resolve().parents[1]
def rd(path):
 with (P/path).open(encoding="utf-8",newline="") as f:return list(csv.DictReader(f,delimiter="\t"))
s=json.loads((P/"V13_CURRENT_V4.json").read_text(encoding="utf-8"))
ledger=rd("V13_LEDGER_V4.tsv")
assert ledger[0]["status"]=="PASSED"
if s["completed_new_rounds"]==1:
 assert s["current_round"]=="N02" and s["current_round_status"] in ("IN_PROGRESS","BLOCKED","FAILED")
 assert ledger[1]["status"]==s["current_round_status"]
elif s["completed_new_rounds"]>=2:
 assert ledger[1]["status"]=="PASSED"
rows=rd("v13_3/n02/N02_LITERARY_B_17.tsv")
m=rd("V13_3_ISSUES_426_TO_ROUNDS.tsv")
expected={r["issue_id"]:r for r in m if r["new_primary_round"]=="N02" and r["issue_type"]=="STAGE0_B_CLAIM"}
assert len(rows)==len(expected)==17 and {r["issue_id"] for r in rows}==set(expected)
assert sum(r["B_disposition"].startswith("REJECT_") for r in rows)==3
assert len(set(r["counterexample"] for r in rows))==17
assert len(set(r["alternative_narration_loss"] for r in rows))==17
cache={}
for row in rows:
 claim=expected[row["issue_id"]]
 assert claim["origin_id"]==row["claim_id"] and row["source_round"]=="R011"
 assert row["method_status"]=="NO_V1_V2_V3_NO_INDEPENDENT_C_NO_PROMOTION"
 for k in ("observable_action","character_view","actual_result","counterexample","alternative_narration_loss","applicability_boundary"):
  assert len(row[k])>=35,(row["claim_id"],k)
 source=claim["source"]
 if source not in cache:
  cache[source]={int(x["narrative_ordinal"]):x for x in (json.loads(line) for line in (P/source).read_text(encoding="utf-8").splitlines() if line.strip())}
 n=int(re.match(r"n(\d+)/",row["actual_loci"]).group(1))
 doc=cache[source][n]
 assert doc["chapter_sha256"]==row["chapter_sha256"] and doc["epub_path"]==row["epub_path"]
 assert doc["source_epub_sha256"]=="a8f3b43dcd496822cd384ac8e9aa85f7dc374f8430f06c6f8321c26825093082"
 h=doc["mechanism_claims"][0]
 assert h["claim_id"]==row["claim_id"] and h["claim_text"]==row["old_claim"]
 assert h["support_anchor_ids"]==row["old_anchor_ids"].split(";")
 assert set(h["support_anchor_ids"])<={q["anchor_id"] for q in doc["anchors"]}
 for part in row["actual_loci"].split("/")[1].split(","):
  mm=re.fullmatch(r"p(\d+)(?:-(\d+))?",part)
  assert mm and 1<=int(mm.group(1))<=int(mm.group(2) or mm.group(1))<=int(doc["body_paragraph_count"]),(n,part)
q=rd("v13_3/n02/N02_LEGACY_R042.tsv")
assert len(q)==1 and q[0]["legacy_issue_id"]=="LEGACY:wm-r011-99-candidate"
assert "OPEN_QUARANTINED" in q[0]["legacy_status"] and "NO_DIRECT_PROMOTION" in q[0]["stage1_permission"]
review=(P/"v13_3/n02/N02_SOURCE_REVIEW.md").read_text(encoding="utf-8")
assert len(review)>12000 and all(r["issue_id"] in review for r in rows)
print("PASS N02 17/17 source contracts + 1 R042 isolated (structure only, no independent literary/skill certification)")
