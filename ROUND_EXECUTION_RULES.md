# V13 不允许跳轮的唯一执行规范

1. 按`CURRENT_ROUND.json`找当前轮，与`ROUND_LEDGER.csv`及`PROGRESS.md`一致后才行动。
2. 读取当前轮完整定义和两套原始SKILL当前阶段**全文、全部依赖**；任何与轮次表冲突必须停下告知，不得自行覆盖。
3. **一轮只执行当前固定工作包；需要用户在对话中明确触发下一次执行**（2026-10-09更新）：用户发送『继续』时先从GitHub读取当前游标；若当前轮 IN_PROGRESS，从真实未读位置恢复而不重头开始；若 NOT_STARTED，启动此轮。完成本轮必须按原始SKILL做证据、质量检查、原子提交和远程回读；**一轮PASS后停止，不自动开始下一轮，等待下一次用户指令**。正文必须实际全文审读，源Hash PASS不能替代文学理解。
4. 每轮保存`runs/R###.md`：source_epub_sha、upstream_git_sha、时间、动作证据、输入与章内定位、成功/失败项、质量测试、用户门、文件名、提交SHA、回读SHA。
5. 所有验收结果必须分开：来源真实性、文学分析充分性、原创新输入的写作任务表现。
6. 一轮未完成IN_PROGRESS，失败FAILED，待用户确认BLOCKED；不能自动编号+1。对于用户确认门（R004/R042/R057/R068/R069/R077/R080/R083/R086/R089），必须具体成果与用户明确批准。
7. 更新本轮产物、`ROUND_LEDGER.csv`、`CURRENT_ROUND.json`、`PROGRESS.md`时使用同一GitHub提交，**远程回读**核对后才称通过，并更新下一轮。
8. 如果该轮依赖用户授权以外的来源/代理/安装/预算，暂停，先列事实、限制及安全替代方案，不能悄悄跳过。
9. 严禁从V12旧研究复制；不上传原著长段/全文，不提取危险实施技巧；原创写作不复刻原著故事和专属语言。
10. 89轮为固定管理编号。若原版SKILL的硬要求与固定89轮主题路径发生矛盾，例如R004选择人物路径而R070以后假设主题路径，先BLOCKED并取得用户明确许可修订版本。

## 运行记录格式
```
round_id: R###
status: IN_PROGRESS|FAILED|BLOCKED|PASSED
upstream_cangjie_sha:
upstream_nuwa_sha:
source_epub_sha:
input_ordinal_ranges:
actual_actions:
artifacts:
source_integrity_checks:
interpretation_and_counterexamples:
independent_output_tests:
user_decision:
git_commit_sha:
remote_readback:
next_round:
```

## 用户最新指令｜2026-10-09 手动启动（高于同日早先自动授权）

用户明确说明：「一个小时一次太慢了，失去意义，还是我手动吧。」**取消每小时定时自动执行和自动跨轮**，后续每次由用户在对话中输入「继续」或新的明确指令才运行。此前“完成一轮自动开始下一轮”的许可已撤回，不能继续用旧许可为无人值守或自动跨轮执行辩护。

- V13后台自动化“V13 连续研究执行”已确认 `is_enabled=false`。**不要重建、启用其他定时任务**，除非用户再次明确要求。
- 每条「继续」恢复**当前唯一轮**；当前轮若是IN_PROGRESS，应从上次真实检查点恢复，读到缺的章节并验收，不要丢弃以前已经读过的成果。当前轮完成并PASS后更新下一轮游标，但**不主动执行下一轮**；用户再次输入「继续」才开始。
- 全部89轮的固定编号、章节覆盖、源EPUB SHA、原版仓颉/女娲流程、写作独立质量审计、GitHub Actions、实际远程回读，以及R042等必审用户关口照常生效。
- 本修改仅是执行调度策略，不是文学工作；原正式进度保持R010 PASSED、R011 IN_PROGRESS、已认证10/89轮及160/1103章，R011已看081—087、下次从088开始。
- 最新调度策略见 `AUTO_CONTINUATION_POLICY.md`；旧自动授权只留历史归档，不再有效。
