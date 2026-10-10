# B076｜28项V1原文定位复核的真实执行记录

status: SOURCE_ANCHORS_RECHECKED_28_OF_28_V1_NOT_PROMOTED
date: 2026-10-10
batch: B076
authority_commit_before: 4a1fabf25267e01fd1c4215f3cdac1956cc570a7
approval: gates/R078_USER_APPROVAL_A_20261010.md
method: user_supplied_private_EPUB_zip_spine_source_loci_context
source_file_wanming_sha256: a8f3b43dcd496822cd384ac8e9aa85f7dc374f8430f06c6f8321c26825093082
source_file_tiexue_sha256: 9100bbcdb9f52bcd5458cbda92e16b646489efbc00df5161ed568ebac83ffbaf
private_local_28_case_full_tsv_sha256: fb4a5cc409873d2dc533125a1be320cb70568bdef5152c789e37b61abbc6a53a
actual_source_pairs_checked: 89
unique_source_locations: 76
distinct_chapter_documents: 36
candidate_ids_checked: 28
wanming_ids: 18
tiexue_ids: 10
independent_source_reviewer: NONE
V1_new_PASS: 0
V2_new_pass: 0
V3_verified_gain: 0
SKILL_certified: 0

## 一、实际做了什么

原始输入是用户本轮上下文中的两份授权EPUB文件，现场SHA-256与R002项目已登记的原始文件SHA-256完全一致，确实是同一本可审计原文。使用EPUB中的真实章节文件（《晚明》`Chapter_*.xhtml`；《铁血残明》`chapter*.html`），按R057存储的有效叙事章节n/p定位逐段原文，而不是引用抽象摘要、检索结果或通用记忆。读取全部28条缺口原文共89次n/p（重合后76个唯一段落），涉及36个源章节文件；每次校验段落确实存在、计算真实章文件SHA256和非空p段落SHA256，并核查相邻段落供解释边界使用。**不把完整原著文本发布至GitHub**，仅提交原始定位、密码学摘要和受限文学解释。

本轮可核实逐条结果：`gates/B076_V1_28_ACTUAL_SOURCE_RECHECK.tsv`，28个候选各有来源位置、全原文文件哈希、段落组合哈希、已见文学事实的最小范围、未被证明的扩展以及当前V1状态。`gates/B076_APPROVED_A_V1_28_REPAIR_QUEUE.tsv`已同步从`NOT_EXECUTED`更新为`SOURCE_RECHECKED_V1_CAUSAL_SCOPE_STILL_OPEN`，旧R057矩阵保持冻结不改；当前最新仍须以新证据+原决策共同判断。

每一条段落组合摘要计算方式：按队列给出的n/p原顺序，提取对应章节的全部非空`<p>`；每段取`''.join(p.itertext()).strip()`的UTF-8 SHA-256；把`nNNN/pP=完整64位段落SHA256`按顺序用竖线`|`串联后，再对UTF-8字符串取SHA-256。此算法不可被短摘要或同义改写替代。离线复验脚本`scripts/verify_b076_v1_private_epub_receipts.py`需用户原始EPUB作为本地输入，不上传版权原文。

## 二、发现及不能越界之处

《晚明》18项：多个不同叙事现场仅能分别支持人物选择、组织愿景、行政分工争论、供给压力或现实认知限制，不能凭不同时段话语自动证明同一制度、资金、通讯或职责已经形成完整的稳定闭环。尤其`WM-c05/WM-ce06`同一源段是对贸易伙伴可能出意外的担忧和随后确认到达，不是实际发生的持续断供；`WM-ce13`有投诉调查及部分处分，但投诉不等于所有指控已获独立事实认定；`WM-ce15`的领导层讨论不能冒充安置对象实际同意；`WM-ce17`不同价值的场上分歧不等于多年试点已成败；`WM-ce18`修改运输计划可见，累计实付成本仍未证。

《铁血残明》10项：书中存在公共资源备货缺口、上级建议与口头认可、层级命令与信息差、财务预估/花费、任职举报、制度疑问、善后负担等真实可定位场面，但不能合并不同事件当作同一笔连续对账或把预估推断成清算结果。`TX-ce12`举报确曾提出，真伪尚无完成核实；`TX-ce15`层级指挥疑问在场上已被回答，但后续落地仍需独立实证；`TX-ce18`两个相距章节的事件不能直接因果拼接。具体逐ID见TSV，不在本报告重复原著受版权保护语句或危险情节操作。

**本次28/28实际来源定位工作完成，但并不表示28个V1 PASS**：28项仍`REVIEW_SOURCE_RECHECKED_NOT_PASSED`；需要正式将各候选核心主张逐句缩窄并重建可执行输入/输出/反例，再进入有隔离的独立V2/V3。既不能因新证据有场面就自动通过，也不能因超范围解释存在就一律拒绝原素材。当前187项四类总数维持verified0/reference90/needs_review97/rejected0，R042旧14隔离不变。

## 三、独立性和下一关

当前可访问GitHub、原始EPUB、代码执行，但没有可核实的**独立创作者与独立匿名评审实例**。无角色隔离证明不得将主Agent分段、自评或同一聊天框改头换面冒充独立评测。69项V3原冻结结果仍非盲；`gates/B076_APPROVED_A_V3_69_REPLICATION_QUEUE.tsv`保持UNASSIGNED/NOT_RUN。原Stage0完整20任务独立C仍NOT_RUN，B077 NOT_STARTED，禁止编译。结构CI验证本报告的表格、行数、Git对象一致性，**不判定文学质量或真实独立V3收益**。

## 四、验收边界

本次成果是**B076内V1来源复核子任务**，不是R078整个批次PASSED；累计正式完成维持75/96。若用户此后仅输入“继续”，仍从B076真实剩余项出发，不可默认选择一个假独立评审者、不越至B077。后续较优顺序是：逐条校正受限候选实际V1陈述和反例，再取得可证独立测试条件进行冻结后的V2/V3新题；未达零verified停止规则则一直阻断。
