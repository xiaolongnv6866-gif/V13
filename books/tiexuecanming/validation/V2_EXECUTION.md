# V13 R055｜《铁血残明》 Stage1.5 V2合法新输入可执行性演练

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

本书独立Stage0任务 **10/10个** 具有新造合法输入，每题事先冻结题干、适用已通过V1的f/p候选、3项完成条件；实际以两种不同场景短文完成演练，含人物台词/动作、来源条件的状态账和未知事件的判停说明。样例文件在 `tests/v2/results/<task>.json`（原始输出）与`tests/v2/R055_RUNBOOK.md`（易读索引）。原作者情节/语言不复制，技术测试只检查当前虚构题目的一致性。

**本书全量候选（96）：实际绑定新题V2纸面PASS 26，V1来源仍REVIEW阻断 16，来源案例/反例/术语仅参考 48，V1 PASS但未分配实际V2新题 6。**

### 每项任务的已固定输入与实际交付

|任务ID|新题|本次实际使用V1-PASS的候选ID|冻结检查条件|真实结果路径|边界|
|---|---|---|---|---|---|
|TX-01|污名与新评价|TX-f01, TX-p01, TX-p11|三组不同见证人；旧污点仍存在；新功不等全员信任|tests/v2/results/TX-01.json|walkthrough only|
|TX-02|申请受理审核|TX-f02, TX-p03, TX-p12|申请/受理/批准/执行/追责分列；签收不等批准；后续职责明确|tests/v2/results/TX-02.json|walkthrough only|
|TX-03|属员纠正负责人|TX-f05, TX-p09, TX-p04|专业自主提出异议；负责人承认知识空白；预留试验结果未知|tests/v2/results/TX-03.json|walkthrough only|
|TX-04|账面与在手物资|TX-p05, TX-p21, TX-f16|货币与实物分离；临时补偿变成新义务；未来归还未知|tests/v2/results/TX-04.json|walkthrough only|
|TX-05|等级与权限|TX-f08, TX-p08, TX-p07|津贴和权力不同；异议被听取；不宣称制度长效成功|tests/v2/results/TX-05.json|walkthrough only|
|TX-06|三方有限协作|TX-f12, TX-p13, TX-p06|三方独立知情和条件；谈成须留条件；未知不得由主角补齐|tests/v2/results/TX-06.json|walkthrough only|
|TX-07|对手与平民目标|TX-f09, TX-p14, TX-f10|配角至少两种自主选择；非主角行动产生后果；公共工程不抹掉生活|tests/v2/results/TX-07.json|walkthrough only|
|TX-08|申请与本人选择|TX-f11, TX-p20, TX-p07|许可和实际离岗不同；代班者不能被强制代言；未定工资留缺口|tests/v2/results/TX-08.json|walkthrough only|
|TX-09|现场与记录版本|TX-f13, TX-p19, TX-p17|现场/草稿/发行三级不同；虚增被质疑；绝不称假报已发行|tests/v2/results/TX-09.json|walkthrough only|
|TX-10|留下未履行义务|TX-f16, TX-p21|纸面承诺和未来兑现不同；实物缺口可见；不得杜撰结局|tests/v2/results/TX-10.json|walkthrough only|

### 有源依据但尚未V2实测的可执行候选

- `TX-f03`：地方调解与官署利益交错的制度现场；V1仅限定原文PASS，没有在冻结的19个新题中执行，不应因别的候选成功而计PASS。
- `TX-f04`：名义官职与跨部门实际约束的不等式；V1仅限定原文PASS，没有在冻结的19个新题中执行，不应因别的候选成功而计PASS。
- `TX-f15`：制度扩大后反对者的真实生存空间；V1仅限定原文PASS，没有在冻结的19个新题中执行，不应因别的候选成功而计PASS。
- `TX-p02`：背会制度文件不能等同实际运用；V1仅限定原文PASS，没有在冻结的19个新题中执行，不应因别的候选成功而计PASS。
- `TX-p15`：对立官员主张不得冒充作者一致立场；V1仅限定原文PASS，没有在冻结的19个新题中执行，不应因别的候选成功而计PASS。
- `TX-p18`：预制方案不能取消现场劳动摩擦；V1仅限定原文PASS，没有在冻结的19个新题中执行，不应因别的候选成功而计PASS。

### 重要保留与不得推广

- 16条V1 REVIEW均沿用R054具体缺口，不能降级规则通过CI后升级；历史R042的14条被隔离旧主张维持`NO_DIRECT_PROMOTION_RECONSTRUCT_FROM_SOURCE`。
- 48条case/counter-example/term候选保留故事来源的参考意义；若欲晋级为可执行方法，需另外证明规则来源与执行输入/输出，不由简单词义概念自动成为skill。
- 两份A/B场景都是**同一个Agent写出的不同版本**，可用于检查文学结构是否受约束，不能证明独立运行复现；预期结果的逐项文本锚点是受审证据，**不是独立盲评质量分数**。R056必须同题设计无候选基线和增益审计。
- 原创场景只涉及架空民间生活，无军事/胁迫/欺诈现实操作，历史真实制度需另证。全局B PROVISIONAL，C独立效用NOT_RUN，认证SKILL0，heldout SEALED。
