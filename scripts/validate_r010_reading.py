#!/usr/bin/env python3
"""R010: validate complete 041-080 TiexueCanming receipts and literary records.
Public GitHub runner validates SHA mappings and structural evidence only.
Actual content reading and private EPUB paragraph SHA were separately checked.
"""
import csv,json,re,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
RECEIPTS=ROOT/"cangjie/reading/R010/tiexue_receipts.jsonl"
INDEX=ROOT/"cangjie/reading/R010/tiexue_source_index.csv"
ORIGINAL=ROOT/"sources/metadata/tiexuecanming_v13_spine.csv"
CLOSE={41,55,57,60,62,65,67,73,79,80}
SHA="9100bbcdb9f52bcd5458cbda92e16b646489efbc00df5161ed568ebac83ffbaf"
def main():
    errors=[]
    def check(cond,msg):
        if not cond:errors.append(msg)
    with ORIGINAL.open(encoding="utf-8",newline="") as f:
        meta={int(r["narrative_ordinal"]):r for r in csv.DictReader(f) if r["narrative_ordinal"]}
    with INDEX.open(encoding="utf-8",newline="") as f:index=list(csv.DictReader(f))
    rr=[json.loads(l) for l in RECEIPTS.read_text("utf-8").splitlines() if l.strip()]
    check(len(rr)==40 and len(index)==40,"Must have 40 unique chapter receipts and index items")
    check([r["narrative_ordinal"] for r in rr]==list(range(41,81)),"R010 wrong ordinal range / repeat / skip")
    check([int(r["narrative_ordinal"]) for r in index]==list(range(41,81)),"Source index gap or duplicate")
    total=0;anchors=0;close=0;event_set=set()
    for r,ix in zip(rr,index):
        n=r["narrative_ordinal"];s=meta.get(n)
        if not s:errors.append("Missing R002 chapter "+str(n));continue
        check(r["book_slug"]=="tiexuecanming" and r["source_epub_sha256"]==SHA,f"{n}: wrong original source")
        check(r["spine_index"]==int(s["spine_index"])==int(ix["spine_index"]),f"{n}: wrong source OPF spine")
        check(r["epub_path"]==s["epub_path"]==ix["epub_path"],f"{n}: ZIP internal path mismatch")
        check(r["chapter_sha256"]==s["chapter_sha256"]==ix["chapter_sha256"],f"{n}: original chapter SHA mismatch")
        p=int(s["nonempty_paragraphs"])
        check(r["body_paragraph_count"]==r["observed_paragraph_count"]==p==int(ix["nonempty_paragraphs"]),f"{n}: body paragraph incomplete or mismatch")
        check(r["mode"]==ix["mode"]==("CLOSE_READ" if n in CLOSE else "FULL_TEXT_READ"),f"{n}: reading mode changed")
        check(r["fixture_only"] is False and r["round_id"]=="R010" and isinstance(r["reader_session_id"],str) and len(r["reader_session_id"])>7,f"{n}: fixture or real reading session absent")
        check(r["paragraph_normalization"]=="xhtml_visible_text_trim_whitespace_v1",f"{n}: normalization missing")
        check(len(r["event_chain"])==2 and all(isinstance(t,str) and len(t)>17 for t in r["event_chain"]),f"{n}: incomplete actual episode/character choice")
        check(r["event_chain"][0] not in event_set,f"{n}: duplicate event summary")
        event_set.add(r["event_chain"][0])
        check(len(r["open_questions"])>=1,f"{n}: consequences not tracked")
        a=r["anchors"]
        check(len(a)>0 and all(0<x["paragraph_index"]<=p and re.fullmatch(r"[0-9a-f]{64}",x["paragraph_sha256"]) for x in a),f"{n}: paragraph anchors missing or invalid")
        check(";".join(f'{x["paragraph_index"]}:{x["paragraph_sha256"]}' for x in a)==ix["paragraph_sha256_anchors"],f"{n}: private source anchor mapping inconsistent")
        if n in CLOSE:
            close+=1
            check(len(r["mechanism_claims"])>=1,f"{n}: promised close reading has no mechanism claims")
            for q in r["mechanism_claims"]:
                check(q["verification_state"]=="PROVISIONAL" and q["counterexample_status"] in ("FOUND","SEARCHED_NONE"),f"{n}: unearned VERIFIED claim")
                check(set(q["support_anchor_ids"]) <= {x["anchor_id"] for x in a},f"{n}: unresolved claim source anchor")
                check(bool(q["failure_boundary"].strip()) and bool(q["alternative_rendering_loss"].strip()),f"{n}: no counterfactual or limit")
        total+=p;anchors+=len(a)
    check(total==2847,"Original full paragraph sum must equal R002 source: 2847")
    check(anchors==60,"R010 60 source anchors required")
    check(close==10,"10 close reading cases required, including first and last")
    for p in ["cangjie/reading/tiexue_041_080.md","cangjie/reading/R010/tiexue_continuity.md","cangjie/reading/R010/LOCAL_SOURCE_VERIFICATION.md"]:
        check((ROOT/p).is_file(),"Missing literature artifact "+p)
    state=json.loads((ROOT/"CURRENT_ROUND.json").read_text("utf-8"))
    token=state["current_round"];num=int(token[1:]) if token.startswith("R") and token[1:].isdigit() else -1
    check(10<=num<=89,"Historical R010 validator invoked outside V13 rounds")
    if num==10:
        check(state["full_text_read_chapters"]["tiexuecanming"]==40,"Cannot count uncertified R010")
        check(state["full_text_read_chapters"]["wanming"]==80,"R009 official count drift")
    elif num>=11:
        check(state["full_text_read_chapters"]["tiexuecanming"]>=80,"R010 certified 40-chapter count regressed")
        check(state["full_text_read_chapters"]["wanming"]>=80,"R009 count regressed")
    for e in errors:print("FAIL:",e)
    if errors:return 1
    print("PASS R010: 40 distinct original narrative chapters 041-080, 2847 source paragraphs, 60 private SHA256 paragraph locators, 10 PROVISIONAL close-read analyses, narrative consequences, correct R002 file hashes; no source prose or blind-test answers included")
    return 0
if __name__=="__main__":sys.exit(main())
