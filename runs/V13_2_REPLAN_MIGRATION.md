# V13.2｜44项剩余旧合同合并为30批次的正式迁移收据

migration_date: 2026-10-10
authority: User explicitly approved replan and requested migration plus new-chat prompt
legacy_before: v13.1 66/110 R066 PASSED R067 NOT_STARTED
new_management_plan: 66 historical completed + 30 new batches = 96 units
new_cursor: V13_CURRENT_V3.json | B067 NOT_STARTED
historical_v13_1_state: V13_CURRENT_V2.json (66/110 unchanged)
old_full_contract_blob_sha1: 55256653a7f9359339a5f7a8924e4210ee25203a
old_v13_1_cursor_blob_sha1: 0b782d604a2217fcc5e1c73a69e4108373e4fe42
old_v13_1_ledger_blob_sha1: 3c5e7a34e752e45a089de926cd7280256e554bdc
cangjie_pin: a28de55ba881b9928956a55048f743f7a9e3b23e
nuwa_pin: fe0374687037c4cc51a65c1e0c145afe2981dc69
skill_certified: 0
v3_completed: 0/47
heldout: SEALED_NOT_RUN

## 迁移实施

经GitHub正式查明用户刚完成的历史执行游标为66/110，main SHA `fe7581b61666b9b4ea455008edfc313c045ff464`；此前R001—R066、两书真实原文来源/质量债、R063—R064旧V1 REVIEW纠偏39条、R065—R066共22条有限非盲纸面V2均留原位置及SHA，不改历史账和原文件。旧110轮原始逐项合同保留全文，不压缩任何实质研究、用户关口或输出。

创建新行政执行计划`V13_V3_BATCH_PLAN.md`，新正式进度`V13_CURRENT_V3.json`、新30批次账`V13_LEDGER_V3.csv`，同时交付`V13_LEGACY_TO_BATCH_V3.tsv`保留原R067—R110 **44/44项旧合同**的原标题、完整必要操作、原有产物、验收标准、硬门及精确批次路由。特别标明旧R069、R072、R073的逐方法跨两批分片及最后批次交付完整旧产物，绝不把旧轮的一部分完成冒充全部。新B067—B096初始全部NOT_STARTED，原44个任务0项被自行宣称提前执行。

`V13_V3_47_METHOD_ALLOCATION_V3.tsv`严格来自历史`gates/R057_REPAIR_V3_47_TEST_QUEUE.tsv`，原WM21+TX26恰好47ID不重不漏：B068=11，B069=10，B070=9，B071=9，B072=8。B067必须先单独冻结47个同题双臂输入/验收合同；B073/B074继续对原先22条V2有限通过方法逐ID做资格及额外V3任务/回退审查，**新增22不是原47的虚增分母**。

原创C的实际独立证明仍未运行，47条新V3单方法双臂输出仍0/47，SKILL0，密封题库SEALED_NOT_RUN。历史14隔离旧claim和192条未逐复查早期B不因本次管理重排而获免除。

原合同真正`MANDATORY_USER_CONFIRM`共6个：R078/R098/R101/R104/R107/R110，对应B076/B087/B088/B090/B093/B096。此前初步合并建议将旧R089/R090误当强制关口，已通过远程原合同查明其状态为NOT_CHECKED并修正，不新增虚假用户审批。B076若0 verified，则严格执行仓颉原版停止晋级/编译的门槛。

执行优化策略只对同批次恢复和提交次数进行优化：缓存SHA可信未变文件、同提交窗口合并研究文档、跨批候选逐ID持证，冻结输入与后续真实输出必须分开提交。当前并未私自关闭现有65项历史Actions；新`scripts/validate_v13_2_batch_migration.py`和`.github/workflows/v13_2_batch_migration.yml`进一步检查44旧合同/47方法/30批次/6用户关口/历史状态不可改。GitHub CI只有结构与一致性意义，不等于文学审稿或方法独立增益。

## 迁移验收门

只有迁移最终HEAD的全部GitHub Actions SUCCESS（新增workflow及既有65项）和远程回读：V3现行游标B067 NOT_STARTED、66/96管理进度、44/44旧合同映射、47/47方法ID分流、V2原历史仍66/110未改，才允许对用户声明正式迁移完成。**本迁移不等于开启B067**；新聊天框仅在用户明确发送“继续”时执行首批预注册，不自动写任何V3输出。
