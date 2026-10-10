#!/usr/bin/env python3
"""B076 three frozen novel V2 walkthroughs: structural checks only, NOT independent literary certification."""
from pathlib import Path
import csv,json,re,subprocess
P=Path(__file__).resolve().parents[1]
f=P/"gates/B076_V2_3_FRESH_TASK_PREREG.json"
p=json.loads(f.read_text(encoding="utf-8"))
assert p["base_main_sha"]=="e8f644ce82ac49cbab6a3b5025fee165db02bc89"
assert p["candidate_ids"]==["WM-f15","WM-p09","WM-p17"]
assert len(p["tasks"])==3
rows=list(csv.DictReader((P/"gates/B076_V2_3_ACTUAL_WALKTHROUGH_RESULTS.tsv").open(encoding="utf-8"),delimiter="\t"))
assert len(rows)==3 and len({r["candidate_id"] for r in rows})==3
src={r["candidate_id"]:r for r in csv.DictReader((P/"gates/B076_V1_4_NARROW_FINAL_ADJUDICATION.tsv").open(encoding="utf-8"),delimiter="\t")}
required={
 "WM-f15":["陆霁","许穗","赵平","东阁","西厢","修订","未知"],
 "WM-p09":["苏仰","杜函","房东","纸商","十二两","五两","三两"],
 "WM-p17":["沈窈","顾岑","阿洛","隔壁私塾","事务","资金","人员","资产","未同意"]
}
for task in p["tasks"]:
 id=task["candidate_id"]
 r=next(x for x in rows if x["candidate_id"]==id)
 assert r["freeze_commit"]=="84f5988e14a5c5b950e27c5d81c6422b280c62c0"
 assert r["source_V1_status"]==src[id]["V1"]=="PASS_NARROW"
 assert r["V2_test_type"]=="SINGLE_AGENT_NEW_INPUT_WALKTHROUGH"
 assert r["V2_decision"]=="WALKTHROUGH_PASS_LIMITED"
 assert r["V3_independent"]=="NOT_RUN" and r["stage4"]=="NOT_RUN" and r["four_way"]=="needs_review"
 assert r["literary_qualitative_review"]=="SAME_AGENT_CONTEXT_NO_BLIND"
 dest=P/r["original_output_path"]
 assert dest.is_file() and dest.parent==P/"tests/b076_v2_3_outputs"
 s=dest.read_text(encoding="utf-8")
 for label in p["common_rules"]["required_sections"]:assert label in s,(id,label)
 assert "task_id: "+task["id"] in s and "candidate_id: "+id in s
 scene=s.split("## 原创场景",1)[1].split("## 状态与来源账",1)[0]
 size=len(re.findall(r"[\u3400-\u9fff]",scene))
 assert p["common_rules"]["min_chinese_chars_scene"]<=size<=p["common_rules"]["max_chinese_chars_scene"]
 assert size==int(r["scene_han_characters"])
 for token in required[id]:assert token in s,(id,token)
 assert "必须拒绝" in s and "## 反例检查" in s
 assert "原著" not in scene and "陈新" not in scene and "庞雨" not in scene
 assert s.index("## 原创场景")<s.index("## 状态与来源账")<s.index("## 反例检查")<s.index("## 结论与未决事项")
state=json.loads((P/"V13_CURRENT_V3.json").read_text())
assert state["current_batch"]=="B076" and state["batch_status"]=="BLOCKED"
assert state["overall_management_units_completed"]==75 and state["skill_certified_count"]==0
assert state["b076_decisions"]["verified"]==0
assert state["b076_v2_walkthrough_limited_count"]==3
assert state["b076_real_v3_replicates"]==0 and state["b076_stage0_full_independent_acceptance"]==0
assert len(list((P/"tests/b076_v2_3_outputs").glob("*.md")))==3
print("PASS structural: 3 frozen-before-output V2 walkthroughs + three distinct original scenes; 0 independent V3; B076 BLOCKED. Narrative quality still requires outside assessment.")
