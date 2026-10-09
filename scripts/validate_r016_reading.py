#!/usr/bin/env python3
"""R016 literary source evidence and chapter-receipt integrity; public SOURCE_STRUCTURE_ONLY.
The GitHub runner has NO private original EPUB; source SHA-locator contents must also
be crosschecked locally with the user's copyrighted original in a private environment.
"""
import csv,json,re,sys
from pathlib import Path
root=Path(__file__).resolve().parents[1]
focus={161,163,165,168,170,173,176,178,180,182,184,186,188,190,191,193,195,197,199,200}
source_sha="9100bbcdb9f52bcd5458cbda92e16b646489efbc00df5161ed568ebac83ffbaf"
with (root/"sources/metadata/tiexuecanming_v13_spine.csv").open(encoding="utf8",newline="") as f:
    metadata={int(row["narrative_ordinal"]):row for row in csv.DictReader(f) if row["narrative_ordinal"]}
with (root/"cangjie/reading/R016/tiexue_source_index.csv").open(encoding="utf8",newline="") as f: indexes=list(csv.DictReader(f))
rs=[json.loads(s) for s in (root/"cangjie/reading/R016/tiexue_receipts.jsonl").read_text(encoding="utf8").splitlines() if s.strip()]
errors=[]
def ck(ok,msg):
    if not ok:errors.append(msg)
ck(len(rs)==len(indexes)==40,"R016 requires forty chapter records")
ck([r["narrative_ordinal"] for r in rs]==list(range(161,201)),"R016 narrative ordinal must be exactly 161..200")
ck([int(i["narrative_ordinal"]) for i in indexes]==list(range(161,201)),"R016 source index non-contiguous")
ck(all(metadata[x]["chapter_title"].startswith("第197章") for x in (197,198)),"Both independent narrative ordinals must retain repeated printed chapter197")
total=locators=close=0;seen=set();digest=2166136261
for r,i in zip(rs,indexes):
 n=r["narrative_ordinal"];m=metadata[n];p=int(m["nonempty_paragraphs"])
 ck(r["book_slug"]=="tiexuecanming" and r["source_epub_sha256"]==source_sha,f"{n} wrong book/EPUB SHA")
 ck(r["spine_index"]==int(m["spine_index"])==int(i["spine_index"])==n+16,f"{n} wrong OPF spine")
 ck(r["epub_path"]==m["epub_path"]==i["epub_path"]==f"OEBPS/Text/chapter{n+7}.html",f"{n} original ZIP member mismatch")
 ck(r["chapter_sha256"]==m["chapter_sha256"]==i["chapter_sha256"],f"{n} original member-byte SHA not matching frozen R002")
 ck(r["body_paragraph_count"]==r["observed_paragraph_count"]==p==int(i["nonempty_paragraphs"]),f"{n} original paragraph index drift")
 ck(r["mode"]==i["mode"]==("CLOSE_READ" if n in focus else "FULL_TEXT_READ"),f"{n} reading mode incorrect")
 ck(r.get("round_id")=="R016" and r.get("fixture_only") is False and len(r.get("reader_session_id",""))>7,f"{n} invalid original reading receipt")
 ck(r.get("paragraph_normalization")=="xhtml_visible_text_trim_whitespace_v1",f"{n} original paragraph normalization")
 events=r["event_chain"]
 ck(len(events)==2 and all(type(v) is str and len(v)>10 for v in events),f"{n} original, substantive two narrative events required")
 ck(events[0] not in seen,f"{n} non-unique first event")
 seen.add(events[0])
 ck(len(r["open_questions"])>=1,f"{n} independent long-form consequence missing")
 aa=r["anchors"];isclose=n in focus
 ck(len(aa)==(3 if isclose else 1),f"{n} original SHA locator count")
 ck(all(0<a["paragraph_index"]<=p and re.fullmatch(r"[a-f0-9]{64}",a["paragraph_sha256"]) for a in aa),f"{n} original SHA locator invalid")
 ck(";".join(f'{a["paragraph_index"]}:{a["paragraph_sha256"]}' for a in aa)==i["paragraph_sha256_anchors"],f"{n} original index-receipt locator drift")
 if isclose:
  close+=1
  ck(len(r["mechanism_claims"])>=1,f"{n} focus mechanism missing")
  for c in r["mechanism_claims"]:
   ck(c["verification_state"]=="PROVISIONAL" and c["counterexample_status"] in ("FOUND","SEARCHED_NONE"),f"{n} premature claimed verified")
   ck(set(c["support_anchor_ids"])<={a["anchor_id"] for a in aa},f"{n} unsupported paragraph reference")
   ck(len(c["alternative_rendering_loss"])>35 and len(c["failure_boundary"])>35,f"{n} no counterfactual or boundary")
 for a in aa:
  for char in f'{n}/{a["paragraph_index"]}/{a["paragraph_sha256"]}\n':
   digest=((digest^ord(char))*16777619)&0xffffffff
 total+=p;locators+=len(aa)
ck((total,locators,close)==(2510,80,20),"R016 must contain original-index 2510 paragraphs, 80 SHA, 20 CLOSE_READ")
ck(f'{digest:08x}'=="4c010a0b","private-original-to-staged locators FNV32 SHA consistency drift")
for p in ["cangjie/reading/tiexue_161_200.md","cangjie/reading/R016/tiexue_continuity.md","cangjie/reading/R016/LOCAL_SOURCE_VERIFICATION.md","runs/R016.md"]:
 ck((root/p).is_file(),"Missing authored R016 required report: "+p)
state=json.loads((root/"CURRENT_ROUND.json").read_text(encoding="utf8"))
current=int(state["current_round"][1:])
ck(current>=16,"R016 cannot be validated before reaching its stage")
if current==16:
 ck(state["full_text_read_chapters"]=={"wanming":200,"tiexuecanming":160},"R016 not yet PASSED cannot count its chapters")
else:
 ck(state["full_text_read_chapters"]["wanming"]>=200 and state["full_text_read_chapters"]["tiexuecanming"]>=200,"R016 count regressed")
for e in errors:print("FAIL:",e)
if errors:sys.exit(1)
print("PASS R016: 40 distinct original Tiexue chapters161-200, 2510 indexed paragraphs, 80 private-derived SHA locators FNV32 4c010a0b, 20 provisional CLOSE_READ, repeated printed chapter197 mapped to two ordinals; public SOURCE_STRUCTURE_ONLY")
