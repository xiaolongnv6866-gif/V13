#!/usr/bin/env python3
"""V13 E05 - build-only adapter for *pinned original* Cangjie compiler.
Never assert that the original Stage1.5 V3/Stage4 was passed.
One official integrated SKILL.md stays in skills/v13-history-military.
"""
from __future__ import annotations
import argparse
import json
import shutil
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
BOOKS=("wanming","tiexuecanming")
REL=ROOT/"capabilities"/"RELATIONSHIPS.json"

def export(out: Path):
    out.mkdir(parents=True,exist_ok=True)
    for sub in ("cards","book"):
        (out/sub).mkdir(parents=True,exist_ok=True)
    items=[]
    for slug in BOOKS:
        obj=json.loads((ROOT/"capabilities"/"bundles"/f"{slug}.json").read_text(encoding="utf-8"))
        assert obj.get("cangjie_verified") is False
        assert obj["build_only"] is True
        for card in obj["capabilities"]:
            old_id=card["capability_id"]
            new_slug=old_id.lower()
            src=ROOT/card["card"]
            if not src.is_file(): raise FileNotFoundError(src)
            text=src.read_text(encoding="utf-8")
            for label in ("R","I","A1","A2","E","B"):
                if f"## {label}｜" not in text: raise ValueError(f"{old_id}: missing {label}")
            (out/"cards"/f"{new_slug}.md").write_text(text,encoding="utf-8")
            items.append(dict(
                capability_id=f"cap.{slug}.{new_slug}",revision=1,
                status="active", # ONLY Cangjie compiler runtime inclusion, *not* V3 approval.
                slug=new_slug,title=card["title"],
                importance="high",
                importance_rationale=f"映射原创叙事Stage0任务；来源{old_id}；未执行独立V3",
                one_liner=f"通过可见行动核查{card['title']}，标记失败条件与跨章状态。",
                intents=[f"原创小说中处理{card['title']}"],
                keywords=[card["title"],slug,new_slug],
                also_read=[],card=f"cards/{new_slug}.md",
                frontmatter=dict(description=f"原创历史长篇处理{card['title']}；有确定角色行为、信息与资源状态时使用；不得用作现实战术指南。仅建设版，独立V3用户免测。",tags=["fiction","build-only"]),
                source_evidence=[dict(source_id=f"private-epub-{slug}",location=card["loci"],version_id="V13-PRIVATE-EPUB-SHA256")],
                promotion=dict(destination="router",gate=dict(independent_intent=False,independent_contract=False,independent_run=False,independent_reuse=False,independent_eval=False),
                               notes="BUILD_ONLY. V3 and independent Stage4 NOT_RUN_USER_WAIVED. Active is compiler inclusion only."),
            ))
    aliases={cap["slug"]:cap["capability_id"] for cap in items}
    edges=json.loads(REL.read_text(encoding="utf-8"))["edges"]
    for edge in edges:
        a,b=edge["from"].lower(),edge["to"].lower()
        if a in aliases and b in aliases:
            for x,y in ((a,b),(b,a)):
                obj=next(z for z in items if z["slug"]==x)
                obj["also_read"].append(aliases[y])
    for c in items: c["also_read"]=sorted(set(c["also_read"]))
    entry_desc=("Build-only, source-traceable RIA++ reference router for writing, outlining, revising, "
                "and resuming entirely original Chinese historical-military fiction. "
                "Independent Cangjie V3 and Stage4 evaluations were not run by user decision.")
    bundle=dict(schema_version=1,bundle_id="bundle.v13-history-military",
      book=dict(title="《晚明》《铁血残明》双书研究的原创叙事操作",author="V13 study synthesis",
                source_pack="PRIVATE_EPUB_SHA256_ONLY"),
      entry=dict(name="v13-history-military",description=entry_desc,
                 core_principles=["原创人物和事件","权限/资金/物资/认知/关系不跳步","现场行动与后果先于总结","原文锚点可追溯、原著不公开"],
                 out_of_scope=["原著文本仿写","现实伤害性战术教程","未经查核的历史事实推断"],
                 stop_conditions=["来源冲突未澄清","不可挽回的连续性矛盾","输出非原创或缺实质现场"]),
      router_entry=dict(name="v13-history-military",description=entry_desc),
      promotion_budget=8,capabilities=items,
      build_adapter_provenance=dict(independent_V3="NOT_RUN_USER_WAIVED",stage4_external="NOT_RUN_USER_WAIVED",
                                    official_skill="skills/v13-history-military/SKILL.md",
                                    runtime_active_does_not_imply_verified=True))
    try:
        import yaml
    except ImportError as exc:
        raise SystemExit("Needs PyYAML: pip install PyYAML") from exc
    (out/"verified.yaml").write_text(
        "# COMPILER-PROTOCOL NAME ONLY: NOT independently verified, V3 NOT_RUN_USER_WAIVED\n"
        +yaml.safe_dump(bundle,allow_unicode=True,sort_keys=False,width=120),encoding="utf-8")
    shutil.copyfile(ROOT/"capabilities"/"GLOSSARY.md",out/"book"/"glossary.md")
    (out/"book"/"overview.md").write_text(
       "# 来源研究与交付边界\n\n双书属于同一小说作者，不能当两个理论学派；"
       "本构建仅为原版仓颉编译实验。64卡均为非V3的创作辅助。\n",
       encoding="utf-8")
    (out/"book"/"critical-review.md").write_text(
        "# 必守来源约束\n\n私人EPUB不出包；来源仅用章节p锚点与SHA。"
        "一切虚构角色行为不等于作者亲自教授的方法。"
        "不得复制原著具体情节或独特语言。独立效果验证按用户决定未执行。\n",
        encoding="utf-8")
    report=dict(capabilities=len(items),cross_links=sum(len(c["also_read"]) for c in items),
                original_v3="NOT_RUN_USER_WAIVED",
                warning="Adapter produces verified.yaml as an original-compiler REQUIRED FILENAME, not VERIFIED evidence.",
                build_only=True)
    (out/"BUILD_ONLY_ADAPTER_STATUS.json").write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding="utf-8")
    print(json.dumps(report,ensure_ascii=False,indent=2))
    return report

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--out",type=Path,required=True)
    args=p.parse_args()
    export(args.out)
