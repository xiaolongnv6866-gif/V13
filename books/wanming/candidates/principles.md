# 《晚明》Stage1 原则提取器｜原始候选（R044）

原版依据：Cangjie `methodology/02-stage1-parallel-extract.md` + `extractors/principle-extractor.md`，从原始EPUB独立重读、逐章扫描后提出。**不是已通过Stage1.5的规则，也不是作者亲自颁布的23条原则。** 人物规范性表态与研究者可疑的文学规则严格分开。原著版权正文不公开，因此`source_quote`保留原版字段但为空，定位/段落SHA见`PRINCIPLE_EVIDENCE.tsv`。原书页脚、正文附注随真实XHTML扫描；现无足以宣称作者给出独立且核实的通用数学公式。

```yaml
- id: p01
  title: "拒绝收益不等于同意交易"
  type: principle
  source_chapter: "n034/p18；n034/p43"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA
  source_loci:
    - "n034/p18"
    - "n034/p43"
  summary: |-
    原著场面：刘民有当面拒绝参与一项不认可的获利分配，交易建议仍被他人继续提出。
    候选规则：只有表达明确拒绝，不可由熟人关系推出该人赞成其余交易安排。
    解释性质：CHARACTER_NORMATIVE；不是作者公开的方法论宣言。
    边界：不等于刘民有在所有时刻都遵守相同伦理底线。
    后续核查：角色拒绝与他人促销方案的冲突；非作者直接提出的经营准则。
  tags: [narrative-rule, historical-fiction, source-audited]
  task_ids: [WM-02, WM-04]
  provenance: CHARACTER_NORMATIVE
  source_observation: "刘民有当面拒绝参与一项不认可的获利分配，交易建议仍被他人继续提出。"
  rule_scope: "只有表达明确拒绝，不可由熟人关系推出该人赞成其余交易安排。"
  counterexample_or_limit: "不等于刘民有在所有时刻都遵守相同伦理底线。"
  missing_conditions: "角色拒绝与他人促销方案的冲突；非作者直接提出的经营准则。"
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
- id: p02
  title: "收付款角色的信任不由口头关系保证"
  type: principle
  source_chapter: "n048/p17；n099/p18"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA
  source_loci:
    - "n048/p17"
    - "n099/p18"
  summary: |-
    原著场面：当事人认为某个朋友独管款项会出问题；另一处则显示经营者担心关键伙伴失去供给能力。
    候选规则：在虚构经营线中，必须把角色的信任主张和资金实际能否由谁支配分开叙述。
    解释性质：NARRATIVE_INFERENCE；不是作者公开的方法论宣言。
    边界：这只是人物的顾虑，不得扩大为该人物已实施可靠的财务监督。
    后续核查：还需查询相关人物后续如何处理账目，暂列源性推断。
  tags: [narrative-rule, historical-fiction, source-audited]
  task_ids: [WM-02, WM-04]
  provenance: NARRATIVE_INFERENCE
  source_observation: "当事人认为某个朋友独管款项会出问题；另一处则显示经营者担心关键伙伴失去供给能力。"
  rule_scope: "在虚构经营线中，必须把角色的信任主张和资金实际能否由谁支配分开叙述。"
  counterexample_or_limit: "这只是人物的顾虑，不得扩大为该人物已实施可靠的财务监督。"
  missing_conditions: "还需查询相关人物后续如何处理账目，暂列源性推断。"
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
- id: p03
  title: "承担新工作前应让角色知道实际代价"
  type: rule
  source_chapter: "n052/p24；n022/p20"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA
  source_loci:
    - "n052/p24"
    - "n022/p20"
  summary: |-
    原著场面：角色谈及加入某项危险工作时，明确提出分批和预先告知风险；另一场景有人担忧向东家说话的后果。
    候选规则：人物在作决定前有没有真实理解成本，与其当场说愿意须分开。
    解释性质：CHARACTER_NORMATIVE_LIMITED；不是作者公开的方法论宣言。
    边界：原场景是带权力差的招募，不等于任何同意都完全自愿，亦非现实招募指南。
    后续核查：只移植叙事中的知情范围与后果延续，不提供危险组织操作步骤。
  tags: [narrative-rule, historical-fiction, source-audited]
  task_ids: [WM-01, WM-08]
  provenance: CHARACTER_NORMATIVE_LIMITED
  source_observation: "角色谈及加入某项危险工作时，明确提出分批和预先告知风险；另一场景有人担忧向东家说话的后果。"
  rule_scope: "人物在作决定前有没有真实理解成本，与其当场说愿意须分开。"
  counterexample_or_limit: "原场景是带权力差的招募，不等于任何同意都完全自愿，亦非现实招募指南。"
  missing_conditions: "只移植叙事中的知情范围与后果延续，不提供危险组织操作步骤。"
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
- id: p04
  title: "不同贡献口径不能被称为自然共识"
  type: principle
  source_chapter: "n085/p25；n085/p29"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA
  source_loci:
    - "n085/p25"
    - "n085/p29"
  summary: |-
    原著场面：集体行动后，各方分别以损失、人数和贡献声称分配资格，人物相互争执。
    候选规则：写公开结算时必须让分配口径和反对人可见；未采纳者的异议不能消失。
    解释性质：NARRATIVE_INFERENCE；不是作者公开的方法论宣言。
    边界：争论存在只证明意见冲突，不证明其中任何一个算法公允。
    后续核查：源为受益者彼此争论，不是作者给出的分配公式。
  tags: [narrative-rule, historical-fiction, source-audited]
  task_ids: [WM-06]
  provenance: NARRATIVE_INFERENCE
  source_observation: "集体行动后，各方分别以损失、人数和贡献声称分配资格，人物相互争执。"
  rule_scope: "写公开结算时必须让分配口径和反对人可见；未采纳者的异议不能消失。"
  counterexample_or_limit: "争论存在只证明意见冲突，不证明其中任何一个算法公允。"
  missing_conditions: "源为受益者彼此争论，不是作者给出的分配公式。"
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
- id: p05
  title: "预计收入不能提前当作现款"
  type: rule
  source_chapter: "n099/p18；n109/p13；n109/p18"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA
  source_loci:
    - "n099/p18"
    - "n109/p13"
    - "n109/p18"
  summary: |-
    原著场面：人物承认对交易伙伴高度依赖；一段财务盘算显示大量投入后手边不足，另一段仍在期待下一批货物回来。
    候选规则：预计到款与已经在手的款项必须有不同故事状态。
    解释性质：NARRATIVE_INFERENCE；不是作者公开的方法论宣言。
    边界：源小说场景有估算与预计，未提供可通用的真实利润率。
    后续核查：仅用于虚构资源连续性，禁止作现实投融资公式。
  tags: [narrative-rule, historical-fiction, source-audited]
  task_ids: [WM-03, WM-04]
  provenance: NARRATIVE_INFERENCE
  source_observation: "人物承认对交易伙伴高度依赖；一段财务盘算显示大量投入后手边不足，另一段仍在期待下一批货物回来。"
  rule_scope: "预计到款与已经在手的款项必须有不同故事状态。"
  counterexample_or_limit: "源小说场景有估算与预计，未提供可通用的真实利润率。"
  missing_conditions: "仅用于虚构资源连续性，禁止作现实投融资公式。"
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
- id: p06
  title: "紧急与重要的先后说法须限定场景"
  type: principle
  source_chapter: "n140/p30；n140/p36"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA
  source_loci:
    - "n140/p30"
    - "n140/p36"
  summary: |-
    原著场面：人物直接提出一条先处理眼前紧急事项的排序说法，随后仍需面对情报不完整。
    候选规则：只能把这当作特定角色临时安排时间的主张，不写成作者证实的万能优先级算法。
    解释性质：CHARACTER_NORMATIVE；不是作者公开的方法论宣言。
    边界：某些重要事项不能被无限推后；故事中也没有对全部事项做完整矩阵测算。
    后续核查：原则存在于人物台词，不把它归为作者公开的工作法。
  tags: [narrative-rule, historical-fiction, source-audited]
  task_ids: [WM-05, WM-08]
  provenance: CHARACTER_NORMATIVE
  source_observation: "人物直接提出一条先处理眼前紧急事项的排序说法，随后仍需面对情报不完整。"
  rule_scope: "只能把这当作特定角色临时安排时间的主张，不写成作者证实的万能优先级算法。"
  counterexample_or_limit: "某些重要事项不能被无限推后；故事中也没有对全部事项做完整矩阵测算。"
  missing_conditions: "原则存在于人物台词，不把它归为作者公开的工作法。"
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
- id: p07
  title: "未知数量保留估计身份"
  type: rule
  source_chapter: "n140/p36；n506/p46"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA
  source_loci:
    - "n140/p36"
    - "n506/p46"
  summary: |-
    原著场面：角色一处承认不知道确数，只给估计；另一处有人提醒汇报者不要把有限观察夸张成庞大数字。
    候选规则：当场见闻、传闻估计、事后证实应在文本叙事中分别表达。
    解释性质：CHARACTER_NORMATIVE_AND_INFERENCE；不是作者公开的方法论宣言。
    边界：不能用角色训话证明其本人此后绝不误报，且不用于现实侦察。
    后续核查：本条强调可信叙述而非现实战场数量推算。
  tags: [narrative-rule, historical-fiction, source-audited]
  task_ids: [WM-05, WM-09]
  provenance: CHARACTER_NORMATIVE_AND_INFERENCE
  source_observation: "角色一处承认不知道确数，只给估计；另一处有人提醒汇报者不要把有限观察夸张成庞大数字。"
  rule_scope: "当场见闻、传闻估计、事后证实应在文本叙事中分别表达。"
  counterexample_or_limit: "不能用角色训话证明其本人此后绝不误报，且不用于现实侦察。"
  missing_conditions: "本条强调可信叙述而非现实战场数量推算。"
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
- id: p08
  title: "被上级否决的提议不能伪作已获授权"
  type: rule
  source_chapter: "n143/p49；n143/p52；n143/p55"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA
  source_loci:
    - "n143/p49"
    - "n143/p52"
    - "n143/p55"
  summary: |-
    原著场面：角色提出不同任务建议，掌权者明确另有安排，提出者最终退让。
    候选规则：叙事应将提出建议、收到决定、实际执行三个事实层次分离。
    解释性质：NARRATIVE_INFERENCE；不是作者公开的方法论宣言。
    边界：相关决定不等于后续所有执行均完成；原旧R013错误p29只能证明人员入座。
    后续核查：本候选以R042纠错后的真实后段证据支撑。
  tags: [narrative-rule, historical-fiction, source-audited]
  task_ids: [WM-01, WM-03]
  provenance: NARRATIVE_INFERENCE
  source_observation: "角色提出不同任务建议，掌权者明确另有安排，提出者最终退让。"
  rule_scope: "叙事应将提出建议、收到决定、实际执行三个事实层次分离。"
  counterexample_or_limit: "相关决定不等于后续所有执行均完成；原旧R013错误p29只能证明人员入座。"
  missing_conditions: "本候选以R042纠错后的真实后段证据支撑。"
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
- id: p09
  title: "纸面压缩不必然兑现现金节约"
  type: principle
  source_chapter: "n155/p30；n305/p29"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA
  source_loci:
    - "n155/p30"
    - "n305/p29"
  summary: |-
    原著场面：角色评价一项行政裁撤的节余仍停在纸面，后文另一场同时为部门支出争执。
    候选规则：纸面减少编制、实际支出降低以及节省款被转用需分开写。
    解释性质：NARRATIVE_INFERENCE；不是作者公开的方法论宣言。
    边界：前段有现代知识与人物自己的因果推断；不能把它当作未经外证的历史财政定论。
    后续核查：规则由叙事比较得出，非明代财政史已核实事实。
  tags: [narrative-rule, historical-fiction, source-audited]
  task_ids: [WM-03, WM-06]
  provenance: NARRATIVE_INFERENCE
  source_observation: "角色评价一项行政裁撤的节余仍停在纸面，后文另一场同时为部门支出争执。"
  rule_scope: "纸面减少编制、实际支出降低以及节省款被转用需分开写。"
  counterexample_or_limit: "前段有现代知识与人物自己的因果推断；不能把它当作未经外证的历史财政定论。"
  missing_conditions: "规则由叙事比较得出，非明代财政史已核实事实。"
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
- id: p10
  title: "事多必错是组织角色的主张而非免责卡"
  type: principle
  source_chapter: "n222/p28；n390/p25"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA
  source_loci:
    - "n222/p28"
    - "n390/p25"
  summary: |-
    原著场面：上级安慰犯错者并提到工作多会出错；另处指出此前看过方案也难发现微小遗漏。
    候选规则：写管理者评语时，应保留是否修正问题以及工作者实际承担什么。
    解释性质：CHARACTER_NORMATIVE；不是作者公开的方法论宣言。
    边界：不可据此推出所有失误都无需追责，也不能把不工作写成合理答案。
    后续核查：只研究责任对白如何塑造角色关系。
  tags: [narrative-rule, historical-fiction, source-audited]
  task_ids: [WM-03, WM-07]
  provenance: CHARACTER_NORMATIVE
  source_observation: "上级安慰犯错者并提到工作多会出错；另处指出此前看过方案也难发现微小遗漏。"
  rule_scope: "写管理者评语时，应保留是否修正问题以及工作者实际承担什么。"
  counterexample_or_limit: "不可据此推出所有失误都无需追责，也不能把不工作写成合理答案。"
  missing_conditions: "只研究责任对白如何塑造角色关系。"
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
- id: p11
  title: "条例中的数字须带作用范围"
  type: checklist
  source_chapter: "n295/p3；n425/p40"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA
  source_loci:
    - "n295/p3"
    - "n425/p40"
  summary: |-
    原著场面：一处城内守备章程出现具体负责单位和对应项目，另一处角色列出事务、资金、人员、资产几类分工。
    候选规则：小说若引用制度条款，至少区分适用谁、管理什么、何时生效和谁实际检查。
    解释性质：FICTIONAL_INSTITUTION_LIST；不是作者公开的方法论宣言。
    边界：书中的具体历史数字尚无外部史料核实，不搬用为现实应急制度或法定标准。
    后续核查：所列项目是人物的虚构制度材料，审计字段是研究者追加。
  tags: [narrative-rule, historical-fiction, source-audited]
  task_ids: [WM-07]
  provenance: FICTIONAL_INSTITUTION_LIST
  source_observation: "一处城内守备章程出现具体负责单位和对应项目，另一处角色列出事务、资金、人员、资产几类分工。"
  rule_scope: "小说若引用制度条款，至少区分适用谁、管理什么、何时生效和谁实际检查。"
  counterexample_or_limit: "书中的具体历史数字尚无外部史料核实，不搬用为现实应急制度或法定标准。"
  missing_conditions: "所列项目是人物的虚构制度材料，审计字段是研究者追加。"
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
- id: p12
  title: "多个部门不能同时花掉同一笔预算"
  type: rule
  source_chapter: "n305/p29；n305/p32"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA
  source_loci:
    - "n305/p29"
    - "n305/p32"
  summary: |-
    原著场面：民事负责人拿出账册与军事提案相冲突，接着双方实际计算缩减的草案。
    候选规则：叙述承诺时，每项钱的可用余额要反映所有互相竞争的用途。
    解释性质：NARRATIVE_INFERENCE；不是作者公开的方法论宣言。
    边界：章节没有证明预测资源一定到账，不能据此建立现实会计准则。
    后续核查：原著是争论事件，原则是服务写作的条件性提炼。
  tags: [narrative-rule, historical-fiction, source-audited]
  task_ids: [WM-03, WM-04]
  provenance: NARRATIVE_INFERENCE
  source_observation: "民事负责人拿出账册与军事提案相冲突，接着双方实际计算缩减的草案。"
  rule_scope: "叙述承诺时，每项钱的可用余额要反映所有互相竞争的用途。"
  counterexample_or_limit: "章节没有证明预测资源一定到账，不能据此建立现实会计准则。"
  missing_conditions: "原著是争论事件，原则是服务写作的条件性提炼。"
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
- id: p13
  title: "暂时同意不等于永久执行"
  type: rule
  source_chapter: "n305/p35；n305/p36；n520/p17"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA
  source_loci:
    - "n305/p35"
    - "n305/p36"
    - "n520/p17"
  summary: |-
    原著场面：一场预算争执双方只勉强接受阶段方案；另一场制度讨论也仅允许受限试点。
    候选规则：一旦文本使用暂行、以后再议或附条件的答复，后续必须保留待复查状态。
    解释性质：NARRATIVE_INFERENCE；不是作者公开的方法论宣言。
    边界：不据此声称全书每项暂行决定后来都失败；判断限定这两场。
    后续核查：原版框架后续再比较，不提前归并成f类可执行模型。
  tags: [narrative-rule, historical-fiction, source-audited]
  task_ids: [WM-03, WM-07]
  provenance: NARRATIVE_INFERENCE
  source_observation: "一场预算争执双方只勉强接受阶段方案；另一场制度讨论也仅允许受限试点。"
  rule_scope: "一旦文本使用暂行、以后再议或附条件的答复，后续必须保留待复查状态。"
  counterexample_or_limit: "不据此声称全书每项暂行决定后来都失败；判断限定这两场。"
  missing_conditions: "原版框架后续再比较，不提前归并成f类可执行模型。"
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
- id: p14
  title: "家属主张不能代替本人意愿"
  type: principle
  source_chapter: "n339/p9；n339/p10；n339/p31"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA
  source_loci:
    - "n339/p9"
    - "n339/p10"
    - "n339/p31"
  summary: |-
    原著场面：一人担忧妹妹的意愿，长辈以惯例拒绝考虑；相邻场景又有少年对教育的真实困难发言。
    候选规则：叙述一个家庭决定时，必须区分本人实际说法、他人的期望和未被听见的愿望。
    解释性质：NARRATIVE_ETHICAL_CHECK；不是作者公开的方法论宣言。
    边界：这是读者对权力不平等的审问，不是小说长辈认可此准则。
    后续核查：缺本人回应的场景只能标未决。
  tags: [narrative-rule, historical-fiction, source-audited]
  task_ids: [WM-08]
  provenance: NARRATIVE_ETHICAL_CHECK
  source_observation: "一人担忧妹妹的意愿，长辈以惯例拒绝考虑；相邻场景又有少年对教育的真实困难发言。"
  rule_scope: "叙述一个家庭决定时，必须区分本人实际说法、他人的期望和未被听见的愿望。"
  counterexample_or_limit: "这是读者对权力不平等的审问，不是小说长辈认可此准则。"
  missing_conditions: "缺本人回应的场景只能标未决。"
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
- id: p15
  title: "批准过方案不保证领会每项细节"
  type: principle
  source_chapter: "n390/p25；n494/p17"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA
  source_loci:
    - "n390/p25"
    - "n494/p17"
  summary: |-
    原著场面：负责人曾细读方案却未察觉一个具体小问题；后段又有属员质疑大规模方案的资源取向。
    候选规则：把事前批准、现场出现的差值和事后追问分开。
    解释性质：NARRATIVE_INFERENCE；不是作者公开的方法论宣言。
    边界：不能反推所有具体错误都应由上级背负，亦不能转成实用军事训练方法。
    后续核查：可移植的是有限注意力的文学真实性。
  tags: [narrative-rule, historical-fiction, source-audited]
  task_ids: [WM-03, WM-05]
  provenance: NARRATIVE_INFERENCE
  source_observation: "负责人曾细读方案却未察觉一个具体小问题；后段又有属员质疑大规模方案的资源取向。"
  rule_scope: "把事前批准、现场出现的差值和事后追问分开。"
  counterexample_or_limit: "不能反推所有具体错误都应由上级背负，亦不能转成实用军事训练方法。"
  missing_conditions: "可移植的是有限注意力的文学真实性。"
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
- id: p16
  title: "基层管理者权力边界要有人明确反对"
  type: principle
  source_chapter: "n425/p27；n425/p40"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA
  source_loci:
    - "n425/p27"
    - "n425/p40"
  summary: |-
    原著场面：角色明确反对把物资裁量全交基层负责人，另一个人在争议后提出类别分工。
    候选规则：权力调整必须写清由谁提出、谁可能失权、谁能质疑。
    解释性质：CHARACTER_NORMATIVE；不是作者公开的方法论宣言。
    边界：某角色的观点不等于改革确实公平；几名负责人甚至尚未谈成具体边界。
    后续核查：源自人物的改革主张而非已生效的法律。
  tags: [narrative-rule, historical-fiction, source-audited]
  task_ids: [WM-07]
  provenance: CHARACTER_NORMATIVE
  source_observation: "角色明确反对把物资裁量全交基层负责人，另一个人在争议后提出类别分工。"
  rule_scope: "权力调整必须写清由谁提出、谁可能失权、谁能质疑。"
  counterexample_or_limit: "某角色的观点不等于改革确实公平；几名负责人甚至尚未谈成具体边界。"
  missing_conditions: "源自人物的改革主张而非已生效的法律。"
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
- id: p17
  title: "事务、资金、人员、资产是场内讨论项"
  type: checklist
  source_chapter: "n425/p40；n425/p35"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA
  source_loci:
    - "n425/p40"
    - "n425/p35"
  summary: |-
    原著场面：角色为一场部门争执指出四类需要协商的事项，之前实际争论并没有顺利完成。
    候选规则：将这四项视为该场会议的检查清单而非普世管理四要素。
    解释性质：CHARACTER_LIST；不是作者公开的方法论宣言。
    边界：来源没有明确的审批表字段、阈值、签署人及实施效果，不能补成完整制度模板。
    后续核查：缺字段的清单按原版提取器要求标missing_conditions。
  tags: [narrative-rule, historical-fiction, source-audited]
  task_ids: [WM-03, WM-07]
  provenance: CHARACTER_LIST
  source_observation: "角色为一场部门争执指出四类需要协商的事项，之前实际争论并没有顺利完成。"
  rule_scope: "将这四项视为该场会议的检查清单而非普世管理四要素。"
  counterexample_or_limit: "来源没有明确的审批表字段、阈值、签署人及实施效果，不能补成完整制度模板。"
  missing_conditions: "缺字段的清单按原版提取器要求标missing_conditions。"
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
- id: p18
  title: "新设想经比较后可以被拒绝"
  type: principle
  source_chapter: "n437/p6；n345/p29"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA
  source_loci:
    - "n437/p6"
    - "n345/p29"
  summary: |-
    原著场面：一处小说中技术新案被评价后未获采纳；另一处有商场外部模仿带来的不利局面。
    候选规则：表现人物创新时，不得由提出或拥有现代知识直接跳到成功。
    解释性质：NARRATIVE_INFERENCE；不是作者公开的方法论宣言。
    边界：不把原著涉及危险器械的内容、生产数据或竞争性伤害转成实施说明。
    后续核查：文学约束只保留可否认的结果与人物责任。
  tags: [narrative-rule, historical-fiction, source-audited]
  task_ids: [WM-04, WM-07]
  provenance: NARRATIVE_INFERENCE
  source_observation: "一处小说中技术新案被评价后未获采纳；另一处有商场外部模仿带来的不利局面。"
  rule_scope: "表现人物创新时，不得由提出或拥有现代知识直接跳到成功。"
  counterexample_or_limit: "不把原著涉及危险器械的内容、生产数据或竞争性伤害转成实施说明。"
  missing_conditions: "文学约束只保留可否认的结果与人物责任。"
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
- id: p19
  title: "证词的数字不应越过所见范围"
  type: rule
  source_chapter: "n506/p46；n140/p36"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA
  source_loci:
    - "n506/p46"
    - "n140/p36"
  summary: |-
    原著场面：人物直接要求报告者避免用超大、无从核实的数目代替自己所见，前章也展示估算的不确定。
    候选规则：有不完全目击只报相应范围，未目击部分单独标猜想；不提供实际侦察指引。
    解释性质：CHARACTER_NORMATIVE；不是作者公开的方法论宣言。
    边界：报告人的训话并不足以证明每次记录都精准。
    后续核查：本候选是文学信息口径规则。
  tags: [narrative-rule, historical-fiction, source-audited]
  task_ids: [WM-05, WM-09]
  provenance: CHARACTER_NORMATIVE
  source_observation: "人物直接要求报告者避免用超大、无从核实的数目代替自己所见，前章也展示估算的不确定。"
  rule_scope: "有不完全目击只报相应范围，未目击部分单独标猜想；不提供实际侦察指引。"
  counterexample_or_limit: "报告人的训话并不足以证明每次记录都精准。"
  missing_conditions: "本候选是文学信息口径规则。"
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
- id: p20
  title: "提出理由的要求与实际给出的理由不同"
  type: rule
  source_chapter: "n519/p69；n519/p70"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA
  source_loci:
    - "n519/p69"
    - "n519/p70"
  summary: |-
    原著场面：主持人要求说明判定的根据，普通成员随后以自身经验解释选择。
    候选规则：写制度会议时不能把要求说明当作已有说明，要让理由真正从独立人物口中出现。
    解释性质：NARRATIVE_INFERENCE；不是作者公开的方法论宣言。
    边界：理由出现不等于其符合法律、也不能代替受影响人的同意。
    后续核查：只观察叙事的多方自主表达，不提供现实法律意见。
  tags: [narrative-rule, historical-fiction, source-audited]
  task_ids: [WM-07, WM-08]
  provenance: NARRATIVE_INFERENCE
  source_observation: "主持人要求说明判定的根据，普通成员随后以自身经验解释选择。"
  rule_scope: "写制度会议时不能把要求说明当作已有说明，要让理由真正从独立人物口中出现。"
  counterexample_or_limit: "理由出现不等于其符合法律、也不能代替受影响人的同意。"
  missing_conditions: "只观察叙事的多方自主表达，不提供现实法律意见。"
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
- id: p21
  title: "试点范围是许可的一部分"
  type: rule
  source_chapter: "n520/p17；n425/p27"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA
  source_loci:
    - "n520/p17"
    - "n425/p27"
  summary: |-
    原著场面：人物同意继续小范围试验同时明确不准扩展；之前也有对旧基层制度的争论。
    候选规则：角色允许试验和允许全面推行必须在剧情中分别登记。
    解释性质：CHARACTER_NORMATIVE；不是作者公开的方法论宣言。
    边界：不能由这次口头许可推断具体试点后来成功或者有持续授权。
    后续核查：原文是虚构政治谈判，仅用于写有限许可的叙事后果。
  tags: [narrative-rule, historical-fiction, source-audited]
  task_ids: [WM-07]
  provenance: CHARACTER_NORMATIVE
  source_observation: "人物同意继续小范围试验同时明确不准扩展；之前也有对旧基层制度的争论。"
  rule_scope: "角色允许试验和允许全面推行必须在剧情中分别登记。"
  counterexample_or_limit: "不能由这次口头许可推断具体试点后来成功或者有持续授权。"
  missing_conditions: "原文是虚构政治谈判，仅用于写有限许可的叙事后果。"
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
- id: p22
  title: "风险预期必须落实为未来时间状态"
  type: principle
  source_chapter: "n530/p1；n099/p18"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA
  source_loci:
    - "n530/p1"
    - "n099/p18"
  summary: |-
    原著场面：当事人确定了眼前运输月份与之后仍将发生的补给安排，亦有人忧虑供应伙伴出问题。
    候选规则：未来风险在长篇里是尚待兑现的承诺，不能写成已经完成。
    解释性质：NARRATIVE_INFERENCE；不是作者公开的方法论宣言。
    边界：原文存在战争背景，但此处不提取运输路线、规模和现实补给执行技巧。
    后续核查：属于时间连续性的文学审计候选。
  tags: [narrative-rule, historical-fiction, source-audited]
  task_ids: [WM-04, WM-06]
  provenance: NARRATIVE_INFERENCE
  source_observation: "当事人确定了眼前运输月份与之后仍将发生的补给安排，亦有人忧虑供应伙伴出问题。"
  rule_scope: "未来风险在长篇里是尚待兑现的承诺，不能写成已经完成。"
  counterexample_or_limit: "原文存在战争背景，但此处不提取运输路线、规模和现实补给执行技巧。"
  missing_conditions: "属于时间连续性的文学审计候选。"
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
- id: p23
  title: "被讲述的版本不等于现场真实"
  type: principle
  source_chapter: "n166/p30；n571/p5"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA
  source_loci:
    - "n166/p30"
    - "n571/p5"
  summary: |-
    原著场面：故事前后存在说书者和听众参与公开讲述的层次，与此前实际展示的现场不同。
    候选规则：在结尾重新评说旧事时，应标明传闻、亲历和主持叙事的不同证据来源。
    解释性质：NARRATIVE_INFERENCE；不是作者公开的方法论宣言。
    边界：此条并非作者公开写成的创作法，更不能推断前文全部不真实。
    后续核查：不得仿造原小说独有结尾场景。
  tags: [narrative-rule, historical-fiction, source-audited]
  task_ids: [WM-09]
  provenance: NARRATIVE_INFERENCE
  source_observation: "故事前后存在说书者和听众参与公开讲述的层次，与此前实际展示的现场不同。"
  rule_scope: "在结尾重新评说旧事时，应标明传闻、亲历和主持叙事的不同证据来源。"
  counterexample_or_limit: "此条并非作者公开写成的创作法，更不能推断前文全部不真实。"
  missing_conditions: "不得仿造原小说独有结尾场景。"
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
```

## 未形成数学公式的记录

本次按全量范围检索了公式、单位、表头、成数、支出数字及章节附注。出现过角色当场估算、小说化费用数字和某处机构清单，但原著属于文学叙述，**未发现经文本逐条证明可以安全外推的独立通用计算规则**。故不为凑类别制造`calculation`或不具实际字段来源的公式。若后续专项审查发现完整计算口径，可新增带来源的候选，不默认为“无公式已获证明”。

## 覆盖与阶段边界

WM-01—WM-09皆有至少一个候选任务关联；S1—S6均有原文依据。原著多处讲人物“必须”与另一人反对，存在伦理差异；不能把单方道德断言变成写作SKILL规范。14条R042旧问题claim_id仍禁止直接晋级；其余旧阅读候选也只有待源审资格。此为第二个（principle）独立提取器结果，不能冒充五路协作完成。B PROVISIONAL / C NOT_RUN / certified SKILL 0。
