# V13.3｜唯一轻量恢复入口

状态快照（2026-10-12）：**N01—N20 PASSED；N21 NOT_STARTED（20/48）**。此行供人核对；每次执行必须先从远程 **V13_CURRENT_V4.json** 与 **V13_LEDGER_V4.tsv** 实时确认，不允许以静态快照覆盖。

## 每次最小读取集合
1. **V13_CURRENT_V4.json**：唯一当前轮与完成数量；**V13_LEDGER_V4.tsv**：只解释当前轮及其依赖的行。
2. **V13_3_FIXED_48_ROUNDS.md**：当前轮的完整合同、用户关口及必要前置条件；按当前轮需要读取对应的 V13_3_* 映射表与历史原始合同，不可漏项。
3. **ROUND_EXECUTION_RULES.md**：现行全局不变量；**SKILL_SOURCES.md**：仓颉、女娲钉住的原始版本。进入适用阶段时必须实际读取原版SKILL正文和全部适用依赖，不能以本入口代替原始流程。
4. **NEXT_ACTION.md**：只作简短导航；执行证据在当前轮的 v13_3/nNN、runs/NNN_V4.md 和关联来源/脚本中。只读取确有依赖的历史文件、检验结果和原著原文。

## 执行边界
- 用户每条新的“继续”最多执行当前N轮，PASS后等下一条用户消息；遇重大阻断或新增成本按已批准48轮合同报告，不能擅自减标、跳轮或改计划。
- 分别检验**原文来源真实性、文学理解充分性、独立原创效用**。SHA或CI结构通过≠文学审查≠真正独立V3≠已认证Skill。
- 用户提供的两部原著EPUB正文不在公开仓库；如果当前运行环境无原文，只能复核仓库存量证据，不许冒充重新阅读。
- 轮次完成时保留完整研究成果、失败记录、关联提交和远程回读。精简的是恢复入口，不是成果或验证流程。
- 不把旧的 CURRENT_ROUND.json、ROUND_LEDGER.csv、V13_CURRENT_V2/V3、旧89/110/96轮计划当作当前启动游标。

## 历史文档
清理之前的长版START_HERE与PROGRESS及旧入口[保留原始Git blob归档](archive/2026-10-11-pre-cleanup/CLEANUP_MANIFEST.md)，按需查证，平时不全文读取。

## 必须执行的零信任恢复补充（2026-10-11维护，不移动轮次）
先遵循 [V13_3_RECOVERY_GUARD.md](V13_3_RECOVERY_GUARD.md)，核对 [V13_3_GOVERNANCE_LOCK.json](V13_3_GOVERNANCE_LOCK.json) 的原版SKILL SHA与正式48轮Git blob锁。代码检验：`python3 scripts/v13_resume.py --check`；变更用户审批要求见 [V13_3_CHANGE_CONTROL.md](V13_3_CHANGE_CONTROL.md)。**保留完整原始验收；该校验仅防行政漂移，不能代替文学/盲测质量。**

## 全原版执行 + 真正写小说的唯一新增强制入口
- [35项原版SKILL工序与证据映射](V13_3_FULL_SKILL_REQUIREMENTS.tsv)；[原48轮内一次完工路径](V13_3_FINISH_TO_SKILL_PLAN.md)；[五项原创长篇能力最终验收](V13_3_SKILL_DELIVERY_ACCEPTANCE.md)。
- 恢复时只能把此清单当“检查是否遗漏”的工具，**不得代替仓颉/女娲锁定上游原版逐阶段全文及所有适用文件**。已经存在的旧文学研究并不代表真正写作Skill可调用。
