# V13 R046｜《晚明》Stage1反例提取器：独立核查与质量审计

status: RAW_COUNTEREXAMPLES_UNVERIFIED
date: 2026-10-09
source_epub_sha256: a8f3b43dcd496822cd384ac8e9aa85f7dc374f8430f06c6f8321c26825093082
cangjie_pinned_sha: a28de55ba881b9928956a55048f743f7a9e3b23e
nuwa_pinned_sha: fe0374687037c4cc51a65c1e0c145afe2981dc69
input_overview: books/wanming/BOOK_OVERVIEW.md (R042 explicit user approval)
extractor: extractors/counter-example-extractor.md
methodology: methodology/02-stage1-parallel-extract.md

## 一、真实输入与边界

本轮核对了GitHub authoritative R046 NOT_STARTED、45/89、R045 PASSED；全文阅读了仓颉原版Stage1提取方法及该反例提取器prompt，保留原版职责而未偷换成框架/案例/原则。并读取Stage0质量债台账与14个具体旧claim隔离列表。无Task并行环境，依原版串行隔离后备流程只执行**反例提取器**，R047术语提取尚未开始。

使用用户提供的私有《晚明》原始EPUB，重新校验完整SHA256和ZIP CRC；遵从R002冻结OPF映射读取571个真实叙事章，正文总计30,221非空段、2,245,824字符。对全书章节的反向信号（以为、错误、无奈、出错、反对、不够、漏洞、失算等）做检索式多路召回，并复用前一轮**私有**848个基于原XHTML章节的源块和SQLite FTS5中文索引，扩大至邻接段与必要时整章复核。本轮未声称重新执行原版索引脚本，而是重用上轮已如实声明的兼容索引；并对选中20个有效叙事章的现场因果进行独立再核。程序扫到一处用词不是文学解释的验证。

产生**19个ce01—ce19候选**（按六大原著叙事阶段覆盖），公开保存**62个n/p段落SHA**与**21个私人检索块定位**（其中ce17跨n519和n520三块）。所有62个paragraph SHA来自此次读取的原私有EPUB实际非空段UTF-8文本，不由模型臆造，不上传原书段落。冻结chapter sha、XHTML路径、段落数量由R002元数据在公开Actions里进行结构对照；A的原书SHA与正文哈希仅是来源核查，不能证明解释正确。

## 二、体裁适配：反例身份必须分层

仓颉原版提取器希望识别“作者明确警告/反对”的错误与实际失败；然而本书是虚构长篇：主角、配角和叙述者说出的事不等于作者本人认可。因此每条明示`evidence_kind`及`missing_conditions`。

- **OBSERVED类**：确有现场争议或局部不利后果，如n080群体失序造成耗时、n305预算提出反证后的妥协、n506目击数被要求澄清、n519/520普通成员作出不同判断。这并不自动认证原因解释或后续终局。
- **ANTICIPATED/CHARACTER类**：人物担忧某项方案的副作用或当场拒绝选项，如n061不选择排除带家属应聘者、n064原委派方案不被接受、n380渠道垄断可能妨碍创新、n494新安排可能引起群体不满。**尚未发生的潜在风险不能伪造成已经失败。**
- **NARRATOR_HISTORICAL_CLAIM_UNVERIFIED**：n155的行政裁撤与后世后果为原书叙事断言，外部史学真伪尚未验证；即便文内说法成立，也不能据此认定真实历史因果已经核实。
- **SOURCE_SCOPED_ETHICAL_INFERENCE**：n265中权力者以公益语言要求办理个人控制资源的手续；原文可确认实际说法与官员压力，但未见实际原权利人审查，不能变为可实施的社会控制或法律规避方法。
- **PARTIAL_SUCCESS**：n339有有限援助、n437某构想确实被否决、n520试点有有限许可；原著既有实际动作不能因研究者需要“失败例子”而被删掉或颠倒成完全无效。

原版反例字段`failure_mode`、`mechanism`、`warning_signs`、`bound_to`均逐条填写，每一来源按原版`source_chapter`与`source_quote`字段保留；版权小说原文不在公开仓库粘贴，故`source_quote: ""`且加不可逆`source_loci`/SHA。原版引用门在Stage1.5 V1须通过实际私有文本核验，不能把公开SHA当引用充分性。

## 三、19条具体负面机制候选

|编号|源章节|已观察到/未证的事情|重点限制|
|---|---|---|---|
|ce01|010|求职者真实账目技能与宣称不符|现代优势不代表当地资格|
|ce02|061|排斥有家属者的建议未被采纳|组织方便不等于受影响者权益|
|ce03|064|授权对象选择遇到既有员工关系阻力|名义委派不等于同意|
|ce04|080|群体协调失序并耗费时间|头衔不等于执行力|
|ce05|085|功劳分配口径互相抵触|表功不是公允|
|ce06|099|经营对单一合作者依赖显露|有人回来不等于渠道安全|
|ce07|140|“先紧急”说法与信息不完整并存|人物口号不是普遍排序|
|ce08|155|纸面裁撤后果为叙述性历史推断|未经史实外证|
|ce09|265|公益说辞与资源控制、被迫服从不一致|正当性口号不等于权利人同意|
|ce10|305|双重许诺资金与预算冲突|暂时妥协不等于后续履约|
|ce11|339|家庭期望与个体教育意愿落差|部分救助≠结构性解决|
|ce12|380|角色担心垄断使竞争与创新停滞|担忧非已失败|
|ce13|425|基层投诉和分权难题|监督缺口未因提新部门自动修复|
|ce14|437|新技术建议被否决|想法非成果，避免危险操作细节|
|ce15|494|组织安置方案可能挤压个人生活|收益测算不等于个人同意|
|ce16|506|目击规模用词夸张被现场纠正|叙述信息不能超越见闻|
|ce17|519—520|独立参加者持不同伦理判断、试点仅暂准|制度程序不保证意见统一|
|ce18|529|频繁改变需求引起部门排期冲突|口头变更有时间代价|
|ce19|571|听众偏好试图重塑多主体历史|受众喜好不是已证事实|

WM-01—WM-09九项Stage0独立任务均有关联，但这是“反例候选覆盖”，并非九项原创写作能力已验证。部分段落与旧R007—R024发现重合，只有本轮重新定位源场景后方可有待证资格；R042的14条历史问题claim继续`NO_DIRECT_PROMOTION_RECONSTRUCT_FROM_SOURCE`，未审老论断仍B PROVISIONAL。

## 四、R046验收及未来限制

本轮输出`books/wanming/candidates/counter-examples.md`、`COUNTEREXAMPLE_EVIDENCE.tsv`、`R046_PRIVATE_SOURCE_SHA.tsv`、`COUNTEREXAMPLE_CHUNKS.tsv`和本审计报告；`scripts/validate_r046_counterexample_extractor.py`及对应GitHub Actions须验证19候选、62段、21块、20章、六段与九任务映射、旧质量债不解除，且`CURRENT_ROUND.json`/ledger必须只到下一游标`R047 NOT_STARTED`。Github Actions仅能检验源结构和状态契约，不能核验本地私有EPUB明文或作者真实意图。

A私有来源认证；B文学解释仍`PROVISIONAL`，Stage1.5/1.6未进行；C原创新输入任务`NOT_RUN`；已认证SKILL=0；heldout=`SEALED_NOT_RUN`；Nuwa Phase1未开始，旧质量债`OPEN_QUARANTINED`。本轮成功提交CI并远程回读后，才有资格正式标R046 PASSED/46轮；R047必须另一次用户“继续”启动。

## R046首轮CI结果与技术修订

首次正式提交`2fc258254271c2b0b7265b24b5735d9be6a133c5`的R046专项工作流run`37947878890`失败，因为本审计虽用中文说明公开CI不验证私有原著文学解释，但缺少统一的机器标记`SOURCE_STRUCTURE_ONLY`；验证脚本因此正确拒绝。**修订不改变19个候选、62个哈希、21个来源块、20个有效章节或旧质量债门槛**，只补足与本项目A/B/C分门一致的声明：`CI_CLASSIFICATION: SOURCE_STRUCTURE_ONLY`；文学B仍PROVISIONAL、原创C仍NOT_RUN。正式修订提交须重新运行全部Actions并远程回读后才称R046 PASSED。
