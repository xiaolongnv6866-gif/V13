#!/usr/bin/env python3
"""N01 hard source & contract gate; structural only, no semantic literary certification."""
import csv,json,re
from pathlib import Path
P=Path(__file__).resolve().parents[1]
def tab(file):
 with (P/file).open(encoding="utf-8",newline="") as f:return list(csv.DictReader(f,delimiter="\t"))
cursor=json.loads((P/"V13_CURRENT_V4.json").read_text(encoding="utf-8"))
ledger=tab("V13_LEDGER_V4.tsv")
if cursor["completed_new_rounds"]==0:
 assert ledger[0]["status"] in ("IN_PROGRESS","BLOCKED","FAILED"),"N01 cannot be marked NOT_STARTED after evidence starts"
elif cursor["completed_new_rounds"]>=1:
 assert ledger[0]["status"]=="PASSED"
rows=tab("v13_3/n01/N01_LITERARY_B_17.tsv")
claims=tab("V13_3_ISSUES_426_TO_ROUNDS.tsv")
expected={x["issue_id"]:x for x in claims if x["new_primary_round"]=="N01" and x["issue_type"]=="STAGE0_B_CLAIM"}
assert len(expected)==len(rows)==17 and set(expected)=={x["issue_id"] for x in rows}
assert sum(x["literary_B_disposition"]=="SCOPED_CREDIBLE" for x in rows)==15
assert sum(x["literary_B_disposition"].startswith("REJECT_") for x in rows)==2
cache={}
for x in rows:
 for k in ("claim_id","source_round","epub_path","chapter_sha256","original_anchor_ids","original_claim","reviewed_loci","observable_action","character_view_or_inference","observed_or_unsettled_result","contrary_evidence","alternative_narration_loss","applicability_failure_boundary","literary_B_disposition"):
  assert len(x[k])>10 if k in ("observable_action","character_view_or_inference","observed_or_unsettled_result","contrary_evidence","alternative_narration_loss","applicability_failure_boundary") else bool(x[k]),(x["issue_id"],k)
 assert x["method_status"]=="NO_V1_V2_V3_NO_INDEPENDENT_C_NO_PROMOTION"
 ref=expected[x["issue_id"]];assert x["source_round"]==ref["original_source_round"] and x["claim_id"]==ref["origin_id"]
 f=ref["source"]
 if f not in cache:cache[f]={v["narrative_ordinal"]:v for v in (json.loads(l) for l in (P/f).read_text(encoding="utf-8").splitlines() if l.strip())}
 n=int(re.search(r"n(\d+)",x["reviewed_loci"]).group(1))
 item=cache[f][n]
 assert item["epub_path"]==x["epub_path"] and item["chapter_sha256"]==x["chapter_sha256"]
 assert item["source_epub_sha256"]=="a8f3b43dcd496822cd384ac8e9aa85f7dc374f8430f06c6f8321c26825093082"
 method=item["mechanism_claims"][0]
 assert method["claim_id"]==x["claim_id"] and method["claim_text"]==x["original_claim"]
 assert method["support_anchor_ids"]==x["original_anchor_ids"].split(";")
 assert all(z in {v["anchor_id"] for v in item["anchors"]} for z in method["support_anchor_ids"])
 body=int(item["body_paragraph_count"])
 loci=x["reviewed_loci"].split("/")[1].split(",")
 assert len(loci)>=3
 for token in loci:
  m=re.fullmatch(r"p(\d+)(?:-(\d+))?",token)
  if not m:continue
  assert 1<=int(m.group(1))<=int(m.group(2) or m.group(1))<=body,(x["claim_id"],token,body)
 assert "n"+str(n)==x["reviewed_loci"].split("/")[0]
assert len(set(x["contrary_evidence"] for x in rows))==17
assert len(set(x["alternative_narration_loss"] for x in rows))==17
legacy=tab("v13_3/n01/N01_LEGACY_R042.tsv")
assert len(legacy)==1 and legacy[0]["legacy_issue_id"]=="LEGACY:wm-r009-65-candidate"
assert legacy[0]["legacy_claim_id"]=="wm-r009-65-candidate"
assert "RETAIN_TO_N16" in legacy[0]["legacy_disposition"] and "NO_DIRECT_PROMOTION" in legacy[0]["promotion_permission"]
assert len((P/"v13_3/n01/N01_SOURCE_REVIEW.md").read_text(encoding="utf-8"))>10000
assert len((P/"runs/N01_V4.md").read_text(encoding="utf-8"))>300
print("PASS N01 17/17 traceable claims and independent old R042 disposition; structural only, no independent literary or method validation.")
