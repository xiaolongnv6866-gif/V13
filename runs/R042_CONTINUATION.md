# R042｜用户继续后的定向来源修复

status: BLOCKED_PENDING_USER_CONFIRMATION
base_main: 4dd1d14d47d5057e72c2740ba2603bd910833d75
source: 用户两份原EPUB；原SHA匹配
coverage: 正文历史登记1103章不变，本次五章31个段落位置复核

本次针对R008、R013、R017、R018、R023原证据的五处解释范围偏大，新增准确位置与竞争解释。详情以`cangjie/reading/R042_TARGETED_REPAIR.md`及`R042_TARGETED_SOURCE_EVIDENCE.tsv`为准。五条旧claim_id均为SUPERSEDED_FOR_EXTRACTION，修订后仍为PROVISIONAL，旧历史批次其余质量债保持开放。

A：本地原文校验；公开CI仅SOURCE_STRUCTURE_ONLY。B：PROVISIONAL。C：NOT_RUN。正式完成41/89，R042 BLOCKED，R043 NOT_STARTED，Stage0 NOT_PASSED，Skill 0。仅新明确批准两书BOOK_OVERVIEW才可解除用户确认门。

## 用户再次「继续」：第二批历史债务质量抽审

对照Stage0旧质量债台账事前选定R009/R011/R012/R014/R016/R019/R020/R021/R022九批次各1个CLOSE_READ；按用户原EPUB重新细查9个实际章、35处段落SHA，保留旧弱支持点、必要上下文和反向位置。新增`cangjie/reading/R042_RISK_WAVE2_EVIDENCE.tsv`、`cangjie/reading/R042_RISK_WAVE2_AUDIT.md`与`scripts/validate_r042_risk_wave2.py`。R011 n099原p28确有错配，但进一步通读该章后半部p39发现相关说法，改判`REVISED_PROVISIONAL`，原错误锚点不用；R021 n305旧证据局部有效判`CONFIRMED_NARROW_PROVISIONAL`；其余七条`REVISED_PROVISIONAL`，必须在提取前以新证据复核。不能把9个风险选样的失败比例冒充296条声明整体失败率。A私有原始ZIP哈希复核，公开CI仅SOURCE_STRUCTURE_ONLY；B PROVISIONAL，C NOT_RUN；Stage0尚待用户书面确认，R042 BLOCKED，正式41/89、R043未启动。先验证GitHub Actions及远程回读，绝不提前报告通过。

**纠偏经过保留**：初步抽看R011 n099/p28未见旧候选涉及的身份归类，曾准备剔除整条旧命题；后来继续检查该章p34—40，在p39确见人物提出重新命名身份的对白，故不应把原证据失配误当全章机制不存在。改为p39窄范围有效、p28失配，所有衍生伦理和历史合法性仍未证实；最新公开证据表35行。此项复核优先于本轮初始暂定判断，不应误读为藏匿错误。

GitHub第二批首稿提交`49509701e02bc76dff4b33f4f6f7ebea90227f3b`，专项R042 run [37934840468](https://github.com/xiaolongnv6866-gif/V13/actions/runs/37934840468)首次FAILED：公开审计尚未明确写出后段补证角色`LATE_CORRECTIVE`，虽然TSV已有该真实位置。修正仅增加审计解释，validator不降标准；全套Actions须另核，R042仍BLOCKED。

## R042第三次「继续」：两书总览验收准备及14条历史候选隔离

- GitHub远程HEAD核对上一正式提交`8329888207eb61dae8a140bcf1fecd74ee1f59f7`，游标R042 BLOCKED、R041最后通过、41/89、R043 NOT_STARTED。读取原固定Cangjie Stage0 Adler四步及BOOK_OVERVIEW模板、Nuwa固定SKILL阶段约束；未修改版本或冻结合同。
- 本次不冒充又一次独立原创盲评或全文重读；整合R042两次来源抽审：前5条原始旧候选+后一批9条，共14条原始claim_id，按原R008—R023对应历史JSON收据回查全部14条ID存在。录入`cangjie/reading/R042_OLD_CLAIM_QUARANTINE.tsv`，标原support和修订源位、`NO_DIRECT_PROMOTION_RECONSTRUCT_FROM_SOURCE`，未复核的剩余旧机制默认B PROVISIONAL而非事实认证。
- 输出一页`cangjie/reading/R042_APPROVAL_BRIEF.md`：明确两书六段/核心理解/边界与9+10项任务，并区分《晚明》原OPF卷段与《铁血残明》研究者划分六弧，提供须由用户具体决定的批准范围。两份原版BOOK_OVERVIEW追加该决策材料和旧历史质量债隔离入口；原模板四步保留。
- 增加`scripts/validate_r042_gate_brief.py`和R042 Actions新检查，要求14条旧ID真实存在、未标B VERIFIED、两书审批仍PENDING且游标BLOCKED，验证公开SOURCE_STRUCTURE_ONLY。补充R042审核政策记录、项目进度和两书Pipeline State。没有用户独立批准，**不能正式PASS或启动R043**。
- 来源层A=既有原始EPUB和段落定位阶段性可追溯；B=PROVISIONAL且残留旧质量债；C=NOT_RUN；技能数=0。新增质量闸脚本不允许把Github工作流绿灯当作用户明确签署。
