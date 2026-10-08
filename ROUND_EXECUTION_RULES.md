# V13 不允许跳轮的唯一执行规范

1. 按`CURRENT_ROUND.json`找当前轮，与`ROUND_LEDGER.csv`及`PROGRESS.md`一致后才行动。
2. 读取当前轮完整定义和两套原始SKILL当前阶段**全文、全部依赖**；任何与轮次表冲突必须停下告知，不得自行覆盖。
3. **只执行当前轮**。长阅读分子批次留在同一R###；每章正文确实完整审读才算，源Hash PASS不等于文学推断PASS。
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
