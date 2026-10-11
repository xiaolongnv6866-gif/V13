#!/usr/bin/env python3
"""N18 full TX96 V1-source structural contract; DOES NOT test private EPUB or V2/V3."""
from __future__ import annotations
import csv,json,re
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
GROUPS=[("frameworks","FRAMEWORK_EVIDENCE",17),("principles","PRINCIPLE_EVIDENCE",22),("cases","CASE_EVIDENCE",16),("counter-examples","COUNTEREXAMPLE_EVIDENCE",21),("glossary","GLOSSARY_EVIDENCE",20)]
SOURCE=ROOT/"books/tiexuecanming/candidates"
def rows(path):
    with (ROOT/path).open(encoding="utf-8",newline="") as f:return list(csv.DictReader(f,delimiter="\t"))
v1=rows("v13_3/n18/N18_TX_V1_96.tsv")
assert len(v1)==96 and len({a["candidate_id"] for a in v1})==96
counts=Counter(a["V1_decision"] for a in v1)
assert counts=={"V1_SOURCE_SUPPORTED_SCOPED_V2_PENDING":32,"V1_NEEDS_REVIEW_NO_V2":4,"V1_REFERENCE_NOT_EXECUTABLE_METHOD":60},counts
allids=set();loci=set();amount=0;taskmap={f"TX-{i:02d}":[] for i in range(1,11)}
for filename,tablename,n in GROUPS:
    raw=(SOURCE/(filename+".md")).read_text(encoding="utf-8")
    blocks=raw.split("\n- id: ")[1:]
    assert len(blocks)==n,(filename,len(blocks),n)
    e=rows(f"books/tiexuecanming/candidates/{tablename}.tsv")
    amount+=len(e)
    emap={x["source_locus"]:x for x in e}
    assert len(emap)==len(e),"duplicate evidence loc in type "+filename
    for block in blocks:
        cid=re.match(r"(\w+)",block).group(1)
        assert cid not in allids,cid
        allids.add(cid)
        match=re.search(r"\n  source_loci:\s*\n((?:\s+-[^\n]+\n)+)",block)
        assert match,cid
        matches=re.findall(r"n\d{3}/p\d+",match.group(1))
        assert matches and all(x in emap for x in matches),cid
        row=next((z for z in v1 if z["candidate_id"]==cid),None)
        assert row is not None,cid
        assert row["upstream_extractor"]==filename
        assert row["original_candidate_path"]==f"books/tiexuecanming/candidates/{filename}.md"
        assert row["original_evidence_path"]==f"books/tiexuecanming/candidates/{tablename}.tsv"
        assert row["all_source_loci"]==";".join(matches)
        assert row["all_paragraph_sha256"]==";".join(emap[x]["paragraph_sha256"] for x in matches)
        assert row["source_first_locus"]==matches[0]
        assert row["source_epub_path"]==emap[matches[0]]["epub_path"]
        assert row["chapter_sha256"]==emap[matches[0]]["chapter_sha256"]
        assert row["paragraph_sha256"]==emap[matches[0]]["paragraph_sha256"]
        assert 3<=len(row["short_source_quote"])<=12,cid
        assert row["source_scope_adjudication"] and row["competing_evidence_and_boundary"]
        assert row["promotion_permission"]=="NO_V2_V3_OR_METHOD_PROMOTION",cid
        decision=row["V1_decision"]
        if filename in ("cases","counter-examples","glossary"):
            assert decision=="V1_REFERENCE_NOT_EXECUTABLE_METHOD",cid
        if decision=="V1_SOURCE_SUPPORTED_SCOPED_V2_PENDING":
            assert filename in ("frameworks","principles") and row["next_gate"]=="N20_V2_ACTUAL_NEW_INPUT",cid
        elif decision=="V1_NEEDS_REVIEW_NO_V2":
            assert row["next_gate"]=="N28_NEEDS_REVIEW_NONACTIVE_UNTIL_REBUILT",cid
        else:assert row["next_gate"]=="N28_REFERENCE_MAPPING_KEEP_SOURCE",cid
        taskids=(row["related_Stage0_task_ids"] or "").split(";")
        for t in taskids:
            if t:
                assert t in taskmap,(cid,t)
                taskmap[t].append((cid,decision))
        if filename=="cases":
            assert row["original_example_kind"]=="fictional_narrative_case",cid
        loci.update(matches)
assert amount==264 and len(loci)==177 and allids=={x["candidate_id"] for x in v1}
assert {x["candidate_id"] for x in v1 if x["V1_decision"]=="V1_NEEDS_REVIEW_NO_V2"}=={"f03","f06","f14","p16"}
coverage=rows("v13_3/n18/N18_TX_STAGE0_10_V1_COVERAGE.tsv")
assert len(coverage)==10 and {x["task_id"] for x in coverage}==set(taskmap)
for item in coverage:
    data=taskmap[item["task_id"]]
    assert item["candidate_ids"]==";".join(x[0] for x in data)
    assert int(item["V1_source_supported"])==sum(x[1]=="V1_SOURCE_SUPPORTED_SCOPED_V2_PENDING" for x in data)
    assert int(item["V1_needs_review"])==sum(x[1]=="V1_NEEDS_REVIEW_NO_V2" for x in data)
    assert int(item["V1_reference"])==sum(x[1]=="V1_REFERENCE_NOT_EXECUTABLE_METHOD" for x in data)
    assert item["current_original_Stage0_C_execution"]=="NOT_RUN"
state=json.loads((ROOT/"V13_CURRENT_V4.json").read_text(encoding="utf-8"))
assert state["completed_new_rounds"]>=17
if state["completed_new_rounds"]==17:assert state["current_round"]=="N18"
else: assert rows("V13_LEDGER_V4.tsv")[17]["status"]=="PASSED"
if state["completed_new_rounds"]<28:
    assert (state["verified"],state["reference"],state["needs_review"],state["rejected"])==(0,108,79,0)
    assert state["v13_3_R042_quarantines_still_not_promoted"]==14
if state["completed_new_rounds"]<37:assert state["certified_skills"]==0
assert (ROOT/"v13_3/n18/N18_TX_V1_SOURCE_AUDIT.md").is_file()
print("PASS N18 public structural contract: TX96 / 264 evidence rows / 177 loci / 10 tasks; V1 32 scoped,4 needs,60 reference; NOT a private EPUB or independent literary validation.")
