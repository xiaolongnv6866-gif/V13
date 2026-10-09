#!/usr/bin/env python3
"""R017 source metadata, chapter receipts, original paragraph locator SHA structure.
PUBLIC SOURCE_STRUCTURE_ONLY: this CI runner cannot read the user's private EPUB.
"""
import csv,json,re,sys
from pathlib import Path
root=Path(__file__).resolve().parents[1]
source_sha="a8f3b43dcd496822cd384ac8e9aa85f7dc374f8430f06c6f8321c26825093082"
focus={201,202,203,207,212,213,214,216,217,219,220,222,223,225,229,231,233,237,239,240}
with (root/"sources/metadata/wanming_v13_spine.csv").open(encoding="utf-8",newline="") as f:
    master={int(v["narrative_ordinal"]):v for v in csv.DictReader(f) if v["narrative_ordinal"]}
with (root/"cangjie/reading/R017/wanming_source_index.csv").open(encoding="utf-8",newline="") as f:
    index=list(csv.DictReader(f))
receipts=[json.loads(x) for x in (root/"cangjie/reading/R017/wanming_receipts.jsonl").read_text(encoding="utf-8").splitlines() if x.strip()]
errors=[]
def ck(cond,label):
    if not cond:errors.append(label)
ck(len(receipts)==len(index)==40,"R017 must have 40 independent originals")
ck([r["narrative_ordinal"] for r in receipts]==list(range(201,241)),"Narrative ordinals 201..240 missing, repeated or reordered")
ck([int(v["narrative_ordinal"]) for v in index]==list(range(201,241)),"Source index ordinals misordered")
seen=set();total=anchors=close=0;digest=2166136261
for r,i in zip(receipts,index):
    n=r["narrative_ordinal"];m=master[n];p=int(m["nonempty_paragraphs"])
    ck(r["book_slug"]=="wanming" and r["source_epub_sha256"]==source_sha,str(n)+" original source fingerprint")
    ck(r["spine_index"]==int(i["spine_index"])==int(m["spine_index"])==n+14,str(n)+" OPF spine")
    ck(r["epub_path"]==i["epub_path"]==m["epub_path"]==f"OEBPS/Text/Chapter_{n+11:04d}.xhtml",str(n)+" original ZIP member")
    ck(r["chapter_sha256"]==i["chapter_sha256"]==m["chapter_sha256"],str(n)+" chapter original SHA")
    ck(r["body_paragraph_count"]==r["observed_paragraph_count"]==int(i["nonempty_paragraphs"])==p,str(n)+" original para count")
    ck(r["mode"]==i["mode"]==("CLOSE_READ" if n in focus else "FULL_TEXT_READ"),str(n)+" mode mapping")
    ck(r.get("fixture_only") is False and r.get("round_id")=="R017",str(n)+" not source")
    ck(len(r.get("reader_session_id",""))>=18 and r.get("paragraph_normalization")=="xhtml_visible_text_trim_whitespace_v1",str(n)+" original reader metadata")
    ev=r["event_chain"]
    ck(type(ev) is list and len(ev)==2 and all(type(s) is str and len(s.strip())>20 for s in ev),str(n)+" two original narrative event steps")
    ck(ev[0] not in seen,str(n)+" cloned event claim")
    seen.add(ev[0])
    ck(bool(r["open_questions"]),str(n)+" missing consequence question")
    aa=r["anchors"]
    ck(len(aa)==(3 if n in focus else 1),str(n)+" locator count")
    ck(all(0<a["paragraph_index"]<=p and re.fullmatch("[0-9a-f]{64}",a["paragraph_sha256"]) for a in aa),str(n)+" SHA syntax/range")
    ck(";".join(f'{a["paragraph_index"]}:{a["paragraph_sha256"]}' for a in aa)==i["paragraph_sha256_anchors"],str(n)+" independent index mismatch")
    if n in focus:
        close+=1; ck(len(r["mechanism_claims"])>=1,str(n)+" focused analysis missing")
        for c in r["mechanism_claims"]:
            ck(c["verification_state"]=="PROVISIONAL" and c["counterexample_status"] in ("FOUND","SEARCHED_NONE"),str(n)+" improper certainty")
            ck(set(c["support_anchor_ids"])<={a["anchor_id"] for a in aa},str(n)+" dangling support anchor")
            ck(len(c["alternative_rendering_loss"])>=40 and len(c["failure_boundary"])>=40,str(n)+" no counterfactual/boundary")
    for a in aa:
        for ch in f'{n}/{a["paragraph_index"]}/{a["paragraph_sha256"]}\n':
            digest=((digest^ord(ch))*16777619)&0xffffffff
    total+=p;anchors+=len(aa)
ck((total,anchors,close)==(1920,80,20),"R017 original index 1920 paragraphs/80 anchors/20 close required")
ck(f'{digest:08x}'=="da1bad61","R017 private original anchor digest mismatch")
for path in ["cangjie/reading/wanming_201_240.md","cangjie/reading/R017/wanming_continuity.md","cangjie/reading/R017/LOCAL_SOURCE_VERIFICATION.md","runs/R017.md"]:
    ck((root/path).is_file(),"missing required report "+path)
state=json.loads((root/"CURRENT_ROUND.json").read_text(encoding="utf-8"))
current=int(state["current_round"][1:])
ck(current>=17,"R017 prematurely started")
if current==17:
    ck(state["full_text_read_chapters"]=={"wanming":200,"tiexuecanming":200},"R017 must not count before PASS")
else:
    ck(state["full_text_read_chapters"]["wanming"]>=240 and state["full_text_read_chapters"]["tiexuecanming"]>=200,"R017 certified counts regressed")
for error in errors:print("FAIL:",error)
if errors:sys.exit(1)
print("PASS R017 public SOURCE_STRUCTURE_ONLY: original Wanming 201..240 40 authored receipt records, 1920 source-index paragraphs, 80 locators private-derived SHA FNV32 da1bad61, 20 provisional CLOSE_READ, stage correctness")
