#!/usr/bin/env python3
"""Fail-closed *structural* pre-publication check for original V13 chapters.

This does NOT independently evaluate literary quality, historical correctness,
or prove that a model internally used a method card.
"""
from __future__ import annotations
import argparse
import difflib
import json
from pathlib import Path
from validate_state import validate, LedgerError

SKILL_ROOT = Path(__file__).resolve().parent.parent
BRIEF_FIELDS = (
    "可观察目标", "时间地点、人物站位和进入时动作", "POV及其未知情报",
    "场内每人自身目标/能拒绝什么", "行动→反应→逆转→选择→差分",
    "退出场景时具体悬念", "跨三章因果义务",
)
HISTORY_CLASSES = {"VERIFIED_HISTORICAL", "IN_WORLD_FICTION", "CHARACTER_BELIEF"}
NUWA_MODELS = {"M1", "M2", "M3", "M4"}

class GateError(ValueError):
    pass

def need(test, msg):
    if not test:
        raise GateError(msg)

def substantive(x):
    return isinstance(x, str) and len(x.strip()) >= 4

def read(path):
    need(path.is_file(), f"missing artifact: {path}")
    return path.read_text(encoding="utf-8")

def records(data, name, keys, minimum):
    items = data.get(name)
    need(isinstance(items, list) and len(items) >= minimum, f"{name}: need {minimum} entries")
    for i, item in enumerate(items):
        need(isinstance(item, dict), f"{name}[{i}] must be object")
        for key in keys:
            val = item.get(key)
            need(isinstance(val, str) and val.strip()
                 and (key in {"id", "name", "classification"} or substantive(val)),
                 f"{name}[{i}].{key} missing")
    return items

def verify(project: Path, chapter: int, skill_root: Path = SKILL_ROOT):
    need(type(chapter) is int and chapter >= 1 and project.is_dir(),
         "invalid chapter or project")
    base = f"CHAPTER_{chapter:03}"
    bible = read(project / "PROJECT_BIBLE.md")
    brief = read(project / (base + "_BRIEF.md"))
    draft = read(project / (base + "_DRAFT.md"))
    final = read(project / (base + ".md"))
    next_scene = read(project / "NEXT_SCENE.md")
    receipt = json.loads(read(project / (base + "_REVIEW.json")))
    state = json.loads(read(project / "STATE.json"))
    need(len(bible.strip()) >= 200, "PROJECT_BIBLE not substantive")
    need(len(final.strip()) >= 800 and len(draft.strip()) >= 800,
         "chapter not a complete prose sample")
    need(len(next_scene.strip()) >= 24, "NEXT_SCENE needs a concrete pressure")
    for label in BRIEF_FIELDS:
        matches = [line.split("：", 1)[1].strip() for line in brief.splitlines()
                   if line.strip().startswith(label + "：")]
        need(any(substantive(x) for x in matches),
             "chapter brief field missing/empty: " + label)
    need(receipt.get("schema") == "v13-chapter-review-receipt-1",
         "wrong receipt schema")
    need(receipt.get("chapter") == chapter, "receipt chapter mismatch")
    need(receipt.get("status") == "REVISED_AND_RECHECKED",
         "adversarial revision and recheck incomplete")
    for key in ("opening_goal", "exit_change", "unpaid_obligation"):
        need(substantive(receipt.get(key)), "missing: " + key)
    actors = records(receipt, "independent_characters",
                     ("name", "wants", "can_refuse", "choice", "consequence"), 2)
    need(len({x["name"] for x in actors}) == len(actors),
         "duplicate independent character")
    scenes = records(receipt, "scenes",
                     ("entry", "conflict", "choice", "visible_delta", "cost"), 2)
    cards = records(receipt, "applied_cards",
                    ("id", "why", "how", "boundary"), 1)
    need(len(cards) <= 12, "over-routing: use only matching method cards")
    card_ids = {p.stem for p in (skill_root / "capabilities/cards").glob("*.md")}
    need(card_ids, "skill method cards unavailable")
    for card in cards:
        need(card["id"] in card_ids, "unknown card: " + card["id"])
    models = records(receipt, "nuwa_models", ("id", "why", "observed_effect"), 1)
    for model in models:
        need(model["id"] in NUWA_MODELS, "unknown Nuwa model: " + model["id"])
    history = records(receipt, "history_boundaries",
                      ("claim", "classification", "evidence_or_assumption"), 1)
    for item in history:
        need(item["classification"] in HISTORY_CLASSES,
             "history category is not verified/fiction/character belief")
    fixes = records(receipt, "adversarial_fixes",
                    ("draft_excerpt", "fault", "final_excerpt", "state_delta"), 2)
    for item in fixes:
        need(item["draft_excerpt"] in draft, "review quotation missing from draft")
        need(item["final_excerpt"] in final, "edited quotation missing from final")
        need(item["draft_excerpt"] != item["final_excerpt"], "review edit unchanged")
    need(draft != final and
         difflib.SequenceMatcher(None, draft, final, autojunk=True).ratio() < .997,
         "no substantive difference between draft and final")
    try:
        checked = validate(state)
    except (LedgerError, KeyError, TypeError) as e:
        raise GateError("invalid state: " + str(e)) from e
    need(state.get("project") != "YOUR_NEW_ORIGINAL_NOVEL", "state is a placeholder")
    chapter_events = [x for x in state.get("events", []) if x.get("chapter") == chapter]
    need(chapter_events, "chapter has no state events")
    need(any(base + ".md" in x.get("evidence_ref", "") for x in chapter_events),
         "state lacks source link to this finalized chapter")
    need(bool(state.get("open_loops")), "no open loops recorded")
    need(substantive(state.get("next_chapter_brief")), "next chapter brief empty")
    return {"result": "PASS_STRUCTURAL_GATE_ONLY", "chapter": chapter,
            "actors": len(actors), "scenes": len(scenes),
            "cards": [x["id"] for x in cards], "nuwa": [x["id"] for x in models],
            "revisions": len(fixes), "events": checked["events"],
            "warning": "NOT literary quality, historical proof, or independent V3."}

def main():
    parser = argparse.ArgumentParser(description="Structural publication gate for V13 chapters")
    parser.add_argument("--project", type=Path, required=True)
    parser.add_argument("--chapter", type=int, required=True)
    args = parser.parse_args()
    try:
        outcome = verify(args.project, args.chapter)
    except (GateError, ValueError, OSError, json.JSONDecodeError) as e:
        print(json.dumps({"result": "FAIL", "reason": str(e)}, ensure_ascii=False))
        raise SystemExit(1)
    print(json.dumps(outcome, ensure_ascii=False, sort_keys=True))

if __name__ == "__main__":
    main()
