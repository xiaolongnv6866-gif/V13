#!/usr/bin/env python3
"""V13 R024 public metadata/source-structure verification; no copyrighted original in CI."""
import csv,json,re,sys
from pathlib import Path
root=Path(__file__).resolve().parents[1]
with (root/"sources/metadata/tiexuecanming_v13_spine.csv").open(encoding="utf-8",newline="") as f:
    master={int(z["narrative_ordinal"]):z for z in csv.DictReader(f) if z["narrative_ordinal"]}
with (root/"cangjie/reading/R024/tiexue_source_index.csv").open(encoding="utf-8",newline="") as f:
    source=list(csv.DictReader(f))
receipts=[json.loads(s) for s in (root/"cangjie/reading/R024/tiexue_receipts.jsonl").read_text(encoding="utf-8").splitlines() if s.strip()]
focus=set([321,324,328,329,331,333,336,337,340,341,343,344,345,346,347,350,352,355,357,360])
errors=[]
def check(v,m):
    if not v:errors.append(m)
check(len(source)==len(receipts)==40,"exactly 40 receipts/index")
check([z["narrative_ordinal"] for z in receipts]==list(range(321,361)),"missing/out-of-order ordinals")
check([int(z["narrative_ordinal"]) for z in source]==list(range(321,361)),"source order")
body=anchors=close=0;d=m=2166136261;seen=set()
for r,s in zip(receipts,source):
    n=r["narrative_ordinal"];z=master[n];p=int(z["nonempty_paragraphs"]);aa=r["anchors"];fm=n in focus
    check(r["book_slug"]=="tiexuecanming" and r["source_epub_sha256"]=="9100bbcdb9f52bcd5458cbda92e16b646489efbc00df5161ed568ebac83ffbaf",f"{n} book fingerprint")
    check(r["spine_index"]==int(z["spine_index"])==int(s["spine_index"])==n+16,f"{n} spine")
    check(r["epub_path"]==z["epub_path"]==s["epub_path"]==f"OEBPS/Text/chapter{n+7}.html",f"{n} member path")
    check(r["chapter_sha256"]==z["chapter_sha256"]==s["chapter_sha256"],f"{n} member sha")
    check(r["body_paragraph_count"]==r["observed_paragraph_count"]==int(s["nonempty_paragraphs"])==p,f"{n} paragraph total")
    check(r["mode"]==s["mode"]==("CLOSE_READ" if fm else "FULL_TEXT_READ"),f"{n} mode")
    check(r.get("fixture_only") is False and r.get("round_id")=="R024" and len(r.get("reader_session_id",""))>12,f"{n} receipt session")
    check(len(aa)==(3 if fm else 1) and all(1<=a["paragraph_index"]<=p and re.fullmatch(r"[0-9a-f]{64}",a["paragraph_sha256"]) for a in aa),f"{n} anchors")
    check(";".join(str(a["paragraph_index"])+":"+a["paragraph_sha256"] for a in aa)==s["paragraph_sha256_anchors"],f"{n} inconsistent anchors")
    ev=r["event_chain"];check(len(ev)==2 and all(len(x)>=20 for x in ev) and ev[0] not in seen,f"{n} distinct event chain")
    seen.add(ev[0]);check(bool(r["open_questions"]),f"{n} unresolved question")
    if fm:
        close+=1
        check(len(r["mechanism_claims"])>=1,f"{n} missing close analysis")
        for c in r["mechanism_claims"]:
            check(c["verification_state"]=="PROVISIONAL" and c["counterexample_status"]=="SEARCHED_NONE",f"{n} overclaim")
            check(len(c["alternative_rendering_loss"])>=35 and len(c["failure_boundary"])>=35,f"{n} weak interpretation")
    for a in aa:
        for ch in f'{n}/{a["paragraph_index"]}/{a["paragraph_sha256"]}\n':
            d=((d^ord(ch))*16777619)&0xffffffff
    for ch in f'{n}|{z["spine_index"]}|{z["epub_path"]}|{z["chapter_sha256"]}|{z["nonempty_paragraphs"]}\n':
        m=((m^ord(ch))*16777619)&0xffffffff
    body+=p;anchors+=len(aa)
check((body,anchors,close)==(2220,80,20),"40 chapters 2220 paragraphs 80 original locators 20 close required")
check(f"{d:08x}"=="12642d3d","private paragraph sequence FNV mismatch")
check(f"{m:08x}"=="8dd29619","frozen member sequence FNV mismatch")
for path in ("cangjie/reading/tiexue_321_360.md","cangjie/reading/R024/tiexue_continuity.md","cangjie/reading/R024/LOCAL_SOURCE_VERIFICATION.md","runs/R024.md"):
    check((root/path).is_file(),"missing "+path)
state=json.loads((root/"CURRENT_ROUND.json").read_text(encoding="utf-8"))
cur=int(state["current_round"][1:])
check(cur>=24,"R024 not authorized")
if cur==24:check(state["full_text_read_chapters"]=={"wanming":360,"tiexuecanming":320},"premature increment before official PASS")
else:check(state["full_text_read_chapters"]["tiexuecanming"]>=360 and state["full_text_read_chapters"]["wanming"]>=360,"regressed counts")
for e in errors:print("FAIL:",e)
if errors:sys.exit(1)
print("PASS R024 PUBLIC SOURCE_STRUCTURE_ONLY: TiexueCanming ordinals321-360 40 receipts,2220 paragraphs,20 close,80 SHA anchors FNV12642d3d; member FNV8dd29619")
