#!/usr/bin/env python3
"""R011 frozen reading protocol audit (public R002 metadata+receipt integrity).
This program does NOT claim public Actions contains the private original EPUB.
"""
import csv,json,re,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
R=ROOT/"cangjie/reading/R011/wanming_receipts.jsonl"
INDEX=ROOT/"cangjie/reading/R011/wanming_source_index.csv"
SRC=ROOT/"sources/metadata/wanming_v13_spine.csv"
SHA="a8f3b43dcd496822cd384ac8e9aa85f7dc374f8430f06c6f8321c26825093082"
CLOSE={81,88,95,99,100,102,105,106,107,110,112,113,115,116,118,119,120}
REPAIRED_P83="6d1480f456e7236695a8a2ed0ed413b720f29bda17cf855a8f49b1e53419fd22"
def main():
    errors=[]
    def ck(cond,msg):
        if not cond:errors.append(msg)
    with SRC.open(encoding="utf-8",newline="") as f:original={int(x["narrative_ordinal"]):x for x in csv.DictReader(f) if x["narrative_ordinal"]}
    with INDEX.open(encoding="utf-8",newline="") as f:index=list(csv.DictReader(f))
    receipts=[json.loads(s) for s in R.read_text("utf-8").splitlines() if s.strip()]
    ck(len(receipts)==40 and len(index)==40,"R011 must have exactly 40 independent full chapter receipts")
    ck([x["narrative_ordinal"] for x in receipts]==list(range(81,121)),"R011 081-120 actual ordinal gap or duplicate")
    ck([int(x["narrative_ordinal"]) for x in index]==list(range(81,121)),"R011 source index incorrect")
    paragraphs=0;anchors=0;close_count=0;events=set();h=2166136261
    for r,ix in zip(receipts,index):
        n=r["narrative_ordinal"];m=original.get(n)
        if not m:errors.append(f"{n} not found in R002");continue
        ck(r["book_slug"]=="wanming" and r["source_epub_sha256"]==SHA,f"{n} source EPUB SHA invalid")
        ck(r["spine_index"]==int(m["spine_index"])==int(ix["spine_index"]),f"{n} OPF spine mismatch")
        ck(r["epub_path"]==m["epub_path"]==ix["epub_path"],f"{n} original ZIP path mismatch")
        ck(r["chapter_sha256"]==m["chapter_sha256"]==ix["chapter_sha256"],f"{n} original chapter member sha mismatch")
        p=int(m["nonempty_paragraphs"])
        ck(r["body_paragraph_count"]==r["observed_paragraph_count"]==int(ix["nonempty_paragraphs"])==p,f"{n} incomplete original source paragraph count")
        ck(r["mode"]==ix["reading_mode"]==("CLOSE_READ" if n in CLOSE else "FULL_TEXT_READ"),f"{n} original whole-body mode mismatch")
        ck(r["fixture_only"] is False and r["round_id"]=="R011" and isinstance(r["reader_session_id"],str) and len(r["reader_session_id"])>8,f"{n} no chapter reading session")
        ck(r["paragraph_normalization"]=="xhtml_visible_text_trim_whitespace_v1",f"{n} paragraph normalization drift")
        ck(len(r["event_chain"])==2 and all(isinstance(x,str) and len(x)>24 for x in r["event_chain"]),f"{n} substantive per-chapter agency/event evidence insufficient")
        ck(r["event_chain"][0] not in events,f"{n} copied same event across unrelated chapters")
        events.add(r["event_chain"][0])
        ck(len(r["open_questions"])>=1,f"{n} unresolved consequence missing")
        loc=r["anchors"]
        ck(len(loc)>0 and all(0<a["paragraph_index"]<=p and re.fullmatch(r"[0-9a-f]{64}",a["paragraph_sha256"]) for a in loc),f"{n} invalid source paragraph SHA locator")
        ck(";".join(f'{a["paragraph_index"]}:{a["paragraph_sha256"]}' for a in loc)==ix["paragraph_index_sha256_anchors"],f"{n} staged SHA index disagree")
        if n==83:
            ck(len(loc)==1 and loc[0]["paragraph_index"]==26 and loc[0]["paragraph_sha256"]==REPAIRED_P83,"R011 checkpoint bad 61-hex SHA for original paragraph83/26 not repaired")
        if n in CLOSE:
            close_count+=1
            ck(len(r["mechanism_claims"])>=1,f"{n} CLOSE_READ without scene mechanism")
            for q in r["mechanism_claims"]:
                ck(q["verification_state"]=="PROVISIONAL" and q["counterexample_status"]=="SEARCHED_NONE",f"{n} claimed whole book mechanism too early")
                ck(set(q["support_anchor_ids"]) <= {a["anchor_id"] for a in loc},f"{n} source claim anchor missing")
                ck(bool(q["alternative_rendering_loss"]) and bool(q["failure_boundary"]),f"{n} no alternate narrative or failure boundary")
        for a in sorted(loc,key=lambda x:x["paragraph_index"]):
            for char in f'{n}/{a["paragraph_index"]}/{a["paragraph_sha256"]}\n':h=((h^ord(char))*16777619)&0xffffffff
        paragraphs+=p;anchors+=len(loc)
    ck(paragraphs==2295,"R011 original paragraph count must be 2295")
    ck(anchors==74,"74 source paragraph hash locators required")
    ck(close_count==17,"17 focus chapters (including first/mid/last) required")
    ck(format(h,"08x")=="45cc01df","Private original to public receipt anchors changed")
    for p in ["cangjie/reading/wanming_081_120.md","cangjie/reading/R011/wanming_continuity.md","cangjie/reading/R011/LOCAL_SOURCE_VERIFICATION.md","cangjie/reading/R011/wanming_081_087_checkpoint.jsonl"]:
        ck((ROOT/p).is_file(),"R011 missing narrative artifact "+p)
    s=json.loads((ROOT/"CURRENT_ROUND.json").read_text("utf-8"));rnd=s.get("current_round","");num=int(rnd[1:]) if rnd.startswith("R") and rnd[1:].isdigit() else -1
    ck(11<=num<=89,"R011 validator unexpectedly invoked in prior round")
    if num==11:
        ck(s["full_text_read_chapters"]=={"wanming":80,"tiexuecanming":80},"R011 cannot increase reading count while IN_PROGRESS")
    elif num>=12:
        ck(s["full_text_read_chapters"]["wanming"]>=120 and s["full_text_read_chapters"]["tiexuecanming"]>=80,"R011 certified literary reading count regressed")
    for error in errors:print("FAIL:",error)
    if errors:return 1
    print("PASS R011: 40 distinct original Wanming ordinals 081-120, 2295 source paragraph counts, 74 anchored SHA locators/private digest 45cc01df, 17 provisional CLOSE_READ studies, Ch83 source typo correctly repaired; no novel prose or original-skill performance claims in public")
    return 0
if __name__=="__main__":sys.exit(main())
