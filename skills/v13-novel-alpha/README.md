# V13 原创历史军事写作 ALPHA｜可显式加载，未认证

此目录是从前次真实三章创作与世界连续性缺陷中整理出的**可运行实验SKILL包**，而不是项目正式“仓颉蒸馏/女娲主题Skill/两者融合”已通过的证明。真正身份为 `ALPHA`；V13 V5当前仍W01 BLOCKED、独立V3=0、认证=0。

## 你现在就能用的东西

1. `SKILL.md` 是可供普通模型明确读取的入口；首次用先将它与正在处理的原创小说状态一同提交给模型。
2. `references/NARRATIVE_ENGINE.md` 控制全书终局反推、人物独立动机、镜头化场景、长期因果；`STATE_PROTOCOL.md` 管权限、资源、认知；`EDITOR_PROTOCOL.md` 管现场改稿。
3. `templates/CHAPTER_BRIEF.md` 和 `templates/STATE_TEMPLATE.json` 可以复制建立新原创项目。
4. `scripts/validate_state.py` 真正执行一致性检查，包括现货与未到货、欠薪支付、授权时序和封顶额度、传闻核实证据、章序。它不提供史实真实性认证和文学独立评分。
5. `fixtures/chaoxun_ch03.json` 将此前实际原创《潮汛账》前三章复盘为**14袋干粮、6袋湿粮、12袋未到承诺、3两现银、旧工钱结清、8两船费未付、河东户数未核**的可续写状态。
6. `scripts/build_handoff.py` 把SKILL、最新正文、当前账和下一章冲突组为一个**显式**新聊天载荷。生成文件可以直接粘贴至普通新聊天，但**没有证明已经自动安装或真的在新聊天测试成功**。

## 快速复核

在仓库根目录执行：

```bash
python3 -m unittest discover -s skills/v13-novel-alpha/tests -p 'test_*.py' -v
python3 skills/v13-novel-alpha/scripts/validate_state.py skills/v13-novel-alpha/fixtures/chaoxun_ch03.json
python3 skills/v13-novel-alpha/scripts/build_handoff.py --out /tmp/V13_EXPLICIT_HANDOFF.md
```

测试将**故意注入非法情形**：没有授权就开粮、开5袋超4袋许可、现款超支、只抹债不支付、把未经证实17户直接写成已确认、把未来承诺当实物、重复事件、越时间许可；应当被拒绝。未通过的负例保留为测试，不靠自评加分。

## 限制（必须保留）

本包只验证功能契约和可重放状态，不能认证文学趣味与历史制度史实。不是仓颉Stage2已晋级能力卡，不是女娲Phase3正式主题SKILL，缺少真正独立V3/Phase4/Phase5和四臂盲审、以及干净宿主加载实测；V13正式游标仍是W01 BLOCKED。不得以此ALPHA包替换源SKILL原版阶段或原20个独立Stage0 C任务。

## CH04增量功能回归（仍未独立验收）

新增第四章[原文](../../experiments/novel_field_test_20261012/CH04.md)、[事件账](fixtures/chaoxun_ch04.json)和[专门反例测试](tests/test_ch04_integrity.py)：同号异日两张单据、各方保留原件、留字面回执但不把索款变成已付款；修复收据转存数量守恒、授权记录类型与未知许可引用。前三章冻结资产值没有改写。

## 新聊天交接的补强

显式载荷现在默认选择CH04及其6事件状态账，并在B2区包含可被重新JSON解析和机器复核的**完整事件源状态**（授权生效范围、逐项变动、人物、事实、待偿义务），而非只交余额摘要。可运行 `python3 skills/v13-novel-alpha/scripts/build_handoff.py --out /tmp/V13_EXPLICIT_HANDOFF.md` 检查。这个交接能力是**可移植上下文文本生成**，并未证明另一个干净宿主会自动安装SKILL或在真实新会话成功。
