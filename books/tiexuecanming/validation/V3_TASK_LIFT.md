# V13 R056｜《铁血残明》 V3任务增益匹配对照报告

round: R056
stage: Cangjie_Stage1.5_V3
status: MATCHED_PROMPT_EXPLORATORY_COMPARISON_NO_CERTIFIED_GAIN
comparison: same original writing input + same three expected criteria + same two scenes/state_contract/unknowns; baseline receives no candidate method card
comparison_limit: same model wrote both arms and scored them, not independent blind
heldout: SEALED_NOT_RUN
stage4_runtime: NOT_RUN
V3_certified_candidate_count: 0

## 有数据而没有净收益认证

- 本书原创任务10题；对照 **107/110**，候选 **107/110**，候选胜 0、平 10、负 0；实际场景输出19题各2组A/B，全部本地仓库可追查。
- **公平性修正**：第一批只给题干、不提供冻结标准的对照不公平；其候选201/209、普通168/209只是输入信息不对称的失败示例，不计入主统计。匹配组让两方都知道3条标准但无候选组不读技能卡，仅此才能观察候选额外效果。
- 本书候选状态明细由`tests/v3/R056_CANDIDATE_OUTCOMES.tsv`逐一沿用R055的187条原始ID与来源任务映射。47条V2有限通过方法没有额外任务增益认证，剩余11未测V2方法、90项参考、39项V1 REVIEW阻断不应自动晋级。
- 文学B仍`PROVISIONAL`，独立原创效用C仍`NOT_RUN`（此处纸面同一Agent探索已执行，但尚未独立盲审/运行）；SKILL认证数0。剧中战争军事操作未成为实际行动教程，原著人物/特征文字未复制。
- 本书任务是架空公共生活微场景，尚不覆盖真正长篇跨卷耐久性、宏观史实和战争/组织复杂度。评分有**清单合规偏好**，文笔自然感、深层次读者反应、跨长时间叙事均未测。

## 逐题可复查评分（10组）

### TX-01｜污名与新评价

- **相同输入真实路径**：`tests/v2/R055_FROZEN_INPUTS.json`；匹配无候选方法 `tests/v3/matched_baseline/TX-01.json`；原候选 `tests/v2/results/TX-01.json`。每组A/B两段场景、状态账、未知后果；两组均已收到完全相同的3条预注册标准。
- **评分**：公平对照 11/11；原候选 11/11；差值 **0**。对照的因果、人物、知情、交付各为`causal_chain=2；character_agency_continuity=2；epistemic_boundaries=2；deliverable_traceability=2`；候选对应`causal_chain=2；character_agency_continuity=2；epistemic_boundaries=2；deliverable_traceability=2`。
- **可在真实场景/状态账搜到的冻结标准片段**（短摘，每条必须能在相应文件复核）：

|预先冻结的条件|公平对照证据|原候选证据|
|---|---|---|
|三组不同见证人|旧雇主当众说|旧雇主指出|
|旧污点仍存在|旧名声=误报|曾误报水位|
|新功不等全员信任|信用=未定|旧雇主仍不肯担保|

- **判定理由及失败边界**：两组均让旧雇主、村妇和公署持不同评价，历史污点保留。 所关联的候选`TX-f01`、`TX-p01`、`TX-p11`共同出现，不能将差值分别归因到每张卡片；同一作者写作并评分，非独立盲测。

### TX-02｜申请受理审核

- **相同输入真实路径**：`tests/v2/R055_FROZEN_INPUTS.json`；匹配无候选方法 `tests/v3/matched_baseline/TX-02.json`；原候选 `tests/v2/results/TX-02.json`。每组A/B两段场景、状态账、未知后果；两组均已收到完全相同的3条预注册标准。
- **评分**：公平对照 10/11；原候选 10/11；差值 **0**。对照的因果、人物、知情、交付各为`causal_chain=2；character_agency_continuity=1；epistemic_boundaries=2；deliverable_traceability=2`；候选对应`causal_chain=2；character_agency_continuity=1；epistemic_boundaries=2；deliverable_traceability=2`。
- **可在真实场景/状态账搜到的冻结标准片段**（短摘，每条必须能在相应文件复核）：

|预先冻结的条件|公平对照证据|原候选证据|
|---|---|---|
|申请/受理/批准/执行/追责分列|申请、受理、批准、开工、追责|递交、受理两格已有字|
|签收不等批准|受理格盖章|不能凭那张收据开工|
|后续职责明确|馆主实际批复|追责=未分配|

- **判定理由及失败边界**：配对对照也明确五阶段办理与独立财务承诺，申请不等批准不需额外卡片。 所关联的候选`TX-f02`、`TX-p03`、`TX-p12`共同出现，不能将差值分别归因到每张卡片；同一作者写作并评分，非独立盲测。

### TX-03｜属员纠正负责人

- **相同输入真实路径**：`tests/v2/R055_FROZEN_INPUTS.json`；匹配无候选方法 `tests/v3/matched_baseline/TX-03.json`；原候选 `tests/v2/results/TX-03.json`。每组A/B两段场景、状态账、未知后果；两组均已收到完全相同的3条预注册标准。
- **评分**：公平对照 11/11；原候选 11/11；差值 **0**。对照的因果、人物、知情、交付各为`causal_chain=2；character_agency_continuity=2；epistemic_boundaries=2；deliverable_traceability=2`；候选对应`causal_chain=2；character_agency_continuity=2；epistemic_boundaries=2；deliverable_traceability=2`。
- **可在真实场景/状态账搜到的冻结标准片段**（短摘，每条必须能在相应文件复核）：

|预先冻结的条件|公平对照证据|原候选证据|
|---|---|---|
|专业自主提出异议|安意说可以先在一小排试三天|安意发现展窗木版晒褪色|
|负责人承认知识空白|柳明承认自己不懂染料|主事者请安意记颜色|
|预留试验结果未知|评估=待观察|正式改制=未定|

- **判定理由及失败边界**：同标准下安意的自主质疑、领导知识缺口和三日复查均清晰。 所关联的候选`TX-f05`、`TX-p09`、`TX-p04`共同出现，不能将差值分别归因到每张卡片；同一作者写作并评分，非独立盲测。

### TX-04｜账面与在手物资

- **相同输入真实路径**：`tests/v2/R055_FROZEN_INPUTS.json`；匹配无候选方法 `tests/v3/matched_baseline/TX-04.json`；原候选 `tests/v2/results/TX-04.json`。每组A/B两段场景、状态账、未知后果；两组均已收到完全相同的3条预注册标准。
- **评分**：公平对照 10/11；原候选 10/11；差值 **0**。对照的因果、人物、知情、交付各为`causal_chain=2；character_agency_continuity=1；epistemic_boundaries=2；deliverable_traceability=2`；候选对应`causal_chain=2；character_agency_continuity=1；epistemic_boundaries=2；deliverable_traceability=2`。
- **可在真实场景/状态账搜到的冻结标准片段**（短摘，每条必须能在相应文件复核）：

|预先冻结的条件|公平对照证据|原候选证据|
|---|---|---|
|货币与实物分离|募款=承诺数足但尚未到账|捐款只是承诺|
|临时补偿变成新义务|但要明春归还|要求明春归还|
|未来归还未知|还毯=明春义务|返还义务=未履行|

- **判定理由及失败边界**：在给予相同要求后，对照把现款/现货/借物/未来归还完整列清，候选没有额外收益。 所关联的候选`TX-p05`、`TX-p21`、`TX-f16`共同出现，不能将差值分别归因到每张卡片；同一作者写作并评分，非独立盲测。

### TX-05｜等级与权限

- **相同输入真实路径**：`tests/v2/R055_FROZEN_INPUTS.json`；匹配无候选方法 `tests/v3/matched_baseline/TX-05.json`；原候选 `tests/v2/results/TX-05.json`。每组A/B两段场景、状态账、未知后果；两组均已收到完全相同的3条预注册标准。
- **评分**：公平对照 11/11；原候选 11/11；差值 **0**。对照的因果、人物、知情、交付各为`causal_chain=2；character_agency_continuity=2；epistemic_boundaries=2；deliverable_traceability=2`；候选对应`causal_chain=2；character_agency_continuity=2；epistemic_boundaries=2；deliverable_traceability=2`。
- **可在真实场景/状态账搜到的冻结标准片段**（短摘，每条必须能在相应文件复核）：

|预先冻结的条件|公平对照证据|原候选证据|
|---|---|---|
|津贴和权力不同|新津贴不改原来的核准签名|只调酬劳不改装帧核准权|
|异议被听取|装帧工答应暂时照办|装帧工提出一个月后|
|不宣称制度长效成功|复核=一月后|长期实测=未开始|

- **判定理由及失败边界**：两组均独立处理加薪与核签权利，并把实测结果留在一个月后。 所关联的候选`TX-f08`、`TX-p08`、`TX-p07`共同出现，不能将差值分别归因到每张卡片；同一作者写作并评分，非独立盲测。

### TX-06｜三方有限协作

- **相同输入真实路径**：`tests/v2/R055_FROZEN_INPUTS.json`；匹配无候选方法 `tests/v3/matched_baseline/TX-06.json`；原候选 `tests/v2/results/TX-06.json`。每组A/B两段场景、状态账、未知后果；两组均已收到完全相同的3条预注册标准。
- **评分**：公平对照 11/11；原候选 11/11；差值 **0**。对照的因果、人物、知情、交付各为`causal_chain=2；character_agency_continuity=2；epistemic_boundaries=2；deliverable_traceability=2`；候选对应`causal_chain=2；character_agency_continuity=2；epistemic_boundaries=2；deliverable_traceability=2`。
- **可在真实场景/状态账搜到的冻结标准片段**（短摘，每条必须能在相应文件复核）：

|预先冻结的条件|公平对照证据|原候选证据|
|---|---|---|
|三方独立知情和条件|东乡代表说有诗会的大厅|东乡说可以借诗会大厅|
|谈成须留条件|协议=一次附条件|三方仅同意先办一次|
|未知不得由主角补齐|时间=待确认|日期=未定|

- **判定理由及失败边界**：对照明确三乡信息不对称、署名条件与风险，候选未增加可见因果。 所关联的候选`TX-f12`、`TX-p13`、`TX-p06`共同出现，不能将差值分别归因到每张卡片；同一作者写作并评分，非独立盲测。

### TX-07｜对手与平民目标

- **相同输入真实路径**：`tests/v2/R055_FROZEN_INPUTS.json`；匹配无候选方法 `tests/v3/matched_baseline/TX-07.json`；原候选 `tests/v2/results/TX-07.json`。每组A/B两段场景、状态账、未知后果；两组均已收到完全相同的3条预注册标准。
- **评分**：公平对照 11/11；原候选 11/11；差值 **0**。对照的因果、人物、知情、交付各为`causal_chain=2；character_agency_continuity=2；epistemic_boundaries=2；deliverable_traceability=2`；候选对应`causal_chain=2；character_agency_continuity=2；epistemic_boundaries=2；deliverable_traceability=2`。
- **可在真实场景/状态账搜到的冻结标准片段**（短摘，每条必须能在相应文件复核）：

|预先冻结的条件|公平对照证据|原候选证据|
|---|---|---|
|配角至少两种自主选择|修船匠先忙着抢救自己的木料|女掌柜却在湿地上找账册|
|非主角行动产生后果|女掌柜从旧木箱里找到半本账|他们没等负责人指挥|
|公共工程不抹掉生活|露宿者=保留挡风|露宿者=挡风|

- **判定理由及失败边界**：对照让非主角独立做事和发生后果，候选也完成；本题未见新机制增益。 所关联的候选`TX-f09`、`TX-p14`、`TX-f10`共同出现，不能将差值分别归因到每张卡片；同一作者写作并评分，非独立盲测。

### TX-08｜申请与本人选择

- **相同输入真实路径**：`tests/v2/R055_FROZEN_INPUTS.json`；匹配无候选方法 `tests/v3/matched_baseline/TX-08.json`；原候选 `tests/v2/results/TX-08.json`。每组A/B两段场景、状态账、未知后果；两组均已收到完全相同的3条预注册标准。
- **评分**：公平对照 11/11；原候选 11/11；差值 **0**。对照的因果、人物、知情、交付各为`causal_chain=2；character_agency_continuity=2；epistemic_boundaries=2；deliverable_traceability=2`；候选对应`causal_chain=2；character_agency_continuity=2；epistemic_boundaries=2；deliverable_traceability=2`。
- **可在真实场景/状态账搜到的冻结标准片段**（短摘，每条必须能在相应文件复核）：

|预先冻结的条件|公平对照证据|原候选证据|
|---|---|---|
|许可和实际离岗不同|编辑说可准，但要先安排校样交接|编辑答应先完成校样交接|
|代班者不能被强制代言|代班者=本人确认愿代|同事只说愿看看稿|
|未定工资留缺口|额外报酬=待谈|报酬=未决定|

- **判定理由及失败边界**：给定相同条件后，普通对照也写出代班者自愿与工资未决。 所关联的候选`TX-f11`、`TX-p20`、`TX-p07`共同出现，不能将差值分别归因到每张卡片；同一作者写作并评分，非独立盲测。

### TX-09｜现场与记录版本

- **相同输入真实路径**：`tests/v2/R055_FROZEN_INPUTS.json`；匹配无候选方法 `tests/v3/matched_baseline/TX-09.json`；原候选 `tests/v2/results/TX-09.json`。每组A/B两段场景、状态账、未知后果；两组均已收到完全相同的3条预注册标准。
- **评分**：公平对照 11/11；原候选 11/11；差值 **0**。对照的因果、人物、知情、交付各为`causal_chain=2；character_agency_continuity=2；epistemic_boundaries=2；deliverable_traceability=2`；候选对应`causal_chain=2；character_agency_continuity=2；epistemic_boundaries=2；deliverable_traceability=2`。
- **可在真实场景/状态账搜到的冻结标准片段**（短摘，每条必须能在相应文件复核）：

|预先冻结的条件|公平对照证据|原候选证据|
|---|---|---|
|现场/草稿/发行三级不同|评审册只记下暂时停赛|评审册只记暂停|
|虚增被质疑|目击孩子却提醒他|目击的孩子指出|
|绝不称假报已发行|实际刊发=未发生|刊发=未发生|

- **判定理由及失败边界**：两组严格区分风停现场、未发行草稿和角色提出的质疑；没有净收益。 所关联的候选`TX-f13`、`TX-p19`、`TX-p17`共同出现，不能将差值分别归因到每张卡片；同一作者写作并评分，非独立盲测。

### TX-10｜留下未履行义务

- **相同输入真实路径**：`tests/v2/R055_FROZEN_INPUTS.json`；匹配无候选方法 `tests/v3/matched_baseline/TX-10.json`；原候选 `tests/v2/results/TX-10.json`。每组A/B两段场景、状态账、未知后果；两组均已收到完全相同的3条预注册标准。
- **评分**：公平对照 10/11；原候选 10/11；差值 **0**。对照的因果、人物、知情、交付各为`causal_chain=2；character_agency_continuity=1；epistemic_boundaries=2；deliverable_traceability=2`；候选对应`causal_chain=2；character_agency_continuity=1；epistemic_boundaries=2；deliverable_traceability=2`。
- **可在真实场景/状态账搜到的冻结标准片段**（短摘，每条必须能在相应文件复核）：

|预先冻结的条件|公平对照证据|原候选证据|
|---|---|---|
|纸面承诺和未来兑现不同|下一季修好二十本旧谱|写下下季修二十本旧谱|
|实物缺口可见|现有纸料=六本份|纸料=仅六本|
|不得杜撰结局|责任=下一季仍待履行|责任=未履行|

- **判定理由及失败边界**：相同明确三标准使普通稿也保留二十本承诺、六本库存和零本实际完工。 所关联的候选`TX-f16`、`TX-p21`共同出现，不能将差值分别归因到每张卡片；同一作者写作并评分，非独立盲测。

