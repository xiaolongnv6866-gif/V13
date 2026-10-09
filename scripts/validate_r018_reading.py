#!/usr/bin/env python3
"""V13 R018 original chapter source and literary receipt audit.
GitHub CI: SOURCE_STRUCTURE_ONLY; user copyrighted EPUB not available publicly.
"""
import csv
import json
import re
import sys
from pathlib import Path

root=Path(__file__).resolve().parents[1]
source_sha="9100bbcdb9f52bcd5458cbda92e16b646489efbc00df5161ed568ebac83ffbaf"
focus={201,202,205,206,207,210,214,218,220,223,226,227,228,230,231,232,234,237,239,240}
with (root/"sources/metadata/tiexuecanming_v13_spine.csv").open(encoding="utf-8",newline="") as f:
    master={int(r["narrative_ordinal"]):r for r in csv.DictReader(f) if r["narrative_ordinal"]}
with (root/"cangjie/reading/R018/tiexue_source_index.csv").open(encoding="utf-8",newline="") as f:
    index=list(csv.DictReader(f))
receipts=[json.loads(s) for s in (root/"cangjie/reading/R018/tiexue_receipts.jsonl").read_text(encoding="utf-8").splitlines() if s.strip()]
errors=[]
def check(ok,message):
    if not ok: errors.append(message)
check(len(index)==len(receipts)==40,"R018 must have exactly40 independent full-original receipts")
check([r["narrative_ordinal"] for r in receipts]==list(range(201,241)),"Original narrative ordinal order and uniqueness")
check([int(r["narrative_ordinal"]) for r in index]==list(range(201,241)),"Frozen source metadata ordinal uniqueness")
total=locators=close=0
digest=2166136261
seen=set()
for row,ix in zip(receipts,index):
    n=row["narrative_ordinal"]
    m=master[n]
    para=int(m["nonempty_paragraphs"])
    check(row["book_slug"]=="tiexuecanming" and row["source_epub_sha256"]==source_sha,f"{n}: source book sha")
    check(row["spine_index"]==int(m["spine_index"])==int(ix["spine_index"])==n+16,f"{n}: OPF spine drift")
    check(row["epub_path"]==m["epub_path"]==ix["epub_path"]==f"OEBPS/Text/chapter{n+7}.html",f"{n}: original XHTML path drift")
    check(row["chapter_sha256"]==m["chapter_sha256"]==ix["chapter_sha256"],f"{n}: original chapter SHA drift")
    check(row["observed_paragraph_count"]==row["body_paragraph_count"]==para==int(ix["nonempty_paragraphs"]),f"{n}: original full body paragraph count")
    fm=n in focus
    check(row["mode"]==ix["mode"]==("CLOSE_READ" if fm else "FULL_TEXT_READ"),f"{n}: focus mode")
    check(row.get("fixture_only") is False and row.get("round_id")=="R018",f"{n}: this round authentic and nonfixture")
    check(row.get("paragraph_normalization")=="xhtml_visible_text_trim_whitespace_v1" and len(row.get("reader_session_id",""))>=18,f"{n}: normalization/session")
    events=row["event_chain"]
    check(type(events) is list and len(events)==2 and all(type(e) is str and len(e)>=24 for e in events),f"{n}: substantive two event strings")
    if events:
        check(events[0] not in seen,f"{n}: duplicated main event")
        seen.add(events[0])
    check(len(row["open_questions"])>=1,f"{n}: no forward uncertainty")
    aa=row["anchors"]
    check(len(aa)==(3 if fm else 1),f"{n}: source anchor cardinality")
    check(all(0<a["paragraph_index"]<=para and re.fullmatch(r"[a-f0-9]{64}",a["paragraph_sha256"]) for a in aa),f"{n}: SHA format/position")
    check(";".join(f'{a["paragraph_index"]}:{a["paragraph_sha256"]}' for a in aa)==ix["paragraph_sha256_anchors"],f"{n}: source index and receipt inconsistency")
    if fm:
        close+=1
        check(len(row["mechanism_claims"])>=1,f"{n}: no original focused mechanism analysis")
        for c in row["mechanism_claims"]:
            check(c["verification_state"]=="PROVISIONAL" and c["counterexample_status"] in ("FOUND","SEARCHED_NONE"),f"{n}: premature verified claim")
            check(set(c["support_anchor_ids"])<={a["anchor_id"] for a in aa},f"{n}: missing supporting original SHA")
            check(len(c["alternative_rendering_loss"])>=40 and len(c["failure_boundary"])>=40,f"{n}: missing counterfactual or boundary")
    for a in aa:
        for char in f'{n}/{a["paragraph_index"]}/{a["paragraph_sha256"]}\n':
            digest=((digest^ord(char))*16777619)&0xffffffff
    total+=para
    locators+=len(aa)
check((total,close,locators)==(2650,20,80),"Need2650 paragraphs,20 focused and80 source locators")
check(f"{digest:08x}"=="095e5bfb","Private original paragraph locator digest mismatch")
for path in ["cangjie/reading/tiexue_201_240.md","cangjie/reading/R018/tiexue_continuity.md","cangjie/reading/R018/LOCAL_SOURCE_VERIFICATION.md","runs/R018.md"]:
    check((root/path).is_file(),"Missing required authored report "+path)
state=json.loads((root/"CURRENT_ROUND.json").read_text(encoding="utf-8"))
current=int(state["current_round"][1:])
check(current>=18,"R018 must not be run before official cursor")
if current==18:
    check(state["full_text_read_chapters"]=={"wanming":240,"tiexuecanming":200},"R018 must not be counted before PASS")
else:
    check(state["full_text_read_chapters"]["wanming"]>=240 and state["full_text_read_chapters"]["tiexuecanming"]>=240,"R018 fully read counts regressed")
for e in errors: print("FAIL:",e)
if errors: sys.exit(1)
print("PASS R018: 40 original Tiexue ordinals201--240,2650 source paragraphs,80 original private-derived SHA locators FNV095e5bfb,20 CLOSE_READ candidate studies; PUBLIC SOURCE_STRUCTURE_ONLY")
