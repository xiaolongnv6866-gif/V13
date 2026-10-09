#!/usr/bin/env python3
"""R015 public source-structure, chapter-locator and literary-receipt integrity.
SOURCE_STRUCTURE_ONLY: never claims this GitHub runner has copyrighted EPUB bytes.
"""
import csv,json,re,sys
from pathlib import Path
root=Path(__file__).resolve().parents[1]
focus={161,164,169,173,176,179,180,182,185,187,189,190,191,194,196,197,199,200}
fullsha="a8f3b43dcd496822cd384ac8e9aa85f7dc374f8430f06c6f8321c26825093082"
with (root/"sources/metadata/wanming_v13_spine.csv").open(encoding="utf8",newline="") as f:
    master={int(x["narrative_ordinal"]):x for x in csv.DictReader(f) if x["narrative_ordinal"]}
with (root/"cangjie/reading/R015/wanming_source_index.csv").open(encoding="utf8",newline="") as f: idx=list(csv.DictReader(f))
rs=[json.loads(x) for x in (root/"cangjie/reading/R015/wanming_receipts.jsonl").read_text("utf8").splitlines() if x.strip()]
fail=[]
def ck(q,m):
    if not q:fail.append(m)
ck(len(rs)==len(idx)==40,"Expected 40 R015 originals/records")
ck([r["narrative_ordinal"] for r in rs]==list(range(161,201)),"Non-contiguous narrative ordinals")
ck([int(i["narrative_ordinal"]) for i in idx]==list(range(161,201)),"Index ordinal mismatch")
total=locators=close=0;seen=set();digest=2166136261
for r,i in zip(rs,idx):
    n=r["narrative_ordinal"];m=master[n];p=int(m["nonempty_paragraphs"])
    ck(r["book_slug"]=="wanming" and r["source_epub_sha256"]==fullsha,str(n)+" wrong source")
    ck(r["spine_index"]==int(m["spine_index"])==int(i["spine_index"]),str(n)+" wrong OPF")
    ck(r["epub_path"]==m["epub_path"]==i["epub_path"],str(n)+" wrong ZIP member")
    ck(r["chapter_sha256"]==m["chapter_sha256"]==i["chapter_sha256"],str(n)+" bad chapter hash")
    ck(r["body_paragraph_count"]==r["observed_paragraph_count"]==p==int(i["nonempty_paragraphs"]),str(n)+" count drift")
    ck(r["mode"]==i["mode"]==("CLOSE_READ" if n in focus else "FULL_TEXT_READ"),str(n)+" wrong mode")
    ck(r.get("fixture_only") is False and r.get("round_id")=="R015" and len(r.get("reader_session_id",""))>=10,str(n)+" fake/absent session")
    ck(r.get("paragraph_normalization")=="xhtml_visible_text_trim_whitespace_v1",str(n)+" normalization")
    ck(len(r["event_chain"])>=2 and all(len(s)>=25 for s in r["event_chain"]),str(n)+" events absent")
    ck(r["event_chain"][0] not in seen,str(n)+" cloned event")
    seen.add(r["event_chain"][0])
    ck(len(r["open_questions"])>=1,str(n)+" open questions absent")
    a=r["anchors"];isclose=n in focus
    ck(len(a)==(3 if isclose else 1),str(n)+" required anchor count")
    ck(all(0<x["paragraph_index"]<=p and re.fullmatch(r"[0-9a-f]{64}",x["paragraph_sha256"]) for x in a),str(n)+" SHA syntax/range")
    ck(";".join(f'{x["paragraph_index"]}:{x["paragraph_sha256"]}' for x in a)==i["paragraph_sha256_anchors"],str(n)+" source index drift")
    if isclose:
        close+=1
        ck(len(r["mechanism_claims"])>=1,str(n)+" no focus study")
        for claim in r["mechanism_claims"]:
            ck(claim["verification_state"]=="PROVISIONAL",str(n)+" early certified claim")
            ck(claim["counterexample_status"] in ("FOUND","SEARCHED_NONE"),str(n)+" falsified counterexample")
            ck(set(claim["support_anchor_ids"])<={x["anchor_id"] for x in a},str(n)+" dangling anchor")
            ck(len(claim["alternative_rendering_loss"])>=25 and len(claim["failure_boundary"])>=25,str(n)+" counterfactual/boundary absent")
    for x in sorted(a,key=lambda y:y["paragraph_index"]):
        for ch in f'{n}/{x["paragraph_index"]}/{x["paragraph_sha256"]}\n':
            digest=((digest^ord(ch))*16777619)&0xffffffff
    total+=p;locators+=len(a)
ck(total==2137 and locators==76 and close==18,"private original batch measurements must be 2137/76/18")
ck(f'{digest:08x}'=="cf341ba9","Original private SHA locator digest differs from staged public records")
for p in ["cangjie/reading/wanming_161_200.md","cangjie/reading/R015/wanming_continuity.md","cangjie/reading/R015/LOCAL_SOURCE_VERIFICATION.md","runs/R015.md"]:
    ck((root/p).is_file(),"Missing authored report "+p)
state=json.loads((root/"CURRENT_ROUND.json").read_text("utf8"))
active=int(state["current_round"][1:])
ck(active>=15,"R015 premature")
if active==15:ck(state["full_text_read_chapters"]=={"wanming":160,"tiexuecanming":160},"cannot count until R015 formal PASS")
else:ck(state["full_text_read_chapters"]["wanming"]>=200 and state["full_text_read_chapters"]["tiexuecanming"]>=160,"R015 reading count regression")
for s in fail:print("FAIL:",s)
if fail:sys.exit(1)
print("PASS R015: 40 unique Wanming original chapter records 161--200, 2137 original-index paragraphs, 76 private SHA locators digest cf341ba9, 18 provisional CLOSE_READ, public SOURCE_STRUCTURE_ONLY")
