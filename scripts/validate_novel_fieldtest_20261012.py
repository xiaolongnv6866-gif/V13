#!/usr/bin/env python3
"""V13 experimental fiction continuity smoke test. NOT independent literary quality certification."""
from pathlib import Path
import hashlib
import json
import re
from collections import Counter

ROOT = Path(__file__).resolve().parents[1]
DIR = ROOT / "experiments" / "novel_field_test_20261012"

def sha_blob(path):
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()

def read(name):
    return (DIR / name).read_text(encoding="utf-8")

# The two test inputs were committed separately before any chapter outputs.
assert sha_blob(DIR / "FROZEN_INPUT.md") == "1974ce8ca0734d223bf3a98e2413eda8f387412e"
assert sha_blob(DIR / "FROZEN_WORLD.json") == "cb3dd27e5fa0e46a2735a5e1b7419648068b7f3f"
initial = json.loads(read("FROZEN_WORLD.json"))["starting_state"]
assert initial["warehouse_paper"] == initial["warehouse_physical"] + initial["undelivered_promises"] == 36
assert initial["warehouse_physical"] == initial["wet_frozen"] + initial["dry_available"] == 24
assert initial["public_silver"] == 6
assert initial["east_verified_households"] is None

for filename in ("EXPERIMENTAL_SKILL.md", "OUTLINE.md", "STATE.json", "EDIT_AUDIT.md", "README.md"):
    assert (DIR / filename).is_file(), "Missing required creative artifact: " + filename
    assert len(read(filename)) > 400, "Unusable short artifact: " + filename

chapters = [read("CH01.md"), read("CH02.md"), read("CH03.md")]
chars = []
for i, chapter in enumerate(chapters, 1):
    han = len(re.findall(r"[\u4e00-\u9fff]", chapter))
    chars.append(han)
    assert han >= 900, ("Chapter too short", i, han)
    assert chapter.count("# ") == 1, ("Unexpected chapter heading", i)
    assert chapter.count("\n") > 25, ("Not chapter prose", i)
    assert "陆时安" in chapter and "方启闻" in chapter
    assert "吴嫂" in chapter
    # 苏鹭 first enters on the second chapter; forcing every character into every
    # chapter would invalidate POV and turn the test into an arbitrary cast quota.
    if i >= 2: assert "苏鹭" in chapter
assert len(set(chapters)) == 3

plan = read("OUTLINE.md")
for target in ("A1", "A2", "A3", "陆时安", "吴嫂", "苏鹭"):
    assert target in plan, target
skill = read("EXPERIMENTAL_SKILL.md")
assert skill.startswith("---\nname:")
for critical in ("终局倒推", "逐场", "STATE", "审稿", "未认证"):
    assert critical in skill, critical
assert "DIAGNOSTIC_ONLY" in skill

state = json.loads(read("STATE.json"))
assert state["classification"] == "EXPERIMENT_NONINDEPENDENT"
s = state["chapters"]
assert len(s) == 3 and [x["chapter"] for x in s] == [1, 2, 3]
for x in s:
    assert x["wet_quarantined_bags"] == 6
    assert x["paper_count_historical"] == 36
    assert x["unopened_dry_bags"] + x["wet_quarantined_bags"] == x["physical_warehouse_bags"]
    assert x["original_promised_bags_not_arrived"] == 12
    assert x["boat_deposit_required_taels"] == 8
    assert not x["boat_deposit_paid"]
    assert x["merchant_promise_not_received_taels"] == 5
    assert x["east_households_verified"] is None
    assert x["east_bags_received"] == 0
    assert x["opened_delivered_bags_total"] + x["physical_warehouse_bags"] == 24
assert [x["physical_warehouse_bags"] for x in s] == [24, 24, 20]
assert [x["unopened_dry_bags"] for x in s] == [18, 18, 14]
assert [x["opened_delivered_bags_total"] for x in s] == [0, 0, 4]
assert [x["cash_taels"] for x in s] == [6, 6, 3]
assert [x["old_wages_due_taels"] for x in s] == [3, 3, 0]
assert s[0]["four_bag_permission"] == "DISCUSSION_ONLY"
assert s[1]["four_bag_permission"] == "SIGNED_EFFECTIVE_NEXT_MORNING_TWO_WITNESSES"
assert s[2]["four_bag_permission"] == "EXECUTED_LOCALLY_ONLY_WITNESSED"
assert s[2]["cash_taels"] == s[1]["cash_taels"] - 3
assert s[2]["unopened_dry_bags"] == s[1]["unopened_dry_bags"] - 4
assert state["sources_of_knowledge"]["east_households_17"] == "UNVERIFIED_HEARSAY"
assert state["sources_of_knowledge"]["boat_contract"] == "NOT_SIGNED_OR_PAID"
assert state["sources_of_knowledge"]["second_receipt"] == "NOT_YET_EXAMINED"
assert "独立" in read("EDIT_AUDIT.md") and "不足" in read("EDIT_AUDIT.md")

# Narrative action markers are diagnostic smoke checks only; no quality or independent score.
assert "受潮" in chapters[0] and "三十六" in chapters[0] and "未到" in chapters[0]
assert "八两" in chapters[1] and "六两" in chapters[1] and "收讫" in chapters[1]
assert "十四袋" in chapters[2] and "三两" in chapters[2] and "未见河东交接" in chapters[2]
print("PASS V13 fiction fieldtest: 3 full chapters", chars,
      "Han chars; frozen source checked; 24->20 bags, 6->3 silver, 0 east delivery; NONINDEPENDENT")
