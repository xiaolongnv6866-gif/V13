# R047｜《晚明》Stage1原版Glossary Extractor：来源、定义归属与覆盖审计

status: RAW_GLOSSARY_B_PROVISIONAL
date: 2026-10-09
cangjie_pin: a28de55ba881b9928956a55048f743f7a9e3b23e
nuwa_pin: fe0374687037c4cc51a65c1e0c145afe2981dc69
private_source: user-uploaded original Wanming EPUB
original_source_sha256: a8f3b43dcd496822cd384ac8e9aa85f7dc374f8430f06c6f8321c26825093082
input_global_anchor: books/wanming/BOOK_OVERVIEW.md (Stage0 user-approved with legacy debts)
upstream_prompts: SKILL.md / methodology/00-overview.md / methodology/02-stage1-parallel-extract.md / extractors/glossary-extractor.md
intended_output: books/wanming/candidates/glossary.md (reference vocabulary, not stand-alone executable Skill)

## 一、真实原文范围、定位与检索

使用用户私有EPUB，全文SHA256匹配冻结版本，ZIP CRC无损坏；重用R045原始EPUB按OPF筛出的571有效叙事章，私有原始XHTML每章SHA均重新核对匹配，正文**30,221个非空段落，共2,245,824个Unicode字符**。源书全文仍在用户私有工作区；GitHub不托管版权小说。

依原版glossary-extractor的局部检索路径，先以R042用户确认的整书概念清单及原书自然章节作为全局锚点，用确定性脚本扫描571章精确子串词频，记录每词总出现次数与实际出现章节数（见`GLOSSARY_CENSUS.tsv`）；复用R045已存在私有的**848个章节边界检索块/SQLite FTS5索引**做定向召回，回读词项所在的完整原文段落与上下文，按检索缺口扩大窗口。

本轮**并未冒称调用原版scripts/build_chunks.py或build_index.py**：上游对应脚本针对Markdown/TXT输入，此处重用前轮已公开说明的EPUB兼容块与FTS5索引；若未来需要与原版索引契约逐字段匹配，Stage1.5单独对照检查。当前环境也不支持五个并行Task子代理，按上游允许的**干净隔离串行**仅执行第五个、glossary extractor，不把R043—R046候选当作本轮的语义答案。

候选**18个g01—g18**（原版推荐5—20），每个实际词形在用户原书出现次数均不少于3次，并在本轮回核**至少两处语境**；合计36处术语与章节锚点引用，去重后**34个不同的n/p段落位置，分布27个有效章节**。位置及实际段落UTF-8 SHA256见`GLOSSARY_EVIDENCE.tsv`，还附冻结R002的原始章节XHTML路径和byte SHA256。公开GitHub CI可检测结构/引用/字段关系，**无法复算私有EPUB正文SHA或独立文学判断**，统一状态`CI_CLASSIFICATION: SOURCE_STRUCTURE_ONLY`。

## 二、术语归属和不造“作者定义”

上游Glossary Extractor要求`author_definition`、`key_distinction`和`why_it_matters`。本书是小说，不是作者专门著述管理学或军制词典；多数术语没有出现“作者明言：定义为……”的形式化段落。因此18条保留原字段`author_definition: ""`，并明示`definition_status: SOURCE_CONTEXT_PARAPHRASE_NOT_EXPLICIT_AUTHOR_DEFINITION`；实际可观察义写`textual_usage`，与普通误用的分歧写`key_distinction`，后续概念歧义的价值写`why_it_matters`。**不能把研究者自己推断的概念释义冒充柯山梦本人的文字。**

术语分为四类并保留时空边界：
1. **历史名词在故事里的用法**：卫所、军户、牙行、塘报等。小说人物如何理解和使用可观察，但实际明代制度的细节须有独立历史一手史料才能通过外部史实门。
2. **故事组织的命名与阶段变化**：文登营、登州镇、屯堡、屯长、商社、民事部等。组织名称不是组织已拥有的人、钱、命令执行力和正当性的证明，更不能直接把小说组织设计拿到现实使用。
3. **人物资源、认可和时间的词义**：官身、军功、军饷、工坊、试点等。官方承诺/人物期望、实际决策/兑现必须分开；小说中的钱数不能当通用公式。
4. **不同主体知道和再讲述的事实来源**：陪审、情报、评书；也包括塘报。旁观、报告、角色估计和转述互不等价，故事中的有限审判实验不构成真实法律指导。

特别不收“叙述权”“合法性差分”“长期资源债”等**研究者分析标签**，因为没有足够根据宣称是原书词汇；可留待Stage3参考层判断而不能污染作者术语表。18条涵盖六个叙事大段，WM-01至WM-09均有源概念关联，但**这个9/9只是RAW词典候选关联，不是原创任务增益或已经编译的独立技能**。

## 三、精确子串检索的局限与反向质询

- `GLOSSARY_CENSUS.tsv`计量的是每个词形在所有571章节非空段落中的**直接子串总次数**与章数，不是经人工分词或歧义消除后的概念使用次数。例如“情报”在不同角色/叙述者的语境可能有不同可靠度；“文登营”与“登州镇”也可能在同一段出现。
- 因原版词典质量重在**区分普通词的特别用法**，本轮不按词频排名收录“官、兵、钱、民”等普通字词；也没有把每个历史地名、器具和具体人物专名都堆成词典。
- 人物对于“卫所”“军户”“陪审”等词的理解可能混杂穿越者所知、官场传言与虚构制度安排；若要写真实史实，需在Stage1.5查真正历史档案，不得将小说释义直接升格。
- 与R042证据债务的连接：14条旧有误用/过强文学主张仍`NO_DIRECT_PROMOTION_RECONSTRUCT_FROM_SOURCE`，本轮的词频与哈希不能回头“自动修复”旧错引。B全部`PROVISIONAL`，不得进入verified.yaml/最终SKILL。

## 四、下游使用与验收边界

Stage1词典只会为未来Stage3共享Glossary提供原始材料；**本轮绝不提前生成正式GLOSSARY.md、Capability Bundle、SKILL.md或编译产物**。五种Wanming候选（framework, principle, case, counterexample, glossary）至此依固定计划分五轮独立提取完原始稿，**原版的Stage1.5三重验证尚未启动**；R048开始的《铁血残明》是另一阶段的新轮次，不允许本轮执行。

A：私有源文件/路径/段落SHA已核对，GitHub public SOURCE_STRUCTURE_ONLY。B：解释仍PROVISIONAL。C：NOT_RUN，heldout SEALED_NOT_RUN，已认证SKILL=0。legacy_quality_debt_status OPEN_QUARANTINED。冻结控制器必须以一次原子提交同步`CURRENT_ROUND.json`、`ROUND_LEDGER.csv`、`PROGRESS.md`、`books/wanming/PIPELINE_STATE.md`、候选和本审计，GitHub Actions与远程回读全部通过才可宣布R047 PASSED，进度47/89且R048 NOT_STARTED。
