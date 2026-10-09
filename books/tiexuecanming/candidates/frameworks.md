# 《铁血残明》 Stage1 独立框架提取器｜R048 原始候选

> 依据仓颉 v2.5 原版 `methodology/02-stage1-parallel-extract.md` 与 `extractors/framework-extractor.md`，输入是 R042 用户已批准的本书 BOOK_OVERVIEW 与用户提供的实际 EPUB。仅执行 framework extractor；principle/case/counter-example/glossary 分属未来四轮。所有条目是研究者提炼的叙事写作**候选**，不是小说作者自述方法，也不代表实际军事、治理、金融程序。

> **源性与版权**：源章节 n001—n532 依本 EPUB 的 OPF/R002 有效叙事序号，而不是印刷章号。保留原版 `source_quote` 字段，因公开仓库不刊载受版权保护原文而留空；每个来源绑定私有原文 p-index 与不可逆 SHA（`FRAMEWORK_EVIDENCE.tsv`）。其中部分人物承受胁迫，不应将其表面顺从写成真正自愿。全部 B PROVISIONAL，C NOT_RUN，Stage1.5 待审。

```yaml
- id: f01
  title: "旧名声、当场能力、外部评价的三层身份连续性"
  type: framework
  source_chapter: "《铁血残明》 n001/p20、n002/p36、n201/p54、n201/p56"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_ORIGINAL_SHA
  source_loci:
    - "n001/p20"
    - "n002/p36"
    - "n201/p54"
    - "n201/p56"
  summary: |-
    原始场面：叙事中的人物带着旁人已经形成的恶劣评价进入新局面；由家庭旧债、后来上级的赞许及突然响起的私人指责构成多见证人之间的不一致。
    可迁移的文学结构：将旧身份与新行为分别给不同角色观察，随后允许新的公共评价与仍未解决的私人旧债同场存在；读者从现场变化判断信誉而非由旁白统一宣布。
    操作时的输入：有争议人物在不同时期的行为记录与三个互不共享全部消息的见证人
    预期的原创叙事交付：旧评/新行为/官方评价/私人异议四态人物信用账
    原文仍未证明的边界：某位官员称赞并非主角道德可靠的作者结论；不能凭突然出现的私人指责反向证明所有正面行为虚伪。
  tags: [historical-fiction, narrative-framework, source-bounded]
  task_ids: [TX-01, TX-08]
  inputs: "有争议人物在不同时期的行为记录与三个互不共享全部消息的见证人"
  outputs: "旧评/新行为/官方评价/私人异议四态人物信用账"
  steps:
    - "给原创人物建立旧评、最近行为、不同见证人的利害立场；安排三次互不替代的评价并记录各自知道的范围。"
    - "切换至少一个拥有独立信息或利益的非主角人物，让其明确不同意或补充未知事实。"
    - "用后续场面验证选择引发何种实际后果；未发生的部分继续标未知。"
  missing_conditions: "原书证据不能填补陌生历史制度真伪、原创人物测试与持续长篇效果。"
  counterexample_or_limit: "某位官员称赞并非主角道德可靠的作者结论；不能凭突然出现的私人指责反向证明所有正面行为虚伪。"
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
- id: f02
  title: "办事从会背文书到得到第三方认可的多级路径"
  type: procedure
  source_chapter: "《铁血残明》 n030/p33、n055/p30、n055/p31、n055/p32"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_ORIGINAL_SHA
  source_loci:
    - "n030/p33"
    - "n055/p30"
    - "n055/p31"
    - "n055/p32"
  summary: |-
    原始场面：熟悉条目与实际能用并非同一种技能；申请文书由不同当事人撰改、传送、争夺提交时点，拥有上级审核权的人仍可能另作裁量。
    可迁移的文学结构：按角色提出、写成、他人修改、送达、上级是否接受、后续能否执行六态维护信息；核心戏剧来自各阶段并不自动重合。
    操作时的输入：原创事务目标、文书作者、审核者以及相互冲突的要求
    预期的原创叙事交付：申请/修改/送达/采信/兑现五种可回查场面
    原文仍未证明的边界：n055/p32明确质疑文书先到能否决定功劳归属；故事中说明性历史词不等于史实可靠。
  tags: [historical-fiction, narrative-framework, source-bounded]
  task_ids: [TX-02, TX-03]
  inputs: "原创事务目标、文书作者、审核者以及相互冲突的要求"
  outputs: "申请/修改/送达/采信/兑现五种可回查场面"
  steps:
    - "只写具有角色利害、实际受理权限和未获确认状态的手续现场，不将明代具体办事规则当现实行政流程。"
    - "切换至少一个拥有独立信息或利益的非主角人物，让其明确不同意或补充未知事实。"
    - "用后续场面验证选择引发何种实际后果；未发生的部分继续标未知。"
  missing_conditions: "原书证据不能填补陌生历史制度真伪、原创人物测试与持续长篇效果。"
  counterexample_or_limit: "n055/p32明确质疑文书先到能否决定功劳归属；故事中说明性历史词不等于史实可靠。"
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
- id: f03
  title: "地方调解与官署利益交错的制度现场"
  type: framework
  source_chapter: "《铁血残明》 n008/p2、n030/p33、n055/p31"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_ORIGINAL_SHA
  source_loci:
    - "n008/p2"
    - "n030/p33"
    - "n055/p31"
  summary: |-
    原始场面：基层调解机构、县衙、里老和衙中人员在地方事务中有不同利益；会读行政册子和抢发申请都暴露规则与真实影响力的差异。
    可迁移的文学结构：不能单靠制度名称陈述公正；把哪位当事人能发言、谁提供场地资源、谁实际裁断交代为具体场面。
    操作时的输入：一件原创争议与机构之间互相限制的管辖范围
    预期的原创叙事交付：谁陈述/谁受理/谁控制资源/谁签署/尚未解决什么的视角表
    原文仍未证明的边界：n008/p2是小说叙事者对制度沿革的概括，尚未核实适用于所有真实明末地方。
  tags: [historical-fiction, narrative-framework, source-bounded]
  task_ids: [TX-01, TX-02]
  inputs: "一件原创争议与机构之间互相限制的管辖范围"
  outputs: "谁陈述/谁受理/谁控制资源/谁签署/尚未解决什么的视角表"
  steps:
    - "安排不同权力位置的两名角色对一件民事事务作不同解释，再让受影响者的行动改变局面。"
    - "切换至少一个拥有独立信息或利益的非主角人物，让其明确不同意或补充未知事实。"
    - "用后续场面验证选择引发何种实际后果；未发生的部分继续标未知。"
  missing_conditions: "原书证据不能填补陌生历史制度真伪、原创人物测试与持续长篇效果。"
  counterexample_or_limit: "n008/p2是小说叙事者对制度沿革的概括，尚未核实适用于所有真实明末地方。"
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
- id: f04
  title: "名义官职与跨部门实际约束的不等式"
  type: framework
  source_chapter: "《铁血残明》 n145/p29、n315/p40、n420/p2、n485/p23"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_ORIGINAL_SHA
  source_loci:
    - "n145/p29"
    - "n315/p40"
    - "n420/p2"
    - "n485/p23"
  summary: |-
    原始场面：角色期待新头衔带来行动能力，但一处上级号令对另一独立将领无实际约束；不同部门对指挥归属公开发问，后续合作又必须得到对方现场答应。
    可迁移的文学结构：名义级别、可以发出命令、对方接收以及自愿协作是四种不同的故事状态；不能把协作失败与合作成功简化成权力大小的直接推论。
    操作时的输入：多方权限关系与各自目标，所有行动均停留文学决策层
    预期的原创叙事交付：名义指令/实际同意/执行疑问/协作代价四栏
    原文仍未证明的边界：n485只证明那一次有限合作，不代表指挥关系已经永久统一；不输出实战调度步骤。
  tags: [historical-fiction, narrative-framework, source-bounded]
  task_ids: [TX-02, TX-06]
  inputs: "多方权限关系与各自目标，所有行动均停留文学决策层"
  outputs: "名义指令/实际同意/执行疑问/协作代价四栏"
  steps:
    - "在原创组织戏中分别让上级、合作者、属员说明能承诺什么，并让合作以具体条件成立或退出。"
    - "切换至少一个拥有独立信息或利益的非主角人物，让其明确不同意或补充未知事实。"
    - "用后续场面验证选择引发何种实际后果；未发生的部分继续标未知。"
  missing_conditions: "原书证据不能填补陌生历史制度真伪、原创人物测试与持续长篇效果。"
  counterexample_or_limit: "n485只证明那一次有限合作，不代表指挥关系已经永久统一；不输出实战调度步骤。"
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
- id: f05
  title: "首领的知识缺口如何交给专业属员修正"
  type: procedure
  source_chapter: "《铁血残明》 n081/p59、n165/p1、n174/p23、n174/p24"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_ORIGINAL_SHA
  source_loci:
    - "n081/p59"
    - "n165/p1"
    - "n174/p23"
    - "n174/p24"
  summary: |-
    原始场面：公开训话之后领导私下承认自己尚未想好后续内容；懂得规章的属官会提出修改；岗位人员掌握文书、客户及使用成本信息并向上说明。
    可迁移的文学结构：把领导初始不确定、下属独立提出不同方案、当场选择与后续是否落实分为连续叙事节点，避免主角发令便显得组织成熟。
    操作时的输入：原创团队的知识边界、专业属员与共同职责
    预期的原创叙事交付：提出缺口—收到异议—裁量—实施情况的分镜
    原文仍未证明的边界：n174某些建议带有权力攫取及伤害风险，不能提炼为现实组织控制技巧；源场只证明人物意见冲突。
  tags: [historical-fiction, narrative-framework, source-bounded]
  task_ids: [TX-03, TX-05]
  inputs: "原创团队的知识边界、专业属员与共同职责"
  outputs: "提出缺口—收到异议—裁量—实施情况的分镜"
  steps:
    - "先展示领导留下的真实知识空档，再赋予下属一个对选择有影响的专业事实，最后呈现接受或拒绝的成本。"
    - "切换至少一个拥有独立信息或利益的非主角人物，让其明确不同意或补充未知事实。"
    - "用后续场面验证选择引发何种实际后果；未发生的部分继续标未知。"
  missing_conditions: "原书证据不能填补陌生历史制度真伪、原创人物测试与持续长篇效果。"
  counterexample_or_limit: "n174某些建议带有权力攫取及伤害风险，不能提炼为现实组织控制技巧；源场只证明人物意见冲突。"
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
- id: f06
  title: "账面储备、临时替代与后来对账的三段资源链"
  type: procedure
  source_chapter: "《铁血残明》 n114/p27、n114/p29、n531/p8"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_ORIGINAL_SHA
  source_loci:
    - "n114/p27"
    - "n114/p29"
    - "n531/p8"
  summary: |-
    原始场面：官仓被期待承担的储备并未实际到位；角色在城内寻找其他资源暂时补足；很久以后另一起供给争议仍围绕是否真正运达以及账册核对。
    可迁移的文学结构：人物认为有资源、实物可用、谁承诺转移以及后续是否入账分别保留状态；一处有临时补救不等于另处所有财政已解决。
    操作时的输入：原创集体事件所需物资、相互独立的保管与认定者
    预期的原创叙事交付：预期/库存/替代/实际交接/对账的跨章后果表
    原文仍未证明的边界：n114明确存在有作用的替代资源，不能把空仓扩写成整个守城必然失败；n531不能证明另一笔款项最终兑现。
  tags: [historical-fiction, narrative-framework, source-bounded]
  task_ids: [TX-04, TX-10]
  inputs: "原创集体事件所需物资、相互独立的保管与认定者"
  outputs: "预期/库存/替代/实际交接/对账的跨章后果表"
  steps:
    - "以原创虚构需求列出承诺、实物、已到场、已记账与仍受争议的交付状态，只写人物与约束，不提供现实军事补给细节。"
    - "切换至少一个拥有独立信息或利益的非主角人物，让其明确不同意或补充未知事实。"
    - "用后续场面验证选择引发何种实际后果；未发生的部分继续标未知。"
  missing_conditions: "原书证据不能填补陌生历史制度真伪、原创人物测试与持续长篇效果。"
  counterexample_or_limit: "n114明确存在有作用的替代资源，不能把空仓扩写成整个守城必然失败；n531不能证明另一笔款项最终兑现。"
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
- id: f07
  title: "外来上级命令与本地原方案相撞的局部重规划"
  type: framework
  source_chapter: "《铁血残明》 n315/p40、n320/p36、n420/p2、n485/p23"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_ORIGINAL_SHA
  source_loci:
    - "n315/p40"
    - "n320/p36"
    - "n420/p2"
    - "n485/p23"
  summary: |-
    原始场面：地方组织不得不面对另一路权威的临时指令、同盟成员不愿听调以及原先设想被改变；另一场多方公开争论权源，仍可在特定任务上取得有限同意。
    可迁移的文学结构：用多条时差不同的消息让人物不得不重新做政治与人际选择；不把小说中的具体路线、战术或编成抽取为实操。
    操作时的输入：不同主体承诺与消息到达的时间点
    预期的原创叙事交付：原计划、外部变更、人物同意、未谈成之处的故事状态
    原文仍未证明的边界：不同书内场景不能拼成一条真实军事标准作业流程；某次协作不意味着长期团结。
  tags: [historical-fiction, narrative-framework, source-bounded]
  task_ids: [TX-05, TX-06]
  inputs: "不同主体承诺与消息到达的时间点"
  outputs: "原计划、外部变更、人物同意、未谈成之处的故事状态"
  steps:
    - "前章确认各方目标与预期，随后送达改变边界的新信息，由各人按有限权限分别作出可见回应。"
    - "切换至少一个拥有独立信息或利益的非主角人物，让其明确不同意或补充未知事实。"
    - "用后续场面验证选择引发何种实际后果；未发生的部分继续标未知。"
  missing_conditions: "原书证据不能填补陌生历史制度真伪、原创人物测试与持续长篇效果。"
  counterexample_or_limit: "不同书内场景不能拼成一条真实军事标准作业流程；某次协作不意味着长期团结。"
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
- id: f08
  title: "岗位待遇、实际权限与专业承认之间的区分"
  type: framework
  source_chapter: "《铁血残明》 n361/p34、n361/p35、n361/p36、n380/p31"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_ORIGINAL_SHA
  source_loci:
    - "n361/p34"
    - "n361/p35"
    - "n361/p36"
    - "n380/p31"
  summary: |-
    原始场面：人物讨论新增岗位等级以承认经验，但专业属官立刻质疑新等级是否压过原指挥权，主持人作出解释；另一处个体以不安姿态请求继续参与考核。
    可迁移的文学结构：把岗位名、报酬、谁有决定权、成员愿意承担什么分成四层，不能因得到高待遇就推定可以对他人发令或得到自由同意。
    操作时的输入：原创组织中两类岗位与当事人可拒绝的范围
    预期的原创叙事交付：名分/薪酬/实际职权/本人意愿的差异矩阵
    原文仍未证明的边界：n361只有方案与当场解释，并未证明全体系长期执行成功；n380受压表达不能算无压力的自愿。
  tags: [historical-fiction, narrative-framework, source-bounded]
  task_ids: [TX-03, TX-05]
  inputs: "原创组织中两类岗位与当事人可拒绝的范围"
  outputs: "名分/薪酬/实际职权/本人意愿的差异矩阵"
  steps:
    - "从当事人待遇期望切入，由专业人员提出权责矛盾，再在后段写出成员的主动申请或压力。"
    - "切换至少一个拥有独立信息或利益的非主角人物，让其明确不同意或补充未知事实。"
    - "用后续场面验证选择引发何种实际后果；未发生的部分继续标未知。"
  missing_conditions: "原书证据不能填补陌生历史制度真伪、原创人物测试与持续长篇效果。"
  counterexample_or_limit: "n361只有方案与当场解释，并未证明全体系长期执行成功；n380受压表达不能算无压力的自愿。"
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
- id: f09
  title: "对立阵营与弱势人物的独立利益空间"
  type: framework
  source_chapter: "《铁血残明》 n250/p31、n305/p50、n350/p69"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_ORIGINAL_SHA
  source_loci:
    - "n250/p31"
    - "n305/p50"
    - "n350/p69"
  summary: |-
    原始场面：对立方主事者在主角缺席时评估自己内部问题；从集体位置转到无法预知明天的少年，再到被卷入者面对互相矛盾的求生选择。
    可迁移的文学结构：原始行为动机不是主角的错误注释；不同阵营内部有自己不同的消息、恐惧、个人目标，前一个决定会影响但不能替后者发言。
    操作时的输入：三位角色各自的有限知识、权益与风险
    预期的原创叙事交付：双阵营场景及一条脱离主角视角的个体后果链
    原文仍未证明的边界：有独立描写也不意味着弱者拥有同样多的自由；不得复制具体原书人物和事件组合。
  tags: [historical-fiction, narrative-framework, source-bounded]
  task_ids: [TX-06, TX-07]
  inputs: "三位角色各自的有限知识、权益与风险"
  outputs: "双阵营场景及一条脱离主角视角的个体后果链"
  steps:
    - "在主角不在场时至少保留一名对手与一名弱势人物的独立选择，换场不替他们直接宣布情绪结论。"
    - "切换至少一个拥有独立信息或利益的非主角人物，让其明确不同意或补充未知事实。"
    - "用后续场面验证选择引发何种实际后果；未发生的部分继续标未知。"
  missing_conditions: "原书证据不能填补陌生历史制度真伪、原创人物测试与持续长篇效果。"
  counterexample_or_limit: "有独立描写也不意味着弱者拥有同样多的自由；不得复制具体原书人物和事件组合。"
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
- id: f10
  title: "公共事件的成果与普通人战后生活双后果账"
  type: framework
  source_chapter: "《铁血残明》 n350/p69、n490/p28、n505/p8"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_ORIGINAL_SHA
  source_loci:
    - "n350/p69"
    - "n490/p28"
    - "n505/p8"
  summary: |-
    原始场面：大局变化首先让民众在河岸犹疑，后来物资与现场工作出现书面计划以外的困难，战后普通人仍在分配物品时产生争吵。
    可迁移的文学结构：把组织目标、现场执行者、一般人生活和下一章仍需处理的问题同时记账，不用胜利独白消除个人损失和秩序矛盾。
    操作时的输入：原创共同事件和不依赖主角认可的普通人
    预期的原创叙事交付：公共成果/现场困难/具体生活/未结责任四条连锁
    原文仍未证明的边界：n505既有实际组织帮助也有零星争斗，不得将现场简化为彻底无序或彻底和谐。
  tags: [historical-fiction, narrative-framework, source-bounded]
  task_ids: [TX-04, TX-07, TX-08]
  inputs: "原创共同事件和不依赖主角认可的普通人"
  outputs: "公共成果/现场困难/具体生活/未结责任四条连锁"
  steps:
    - "从宏观成果转入独立普通人现场，并至少让一个执行者发现原计划未知的民生障碍。"
    - "切换至少一个拥有独立信息或利益的非主角人物，让其明确不同意或补充未知事实。"
    - "用后续场面验证选择引发何种实际后果；未发生的部分继续标未知。"
  missing_conditions: "原书证据不能填补陌生历史制度真伪、原创人物测试与持续长篇效果。"
  counterexample_or_limit: "n505既有实际组织帮助也有零星争斗，不得将现场简化为彻底无序或彻底和谐。"
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
- id: f11
  title: "家户与属员是否同意须脱离命令单独审视"
  type: framework
  source_chapter: "《铁血残明》 n015/p49、n161/p65、n370/p19、n527/p30、n527/p31"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_ORIGINAL_SHA
  source_loci:
    - "n015/p49"
    - "n161/p65"
    - "n370/p19"
    - "n527/p30"
    - "n527/p31"
  summary: |-
    原始场面：身份较低的女性通过返还财物表明自己的选择；身边仆人对改变身份表达不愿；个人离别并未自动消除情感后果；后来请假接家人的申请须多级同意并附条件。
    可迁移的文学结构：把说出自己的意愿、他人的回应、现实上能否拒绝及日后能否兑现分别书写，制度同意与自由同意不能混为一谈。
    操作时的输入：原创普通人物需要什么、可以拒绝什么及担保约束
    预期的原创叙事交付：请求/回答/附加条件/当事人真实机会/以后结果的剧情账
    原文仍未证明的边界：n161的拒绝明确未被尊重，不能改写成幸福自愿从军；n527只展示附条件许可，不证明当事人最终返家。
  tags: [historical-fiction, narrative-framework, source-bounded]
  task_ids: [TX-01, TX-08]
  inputs: "原创普通人物需要什么、可以拒绝什么及担保约束"
  outputs: "请求/回答/附加条件/当事人真实机会/以后结果的剧情账"
  steps:
    - "选择最缺乏权力的角色先展示其行动，随后切换到批准者一侧，检查是否承受持续义务。"
    - "切换至少一个拥有独立信息或利益的非主角人物，让其明确不同意或补充未知事实。"
    - "用后续场面验证选择引发何种实际后果；未发生的部分继续标未知。"
  missing_conditions: "原书证据不能填补陌生历史制度真伪、原创人物测试与持续长篇效果。"
  counterexample_or_limit: "n161的拒绝明确未被尊重，不能改写成幸福自愿从军；n527只展示附条件许可，不证明当事人最终返家。"
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
- id: f12
  title: "把猜测、对方未知和事后判断分成有限视角"
  type: framework
  source_chapter: "《铁血残明》 n430/p58、n430/p59、n500/p24、n500/p25"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_ORIGINAL_SHA
  source_loci:
    - "n430/p58"
    - "n430/p59"
    - "n500/p24"
    - "n500/p25"
  summary: |-
    原始场面：熟悉未来趋势的人物仍承认不知道对手将选哪个目标，只能等待消息；另一现场同样传来不明动静时，不同当事人从声音推断不同的可能。
    可迁移的文学结构：每条消息附一个知道它的人、他看到什么、误判概率何处产生及什么时候可核实，不让全知旁白填补任何人物视角缺口。
    操作时的输入：原创事件和至少两种不完整的目击条件
    预期的原创叙事交付：实际发生/每人所知/每人推测/后来确认四层叙事状态
    原文仍未证明的边界：n500/p25仅是吴达财一人的估计，不能作为对面人的真实意图；拒绝提取现实侦察技巧。
  tags: [historical-fiction, narrative-framework, source-bounded]
  task_ids: [TX-06, TX-07]
  inputs: "原创事件和至少两种不完整的目击条件"
  outputs: "实际发生/每人所知/每人推测/后来确认四层叙事状态"
  steps:
    - "以两名人物不同观察条件描写同一变化，延迟验证，之后让角色按实际所得信息更改判断。"
    - "切换至少一个拥有独立信息或利益的非主角人物，让其明确不同意或补充未知事实。"
    - "用后续场面验证选择引发何种实际后果；未发生的部分继续标未知。"
  missing_conditions: "原书证据不能填补陌生历史制度真伪、原创人物测试与持续长篇效果。"
  counterexample_or_limit: "n500/p25仅是吴达财一人的估计，不能作为对面人的真实意图；拒绝提取现实侦察技巧。"
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
- id: f13
  title: "现场事件、报功文本与编辑再传播的层级差"
  type: procedure
  source_chapter: "《铁血残明》 n175/p23、n175/p24、n244/p30、n526/p82、n526/p87、n531/p25、n531/p26"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_ORIGINAL_SHA
  source_loci:
    - "n175/p23"
    - "n175/p24"
    - "n244/p30"
    - "n526/p82"
    - "n526/p87"
    - "n531/p25"
    - "n531/p26"
  summary: |-
    原始场面：早期负责出版物的配角质疑成本及渠道被他人控制，另一场地方士人讨论战报和其他叙述同时出现；后期功劳文字存在编辑式改动提议又被当事人驳回，报道内容引起独立编辑不满仍被要求刊发。
    可迁移的文学结构：真正发生的现场、初稿、编辑意图、文本获批与读者可能理解是五个不能互为证明的层次，写成跨卷信息变化而非宣传诀窍。
    操作时的输入：原创事件事实、两类内容把关者与传播时差
    预期的原创叙事交付：事实版本/草稿/争议/刊发/受众未知的文学对照表
    原文仍未证明的边界：n526的夸大建议被明确否决，不能说虚假版本已发表；n531刊出不保证受众会相信，更不能变成现实舆论操控指南。
  tags: [historical-fiction, narrative-framework, source-bounded]
  task_ids: [TX-02, TX-09]
  inputs: "原创事件事实、两类内容把关者与传播时差"
  outputs: "事实版本/草稿/争议/刊发/受众未知的文学对照表"
  steps:
    - "先确立角色目击到的有限事实，再换到记录者/审阅者场面，最后保留刊发与读者是否相信之间的未证状态。"
    - "切换至少一个拥有独立信息或利益的非主角人物，让其明确不同意或补充未知事实。"
    - "用后续场面验证选择引发何种实际后果；未发生的部分继续标未知。"
  missing_conditions: "原书证据不能填补陌生历史制度真伪、原创人物测试与持续长篇效果。"
  counterexample_or_limit: "n526的夸大建议被明确否决，不能说虚假版本已发表；n531刊出不保证受众会相信，更不能变成现实舆论操控指南。"
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
- id: f14
  title: "地点技术条件与计划外现场障碍的回写"
  type: troubleshooting
  source_chapter: "《铁血残明》 n285/p5、n285/p6、n490/p28"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_ORIGINAL_SHA
  source_loci:
    - "n285/p5"
    - "n285/p6"
    - "n490/p28"
  summary: |-
    原始场面：一个工坊地点被质疑存在自然条件风险，专业人员解释所知但仍承认设备受损可能；另外现场工作比事前纸面安排出现更多无法预见的麻烦。
    可迁移的文学结构：若在故事里新计划遭遇具体材料/天气/人员状态问题，必须给受影响专业者一个可以反驳首领设想的现场，而不是凭主角解释取消风险。
    操作时的输入：非危险原创设施的场地条件、专业疑问和实施场景
    预期的原创叙事交付：风险被指出—方案受质疑—现场反馈—修订或搁置四态剧情骨架
    原文仍未证明的边界：源中自然灾害概率和真实设备性能未经外部核证，本条不是机械制造、战争施工或现场操作指南。
  tags: [historical-fiction, narrative-framework, source-bounded]
  task_ids: [TX-03, TX-04]
  inputs: "非危险原创设施的场地条件、专业疑问和实施场景"
  outputs: "风险被指出—方案受质疑—现场反馈—修订或搁置四态剧情骨架"
  steps:
    - "写出现实条件的症状与角色判断之间的差距，设计审视者提出相反证据，后续是否解决仍单列未知。"
    - "切换至少一个拥有独立信息或利益的非主角人物，让其明确不同意或补充未知事实。"
    - "用后续场面验证选择引发何种实际后果；未发生的部分继续标未知。"
  missing_conditions: "原书证据不能填补陌生历史制度真伪、原创人物测试与持续长篇效果。"
  counterexample_or_limit: "源中自然灾害概率和真实设备性能未经外部核证，本条不是机械制造、战争施工或现场操作指南。"
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
- id: f15
  title: "制度扩大后反对者的真实生存空间"
  type: framework
  source_chapter: "《铁血残明》 n161/p65、n380/p31、n527/p29、n527/p30"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_ORIGINAL_SHA
  source_loci:
    - "n161/p65"
    - "n380/p31"
    - "n527/p29"
    - "n527/p30"
  summary: |-
    原始场面：看似有效率的登记和考核会让不愿意的人被直接压过；处理工作中的人员可能为了迎合上级忽略另一个被质疑者的权益，而另有成员需申请照顾家人。
    可迁移的文学结构：以一个受影响者的拒绝能力、程序受理真实情况和掌权者的责任作为制度运行的文学反证，不能以组织效率自动压平伦理。
    操作时的输入：原创制度变动及受影响者的自主利益
    预期的原创叙事交付：批准/反对/私下规避/长远个人负担的视角清单
    原文仍未证明的边界：n527/p29只证明属员当下偏听并非全部程序必然不公；不可从小说提炼胁迫人员的实操手段。
  tags: [historical-fiction, narrative-framework, source-bounded]
  task_ids: [TX-05, TX-08]
  inputs: "原创制度变动及受影响者的自主利益"
  outputs: "批准/反对/私下规避/长远个人负担的视角清单"
  steps:
    - "为每条新规安排一名能够受益但不必赞成它的人，并在后续描写被忽略意见如何继续形成代价。"
    - "切换至少一个拥有独立信息或利益的非主角人物，让其明确不同意或补充未知事实。"
    - "用后续场面验证选择引发何种实际后果；未发生的部分继续标未知。"
  missing_conditions: "原书证据不能填补陌生历史制度真伪、原创人物测试与持续长篇效果。"
  counterexample_or_limit: "n527/p29只证明属员当下偏听并非全部程序必然不公；不可从小说提炼胁迫人员的实操手段。"
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
- id: f16
  title: "信誉想象到新承诺形成，不能直接跳至兑现"
  type: procedure
  source_chapter: "《铁血残明》 n530/p41、n531/p8、n532/p47、n532/p49"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_ORIGINAL_SHA
  source_loci:
    - "n530/p41"
    - "n531/p8"
    - "n532/p47"
    - "n532/p49"
  summary: |-
    原始场面：人物口头将未来信用折算为预计资源，另一场账务争论提示必须有实物实际到位的核验，所提供版本最后只是个人在正式文件写下金额。
    可迁移的文学结构：预计价值、文件内容、外界是否接受与实际付款具有不同的故事时态；故事停止在决定动作时便应保留未来条件未知。
    操作时的输入：原创承诺事件、独立认定人和未兑现的未来责任
    预期的原创叙事交付：想法/承诺/实物证明/签署/未证实际兑现的五栏连续账
    原文仍未证明的边界：本版EPUB n532/p49没有任何后续兑付事实，不能宣称作者安排成功或崩溃；不提供票据发行或现实融资操作。
  tags: [historical-fiction, narrative-framework, source-bounded]
  task_ids: [TX-04, TX-09, TX-10]
  inputs: "原创承诺事件、独立认定人和未兑现的未来责任"
  outputs: "想法/承诺/实物证明/签署/未证实际兑现的五栏连续账"
  steps:
    - "在原创、非现实金融情境里建立一个角色许诺、另一个角色提出交付证据、末尾完成签署但后果未知的叙事闭环。"
    - "切换至少一个拥有独立信息或利益的非主角人物，让其明确不同意或补充未知事实。"
    - "用后续场面验证选择引发何种实际后果；未发生的部分继续标未知。"
  missing_conditions: "原书证据不能填补陌生历史制度真伪、原创人物测试与持续长篇效果。"
  counterexample_or_limit: "本版EPUB n532/p49没有任何后续兑付事实，不能宣称作者安排成功或崩溃；不提供票据发行或现实融资操作。"
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
- id: f17
  title: "属员提案—首领裁量—未来责任归属的会商机制"
  type: framework
  source_chapter: "《铁血残明》 n174/p23、n174/p24、n361/p35、n361/p36、n527/p30、n527/p31"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_ORIGINAL_SHA
  source_loci:
    - "n174/p23"
    - "n174/p24"
    - "n361/p35"
    - "n361/p36"
    - "n527/p30"
    - "n527/p31"
  summary: |-
    原始场面：文书岗位人员提出自己的收益安排，高级属官对新增职位造成的权限歧义当场发问，末期家属申请又由多级担保与审批后产生附加条件。
    可迁移的文学结构：不同职能属员会基于经验提供主角未想到的后果；有会商、有解释、有条件通过都不是之后已经做到的证明。
    操作时的输入：原创团队提案、各方所知及最终受影响者
    预期的原创叙事交付：提出方案—独立反问—给出边界—条件批准—后续核实的对话场
    原文仍未证明的边界：源内有人提出剥削性收费与有压力的等级分配，不能转译为值得现实采用的具体措施。
  tags: [historical-fiction, narrative-framework, source-bounded]
  task_ids: [TX-03, TX-05, TX-08]
  inputs: "原创团队提案、各方所知及最终受影响者"
  outputs: "提出方案—独立反问—给出边界—条件批准—后续核实的对话场"
  steps:
    - "把专业异议者写成能够影响决策的独立角色，同时登记决定由谁承担以及谁在决策时缺席。"
    - "切换至少一个拥有独立信息或利益的非主角人物，让其明确不同意或补充未知事实。"
    - "用后续场面验证选择引发何种实际后果；未发生的部分继续标未知。"
  missing_conditions: "原书证据不能填补陌生历史制度真伪、原创人物测试与持续长篇效果。"
  counterexample_or_limit: "源内有人提出剥削性收费与有压力的等级分配，不能转译为值得现实采用的具体措施。"
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
```

## 覆盖审计与隔离

- 依据 **TX-01—TX-10** 十个 Stage0 独立原创任务对照候选，十项皆有关联，但这只是 RAW 文本候选**提及**，不等于 V1 来源充分性、V2 可执行性或 V3 任务增益通过。
- 来源横跨研究者划定的六个一级叙事弧 S1=001—080、S2=081—160、S3=161—280、S4=281—400、S5=401—480、S6=481—532。研究者并未认定其为原著原始六卷。
- 小说当前用户所给版本到 n532 即止；n532/p49 是写下金额而非后来兑现，不擅改作者结局。人物提出的规章及机构方案不等于现实法定规范，军政及财务数据不开发为现实实施指南。
- 全量源文本机器结构扫描与少量关键场面的语义复读应区分，不能将输入全部字符的哈希统计说成532章每段都已完成独立B文学审查；R008—R024旧研究质量债未清零，其中14条旧问题 claim 仍禁止直晋。
- 不运行Stage1.5、Nuwa新Phase、Skill编译或密封原创评测；四种其他提取器不得冒称已完成。
