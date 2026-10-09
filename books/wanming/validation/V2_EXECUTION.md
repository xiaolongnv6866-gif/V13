# V13 R055｜《晚明》 Stage1.5 V2合法新输入可执行性演练

status: V2_PAPER_WALKTHROUGH_COMPLETED_PARTIAL_METHOD_COVERAGE
source_of_frozen_inputs: tests/v2/R055_FROZEN_INPUTS.json
input_freeze_commit: 27fa253c133ad892f67f14c6236716835d7c365d
V2_mode: CANGJIE_PAPER_WALKTHROUGH
host_runtime_execution: NOT_RUN_STAGE4
independent_model_repetition: NOT_RUN
V3_task_utility: NOT_STARTED_R056
project_literary_B: PROVISIONAL
project_original_C_independent_test: NOT_RUN
skill_certified_count: 0

## 当轮真实执行结果

本书独立Stage0任务 **9/9个** 具有新造合法输入，每题事先冻结题干、适用已通过V1的f/p候选、3项完成条件；实际以两种不同场景短文完成演练，含人物台词/动作、来源条件的状态账和未知事件的判停说明。样例文件在 `tests/v2/results/<task>.json`（原始输出）与`tests/v2/R055_RUNBOOK.md`（易读索引）。原作者情节/语言不复制，技术测试只检查当前虚构题目的一致性。

**本书全量候选（91）：实际绑定新题V2纸面PASS 21，V1来源仍REVIEW阻断 23，来源案例/反例/术语仅参考 42，V1 PASS但未分配实际V2新题 5。**

### 每项任务的已固定输入与实际交付

|任务ID|新题|本次实际使用V1-PASS的候选ID|冻结检查条件|真实结果路径|边界|
|---|---|---|---|---|---|
|WM-01|身份入口|WM-f01, WM-p08, WM-p03|多见证人判断不同；资格、赞许、权限分别留痕；申请不等获得职权|tests/v2/results/WM-01.json|walkthrough only|
|WM-02|长期合作者异议|WM-f02, WM-p01|两种伦理理由都可辨认；拒绝改变行动；保留长期关系负担|tests/v2/results/WM-02.json|walkthrough only|
|WM-03|授权与资源|WM-f06, WM-p12, WM-p08|名义与实权分离；人财物承诺四项分开；限定同意和未结事|tests/v2/results/WM-03.json|walkthrough only|
|WM-04|商货与到账|WM-f04, WM-p05, WM-p12|预测与现款不等；两商人自主选择；可见选择代价|tests/v2/results/WM-04.json|walkthrough only|
|WM-05|有限知情|WM-f08, WM-p07, WM-p19|两种视角不共享信息；亲见/转闻/未知分明；不能伪造桥安全结论|tests/v2/results/WM-05.json|walkthrough only|
|WM-06|功劳与家庭成本|WM-f10, WM-p04|公共成果/私人损失并置；三个分配声音；不虚构补偿已完成|tests/v2/results/WM-06.json|walkthrough only|
|WM-07|治理试验|WM-f12, WM-p20, WM-p21|有实际异议及理由；试点边界与复查日明确；暂行不等永久公正|tests/v2/results/WM-07.json|walkthrough only|
|WM-08|普通人独立意愿|WM-f14, WM-p14|少年自述意愿；亲属意见不得代本人同意；时间推进中保留个人线|tests/v2/results/WM-08.json|walkthrough only|
|WM-09|亲历与重述|WM-f13, WM-p23|亲历记忆/舞台版本/未明区分；不让争论抹掉历史现场；原创表演场所|tests/v2/results/WM-09.json|walkthrough only|

### 有源依据但尚未V2实测的可执行候选

- `WM-f11`：制度宣称、他人权利与实际手续的分层；V1仅限定原文PASS，没有在冻结的19个新题中执行，不应因别的候选成功而计PASS。
- `WM-f16`：想法—评估—否决—组织后果的创新检验；V1仅限定原文PASS，没有在冻结的19个新题中执行，不应因别的候选成功而计PASS。
- `WM-p06`：紧急与重要的先后说法须限定场景；V1仅限定原文PASS，没有在冻结的19个新题中执行，不应因别的候选成功而计PASS。
- `WM-p13`：暂时同意不等于永久执行；V1仅限定原文PASS，没有在冻结的19个新题中执行，不应因别的候选成功而计PASS。
- `WM-p18`：新设想经比较后可以被拒绝；V1仅限定原文PASS，没有在冻结的19个新题中执行，不应因别的候选成功而计PASS。

### 重要保留与不得推广

- 23条V1 REVIEW均沿用R054具体缺口，不能降级规则通过CI后升级；历史R042的14条被隔离旧主张维持`NO_DIRECT_PROMOTION_RECONSTRUCT_FROM_SOURCE`。
- 42条case/counter-example/term候选保留故事来源的参考意义；若欲晋级为可执行方法，需另外证明规则来源与执行输入/输出，不由简单词义概念自动成为skill。
- 两份A/B场景都是**同一个Agent写出的不同版本**，可用于检查文学结构是否受约束，不能证明独立运行复现；预期结果的逐项文本锚点是受审证据，**不是独立盲评质量分数**。R056必须同题设计无候选基线和增益审计。
- 原创场景只涉及架空民间生活，无军事/胁迫/欺诈现实操作，历史真实制度需另证。全局B PROVISIONAL，C独立效用NOT_RUN，认证SKILL0，heldout SEALED。
