# 《晚明》Stage1｜反例提取器原始候选（R046）

> 原版Cangjie v2.5 `extractors/counter-example-extractor.md` 独立执行；基于R042已确认的`BOOK_OVERVIEW.md`与用户私有《晚明》原始EPUB，不用R043—R045候选内容作为证据。原著属于小说：**小说人物的错误/警告不等于作者本人提出的规范**；所有候选B=PROVISIONAL，须Stage1.5验证。

> 来源可在私有原书按n/p及本轮段落SHA重验，公开GitHub不转载原书段落，保留原版`source_quote`字段但显式留空。风险/尚未发生的可能性和已观察失效分开，不能夸大。

```yaml
- id: ce01
  title: "会说账房术语，不等于会实际记账"
  type: counter-example
  source_chapter: "n010/p29;n010/p39"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA
  evidence_kind: SCENE_DEMONSTRATED_LIMIT
  source_loci:
    - "n010/p29"
    - "n010/p39"
  chunk_ids:
    - "ck-2f9e2e835d0c"
  summary: |-
    局面：自称熟悉店铺业务的人正在争取职位。
    原文可见：同伴当场发现算盘与旧式账目技能并非其真实能力，继而质疑即将到来的正式面试。
    失效边界：尚未证明后来一定考核失败；不直接推出作者对整个时代职业的判断。
    推断的机制：人物把现代知识和体面身份错误地等同于当地技术资格，造成需要掩饰的专业缺口。
    状态：这是小说场景中的反例候选，不是作者的真实经历或通用定律。
  failure_mode: "人物把现代知识和体面身份错误地等同于当地技术资格，造成需要掩饰的专业缺口。"
  mechanism: "原书因果可见：同伴当场发现算盘与旧式账目技能并非其真实能力，继而质疑即将到来的正式面试。；分析解释：人物把现代知识和体面身份错误地等同于当地技术资格，造成需要掩饰的专业缺口。"
  warning_signs:
    - "被问到本地实际工序却只谈抽象经验"
    - "同伴能指出具体不会的环节。"
  bound_to:
    - "身份入口真实度;制度环境对现代人的反向限制"
  task_ids: [WM-01, WM-04]
  missing_conditions: "尚未证明后来一定考核失败；不直接推出作者对整个时代职业的判断。"
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
  tags: [historical-fiction, narrative-failure, source-anchored]
- id: ce02
  title: "只按组织成本选人，忽略家庭负担"
  type: counter-example
  source_chapter: "n061/p47;n061/p49;n061/p50"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA
  evidence_kind: REJECTED_RISK_IN_SCENE
  source_loci:
    - "n061/p47"
    - "n061/p49"
    - "n061/p50"
  chunk_ids:
    - "ck-4dd7d25df687"
  summary: |-
    局面：主角正在贫困人群中选择新的工作参与者。
    原文可见：有人建议只选择单身者以规避家属成本；主角意识到一户人的处境，最后没有执行这一排除建议。
    失效边界：危险建议没有最终实施；不能写成已发生的虐待或已长期解决救助问题。
    推断的机制：把依赖人群视为可替换成本，会让人员筛选与真实个人责任发生冲突。
    状态：这是小说场景中的反例候选，不是作者的真实经历或通用定律。
  failure_mode: "把依赖人群视为可替换成本，会让人员筛选与真实个人责任发生冲突。"
  mechanism: "原书因果可见：有人建议只选择单身者以规避家属成本；主角意识到一户人的处境，最后没有执行这一排除建议。；分析解释：把依赖人群视为可替换成本，会让人员筛选与真实个人责任发生冲突。"
  warning_signs:
    - "把家属视为无效成本"
    - "只有组织便利而无当事人后续生活安排。"
  bound_to:
    - "非主角人物权利;组织招募叙事的伦理边界"
  task_ids: [WM-02, WM-08]
  missing_conditions: "危险建议没有最终实施；不能写成已发生的虐待或已长期解决救助问题。"
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
  tags: [historical-fiction, narrative-failure, source-anchored]
- id: ce03
  title: "纸面委派熟人，内部信任未闭合"
  type: counter-example
  source_chapter: "n064/p41;n064/p45;n064/p46"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA
  evidence_kind: ANTICIPATED_CONFLICT
  source_loci:
    - "n064/p41"
    - "n064/p45"
    - "n064/p46"
  chunk_ids:
    - "ck-72b7daac54b9"
  summary: |-
    局面：原负责者需离开现有店铺并给出经营接替人选。
    原文可见：角色明确认为较有才能的人选会受到内部排挤，另一候选可能被下属利用，于是更换店铺负责人。
    失效边界：这些不利后果是人物预测，源段没有演示所有候选都已遭实际排挤。
    推断的机制：名义任命不能自动取得旧员工的合作；组织内部地位与关系可能抵消能力评价。
    状态：这是小说场景中的反例候选，不是作者的真实经历或通用定律。
  failure_mode: "名义任命不能自动取得旧员工的合作；组织内部地位与关系可能抵消能力评价。"
  mechanism: "原书因果可见：角色明确认为较有才能的人选会受到内部排挤，另一候选可能被下属利用，于是更换店铺负责人。；分析解释：名义任命不能自动取得旧员工的合作；组织内部地位与关系可能抵消能力评价。"
  warning_signs:
    - "提拔者只询问自己的好恶"
    - "未考虑旧成员的相互约束和实际服从。"
  bound_to:
    - "人物权威;组织继任与内部关系"
  task_ids: [WM-01, WM-03]
  missing_conditions: "这些不利后果是人物预测，源段没有演示所有候选都已遭实际排挤。"
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
  tags: [historical-fiction, narrative-failure, source-anchored]
- id: ce04
  title: "名义负责人不能代替现场组织协调"
  type: counter-example
  source_chapter: "n080/p30;n080/p34;n080/p36"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA
  evidence_kind: OBSERVED_BREAKDOWN
  source_loci:
    - "n080/p30"
    - "n080/p34"
    - "n080/p36"
  chunk_ids:
    - "ck-14015cd82165"
  summary: |-
    局面：多人共同参与一次较长的跨地点集体移动。
    原文可见：成员集合迟缓、指挥者临时漏掉组织安排，最终全天进程明显落后原有意图。
    失效边界：这里只分析戏剧情节组织与时间后果，不转成真实队伍调度或军事实施技巧。
    推断的机制：拥有头衔、随从和口头命令，并不能保证各组人员在时间上同步行动。
    状态：这是小说场景中的反例候选，不是作者的真实经历或通用定律。
  failure_mode: "拥有头衔、随从和口头命令，并不能保证各组人员在时间上同步行动。"
  mechanism: "原书因果可见：成员集合迟缓、指挥者临时漏掉组织安排，最终全天进程明显落后原有意图。；分析解释：拥有头衔、随从和口头命令，并不能保证各组人员在时间上同步行动。"
  warning_signs:
    - "现场时间表被不断推后"
    - "角色不清楚谁先谁后"
    - "群众抱怨而无人解决。"
  bound_to:
    - "虚构组织执行与计划兑现"
  task_ids: [WM-03, WM-05]
  missing_conditions: "这里只分析戏剧情节组织与时间后果，不转成真实队伍调度或军事实施技巧。"
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
  tags: [historical-fiction, narrative-failure, source-anchored]
- id: ce05
  title: "声称贡献就能独占分配标准"
  type: counter-example
  source_chapter: "n085/p25;n085/p27;n085/p29"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA
  evidence_kind: OBSERVED_DISPUTE
  source_loci:
    - "n085/p25"
    - "n085/p27"
    - "n085/p29"
  chunk_ids:
    - "ck-64574098eea7"
  summary: |-
    局面：集体事件后，多个利益方讨论一批资源应由谁得到。
    原文可见：不同参与者分别以损失补偿、参与人数、现场作用来提出不兼容的分配要求，争议当场没有自然消散。
    失效边界：争议出现不代表任何一套算法正确，也不证明最后结算失败。
    推断的机制：各方把最有利于自己的口径包装成公允标准，造成利益冲突而非共识。
    状态：这是小说场景中的反例候选，不是作者的真实经历或通用定律。
  failure_mode: "各方把最有利于自己的口径包装成公允标准，造成利益冲突而非共识。"
  mechanism: "原书因果可见：不同参与者分别以损失补偿、参与人数、现场作用来提出不兼容的分配要求，争议当场没有自然消散。；分析解释：各方把最有利于自己的口径包装成公允标准，造成利益冲突而非共识。"
  warning_signs:
    - "每一方只统计自己贡献的维度"
    - "忽略别人承担的实际损失。"
  bound_to:
    - "战后利益账;权利与荣誉分配"
  task_ids: [WM-06]
  missing_conditions: "争议出现不代表任何一套算法正确，也不证明最后结算失败。"
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
  tags: [historical-fiction, narrative-failure, source-anchored]
- id: ce06
  title: "核心贸易伙伴单点依赖"
  type: counter-example
  source_chapter: "n099/p17;n099/p18;n099/p19"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA
  evidence_kind: DISCOVERED_VULNERABILITY
  source_loci:
    - "n099/p17"
    - "n099/p18"
    - "n099/p19"
  chunk_ids:
    - "ck-35cf27b3b35b"
  summary: |-
    局面：负责人把后续多项经营计划寄托在一位合作伙伴的归来。
    原文可见：看见对方的船只异常后担心对方安危，确认其本人返回才暂时放心；自己也察觉经营对单一关系过于依赖。
    失效边界：最终未发生合作方死亡或长期供给断裂；只能标风险被意识到。
    推断的机制：外部合作方若出意外，主角原以为稳定的收入承诺就可能同步失效。
    状态：这是小说场景中的反例候选，不是作者的真实经历或通用定律。
  failure_mode: "外部合作方若出意外，主角原以为稳定的收入承诺就可能同步失效。"
  mechanism: "原书因果可见：看见对方的船只异常后担心对方安危，确认其本人返回才暂时放心；自己也察觉经营对单一关系过于依赖。；分析解释：外部合作方若出意外，主角原以为稳定的收入承诺就可能同步失效。"
  warning_signs:
    - "一项收入来源撑住多项预算"
    - "伙伴失联时无已确认替代来源。"
  bound_to:
    - "虚构供给承诺与长期因果"
  task_ids: [WM-04, WM-05]
  missing_conditions: "最终未发生合作方死亡或长期供给断裂；只能标风险被意识到。"
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
  tags: [historical-fiction, narrative-failure, source-anchored]
- id: ce07
  title: "紧急排序口号掩盖知情不足"
  type: counter-example
  source_chapter: "n140/p29;n140/p30;n140/p36"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA
  evidence_kind: NARROW_CHARACTER_COUNTERPRESSURE
  source_loci:
    - "n140/p29"
    - "n140/p30"
    - "n140/p36"
  chunk_ids:
    - "ck-034c19edb6d9"
  summary: |-
    局面：公共事务中主角优先接待有权者，并以紧急事项优先解释。
    原文可见：同伴当场不满其忽视家中关切；在另一问题上主角也承认不能确定对方规模，只能估计。
    失效边界：没有证明此处排序已经造成实质灾难，不能把估计数写成确切事实。
    推断的机制：管理口号并不能为一切人物价值排序或不确定判断背书。
    状态：这是小说场景中的反例候选，不是作者的真实经历或通用定律。
  failure_mode: "管理口号并不能为一切人物价值排序或不确定判断背书。"
  mechanism: "原书因果可见：同伴当场不满其忽视家中关切；在另一问题上主角也承认不能确定对方规模，只能估计。；分析解释：管理口号并不能为一切人物价值排序或不确定判断背书。"
  warning_signs:
    - "以口号迅速压过熟人异议"
    - "猜测和已获证实的信息混在同一场。"
  bound_to:
    - "人物伦理分歧;限定视角中的事实口径"
  task_ids: [WM-02, WM-05]
  missing_conditions: "没有证明此处排序已经造成实质灾难，不能把估计数写成确切事实。"
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
  tags: [historical-fiction, narrative-failure, source-anchored]
- id: ce08
  title: "机构裁撤的纸面节省不等于实际财政恢复"
  type: counter-example
  source_chapter: "n155/p28;n155/p30"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA
  evidence_kind: NARRATOR_HISTORICAL_CLAIM_UNVERIFIED
  source_loci:
    - "n155/p28"
    - "n155/p30"
  chunk_ids:
    - "ck-43b81546266f"
  summary: |-
    局面：叙事回望社会变动及行政整顿对普通人的潜在影响。
    原文可见：文本提出某项裁撤的省费主要停留在纸面，并联系到随后更大社会问题。
    失效边界：这是书内叙事判断，未经独立历史史料确认；不能宣称真实史学因果已被证实。
    推断的机制：只列出缩减编制的账面数字，无法自动证明支出已减、失业风险已消失或外部后果可以忽略。
    状态：这是小说场景中的反例候选，不是作者的真实经历或通用定律。
  failure_mode: "只列出缩减编制的账面数字，无法自动证明支出已减、失业风险已消失或外部后果可以忽略。"
  mechanism: "原书因果可见：文本提出某项裁撤的省费主要停留在纸面，并联系到随后更大社会问题。；分析解释：只列出缩减编制的账面数字，无法自动证明支出已减、失业风险已消失或外部后果可以忽略。"
  warning_signs:
    - "把表面裁撤当作到手现款"
    - "完全不描写失去生计的人。"
  bound_to:
    - "制度改变的社会代价;小说财政账的可信程度"
  task_ids: [WM-03, WM-06]
  missing_conditions: "这是书内叙事判断，未经独立历史史料确认；不能宣称真实史学因果已被证实。"
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
  tags: [historical-fiction, narrative-failure, source-anchored]
- id: ce09
  title: "以公共利益为名不等于权利人真实同意"
  type: counter-example
  source_chapter: "n265/p19;n265/p21;n265/p22;n265/p29"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA
  evidence_kind: OBSERVED_COERCIVE_CLAIM
  source_loci:
    - "n265/p19"
    - "n265/p21"
    - "n265/p22"
    - "n265/p29"
  chunk_ids:
    - "ck-956f575fa961"
  summary: |-
    局面：权力人物要求地方官迅速修改资源归属手续，公开强调有利民生。
    原文可见：该人物又承认相关资源实际上由自己控制；地方官在高压关系中表示服从，文本未核实原所有人权益。
    失效边界：不能证明所有产权争议已完成，也不能据此制作现实强制、侵占或规避法律的操作指南。
    推断的机制：拥有正当语言和强势职位的行为，可能与受影响人的知情、授权和实际受益分离。
    状态：这是小说场景中的反例候选，不是作者的真实经历或通用定律。
  failure_mode: "拥有正当语言和强势职位的行为，可能与受影响人的知情、授权和实际受益分离。"
  mechanism: "原书因果可见：该人物又承认相关资源实际上由自己控制；地方官在高压关系中表示服从，文本未核实原所有人权益。；分析解释：拥有正当语言和强势职位的行为，可能与受影响人的知情、授权和实际受益分离。"
  warning_signs:
    - "受影响者未到场"
    - "口头善意替代真实同意"
    - "办理期限与责任无人独立复核。"
  bound_to:
    - "制度合法性叙事;弱势当事人的自主空间"
  task_ids: [WM-03, WM-07]
  missing_conditions: "不能证明所有产权争议已完成，也不能据此制作现实强制、侵占或规避法律的操作指南。"
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
  tags: [historical-fiction, narrative-failure, source-anchored]
- id: ce10
  title: "把预计收益重复投入多个部门"
  type: counter-example
  source_chapter: "n305/p29;n305/p32;n305/p35;n305/p36"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA
  evidence_kind: OBSERVED_BUDGET_CONFLICT
  source_loci:
    - "n305/p29"
    - "n305/p32"
    - "n305/p35"
    - "n305/p36"
  chunk_ids:
    - "ck-2dee35e976d6"
  summary: |-
    局面：组织计划追加人员编制，而其他部门已有在先支出。
    原文可见：负责预算的另一人拿出总账提出异议，双方改变原计划并只达成阶段性妥协。
    失效边界：此章证实现场讨论和缩减，不能证明长远财政危机已解决或所有数字正确。
    推断的机制：决策者误把理论总收益当可无限同时支用的资源，忽略其他必要开销及到账时间。
    状态：这是小说场景中的反例候选，不是作者的真实经历或通用定律。
  failure_mode: "决策者误把理论总收益当可无限同时支用的资源，忽略其他必要开销及到账时间。"
  mechanism: "原书因果可见：负责预算的另一人拿出总账提出异议，双方改变原计划并只达成阶段性妥协。；分析解释：决策者误把理论总收益当可无限同时支用的资源，忽略其他必要开销及到账时间。"
  warning_signs:
    - "多部门同时声称已占用同一笔钱"
    - "计划没有分期"
    - "当场必须修改规模。"
  bound_to:
    - "长篇连续性中的资源限制"
  task_ids: [WM-03, WM-04]
  missing_conditions: "此章证实现场讨论和缩减，不能证明长远财政危机已解决或所有数字正确。"
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
  tags: [historical-fiction, narrative-failure, source-anchored]
- id: ce11
  title: "家庭荣誉与少量救济无法代替独立人生决定"
  type: counter-example
  source_chapter: "n339/p9;n339/p10;n339/p31;n339/p34"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA
  evidence_kind: OBSERVED_PARTIAL_REMEDY
  source_loci:
    - "n339/p9"
    - "n339/p10"
    - "n339/p31"
    - "n339/p34"
  chunk_ids:
    - "ck-312a7425ee02"
  summary: |-
    局面：参与公共事业而受表彰的人回到私人生活场所。
    原文可见：年长亲属替女儿做出决定而本人尚未发言；一个失去家庭劳力的孩子也可能被迫放弃学习，旁人给了有限帮助。
    失效边界：具体资助确实发生，不能抹掉有效行为；长期安排和女孩意愿仍待剧情另证。
    推断的机制：集体荣誉、收入补助与本人同意是三件事；帮助当场发生却不能自动偿清长期教育或家庭责任。
    状态：这是小说场景中的反例候选，不是作者的真实经历或通用定律。
  failure_mode: "集体荣誉、收入补助与本人同意是三件事；帮助当场发生却不能自动偿清长期教育或家庭责任。"
  mechanism: "原书因果可见：年长亲属替女儿做出决定而本人尚未发言；一个失去家庭劳力的孩子也可能被迫放弃学习，旁人给了有限帮助。；分析解释：集体荣誉、收入补助与本人同意是三件事；帮助当场发生却不能自动偿清长期教育或家庭责任。"
  warning_signs:
    - "家属说法代替当事人选择"
    - "一次支援被写成所有后果消失。"
  bound_to:
    - "普通人生命史;战后责任和家庭自主"
  task_ids: [WM-06, WM-08]
  missing_conditions: "具体资助确实发生，不能抹掉有效行为；长期安排和女孩意愿仍待剧情另证。"
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
  tags: [historical-fiction, narrative-failure, source-anchored]
- id: ce12
  title: "压制竞争会诱发忽视实际改进的诱因"
  type: counter-example
  source_chapter: "n380/p25;n380/p27;n380/p28"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA
  evidence_kind: CHARACTER_PREDICTED_RISK
  source_loci:
    - "n380/p25"
    - "n380/p27"
    - "n380/p28"
  chunk_ids:
    - "ck-a38e2cb073f1"
  summary: |-
    局面：商业机构讨论是否进一步吞并生产环节。
    原文可见：主管角色回忆此前有人提出只靠打压对手而非继续开发新品的说法，因此暂未同意把生产体系全交给渠道商。
    失效边界：该段只是人物担忧与一次暂缓决定，未证明企业此后实际停止创新；不引申为现实商业打击技术。
    推断的机制：若企业把既有优势误当永久保障，可能削弱对产品和多方竞争者的持续响应。
    状态：这是小说场景中的反例候选，不是作者的真实经历或通用定律。
  failure_mode: "若企业把既有优势误当永久保障，可能削弱对产品和多方竞争者的持续响应。"
  mechanism: "原书因果可见：主管角色回忆此前有人提出只靠打压对手而非继续开发新品的说法，因此暂未同意把生产体系全交给渠道商。；分析解释：若企业把既有优势误当永久保障，可能削弱对产品和多方竞争者的持续响应。"
  warning_signs:
    - "某一渠道同时控制所有部门的想象"
    - "有人公开主张只靠压制对手。"
  bound_to:
    - "商业结构的叙事风险;配角自主与利益冲突"
  task_ids: [WM-04, WM-07]
  missing_conditions: "该段只是人物担忧与一次暂缓决定，未证明企业此后实际停止创新；不引申为现实商业打击技术。"
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
  tags: [historical-fiction, narrative-failure, source-anchored]
- id: ce13
  title: "基层负责人集资源权与监督权的隐藏成本"
  type: counter-example
  source_chapter: "n425/p25;n425/p26;n425/p35;n425/p40"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA
  evidence_kind: OBSERVED_COMPLAINT_AND_OPEN_DESIGN
  source_loci:
    - "n425/p25"
    - "n425/p26"
    - "n425/p35"
    - "n425/p40"
  chunk_ids:
    - "ck-507de61e85d6"
  summary: |-
    局面：原来被认为熟练稳定的基层体系持续扩大职责。
    原文可见：监督部门尚有部分资源分配投诉未处理完，领导提出收权；另几位管理者为如何分配新职责讨论许久仍无定论。
    失效边界：投诉与少量处理可以确认，但对全部基层干部的怀疑是角色推测；分权方案还没落实。
    推断的机制：组织既有绩效不能消除岗位权力与个人利益之间的张力；提出改革并非改革已经执行。
    状态：这是小说场景中的反例候选，不是作者的真实经历或通用定律。
  failure_mode: "组织既有绩效不能消除岗位权力与个人利益之间的张力；提出改革并非改革已经执行。"
  mechanism: "原书因果可见：监督部门尚有部分资源分配投诉未处理完，领导提出收权；另几位管理者为如何分配新职责讨论许久仍无定论。；分析解释：组织既有绩效不能消除岗位权力与个人利益之间的张力；提出改革并非改革已经执行。"
  warning_signs:
    - "发生资源投诉后仍声称制度完全无缺陷"
    - "部门分工没有实际负责人。"
  bound_to:
    - "虚构制度监督;权责边界的写法"
  task_ids: [WM-03, WM-07]
  missing_conditions: "投诉与少量处理可以确认，但对全部基层干部的怀疑是角色推测；分权方案还没落实。"
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
  tags: [historical-fiction, narrative-failure, source-anchored]
- id: ce14
  title: "新技术设想不等于可用成果"
  type: counter-example
  source_chapter: "n437/p6;n437/p29;n437/p30"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA
  evidence_kind: OBSERVED_PROPOSAL_REJECTION
  source_loci:
    - "n437/p6"
    - "n437/p29"
    - "n437/p30"
  chunk_ids:
    - "ck-dff261ebc036"
  summary: |-
    局面：一位掌权人物每年尝试提出新构思，机构负责论证。
    原文可见：一个新构思被研究部门判断不具优势并否决；后来他再提出新合同关系时，执行者当场困惑。
    失效边界：只研究故事里的评审与人员理解，不涉及器械技术、真实制造或组织压迫的可执行步骤。
    推断的机制：构想、审核、认可和实际交付必须是不同状态，人物声望不能免除负面反馈。
    状态：这是小说场景中的反例候选，不是作者的真实经历或通用定律。
  failure_mode: "构想、审核、认可和实际交付必须是不同状态，人物声望不能免除负面反馈。"
  mechanism: "原书因果可见：一个新构思被研究部门判断不具优势并否决；后来他再提出新合同关系时，执行者当场困惑。；分析解释：构想、审核、认可和实际交付必须是不同状态，人物声望不能免除负面反馈。"
  warning_signs:
    - "刚提出想法就称完成"
    - "一个职位变更就宣称合同制已有效运转。"
  bound_to:
    - "现代知识在历史环境中的失效支路"
  task_ids: [WM-03, WM-04]
  missing_conditions: "只研究故事里的评审与人员理解，不涉及器械技术、真实制造或组织压迫的可执行步骤。"
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
  tags: [historical-fiction, narrative-failure, source-anchored]
- id: ce15
  title: "从组织总体利益推算的安置政策可能忽视个人意愿"
  type: counter-example
  source_chapter: "n494/p8;n494/p11;n494/p18"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA
  evidence_kind: ANTICIPATED_PARTICIPANT_FRICTION
  source_loci:
    - "n494/p8"
    - "n494/p11"
    - "n494/p18"
  chunk_ids:
    - "ck-033094aa0c57"
  summary: |-
    局面：管理者认为让成员迁居另一个地方对组织和个人都有长远好处。
    原文可见：另一人物提醒已有家庭与生活基础的人未必愿意搬迁，且被迫失去旧待遇会引起不满；随后其他管理者又指出不同地点的资源承载有上限。
    失效边界：场景主要是政策争论和预判，未证明所有成员已经拒绝或迁居失败。
    推断的机制：组织层面的便利与具体人的选择、福利、居住成本不等价。
    状态：这是小说场景中的反例候选，不是作者的真实经历或通用定律。
  failure_mode: "组织层面的便利与具体人的选择、福利、居住成本不等价。"
  mechanism: "原书因果可见：另一人物提醒已有家庭与生活基础的人未必愿意搬迁，且被迫失去旧待遇会引起不满；随后其他管理者又指出不同地点的资源承载有上限。；分析解释：组织层面的便利与具体人的选择、福利、居住成本不等价。"
  warning_signs:
    - "从高层“划算”直接跳到全体自愿"
    - "转移计划没有估计家庭承受条件。"
  bound_to:
    - "个人选择对组织扩大的限制"
  task_ids: [WM-03, WM-08]
  missing_conditions: "场景主要是政策争论和预判，未证明所有成员已经拒绝或迁居失败。"
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
  tags: [historical-fiction, narrative-failure, source-anchored]
- id: ce16
  title: "惊慌报告中的数字膨胀"
  type: counter-example
  source_chapter: "n506/p45;n506/p46"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA
  evidence_kind: OBSERVED_REPORT_CORRECTION
  source_loci:
    - "n506/p45"
    - "n506/p46"
  chunk_ids:
    - "ck-6d4164c5cb21"
  summary: |-
    局面：受惊的报信者向上级描述刚才观察到的数量。
    原文可见：报信者用极宽泛的巨大数字作陈述，接受报告的人当场要求其不要把听闻和目测夸大。
    失效边界：纠正了表述不等于现场实际规模已查证；只提取写作中的信息边界，不涉及现实侦察。
    推断的机制：强烈情绪易使角色把尚未确认的局部见闻包装成完整事实。
    状态：这是小说场景中的反例候选，不是作者的真实经历或通用定律。
  failure_mode: "强烈情绪易使角色把尚未确认的局部见闻包装成完整事实。"
  mechanism: "原书因果可见：报信者用极宽泛的巨大数字作陈述，接受报告的人当场要求其不要把听闻和目测夸大。；分析解释：强烈情绪易使角色把尚未确认的局部见闻包装成完整事实。"
  warning_signs:
    - "使用无边界的大数词"
    - "来源不清却先要求他人相信。"
  bound_to:
    - "限知视角;证言与叙事可靠性"
  task_ids: [WM-05, WM-09]
  missing_conditions: "纠正了表述不等于现场实际规模已查证；只提取写作中的信息边界，不涉及现实侦察。"
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
  tags: [historical-fiction, narrative-failure, source-anchored]
- id: ce17
  title: "新制度引入后未必产生预想中的共同价值观"
  type: counter-example
  source_chapter: "n519/p66;n519/p67;n519/p69;n519/p70;n520/p15;n520/p17"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA
  evidence_kind: OBSERVED_UNEXPECTED_VERDICT
  source_loci:
    - "n519/p66"
    - "n519/p67"
    - "n519/p69"
    - "n519/p70"
    - "n520/p15"
    - "n520/p17"
  chunk_ids:
    - "ck-a7e713d93ef2"
    - "ck-9cf793319d6f"
    - "ck-d005282755fd"
  summary: |-
    局面：熟悉旧法律程序的人对试办制度里的普通参与者有强烈预期。
    原文可见：普通参与者作出不同于主角预期的回答并说明其个人生活理由，之后两位改革者争论制度是否应推广，只同意继续小范围试办。
    失效边界：有独立意见不等于法律结论正确或制度全面失败；试点许可不是有效性的终局判决。
    推断的机制：制度程序的外形不自动决定参与者使用何种伦理标准，也不能免去后续检验。
    状态：这是小说场景中的反例候选，不是作者的真实经历或通用定律。
  failure_mode: "制度程序的外形不自动决定参与者使用何种伦理标准，也不能免去后续检验。"
  mechanism: "原书因果可见：普通参与者作出不同于主角预期的回答并说明其个人生活理由，之后两位改革者争论制度是否应推广，只同意继续小范围试办。；分析解释：制度程序的外形不自动决定参与者使用何种伦理标准，也不能免去后续检验。"
  warning_signs:
    - "主角预先判定所有人将同样理解正义"
    - "把要求说出理由当作理由已经正确。"
  bound_to:
    - "多方价值冲突;制度改革与未结责任"
  task_ids: [WM-02, WM-07]
  missing_conditions: "有独立意见不等于法律结论正确或制度全面失败；试点许可不是有效性的终局判决。"
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
  tags: [historical-fiction, narrative-failure, source-anchored]
- id: ce18
  title: "频繁改动部门需求会积累隐形时间成本"
  type: counter-example
  source_chapter: "n529/p38;n529/p40;n529/p41"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA
  evidence_kind: OBSERVED_INTERDEPARTMENT_CONFLICT
  source_loci:
    - "n529/p38"
    - "n529/p40"
    - "n529/p41"
  chunk_ids:
    - "ck-819d088ba528"
  summary: |-
    局面：多个部门正在处理已经排定的运输与物资供给计划。
    原文可见：一项临时统计尚不能确定真实需求，另一项人员时程却反复变动；负责排期的人当场抗议造成多项其他任务重新安排。
    失效边界：只证明现场实际抱怨和重排风险，后来的真实交付日期未在选定段落得到验证。
    推断的机制：只看提出需求者的便利而无视其他部门此前承诺，会使故事中原本可用的时间与资源互相争夺。
    状态：这是小说场景中的反例候选，不是作者的真实经历或通用定律。
  failure_mode: "只看提出需求者的便利而无视其他部门此前承诺，会使故事中原本可用的时间与资源互相争夺。"
  mechanism: "原书因果可见：一项临时统计尚不能确定真实需求，另一项人员时程却反复变动；负责排期的人当场抗议造成多项其他任务重新安排。；分析解释：只看提出需求者的便利而无视其他部门此前承诺，会使故事中原本可用的时间与资源互相争夺。"
  warning_signs:
    - "计划改动被当成无需成本的口头指令"
    - "执行者反复等候与重新排期。"
  bound_to:
    - "跨章承诺的可追责性;组织时间账"
  task_ids: [WM-03, WM-04]
  missing_conditions: "只证明现场实际抱怨和重排风险，后来的真实交付日期未在选定段落得到验证。"
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
  tags: [historical-fiction, narrative-failure, source-anchored]
- id: ce19
  title: "迎合听众会把独立合作者压缩成单一英雄"
  type: counter-example
  source_chapter: "n571/p5;n571/p20;n571/p25;n571/p26"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA
  evidence_kind: OBSERVED_AUDIENCE_PRESSURE
  source_loci:
    - "n571/p5"
    - "n571/p20"
    - "n571/p25"
    - "n571/p26"
  chunk_ids:
    - "ck-e9d40a8c080f"
  summary: |-
    局面：多年后的公开讲述会受到听众个人偏好的影响。
    原文可见：现场有人鼓励夸张改变人物命运，也有人反对；另有人明确建议少讲原来另一位重要合作者，只突出更受欢迎的一个人。
    失效边界：这仍是茶客建议，不能假称说书人已照办；不得复制原书独有结尾场景。
    推断的机制：二手讲述的受众压力可能重排事件主角和道德评价，却无法改变原先场景本身曾如何呈现。
    状态：这是小说场景中的反例候选，不是作者的真实经历或通用定律。
  failure_mode: "二手讲述的受众压力可能重排事件主角和道德评价，却无法改变原先场景本身曾如何呈现。"
  mechanism: "原书因果可见：现场有人鼓励夸张改变人物命运，也有人反对；另有人明确建议少讲原来另一位重要合作者，只突出更受欢迎的一个人。；分析解释：二手讲述的受众压力可能重排事件主角和道德评价，却无法改变原先场景本身曾如何呈现。"
  warning_signs:
    - "讲故事只听市场掌声"
    - "多人的真实贡献被简化到一个受欢迎的人物。"
  bound_to:
    - "历史回声与叙事可靠性;合作者主体性"
  task_ids: [WM-02, WM-09]
  missing_conditions: "这仍是茶客建议，不能假称说书人已照办；不得复制原书独有结尾场景。"
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
  tags: [historical-fiction, narrative-failure, source-anchored]
```

## 原版方法与小说体裁的责任边界

原版Counter-Example提取器针对“作者告诫的错误”与亲身事实。本书是小说，并不以人物论断代替作者规范。本轮逐条附`evidence_kind`，把已观察的争议/局部损失与**人物预测、叙述者历史断言、尚未执行的提议**分开；未见后果的情况不做结果证明，也不把一般道德批判冒充机制。

严格按`source_loci`回到私有原始EPUB；R042旧14条问题机制继续隔离，尤其n143旧错误单段不得直接晋级。WM-01—WM-09九项均有关联，不等于能力覆盖获证。作者原文与特有场面不复制进最终原创写作。

本文件仅Stage1反例候选，Stage1.5三重验证、Nuwa、C原创盲测均未执行。原版权文字未上传，B PROVISIONAL，C NOT_RUN，SKILL认证0。
