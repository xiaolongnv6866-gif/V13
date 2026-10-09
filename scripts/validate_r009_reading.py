#!/usr/bin/env python3
"""R009 original body-receipt audit; public runner checks R002 byte-SHA metadata,
not private EPUB prose. An actual source SHA/paragraph private comparison is
recorded separately in LOCAL_SOURCE_VERIFICATION.md.
"""
import csv,json,re,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
REC=ROOT/"cangjie/reading/R009/wanming_receipts.jsonl"
INDEX=ROOT/"cangjie/reading/R009/wanming_source_index.csv"
SOURCE=ROOT/"sources/metadata/wanming_v13_spine.csv"
SOURCE_SHA="a8f3b43dcd496822cd384ac8e9aa85f7dc374f8430f06c6f8321c26825093082"
CLOSE={41,51,60,61,65,68,70,71,74,75,80}
def main():
  fail=[]
  def ck(test,msg):
    if not test:fail.append(msg)
  with SOURCE.open(encoding="utf-8",newline="") as f:
    original={int(row["narrative_ordinal"]):row for row in csv.DictReader(f) if row["narrative_ordinal"]}
  with INDEX.open(encoding="utf-8",newline="") as f:index=list(csv.DictReader(f))
  records=[json.loads(r) for r in REC.read_text("utf-8").splitlines() if r.strip()]
  ck(len(records)==40 and len(index)==40,"40 unique receipts and 40 indexed source chapters required")
  ck([r["narrative_ordinal"] for r in records]==list(range(41,81)),"R009 records not in exact 041—080 ordinal range")
  ck([int(r["narrative_ordinal"]) for r in index]==list(range(41,81)),"R009 index not in exact 041—080 range")
  total=0;anchors=0;seen=set();close_count=0
  for r,ix in zip(records,index):
    n=r["narrative_ordinal"];m=original.get(n)
    if not m:fail.append(f"{n} missing R002 source");continue
    ck(r["book_slug"]=="wanming" and r["source_epub_sha256"]==SOURCE_SHA,f"{n} EPUB SHA incorrect")
    ck(r["spine_index"]==int(m["spine_index"])==int(ix["spine_index"]),f"{n} spine incorrect")
    ck(r["epub_path"]==m["epub_path"]==ix["epub_path"],f"{n} OPF ZIP path incorrect")
    ck(r["chapter_sha256"]==m["chapter_sha256"]==ix["chapter_sha256"],f"{n} original ZIP chapter bytes incorrectly identified")
    p=int(m["nonempty_paragraphs"])
    ck(r["body_paragraph_count"]==r["observed_paragraph_count"]==int(ix["body_paragraph_count"])==p,f"{n} body paragraph count mismatch")
    ck(r["mode"]==ix["receipt_mode"]==("CLOSE_READ" if n in CLOSE else "FULL_TEXT_READ"),f"{n} close and full-read modes incorrect")
    ck(r["fixture_only"] is False and r["round_id"]=="R009" and r["reader_session_id"],f"{n} fixture or reader session invalid")
    ck(r["paragraph_normalization"]=="xhtml_visible_text_trim_whitespace_v1",f"{n} paragraph hashing normalization invalid")
    ck(len(r["event_chain"])==2 and all(isinstance(x,str) and len(x)>=22 for x in r["event_chain"]),f"{n} distinct literary event and agency evidence insufficient")
    ck(len(r["open_questions"])>=1,f"{n} omitted unresolved next-chapter consequence")
    ck(r["event_chain"][0] not in seen,f"{n} duplicated episode apparently auto-copied")
    seen.add(r["event_chain"][0])
    a=r["anchors"]
    ck(len(a)>0 and all(0<x["paragraph_index"]<=p and re.fullmatch(r"[0-9a-f]{64}",x["paragraph_sha256"]) for x in a),f"{n} paragraph anchors incomplete")
    ck(";".join(f'{x["paragraph_index"]}:{x["paragraph_sha256"]}' for x in a)==ix["paragraph_index_sha256_anchors"],f"{n} public receipt vs source locator mismatch")
    if n in CLOSE:
      close_count+=1;ck(len(r["mechanism_claims"])>=1,f"{n} focus chapter missing detailed hypothesis")
      for c in r["mechanism_claims"]:
        ck(c["verification_state"]=="PROVISIONAL" and c["counterexample_status"] in ("FOUND","SEARCHED_NONE"),f"{n} hypothesis over-claimed")
        ck(all(z in {x["anchor_id"] for x in a} for z in c["support_anchor_ids"]),f"{n} claim points to non-existent original anchor")
    total+=p;anchors+=len(a)
  ck(total==2327,"original 40 chapters total paragraphs drifted")
  ck(anchors==62,"original 62 saved paragraph anchors missing")
  ck(close_count==11,"R009 focus chapter count must be 11")
  for f in ["cangjie/reading/wanming_041_080.md","cangjie/reading/R009/wanming_continuity.md","cangjie/reading/R009/LOCAL_SOURCE_VERIFICATION.md"]:
    ck((ROOT/f).exists(),"missing literary artifact "+f)
  current=json.loads((ROOT/"CURRENT_ROUND.json").read_text("utf-8"))
  token=current.get("current_round","");num=int(token[1:]) if token.startswith("R") and token[1:].isdigit() else -1
  ck(9<=num<=89,"R009 historical validator cannot run before R009")
  if num==9:
    ck(current["full_text_read_chapters"]["wanming"]==40,"can't increment before R009 formal PASS")
    ck(current["full_text_read_chapters"]["tiexuecanming"]==40,"R008 count regressed")
  else:
    ck(current["full_text_read_chapters"]["wanming"]>=80,"R009 certified full reading count regressed")
    ck(current["full_text_read_chapters"]["tiexuecanming"]>=40,"R008 certified full reading count regressed")
  for f in fail:print("FAIL",f)
  if fail:return 1
  print("PASS R009: 40 original consecutive wanming narrative ordinals 041-080, 2327 body paragraphs, 62 private anchored SHA256 locators, 11 provisional close-reading chapters, 40 distinct event/agency notes, all R002 chapter SHA values; no private text or independent performance score in public CI")
  return 0
if __name__=="__main__":sys.exit(main())
