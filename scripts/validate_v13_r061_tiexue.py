#!/usr/bin/env python3
"""R061 provenance, frozen IDs, paragraph SHA format, and conservative disposition only.
No public CI can semantic-grade the private EPUB, V1/V2/V3, or creative uplift.
Optionally run locally with --epub <USER_PRIVATE_TIE_XUE_EPUB> to verify byte-level source.
"""
import csv,json,re,sys,hashlib,zipfile
from pathlib import Path
from lxml import etree
P=Path(__file__).resolve().parents[1]
def table(f):
 with (P/f).open(encoding="utf-8",newline="") as h:return list(csv.DictReader(h,delimiter="\t"))
rows=table("v2/legacy/TIEXUE_7_DECISIONS.tsv")
quarantine=[r for r in table("gates/R057_LEGACY_QUARANTINE.tsv") if r["book_slug"]=="tiexuecanming"]
assert len(rows)==len(quarantine)==7
assert {r["legacy_claim_id"] for r in rows}=={r["legacy_claim_id"] for r in quarantine}
assert len({r["new_candidate_id"] for r in rows})==7
expected_source="9100bbcdb9f52bcd5458cbda92e16b646489efbc00df5161ed568ebac83ffbaf"
epub=None
if "--epub" in sys.argv:
 ix=sys.argv.index("--epub")
 assert len(sys.argv)>ix+1
 file=Path(sys.argv[ix+1])
 assert hashlib.sha256(file.read_bytes()).hexdigest()==expected_source
 epub=zipfile.ZipFile(file)
 assert epub.testzip() is None
for r in rows:
 assert r["book_slug"]=="tiexuecanming" and r["source_round"] in ("R008","R012","R014","R016","R018","R020","R022")
 receipt=P/"cangjie"/"reading"/r["source_round"]/"tiexue_receipts.jsonl"
 original=[json.loads(t) for t in receipt.read_text(encoding="utf-8").splitlines() if t.strip()]
 matched=[(a,c) for a in original for c in a["mechanism_claims"] if c["claim_id"]==r["legacy_claim_id"]]
 assert len(matched)==1,r["legacy_claim_id"]
 item,c=matched[0]
 assert item["book_slug"]=="tiexuecanming" and str(item["narrative_ordinal"])==r["narrative_ordinal"]
 assert item["epub_path"]==r["original_epub_path"] and item["chapter_sha256"]==r["source_chapter_sha256"]
 assert int(r["body_paragraph_count"])==item["body_paragraph_count"]
 assert r["old_support_anchor"] in c["support_anchor_ids"]
 seen=set()
 for p in r["rechecked_loci"].split(";"):
  a=re.fullmatch(r"p(\d+)",p)
  assert a and 1<=int(a[1])<=item["body_paragraph_count"]
  seen.add(int(a[1]))
 assert len(seen)>=6 and int(r["old_support_anchor"][1:]) in seen
 hashes={}
 for v in r["private_paragraph_sha256_samples"].split(";"):
  a=re.fullmatch(r"p(\d+):([a-f0-9]{64})",v)
  assert a and 1<=int(a[1])<=item["body_paragraph_count"]
  hashes[int(a[1])]=a[2]
 assert len(hashes)>=4 and set(hashes).issubset(seen)
 assert r["old_claim_status"]=="OPEN_QUARANTINED"
 assert r["new_candidate_status"]=="B_PROVISIONAL"
 assert all(r[k]=="NOT_RUN" for k in ("v1_status","v2_status","v3_status","independent_c_status"))
 assert r["next_gate"].startswith("R062")
 for k in ("old_defect","observed_actions_and_information","counterexample_or_competing_explanation","bounded_new_literary_hypothesis","agency_authority_time_and_payoff","alternative_rendering_loss"):
  assert len(r[k])>=25, (r["legacy_claim_id"],k)
 if epub:
  data=epub.read(item["epub_path"])
  assert hashlib.sha256(data).hexdigest()==item["chapter_sha256"]
  ps=["".join(e.itertext()).strip() for e in etree.HTML(data).xpath("//body//p")]
  ps=[p for p in ps if p]
  assert len(ps)==item["body_paragraph_count"]
  for i,digest in hashes.items():
   assert hashlib.sha256(ps[i-1].encode("utf-8")).hexdigest()==digest,(r["legacy_claim_id"],i)
cur=json.loads((P/"V13_CURRENT_V2.json").read_text(encoding="utf-8"))
assert cur["rounds_completed"]>=60 and cur["skill_certified_count"]==cur["v3_full47_completed"]==0
assert cur["heldout_bank_status"]=="SEALED_NOT_RUN"
assert "status: PASSED" in (P/"runs/R061_V2.md").read_text(encoding="utf-8") or cur["rounds_completed"]==60
print("R061 STRUCTURAL SOURCE PASS: 7 original IDs, source receipts, location bounds, zero certification"+(" + PRIVATE EPUB bytes/paragraph SHA VERIFIED" if epub else " (private EPUB not available to public CI)"))
