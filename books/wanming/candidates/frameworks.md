# 《晚明》Stage1 / Framework Extractor — candidates/frameworks.md

> status: STAGE1_RAW_CANDIDATES / NOT_VERIFIED。严格按 pinned Cangjie v2.5 `methodology/02-stage1-parallel-extract.md` 和 `extractors/framework-extractor.md`；本文件仅为框架提取器独立候选，不执行原则、案例、反例或术语提取器。全书571有效章的私有源XHTML已按OPF顺序读取、统计；机器完整结构扫描不能冒称模型已逐段完成所有章节的精读，候选仍须源语境反查、Stage1.5 V1/V2/V3与原创任务测试。

> 版权：原著由用户私有提供。原版要求 `source_quote` 字段，故保留该键但值为空；不在公开GitHub复制原书表达，而由 `source_loci`、冻结章节源Hash、私有段落SHA证明定位。任何候选不等于作者明确给出的框架，也不应转为现实军事、强制、经济操纵操作指南。

```yaml
- id: f01
  title: "社会入口—资格—实际被承认的分层框架"
  type: framework
  source_chapter: "《晚明》n001/p44；《晚明》n022/p1；《晚明》n052/p28"
  source_quote: ""
  source_quote_status: "COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA"
  source_loci:
    - "n001/p44"
    - "n022/p1"
    - "n052/p28"
  summary: |-
    主人公落入陌生制度时，先让衣食住所与谋生碰壁成为可见障碍，不把超前知识等同社会通行证。
    借人物工作与官位选择显示组织内部与外部对其身份的评价不同。
    取得文书、获得人情接纳、实际能够调动资源是三个可分开的状态。
    这是从小说场面提炼出的原创构思框架，非作者自述的行政方法。
  tags: [legitimacy, character-entry, historical-fiction]
  task_ids: [WM-01, WM-03]
  inputs: "原创人物的身份状态、可选择的社会入口、旁人权限与短期生计"
  outputs: "三场不同当事人认可程度的现场及身份状态变化表"
  steps:
    - "先展示生存问题和不能直接获得的资源"
    - "安排两名具有不同评价标准的当事人作出实际回应"
    - "记录授予名分后的可用权限和仍未满足的条件"
  missing_conditions: "陌生历史场景的外部制度史料及独立原创对照试写"
  counterexample_or_limit: "若新身份一出所有人立即服从，则与源内长期资格摩擦不一致；但某些角色可能迅速认可，不能强制每场拒绝。"
  status: "RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN"
  verification_state: "NOT_STARTED_STAGE1_5"
- id: f02
  title: "长期合作者分歧与关系债务的两本账"
  type: framework
  source_chapter: "《晚明》n034/p18；《晚明》n305/p29；《晚明》n305/p36；《晚明》n468/p44"
  source_quote: ""
  source_quote_status: "COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA"
  source_loci:
    - "n034/p18"
    - "n305/p29"
    - "n305/p36"
    - "n468/p44"
  summary: |-
    共同利益并不等于共同伦理，两位合作人物在现场会对手段或分配方案提出不同意见。
    一方的反对必须改变后续选择，不能仅用作提醒主角的工具性台词。
    当场的折中方案与长期关系债务是两种结局，下一章不能自动清账。
    分歧可导致阶段合作、拖延或破裂，不能预设所有冲突终究和解。
  tags: [character-autonomy, disagreement, long-arc]
  task_ids: [WM-02, WM-07]
  inputs: "两名独立人物的目标、不能共同接受的方案、共同承担的责任"
  outputs: "对立主张场、暂时决定及跨章关系债务账"
  steps:
    - "写出反对方能够实际拒绝的具体事项"
    - "迫使双方对同一资源或价值选择发生可见取舍"
    - "记下暂时达成的安排及尚无人同意的部分"
  missing_conditions: "新角色社会背景与独立读者评价"
  counterexample_or_limit: "n305只达成勉强的暂时共识；不得假定它解决n468的后续价值冲突。"
  status: "RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN"
  verification_state: "NOT_STARTED_STAGE1_5"
- id: f03
  title: "纸面职位向长期组织能力转换的阶段框架"
  type: framework
  source_chapter: "《晚明》n052/p28；《晚明》n070/p36；《晚明》n494/p17；《晚明》n514/p34"
  source_quote: ""
  source_quote_status: "COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA"
  source_loci:
    - "n052/p28"
    - "n070/p36"
    - "n494/p17"
    - "n514/p34"
  summary: |-
    正式身份仅打开人员与外部机构的接触可能，并不直接产生训练完整的组织。
    小说先描画誓言与内部忠诚表态，再在后续章节由基层观察者和下属指出现实差异。
    组织扩大后人事、预算和部门之间的冲突成为新的依赖。
    一时的外部惊叹不能代替对内部真实成本的分析。
  tags: [organization, authority, continuity]
  task_ids: [WM-03, WM-06]
  inputs: "虚构机构的纸面任命、人员来源、日常开销、组织执行者"
  outputs: "名义权限/实际组织/外部评价三列跨章状态表"
  steps:
    - "把身份取得作为开始而非结果"
    - "安排成员各自从待遇、纪律和职位作不同回应"
    - "跨章呈现组织扩张带来的新职位与资源矛盾"
  missing_conditions: "真实历史军制细节另查，只形成文学约束而非组织实施指引"
  counterexample_or_limit: "n514的旁观者惊叹只是外界所见；n494的编制质疑说明规模增长未自动闭合。"
  status: "RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN"
  verification_state: "NOT_STARTED_STAGE1_5"
- id: f04
  title: "承诺—可支配资金—实物到位的时间差"
  type: procedure
  source_chapter: "《晚明》n099/p18；《晚明》n305/p29；《晚明》n305/p32；《晚明》n529/p38；《晚明》n530/p1"
  source_quote: ""
  source_quote_status: "COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA"
  source_loci:
    - "n099/p18"
    - "n305/p29"
    - "n305/p32"
    - "n529/p38"
    - "n530/p1"
  summary: |-
    角色宣称拥有贸易收入、库存或朝廷拨款时，现场可用资源可能仍受伙伴、时间和别的部门控制。
    预算册子会与人物新增要求撞车，必须让各方作具体延期或缩减选择。
    后续收到一项运送需求与真正交付是两种不同状态。
    此候选用于写可信的虚构时间因果，不代表真实战争筹措或金融经营方法。
  tags: [fictional-budget, logistics, time-debt]
  task_ids: [WM-03, WM-04, WM-06]
  inputs: "虚构故事中预计所得、实际可用款、其他部门支出、交付日期"
  outputs: "预计/可动用/在途/已交付四态叙事核对表与争议现场"
  steps:
    - "先明确谁认为资源可用、何时才可用"
    - "安排另一个人物用账册或实际需求提出限制"
    - "给出可以被后来章节推翻或验证的阶段性答复"
  missing_conditions: "陌生题目财务数字的独立事实核验和伦理边界"
  counterexample_or_limit: "n305的计算让双方暂时接受缩编，并不证实未来钱粮持续到位。"
  status: "RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN"
  verification_state: "NOT_STARTED_STAGE1_5"
- id: f05
  title: "组织训后复盘—异议—编制调整的反馈环"
  type: procedure
  source_chapter: "《晚明》n089/p1；《晚明》n089/p18；《晚明》n089/p26；《晚明》n111/p1；《晚明》n488/p2"
  source_quote: ""
  source_quote_status: "COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA"
  source_loci:
    - "n089/p1"
    - "n089/p18"
    - "n089/p26"
    - "n111/p1"
    - "n488/p2"
  summary: |-
    一轮实际事件之后开讨论会，基层提出的问题并不必定被首领接受。
    拒绝意见仍需有理由和人物的实际反应，下一次编制调整带走先前已知的欠账。
    训练风气本身会引起属员抗议与其他管理者不同判断。
    文学框架强调反馈有代价，不把源书高压治理翻译为现实惩罚方式。
  tags: [feedback, team-autonomy, revision]
  task_ids: [WM-03, WM-07]
  inputs: "已发生的虚构组织事件、两种互相冲突的改进意见"
  outputs: "事件复盘场/是否采纳/组织后果的三段场景"
  steps:
    - "由非主角人物提出具体现场差值"
    - "让掌权者作出接受或拒绝并暴露依据"
    - "在后段让人员职位、资源或关系作真实变化"
  missing_conditions: "不能从原书惩罚场面提取现实纪律操作"
  counterexample_or_limit: "n111显示压力过大有反对意见，组织整齐并不等于做法合理。"
  status: "RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN"
  verification_state: "NOT_STARTED_STAGE1_5"
- id: f06
  title: "上级公开定案与当事人目标落差"
  type: framework
  source_chapter: "《晚明》n143/p49；《晚明》n143/p52；《晚明》n143/p53；《晚明》n143/p55"
  source_quote: ""
  source_quote_status: "COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA"
  source_loci:
    - "n143/p49"
    - "n143/p52"
    - "n143/p53"
    - "n143/p55"
  summary: |-
    公开会议里主人公提出个人方案，与更高权限者的决定相碰撞。
    由主角现场的意外反应让读者发现个人私利与名义服从之间的差别。
    上级提供的理由使其当场结束争执，但不证明此后所有执行问题已经消失。
    特别拒绝旧R013只看人员入席便推断会议已定案的误引。
  tags: [public-decision, rank, scene-tension]
  task_ids: [WM-01, WM-03]
  inputs: "原创会议中不同权限者的职责期待与公开决定"
  outputs: "提议—裁决—反应—未结执行责任的场面"
  steps:
    - "明确提案者与最终决定者并非同一人"
    - "在决定公开时让人物显示个人目标和被改变之处"
    - "只将当场反应写成事实，后续履约另立剧情"
  missing_conditions: "该章节以外延展效果仍需下一阶段反证"
  counterexample_or_limit: "n143/p29是入座而非实际裁决，无法用来证明此流程。"
  status: "RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN"
  verification_state: "NOT_STARTED_STAGE1_5"
- id: f07
  title: "消息产生—转述—接收的有限视角链"
  type: framework
  source_chapter: "《晚明》n140/p36；《晚明》n220/p35；《晚明》n220/p42；《晚明》n248/p35"
  source_quote: ""
  source_quote_status: "COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA"
  source_loci:
    - "n140/p36"
    - "n220/p35"
    - "n220/p42"
    - "n248/p35"
  summary: |-
    事件发生、消息经某人转交、另一个人物据此判断，须以不同场次分别交代。
    人物的推测和转述不能被无声升格成作者所证实的事实。
    读者可以先获得一方不完整信息，等待后文有人纠正其假设。
    仅研究小说信息分配的叙事逻辑，不制作现实情报收集或操纵手册。
  tags: [limited-pov, rumor, information-delay]
  task_ids: [WM-05, WM-09]
  inputs: "同一虚构事件的多名有限知情人物及各自错误判断"
  outputs: "现场事实/角色所知/公开说法三态信息账和两次转场"
  steps:
    - "先记录各角色真实目睹到的局部事实"
    - "让关键消息在新一场传递并发生转述偏差"
    - "延迟或限制第三方的核实，不把猜想直接宣布成真"
  missing_conditions: "不复刻真实谍报或政治传播手段"
  counterexample_or_limit: "n140/p36是当事人估算而非已查明规模，n220/p42的消息仍来自角色讲述。"
  status: "RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN"
  verification_state: "NOT_STARTED_STAGE1_5"
- id: f08
  title: "对立阵营的独立目标与认知约束"
  type: framework
  source_chapter: "《晚明》n106/p1；《晚明》n482/p9；《晚明》n482/p15；《晚明》n556/p3"
  source_quote: ""
  source_quote_status: "COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA"
  source_loci:
    - "n106/p1"
    - "n482/p9"
    - "n482/p15"
    - "n556/p3"
  summary: |-
    对立人物拥有不为主角服务的生活空间、权力关系和内部冲突。
    其说辞、知情范围和实际选择不应按全知主角的解释统一。
    同一大事件中的不同阵营可以有自洽却互相冲突的估计。
    独立视角不意味着合理化伤害，也不能移植原小说独有的角色组合。
  tags: [opponent-agency, ensemble, partial-knowledge]
  task_ids: [WM-05, WM-06]
  inputs: "原创两方以上角色的不同价值目标、信息偏差与成本"
  outputs: "两方有限视角人物弧与对外事件造成的差异回收"
  steps:
    - "在主角不在场时展示对方独立决定"
    - "让对方内部至少出现一次意见不一致"
    - "下一次同一事件发生时保留各方理解差距"
  missing_conditions: "新故事不能复制真实历史人物独有场景与结局"
  counterexample_or_limit: "n556/p3主角对对方动机仍是推测，不能把单方推测当对方本人供述。"
  status: "RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN"
  verification_state: "NOT_STARTED_STAGE1_5"
- id: f09
  title: "市场收益与组织供给之间的竞争制约"
  type: framework
  source_chapter: "《晚明》n099/p18；《晚明》n297/p1；《晚明》n345/p29；《晚明》n437/p6"
  source_quote: ""
  source_quote_status: "COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA"
  source_loci:
    - "n099/p18"
    - "n297/p1"
    - "n345/p29"
    - "n437/p6"
  summary: |-
    早期对交易伙伴的依赖持续影响后续组织的收入想象。
    本地经营者、模仿者及渠道参与者会提出自己的价格和风险。
    一项新构想被提出并不意味着得到生产、推广或技术验证；书内也展示明确被否决的提案。
    仅把竞争和技术不确定性当叙事约束，不抽取现实操纵价格或不安全商品的做法。
  tags: [commerce-in-fiction, supply-dependency, negative-control]
  task_ids: [WM-04, WM-03]
  inputs: "原创产品或贸易事件的供应节点、参与者意愿和验证状态"
  outputs: "预期收益/实际条件/反对方反应的场景时序"
  steps:
    - "先找出收入对外部伙伴的依赖"
    - "让别的角色有独立竞争选择"
    - "写一次受到质疑、否决或调整后的真实后果"
  missing_conditions: "商业史和技术事实须另行核实"
  counterexample_or_limit: "n437/p6有被否决的技术构想，是对创新必胜论的直接限制。"
  status: "RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN"
  verification_state: "NOT_STARTED_STAGE1_5"
- id: f10
  title: "胜利表彰与战后家庭成本的双后果网"
  type: framework
  source_chapter: "《晚明》n085/p25；《晚明》n155/p52；《晚明》n338/p40；《晚明》n339/p31；《晚明》n339/p36"
  source_quote: ""
  source_quote_status: "COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA"
  source_loci:
    - "n085/p25"
    - "n155/p52"
    - "n338/p40"
    - "n339/p31"
    - "n339/p36"
  summary: |-
    在公开功劳叙事之外，同场存在资源分配异议和失去收入的具体家庭。
    主角或军人受到赞誉不等于其亲属从此拥有稳定生活。
    跨章让个体重回家庭视角后，重新衡量战争成果的分配和日常义务。
    要求场面里的普通人继续拥有可见选择，不能成为主角光环的装饰。
  tags: [aftermath, distribution, ordinary-life]
  task_ids: [WM-06, WM-08]
  inputs: "虚构重大集体成就、公开声望、至少两个私人生活的未结问题"
  outputs: "荣誉/资源/失落/补救四条后果链"
  steps:
    - "安排公开结算或奖励意见冲突"
    - "换到一个不在胜利中心的人所面对的具体障碍"
    - "让短期帮助与长期不可解决的问题并存"
  missing_conditions: "陌生角色需要原创独立利益背景"
  counterexample_or_limit: "n339/p35援助只是当时行为，不代表n339/p36所有家庭困难解除。"
  status: "RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN"
  verification_state: "NOT_STARTED_STAGE1_5"
- id: f11
  title: "制度宣称、他人权利与实际手续的分层"
  type: framework
  source_chapter: "《晚明》n265/p21；《晚明》n265/p29；《晚明》n425/p27"
  source_quote: ""
  source_quote_status: "COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA"
  source_loci:
    - "n265/p21"
    - "n265/p29"
    - "n425/p27"
  summary: |-
    具有权力的一方可以使用看似正当的公开语言，但弱势当事人的真实权益需另行观察。
    被要求配合的人可能出于职位和安全顾虑行动，而不是出于认可。
    当组织试图改革基层分配权时，会出现权力部门对自身职责的不同解释。
    本候选是批判性叙事审计，不是现实夺权或行政规避步骤。
  tags: [legality-in-fiction, independent-party, procedural-gap]
  task_ids: [WM-03, WM-07]
  inputs: "原创组织中权力主张、相对人的拒绝能力和具体资源归属"
  outputs: "名义权利/实际知情/责任承担对照场景"
  steps:
    - "先在现场说清由谁提出正当性主张"
    - "切换到承受者视角确认是否有真实选择"
    - "将程序结果与实质公平分别登记为已发生或未证明"
  missing_conditions: "任何历史法令真实性另证"
  counterexample_or_limit: "n265/p29显示承受官员对公开说辞有保留，但无法凭此单点推断全部土地案已依法终局。"
  status: "RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN"
  verification_state: "NOT_STARTED_STAGE1_5"
- id: f12
  title: "治理试点由争议到有限授权的状态框架"
  type: procedure
  source_chapter: "《晚明》n425/p27；《晚明》n519/p69；《晚明》n519/p70；《晚明》n520/p17"
  source_quote: ""
  source_quote_status: "COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA"
  source_loci:
    - "n425/p27"
    - "n519/p69"
    - "n519/p70"
    - "n520/p17"
  summary: |-
    制度争辩中的理念需要通过另一个角色实际提出异议才能成场。
    试点场景里询问意见与陪审者给出理由是不同的两个叙事动作。
    上级允许继续做有限试验并不等于批准推广或宣布永久公平。
    把小说的制度理想和虚构试点条件分开，不当作现实法律执行建议。
  tags: [pilots, counterarguments, governance-fiction]
  task_ids: [WM-07, WM-02]
  inputs: "原创制度提案、被约束人群、质疑者和裁决权限"
  outputs: "提案/试点/理由/条件许可/后续未知五态表与争议场"
  steps:
    - "让争论双方提出各自担忧与判断证据"
    - "在具体受影响者面前展示制度试验反应"
    - "明确记录继续试办的范围及禁止扩大之处"
  missing_conditions: "独立社会情境伦理评估与法律史核实"
  counterexample_or_limit: "n519/p69单为要求说明理由，需连读p70；n520/p17只是限制性许可。"
  status: "RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN"
  verification_state: "NOT_STARTED_STAGE1_5"
- id: f13
  title: "已演事件与后世讲述版本的分层框架"
  type: framework
  source_chapter: "《晚明》n166/p30；《晚明》n571/p5；《晚明》n571/p25"
  source_quote: ""
  source_quote_status: "COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA"
  source_loci:
    - "n166/p30"
    - "n571/p5"
    - "n571/p25"
  summary: |-
    书中早已出现说书现场，提供人们理解事件的第二种叙述渠道。
    结尾听众可以带着各自性格、记忆和偏见评论先前发生的事情。
    对版本的反讽与质疑并不意味着此前每一个现场都不曾发生。
    未来原创作品可保留多层讲述，但不得复制原书结尾茶馆结构、人物群或原语言。
  tags: [framing-story, testimony, narrative-echo]
  task_ids: [WM-09]
  inputs: "原创长期事件、两类信息来源和多年后的不同记忆者"
  outputs: "事实/见证/转述/当代评价四层叙事对照"
  steps:
    - "先把早期事件写成可独立检验的现场"
    - "为事件增加有选择性保留的信息版本"
    - "在后期让读者看到版本变化及其尚存歧义"
  missing_conditions: "必须原创新的场域和人物，避免沿用原场面"
  counterexample_or_limit: "n571的听众争论是对讲述的评价，不必推出前面所有章节都不可靠。"
  status: "RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN"
  verification_state: "NOT_STARTED_STAGE1_5"
- id: f14
  title: "重大历史线与家庭个体选择的双进度账"
  type: framework
  source_chapter: "《晚明》n339/p9；《晚明》n339/p10；《晚明》n339/p31；《晚明》n540/p33；《晚明》n569/p21"
  source_quote: ""
  source_quote_status: "COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA"
  source_loci:
    - "n339/p9"
    - "n339/p10"
    - "n339/p31"
    - "n540/p33"
    - "n569/p21"
  summary: |-
    当大规模组织扩张时，家庭内部关于工作、婚事和教育的矛盾仍可独立产生剧情。
    家长、兄妹、孩子的说法不必等于当事人的实际同意。
    跨段让人物携带自己先前尚未解决的愿望进入新局面。
    宏大战事成为一条背景压力，不自动完成私人生活的故事线。
  tags: [private-life, agency, long-running-subplot]
  task_ids: [WM-08, WM-06]
  inputs: "原创普通人的个人目标、亲属期望与公共事件的时间线"
  outputs: "宏观事件与个体愿望两条跨章节追踪表"
  steps:
    - "为非主角设定不依赖大战胜负的实际愿望"
    - "写出至少两名家庭成员不同意见"
    - "在后续时段检查被延迟的选择是否得到回应"
  missing_conditions: "应另设独立人物而不是沿用原著亲属网络"
  counterexample_or_limit: "n339/p10仅是长辈当场意见，不能替代妹妹本人的决定。"
  status: "RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN"
  verification_state: "NOT_STARTED_STAGE1_5"
- id: f15
  title: "内部方案与外部见证的两种真实性检验"
  type: framework
  source_chapter: "《晚明》n390/p25；《晚明》n494/p17；《晚明》n514/p34；《晚明》n561/p45"
  source_quote: ""
  source_quote_status: "COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA"
  source_loci:
    - "n390/p25"
    - "n494/p17"
    - "n514/p34"
    - "n561/p45"
  summary: |-
    组织的详细方案不是行动者在任何现场都能完全掌握的事实。
    内部会议里来自属员的资源或空间质疑可能改变主角自信。
    外来观察者能看到整齐与变化，却仍无法获知全部制度代价。
    某些战场场面存在看不清的情况，不能把旁观信息当作全知解释。
  tags: [organization-observation, pov-contrast, limits]
  task_ids: [WM-03, WM-05]
  inputs: "原创组织预案、执行现场、观察者的不同知识界限"
  outputs: "方案/执行/外部观察/无法确认事实四栏差异账"
  steps:
    - "先呈现组织预期与提出异议的具体角色"
    - "再展示一个不属于决策层的人能看见的结果"
    - "列出观察者没有渠道确认的代价和误判"
  missing_conditions: "避开真实战术可执行操作而只分析叙事镜头与认知"
  counterexample_or_limit: "n514/p34赞叹训练只能证明观察者印象，不是所有制度后果的独立评估。"
  status: "RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN"
  verification_state: "NOT_STARTED_STAGE1_5"
- id: f16
  title: "想法—评估—否决—组织后果的创新检验"
  type: troubleshooting
  source_chapter: "《晚明》n345/p29；《晚明》n437/p6；《晚明》n437/p29"
  source_quote: ""
  source_quote_status: "COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA"
  source_loci:
    - "n345/p29"
    - "n437/p6"
    - "n437/p29"
  summary: |-
    源书同时出现商业模仿的竞争和新技术想法经组织判断后被否决的场景。
    提出新技术不等于成功试制，试制不等于可推广，终端收益更需后续市场反应。
    组织调节生产任务并非全由发明者一句话完成。
    提取为文学叙事的失败分支，绝不转化为现实武器设计或商业打击教程。
  tags: [innovation, falsifiability, institution]
  task_ids: [WM-04, WM-07]
  inputs: "原创技术想法、评估者、既有替代方案及资源限制"
  outputs: "提出/比较/修订/拒绝/后续责任的分支表"
  steps:
    - "先让构思有明确希望解决的缺口"
    - "安排具备独立意见的评价者提出不利证据"
    - "保留失败或延期分支，书写这项决定如何影响人物关系"
  missing_conditions: "真实技术性能与安全性不可从小说推出"
  counterexample_or_limit: "n437/p6确实有方案被否决，不应扭曲成小说中的所有创新必定成功。"
  status: "RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN"
  verification_state: "NOT_STARTED_STAGE1_5"
- id: f17
  title: "新义务产生后跨章节偿还的追踪框架"
  type: procedure
  source_chapter: "《晚明》n089/p26；《晚明》n305/p35；《晚明》n529/p38；《晚明》n529/p40；《晚明》n530/p1"
  source_quote: ""
  source_quote_status: "COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA"
  source_loci:
    - "n089/p26"
    - "n305/p35"
    - "n529/p38"
    - "n529/p40"
    - "n530/p1"
  summary: |-
    角色表达招募或供给需求只是故事产生新义务的时点。
    当章会议对计划作出折中并不等于后来实际执行。
    物资统计、时间变更和上级风险预案可以发生在分离的章节与人物视角。
    用未决事项作为后续叙事记忆，而非为了制造循环冲突机械拖延。
  tags: [longform-continuity, unpaid-debt, future-checkpoint]
  task_ids: [WM-04, WM-06, WM-08]
  inputs: "虚构故事中提出的职责、负责人与最迟兑现的剧情检查点"
  outputs: "申请/承诺/执行/变更/兑现或失约五态事件表"
  steps:
    - "记下最初提出需求者与对方真实答复"
    - "给计划增加会改变成本的后续事件"
    - "由后来的独立人物确认结果，未确认就标未知"
  missing_conditions: "长篇具体角色、地点与时序应按全新原创世界构造"
  counterexample_or_limit: "n530/p1安排运输月份并不证实秋冬需求均已实际交付。"
  status: "RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN"
  verification_state: "NOT_STARTED_STAGE1_5"
```

## 覆盖核查与来源隔离（Stage1.5前不得直接升级）

本批框架候选17个，任务关联：WM-01—WM-09 均有明确关联，但“被候选提及”不等于后续 V1 充分证据已通过。原书极少数单章可独立成立的完整场景也保留，不用重复出现的次数当筛选门槛。所有定位在`FRAMEWORK_EVIDENCE.tsv`，严格按原用户EPUB计算不可逆 SHA；只发布观察归纳，不发布原文。

框架类的范围只包括跨场决策结构、故事程序、组织状态与验证链；其它四路候选未启动。每条均明确缺口与竞争解释，旧R007—R024的任何收据声明未经独立回到原文不得自动作为证据；例如旧R013 n143/p29、旧R019 n265/p28只可在R042纠正资料约束内使用。禁止从原著复制具体人物配置、情节序列、标识性语言。B=PROVISIONAL, C=NOT_RUN, SKILL认证=0。
