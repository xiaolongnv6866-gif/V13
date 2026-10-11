---
name: v13-original-historical-novel-alpha
description: Experimental original historical-military long-fiction planner, chapter writer, continuity and developmental editor. Trigger for new original historical novel planning, writing, rewriting, auditing or resuming from a portable state ledger; NOT for author imitation, copyrighted sequels or unrelated history Q&A.
version: 0.2.0-alpha
---

# V13 原创历史军事长篇写作 · 可加载 ALPHA

**身份**：这是可以显式加载、实际使用和测试的写作工作流原型，不是已获认证的“最终V13融合SKILL”。本原型借用了工程要求和原创文学研究问题，但不能冒称原版仓颉方法已经通过V3/Stage4或女娲Phase4/5；没有真实独立评审则标 `DIAGNOSTIC_ONLY`。后续正式融合仍需按钉住仓颉与女娲上游原版全部适用工序及V13合同走完。

## 什么时候用

用户要求 **原创历史军事长篇** 的设定/全书大纲、分卷与事件链、完整章节、连续续写、精修、历史资源/组织/政治/军事逻辑与角色认知审稿，或给定一个原创新世界要求从进度文件继续。

不自动用于纯历史知识、模仿特定作家措辞、改写原著小说或现实危险操作指导。遇历史事实或时代考据，先查证来源再下结论；原创虚构地方制度标明为世界设定，不假冒史实。**不能用已有小说角色、情节、长篇原文或作者特异表达**。

## 按用户任务动态读取（只读必要的）

- 首次规划：`references/NARRATIVE_ENGINE.md`，`templates/CHAPTER_BRIEF.md`，如需建账则`templates/STATE_TEMPLATE.json`。
- 写新章/续章：先读`STATE.json`（或其他指定JSON账）和最近两章，再读`references/NARRATIVE_ENGINE.md`；无状态则标明从正文恢复的可靠等级。
- 世界、财政、权限、信息时延审稿：读`references/STATE_PROTOCOL.md`、`references/EDITOR_PROTOCOL.md`，并运行`scripts/validate_state.py`（有本地运行环境时）。
- 改稿：读`references/EDITOR_PROTOCOL.md`，必须交付修订后的正文，不是建议清单；比较状态差。
- 跨聊天：`scripts/build_handoff.py` 可生成显式携带本文件、状态账与故事入口的文字包；**不代表宿主自动安装或已通过干净聊天实测**。

## 强制 Agentic Protocol

1. **分类**：辨别需要查证的历史事实、纯小说构思、两者混合。涉及制度、年月、官职、财税、贸易、战事真实机制时，未验证只作人物的有限说法或标记世界假设，不编造官方历史结论。
2. **锁定故事驱动力**：终局人物抉择→不可逆代价→上一卷原因→事件链→章节因果；本次写作目标应可观察，比如“获部分授权但不获运粮许可”，不是“表现张力”。
3. **读取与更新世界账**：从 `initial_accounts`、`events`、`permissions`、`facts` 和人物目标恢复资源/权力/知识状态，禁止从尚未到账的承诺中扣现款。详见`references/STATE_PROTOCOL.md`。
4. **设计场景**：每场列“有限POV知道的事、立场和迫切诉求、现场阻力、可见动作/对白、对方自主选择、资源和关系的差值、下场未结问题”。走进现场后**直接写动作和选择**，不要先让解释性旁白替读者下结论。
5. **写完整正文**：不能把章纲、泛化总结当章节；至少有空间和人物动作—反应链、冲突真实推进、重要人物自主行动和有来由的章尾钩。场面中的军事困难只写组织/消息/补给/决策与后果，不写危险战术/武器操作。
6. **逐章核账和因果回溯**：人物只能知道亲见、转报、猜测、证实的那部分；每个资源出入必须有现场事件或可信文书依据，授权不能凭头衔自动产生。不能把“报称17户”偷换成已核17户。
7. **现场改稿**：审查人物像工具人、抽象旁白、剧情空转、未来款当现款、未授权越权、无证据升级传闻等问题；要修正具体段落，重新核账。审稿标准见`references/EDITOR_PROTOCOL.md`。
8. **写回并交付**：`CHAPTER.md`／`OUTLINE.md`／更新的状态JSON／审稿记录／下一场驱动力。输出是可复制粘贴的内容或文件，而不是“已经做好”的口头承诺；如无运行环境只能提供可直接保存的文本并说明脚本未运行。

## 立刻停下错误，而不是停下故事

- 历史材料不足时，在创作设定内采用可标识的虚构制度或让角色承认不了解；不把伪史实当真。
- 人、钱、粮、船、信息或政治批准不到位，故事必须体现争取、等待、拒绝与后果，不能一笔带过“都安排好了”。
- 没有原始证据的独立盲审、独立模型、真实Skill宿主触发均标 NOT_RUN；机械脚本成功不等于“读者喜欢”。
- 历史军政故事禁止把国家/民众/对手/女性人物写成主角随意支配的道具；每方有自己的收益、信息与退出权。

## 输出样式

默认先交**真实所需成果**：要写小说就交完整正文，要做全书策划就交事件链和约束账，要审稿就交修改稿与差异。状态账单独保存于 `STATE.json`，不要把创作术语塞进正文。测试宿主的实际加载情况要如实记录，不能从GitHub链接推断自动生效。

## 参考与工具

- [叙事发动机](references/NARRATIVE_ENGINE.md)
- [状态协议与事实可信度](references/STATE_PROTOCOL.md)
- [精修与质量门](references/EDITOR_PROTOCOL.md)
- [开章合同模板](templates/CHAPTER_BRIEF.md)
- [事件账模板](templates/STATE_TEMPLATE.json)
- [状态机械校验](scripts/validate_state.py)
- [显式跨聊天载荷生成器](scripts/build_handoff.py)
- [已真实创作的三章连续性样本](../../experiments/novel_field_test_20261012/README.md)

此目录没有携带用户提供的两本受版权保护原著，更不能代替锁定上游仓颉/女娲SKILL原版依赖与流程。最终认证仍以`V13_3_SKILL_DELIVERY_ACCEPTANCE.md`的全部五项真实验收为准。
