# R045｜《晚明》原版Cangjie案例提取器独立执行审计

status: STAGE1_RAW_CASE_CANDIDATES_B_PROVISIONAL
date: 2026-10-09
cangjie_pin: a28de55ba881b9928956a55048f743f7a9e3b23e
nuwa_pin: fe0374687037c4cc51a65c1e0c145afe2981dc69
private_epub_sha256: a8f3b43dcd496822cd384ac8e9aa85f7dc374f8430f06c6f8321c26825093082
source_book: 柯山梦《晚明》，用户私有EPUB
independent_source_anchor: books/wanming/BOOK_OVERVIEW.md（R042用户已批准）
upstream_method: methodology/02-stage1-parallel-extract.md
upstream_extractor: extractors/case-extractor.md

## 一、真实输入与章节检索流程

1. 独立从源文件按EPUB OPF/R002冻结编号解析571个有效叙事章节，校验源文件SHA和ZIP CRC为PASS。真实正文共30,221非空段、2,245,824字符；剔除13个非叙事Chapter XHTML条目，不通过相邻数字盲猜位置。
2. 源文件留在私有环境，将真实章节按小于4,000个字符的连续正文段落分为**848个有稳定chunk_id的自然章节块**；建立SQLite FTS5 bigram中文私有全文索引`/mnt/data/V13_R045_private/case_index.sqlite`并保留本地私有章节映射。此处是与原版`build_chunks.py`和`build_index.py`匹配的自建确定性索引**兼容实现**，**没有冒称运行上游原脚本，也未上传版权全文**；本轮没有假定此前已有官方`.cangjie/index/`。
3. 做了多轮检索，包括职业工作、信任争议、账册收支、家属、商人、规则争执、试点和说书等来源线索；并从阶段0九项独立任务的原文位置定向取邻接块，证据不足时扩大为章节全文核读。按叙事弧选出**14个源内确有行动/决定/结果可区分**的虚构场景；不是按R043/R044既有候选“改写”；六段均有场景。
4. 公开只保存`CASE_CHUNK_MANIFEST.tsv`中17个已用chunk_id（分布16章）以及`CASE_EVIDENCE.tsv`中的**45个去重实际n/p锚点**（其中16处本次额外私有全文段落SHA复核），每处还包含R002原始XHTML路径及chapter SHA。私有索引848块不公开正文和原始chunk文本。
5. R045真正有重点场景的**章节邻接阅读**，没有声称本轮逐句完成571章的文学B认证。高频语汇和原始哈希只负责召回与来源追踪，场面之内不同角色口径、未兑现的结果仍需独立解释审计。

## 二、原版案例类型与小说体裁冲突：明确隔离而非造假

上游Case Extractor定义的示例类型是`firsthand`（作者亲历）、`reported_case`（作者转述真实案例）、`worked_example`（作者给出的演算/模拟示例）。本书是**长篇虚构小说**，其中所写人物遭遇不能归到其中任何一个真实事件类型。为同时遵守“来源真实、类型诚实”和“不凭空制造已认证案例”，本轮候选记录`type: case`并另加**`example_kind: fictional_narrative_case`**、`source_reality: FICTIONAL_NOVEL_SCENE_NOT_HISTORICAL_EVIDENCE`与`example_kind_extension_status: REQUIRES_STAGE1_5_REVIEW`。

**这不是原版枚举值，不伪称已完全通过上游最终case schema**；其是否可在原创小说SKILL的Stage2 A1使用，必须在Stage1.5按原版来源/用途/任务增益三重门另做合法性与产品价值决定。倘若后续原版对该扩展不认可，将其导流到`references.md`或`needs-review.md`，不能为了凑数重命名为“作者亲历”“历史真例”或演算例题。

版权和来源：遵照原版`source_quote`字段但**公开仓库留空**，以私有原文n/p SHA和自己的场景非逐字总结替代，明确需要今后V1原文复核。小说虚构世界不代替真实历史或现实制度证据。

## 三、14条候选的场面结果和差异

|编号|来源有效章|当场类型|最关键的未证边界|
|---|---|---|---|
|c01|n010|谋生求职尝试|师徒接触不是聘用完成|
|c02|n034|收益争议与合作分歧|有人收钱不等于所有人接受同一伦理|
|c03|n065|店铺负责人交接|任命已宣布，内部分工后果尚待发生|
|c04|n085|不同贡献口径争执|各方说辞不自动产生公平结算|
|c05|n099|合作伙伴安危与供应担忧|暂时见到人不等于长期供货稳固|
|c06|n143|提议被正式否决|当场退让不等于后续执行全成|
|c07|n265|权力话语与地方人实际顾虑|强制下的承诺不能当合法权利证明|
|c08|n305|预算争执后缩减提案|暂时妥协不等于长期账目闭合|
|c09|n339|家庭意愿与教育救助|一次援助不解决制度或长期生活问题|
|c10|n425|基层管理调查与制度权责协商|部分查处有效，新权限仍未谈妥|
|c11|n437|新方案被否定与交易分工变化|新流程宣布不等于实施已成功|
|c12|n519—n520|司法参与者意外观点与复盘|观点不同非现实法律定论；试点有限|
|c13|n540、n569|私人选择跨章变化|不能把追求荣誉解释为获得他人同意的合理途径|
|c14|n571|说书与听众争议|面向观众的版本不自动取消已发生场面|

严格区分小说内现场事实、人物声称、研究者分析以及外部历史事实。各种成就、政治权力及危险行为均不转写成现实实施指引；没有复制原书专属事件链作为小说原创情节模板。

## 四、Stage0任务覆盖、旧质量债与独立性

按用户已确认的WM-01—WM-09关键任务分别找到了具名场景候选，因此**源材料候选级映射9/9**；这不是V1验证通过率，也不是新的写作能力9/9。原版覆盖分母仍为Stage0任务表，不能改用已认证项给自己算覆盖率。

R042所登记14条问题旧claim仍全部NO_DIRECT_PROMOTION_RECONSTRUCT_FROM_SOURCE，尤其n143旧R013 p29入座位置不再作为实际裁决证据，使用n143 p49/52/55的真实场景；n305只是阶段预算妥协。早期其他旧候选B_PROVISIONAL_UNTIL_SOURCE_CHECK。

本轮由无法并行sub-agent的环境按原版允许方式做**独立串行case职责**。未打开框架与原则候选作为这一轮的源事实，不重复计算为独立实验；R046反例和R047术语未开始。三重验证Stage1.5未开始；Nuwa Phase1未开始，C陌生原创效用NOT_RUN、密封测试SEALED_NOT_RUN，已认证技能0。

## 五、正式验收条件

- 候选产物`books/wanming/candidates/cases.md`包含14条原始YAML候选，每条按原版有ID、source_chapter、source_quote、summary、bound_to、outcome、tags及本项目task_ids，另有源案例类型保留、chunk_id和未证限制；
- `CASE_EVIDENCE.tsv`真实45条不同段落SHA，`R045_NEW_SOURCE_LOCI.tsv`16条本轮重核位置，`CASE_CHUNK_MANIFEST.tsv`17块、14个候选、16有效章范围，须与R002元数据一致；
- 自动脚本`scripts/validate_r045_case_extractor.py`必须对上述结果和旧质量债做SOURCE_STRUCTURE_ONLY回归检查，新Actions工作流与原冻结controller均需成功；
- R045若完成为**PASSED 45/89**，游标R046`NOT_STARTED`；本轮只在GitHub提交和远程回读成功后才报告完成。**B仍PROVISIONAL、C仍NOT_RUN、Skill0**。
