#!/usr/bin/env python3
"""V13 R014 public source-structure and substantive literary receipts validator.
Not proof of private-original full-body semantic comprehension by GitHub runner.
"""
import csv,json,re,sys
from pathlib import Path
root=Path(__file__).resolve().parents[1]
focus={121,122,127,129,130,135,140,142,148,152,153,155,157,160}
sha="9100bbcdb9f52bcd5458cbda92e16b646489efbc00df5161ed568ebac83ffbaf"
with (root/"sources/metadata/tiexuecanming_v13_spine.csv").open(encoding="utf8",newline="") as f:
    source={int(m["narrative_ordinal"]):m for m in csv.DictReader(f) if m["narrative_ordinal"]}
with (root/"cangjie/reading/R014/tiexue_source_index.csv").open(encoding="utf8",newline="") as f:
    index=list(csv.DictReader(f))
rs=[json.loads(x) for x in (root/"cangjie/reading/R014/tiexue_receipts.jsonl").read_text("utf8").splitlines() if x.strip()]
fail=[]
def ck(cond,msg):
    if not cond:fail.append(msg)
ck(len(rs)==len(index)==40,"R014 must contain 40 distinct narrative chapter receipts")
ck([r["narrative_ordinal"] for r in rs]==list(range(121,161)),"R014 ordinals must be 121--160 exactly")
ck([int(r["narrative_ordinal"]) for r in index]==list(range(121,161)),"R014 source index must be 121--160")
para=anchors=close=0;events=set();digest=2166136261
for r,i in zip(rs,index):
 n=r["narrative_ordinal"];m=source[n];p=int(m["nonempty_paragraphs"])
 ck(r["book_slug"]=="tiexuecanming" and r["source_epub_sha256"]==sha,f"{n} wrong source book")
 ck(r["spine_index"]==int(m["spine_index"])==int(i["spine_index"]),f"{n} wrong OPF spine")
 ck(r["epub_path"]==m["epub_path"]==i["epub_path"],f"{n} wrong real ZIP chapter (possible empty divider confusion)")
 ck(r["chapter_sha256"]==m["chapter_sha256"]==i["chapter_sha256"],f"{n} original chapter-byte SHA mismatched")
 ck(r["body_paragraph_count"]==r["observed_paragraph_count"]==p==int(i["nonempty_paragraphs"]),f"{n} nonempty XHTML paragraph count drift")
 ck(r["mode"]==i["mode"]==("CLOSE_READ" if n in focus else "FULL_TEXT_READ"),f"{n} reading mode wrong")
 ck(r["round_id"]=="R014" and r["fixture_only"] is False and len(r["reader_session_id"])>6,f"{n} actual reading receipt missing")
 ck(r["paragraph_normalization"]=="xhtml_visible_text_trim_whitespace_v1",f"{n} source normalization wrong")
 ck(len(r["event_chain"])==2 and all(isinstance(s,str) and len(s)>24 for s in r["event_chain"]),f"{n} specific event/agency evidence insufficient")
 ck(r["event_chain"][0] not in events,f"{n} copied event")
 events.add(r["event_chain"][0])
 ck(len(r["open_questions"])>=1,f"{n} follow-up consequence missing")
 a=r["anchors"];is_focus=n in focus
 ck(len(a)==(3 if is_focus else 1) and all(0<x["paragraph_index"]<=p and re.fullmatch("[0-9a-f]{64}",x["paragraph_sha256"]) for x in a),f"{n} original paragraph hashes invalid")
 ck(";".join(f'{x["paragraph_index"]}:{x["paragraph_sha256"]}' for x in a)==i["paragraph_sha256_anchors"],f"{n} index-receipt source locator inconsistency")
 if n==130:
    ck("chapter137.html" in r["epub_path"] and r["spine_index"]==146,f"{n} mistaken non-narrative empty XHTML as original narrative chapter")
 if is_focus:
    close+=1
    ck(len(r["mechanism_claims"])>=1,f"{n} focused mechanism missing")
    for claim in r["mechanism_claims"]:
        ck(claim["verification_state"]=="PROVISIONAL" and claim["counterexample_status"] in ("FOUND","SEARCHED_NONE"),f"{n} premature literature certification")
        ck(set(claim["support_anchor_ids"]) <= {x["anchor_id"] for x in a},f"{n} claim anchor not located")
        ck(bool(claim["alternative_rendering_loss"]) and bool(claim["failure_boundary"]),f"{n} missing counterfactual or limit")
 for x in sorted(a,key=lambda v:v["paragraph_index"]):
    for c in f'{n}/{x["paragraph_index"]}/{x["paragraph_sha256"]}\n':
        digest=((digest^ord(c))*16777619)&0xffffffff
 para+=p;anchors+=len(a)
ck(para==2426 and anchors==68 and close==14,"R014 2426 paragraphs / 68 source anchors / 14 focus chapters expected")
ck(f'{digest:08x}'=="cd98332d","R014 original-private vs staged-public paragraph SHA anchor digest drift")
for path in ["cangjie/reading/tiexue_121_160.md","cangjie/reading/R014/tiexue_continuity.md","cangjie/reading/R014/LOCAL_SOURCE_VERIFICATION.md"]:
 ck((root/path).is_file(),"missing literary analysis artifact "+path)
state=json.loads((root/"CURRENT_ROUND.json").read_text("utf8"));current=int(state["current_round"][1:])
ck(current>=14,"R014 validator used before reading round")
if current==14:
 ck(state["full_text_read_chapters"]=={"wanming":160,"tiexuecanming":120},"must not count R014 before formal PASS")
else:
 ck(state["full_text_read_chapters"]["wanming"]>=160 and state["full_text_read_chapters"]["tiexuecanming"]>=160,"R014 official completed chapter count regressed")
for error in fail:print("FAIL:",error)
if fail:sys.exit(1)
print("PASS R014: 40 distinct original TiexueCanming chapters 121--160, 2426 indexed source paragraphs, 68 privately derived SHA locators (digest cd98332d), 14 PROVISIONAL focused studies, corrected non-narrative spine145/chapter136 gap; public SOURCE_STRUCTURE_ONLY")
