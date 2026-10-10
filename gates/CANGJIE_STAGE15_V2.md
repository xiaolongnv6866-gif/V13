# V13.2 B076｜Cangjie Stage1.5 V2分流及用户强制确认

status: BLOCKED_ZERO_VERIFIED_APPROVAL_A_RECORDED
batch: B076
legacy: R078
cangjie_pin: a28de55ba881b9928956a55048f743f7a9e3b23e
nuwa_pin: fe0374687037c4cc51a65c1e0c145afe2981dc69
authority_before_commit: 7938fd9160350f88fb11be1e2c1a69f7bca273ba
original_47_freeze: 4e24d782632210c1e1637eba4954bde3d8f3846f
extra_WM_freeze: a62d1ade7017fca01e405edbcb93368489c9122f
extra_TX_freeze: b44928f5728e771127dacdeefb0ad61a12ad8c28
independent_verified: 0
skill_certified: 0
independent_creative_C: NOT_RUN
heldout: SEALED_NOT_RUN
user_confirmation: APPROVED_A_2026_10_10_PLANNING_ONLY

## 一、按唯一候选ID重新聚合，绝不重复计数

| 书 | R057独立候选 | verified | reference | needs_review | rejected | 原R042历史隔离另计 |
|---|---:|---:|---:|---:|---:|---:|
| 晚明 | 91 | 0 | 42 | 49 | 0 | 7 |
| 铁血残明 | 96 | 0 | 48 | 48 | 0 | 7 |
| 合计 | **187** | **0** | **90** | **97** | **0** | **14** |

B068–B072 original47, B073 WM额外10, B074 TX额外12的候选ID全部是原R057那187项中的子集，**没有新增22个独立候选**；只新增V3诊断证据。原187中的97条needs_review现可具体分为69个V1窄/纸面V2及同Agent非盲双臂V3但不独立verified，另28个仍存在V1来源证据/因果边界，暂不能进V2、V3有效方法门。原V1 REVIEW 39条中11条已在R063/64缩为PASS_NARROW，但未自动使其V3有效。

真实诊断69项共138臂，50项同分，19项自评方法组+1，无一达到预注册delta>=2；真实独立评审、干净受试者隔离、独立原创C均缺。原R056旧负面WM-04及WM-09两题仍负向，不由新分数抵消。R042旧隔离14项始终不能直接升级。

## 二、实际交付、Stage3未来材料与覆盖

原R078合同所需四分流分书实物全部应保留：`books/wanming/`、`books/tiexuecanming/`各自`verified.md`、`references.md`、`needs-review.md`、`rejected/README.md`、`coverage-audit.md`；每条当前决策和旧证据状态分别见两书`R078_V2_DECISION_MATRIX.tsv`。其中现今真正在references.md已有的参考90项：晚明42条（12案例、12反例、18术语）；铁血48条（15案例、13反例、20术语）。Stage3计划：案例/反例归`.cangjie/capabilities/book/overview.md`，术语归`book/glossary.md`，**明确标PLANNED_ONLY**。因无verified不得编译或假称Stage3实际已生成。

原R057 19个任务（WM9/TX10）在69个已测试候选中19/19有至少一关联，但并非19项任务完整写作试验通过。更早两书Adler原Stage0任务合计20（WM-T01..T10及TX-T01..T10），与正式19任务并非同一标识体系；`gates/R078_STAGE0_ORIGINAL20_TO_R057_19_CROSSWALK.tsv`逐旧ID保存主题关联及任务差异，尤其WM-T05命令层级理解、WM-T09跨卷连续性不可偷换为已验收。完整Stage0独立C验收0，192条B文学原审计债仍待个别核验。任务真实材料见`v2/v3/B075_STAGE0_19_COVERAGE_AUDIT.tsv`。

## 三、原版Cangjie/Nuwa限制与禁止越门

Cangjie pinned `methodology/03-stage1.5-triple-verify.md` 规定：verified须V1来源、V2可执行、V3任务效用**全部**通过；无verified则交付参考和缺口、停止编译。原Nuwa pinned SKILL Phase1.5、2.5、4、5各检查点、真正子Agent验证和两主体精炼也不能被假扮同一Agent取代。结构CI只审核账本和Git原始输出存在，不构成专业文学鉴定。

## 四、本轮用户确认已收到，不代表三重验证通过

用户于2026-10-10在本聊天明确批准B076方案A，核准187项四分类与全部现有欠证，允许仅在B076内部规划真实独立V3补证、28项V1来源修复和原Stage0完整任务映射。正式确认及权限限制：`gates/R078_USER_APPROVAL_A_20261010.md`；可逐项复核的计划见`gates/B076_APPROVED_A_EVIDENCE_PROTOCOL.md`及三份具体队列TSV。

原R078强制用户选择要求现**已满足**，先前的“等待用户确认”仅为历史进程。但B076仍`BLOCKED`，因为真正独立效用verified=0，正式Stage1.6或编译必须遵守仓颉零verified停止规则。原47及额外22项非盲诊断无独立增益认证；无独立作者、盲评者时不得冒充完成测试。早期Stage0二十原任务及旧14隔离持续保留，独立C=NOT_RUN，SKILL=0。

下一轮不是B077。需在B076范围内先取得真实独立主体/证据条件并重新完成可信V1/V2/V3验证；若无法获得该条件，继续阻断，不为了管理进度强行认定PASS。
