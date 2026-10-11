#!/usr/bin/env python3
"""Produce the brief from authoritative current files; use --check to fail closed."""
from __future__ import annotations
import csv
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
s = json.loads((ROOT / "V13_CURRENT_V4.json").read_text(encoding="utf-8"))
lock = json.loads((ROOT / "V13_3_GOVERNANCE_LOCK.json").read_text(encoding="utf-8"))
with (ROOT / "V13_LEDGER_V4.tsv").open(encoding="utf-8", newline="") as stream:
    ledger = list(csv.DictReader(stream, delimiter="\t"))
if "--check" in sys.argv:
    subprocess.run([sys.executable, str(ROOT / "scripts/validate_v13_governance.py")], check=True)
    subprocess.run([sys.executable, str(ROOT / "scripts/validate_v13_v4_sync.py")], check=True)
current = next((x for x in ledger if x["round_id"] == s["current_round"]), None)
if not current or current["status"] != s["current_round_status"]:
    raise SystemExit("BLOCKED: remote ledger/cursor disagree")
out = {
    "authority": ["V13_CURRENT_V4.json", "V13_LEDGER_V4.tsv", "V13_3_FIXED_48_ROUNDS.md"],
    "round": current["round_id"],
    "round_status": current["status"],
    "completed": s["completed_new_rounds"],
    "total": s["total_new_rounds"],
    "must_read_current_round_full_contract": "V13_3_FIXED_48_ROUNDS.md",
    "stage": current["stage"],
    "required_objects": current["required_objects"],
    "tasks": current["tasks"],
    "acceptance": current["acceptance"],
    "user_gate": current["required_user_gate"],
    "original_source_rounds": current["original_source_rounds"],
    "skill_pins": lock["original_skills"],
    "critical_deficits": {"independent_V3": "not proven until independently executed", "original_Stage0_C": "20 frozen tasks", "certified_skills": s["certified_skills"]},
    "do_not_advance_without": ["source/quality/independent evidence as applicable", "all relevant CI", "final commit and remote readback"]
}
print(json.dumps(out, ensure_ascii=False, indent=2))
