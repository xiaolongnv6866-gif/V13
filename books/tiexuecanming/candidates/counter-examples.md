# V13 R051｜《铁血残明》反例提取器原始候选（仅研究层）

> 固定Cangjie Counter-Example Extractor独立职责。长篇小说中的人物言论、场面失败、预期风险和开放结局不能等同作者明确提出的外部管理法则。依据用户原始EPUB独立检索和邻接场面重读，原文版权正文不上传公开仓库；原版source_quote字段保留为空，使用n/p及private SHA定位。以下均未通过Stage1.5。原版五提取器原本并行；当前环境按原版允许的隔离串行降级，本轮只做反例，不冒充五代理同时工作。

```yaml
- id: ce01
  title: "后台倚赖被人事变动打断"
  type: counter-example
  evidence_kind: OBSERVED_FAILURE
  source_chapter: "n013/p34；n013/p52；n013/p56"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA
  source_loci:
    - "n013/p34"
    - "n013/p52"
    - "n013/p56"
  chunk_ids:
    - "ck-b3eadb1d9092"
    - "ck-eeeb24716a53"
  summary: |-
    原文当场可见：原来靠上级默许安排行事的承发官，遭临时主事者追问后才发觉程序本身成了追责凭据。
    核查的失败或不利预期：把非正式关系当成永久授权，无法面对权限和解释权突然变化。
    作用机制：一方拥有行政惯例记忆，另一方掌握当场裁量，隐瞒程序无法消除已留下的记录。
    不利结果的时间状态：OBSERVED_FAILURE；不得由角色担忧补成已经发生的失败。
    反向证据及成立边界：权力交接后旧后台不再保护具体决策；当场未完成所有官司争议的裁定。
    独立原创用途：写制度冲突时须补出当前实际有权者与利益相关者；不复制此具体官场算计或实施技巧。
  failure_mode: "把非正式关系当成永久授权，无法面对权限和解释权突然变化。"
  mechanism: "一方拥有行政惯例记忆，另一方掌握当场裁量，隐瞒程序无法消除已留下的记录。"
  warning_signs:
    - "当人物的口头承诺被叙述直接当作真实完成状态"
    - "当其他角色的不同知情、同意或未兑现成本被删去"
  bound_to:
    - "写制度冲突时须补出当前实际有权者与利益相关者；不复制此具体官场算计或实施技巧。"
  observed_status: OBSERVED_FAILURE
  counterpressure_or_limit: "权力交接后旧后台不再保护具体决策；当场未完成所有官司争议的裁定。"
  task_ids: [TX-02]
  tags: [fictional-narrative-counterexample, source-anchored, pending-triple-verification]
  source_reality: FICTIONAL_NOVEL_SCENE_NOT_HISTORICAL_EVIDENCE
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
- id: ce02
  title: "先递报文不保证取得功劳"
  type: counter-example
  evidence_kind: ANTICIPATED_RISK
  source_chapter: "n055/p30；n055/p31；n055/p32"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA
  source_loci:
    - "n055/p30"
    - "n055/p31"
    - "n055/p32"
  chunk_ids:
    - "ck-50a0a3ab62de"
  summary: |-
    原文当场可见：当事人希望抢先送达申详，幕友指出上级仍可能尊重另一官员的地位。
    核查的失败或不利预期：把提交时间写成最终认定结果，将权力裁量抹去。
    作用机制：文书时间和批复者对人事地位的判断不等价。
    不利结果的时间状态：ANTICIPATED_RISK；不得由角色担忧补成已经发生的失败。
    反向证据及成立边界：这里只是人物对未来审批的预判，不是后来的首功结果已经证实失败。
    独立原创用途：新小说把申请、审核、公布分层，不复用原报功人物与情节。
  failure_mode: "把提交时间写成最终认定结果，将权力裁量抹去。"
  mechanism: "文书时间和批复者对人事地位的判断不等价。"
  warning_signs:
    - "当人物的口头承诺被叙述直接当作真实完成状态"
    - "当其他角色的不同知情、同意或未兑现成本被删去"
  bound_to:
    - "新小说把申请、审核、公布分层，不复用原报功人物与情节。"
  observed_status: ANTICIPATED_RISK
  counterpressure_or_limit: "这里只是人物对未来审批的预判，不是后来的首功结果已经证实失败。"
  task_ids: [TX-02, TX-09]
  tags: [fictional-narrative-counterexample, source-anchored, pending-triple-verification]
  source_reality: FICTIONAL_NOVEL_SCENE_NOT_HISTORICAL_EVIDENCE
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
- id: ce03
  title: "现场应募热度不等于真实到岗"
  type: counter-example
  evidence_kind: OBSERVED_CONTRADICTION
  source_chapter: "n080/p19；n080/p67；n080/p68"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA
  source_loci:
    - "n080/p19"
    - "n080/p67"
    - "n080/p68"
  chunk_ids:
    - "ck-21a7316cb715"
  summary: |-
    原文当场可见：初期报名场面热闹，但实际报到者明显更少，营房物资也没有随着报名自动齐备。
    核查的失败或不利预期：把口头热情或一纸名单直接当成可用的成熟组织。
    作用机制：个人回家考虑会改变意愿，招募以外还必须兑现资源与场地。
    不利结果的时间状态：OBSERVED_CONTRADICTION；不得由角色担忧补成已经发生的失败。
    反向证据及成立边界：报到减少并非全然失败，故事明确接纳现实筛选后的人员。
    独立原创用途：用于写资源与时间错位，不转为现实军事招募或训练方法。
  failure_mode: "把口头热情或一纸名单直接当成可用的成熟组织。"
  mechanism: "个人回家考虑会改变意愿，招募以外还必须兑现资源与场地。"
  warning_signs:
    - "当人物的口头承诺被叙述直接当作真实完成状态"
    - "当其他角色的不同知情、同意或未兑现成本被删去"
  bound_to:
    - "用于写资源与时间错位，不转为现实军事招募或训练方法。"
  observed_status: OBSERVED_CONTRADICTION
  counterpressure_or_limit: "报到减少并非全然失败，故事明确接纳现实筛选后的人员。"
  task_ids: [TX-03, TX-04]
  tags: [fictional-narrative-counterexample, source-anchored, pending-triple-verification]
  source_reality: FICTIONAL_NOVEL_SCENE_NOT_HISTORICAL_EVIDENCE
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
- id: ce04
  title: "职位威压不能解决知情不足"
  type: counter-example
  evidence_kind: OBSERVED_CONTRADICTION
  source_chapter: "n082/p1；n082/p10；n082/p31"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA
  source_loci:
    - "n082/p1"
    - "n082/p10"
    - "n082/p31"
  chunk_ids:
    - "ck-765be0f3dbe0"
  summary: |-
    原文当场可见：主角面对不明局势承认知识空白，同时下属在职位选择上因揣测上司意图而迟疑。
    核查的失败或不利预期：将绝对权威等同完备情报或高质量下属判断。
    作用机制：领导的压力可以压低公开异议，却不能产生原本缺失的外部事实。
    不利结果的时间状态：OBSERVED_CONTRADICTION；不得由角色担忧补成已经发生的失败。
    反向证据及成立边界：下属并非处处不能自主，不能由一场迟疑推断未来全员无能。
    独立原创用途：只用于角色认知边界与对白潜台词，不输出军事情报实施步骤。
  failure_mode: "将绝对权威等同完备情报或高质量下属判断。"
  mechanism: "领导的压力可以压低公开异议，却不能产生原本缺失的外部事实。"
  warning_signs:
    - "当人物的口头承诺被叙述直接当作真实完成状态"
    - "当其他角色的不同知情、同意或未兑现成本被删去"
  bound_to:
    - "只用于角色认知边界与对白潜台词，不输出军事情报实施步骤。"
  observed_status: OBSERVED_CONTRADICTION
  counterpressure_or_limit: "下属并非处处不能自主，不能由一场迟疑推断未来全员无能。"
  task_ids: [TX-03, TX-06]
  tags: [fictional-narrative-counterexample, source-anchored, pending-triple-verification]
  source_reality: FICTIONAL_NOVEL_SCENE_NOT_HISTORICAL_EVIDENCE
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
- id: ce05
  title: "有限物证不能被政治压力自动补足"
  type: counter-example
  evidence_kind: CHARACTER_DISAGREEMENT
  source_chapter: "n102/p2；n102/p6；n102/p10"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA
  source_loci:
    - "n102/p2"
    - "n102/p6"
    - "n102/p10"
  chunk_ids:
    - "ck-0ea0f0a7708d"
  summary: |-
    原文当场可见：一方指出眼前物证仍不足以断言身份，另一方强调拖延判断的严重风险。
    核查的失败或不利预期：用单一物证证明完整因果，或反过来要求风险必须消失才能行动。
    作用机制：证据精度和即时责任存在不可回避的拉扯，两人有各自的失误代价。
    不利结果的时间状态：CHARACTER_DISAGREEMENT；不得由角色担忧补成已经发生的失败。
    反向证据及成立边界：双方在这一场争论不等于哪方的判断已被后续事实证实。
    独立原创用途：提取文学的不确定性而不是侦查或社会控制指南。
  failure_mode: "用单一物证证明完整因果，或反过来要求风险必须消失才能行动。"
  mechanism: "证据精度和即时责任存在不可回避的拉扯，两人有各自的失误代价。"
  warning_signs:
    - "当人物的口头承诺被叙述直接当作真实完成状态"
    - "当其他角色的不同知情、同意或未兑现成本被删去"
  bound_to:
    - "提取文学的不确定性而不是侦查或社会控制指南。"
  observed_status: CHARACTER_DISAGREEMENT
  counterpressure_or_limit: "双方在这一场争论不等于哪方的判断已被后续事实证实。"
  task_ids: [TX-06, TX-09]
  tags: [fictional-narrative-counterexample, source-anchored, pending-triple-verification]
  source_reality: FICTIONAL_NOVEL_SCENE_NOT_HISTORICAL_EVIDENCE
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
- id: ce06
  title: "预备仓落空但替代供给有限存在"
  type: counter-example
  evidence_kind: OBSERVED_CONTRADICTION
  source_chapter: "n114/p27；n114/p29；n114/p31"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA
  source_loci:
    - "n114/p27"
    - "n114/p29"
    - "n114/p31"
  chunk_ids:
    - "ck-4f52a5896754"
  summary: |-
    原文当场可见：官员发现原已要求留存的仓库不具备预期库存，其他在地供给却暂时能够填补缺口。
    核查的失败或不利预期：把行政命令当成真实库存，或把临时替代当永久解决。
    作用机制：同一时间账面、仓储与地方自有资源可以朝不同方向变化。
    不利结果的时间状态：OBSERVED_CONTRADICTION；不得由角色担忧补成已经发生的失败。
    反向证据及成立边界：原书确有临时补救，不能为了反例而改写成完全断供。
    独立原创用途：适用于虚构后勤与财务连贯性，禁止输出战争供给实施细节。
  failure_mode: "把行政命令当成真实库存，或把临时替代当永久解决。"
  mechanism: "同一时间账面、仓储与地方自有资源可以朝不同方向变化。"
  warning_signs:
    - "当人物的口头承诺被叙述直接当作真实完成状态"
    - "当其他角色的不同知情、同意或未兑现成本被删去"
  bound_to:
    - "适用于虚构后勤与财务连贯性，禁止输出战争供给实施细节。"
  observed_status: OBSERVED_CONTRADICTION
  counterpressure_or_limit: "原书确有临时补救，不能为了反例而改写成完全断供。"
  task_ids: [TX-04]
  tags: [fictional-narrative-counterexample, source-anchored, pending-triple-verification]
  source_reality: FICTIONAL_NOVEL_SCENE_NOT_HISTORICAL_EVIDENCE
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
- id: ce07
  title: "从属者的服从未必出于自愿"
  type: counter-example
  evidence_kind: OBSERVED_COERCION
  source_chapter: "n161/p5；n161/p65；n161/p66"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA
  source_loci:
    - "n161/p5"
    - "n161/p65"
    - "n161/p66"
  chunk_ids:
    - "ck-81185a14e235"
    - "ck-38346ea3f6ed"
  summary: |-
    原文当场可见：一人受命加入组织时提出希望保留原有身份，掌权者直接否决并要求服从式回话。
    核查的失败或不利预期：把口头顺从或身份登记作为自主同意的证明。
    作用机制：身分差和惩戒预期削弱当事人的真正拒绝空间。
    不利结果的时间状态：OBSERVED_COERCION；不得由角色担忧补成已经发生的失败。
    反向证据及成立边界：这里可以确认当场拒绝要求，不能凭此断定其未来所有行动均非自愿。
    独立原创用途：用于伦理和人物主动性审计，不提取任何强制管理手段。
  failure_mode: "把口头顺从或身份登记作为自主同意的证明。"
  mechanism: "身分差和惩戒预期削弱当事人的真正拒绝空间。"
  warning_signs:
    - "当人物的口头承诺被叙述直接当作真实完成状态"
    - "当其他角色的不同知情、同意或未兑现成本被删去"
  bound_to:
    - "用于伦理和人物主动性审计，不提取任何强制管理手段。"
  observed_status: OBSERVED_COERCION
  counterpressure_or_limit: "这里可以确认当场拒绝要求，不能凭此断定其未来所有行动均非自愿。"
  task_ids: [TX-05, TX-08]
  tags: [fictional-narrative-counterexample, source-anchored, pending-triple-verification]
  source_reality: FICTIONAL_NOVEL_SCENE_NOT_HISTORICAL_EVIDENCE
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
- id: ce08
  title: "严密军律的内部张力不是已发生崩溃"
  type: counter-example
  evidence_kind: ANTICIPATED_RISK
  source_chapter: "n165/p1；n165/p5；n165/p80"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA
  source_loci:
    - "n165/p1"
    - "n165/p5"
    - "n165/p80"
  chunk_ids:
    - "ck-be2cd13f75cc"
    - "ck-5dd12ab06437"
  summary: |-
    原文当场可见：一名文职属员对制度条款提出具体质疑，主持者担心长期紧张产生反作用，同时强调职位权威。
    核查的失败或不利预期：把条文制定自动写成全员心悦诚服且经受长期考验。
    作用机制：规章的形式权力与基层承受压力具有不同的时间效应。
    不利结果的时间状态：ANTICIPATED_RISK；不得由角色担忧补成已经发生的失败。
    反向证据及成立边界：场内所说的群体反作用是人物预测，不是本章已经出现该结局。
    独立原创用途：仅用于小说内部权力伦理冲突，不成为现实军纪准则。
  failure_mode: "把条文制定自动写成全员心悦诚服且经受长期考验。"
  mechanism: "规章的形式权力与基层承受压力具有不同的时间效应。"
  warning_signs:
    - "当人物的口头承诺被叙述直接当作真实完成状态"
    - "当其他角色的不同知情、同意或未兑现成本被删去"
  bound_to:
    - "仅用于小说内部权力伦理冲突，不成为现实军纪准则。"
  observed_status: ANTICIPATED_RISK
  counterpressure_or_limit: "场内所说的群体反作用是人物预测，不是本章已经出现该结局。"
  task_ids: [TX-05, TX-08]
  tags: [fictional-narrative-counterexample, source-anchored, pending-triple-verification]
  source_reality: FICTIONAL_NOVEL_SCENE_NOT_HISTORICAL_EVIDENCE
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
- id: ce09
  title: "资源收入预估无法抹掉真实现金流压力"
  type: counter-example
  evidence_kind: OBSERVED_CONTRADICTION
  source_chapter: "n174/p13；n174/p37；n174/p39"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA
  source_loci:
    - "n174/p13"
    - "n174/p37"
    - "n174/p39"
  chunk_ids:
    - "ck-ed04a60bce49"
  summary: |-
    原文当场可见：码头生意已因驻军影响流量，管事报告收入安排，但家属账册显示现有开支更大。
    核查的失败或不利预期：把新收入渠道的设想当成随时可支出的净收入。
    作用机制：商人自主回避、利益分配与成本开销都与管理者估计存在差距。
    不利结果的时间状态：OBSERVED_CONTRADICTION；不得由角色担忧补成已经发生的失败。
    反向证据及成立边界：码头收益并非完全不存在，无法由当场短缺判定后续一定破产。
    独立原创用途：用于叙事上的资金/时间三态，不输出真实经营强制或金融操盘方法。
  failure_mode: "把新收入渠道的设想当成随时可支出的净收入。"
  mechanism: "商人自主回避、利益分配与成本开销都与管理者估计存在差距。"
  warning_signs:
    - "当人物的口头承诺被叙述直接当作真实完成状态"
    - "当其他角色的不同知情、同意或未兑现成本被删去"
  bound_to:
    - "用于叙事上的资金/时间三态，不输出真实经营强制或金融操盘方法。"
  observed_status: OBSERVED_CONTRADICTION
  counterpressure_or_limit: "码头收益并非完全不存在，无法由当场短缺判定后续一定破产。"
  task_ids: [TX-03, TX-04]
  tags: [fictional-narrative-counterexample, source-anchored, pending-triple-verification]
  source_reality: FICTIONAL_NOVEL_SCENE_NOT_HISTORICAL_EVIDENCE
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
- id: ce10
  title: "高回报说辞不能消灭家庭现金需求"
  type: counter-example
  evidence_kind: CHARACTER_DISAGREEMENT
  source_chapter: "n180/p12；n180/p20；n180/p29"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA
  source_loci:
    - "n180/p12"
    - "n180/p20"
    - "n180/p29"
  chunk_ids:
    - "ck-0e87ea162375"
  summary: |-
    原文当场可见：不同文职人员对储蓄利息与每日生活需要给出不同选择与理由。
    核查的失败或不利预期：把一个角色认可的存款计划写成全体员工都适用的好办法。
    作用机制：人物的家属负担、短期可用现金和风险感知不是同一尺度。
    不利结果的时间状态：CHARACTER_DISAGREEMENT；不得由角色担忧补成已经发生的失败。
    反向证据及成立边界：对立意见当场存在，但并未证明该存款制度最终失败。
    独立原创用途：用作原创家庭选择的伦理对照，不得作为现实投资建议。
  failure_mode: "把一个角色认可的存款计划写成全体员工都适用的好办法。"
  mechanism: "人物的家属负担、短期可用现金和风险感知不是同一尺度。"
  warning_signs:
    - "当人物的口头承诺被叙述直接当作真实完成状态"
    - "当其他角色的不同知情、同意或未兑现成本被删去"
  bound_to:
    - "用作原创家庭选择的伦理对照，不得作为现实投资建议。"
  observed_status: CHARACTER_DISAGREEMENT
  counterpressure_or_limit: "对立意见当场存在，但并未证明该存款制度最终失败。"
  task_ids: [TX-04, TX-08]
  tags: [fictional-narrative-counterexample, source-anchored, pending-triple-verification]
  source_reality: FICTIONAL_NOVEL_SCENE_NOT_HISTORICAL_EVIDENCE
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
- id: ce11
  title: "公众赞誉不能清除私人关系旧债"
  type: counter-example
  evidence_kind: OBSERVED_CONTRADICTION
  source_chapter: "n202/p3；n202/p20；n202/p33"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA
  source_loci:
    - "n202/p3"
    - "n202/p20"
    - "n202/p33"
  chunk_ids:
    - "ck-6236a5ac5eae"
  summary: |-
    原文当场可见：公共场合突现旧关系争议，旁观官员改变了对主人公的部分看法，另一当事人又提出自己的意愿。
    核查的失败或不利预期：让公共事业上的成功取消他人尚未解决的私人判断。
    作用机制：不同目击者掌握不同材料，社会评价不随一次嘉奖同步。
    不利结果的时间状态：OBSERVED_CONTRADICTION；不得由角色担忧补成已经发生的失败。
    反向证据及成立边界：公开控诉与女子口述都尚待核验，不能在此强判谁全对。
    独立原创用途：写新人物信誉账，不复制退婚相关具体情节。
  failure_mode: "让公共事业上的成功取消他人尚未解决的私人判断。"
  mechanism: "不同目击者掌握不同材料，社会评价不随一次嘉奖同步。"
  warning_signs:
    - "当人物的口头承诺被叙述直接当作真实完成状态"
    - "当其他角色的不同知情、同意或未兑现成本被删去"
  bound_to:
    - "写新人物信誉账，不复制退婚相关具体情节。"
  observed_status: OBSERVED_CONTRADICTION
  counterpressure_or_limit: "公开控诉与女子口述都尚待核验，不能在此强判谁全对。"
  task_ids: [TX-01, TX-08]
  tags: [fictional-narrative-counterexample, source-anchored, pending-triple-verification]
  source_reality: FICTIONAL_NOVEL_SCENE_NOT_HISTORICAL_EVIDENCE
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
- id: ce12
  title: "签了任命册也有尚未核清的职位空缺"
  type: counter-example
  evidence_kind: OBSERVED_FAILURE
  source_chapter: "n213/p2；n213/p5；n213/p18；n213/p21"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA
  source_loci:
    - "n213/p2"
    - "n213/p5"
    - "n213/p18"
    - "n213/p21"
  chunk_ids:
    - "ck-4196dc342c08"
  summary: |-
    原文当场可见：上司已签署人事册，却遇到举报尚需调查；争端在营内升级，而例行简报没有完整呈报。
    核查的失败或不利预期：用任命动作掩盖岗位实际不可就位和机构间信息遮蔽。
    作用机制：正式名单、事实调查、实际执行及不愿公布的信息可以不同步。
    不利结果的时间状态：OBSERVED_FAILURE；不得由角色担忧补成已经发生的失败。
    反向证据及成立边界：指控仍应保留待证身份，不能把举报本身当作裁决。
    独立原创用途：仅提取叙事证据分层，不能转换成武力或惩罚操作。
  failure_mode: "用任命动作掩盖岗位实际不可就位和机构间信息遮蔽。"
  mechanism: "正式名单、事实调查、实际执行及不愿公布的信息可以不同步。"
  warning_signs:
    - "当人物的口头承诺被叙述直接当作真实完成状态"
    - "当其他角色的不同知情、同意或未兑现成本被删去"
  bound_to:
    - "仅提取叙事证据分层，不能转换成武力或惩罚操作。"
  observed_status: OBSERVED_FAILURE
  counterpressure_or_limit: "指控仍应保留待证身份，不能把举报本身当作裁决。"
  task_ids: [TX-02, TX-03, TX-05]
  tags: [fictional-narrative-counterexample, source-anchored, pending-triple-verification]
  source_reality: FICTIONAL_NOVEL_SCENE_NOT_HISTORICAL_EVIDENCE
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
- id: ce13
  title: "共同军事目的不能取代盟友独立同意"
  type: counter-example
  evidence_kind: OBSERVED_FAILURE_WITH_COUNTER
  source_chapter: "n315/p35；n315/p40；n485/p8；n485/p23"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA
  source_loci:
    - "n315/p35"
    - "n315/p40"
    - "n485/p8"
    - "n485/p23"
  chunk_ids:
    - "ck-c775a37b2c4c"
    - "ck-f8106dc67ad3"
  summary: |-
    原文当场可见：一次协调中主角无法用既有军令说服他方；另一次相似协作须在条件得到讨论后才有限谈成。
    核查的失败或不利预期：把主角的命令与既有盟友名义视为毫无条件的同一意志。
    作用机制：另一方有自己的风险与收益判断，合作需要可见的相互约束。
    不利结果的时间状态：OBSERVED_FAILURE_WITH_COUNTER；不得由角色担忧补成已经发生的失败。
    反向证据及成立边界：第二场有条件成功，明确反证一律不能合作的过度归纳。
    独立原创用途：只提取多方决策叙事与条件同意，不供战术指引。
  failure_mode: "把主角的命令与既有盟友名义视为毫无条件的同一意志。"
  mechanism: "另一方有自己的风险与收益判断，合作需要可见的相互约束。"
  warning_signs:
    - "当人物的口头承诺被叙述直接当作真实完成状态"
    - "当其他角色的不同知情、同意或未兑现成本被删去"
  bound_to:
    - "只提取多方决策叙事与条件同意，不供战术指引。"
  observed_status: OBSERVED_FAILURE_WITH_COUNTER
  counterpressure_or_limit: "第二场有条件成功，明确反证一律不能合作的过度归纳。"
  task_ids: [TX-06]
  tags: [fictional-narrative-counterexample, source-anchored, pending-triple-verification]
  source_reality: FICTIONAL_NOVEL_SCENE_NOT_HISTORICAL_EVIDENCE
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
- id: ce14
  title: "胜利发生不表示战后责任已经关闭"
  type: counter-example
  evidence_kind: OBSERVED_UNRESOLVED
  source_chapter: "n357/p49；n357/p58；n357/p60"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA
  source_loci:
    - "n357/p49"
    - "n357/p58"
    - "n357/p60"
  chunk_ids:
    - "ck-d45164547c01"
  summary: |-
    原文当场可见：事后大量人员安置、粮食、地方承受力和管理责任成为新争论，地方官提出附带条件。
    核查的失败或不利预期：以场面胜负取代受影响人之后生活与财政的安排。
    作用机制：事件成果创造新人口和治理义务，第三方拥有接受或拒绝的条件。
    不利结果的时间状态：OBSERVED_UNRESOLVED；不得由角色担忧补成已经发生的失败。
    反向证据及成立边界：这里的安置方案正在谈判，既不能宣称全面成功也不能伪造未来失败。
    独立原创用途：用于人道后果与公共责任小说结构，不涉及战俘管理技巧。
  failure_mode: "以场面胜负取代受影响人之后生活与财政的安排。"
  mechanism: "事件成果创造新人口和治理义务，第三方拥有接受或拒绝的条件。"
  warning_signs:
    - "当人物的口头承诺被叙述直接当作真实完成状态"
    - "当其他角色的不同知情、同意或未兑现成本被删去"
  bound_to:
    - "用于人道后果与公共责任小说结构，不涉及战俘管理技巧。"
  observed_status: OBSERVED_UNRESOLVED
  counterpressure_or_limit: "这里的安置方案正在谈判，既不能宣称全面成功也不能伪造未来失败。"
  task_ids: [TX-04, TX-07]
  tags: [fictional-narrative-counterexample, source-anchored, pending-triple-verification]
  source_reality: FICTIONAL_NOVEL_SCENE_NOT_HISTORICAL_EVIDENCE
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
- id: ce15
  title: "新士官饷等会制造新的权责歧义"
  type: counter-example
  evidence_kind: ANTICIPATED_RISK_PARTIALLY_RESOLVED
  source_chapter: "n361/p34；n361/p35；n361/p36"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA
  source_loci:
    - "n361/p34"
    - "n361/p35"
    - "n361/p36"
  chunk_ids:
    - "ck-68ca5ccbce7e"
  summary: |-
    原文当场可见：上级宣布按待遇分级，专业属员立即质疑这是否会改变指挥的上下级关系，并获得解释。
    核查的失败或不利预期：把待遇提升、身份变化和实质权限写成天然一致。
    作用机制：新增称谓会与原有权威产生读者和角色均须厘清的冲突。
    不利结果的时间状态：ANTICIPATED_RISK_PARTIALLY_RESOLVED；不得由角色担忧补成已经发生的失败。
    反向证据及成立边界：当场疑问得到答复，但缺失长期实测结果。
    独立原创用途：小说内需验证实施，禁止作为真实军事组织管理规范。
  failure_mode: "把待遇提升、身份变化和实质权限写成天然一致。"
  mechanism: "新增称谓会与原有权威产生读者和角色均须厘清的冲突。"
  warning_signs:
    - "当人物的口头承诺被叙述直接当作真实完成状态"
    - "当其他角色的不同知情、同意或未兑现成本被删去"
  bound_to:
    - "小说内需验证实施，禁止作为真实军事组织管理规范。"
  observed_status: ANTICIPATED_RISK_PARTIALLY_RESOLVED
  counterpressure_or_limit: "当场疑问得到答复，但缺失长期实测结果。"
  task_ids: [TX-05]
  tags: [fictional-narrative-counterexample, source-anchored, pending-triple-verification]
  source_reality: FICTIONAL_NOVEL_SCENE_NOT_HISTORICAL_EVIDENCE
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
- id: ce16
  title: "请旨中的责任推让会产生实际时间差"
  type: counter-example
  evidence_kind: OBSERVED_DELAY
  source_chapter: "n424/p9；n424/p11；n424/p25"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA
  source_loci:
    - "n424/p9"
    - "n424/p11"
    - "n424/p25"
  chunk_ids:
    - "ck-491658b4759f"
  summary: |-
    原文当场可见：中央商议与上级模糊批示反复往返，文件最终确定时外部局势又变。
    核查的失败或不利预期：把有程序、有签章写成决策已经在有效时限内完成。
    作用机制：当事人试图避免承担责任，造成重复确认，而消息有不可逆时间差。
    不利结果的时间状态：OBSERVED_DELAY；不得由角色担忧补成已经发生的失败。
    反向证据及成立边界：并非所有延迟都无益；此场确实出现时间损失，不等于已经展示最终战局结果。
    独立原创用途：只提取多主体信息与叙事时间机制，不作战术或现实政治建议。
  failure_mode: "把有程序、有签章写成决策已经在有效时限内完成。"
  mechanism: "当事人试图避免承担责任，造成重复确认，而消息有不可逆时间差。"
  warning_signs:
    - "当人物的口头承诺被叙述直接当作真实完成状态"
    - "当其他角色的不同知情、同意或未兑现成本被删去"
  bound_to:
    - "只提取多主体信息与叙事时间机制，不作战术或现实政治建议。"
  observed_status: OBSERVED_DELAY
  counterpressure_or_limit: "并非所有延迟都无益；此场确实出现时间损失，不等于已经展示最终战局结果。"
  task_ids: [TX-02, TX-06]
  tags: [fictional-narrative-counterexample, source-anchored, pending-triple-verification]
  source_reality: FICTIONAL_NOVEL_SCENE_NOT_HISTORICAL_EVIDENCE
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
- id: ce17
  title: "有银不能当即兑换出需要的粮食"
  type: counter-example
  evidence_kind: OBSERVED_RESOURCE_FAILURE
  source_chapter: "n431/p10；n431/p17；n431/p18；n431/p19"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA
  source_loci:
    - "n431/p10"
    - "n431/p17"
    - "n431/p18"
    - "n431/p19"
  chunk_ids:
    - "ck-12cf33d9bcc0"
  summary: |-
    原文当场可见：军中粮食实际短缺，地方承诺的一日实物供给变成折银，前线却无法用货币买到当下所需物资。
    核查的失败或不利预期：以可结算的货币数字代替所在地即时可得的实物。
    作用机制：供给地点和市场可得性为人物当场缺粮提供决定性约束。
    不利结果的时间状态：OBSERVED_RESOURCE_FAILURE；不得由角色担忧补成已经发生的失败。
    反向证据及成立边界：原书并未由此断定未来所有地域均无法用银换粮。
    独立原创用途：仅分析资源条件推动剧情，拒绝战争物流可操作指导。
  failure_mode: "以可结算的货币数字代替所在地即时可得的实物。"
  mechanism: "供给地点和市场可得性为人物当场缺粮提供决定性约束。"
  warning_signs:
    - "当人物的口头承诺被叙述直接当作真实完成状态"
    - "当其他角色的不同知情、同意或未兑现成本被删去"
  bound_to:
    - "仅分析资源条件推动剧情，拒绝战争物流可操作指导。"
  observed_status: OBSERVED_RESOURCE_FAILURE
  counterpressure_or_limit: "原书并未由此断定未来所有地域均无法用银换粮。"
  task_ids: [TX-04, TX-06]
  tags: [fictional-narrative-counterexample, source-anchored, pending-triple-verification]
  source_reality: FICTIONAL_NOVEL_SCENE_NOT_HISTORICAL_EVIDENCE
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
- id: ce18
  title: "纸面后勤方案无法覆盖实际劳动现场"
  type: counter-example
  evidence_kind: OBSERVED_EXECUTION_GAP
  source_chapter: "n490/p28；n490/p30；n505/p8"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA
  source_loci:
    - "n490/p28"
    - "n490/p30"
    - "n505/p8"
  chunk_ids:
    - "ck-accd0b1e8cba"
    - "ck-c160e6655638"
  summary: |-
    原文当场可见：负责人执行已有安排，却在现场面对人手分散与不断出现的小问题，稍后普通人仍有生计与秩序争议。
    核查的失败或不利预期：将方案成文或上级经过当作执行没有摩擦的保证。
    作用机制：现场人员、物资和个体行为有独立连续性，必须由场景显示差距。
    不利结果的时间状态：OBSERVED_EXECUTION_GAP；不得由角色担忧补成已经发生的失败。
    反向证据及成立边界：不能从局部混乱宣布整体计划已完全失败。
    独立原创用途：不提供战场操作细节，聚焦劳动与普通人后续生活。
  failure_mode: "将方案成文或上级经过当作执行没有摩擦的保证。"
  mechanism: "现场人员、物资和个体行为有独立连续性，必须由场景显示差距。"
  warning_signs:
    - "当人物的口头承诺被叙述直接当作真实完成状态"
    - "当其他角色的不同知情、同意或未兑现成本被删去"
  bound_to:
    - "不提供战场操作细节，聚焦劳动与普通人后续生活。"
  observed_status: OBSERVED_EXECUTION_GAP
  counterpressure_or_limit: "不能从局部混乱宣布整体计划已完全失败。"
  task_ids: [TX-03, TX-07]
  tags: [fictional-narrative-counterexample, source-anchored, pending-triple-verification]
  source_reality: FICTIONAL_NOVEL_SCENE_NOT_HISTORICAL_EVIDENCE
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
- id: ce19
  title: "把文书写得合理可能扭曲真实发生的事"
  type: counter-example
  evidence_kind: CHARACTER_PROPOSAL_REJECTED
  source_chapter: "n526/p82；n526/p85；n526/p87"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA
  source_loci:
    - "n526/p82"
    - "n526/p85"
    - "n526/p87"
  chunk_ids:
    - "ck-2fe7ec8ea640"
  summary: |-
    原文当场可见：书面记录者建议让数字看起来符合常识，当场承担事件的人拒绝并撕去不实文稿。
    核查的失败或不利预期：让未经核实的文本整齐性取代现场见证。
    作用机制：同一事件的描述权在两个角色手中相互冲突，发表与提议必须分开。
    不利结果的时间状态：CHARACTER_PROPOSAL_REJECTED；不得由角色担忧补成已经发生的失败。
    反向证据及成立边界：此处虚报建议遭拒，不能宣称假数字最后已经获准。
    独立原创用途：仅分析报告真实度的叙事张力，不给误导或造假教程。
  failure_mode: "让未经核实的文本整齐性取代现场见证。"
  mechanism: "同一事件的描述权在两个角色手中相互冲突，发表与提议必须分开。"
  warning_signs:
    - "当人物的口头承诺被叙述直接当作真实完成状态"
    - "当其他角色的不同知情、同意或未兑现成本被删去"
  bound_to:
    - "仅分析报告真实度的叙事张力，不给误导或造假教程。"
  observed_status: CHARACTER_PROPOSAL_REJECTED
  counterpressure_or_limit: "此处虚报建议遭拒，不能宣称假数字最后已经获准。"
  task_ids: [TX-09]
  tags: [fictional-narrative-counterexample, source-anchored, pending-triple-verification]
  source_reality: FICTIONAL_NOVEL_SCENE_NOT_HISTORICAL_EVIDENCE
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
- id: ce20
  title: "离队许可不能消除家眷和结保责任"
  type: counter-example
  evidence_kind: PARTIAL_SUCCESS_FUTURE_UNKNOWN
  source_chapter: "n527/p30；n527/p31；n527/p38；n527/p39"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA
  source_loci:
    - "n527/p30"
    - "n527/p31"
    - "n527/p38"
    - "n527/p39"
  chunk_ids:
    - "ck-744b1d1ff9a3"
  summary: |-
    原文当场可见：同意人员暂时回乡，但费用被扣留一部分，资助和结保又有其他人的担忧。
    核查的失败或不利预期：把批准请求等同实际资金足够、家庭平安团聚与人必然按时返回。
    作用机制：申请项目、附条件许可、到手资源和未来行动是不同事实。
    不利结果的时间状态：PARTIAL_SUCCESS_FUTURE_UNKNOWN；不得由角色担忧补成已经发生的失败。
    反向证据及成立边界：原书展示人物作出保证但并未于此完成返营验证。
    独立原创用途：用于自主选择和后续因果账，不模仿原书人物关系。
  failure_mode: "把批准请求等同实际资金足够、家庭平安团聚与人必然按时返回。"
  mechanism: "申请项目、附条件许可、到手资源和未来行动是不同事实。"
  warning_signs:
    - "当人物的口头承诺被叙述直接当作真实完成状态"
    - "当其他角色的不同知情、同意或未兑现成本被删去"
  bound_to:
    - "用于自主选择和后续因果账，不模仿原书人物关系。"
  observed_status: PARTIAL_SUCCESS_FUTURE_UNKNOWN
  counterpressure_or_limit: "原书展示人物作出保证但并未于此完成返营验证。"
  task_ids: [TX-08, TX-10]
  tags: [fictional-narrative-counterexample, source-anchored, pending-triple-verification]
  source_reality: FICTIONAL_NOVEL_SCENE_NOT_HISTORICAL_EVIDENCE
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
- id: ce21
  title: "写下财务承诺不等于履行与兑付"
  type: counter-example
  evidence_kind: OUTCOME_NOT_SHOWN
  source_chapter: "n531/p8；n532/p47；n532/p49"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA
  source_loci:
    - "n531/p8"
    - "n532/p47"
    - "n532/p49"
  chunk_ids:
    - "ck-0480b01161d6"
    - "ck-988023f3637e"
  summary: |-
    原文当场可见：相关角色面对账实与信用压力，当前提供版本以写下拟承担的金额结束这一线索。
    核查的失败或不利预期：把决定承诺的高潮误写成已经兑现的成果或失败。
    作用机制：纸面决定创造新义务，而兑现依赖后续尚未写出的行为。
    不利结果的时间状态：OUTCOME_NOT_SHOWN；不得由角色担忧补成已经发生的失败。
    反向证据及成立边界：这是未完成的风险，并非证实的金融失败；不能编造原著后续。
    独立原创用途：只作原创小说悬念结构参考，不提供融资发行指引。
  failure_mode: "把决定承诺的高潮误写成已经兑现的成果或失败。"
  mechanism: "纸面决定创造新义务，而兑现依赖后续尚未写出的行为。"
  warning_signs:
    - "当人物的口头承诺被叙述直接当作真实完成状态"
    - "当其他角色的不同知情、同意或未兑现成本被删去"
  bound_to:
    - "只作原创小说悬念结构参考，不提供融资发行指引。"
  observed_status: OUTCOME_NOT_SHOWN
  counterpressure_or_limit: "这是未完成的风险，并非证实的金融失败；不能编造原著后续。"
  task_ids: [TX-04, TX-10]
  tags: [fictional-narrative-counterexample, source-anchored, pending-triple-verification]
  source_reality: FICTIONAL_NOVEL_SCENE_NOT_HISTORICAL_EVIDENCE
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
```

## 反例不是负面情绪的代称

此表同时包含OBSERVED(已经出现的局部困难)、ANTICIPATED(角色担忧)、CHARACTER_DISAGREEMENT(对立观点)、PARTIAL_SUCCESS(已有有限解决但长远未知)与OUTCOME_NOT_SHOWN(尚未发生)。不可把所有条目说成已证实失败；也不把小说人物的功利判断等同作者立场。十项TX任务只是候选来源覆盖，不是SKILL可执行性认证。R042隔离的14项旧claim不直接晋级。A真实私有来源已审，文学B仍PROVISIONAL，C NOT_RUN，Skill0。
