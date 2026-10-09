# V13 — 新会话唯一启动与恢复协议

**已完成R001的独立仓库初始化；当前工作轮次不是R001而是GitHub游标规定的R002。** 此行是2026-10-09首版说明；以后无论这里的文本如何过时，均以`CURRENT_ROUND.json`、`ROUND_LEDGER.csv`与`PROGRESS.md`互相核对为唯一真实状态。

1. 先从`https://github.com/xiaolongnv6866-gif/V13`的main分支读取`CURRENT_ROUND.json`、`ROUND_LEDGER.csv`、`PROGRESS.md`，如有矛盾暂停。
2. **先读取 `STAGE0_QUALITY_CONTROL_POLICY.md` 与 `cangjie/reading/STAGE0_QUALITY_DEBT_AUDIT.md`：保留旧真实来源研究，风险抽审定向修复，不清零也不虚报文学验证。** 再从`V13_FIXED_89_ROUNDS.md`读取当前轮**完整必须操作、原版依据、产物、验收与用户门**，再读取`ROUND_EXECUTION_RULES.md`。用户2026-10-09最新决定改为手动触发，停止自动跨轮与一小时任务；每次输入『继续』只恢复GitHub游标指定的当前轮；详见`AUTO_CONTINUATION_POLICY.md`。不得跳轮或跳验收。
3. 按`SKILL_SOURCES.md`固定版本完整读取上游Cangjie/Nuwa原始`SKILL.md`与当前阶段全部依赖；不能从旧项目恢复笔记或用摘要替代原版。
4. 当轮需要原著时必须真实取得用户提供的两本EPUB，校验`SOURCE_MANIFEST.md`中的SHA256。公开仓库不含原著，若新对话无法读取则暂停并请用户重新提供；**绝不从目录标题冒充全文阅读**。
5. R002从原文实际OPF spine生成只含元数据的两份CSV，检查章节数/路径异常，按轮次真实要求提交GitHub。此轮之前已完成的本地ZIP预检仅是准备，不等于R002通过。
6. 每轮完工把`runs/R###.md`、产物、`ROUND_LEDGER.csv`、`CURRENT_ROUND.json`和`PROGRESS.md`一次提交，远程回读通过后才升级为下一编号；缺用户明确确认就BLOCKED。
7. 对小说的判断要独立审核文本证据与反例；保留原创叙事、人物选择、对白、视角、节奏和跨章因果。不上传小说全文，不仿写作者专属语句。

**工作起点**：V13文学研究0/1103；Cangjie Stage0未启动；Nuwa Phase0待R004确认；原创写作SKILL0。
## 当前手动触发与跨会话恢复（2026-10-09最新）

用户已撤回同日较早的自动跨轮授权：「一个小时一次太慢了，失去意义，还是我手动吧。」每小时定时任务已停用。只有用户在对话中输入「继续」才启动当前轮，完成并通过后**停下**，等待下一次用户输入，不会在后台自发继续。

当下R011 IN_PROGRESS，081—087七章已存检查点；请从《晚明》有效叙事ordinal088继续到120，完成40章整体文学证据和GitHub真实验收前保持R011，正式进度10/89轮、160/1103章。权威游标永远以GitHub三份状态为准。
