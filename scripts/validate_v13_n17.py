#!/usr/bin/env python3
"""N17: 91 V1 candidate provenance/decision ledger. STRUCTURE ONLY, not literary or independent V3 testing."""
from __future__ import annotations
import csv, json, re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "books/wanming/candidates"
GROUPS = [
    ("frameworks", "FRAMEWORK_EVIDENCE",17),
    ("principles", "PRINCIPLE_EVIDENCE",23),
    ("cases", "CASE_EVIDENCE",14),
    ("counter-examples", "COUNTEREXAMPLE_EVIDENCE",19),
    ("glossary", "GLOSSARY_EVIDENCE",18),
]
def rows(p):
    with (ROOT / p).open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))
decisions = rows("v13_3/n17/N17_WM_V1_91.tsv")
assert len(decisions) == 91
ids = [x["candidate_id"] for x in decisions]
assert len(set(ids)) == 91
got = Counter(x["V1_source_decision"] for x in decisions)
assert got == {
    "V1_SOURCE_SUPPORTED_SCOPED_V2_PENDING": 32,
    "V1_NEEDS_REVIEW_NO_V2": 6,
    "V1_REFERENCE_NOT_EXECUTABLE_METHOD": 53,
}, got
canon = {}; all_loci = set(); total_evidence_rows = 0
for name, table, size in GROUPS:
    md = (SOURCE / (name + ".md")).read_text(encoding="utf-8")
    blocks = md.split("\n- id: ")[1:]
    assert len(blocks) == size, (name, len(blocks),size)
    ev = rows("books/wanming/candidates/" + table + ".tsv")
    total_evidence_rows += len(ev)
    loci = {e["source_locus"]: e for e in ev}
    for block in blocks:
        mid = re.match(r"(\w+)",block).group(1)
        assert mid not in canon
        m = re.search(r"\n  source_loci:\s*\n((?:\s+-[^\n]+\n)+)", block)
        assert m, mid
        doc_loci = re.findall(r"n\d{3}/p\d+", m.group(1))
        assert doc_loci and all(a in loci for a in doc_loci),mid
        canon[mid]=(name,table,doc_loci,[loci[a]["paragraph_sha256"][:12] for a in doc_loci])
        all_loci.update(doc_loci)
assert len(canon)==91 and total_evidence_rows==237 and len(all_loci)==145
for item in decisions:
    cid = item["candidate_id"]
    assert cid in canon,cid
    name,table,loc,sha = canon[cid]
    assert item["all_original_loci"] == ";".join(loc),cid
    assert item["paragraph_sha12_all"] == ",".join(sha),cid
    assert item["first_original_locus"] == loc[0],cid
    assert item["source_candidate_file"] == f"books/wanming/candidates/{name}.md",cid
    assert item["source_evidence_file"] == f"books/wanming/candidates/{table}.tsv",cid
    assert item["short_source_quote"] and len(item["short_source_quote"])<=20,cid
    for k in ("V1_observed_original_scope","V1_counterexample_and_boundary","V1_source_decision","next_gate"):
        assert item[k].strip(),(cid,k)
    assert item["promotion_status"] == "NO_V2_OR_V3_OR_METHOD_PROMOTION_YET"
    d=item["V1_source_decision"]
    if name in ("cases","counter-examples","glossary"):
        assert d=="V1_REFERENCE_NOT_EXECUTABLE_METHOD",cid
    if d=="V1_SOURCE_SUPPORTED_SCOPED_V2_PENDING":
        assert name in ("frameworks","principles") and item["next_gate"]=="N19_V2_ACTUAL_NEW_INPUT",cid
    elif d=="V1_NEEDS_REVIEW_NO_V2":
        assert name in ("frameworks","principles") and item["next_gate"]=="N17_V1_SOURCE_OR_METHOD_REBUILD_REQUIRED",cid
    else:
        assert item["next_gate"]=="N28_REFERENCE_MAPPING_KEEP_SOURCE",cid
assert {x["candidate_id"] for x in decisions if x["V1_source_decision"]=="V1_NEEDS_REVIEW_NO_V2"}=={"f07","f09","p02","p06","p09","p10"}
s=json.loads((ROOT/"V13_CURRENT_V4.json").read_text(encoding="utf-8"))
assert s["completed_new_rounds"] in (16,17),s["completed_new_rounds"]
if s["completed_new_rounds"]==16:
    assert s["current_round"]=="N17"
else:
    assert s["current_round"]=="N18"
assert s["verified"]==0 and s["reference"]==108 and s["needs_review"]==79 and s["rejected"]==0
assert s["true_independent_V3_69_not_run"]==69 and s["original_stage0_20_independent_C_not_run"]==20
assert s["certified_skills"]==0 and s["v13_3_R042_quarantines_still_not_promoted"]==14
assert (ROOT/"v13_3/n17/N17_WM_V1_SOURCE_AUDIT.md").is_file()
print("PASS N17 structural 91/91: WM17+23+14+19+18; unique source 145, evidence rows 237; 32 limited, 6 needs, 53 reference; no verified promotions. NOT literary independent certification.")
