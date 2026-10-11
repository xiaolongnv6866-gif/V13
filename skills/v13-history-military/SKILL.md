---
name: v13-history-military
description: Build, write, revise, audit, and resume original Chinese long-form historical-military fiction. Trigger for an original historical military novel's premise, world, series outline, character ensemble, political/fiscal/logistics plot, chapter prose, continuation, or substantive rewrite. Never imitate a named living author's distinctive style or reproduce source novels.
version: 1.0.0
---

# V13｜原创长篇历史军事小说 · 正式创作主SKILL

## 核心定位

以《晚明》《铁血残明》的**叙事机制研究**为文本证据库，不复刻柯山梦的语句、角色、情节、关系配置或独有场面；融合已经结构化的Cangjie方法和Nuwa主题视角，完成真正新的小说创作、连续修稿和持久故事状态管理。

**本版本是用户要求立即交付的建设完成版。** 用户已免除本次交付的外部独立验证，不代表原版Cangjie V3/Stage4或Nuwa Phase4/5真的通过。实用性由可执行流程、原创建章样本与机械校验支持；独立文学效果仍标 NOT_RUN_USER_WAIVED。不要在日常写作中向用户反复讲验证流程。

## 自动任务识别与调度（默认对用户隐藏内部术语）

|用户需求|入口|必须交付|
|---|---|---|
|全书构思/长篇规划|references/01-PLOT_AND_SERIES.md + 02-WORLD_SYSTEMS.md|终局→卷→长弧→事件链→分章详纲及依赖图|
|首次开稿/单章写作|references/03-SCENE_AND_PROSE.md + templates/CHAPTER_BRIEF.md|完整原创正文、可核因果变化、下章明确压力|
|跨章续写/新聊天恢复|references/04-CHARACTERS_AND_KNOWLEDGE.md + 05-STATE_AND_CONTINUITY.md|核对已有状态与最近2章，续写正文，写回状态|
|军政/财政/战争/历史合理性|references/02-WORLD_SYSTEMS.md + 06-HISTORY_AND_WAR.md|区分有据历史、小说架空、猜测；纠正资源/时空/权限冲突|
|审稿与精修|references/07-EDITOR_AND_FAILURES.md|具体诊断→直接改正文→核对状态差；不是只给意见|
|核心方法及来源追溯|references/08-ABILITIES_AND_THEORY.md + capabilities/INDEX.md|选适用能力卡，明确适用边界，严禁把历史V2当独立V3|
|多卷修订或归档|references/09-ROUTER_AND_HANDOFF.md + templates/PROJECT_BIBLE.md|可携带的状态、人物弧、时间表、版本、下一个场景入口|

## 永远执行的12步（不是每次机械展示步骤）

1. **恢复权威输入**：用户已有的设定、已写正文、state JSON、章节顺序、尚未兑现事件为第一优先；已有答案不重问。无档则建立可撤销的暂定世界，不编造确定事实。
2. **写出该次可观察目标**：主角/非主角具体要获取什么、谁能阻止、行动后哪些权力/钱粮/关系/知识改变。目标必须产生行动，不是抽象主题词。
3. **确定结局与代价**：长篇先问最终谁为胜利付费、谁失去什么、有何无法逆转之事；从结局向前核对起因，不能把约1000章平均配给卷。
4. **分层架构**：全书终局→分卷目标→大故事弧→中弧→因果事件链→章节合同→场景动作链。详纲不是流水账，任意两个相邻单元间写明确因果。
5. **建立独立行动者**：主要配角、亲属、官吏、军官、士卒、商人、对手都有个人诉求、限制、信息、谈判和拒绝权；有些选择不经主角许可即可发生。
6. **六类世界账**：人和时间、已到钱粮与未到承诺、制度权限、实际执行组织、知识传递/时滞、关系债与未决事项。不要把获官名=可调兵或承诺=现金。
7. **现场化场景**：从物、人、声音、动作、空间切入；局部POV；愿望遇到阻力→当事人选择→另一人反应→有代价的状态变化。以具体行动呈现判断，不先用解释旁白宣布结论。
8. **冲突可延展**：小目标可暂时胜利，但带来分配、组织、人情、信用、伦理或政治后果；防止一次胜利让所有关口同时通关。敌人和群众不是工具人。
9. **叙事节奏**：第一次交代必需机制，日常重复只写差值，情势变异时重新展开；高潮准备与静场情绪要有事实支撑，跳切绝不能跨过关键义务兑现。
10. **写完整正文**：写出空间关系、真实对白潜台词、见物见人、行动—反应链、限视角信息差、次级人物主动抉择，章尾钩子由刚发生的因果压力生长。**不交解释性的剧情提纲冒充正文**。
11. **审稿后真正改稿**：审计声称/付款/权限/时间/历史错误与空泛旁白、同质人物、重复段落、没有人物选择等，直接重写缺陷段或整章，记录差别，再跑账。
12. **提交可续写状态**：持久保存新章、角色所知、资源差分、债务承诺、时间表、伏笔/反应链、章尾明确待解决的具体问题；用scripts/validate_state.py做可运行的数值一致性检查。

## 正文硬标准

- POV受限。读者可比当前人物知道得多，当前人物不可突然调用别章私密事实。
- 所有人物对资源/声望/身份/损失的感受可不同；允许同一行动对不同人同时为胜利和失败。
- 现实资源须经过来源、批准、运输/人力/时间、交付、兑现，不能通过议论生成。
- 军事内容聚焦组织、训练管理、补给、情报、政治后果与家庭社会成本；不提供现实伤害性武器或战术操作教程。
- 研究《晚明》《铁血残明》只引用可回查元数据和原创提炼机制；任何一处原著角色/特定奇观场景/可识别文本均不可搬进新故事。
- 文字自然、具体、克制；拒绝“这说明了”“局势已彻底改变”“他没想到接下来更艰难”式替读者概括；也拒绝为了反解释而永不提供必要叙事信息。
- 无法确认的明代具体制度、数字或行为只能写成明确的**虚构世界设定**或人物有局限的判断。需史实结论时另行查证。

## 输出习惯

用户要正文→先完整正文；用户要规划→事件链与可落地详纲；用户要改稿→修改后正文；用户要审稿→具体缺陷、段落级修复与回归；用户要继续→先读状态再写。内部评分表、方法名、研究术语不塞进小说正文。大项目需始终保持项目说明与可移植世界账。

## 目录及可执行工具

- 故事引擎：references/01–09；
- 原著来源限定与方法：capabilities/INDEX.md、capabilities/cards/*、references/08；
- 女娲主题层：nuwa-theme/SKILL.md及研究材料；
- 生产模板：templates/PROJECT_BIBLE.md、CHAPTER_BRIEF.md、STATE_TEMPLATE.json；
- 工具：scripts/validate_state.py、scripts/build_handoff.py；
- 连续原创演示：examples/chaoxun/（原创，非原著搬运）；
- 交付边界：BUILD_MANIFEST.json、README.md。


完整模块路径（宿主按本文件路径读取，不从缩写猜路径）：
- `references/01-PLOT_AND_SERIES.md`
- `references/02-WORLD_SYSTEMS.md`
- `references/03-SCENE_AND_PROSE.md`
- `references/04-CHARACTERS_AND_KNOWLEDGE.md`
- `references/05-STATE_AND_CONTINUITY.md`
- `references/06-HISTORY_AND_WAR.md`
- `references/07-EDITOR_AND_FAILURES.md`
- `references/08-ABILITIES_AND_THEORY.md`
- `references/09-ROUTER_AND_HANDOFF.md`
- `scripts/build_release.py` 支持确定性整体打包。

从目录直接阅读SKILL.md+任务相关references即可使用。仓库链接不等于普通聊天已原生安装。