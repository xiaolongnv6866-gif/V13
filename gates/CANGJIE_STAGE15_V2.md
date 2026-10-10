# B076新增三项V2原创新题输出（2026-10-10）
冻结SHA：`84f5988e14a5c5b950e27c5d81c6422b280c62c0`，冻结原件blob：`0356af5c12a7987930a62c9562c24d3a3e9892e8`；先冻结并远程验证无输出且76/76CI成功，再创作三份独立原创民事场景及状态账、负例。WM-f15、WM-p09、WM-p17的新题 **3/3 V2_WALKTHROUGH_PASS_LIMITED（同一Agent非独立）**，其3份场景和逐行验收见`tests/b076_v2_3_outputs/`及`gates/B076_V2_3_WALKTHROUGH_REPORT.md`。这不是69项V3独立验证，也不是Stage4或真实盲评；目前 verified=0/reference=108/needs_review=79/rejected=0。B076 BLOCKED 75/96，B077 NOT_STARTED。旧14隔离、192项文学B、原20 Stage0 C均保留。新增CI只审结构且必须保留原总门槛。

---

# 最新B076内部复核（2026-10-10）
通过用户EPUB原文支持的新审核，将旧28项V1来源缺口中的18项案例/反例真实转入两书references.md（WM9/TX9），另外3项只取得限定范围V1 PASS_NARROW（WM-f15/p09/p17），剩7项保持REVIEW。正式分流 **verified0 / reference108 / needs_review79 / rejected0，总187**；早先用户方案A确认的0/90/97/0为修复前基线并保留收据。三项新V1均没有V2实际新题结果和独立V3；全部69个独立V3复制未做。Stage0独立C0、旧隔离14及文学B未审192不清零，SKILL0。B076仍BLOCKED，75/96，B077 NOT_STARTED，零verified不得编译。详情：`gates/B076_V1_REFERENCE_ROUTE_REPORT.md`、`gates/B076_18_SOURCE_ONLY_REFERENCE_ROUTE.tsv`、`gates/B076_V1_NARROW_METHOD_RECORDS.md`。

---

# 2026-10-10｜B076 28项主张缩窄＋Stage0合同缺口实修（最新）
本次对已通过独立本地SHA重算的28/28原文收据（89处/76段/36章）逐ID裁剪。新`gates/B076_V1_28_CLAIM_SCOPE_ADJUDICATION.tsv`分别为窄场景可支持4、不同故事拼接因果仍不足6、仅有可查案例/反例素材18；**正式V1方法PASS新增0、独立V3 0、认证0**，官方187四分类不变。另建20条旧Stage0输出合同差异复核表与WM-T05三级认知、WM-T09跨卷四状态的独立陌生题合同，**仅完成合同复原，未创作和盲评，Stage0独立C仍0/20**。见`gates/B076_V1_28_CLAIM_REPAIR_REPORT.md`和`gates/B076_STAGE0_WM_T05_T09_RESTORED_CONTRACTS.md`。本轮继续B076 BLOCKED，75/96，B077 NOT_STARTED，零verified禁止晋级编译。

---

## B076补证执行状态（最新更新）

2026-10-10：对28个原V1待核候选按两份用户EPUB原始哈希及89次n/p定位执行来源重查，实际36章文件、76个唯一段落；每条限制性结论和段落摘要见`gates/B076_V1_28_ACTUAL_SOURCE_RECHECK.tsv`及`gates/B076_V1_28_SOURCE_RECHECK_REPORT.md`。**这只是来源证据重新核对；28/28的过宽因果/执行主张仍REVIEW，V1新PASS=0。** 69条需要实际独立双臂/盲评的V3仍未执行，原Stage0二十任务完整C未独立验收，verified=0，SKILL0。用户明确选择A已存档，B076继续`BLOCKED`，不得前进B077。原文版权文本不上传GitHub。

---

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
