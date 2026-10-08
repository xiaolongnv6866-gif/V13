# V13 R006｜仓颉 Stage0 全文阅读证据合同（冻结版 v1.0）

status: FROZEN_PROTOCOL_NOT_READING
round: R006
plan: V13 固定89轮
source_cangjie: `kangarooking/cangjie-skill@a28de55ba881b9928956a55048f743f7a9e3b23e`
source_nuwa: `alchaincyf/nuwa-skill@fe0374687037c4cc51a65c1e0c145afe2981dc69`
effective_date: 2026-10-09

此合同是V13为历史军事**文学叙事作品**增订的真实性审计规则，不替代原版仓颉 `SKILL.md`、`methodology/00-overview.md`、`methodology/01-stage0-adler.md` 和 `templates/BOOK_OVERVIEW.md.template`。原版Adler四步（结构/解释/批判/应用）及Stage0之后**用户确认BOOK_OVERVIEW**仍为硬门。**R006冻结证据要求，当前正文阅读0/1103、原著机制结论0、通过验证的原创SKILL0**。

## 一、原始材料与唯一章节标识

| book slug | 叙事章节 | OPF spine项 | 完整用户EPUB SHA256 |
|---|---:|---:|---|
| wanming（《晚明》） | 571 | 588 | `a8f3b43dcd496822cd384ac8e9aa85f7dc374f8430f06c6f8321c26825093082` |
| tiexuecanming（《铁血残明》） | 532 | 551 | `9100bbcdb9f52bcd5458cbda92e16b646489efbc00df5161ed568ebac83ffbaf` |

唯一计数键是 `book_slug + narrative_ordinal`，其原始 `epub_path`、`spine_index` 与该ZIP内部文件 `chapter_sha256` 须匹配 `sources/metadata/*_v13_spine.csv`。不可用书内印刷“第N章”作主键：《晚明》按卷重置章号，《铁血残明》标题有重号/回跳，第535章为正文20字符的非叙事占位。卷界、序、年表等非叙事项可研究，但不计入1103个叙事章。不同电子版须先重做R002指纹和映射，不得混入计数。

## 二、四类互不替代的输入接触及计数

**INDEX_ONLY／目录索引**：仅看OPF/spine、标题、字符数、摘要或检索片段；用于定位，不证明正文阅读。记 `index_seen=1`，**full_read=0，close_read=0**。仅运行ZIP CRC/SHA同理。

**STRUCTURAL_SAMPLE／结构抽样**：真正阅读若干不连续段落/场景，或一段但未覆盖本章全部叙事正文。记 `sample_seen=1`，**full_read=0**，不得以样章数量抵全书阅读数量。结构抽样可以产生待验证的假说，不能独立代表作者整部作品机制。

**FULL_TEXT_READ／全章正文实读**：读者/Agent确实逐段接触**这一个**已匹配SHA的叙事章从第一到最后的全部正文，无截断、没略过对话/场景、没把生成式章节摘要当原文；填写可复核的`reading receipt`，给出该章事件链、人物立场、场景/时间位置变化、至少一个可指回原文的定位锚点，以及遗留不确定处。只有记录齐备并通过来源索引校验，才可给`full_read=1`。工具扫描完整文件、程序输出“已读”、只给目录、引用外部摘要、或遗漏原文段落，一律不算。自动检验只能查证记录一致性，**不能单独证明人或模型真正理解了所有段落**，必须有内容性审查；任意伪证可撤销计数。

**CLOSE_READ／重点段落精研**：须先满足 FULL_TEXT_READ，再针对选中场面逐字查看（在私有语料内），分析叙事视角及可见信息、动作—反应链、句法与节奏、对白与潜台词、情绪与读者预期、跨章因果和章节钩子；做`mechanism_claims`的支持证据、反例或失败边界及替代叙法的反事实比较。记 `close_read=1`，也只记**同一章全读一次**。粗略摘标题和单句点评不能叫精研。**不强制每章都精研，也不允许拿重点精研替代全部章节全读。**

单本读量 `FULL_READ_COUNT=|{ordinal: 有效FULL_TEXT_READ或CLOSE_READ收据}|`，去重计数；`SAMPLE_COUNT`、`INDEX_COUNT`、`CLOSE_READ_COUNT`另外统计，**不相加、不回填**。最终 `FULL_READ_COUNT(wanming)=571`、`FULL_READ_COUNT(tiexuecanming)=532` 才可说1103章真正全读；两书Stage0质量门还须单独通过原版Adler四步与用户确认，不能用计数替代文学理解。

## 三、正文收据：来源性A与内容性B分开审计

正式每章收据采用 `tests/contracts/reading-receipt.schema.json` 的JSONL对象、单个章节单次独立记录；保存于后续批次 `cangjie/reading/<round>/<book>_receipts.jsonl`（未来R007—R035实际执行时再建立）。元数据必填 `book_slug, narrative_ordinal, spine_index, epub_path, source_epub_sha256, chapter_sha256, mode, body_paragraph_count, observed_paragraph_count, anchors, event_chain, open_questions, mechanism_claims`。必须由本轮实际私有EPUB恢复源章进行逐段确认，不能从R002元数据CSV直接生成“阅读收据”。

阅读范围：章正文`body`的完整实际内容、包含嵌入对话的非空段落；目录标题、网页碎片、封面、非叙事插图不算。不擅自合并/删去段落；对真实XHTML段落划分与 `body_paragraph_count` 记录实际规则和总数。若实际parser与R002 `nonempty_paragraphs` 差异，应把差异列为核查，不覆盖原数据。**正文实读需要 `observed_paragraph_count==body_paragraph_count` 且个数大于0及原始文件Hash/路径一致；不能只填相等数字冒充全读。**

证据锚点在原文中的 `paragraph_index`（从1起的章内顺序），`paragraph_sha256`（确切原段落按注明的normalize规则计算）和 `locator_note`（仅标位置或自述场景功能，不贴书中原文）。长引用、EPUB正文、受版权保护桥段不得上传GitHub；如锚点证据需对照原句，只在私有本地资料核验。机制性结论至少要有真实支持锚点和反向检验记录（`counterexample_status`为`FOUND`必须有可复核的反例锚点；无发现记`SEARCHED_NONE`则结论只是`PROVISIONAL`而非`VERIFIED`；未查记`NOT_CHECKED`不能进入已验证知识层），也要写**假说可能失效的条件**。反例可来自本章或其他已阅读章节，但必须携同一套原始来源定位，禁止想象“作者总是这样”。

三证据门彼此独立：**A 来源真实性** = EPUB/ZIP/章SHA/内部路径/段落锚点；**B 文学机制解释** = 行动、视角、对白、节奏及其反例与可否证的因果说明；**C 创作效用** = 在陌生原创任务中相对无SKILL基线输出增益。A通过不能声称B通过；B有机制假说不能声称C通过；C自评高分不能代替真实独立评审。

## 四、近景精研字段与反事实对比（按真实材料填写）

在关键章节 `mechanism_claims` 分析：`scene_entry_exit` 进入/退出时机及读者已知信息；`pov_information` 谁能知道/误判什么；`action_reaction` 行为—可见反应—下一动作；`sentence_rhythm` 语长/停顿/重复及改变；`dialogue_subtext` 言语目的、潜台词与权力关系；`emotion_reader` 情绪如何由具体场面而非先行旁白生成；`causal_payoff` 跨章责任、成本、伏笔回收；`chapter_handoff` 结尾悬念与下一章债务；`historical_constraints` 历史/财政/时间/信息及战争空间真实性。

每条机制声明的记录顺序：**自述观察 → 正向段落锚点 → 可检验的作用解释 → 对比“改用另一种叙法会失去什么” → 找反例/例外 → 适用边界 → 置信度 → 原创任务中的候选触发条件**。不得用抽象术语替代对现场的分析、不得推断小说人物行为就是作者私人思维、不以“文学风格像某作者”作为教学目标。首次完整场面展开、常规重复压缩、出现新差值再展开属于**候选研究问题**，不是已从两书证实的规律。

## 五、抽样与跨章研究：先定规则、不事后只挑好例子

R007—R035每轮按固定章区间**全部章节FULL_TEXT_READ**为目标；每轮预留额外精研`CLOSE_READ`：首章、末章、区间中位章（为避免剧情优选）；在读到有重要状态转折时可另增，但在日志注明为何增抽，并以未增抽的章节或对立场景寻找反例。小于3章的批次去重。抽样计划并**不等于所有章节已读**；额外抽样亦不增加全读章数。

阶段性场景卡以故事弧/事件链为单位：起点公开状态、角色不同目标、对抗成本、改变的权力/钱粮/信息/关系状态、随后还清或扩大债务、反向场景。允许跨章压缩笔记，但任何章的收据都必须有独立序号和实际实读事实。就算结构分析相似，也不得复制同一张记录冒充不同章节。分析原著中的军事技术细节时侧重叙事与约束，不能给出现实危险活动的操作手册。

## 六、仓颉原版 Stage0 与分轮门

每部原著完成全读后**分别**生成原版 `BOOK_OVERVIEW.md`：结构3—7一级主题；解释作者的真实关键术语、5—15核心命题（文学作品可将“作者要解决的问题”解释成作品的叙事议题，但必须是有证据的分析，不能装作作者公开自述）；批判立场/前提/局限和最强反对意见；应用潜力及不能技能化的材料；独立“原书关键任务清单”，有 `task_id`、源章证据、真实任务、交付物、重要性及缺口。此处 **目录/摘要无法推断主旨、命题和适用性**。用户将在计划所列R042对整书骨架做强制确认，未确认不得进入后续提取。

## 七、阅读检查失败/恢复

必须拒绝这些“通过”场景：只有标题/章节索引；只读开头/结尾；只运行哈希；仅用生成摘要或旧研究；章内路径或Hash不一致；所填段落数量不足；重复章节号/印刷章号替代ordinal；文学断言无原文锚点；没有查找反例却标`VERIFIED`；未读小说却声称神奇的创作能力增益；小说细节来自V10—V12。遇断连/上下文丢失则保存实际已读章收据和未完成边界，本轮标IN_PROGRESS，不能递增其他chapter counts。除真实通过全部门外不得更改游标。

**本轮合同冻结行为不是实际执行任何一章。R006静态/合成测试仅检查证据系统的判停能力，`full_text_read_chapters`应保持`{wanming:0,tiexuecanming:0}`。**

## 八、章内段落定位的确定性规范

供未来真实私有EPUB验证的归一化 `xhtml_visible_text_trim_whitespace_v1` 定义与R002独立脚本一致：对ZIP内部章节的**原始字节**使用 `lxml.html.fromstring(raw)`，逐项遍历 `doc.xpath('//body//p')`，取每个 `x.text_content().strip()`，剔除空字符串，得到从1编号的章内有字段落；对各段 `s.encode('utf-8')` 求SHA256。它不等于全部阅读语义（`<body>` 的非p标签中可能也有正文，读者仍须接触全部实际章文本）。真实阅读若`lxml`提取异常、段落条目未对齐，应先记失败/待复核，绝不自行用近似计算宣称PASS。

跨章反例需要在锚点的 `source_ref` 完整填写另一本/章的 `book_slug, narrative_ordinal, epub_path, chapter_sha256`，仍应在私有源ZIP验证其文件SHA及位置。公开元数据能核对章节字节SHA，但**无法仅凭GitHub证明段落哈希指向真实语句**；真正可信的来源性A须未来本地提供私有原著，运行 `python3 scripts/validate_r006_protocol.py --receipts FILE.jsonl --source-dir PRIVATE_EPUB_DIR` 执行读取对照；只有不含 `--source-dir` 的校验只能报告`SOURCE_STRUCTURE_ONLY`，不得宣称全章已读。
