# V13 任何新会话的唯一恢复入口

1. **不使用旧聊天作为任务状态**。先从`https://github.com/xiaolongnv6866-gif/V13`的默认分支读取`CURRENT_ROUND.json`、`ROUND_LEDGER.csv`、`PROGRESS.md`，三者互核；如冲突，BLOCKED而非猜测。
2. 读取`V13_FIXED_89_ROUNDS.md`当前R###整段及`ROUND_EXECUTION_RULES.md`，确认本轮产物与验收。
3. 从`SKILL_SOURCES.md`指定的固定commit读取**完整原始**仓颉、女娲`SKILL.md`及当前阶段全部methodology、extractors、模板、脚本、检查门，不可用本地摘要替代。
4. **原著仅可从用户实际提供的EPUB读取**，两本SHA须匹配`SOURCE_MANIFEST.md`；卷界/路径需由`scripts/build_v13_spine.py`独立重建。当前仓库不包含版权EPUB；新对话若未挂载原书，暂停R002或阅读轮并要求用户提供，**绝不能编造阅读**。
5. 一次普通“继续”只执行当前编号；未完成原轮续做。用户明确要求多轮才可逐轮实际完成、提交、远程回读后推进。遇R004等用户确认门必须明确确认，不用“继续”默认通过。
6. 提交`runs/R###.md`、本轮产物、ledger、cursor、progress同一事务；远程回读所有关键文件后才能宣称PASSED。
7. 绝不能把文件SHA检验当成文学解释审核、把旧原著片段换词当原创、把原版工具脚本通过当V13创作SKILL通过。V13最终SKILL须经独立原创盲测、新聊天独立恢复。

**当前初始状态**：R001仓库初始化；0章正式全文研究；Nuwa Phase0用户决策在R004；正式SKILL0。