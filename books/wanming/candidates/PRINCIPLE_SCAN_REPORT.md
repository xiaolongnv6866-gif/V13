# R044｜《晚明》Stage1原则提取器：独立来源扫描与审计
status: RAW_PRINCIPLE_CANDIDATES_NOT_VERIFIED
date: 2026-10-09
upstream_cangjie_sha: a28de55ba881b9928956a55048f743f7a9e3b23e
source_epub_sha256: a8f3b43dcd496822cd384ac8e9aa85f7dc374f8430f06c6f8321c26825093082
overview: books/wanming/BOOK_OVERVIEW.md (R042 approved)

## 1. 实际范围与源性
从用户私有原EPUB经真实OPF spine映射571有效叙事章；剔除Chapter_0001—0008、0060、0115、0166、0283和0500等非叙事条目。逐章解析自然XHTML结构块，扫描所有30,221非空正文段落、2,245,824 Unicode字符，附注出现时同块处理。私有原EPUB SHA匹配冻结版本、ZIP CRC无问题；GitHub仓库不上传原文。
全量扫描的字符输入和关键词命中并不是模型逐句语义审核，也不意味着每章的每个断言得到B验证。以完整源书六段骨架为全局锚，选择可疑场景逐段复查并对照独立人物的相反主张。未用R043 frameworks.md作为本提取器的事实输入。

## 2. 六阶段检索地图（按正文段至少匹配一次的命中数；不是机制成立次数）
|阶段|有效叙事章|条件句式|规则句式|数字和账册词|
|---|---|---:|---:|---:|
|S1|001—051|47|219|26|
|S2|052—105|69|201|46|
|S3|106—155|65|209|37|
|S4|156—271|143|490|71|
|S5|272—487|240|935|121|
|S6|488—571|88|356|24|
这些次数仅用于扩大检索与寻找竞争意见；不能从“必须”的字频推断作者支持角色的道德宣言。

## 3. 原始输出和文学边界
principles.md记录p01—p23共23条独立原始原则/规则/清单候选，任务关联WM-01—WM-09全部可追踪。每条保留原版id/title/type/source_chapter/source_quote/summary/tags/task_ids，另加角色言论与研究者推断的provenance、source_loci、条件/反例/缺口；不做筛选或生成Skill。
PRINCIPLE_EVIDENCE.tsv共39处去重后的n/p原文SHA锚点，来自25个独立有效叙事章节；14个原来未刊入本阶段证据表的源位置在R044_NEW_SOURCE_LOCI.tsv保存私有重算SHA。只有HASH和不逐字转录的场景说明进GitHub，因版权原因source_quote键留空并明确COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA，Stage1.5以后须凭私有原文完成V1。
来源中有真实的角色式规则（例如n140/p30的临时工作排序与n520/p17有限试点），也有研究者拟出的写作检验（例如n305/p29同一资金被多个部门争取）。不把这二者当成作者本人发表的通用管理定律。n425/p40确实列出事务、银子、人事、资产四类，但没有完整表头或统一数字阈值；不能自己补造完整计算公式或审批表。整体未发现可以独立以当前源书核实并安全外推的通用计算规则，此判断不代表全书绝对没有公式。
负面范围：n085/p25及p29是分配争议而非某一种公平算法；n506/p46要求报告不夸大数字而非现实侦察法；n519/p69要求说明理由，p70才展示实际回答；n520/p17仅限试点许可而非全面成功。小说内冲突主张彼此不能无声合并。

## 4. 后续门禁
本环境不能并行启动五个Task subagent，原版允许干净串行替代；本轮只有原则提取器，R043框架已由上轮提交且不替代本轮。R045案例、R046反例、R047术语等尚未执行，不运行Stage1.5、Nuwa Phase1、Skill编译或密封评测。
14条R042旧claim_id继续NO_DIRECT_PROMOTION_RECONSTRUCT_FROM_SOURCE，其余旧候选B_PROVISIONAL_UNTIL_SOURCE_CHECK。A私有真实源SHA可复查/公开CI SOURCE_STRUCTURE_ONLY，B=PROVISIONAL，C=NOT_RUN，技能认证0，质量债OPEN_QUARANTINED。需要本次R044正式GitHub Actions和远程回读通过后才能将轮次设为PASSED，下一R045 NOT_STARTED且必须等待独立用户触发。
