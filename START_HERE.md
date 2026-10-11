# V13｜正式恢复入口：批准11工作包

**现行V5：W01 IN_PROGRESS，0/11。旧V4历史：N20 PASSED、N21 NOT_STARTED，20/48。** 旧N轮不再推进或作为游标；原N01—N20全部收据保持只读。
用户2026-10-12明确批准28个未开始N轮合并为11工作包。完整责任保留，详情见`V13_W_MIGRATION_APPROVAL_20261012.md`。

## 同一main HEAD最小零信任恢复
1. 读`V13_W_CURRENT_V5.json`、`V13_W_LEDGER_V5.tsv`、`V13_APPROVED_11_WORKPACKAGES.md`、`V13_W_GOVERNANCE_LOCK.json`和`NEXT_ACTION.md`；比对当前包及状态。
2. 对应`V13_W_MIGRATION_MAP_V5.tsv`定位原N21—N48合同，在`V13_3_ORIGINAL_44_CONTRACTS_MAP.tsv`定位原R067—R110必做项；参见全历史`V13_GLOBAL_TRACEABILITY_1058.tsv`及`PROJECT_MASTER_AUDIT_20261012.md`。
3. 根据正在执行的阶段实际读取钉住的Cangjie/Nuwa`SKILL.md`和全部适用methodology、templates、extractors、scripts；`SKILL_SOURCES.md`只是索引，不可代替原版。
4. 执行`python3 scripts/v13_resume.py --check`；检查来源/文学/真正独立评测等级、保留题、失败及原版用户确认。提交并远程回读后才能将包标PASSED。用户继续即推进当前许可的工作，而不是重复讲计划。
5. 禁止自动后台工作或未经批准花费；独立主体确实不可用应停相关关口并展示选择；未阻断的工作继续。

**历史治理说明**：`V13_3_RECOVERY_GUARD.md`与`V13_3_GOVERNANCE_LOCK.json`为老V4冻结证据，不再是唯一执行权威。旧`V13_CURRENT_V4.json`、`V13_LEDGER_V4.tsv`、`V13_3_FIXED_48_ROUNDS.md`不修改。

两部用户私有原著EPUB不进入公开GitHub。296文学审查/14隔离、187候选、69原V3、20原创C、44合同、35义务和全部失败完整承接。终验仍是实际高质量原创连续正文、修稿和新聊天真实加载。
