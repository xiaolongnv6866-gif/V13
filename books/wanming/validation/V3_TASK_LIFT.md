# V13 R056｜《晚明》 V3任务增益匹配对照报告

round: R056
stage: Cangjie_Stage1.5_V3
status: MATCHED_PROMPT_EXPLORATORY_COMPARISON_NO_CERTIFIED_GAIN
comparison: same original writing input + same three expected criteria + same two scenes/state_contract/unknowns; baseline receives no candidate method card
comparison_limit: same model wrote both arms and scored them, not independent blind
heldout: SEALED_NOT_RUN
stage4_runtime: NOT_RUN
V3_certified_candidate_count: 0

## 有数据而没有净收益认证

- 本书原创任务9题；对照 **96/99**，候选 **94/99**，候选胜 0、平 7、负 2；实际场景输出19题各2组A/B，全部本地仓库可追查。
- **公平性修正**：第一批只给题干、不提供冻结标准的对照不公平；其候选201/209、普通168/209只是输入信息不对称的失败示例，不计入主统计。匹配组让两方都知道3条标准但无候选组不读技能卡，仅此才能观察候选额外效果。
- 本书候选状态明细由`tests/v3/R056_CANDIDATE_OUTCOMES.tsv`逐一沿用R055的187条原始ID与来源任务映射。47条V2有限通过方法没有额外任务增益认证，剩余11未测V2方法、90项参考、39项V1 REVIEW阻断不应自动晋级。
- 文学B仍`PROVISIONAL`，独立原创效用C仍`NOT_RUN`（此处纸面同一Agent探索已执行，但尚未独立盲审/运行）；SKILL认证数0。剧中战争军事操作未成为实际行动教程，原著人物/特征文字未复制。
- 本书任务是架空公共生活微场景，尚不覆盖真正长篇跨卷耐久性、宏观史实和战争/组织复杂度。评分有**清单合规偏好**，文笔自然感、深层次读者反应、跨长时间叙事均未测。

## 逐题可复查评分（9组）

### WM-01｜身份入口

- **相同输入真实路径**：`tests/v2/R055_FROZEN_INPUTS.json`；匹配无候选方法 `tests/v3/matched_baseline/WM-01.json`；原候选 `tests/v2/results/WM-01.json`。每组A/B两段场景、状态账、未知后果；两组均已收到完全相同的3条预注册标准。
- **评分**：公平对照 10/11；原候选 10/11；差值 **0**。对照的因果、人物、知情、交付各为`causal_chain=2；character_agency_continuity=1；epistemic_boundaries=2；deliverable_traceability=2`；候选对应`causal_chain=2；character_agency_continuity=1；epistemic_boundaries=2；deliverable_traceability=2`。
- **可在真实场景/状态账搜到的冻结标准片段**（短摘，每条必须能在相应文件复核）：

|预先冻结的条件|公平对照证据|原候选证据|
|---|---|---|
|多见证人判断不同|掌柜说他的测绘本事可靠|商人夸他本领高|
|资格、赞许、权限分别留痕|身份未核仅准公开誊录|身份核实=待核|
|申请不等获得职权|不能以掌柜一句话查看旧档|库册权限=未授权|

- **判定理由及失败边界**：公平对照已分别列清技能赞许、身份审查和库册许可，未测到额外方法收益。 所关联的候选`WM-f01`、`WM-p08`、`WM-p03`共同出现，不能将差值分别归因到每张卡片；同一作者写作并评分，非独立盲测。

### WM-02｜长期合作者异议

- **相同输入真实路径**：`tests/v2/R055_FROZEN_INPUTS.json`；匹配无候选方法 `tests/v3/matched_baseline/WM-02.json`；原候选 `tests/v2/results/WM-02.json`。每组A/B两段场景、状态账、未知后果；两组均已收到完全相同的3条预注册标准。
- **评分**：公平对照 11/11；原候选 11/11；差值 **0**。对照的因果、人物、知情、交付各为`causal_chain=2；character_agency_continuity=2；epistemic_boundaries=2；deliverable_traceability=2`；候选对应`causal_chain=2；character_agency_continuity=2；epistemic_boundaries=2；deliverable_traceability=2`。
- **可在真实场景/状态账搜到的冻结标准片段**（短摘，每条必须能在相应文件复核）：

|预先冻结的条件|公平对照证据|原候选证据|
|---|---|---|
|两种伦理理由都可辨认|催捐可以，但不能拿窘境羞辱人|姚湛说贫户家中正困难|
|拒绝改变行动|他不肯签公告|拒绝签字|
|保留长期关系负担|信任裂隙=留存|关系债务=未消|

- **判定理由及失败边界**：两组都让伦理反对改变公告且关系继续存在；本次不能区分框架带来的附加价值。 所关联的候选`WM-f02`、`WM-p01`共同出现，不能将差值分别归因到每张卡片；同一作者写作并评分，非独立盲测。

### WM-03｜授权与资源

- **相同输入真实路径**：`tests/v2/R055_FROZEN_INPUTS.json`；匹配无候选方法 `tests/v3/matched_baseline/WM-03.json`；原候选 `tests/v2/results/WM-03.json`。每组A/B两段场景、状态账、未知后果；两组均已收到完全相同的3条预注册标准。
- **评分**：公平对照 10/11；原候选 10/11；差值 **0**。对照的因果、人物、知情、交付各为`causal_chain=2；character_agency_continuity=1；epistemic_boundaries=2；deliverable_traceability=2`；候选对应`causal_chain=2；character_agency_continuity=1；epistemic_boundaries=2；deliverable_traceability=2`。
- **可在真实场景/状态账搜到的冻结标准片段**（短摘，每条必须能在相应文件复核）：

|预先冻结的条件|公平对照证据|原候选证据|
|---|---|---|
|名义与实权分离|任命书|新官帖|
|人财物承诺四项分开|纸=不足；资金=待拨|人员=两人；纸张=不足|
|限定同意和未结事|允办=公开目录|不批准调取封存账|

- **判定理由及失败边界**：匹配条件后，两组都分清人手纸张批复和有限实际权限。 所关联的候选`WM-f06`、`WM-p12`、`WM-p08`共同出现，不能将差值分别归因到每张卡片；同一作者写作并评分，非独立盲测。

### WM-04｜商货与到账

- **相同输入真实路径**：`tests/v2/R055_FROZEN_INPUTS.json`；匹配无候选方法 `tests/v3/matched_baseline/WM-04.json`；原候选 `tests/v2/results/WM-04.json`。每组A/B两段场景、状态账、未知后果；两组均已收到完全相同的3条预注册标准。
- **评分**：公平对照 11/11；原候选 10/11；差值 **-1**。对照的因果、人物、知情、交付各为`causal_chain=2；character_agency_continuity=2；epistemic_boundaries=2；deliverable_traceability=2`；候选对应`causal_chain=2；character_agency_continuity=1；epistemic_boundaries=2；deliverable_traceability=2`。
- **可在真实场景/状态账搜到的冻结标准片段**（短摘，每条必须能在相应文件复核）：

|预先冻结的条件|公平对照证据|原候选证据|
|---|---|---|
|预测与现款不等|月末的银不能点亮今夜的集会|未来钱|
|两商人自主选择|魏商不肯立即答应|许商肯现付|
|可见选择代价|村活动=缩小|照明须缩减|

- **判定理由及失败边界**：公平对照写出两商人独立讨价和村里后果，R055候选对其他商人选择略弱，是角色能动性反例。 所关联的候选`WM-f04`、`WM-p05`、`WM-p12`共同出现，不能将差值分别归因到每张卡片；同一作者写作并评分，非独立盲测。

### WM-05｜有限知情

- **相同输入真实路径**：`tests/v2/R055_FROZEN_INPUTS.json`；匹配无候选方法 `tests/v3/matched_baseline/WM-05.json`；原候选 `tests/v2/results/WM-05.json`。每组A/B两段场景、状态账、未知后果；两组均已收到完全相同的3条预注册标准。
- **评分**：公平对照 10/11；原候选 10/11；差值 **0**。对照的因果、人物、知情、交付各为`causal_chain=2；character_agency_continuity=1；epistemic_boundaries=2；deliverable_traceability=2`；候选对应`causal_chain=2；character_agency_continuity=1；epistemic_boundaries=2；deliverable_traceability=2`。
- **可在真实场景/状态账搜到的冻结标准片段**（短摘，每条必须能在相应文件复核）：

|预先冻结的条件|公平对照证据|原候选证据|
|---|---|---|
|两种视角不共享信息|北岸记录员只看到|北岸记录员只量到|
|亲见/转闻/未知分明|南岸=修好/未修好互相冲突的转闻|南岸来源=传闻|
|不能伪造桥安全结论|桥安全|桥是否安全=未查明|

- **判定理由及失败边界**：两组都限制亲见与传闻，桥是否安全仍未确定。 所关联的候选`WM-f08`、`WM-p07`、`WM-p19`共同出现，不能将差值分别归因到每张卡片；同一作者写作并评分，非独立盲测。

### WM-06｜功劳与家庭成本

- **相同输入真实路径**：`tests/v2/R055_FROZEN_INPUTS.json`；匹配无候选方法 `tests/v3/matched_baseline/WM-06.json`；原候选 `tests/v2/results/WM-06.json`。每组A/B两段场景、状态账、未知后果；两组均已收到完全相同的3条预注册标准。
- **评分**：公平对照 11/11；原候选 11/11；差值 **0**。对照的因果、人物、知情、交付各为`causal_chain=2；character_agency_continuity=2；epistemic_boundaries=2；deliverable_traceability=2`；候选对应`causal_chain=2；character_agency_continuity=2；epistemic_boundaries=2；deliverable_traceability=2`。
- **可在真实场景/状态账搜到的冻结标准片段**（短摘，每条必须能在相应文件复核）：

|预先冻结的条件|公平对照证据|原候选证据|
|---|---|---|
|公共成果/私人损失并置|风雨棚的主事者|风雨棚修完|
|三个分配声音|学徒拒绝把赏钱捐回公账|领赏的学徒|
|不虚构补偿已完成|赔付=尚无|赔付=未办|

- **判定理由及失败边界**：两组均把公开胜利、卖花损失、学徒药费和未给付补偿分开。 所关联的候选`WM-f10`、`WM-p04`共同出现，不能将差值分别归因到每张卡片；同一作者写作并评分，非独立盲测。

### WM-07｜治理试验

- **相同输入真实路径**：`tests/v2/R055_FROZEN_INPUTS.json`；匹配无候选方法 `tests/v3/matched_baseline/WM-07.json`；原候选 `tests/v2/results/WM-07.json`。每组A/B两段场景、状态账、未知后果；两组均已收到完全相同的3条预注册标准。
- **评分**：公平对照 11/11；原候选 11/11；差值 **0**。对照的因果、人物、知情、交付各为`causal_chain=2；character_agency_continuity=2；epistemic_boundaries=2；deliverable_traceability=2`；候选对应`causal_chain=2；character_agency_continuity=2；epistemic_boundaries=2；deliverable_traceability=2`。
- **可在真实场景/状态账搜到的冻结标准片段**（短摘，每条必须能在相应文件复核）：

|预先冻结的条件|公平对照证据|原候选证据|
|---|---|---|
|有实际异议及理由|制伞妇人却问|制伞妇人问|
|试点边界与复查日明确|时限=十天|试点=东街十日|
|暂行不等永久公正|推广=不准自动扩大|全面推广=未许可|

- **判定理由及失败边界**：同条件对照也自然写出十日试点、复核人和不得扩大，不能归功于候选。 所关联的候选`WM-f12`、`WM-p20`、`WM-p21`共同出现，不能将差值分别归因到每张卡片；同一作者写作并评分，非独立盲测。

### WM-08｜普通人独立意愿

- **相同输入真实路径**：`tests/v2/R055_FROZEN_INPUTS.json`；匹配无候选方法 `tests/v3/matched_baseline/WM-08.json`；原候选 `tests/v2/results/WM-08.json`。每组A/B两段场景、状态账、未知后果；两组均已收到完全相同的3条预注册标准。
- **评分**：公平对照 11/11；原候选 11/11；差值 **0**。对照的因果、人物、知情、交付各为`causal_chain=2；character_agency_continuity=2；epistemic_boundaries=2；deliverable_traceability=2`；候选对应`causal_chain=2；character_agency_continuity=2；epistemic_boundaries=2；deliverable_traceability=2`。
- **可在真实场景/状态账搜到的冻结标准片段**（短摘，每条必须能在相应文件复核）：

|预先冻结的条件|公平对照证据|原候选证据|
|---|---|---|
|少年自述意愿|陶念听到后开口说|陶念开口说|
|亲属意见不得代本人同意|本人同意=无|伯父代许=未经本人同意|
|时间推进中保留个人线|三个月后大集会上|三个月后的集会上|

- **判定理由及失败边界**：两组保护少年本人对家庭安排的拒绝，连续到三个月后，未测出附加收益。 所关联的候选`WM-f14`、`WM-p14`共同出现，不能将差值分别归因到每张卡片；同一作者写作并评分，非独立盲测。

### WM-09｜亲历与重述

- **相同输入真实路径**：`tests/v2/R055_FROZEN_INPUTS.json`；匹配无候选方法 `tests/v3/matched_baseline/WM-09.json`；原候选 `tests/v2/results/WM-09.json`。每组A/B两段场景、状态账、未知后果；两组均已收到完全相同的3条预注册标准。
- **评分**：公平对照 11/11；原候选 10/11；差值 **-1**。对照的因果、人物、知情、交付各为`causal_chain=2；character_agency_continuity=2；epistemic_boundaries=2；deliverable_traceability=2`；候选对应`causal_chain=2；character_agency_continuity=1；epistemic_boundaries=2；deliverable_traceability=2`。
- **可在真实场景/状态账搜到的冻结标准片段**（短摘，每条必须能在相应文件复核）：

|预先冻结的条件|公平对照证据|原候选证据|
|---|---|---|
|亲历记忆/舞台版本/未明区分|刻碑女工|女工只确认三户在场|
|不让争论抹掉历史现场|不把舞台热闹当作旧事全部|游客也发现|
|原创表演场所|旧渡的戏班|戏班如今却唱成|

- **判定理由及失败边界**：公平对照的游人主动记录两种说法，R055候选仅写游人意识到差异；角色独立行动略弱。 所关联的候选`WM-f13`、`WM-p23`共同出现，不能将差值分别归因到每张卡片；同一作者写作并评分，非独立盲测。

