#!/usr/bin/env python3
"""R020 original Tiexuecanming 241-280 reading receipts, text-index audit.
PUBLIC SOURCE_STRUCTURE_ONLY: GitHub runner cannot read private copyrighted EPUB.
"""
import csv,json,re,sys
from pathlib import Path
root=Path(__file__).resolve().parents[1]
focus={241,242,243,246,248,250,251,253,254,255,256,258,261,262,263,266,267,268,272,280}
source_sha="9100bbcdb9f52bcd5458cbda92e16b646489efbc00df5161ed568ebac83ffbaf"
with (root/"sources/metadata/tiexuecanming_v13_spine.csv").open(encoding="utf8",newline="") as f:
    master={int(x["narrative_ordinal"]):x for x in csv.DictReader(f) if x["narrative_ordinal"]}
with (root/"cangjie/reading/R020/tiexue_source_index.csv").open(encoding="utf8",newline="") as f:
    ix=list(csv.DictReader(f))
rec=[json.loads(x) for x in (root/"cangjie/reading/R020/tiexue_receipts.jsonl").read_text(encoding="utf8").splitlines() if x.strip()]
errors=[]
def ck(test,message):
    if not test:errors.append(message)
ck(len(rec)==len(ix)==40,"R020 needs 40 unique original chapter receipts")
ck([r["narrative_ordinal"] for r in rec]==list(range(241,281)),"R020 chapter ordinal241..280 exact")
ck([int(i["narrative_ordinal"]) for i in ix]==list(range(241,281)),"R020 source index sequence exact")
total=locators=close=0
h=2166136261;sh=2166136261;seen=set()
for r,i in zip(rec,ix):
    n=r["narrative_ordinal"];m=master[n]
    paras=int(m["nonempty_paragraphs"])
    ck(r["book_slug"]=="tiexuecanming" and r["source_epub_sha256"]==source_sha,f"{n} original complete EPUB source")
    ck(r["spine_index"]==int(m["spine_index"])==int(i["spine_index"])==n+16,f"{n} OPF spine")
    ck(r["epub_path"]==m["epub_path"]==i["epub_path"]==f"OEBPS/Text/chapter{n+7}.html",f"{n} member original path")
    ck(r["chapter_sha256"]==i["chapter_sha256"]==m["chapter_sha256"],f"{n} original member SHA256")
    ck(r["body_paragraph_count"]==r["observed_paragraph_count"]==int(i["nonempty_paragraphs"])==paras,f"{n} original full body count")
    focused=n in focus
    ck(r["mode"]==i["mode"]==("CLOSE_READ" if focused else "FULL_TEXT_READ"),f"{n} mode")
    ck(r.get("fixture_only") is False and r.get("round_id")=="R020" and len(r.get("reader_session_id",""))>15,f"{n} original real reading metadata")
    ck(r.get("paragraph_normalization")=="xhtml_visible_text_trim_whitespace_v1",f"{n} frozen normalization")
    ev=r["event_chain"]
    ck(isinstance(ev,list) and len(ev)==2 and all(type(a) is str and len(a)>=14 for a in ev),f"{n} substantive event and independent agency")
    if ev:
        ck(ev[0] not in seen,f"{n} duplicated first event")
        seen.add(ev[0])
    ck(len(r.get("open_questions",[]))>0,f"{n} missing unresolved future consequence")
    anchors=r["anchors"]
    ck(len(anchors)==(3 if focused else 1),f"{n} original private paragraph anchors")
    ck(all(0<a["paragraph_index"]<=paras and re.fullmatch("[0-9a-f]{64}",a["paragraph_sha256"]) for a in anchors),f"{n} anchor position or SHA")
    ck(";".join(f'{a["paragraph_index"]}:{a["paragraph_sha256"]}' for a in anchors)==i["paragraph_sha256_anchors"],f"{n} staged private-source receipt/index disagree")
    if focused:
        close+=1
        ck(len(r["mechanism_claims"])>=1,f"{n} missing literary CLOSE_READ")
        for c in r["mechanism_claims"]:
            ck(c["verification_state"]=="PROVISIONAL" and c["counterexample_status"]=="SEARCHED_NONE",f"{n} invalid certainty")
            ck(set(c["support_anchor_ids"])<={a["anchor_id"] for a in anchors},f"{n} dangling literary support")
            ck(len(c["alternative_rendering_loss"])>=35 and len(c["failure_boundary"])>=35,f"{n} missing concrete counterfactual or failed-boundary")
    for a in anchors:
        for char in f'{n}/{a["paragraph_index"]}/{a["paragraph_sha256"]}\n':
            h=((h^ord(char))*16777619)&0xffffffff
    for char in f'{n}|{m["spine_index"]}|{m["epub_path"]}|{m["chapter_sha256"]}|{m["nonempty_paragraphs"]}\n':
        sh=((sh^ord(char))*16777619)&0xffffffff
    total+=paras;locators+=len(anchors)
ck((total,close,locators)==(2512,20,80),"R020 requires 2512 indexed paragraphs, 20 close, 80 real-source SHA locators")
ck(f'{h:08x}'=="93f49811","R020 private original paragraph digest mismatch")
ck(f'{sh:08x}'=="4371963e","R020 private original chapter/member composite digest mismatch")
for path in ("cangjie/reading/tiexue_241_280.md","cangjie/reading/R020/tiexue_continuity.md","cangjie/reading/R020/LOCAL_SOURCE_VERIFICATION.md","runs/R020.md"):
    ck((root/path).is_file(),"required R020 literary file missing "+path)
state=json.loads((root/"CURRENT_ROUND.json").read_text(encoding="utf8"))
number=int(state["current_round"][1:])
ck(number>=20,"R020 premature validation")
if number==20:
    ck(state["full_text_read_chapters"]=={"wanming":280,"tiexuecanming":240},"R020 must not be counted before PASS")
else:
    ck(state["full_text_read_chapters"]["wanming"]>=280 and state["full_text_read_chapters"]["tiexuecanming"]>=280,"R020 post-PASS count regressed")
for error in errors:print("FAIL:",error)
if errors:sys.exit(1)
print("PASS R020: original chapters 241-280, 2512 paragraphs, 20 CLOSE_READ, 80 private-derived SHA, original member index FNV4371963e, paragraphs FNV93f49811; public SOURCE_STRUCTURE_ONLY")
