# V13 R056｜两书V3任务增益正式研究审计（拒绝不公平正增益）

status: NO_UNCONFOUNDED_V3_INCREMENTAL_GAIN_PROVEN
date: 2026-10-10
initial_repo_head: 7e763e3133258551761df4b4c24b39f776a02ec2
pinned_cangjie: a28de55ba881b9928956a55048f743f7a9e3b23e
pinned_nuwa: fe0374687037c4cc51a65c1e0c145afe2981dc69
source_epubs: a8f3b43dcd496822cd384ac8e9aa85f7dc374f8430f06c6f8321c26825093082 and 9100bbcdb9f52bcd5458cbda92e16b646489efbc00df5161ed568ebac83ffbaf
source_integrity_A: previous R054 original private hash verified, this round does not claim a new literary source review
literary_B: PROVISIONAL
original_skill_efficacy_C_independent: NOT_RUN
skill_certified_count: 0
heldout: SEALED_NOT_RUN

## 实际对照设计及公平性失败与补救

1. **题目严格相同**：沿R055不可变预注册 `27fa253c133ad892f67f14c6236716835d7c365d` 的19条原创剧情任务，冻结后已有候选组38段场景（提交`597b7caa8051db924ba0125e9e0ee4cf37e6c164`）。R056在原件不变基础上，先冻结五维11分评分规则`c4d97a582e9b2ec13bad55db3ec00211f9cf9399`，后写第一批普通对照38段场景，并初评分。
2. **发现失败条件**：第一批只给普通组故事设定，未给R055候选组已看到的57条具体标准；候选201/209对普通168/209、14胜4平1负。这是**输入合同不一致**导致的混杂，不能计作技能增益。原稿及评分仍存在`tests/v3/baseline/`和`R056_PAIRED_RATINGS.json`，没有删去负面发现。
3. **评分合同不变，先登记纠偏再重新生成**：补充协议先以`79b6a619a8c4577546e272bfad074cf499cdc533`冻结，双方现在都收到**相同题干＋相同3个验收条件＋相同A/B两段/状态账/未知输出要求**；普通对照不提供R055所选候选方法卡。R056另写匹配的38段普通原创文本（Git commit `43a51d342f8d94eced48e938a2f013b025db1362`），再按原来11分规则逐题打分并引用源中的确切短语；同一Agent自评，不能宣称盲评独立。
4. **真正公平配对记录结果**：19题中候选 **201/209**，相同要求下不提供方法卡的普通对照 **203/209**；候选胜 **0**、平 **17**、负 **2**；没有任何一题在本次评分获明显净增益。每题都有A/B两组真实文件、冻结评分项、候选/对照短引用、逐维评分和差值，见`R056_MATCHED_PAIRED_RATINGS.json`及两书`V3_TASK_LIFT.md`。
5. **反例必须保留**：《晚明》WM-04同条件对照让两名商人分别表态，候选只保证未擅改订单而较少呈现第二商人自主选择，角色能动性候选少1分；WM-09同条件对照让游客明确决定并列记录两种版本，候选仅指出游客意识到矛盾，独立求证行为较弱，也少1分。均是同一Agent评分，主张仅限这次文本。
6. **全部原候选处置不偷跑**：187个原ID V3账逐个更新，其中**47个V2有限通过方法**被标`NO_INCREMENTAL_GAIN_DEMONSTRATED_NONBLIND`，**11个**V2没实测的f/p`V2_NOT_TESTED_NO_V3`，**90项**参考`REFERENCE_NO_INDEPENDENT_V3`，**39项**仍有V1旧源缺口`BLOCKED_V1_NO_V3`。方法共同出现在同一写作任务中，不能确认具体哪条起作用；**没有一项由此晋级verified或active skill**。R057须给全体和旧14条质量债逐项归宿和明确用户确认；若没有V1/V2/V3都真实通过的单元，原版仓颉明确不得为满足数量凑Skill。
7. **质量结论层次**：本轮真实对照完成可以满足R056要求的输入、实际输出、评分、失败样本的**研究执行验收**；这不等于候选方法V3合格。明确区分R056过程通过与V3技能增益未通过。没有独立评审者、随机化、多个不同模型重复或Stage4宿主评测；评分偏向任务检查而非小说艺术品质，不能把同等检查清单的高分误读为历史军事长篇小说写作水平提高。文学B仍PROVISIONAL，C独立NOT_RUN、Skill0、heldout未拆。
8. **源历史隔离**：R042 14条早期缺陷继续`OPEN_QUARANTINED`、`NO_DIRECT_PROMOTION_RECONSTRUCT_FROM_SOURCE`，R054 39 REVIEW不解封；严禁无证自动修复。强制R057用户确认仅在下一次手动触发执行。

### 后续测试真实补救方向（R056不执行）

在R057确认前说明：若用户要求真正可判因果的增益，需公平固定相同题目和评分、由独立新会话/模型分别写作、独立盲评，再将有无方法差值与语义质量对照；并用含历史组织账和长期连续性的未知任务检验。R056不打开密封题库、不擅改89轮结构。
