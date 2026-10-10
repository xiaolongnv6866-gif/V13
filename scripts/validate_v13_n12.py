#!/usr/bin/env python3
"""N12 frozen 20 literary claims + separate old R042; structural checks, not independent literary review."""
from pathlib import Path
import csv,json,re
from collections import Counter
ROOT=Path(__file__).resolve().parents[1]
def table(path):
 with (ROOT/path).open(encoding="utf-8",newline="") as f:
  return list(csv.DictReader(f,delimiter="\t"))
cursor=json.loads((ROOT/"V13_CURRENT_V4.json").read_text(encoding="utf-8"))
ledger=table("V13_LEDGER_V4.tsv")
assert len(ledger)==48
assert all(x["status"]=="PASSED" for x in ledger[:11])
if cursor["completed_new_rounds"]==11:
 assert cursor["current_round"]=="N12" and cursor["current_round_status"] in ("IN_PROGRESS","BLOCKED","FAILED")
 assert ledger[11]["status"]==cursor["current_round_status"]
else:
 assert cursor["completed_new_rounds"] >=12 and ledger[11]["status"]=="PASSED"
issues=table("V13_3_ISSUES_426_TO_ROUNDS.tsv")
B={x["issue_id"]:x for x in issues if x["new_primary_round"]=="N12" and x["issue_type"]=="STAGE0_B_CLAIM"}
Q=[x for x in issues if x["new_primary_round"]=="N12" and x["issue_type"]=="LEGACY_R042_QUARANTINE"]
C=table("v13_3/n12/N12_LITERARY_B_20.tsv")
S=table("v13_3/n12/N12_ORIGINAL_PARAGRAPH_SHA_40.tsv")
L=table("v13_3/n12/N12_LEGACY_R042.tsv")
assert len(B)==len(C)==20 and {x["issue_id"] for x in C}==set(B)
assert len(Q)==len(L)==1 and L[0]["legacy_issue_id"]==Q[0]["issue_id"]=="LEGACY:v13-R018-tiexue-226-candidate"
assert all("OPEN_QUARANTINED" in x["historical_quarantine_status"] and "NO_DIRECT_PROMOTION" in x["method_promotion_permission"] for x in L)
assert sum(x["literary_B_disposition"].startswith("REJECT_") for x in C)==4
cache={}
for claim in C:
 issue=B[claim["issue_id"]];src=issue["source"]
 assert claim["original_round"] in ("R018","R018") and claim["original_round"]==issue["original_source_round"]
 assert claim["original_claim_id"]==issue["origin_id"]
 assert claim["method_status"]=="STAGE0_B_ONLY_NO_V1_V2_TRUE_INDEPENDENT_V3_C_OR_SKILL"
 for k in ("visible_action","different_voices_knowledge_limit","actual_and_pending_result","counterexample_or_old_error","alternative_narrative_loss","applicability_and_failure_boundary"):
  assert len(claim[k])>=24,(claim["issue_id"],k,len(claim[k]))
 if src not in cache:cache[src]={int(x["narrative_ordinal"]):x for x in (json.loads(t) for t in (ROOT/src).read_text(encoding="utf-8").splitlines() if t.strip())}
 n=int(re.match(r"n(\d+)/",claim["reviewed_loci"]).group(1))
 original=cache[src][n]
 assert original["source_epub_sha256"]=="9100bbcdb9f52bcd5458cbda92e16b646489efbc00df5161ed568ebac83ffbaf"
 assert claim["epub_path"]==original["epub_path"] and claim["chapter_sha256"]==original["chapter_sha256"]
 old=original["mechanism_claims"][0]
 assert claim["original_claim_id"]==old["claim_id"] and claim["original_claim"]==old["claim_text"]
 assert claim["old_support"].split(";")==old["support_anchor_ids"]
 assert set(old["support_anchor_ids"])<={a["anchor_id"] for a in original["anchors"]}
 for loc in claim["reviewed_loci"].split("/",1)[1].split(","):
  m=re.fullmatch(r"p(\d+)(?:-(\d+))?",loc)
  assert m and 1<=int(m.group(1))<=int(m.group(2) or m.group(1))<=int(original["body_paragraph_count"])
assert len(S)==40 and set(x["issue_id"] for x in S)==set(B)
assert set(Counter(x["issue_id"] for x in S).values())=={2}
byId={x["issue_id"]:x for x in C}
for x in S:
 b=byId[x["issue_id"]]
 assert x["claim_id"]==b["original_claim_id"] and x["epub_path"]==b["epub_path"]
 assert re.fullmatch("[0-9a-f]{64}",x["paragraph_sha256"])
 assert x["verification"]=="DIRECT_RECOMPUTED_USER_PRIVATE_EPUB_SHA256"
 assert x["location_role"] in ("FROZEN_OLD_SUPPORT","REVISED_OR_COUNTER")
 n=int(x["narrative_ordinal"])
 assert str(n)==re.match(r"n(\d+)/",b["reviewed_loci"]).group(1)
 doc=cache["cangjie/reading/"+b["original_round"]+"/tiexue_receipts.jsonl"][n]
 assert 1<=int(x["paragraph_index"])<=int(doc["body_paragraph_count"])
 if x["location_role"]=="FROZEN_OLD_SUPPORT":
  assert any(int(a["paragraph_index"])==int(x["paragraph_index"]) and a["paragraph_sha256"]==x["paragraph_sha256"] for a in doc["anchors"])

assert {x["issue_id"] for x in C if x["literary_B_disposition"].startswith("REJECT_")}=={"STAGE0:R018:v13-R018-tiexue-218-candidate","STAGE0:R018:v13-R018-tiexue-226-candidate","STAGE0:R018:v13-R018-tiexue-228-candidate","STAGE0:R018:v13-R018-tiexue-232-candidate"}
body=(ROOT/"v13_3/n12/N12_SOURCE_REVIEW.md").read_text(encoding="utf-8")
assert len(body)>12000 and all(x["issue_id"] in body for x in C)
if cursor["completed_new_rounds"]>=9:
 receipt=(ROOT/"runs/N12_V4.md").read_text(encoding="utf-8")
 assert len(receipt)>600
print("PASS N12 original B 20/20, paragraphs 40/40, old R042 1/1 remains quarantined; structural only")
