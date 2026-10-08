#!/usr/bin/env python3
"""R013 Wanming original 121-160 immutable R002 chapter source and literary evidence.
Public CI checks structure/grounded metadata, not private original book prose.
"""
from pathlib import Path
import json,csv,re,sys
root=Path(__file__).resolve().parents[1]
receipts_file=root/"cangjie/reading/R013/wanming_receipts.jsonl"
index_file=root/"cangjie/reading/R013/wanming_source_index.csv"
sha="a8f3b43dcd496822cd384ac8e9aa85f7dc374f8430f06c6f8321c26825093082"
focus={121,125,128,130,133,135,137,139,140,143,147,149,150,154,156,157,159,160}
rs=[json.loads(x) for x in receipts_file.read_text("utf8").splitlines() if x.strip()]
with index_file.open(encoding="utf8",newline="") as f: ix=list(csv.DictReader(f))
with (root/"sources/metadata/wanming_v13_spine.csv").open(encoding="utf8",newline="") as f: md={int(x["narrative_ordinal"]):x for x in csv.DictReader(f) if x["narrative_ordinal"]}
errors=[]
def verify(ok,msg):
 if not ok:errors.append(msg)
verify(len(rs)==len(ix)==40,"Expected 40 original distinct R013 source receipts")
verify([x["narrative_ordinal"] for x in rs]==list(range(121,161)),"Expected complete ordered 121-160")
verify([int(x["narrative_ordinal"]) for x in ix]==list(range(121,161)),"Source chapter index must exactly align")
counts=0;anchors=0;close_count=0;events=set();checksum=2166136261
for r,i in zip(rs,ix):
 n=r["narrative_ordinal"];m=md[n];p=int(m["nonempty_paragraphs"])
 verify(r["book_slug"]=="wanming" and r["source_epub_sha256"]==sha,f"{n}: book id or SHA")
 verify(r["spine_index"]==int(m["spine_index"])==int(i["spine_index"]),f"{n}: OPF spine index")
 verify(r["epub_path"]==m["epub_path"]==i["epub_path"],f"{n}: source ZIP path")
 verify(r["chapter_sha256"]==m["chapter_sha256"]==i["chapter_sha256"],f"{n}: original member hash")
 verify(r["body_paragraph_count"]==r["observed_paragraph_count"]==p==int(i["nonempty_paragraphs"]),f"{n}: original paragraph count")
 close=n in focus
 verify(r["mode"]==i["mode"]==("CLOSE_READ" if close else "FULL_TEXT_READ"),f"{n}: reading mode")
 verify(r["fixture_only"] is False and r["round_id"]=="R013" and len(r["reader_session_id"])>8,f"{n}: chapter session")
 verify(r["paragraph_normalization"]=="xhtml_visible_text_trim_whitespace_v1",f"{n}: source normalization")
 verify(len(r["event_chain"])==2 and all(len(x)>24 for x in r["event_chain"]),f"{n}: literary event and agency evidence")
 verify(r["event_chain"][0] not in events,f"{n}: duplicate textual event")
 events.add(r["event_chain"][0])
 verify(len(r["open_questions"])>=1,f"{n}: missing unresolved consequence")
 a=r["anchors"]
 verify(len(a)==(3 if close else 1) and all(0<x["paragraph_index"]<=p and re.fullmatch("[a-f0-9]{64}",x["paragraph_sha256"]) for x in a),f"{n}: source anchor")
 verify(";".join(f'{x["paragraph_index"]}:{x["paragraph_sha256"]}' for x in a)==i["paragraph_sha256_anchors"],f"{n}: receipt and index SHA disagreement")
 if close:
  close_count+=1
  verify(len(r["mechanism_claims"])>=1,f"{n}: no close reading")
  for cl in r["mechanism_claims"]:
   verify(cl["verification_state"]=="PROVISIONAL" and cl["counterexample_status"]=="SEARCHED_NONE",f"{n}: unearned verified claim")
   verify(set(cl["support_anchor_ids"]) <= {x["anchor_id"] for x in a},f"{n}: lost paragraph pointer")
   verify(bool(cl["alternative_rendering_loss"]) and bool(cl["failure_boundary"]),f"{n}: unsupported mechanism reasoning")
 for q in sorted(a,key=lambda x:x["paragraph_index"]):
  for ch in f'{n}/{q["paragraph_index"]}/{q["paragraph_sha256"]}\n':
   checksum=((checksum^ord(ch))*16777619)&0xffffffff
 anchors+=len(a);counts+=p
verify(counts==2086 and anchors==76 and close_count==18,"R013 2086 paragraphs/76 source SHA/18 close studies")
verify(f'{checksum:08x}'=="cf9513b1","Private original vs staged Github source digest")
for p in ["cangjie/reading/wanming_121_160.md","cangjie/reading/R013/wanming_continuity.md","cangjie/reading/R013/LOCAL_SOURCE_VERIFICATION.md"]:
 verify((root/p).is_file(),f"Missing original literary artifact {p}")
state=json.loads((root/"CURRENT_ROUND.json").read_text("utf8"))
rnd=int(state["current_round"][1:])
verify(rnd>=13,"Cannot run R013 ahead of actual work")
if rnd==13:verify(state["full_text_read_chapters"]=={"wanming":120,"tiexuecanming":120},"Do not prematurely count pending R013")
else:verify(state["full_text_read_chapters"]["wanming"]>=160 and state["full_text_read_chapters"]["tiexuecanming"]>=120,"Certified R013 reading count regressed")
for e in errors:print("FAIL:",e)
if errors:sys.exit(1)
print("PASS R013: 40 real Wanming ordinals 121-160, 2086 original paragraph counts, 76 private SHA256 locators, 18 provisional focused chapter mechanisms, 40 distinct literary event/agency notes; public SOURCE_STRUCTURE_ONLY")
