#!/usr/bin/env python3
"""N04 18 R015 literary B source audit: structural checks do not certify method quality."""
import csv,json,re
from pathlib import Path
from collections import Counter
P=Path(__file__).resolve().parents[1]
def t(path):
 with (P/path).open(encoding="utf-8",newline="") as f:return list(csv.DictReader(f,delimiter="\t"))
s=json.loads((P/"V13_CURRENT_V4.json").read_text(encoding="utf-8"))
ledger=t("V13_LEDGER_V4.tsv")
assert all(a["status"]=="PASSED" for a in ledger[:3])
if s["completed_new_rounds"]==3:
 assert s["current_round"]=="N04" and s["current_round_status"] in ("IN_PROGRESS","BLOCKED","FAILED")
 assert ledger[3]["status"]==s["current_round_status"]
else:assert s["completed_new_rounds"]>=4 and ledger[3]["status"]=="PASSED"
mapped={i["issue_id"]:i for i in t("V13_3_ISSUES_426_TO_ROUNDS.tsv") if i["new_primary_round"]=="N04"}
r=t("v13_3/n04/N04_LITERARY_B_18.tsv")
assert len(mapped)==len(r)==18 and set(mapped)=={x["issue_id"] for x in r}
assert all(z["issue_type"]=="STAGE0_B_CLAIM" for z in mapped.values())
assert sum(x["literary_B_decision"].startswith("REJECT_") for x in r)==4
assert len(set(x["concrete_counterexample"] for x in r))==18
assert len(set(x["alternative_narration_loss"] for x in r))==18
receipts={}
for x in r:
 ref=mapped[x["issue_id"]]
 assert x["original_claim_id"]==ref["origin_id"] and x["original_round"]=="R015"
 assert x["method_status"]=="B_ONLY_NO_V1_V2_V3_INDEPENDENT_C_OR_CERTIFICATION"
 for key in ("observable_action","character_stance_and_knowledge_limit","confirmed_vs_unsettled_result","concrete_counterexample","alternative_narration_loss","failure_boundary"):
  assert len(x[key])>=25,(x["issue_id"],key)
 p=ref["source"]
 if p not in receipts:receipts[p]={int(z["narrative_ordinal"]):z for z in (json.loads(y) for y in (P/p).read_text(encoding="utf-8").splitlines() if y.strip())}
 n=int(re.match(r"n(\d+)/",x["rechecked_loci"]).group(1))
 ch=receipts[p][n]
 assert ch["epub_path"]==x["epub_path"] and ch["chapter_sha256"]==x["chapter_sha256"]
 assert ch["source_epub_sha256"]=="a8f3b43dcd496822cd384ac8e9aa85f7dc374f8430f06c6f8321c26825093082"
 old=ch["mechanism_claims"][0]
 assert old["claim_id"]==x["original_claim_id"] and old["claim_text"]==x["original_claim"]
 assert ";".join(old["support_anchor_ids"])==x["frozen_support"]
 assert set(old["support_anchor_ids"])<={v["anchor_id"] for v in ch["anchors"]}
 for q in x["rechecked_loci"].split("/",1)[1].split(","):
  v=re.fullmatch(r"p(\d+)(?:-(\d+))?",q)
  assert v and 1<=int(v.group(1))<=int(v.group(2) or v.group(1))<=int(ch["body_paragraph_count"]),(n,q)
proof=t("v13_3/n04/N04_ORIGINAL_PARAGRAPH_SHA_36.tsv")
assert len(proof)==36 and set(x["issue_id"] for x in proof)==set(mapped)
assert set(Counter(x["issue_id"] for x in proof).values())=={2}
for z in proof:
 r0=next(x for x in r if x["issue_id"]==z["issue_id"])
 assert z["claim_id"]==r0["original_claim_id"] and z["epub_path"]==r0["epub_path"]
 assert z["ordinal"]==re.match(r"n(\d+)/",r0["rechecked_loci"]).group(1)
 assert re.fullmatch(r"[0-9a-f]{64}",z["paragraph_sha256"])
 assert z["source_verification"]=="PRIVATE_EPUB_SHA256_RECALCULATED"
 assert z["source_role"] in ("FROZEN_OLD_ANCHOR","REVISED_OR_COUNTER_CONTEXT")
 assert 1<=int(z["paragraph_index"])<=int(receipts["cangjie/reading/R015/wanming_receipts.jsonl"][int(z["ordinal"])]["body_paragraph_count"])
doc=(P/"v13_3/n04/N04_SOURCE_REVIEW.md").read_text(encoding="utf-8")
assert len(doc)>9000 and all(x["issue_id"] in doc for x in r)
assert len((P/"runs/N04_V4.md").read_text(encoding="utf-8"))>500
print("PASS N04 structural 18 R015 B + 36 private paragraph-hash records; NO independent literary or Skill certification.")
