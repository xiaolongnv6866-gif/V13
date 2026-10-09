#!/usr/bin/env python3
"""R021 original Wanming 281..320 study/source audit (public SOURCE_STRUCTURE_ONLY).
Private user-supplied copyrighted EPUB is NOT accessible to GitHub Actions.
"""
import csv,json,re,sys
from pathlib import Path
root=Path(__file__).resolve().parents[1]
expected_sha="a8f3b43dcd496822cd384ac8e9aa85f7dc374f8430f06c6f8321c26825093082"
focus={281,282,283,285,288,291,293,295,297,299,301,303,305,307,309,311,313,316,318,320}
with (root/"sources/metadata/wanming_v13_spine.csv").open(encoding="utf-8",newline="") as f:
    master={int(v["narrative_ordinal"]):v for v in csv.DictReader(f) if v["narrative_ordinal"]}
with (root/"cangjie/reading/R021/wanming_source_index.csv").open(encoding="utf-8",newline="") as f:
    source=list(csv.DictReader(f))
receipts=[json.loads(l) for l in (root/"cangjie/reading/R021/wanming_receipts.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
errors=[]
def ck(ok,description):
    if not ok:errors.append(description)
ck(len(receipts)==len(source)==40,"R021 requires 40 distinct chapter receipts/index entries")
ck([v["narrative_ordinal"] for v in receipts]==list(range(281,321)),"original effective narrative ordinals 281..320 required")
ck([int(v["narrative_ordinal"]) for v in source]==list(range(281,321)),"index order must match 281..320")
body=anchors=close=0;digest=2166136261;member_digest=2166136261;seen=set()
for r,i in zip(receipts,source):
    n=r["narrative_ordinal"];m=master[n];p=int(m["nonempty_paragraphs"])
    ck(r["book_slug"]=="wanming" and r["source_epub_sha256"]==expected_sha,f"{n} original EPub fingerprint")
    ck(r["spine_index"]==int(m["spine_index"])==int(i["spine_index"])==n+15,f"{n} original OPF spine")
    ck(r["epub_path"]==m["epub_path"]==i["epub_path"]==f"OEBPS/Text/Chapter_{n+12:04d}.xhtml",f"{n} original member path")
    ck(r["chapter_sha256"]==i["chapter_sha256"]==m["chapter_sha256"],f"{n} frozen member SHA")
    ck(r["body_paragraph_count"]==r["observed_paragraph_count"]==int(i["nonempty_paragraphs"])==p,f"{n} original full paragraph count")
    fm=n in focus
    ck(r["mode"]==i["mode"]==("CLOSE_READ" if fm else "FULL_TEXT_READ"),f"{n} mode")
    ck(r.get("fixture_only") is False and r.get("round_id")=="R021" and len(r.get("reader_session_id",""))>12,f"{n} source/session metadata")
    ck(r.get("paragraph_normalization")=="xhtml_visible_text_trim_whitespace_v1",f"{n} frozen normalized text")
    ev=r["event_chain"]
    ck(isinstance(ev,list) and len(ev)==2 and all(type(x) is str and len(x)>=20 for x in ev),f"{n} authored event/agency text missing")
    if ev:
        ck(ev[0] not in seen,f"{n} cloned event summary")
        seen.add(ev[0])
    ck(bool(r["open_questions"]),f"{n} no unresolved question")
    aa=r["anchors"]
    ck(len(aa)==(3 if fm else 1),f"{n} original paragraph anchors count")
    ck(all(0<a["paragraph_index"]<=p and re.fullmatch(r"[0-9a-f]{64}",a["paragraph_sha256"]) for a in aa),f"{n} source paragraph SHA/position")
    ck(";".join(f'{a["paragraph_index"]}:{a["paragraph_sha256"]}' for a in aa)==i["paragraph_sha256_anchors"],f"{n} source/receipt anchors inconsistent")
    if fm:
        close+=1
        ck(len(r["mechanism_claims"])>=1,f"{n} CLOSE_READ lacks scene mechanism")
        for c in r["mechanism_claims"]:
            ck(c["verification_state"]=="PROVISIONAL" and c["counterexample_status"]=="SEARCHED_NONE",f"{n} unearned VERIFIED status")
            ck(set(c["support_anchor_ids"])<={a["anchor_id"] for a in aa},f"{n} ungrounded support")
            ck(len(c["alternative_rendering_loss"])>=35 and len(c["failure_boundary"])>=35,f"{n} lacks counterfactual or failure-boundary")
    for a in aa:
        for ch in f'{n}/{a["paragraph_index"]}/{a["paragraph_sha256"]}\n':
            digest=((digest^ord(ch))*16777619)&0xffffffff
    for ch in f'{n}|{m["spine_index"]}|{m["epub_path"]}|{m["chapter_sha256"]}|{m["nonempty_paragraphs"]}\n':
        member_digest=((member_digest^ord(ch))*16777619)&0xffffffff
    body+=p;anchors+=len(aa)
ck((body,close,anchors)==(2223,20,80),"R021 requires 2223 original paragraphs, 20 close, 80 real SHA locators")
ck(f'{digest:08x}'=="2fa4eb5f","80 original private SHA sequence FNV mismatch")
ck(f'{member_digest:08x}'=="b69dfa88","40 frozen original chapter member indexes FNV mismatch")
for path in ["cangjie/reading/wanming_281_320.md","cangjie/reading/R021/wanming_continuity.md","cangjie/reading/R021/LOCAL_SOURCE_VERIFICATION.md","runs/R021.md"]:
    ck((root/path).is_file(),"Missing R021 study/continuity/audit "+path)
state=json.loads((root/"CURRENT_ROUND.json").read_text(encoding="utf-8"))
n=int(state["current_round"][1:])
ck(n>=21,"R021 cannot prematurely start")
if n==21:
    ck(state["full_text_read_chapters"]=={"wanming":280,"tiexuecanming":280},"R021 must not increment counts before PASS")
else:
    ck(state["full_text_read_chapters"]["wanming"]>=320 and state["full_text_read_chapters"]["tiexuecanming"]>=280,"R021 certified count regressed")
for e in errors:print("FAIL:",e)
if errors:sys.exit(1)
print("PASS R021 PUBLIC SOURCE_STRUCTURE_ONLY: Wanming original ordinals281-320,40 authored receipts,2223 paragraphs,80 real-source SHA locators FNV2fa4eb5f,20 close studies and frozen member FNVb69dfa88")
