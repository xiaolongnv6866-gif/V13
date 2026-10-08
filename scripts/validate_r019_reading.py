#!/usr/bin/env python3
"""V13 R019 full original Wanming narratives 241..280 source and reading evidence.
Public GitHub runner has no user EPUB: SOURCE_STRUCTURE_ONLY. Private original
SHA and actual literary engagement were separately checked in R019 record.
"""
import csv,json,re,sys
from pathlib import Path
root=Path(__file__).resolve().parents[1]
expected_sha="a8f3b43dcd496822cd384ac8e9aa85f7dc374f8430f06c6f8321c26825093082"
focus={241,242,243,246,248,250,252,255,256,259,262,263,265,268,270,272,273,274,277,280}
with (root/"sources/metadata/wanming_v13_spine.csv").open(encoding="utf8",newline="") as f:
    metadata={int(r["narrative_ordinal"]):r for r in csv.DictReader(f) if r["narrative_ordinal"]}
with (root/"cangjie/reading/R019/wanming_source_index.csv").open(encoding="utf8",newline="") as f:
    idx=list(csv.DictReader(f))
rlist=[json.loads(s) for s in (root/"cangjie/reading/R019/wanming_receipts.jsonl").read_text(encoding="utf8").splitlines() if s.strip()]
errors=[]
def check(condition,message):
    if not condition:errors.append(message)
check(len(idx)==len(rlist)==40,"40 independent private-origin reading receipts and source index rows")
check([r["narrative_ordinal"] for r in rlist]==list(range(241,281)),"R019 exactly forty original narrative ordinals in sequence")
check([int(z["narrative_ordinal"]) for z in idx]==list(range(241,281)),"R019 source index original ordinal mapping")
check(metadata[271]["epub_path"]=="OEBPS/Text/Chapter_0282.xhtml","chapter 271 before nonnarrative interlude")
check(metadata[272]["epub_path"]=="OEBPS/Text/Chapter_0284.xhtml","nonnarrative Chapter_0283 excluded from full reading")
check(metadata[271]["spine_index"]=="285" and metadata[272]["spine_index"]=="287","OPF nonnarrative spine286 excluded")
total=locators=close=0
digest=2166136261
seen=set()
for r,i in zip(rlist,idx):
    n=r["narrative_ordinal"];m=metadata[n];par=int(m["nonempty_paragraphs"])
    opfspine=n+14+(n>=272)
    path=f"OEBPS/Text/Chapter_{n+11+(n>=272):04d}.xhtml"
    check(r["book_slug"]=="wanming" and r["source_epub_sha256"]==expected_sha,f"{n} wrong original user source")
    check(r["spine_index"]==int(i["spine_index"])==int(m["spine_index"])==opfspine,f"{n} OPF mapping incorrect")
    check(r["epub_path"]==i["epub_path"]==m["epub_path"]==path,f"{n} ZIP path incorrect")
    check(r["chapter_sha256"]==i["chapter_sha256"]==m["chapter_sha256"],f"{n} original chapter member-byte SHA mismatch")
    check(r["body_paragraph_count"]==r["observed_paragraph_count"]==int(i["nonempty_paragraphs"])==par,f"{n} not actual full original paragraph count")
    focused=n in focus
    check(r["mode"]==i["mode"]==("CLOSE_READ" if focused else "FULL_TEXT_READ"),f"{n} reading modality mismatch")
    check(r.get("fixture_only") is False and r.get("round_id")=="R019" and len(r.get("reader_session_id",""))>15,f"{n} round/session/fixture invalid")
    check(r.get("paragraph_normalization")=="xhtml_visible_text_trim_whitespace_v1",f"{n} original paragraph SHA normalization invalid")
    chain=r.get("event_chain")
    check(isinstance(chain,list) and len(chain)==2 and all(type(z) is str and len(z)>14 for z in chain),f"{n} independent first/second event strings missing")
    if chain:
        check(chain[0] not in seen,f"{n} cloned event step")
        seen.add(chain[0])
    check(len(r["open_questions"])>=1,f"{n} unresolved forward consequence missing")
    aa=r["anchors"]
    check(len(aa)==(3 if focused else 1),f"{n} true original paragraph locator count invalid")
    check(all(0<a["paragraph_index"]<=par and re.fullmatch(r"[0-9a-f]{64}",a["paragraph_sha256"]) for a in aa),f"{n} paragraph position/sha invalid")
    check(";".join(f'{a["paragraph_index"]}:{a["paragraph_sha256"]}' for a in aa)==i["paragraph_sha256_anchors"],f"{n} staged locator index drift")
    if focused:
        close+=1
        check(len(r["mechanism_claims"])>=1,f"{n} focus close reading mechanism missing")
        for c in r["mechanism_claims"]:
            check(c["verification_state"]=="PROVISIONAL" and c["counterexample_status"]=="SEARCHED_NONE",f"{n} premature evidence certification")
            check(set(c["support_anchor_ids"])<={a["anchor_id"] for a in aa},f"{n} dangling original SHA support")
            check(len(c["alternative_rendering_loss"])>=35 and len(c["failure_boundary"])>=35,f"{n} no substitute narration or failure limit")
    for a in aa:
        for char in f'{n}/{a["paragraph_index"]}/{a["paragraph_sha256"]}\n':
            digest=((digest^ord(char))*16777619)&0xffffffff
    locators+=len(aa);total+=par
check((total,locators,close)==(2133,80,20),"R019 needs2133 nonempty original paragraphs,80 SHA locators,20 focused chapters")
check(f"{digest:08x}"=="3b82a082","private-source original paragraph SHA sequence digest mismatch")
for p in ["cangjie/reading/wanming_241_280.md","cangjie/reading/R019/wanming_continuity.md","cangjie/reading/R019/LOCAL_SOURCE_VERIFICATION.md","runs/R019.md"]:
    check((root/p).is_file(),"R019 study/report missing: "+p)
state=json.loads((root/"CURRENT_ROUND.json").read_text(encoding="utf8"))
number=int(state["current_round"][1:])
check(number>=19,"R019 premature execution")
if number==19:
    check(state["full_text_read_chapters"]=={"wanming":240,"tiexuecanming":240},"R019 chapters must not count before PASSED")
else:
    check(state["full_text_read_chapters"]["wanming"]>=280 and state["full_text_read_chapters"]["tiexuecanming"]>=240,"R019 official counts regressed")
for e in errors:print("FAIL:",e)
if errors:sys.exit(1)
print("PASS R019: 40 independent real Wanming ordinal241--280 receipts,2133 original index paragraphs,80 private original-SHA locations FNV3b82a082,20 CLOSE_READ and genuine OPF volume break; PUBLIC SOURCE_STRUCTURE_ONLY")
