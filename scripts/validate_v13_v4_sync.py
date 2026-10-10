#!/usr/bin/env python3
"""Fail closed on V13.3 authoritative round-state disagreement.

Run on all commits touching the V4 cursor, ledger, receipts or recovery entry points.
This verifies administrative consistency, NOT literary review or independent V3 quality.
"""
import csv
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
with (ROOT / "V13_LEDGER_V4.tsv").open(encoding="utf-8", newline="") as fh:
    rows = list(csv.DictReader(fh, delimiter="\t"))
state = json.loads((ROOT / "V13_CURRENT_V4.json").read_text(encoding="utf-8"))

assert state["version"] == "V13.3"
assert len(rows) == state["total_new_rounds"] == 48
assert [r["round_id"] for r in rows] == [f"N{i:02d}" for i in range(1, 49)]
k = state["completed_new_rounds"]
assert isinstance(k, int) and 0 <= k <= 48
assert all(r["status"] == "PASSED" for r in rows[:k]), "Missing PASSED in closed prefix"
assert all(r["status"] != "PASSED" for r in rows[k:]), "An unclosed round is marked PASSED"

if k < 48:
    current = f"N{k + 1:02d}"
    assert state["current_round"] == current, (state["current_round"], current)
    assert state["current_round_status"] == rows[k]["status"]
    assert rows[k]["status"] in {"NOT_STARTED", "IN_PROGRESS", "BLOCKED", "FAILED"}
    assert all(r["status"] == "NOT_STARTED" for r in rows[k + 1:])
else:
    assert all(r["status"] == "PASSED" for r in rows)

for i, row in enumerate(rows, start=1):
    receipt = ROOT / "runs" / f"N{i:02d}_V4.md"
    if i <= k:
        assert receipt.is_file(), f"Closed round missing receipt: N{i:02d}"
        content = receipt.read_text(encoding="utf-8")
        assert re.search(rf"(?m)^round:\s*N{i:02d}\s*$", content)
        assert re.search(r"(?m)^status:\s*PASSED\s*$", content), f"Receipt not PASSED: N{i:02d}"
    elif receipt.is_file():
        content = receipt.read_text(encoding="utf-8")
        assert not re.search(r"(?m)^status:\s*PASSED\s*$", content), f"Unclosed round has premature PASSED receipt: N{i:02d}"

source_rounds = [r for r in rows[:k] if r["stage"] == "A_STORY_SOURCE_REPAIR"]
B_count = sum(int(r["required_objects"]) for r in source_rounds)
first_review = sum(int(r["old_unreviewed_count"]) for r in source_rounds)
q_review = sum(int(r["old_R042_quarantine_count"]) for r in source_rounds)
assert state["v13_3_stage0_B_disposed_this_plan"] == B_count
assert state["v13_3_stage0_B_pending_remaining"] == state["old_stage0_B_total"] - B_count
assert state["v13_3_from_old_192_unreviewed_done"] == first_review
assert state["v13_3_from_old_192_unreviewed_remaining"] == state["old_stage0_B_unreviewed"] - first_review
assert state["v13_3_R042_quarantines_source_reviewed"] == q_review
assert state["v13_3_R042_quarantines_still_not_promoted"] == state["old_R042_quarantined"] == 14

if k:
    last = f"N{k:02d}"
    for path in ("START_HERE.md", "PROGRESS.md"):
        front = (ROOT / path).read_text(encoding="utf-8")[:1800]
        assert last in front and "PASSED" in front, f"Stale recovery entrance: {path}"
        if k < 48:
            assert f"N{k + 1:02d}" in front, f"Missing next cursor at recovery entrance: {path}"

print(f"PASS V13.3 sync: {k}/48 completed; cursor "
      f"{state['current_round']} {state['current_round_status']}; "
      f"Stage0 B {B_count}/296; old first review {first_review}/192; R042 {q_review}/14")
