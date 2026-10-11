#!/usr/bin/env python3
"""Build an explicit carry-forward context for a new chat. Not an auto-installed ChatGPT Skill."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
from validate_state import validate

ROOT = Path(__file__).resolve().parent.parent


def render(state, skill_text, last_chapter):
    r = validate(state)
    active = {k: v for k, v in r["balances"].items()}
    facts = r["facts"]
    characters = []
    for actor in state.get("characters", []):
        characters.append(
            "- " + actor["name"] + "｜确知：" + "、".join(actor.get("knows", [])) +
            "｜听闻：" + "、".join(actor.get("heard", [])) +
            "｜目标：" + actor.get("goal", "未定"))
    return (
        "# V13 原创小说 ALPHA 显式跨聊天载荷（非原生自动安装）\n\n"
        "请按下述实验版SKILL工作流继续**原创小说**；不得把独立V3、女娲双主体和外部盲评写成已通过。"
        "不需要重新阅读两部版权原著才能用此原创场景续写。\n\n"
        "## A. 当前实际SKILL（ALPHA，不是最终融合认证）\n\n"
        + skill_text + "\n\n## B. 已核账的续写状态\n\n"
        + json.dumps(active, ensure_ascii=False, indent=2)
        + "\n\n## C. 事实可靠等级\n\n"
        + json.dumps(facts, ensure_ascii=False, indent=2)
        + "\n\n## D. 人物各自所知与目标\n\n"
        + "\n".join(characters)
        + "\n\n## E. 待偿的真实因果\n\n"
        + "\n".join("- " + loop["issue"] for loop in state["open_loops"])
        + "\n\n## F. 下一章入口\n\n"
        + state.get("next_chapter_brief", "")
        + "\n\n## G. 最近正文（仅承接创作，不当历史来源）\n\n"
        + last_chapter
        + "\n\n当前任务：先核实场内权限、资源与角色认知，再写下一章完整正文，"
          "写完交新的事件与状态账，不要用剧情摘要替代。\n"
    )


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--state", default=str(ROOT / "fixtures" / "chaoxun_ch03.json"))
    p.add_argument("--skill", default=str(ROOT / "SKILL.md"))
    p.add_argument("--last-chapter",
                   default=str(ROOT.parent.parent / "experiments" /
                               "novel_field_test_20261012" / "CH03.md"))
    p.add_argument("--out", required=True, help="Explicit handoff markdown destination")
    a = p.parse_args()
    state = json.loads(Path(a.state).read_text(encoding="utf-8"))
    body = render(state, Path(a.skill).read_text(encoding="utf-8"),
                  Path(a.last_chapter).read_text(encoding="utf-8"))
    out = Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(body, encoding="utf-8")
    print("STRUCTURE_ONLY_HANDOFF_GENERATED", out, len(body))


if __name__ == "__main__":
    main()
