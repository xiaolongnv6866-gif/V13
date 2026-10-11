#!/usr/bin/env python3
"""N16 source and Stage1 extraction object structural integrity. Not literary/independent validation."""
from __future__ import annotations
import csv
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COUNTS = [17, 17, 18, 18, 20, 20, 20, 20, 20, 26, 20, 20, 20, 20, 20]
EXTRACTORS = [
    ("framework", "frameworks", "FRAMEWORK_EVIDENCE.tsv", "inputs", "outputs", "steps"),
    ("principle", "principles", "PRINCIPLE_EVIDENCE.tsv", "rule_scope", "provenance"),
    ("case", "cases", "CASE_EVIDENCE.tsv", "example_kind", "bound_to", "outcome"),
    ("counter-example", "counter-examples", "COUNTEREXAMPLE_EVIDENCE.tsv", "failure_mode", "mechanism", "bound_to"),
    ("glossary", "glossary", "GLOSSARY_EVIDENCE.tsv", "key_distinction", "why_it_matters"),
]

def tsv(path):
    with (ROOT / path).open(encoding="utf-8", newline="") as fd:
        return list(csv.DictReader(fd, delimiter="\t"))

def require(value, context):
    assert value is not None and str(value).strip(), context

def get(d, *names):
    return next((d[n] for n in names if n in d), "")

def unique(rows, key, count, desc):
    assert len(rows) == count, (desc, "count", len(rows), count)
    ids = [r[key] for r in rows]
    assert len(set(ids)) == count and all(ids), (desc, "duplicate/empty IDs")

cursor = json.loads((ROOT / "V13_CURRENT_V4.json").read_text(encoding="utf-8"))
ledger = tsv("V13_LEDGER_V4.tsv")
assert len(ledger) == 48
assert all(row["status"] == "PASSED" for row in ledger[:15])
assert 15 <= cursor["completed_new_rounds"] <= 48, cursor["completed_new_rounds"]
if cursor["completed_new_rounds"] == 15:
    assert cursor["current_round"] == "N16"
    assert cursor["current_round_status"] in {"NOT_STARTED", "IN_PROGRESS", "BLOCKED", "FAILED"}
    assert ledger[15]["status"] == cursor["current_round_status"]
else:
    assert ledger[15]["status"] == "PASSED"
    if cursor["completed_new_rounds"] < 48:
        assert cursor["current_round"] == f'N{cursor["completed_new_rounds"]+1:02d}'
        assert cursor["current_round_status"] in {"NOT_STARTED", "IN_PROGRESS", "BLOCKED", "FAILED"}
assert cursor["v13_3_stage0_B_disposed_this_plan"] == 296
assert cursor["v13_3_from_old_192_unreviewed_done"] == 192
assert cursor["v13_3_R042_quarantines_source_reviewed"] == 14
if cursor["completed_new_rounds"] < 28:
    assert cursor["v13_3_R042_quarantines_still_not_promoted"] == 14
    assert (cursor["verified"], cursor["reference"], cursor["needs_review"], cursor["rejected"]) == (0, 108, 79, 0)
if cursor["completed_new_rounds"] < 37:
    assert cursor["certified_skills"] == 0

res = tsv("V13_3_SOURCE_RESOLUTION_296.tsv")
issue = tsv("V13_3_ISSUES_426_TO_ROUNDS.tsv")
unique(res, "issue_id", 296, "source resolution")
unique(issue, "issue_id", 426, "issue routing")
sources = {r["issue_id"]: r for r in res}
issues = {r["issue_id"]: r for r in issue}
b = tsv("v13_3/n16/N16_LITERARY_B_296_MASTER.tsv")
unique(b, "issue_id", 296, "N16 B master")
assert set(sources) == {r["issue_id"] for r in b}
assert sum(r["disposition_class"] == "SCOPED_LITERARY_B_ONLY" for r in b) == 243
assert sum(r["disposition_class"] == "REJECT_OLD_STRONG_CLAIM" for r in b) == 53
assert Counter(r["book"] for r in b) == {"wanming": 150, "tiexuecanming": 146}
oldb = {}
for n, count in enumerate(COUNTS, start=1):
    oldname = f"v13_3/n{n:02d}/N{n:02d}_LITERARY_B_{count}.tsv"
    rows = tsv(oldname)
    unique(rows, "issue_id", count, oldname)
    for x in rows:
        assert x["issue_id"] not in oldb
        oldb[x["issue_id"]] = (x, n, oldname)
assert set(oldb) == set(sources)
for x in b:
    id_ = x["issue_id"]
    orig, n, oldname = oldb[id_]
    source = sources[id_]
    routed = issues[id_]
    assert routed["issue_type"] == "STAGE0_B_CLAIM"
    assert routed["new_primary_round"] == f"N{n:02d}"
    assert routed["original_source_round"] == source["original_source_round"] == x["original_round"]
    assert x["review_round"] == f"N{n:02d}" and x["review_table"] == oldname
    assert x["book"] == source["book"]
    assert x["original_receipt"] == source["corrected_receipt_source"]
    assert x["receipt_git_blob_sha"] == source["receipt_git_blob_sha"]
    assert x["resolution_locator"] == source["resolved_locator"]
    assert x["original_epub_member"] == get(orig, "original_epub_path", "epub_path")
    assert x["original_chapter_sha256"] == orig["chapter_sha256"]
    assert x["literary_B_disposition"] == get(
        orig, "literary_B_disposition", "B_disposition", "B_adjudication",
        "literary_B_decision", "B_decision")
    if x["disposition_class"] == "REJECT_OLD_STRONG_CLAIM":
        assert x["literary_B_disposition"].startswith("REJECT")
    else:
        assert x["literary_B_disposition"].startswith("SCOPED")
    for col in ("original_claim", "observable_action", "counterevidence_or_old_error",
                "alternative_narration_loss", "applicability_and_failure",
                "prior_method_status", "historical_resolution_scope", "remaining_quality_requirement"):
        require(x[col], (id_, col))
    assert x["promotion_permission"] == "NO_DIRECT_PROMOTION"
    assert "NO_V1" in x["prior_method_status"] or "B_SOURCE_REVIEW_ONLY" in x["prior_method_status"]
assert "STAGE0:R024:R024-337-C1" in {x["issue_id"] for x in b if x["disposition_class"].startswith("REJECT")}

quarantines = tsv("v13_3/n16/N16_R042_14_QUARANTINE_MASTER.tsv")
legacy = tsv("cangjie/reading/R042_OLD_CLAIM_QUARANTINE.tsv")
qroutes = tsv("gates/R078_OLD14_QUARANTINE_ROUTE.tsv")
unique(quarantines, "legacy_claim_id", 14, "N16 legacy14")
unique(legacy, "legacy_claim_id", 14, "original legacy14")
assert set(r["legacy_claim_id"] for r in quarantines) == {
    r["legacy_claim_id"] for r in legacy} == {r["legacy_claim_id"] for r in qroutes}
assert Counter(r["book"] for r in quarantines) == {"wanming": 7, "tiexuecanming": 7}
historical = {r["legacy_claim_id"]: r for r in legacy}
for r in quarantines:
    id_ = r["legacy_claim_id"]
    assert r["original_round"] == historical[id_]["round_id"]
    assert r["original_claim_risk"] == historical[id_]["source_boundary"]
    assert r["source_review_state"] == "SOURCE_REVIEWED_ONLY"
    assert r["quarantine_state"] == "OPEN_QUARANTINED"
    assert r["promotion_permission"] == "NO_DIRECT_PROMOTION"
    assert (r["V1"], r["V2"], r["true_independent_V3"], r["full_original_C"]) == (
        "NOT_REBUILT", "NOT_REBUILT", "NOT_INDEPENDENT", "NOT_RUN")
    for k in ("historical_source_locus", "re_reviewed_loci", "original_error_adjudication",
              "scoped_interpretation_only", "historical_next_evidence", "next_quality_gate"):
        require(r[k], (id_, k))

task = tsv("V13_3_STAGE0_20_TO_ROUNDS.tsv")
mapped = tsv("v13_3/n16/N16_STAGE0_20_TO_19_CONTRACT.tsv")
cross = tsv("gates/R078_STAGE0_ORIGINAL20_TO_R057_19_CROSSWALK.tsv")
topics = tsv("gates/R057_TASK_COVERAGE.tsv")
unique(task, "old_task_id", 20, "frozen Stage0")
unique(mapped, "old_task_id", 20, "N16 20/19 mapping")
unique(cross, "old_Stage0_id", 20, "old crosswalk")
unique(topics, "task_id", 19, "R057 19")
contracts = {x["old_task_id"]: x for x in task}
original_cross = {x["old_Stage0_id"]: x for x in cross}
freq = Counter(r["R057_topic_id"] for r in mapped)
assert len(freq) == 19 and freq["WM-05"] == 2
assert all(count == 1 for k, count in freq.items() if k != "WM-05")
assert {x["old_task_id"] for x in mapped} == set(contracts)
assert set(freq) == {x["task_id"] for x in topics}
for r in mapped:
    orig = contracts[r["old_task_id"]]
    c = original_cross[r["old_task_id"]]
    assert r["original_inputs"] == orig["old_inputs"]
    assert r["old_required_output"] == orig["required_output"]
    assert r["old_acceptance_and_failure"] == orig["acceptance_and_failure"]
    assert r["R057_topic_id"] == c["R057_task_id"] == orig["related_R057_topic"]
    assert r["original_exact_C_NOT_RUN"] == "NOT_RUN"
    assert r["preserved_original_independent_C_round"] == orig["original_full_C_round"]
    assert r["final_N28_audit"] == "N28"
assert {x["old_task_id"] for x in mapped if x["R057_topic_id"] == "WM-05"} == {"WM-T05", "WM-T06"}

for book, expected in [("wanming", 91), ("tiexuecanming", 96)]:
    overview = (ROOT / "books" / book / "BOOK_OVERVIEW.md").read_text(encoding="utf-8")
    assert len(overview) > 7000
    assert all(x in overview for x in ("## 1.", "## 2.", "## 3.", "## 4.", "N16", "BOOK_OVERVIEW"))
    assert "R042" in overview and "20" in overview and "19" in overview
    audit = tsv(f"v13_3/n16/N16_EXTRACTOR_{'WM' if book == 'wanming' else 'TX'}_5.tsv")
    unique(audit, "upstream_extractor", 5, book + " extractors")
    assert {r["upstream_extractor"] for r in audit} == {x[0] for x in EXTRACTORS}
    sum_candidates = 0
    for typ, fname, evidencefile, *fields in EXTRACTORS:
        record = next(x for x in audit if x["upstream_extractor"] == typ)
        p = f"books/{book}/candidates/"
        candidate_path = p + fname + ".md"
        evidence_path = p + evidencefile
        assert record["raw_candidate_md"] == candidate_path
        assert record["evidence_tsv"] == evidence_path
        data = (ROOT / candidate_path).read_text(encoding="utf-8")
        units = data.split("\n- id: ")[1:]
        evid = tsv(evidence_path)
        assert int(record["candidate_units"]) == len(units)
        assert int(record["evidence_rows"]) == len(evid)
        assert int(record["candidate_contract_missing_count"]) == 0
        assert int(record["candidate_source_loci_not_in_evidence"]) == 0
        assert int(record["missing_source_location_or_sha"]) == 0
        locations = set()
        for item in evid:
            for col in ("source_locus", "epub_path"):
                require(item[col], (book, typ, col))
            assert re.fullmatch(r"[0-9a-f]{64}", item["chapter_sha256"])
            assert re.fullmatch(r"[0-9a-f]{64}", item["paragraph_sha256"])
            locations.add(item["source_locus"])
        for item in units:
            assert "source_loci:" in item
            assert all(field + ":" in item for field in fields), (book, typ, item[:80])
            match = re.search(r"source_loci:\s*\n((?:[ \t]+-[^\n]*\n)+)", item)
            assert match is not None, (book, typ, "empty candidate loci")
            actual_loci = set(re.findall(r"n\d{3}/p\d+", match.group(1)))
            assert actual_loci <= locations, (book, typ, actual_loci - locations)
        sum_candidates += len(units)
    assert sum_candidates == expected, (book, sum_candidates)

for p in [
    "v13_3/n16/N16_CROSS_OBJECT_AUDIT.md",
    "v13_3/n16/N16_BOOK_OVERVIEW_AUDIT.md",
    "v13_3/n16/N16_STAGE0_20_TO_19_AUDIT.md",
]:
    assert len((ROOT / p).read_text(encoding="utf-8")) > 500, p
print("PASS N16 referential structural contract: B296 (243 scoped+53 rejected), Q14 open,")
print("20 frozen Stage0 tasks to 19 topic mappings, WM/TX original five extractors, no method promotions; NOT an independent literary or Skill test.")
