#!/usr/bin/env python3
"""V13 R007 static 40-receipt validator; does NOT claim direct access to private EPUB.

Book body and authentic anchored paragraph SHA must be separately checked using
private original with scripts/validate_r006_protocol.py --source-dir /mnt/data.
"""
import csv,json,hashlib,re,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SLUG="wanming"
SHA="a8f3b43dcd496822cd384ac8e9aa85f7dc374f8430f06c6f8321c26825093082"
PATH=ROOT/"cangjie/reading/R007/wanming_receipts.jsonl"
SOURCE=ROOT/"sources/metadata/wanming_v13_spine.csv"
INDEX=ROOT/"cangjie/reading/R007/wanming_source_index.csv"
MODE={"FULL_TEXT_READ","CLOSE_READ"}
CLOSE={1,20,34,35,39,40}
def check(cond,msg,errors):
    if not cond:errors.append(msg)
def main():
    errors=[]
    with SOURCE.open(encoding="utf-8",newline="") as f:metadata={int(r["narrative_ordinal"]):r for r in csv.DictReader(f) if r["narrative_ordinal"]}
    with INDEX.open(encoding="utf-8",newline="") as f:index=list(csv.DictReader(f))
    receipts=[json.loads(x) for x in PATH.read_text("utf-8").splitlines() if x.strip()]
    check(len(receipts)==40 and len(index)==40,"R007 must contain exactly 40 per-chapter receipts and index rows",errors)
    check([r["narrative_ordinal"] for r in receipts]==list(range(1,41)),"R007 receipt order must be 001..040",errors)
    check([int(r["narrative_ordinal"]) for r in index]==list(range(1,41)),"R007 index order must be 001..040",errors)
    sha_pat=re.compile(r"^[0-9a-f]{64}$")
    count=0;anchors=0;close_count=0;events=set()
    for r,idx in zip(receipts,index):
        n=r["narrative_ordinal"];m=metadata.get(n)
        if not m:errors.append(f"ordinal {n}: missing R002 source");continue
        check(r["book_slug"]==SLUG and r["source_epub_sha256"]==SHA,f"{n}: incorrect book source",errors)
        check(r["spine_index"]==int(m["spine_index"]) and r["spine_index"]==int(idx["spine_index"]),f"{n}: spine index mismatch",errors)
        check(r["epub_path"]==m["epub_path"]==idx["epub_path"],f"{n}: EPUB member path mismatch",errors)
        check(r["chapter_sha256"]==m["chapter_sha256"]==idx["chapter_sha256"],f"{n}: XHTML member SHA mismatch",errors)
        check(r["body_paragraph_count"]==int(m["nonempty_paragraphs"]) and r["body_paragraph_count"]==r["observed_paragraph_count"]==int(idx["nonempty_paragraphs"]),f"{n}: incomplete paragraph record",errors)
        check(r["fixture_only"] is False and r["mode"] in MODE,f"{n}: synthetic/non-full receipt",errors)
        check(r["mode"]==("CLOSE_READ" if n in CLOSE else "FULL_TEXT_READ"),f"{n}: incorrect preselected close-read sampling",errors)
        check(len(r["anchors"])>=1 and all(0<a["paragraph_index"]<=r["body_paragraph_count"] and sha_pat.fullmatch(a["paragraph_sha256"]) for a in r["anchors"]),f"{n}: no sound anchored claim",errors)
        check(len(r["event_chain"])>=2 and all(isinstance(x,str) and len(x)>=12 for x in r["event_chain"]),f"{n}: insufficient per-chapter independently authored event/agency evidence",errors)
        check(len(r["open_questions"])>=1 and r["round_id"]=="R007" and r["reader_session_id"] and r["paragraph_normalization"]=="xhtml_visible_text_trim_whitespace_v1",f"{n}: provenance or open question absent",errors)
        check(not any(tag in " ".join(r["event_chain"]) for tag in ["V10","V11","V12"]),"Old project content leaked",errors)
        for a in r["anchors"]:
            check(f'{a["paragraph_index"]}:{a["paragraph_sha256"]}' in idx["paragraph_index_sha256_anchors"],f"{n}: anchor absent in index",errors)
        ev=r["event_chain"][0]
        check(ev not in events,f"{n}: duplicated synthetic story notes",errors);events.add(ev)
        if n in CLOSE:
            close_count+=1
            check(len(r["mechanism_claims"])>=1,f"{n}: close read missing mechanism claim",errors)
            for cl in r["mechanism_claims"]:
                check(cl["verification_state"]=="PROVISIONAL" and cl["counterexample_status"] in ("FOUND","SEARCHED_NONE"),f"{n}: unverified original book theory given VERIFIED status",errors)
        count+=r["body_paragraph_count"];anchors+=len(r["anchors"])
    check(count==2285,"Actual corpus XHTML paragraph count drifted from private R007 source scan",errors)
    check(anchors==73,"13 authenticated R007 corrective locators must add to frozen original 60",errors)
    claims=[r["mechanism_claims"][0] for r in receipts if r["mode"]=="CLOSE_READ"]
    check(len(set(c["failure_boundary"] for c in claims))==6,"R007 six close studies must not reuse generic failure boundaries",errors)
    check(len(set(c["alternative_rendering_loss"] for c in claims))==6,"R007 six close studies must compare genuinely different narrative alternatives",errors)
    check(len(set(c["counterexample_search_note"] for c in claims))==6,"R007 counterexample searches must remain scene-specific",errors)
    for rr in receipts:
        if rr["mode"]=="CLOSE_READ":
            cc=rr["mechanism_claims"][0]
            check(len(cc["support_anchor_ids"])>=3 and all(x in {aa["anchor_id"] for aa in rr["anchors"]} for x in cc["support_anchor_ids"]),f"{rr['narrative_ordinal']}: at least three real support positions required for corrected close audit",errors)
    check(close_count==6,"Expected six genuine chapter-level CLOSE_READ receipts",errors)
    for p in ["cangjie/reading/wanming_001_040.md","cangjie/reading/R007/wanming_continuity.md","cangjie/reading/R007/LOCAL_SOURCE_VERIFICATION.md"]:
        check((ROOT/p).is_file(),"Missing required narrative report "+p,errors)
    cursor=json.loads((ROOT/"CURRENT_ROUND.json").read_text("utf-8"))
    round_id=cursor["current_round"]
    check(round_id in ("R007","R008") or (round_id.startswith("R") and round_id[1:].isdigit() and 9<=int(round_id[1:])<=89),"R007 validator on unexpected round",errors)
    if round_id=="R007":check(cursor["full_text_read_chapters"]["wanming"]==0,"Cannot predeclare 40 chapters while R007 still active",errors)
    else:check(cursor["full_text_read_chapters"]["wanming"]>=40,"R007 historical reading count regressed",errors)
    for e in errors:print("FAIL:",e)
    if errors:return 1
    print(f"PASS R007: 40 distinct ordinal receipts in matching R002 source paths; 2285 anchored-body paragraphs, 73 private-paragraph SHA locators including 13 corrective anchors, 6 provisional close studies and 40 unique event notes; no automatic literary understanding or heldout score claimed")
    return 0
if __name__=="__main__":sys.exit(main())
