# 《晚明》｜Stage1 原版仓颉术语提取器（R047）

> 原版来源：Cangjie v2.5 `methodology/02-stage1-parallel-extract.md` 和 `extractors/glossary-extractor.md`；输入为R042用户已批准的整书研究框架以及用户私有原始EPUB。**仅原始术语候选，B PROVISIONAL、C NOT_RUN。**

> 关键证据限制：这些词在原著中确实出现，但书中并不总有形式化定义；因此原版字段 `author_definition` 在无明示定义时留空，`textual_usage`是研究者对书中语境的转述，不是虚构作者原话。公开仓库不上传受版权保护的正文，保留 `source_quote: ""` 和私有段落SHA。凡涉及明末官署、法律和商业制度，均须独立史料外证才能宣布历史真实性。

```yaml
- id: g01
  term: "卫所"
  type: term
  source_chapter: "n039/p45;n050/p27"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SHA
  author_definition: ""
  definition_status: SOURCE_CONTEXT_PARAPHRASE_NOT_EXPLICIT_AUTHOR_DEFINITION
  textual_usage: "小说人物讨论加入军籍、武职来源以及“纳级”与正式授职之间的差别。"
  key_distinction: "≠得到一纸官职即可获得完整可用组织；作品中的卫所与募兵入口不同，现代穿越者仍需要额外条件。"
  why_it_matters: "原创小说构思中，≠得到一纸官职即可获得完整可用组织；作品中的卫所与募兵入口不同，现代穿越者仍需要额外条件。避免把小说词汇直接替换成现代字典释义；需回原始场景判明人物信息与组织实际状态。"
  provenance: HISTORICAL_INSTITUTION_IN_FICTION
  source_loci:
    - "n039/p45"
    - "n050/p27"
  corpus_occurrences: 146
  source_chapter_hits: 68
  summary: |-
    小说用语：小说人物讨论加入军籍、武职来源以及“纳级”与正式授职之间的差别。
    与通俗理解的关键差异：≠得到一纸官职即可获得完整可用组织；作品中的卫所与募兵入口不同，现代穿越者仍需要额外条件。
    来源身份：HISTORICAL_INSTITUTION_IN_FICTION，并非作者发表的独立制度词典定义。
    下游用途：针对WM-01、WM-03任务的概念消歧和事实/主张分层。
    未验证边界：具体明代卫所法律地位、品秩和地域差异必须查独立史料，故事人物解释不可充当历史法规。
  tags: [term, source-scoped, historical-fiction]
  task_ids: [WM-01, WM-03]
  missing_conditions: "具体明代卫所法律地位、品秩和地域差异必须查独立史料，故事人物解释不可充当历史法规。"
  verification_state: STAGE1_RAW_B_PROVISIONAL_C_NOT_RUN
- id: g02
  term: "官身"
  type: term
  source_chapter: "n039/p43;n090/p16"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SHA
  author_definition: ""
  definition_status: SOURCE_CONTEXT_PARAPHRASE_NOT_EXPLICIT_AUTHOR_DEFINITION
  textual_usage: "角色寻求进入官场或武职体系的名分，家庭成员亦把它与体面、安全期待联系起来。"
  key_distinction: "≠个人能力、忠诚或可立即支配人力；有资格入口仍可能只得到社交身份和名义认可。"
  why_it_matters: "原创小说构思中，≠个人能力、忠诚或可立即支配人力；有资格入口仍可能只得到社交身份和名义认可。避免把小说词汇直接替换成现代字典释义；需回原始场景判明人物信息与组织实际状态。"
  provenance: IN_STORY_STATUS_AND_ACCESS
  source_loci:
    - "n039/p43"
    - "n090/p16"
  corpus_occurrences: 22
  source_chapter_hits: 16
  summary: |-
    小说用语：角色寻求进入官场或武职体系的名分，家庭成员亦把它与体面、安全期待联系起来。
    与通俗理解的关键差异：≠个人能力、忠诚或可立即支配人力；有资格入口仍可能只得到社交身份和名义认可。
    来源身份：IN_STORY_STATUS_AND_ACCESS，并非作者发表的独立制度词典定义。
    下游用途：针对WM-01、WM-02任务的概念消歧和事实/主张分层。
    未验证边界：角色在某一场宴饮中的评价并不证明所有人都认可同一官身。
  tags: [term, source-scoped, historical-fiction]
  task_ids: [WM-01, WM-02]
  missing_conditions: "角色在某一场宴饮中的评价并不证明所有人都认可同一官身。"
  verification_state: STAGE1_RAW_B_PROVISIONAL_C_NOT_RUN
- id: g03
  term: "军户"
  type: term
  source_chapter: "n039/p45;n071/p11"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SHA
  author_definition: ""
  definition_status: SOURCE_CONTEXT_PARAPHRASE_NOT_EXPLICIT_AUTHOR_DEFINITION
  textual_usage: "小说将军户作为历史人身与军籍类别呈现，又展示它与生活、盐业、地方权势关系交错。"
  key_distinction: "≠现代受薪军人，也不等于全部军户拥有同样工作及自由；人物对军籍与募兵的说法需要保留主语。"
  why_it_matters: "原创小说构思中，≠现代受薪军人，也不等于全部军户拥有同样工作及自由；人物对军籍与募兵的说法需要保留主语。避免把小说词汇直接替换成现代字典释义；需回原始场景判明人物信息与组织实际状态。"
  provenance: HISTORICAL_INSTITUTION_IN_FICTION
  source_loci:
    - "n039/p45"
    - "n071/p11"
  corpus_occurrences: 219
  source_chapter_hits: 88
  summary: |-
    小说用语：小说将军户作为历史人身与军籍类别呈现，又展示它与生活、盐业、地方权势关系交错。
    与通俗理解的关键差异：≠现代受薪军人，也不等于全部军户拥有同样工作及自由；人物对军籍与募兵的说法需要保留主语。
    来源身份：HISTORICAL_INSTITUTION_IN_FICTION，并非作者发表的独立制度词典定义。
    下游用途：针对WM-01、WM-08任务的概念消歧和事实/主张分层。
    未验证边界：不能直接把书中军户经营、纳籍及军役细节当史实或普遍合法做法。
  tags: [term, source-scoped, historical-fiction]
  task_ids: [WM-01, WM-08]
  missing_conditions: "不能直接把书中军户经营、纳籍及军役细节当史实或普遍合法做法。"
  verification_state: STAGE1_RAW_B_PROVISIONAL_C_NOT_RUN
- id: g04
  term: "文登营"
  type: term
  source_chapter: "n087/p54;n143/p7"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SHA
  author_definition: ""
  definition_status: SOURCE_CONTEXT_PARAPHRASE_NOT_EXPLICIT_AUTHOR_DEFINITION
  textual_usage: "前期围绕既有兵额和地方驻防的组织用语，后随人物与场景变化成为持续被指认的军事组织。"
  key_distinction: "≠最初账面兵额，也不等于后期登州镇的全部层级；其能力与规模必须按剧情阶段分别确认。"
  why_it_matters: "原创小说构思中，≠最初账面兵额，也不等于后期登州镇的全部层级；其能力与规模必须按剧情阶段分别确认。避免把小说词汇直接替换成现代字典释义；需回原始场景判明人物信息与组织实际状态。"
  provenance: NOVEL_ORGANIZATION_AND_EVOLVING_NAME
  source_loci:
    - "n087/p54"
    - "n143/p7"
  corpus_occurrences: 1319
  source_chapter_hits: 206
  summary: |-
    小说用语：前期围绕既有兵额和地方驻防的组织用语，后随人物与场景变化成为持续被指认的军事组织。
    与通俗理解的关键差异：≠最初账面兵额，也不等于后期登州镇的全部层级；其能力与规模必须按剧情阶段分别确认。
    来源身份：NOVEL_ORGANIZATION_AND_EVOLVING_NAME，并非作者发表的独立制度词典定义。
    下游用途：针对WM-03、WM-05任务的概念消歧和事实/主张分层。
    未验证边界：名称多次出现不自动证明原书外真实历史存在相同组织演进。
  tags: [term, source-scoped, historical-fiction]
  task_ids: [WM-03, WM-05]
  missing_conditions: "名称多次出现不自动证明原书外真实历史存在相同组织演进。"
  verification_state: STAGE1_RAW_B_PROVISIONAL_C_NOT_RUN
- id: g05
  term: "登州镇"
  type: term
  source_chapter: "n143/p39;n494/p11"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SHA
  author_definition: ""
  definition_status: SOURCE_CONTEXT_PARAPHRASE_NOT_EXPLICIT_AUTHOR_DEFINITION
  textual_usage: "人物被以登州镇军职称呼，后期这个名号又关联人员安置和地方民生职责。"
  key_distinction: "≠文登营单一队伍；用于分析组织层级扩大后责任与人事分配的变化。"
  why_it_matters: "原创小说构思中，≠文登营单一队伍；用于分析组织层级扩大后责任与人事分配的变化。避免把小说词汇直接替换成现代字典释义；需回原始场景判明人物信息与组织实际状态。"
  provenance: NOVEL_ORGANIZATION_AND_POLITICAL_SCOPE
  source_loci:
    - "n143/p39"
    - "n494/p11"
  corpus_occurrences: 1503
  source_chapter_hits: 271
  summary: |-
    小说用语：人物被以登州镇军职称呼，后期这个名号又关联人员安置和地方民生职责。
    与通俗理解的关键差异：≠文登营单一队伍；用于分析组织层级扩大后责任与人事分配的变化。
    来源身份：NOVEL_ORGANIZATION_AND_POLITICAL_SCOPE，并非作者发表的独立制度词典定义。
    下游用途：针对WM-03、WM-06任务的概念消歧和事实/主张分层。
    未验证边界：不可把小说组织体制当完全准确的明末制度模型。
  tags: [term, source-scoped, historical-fiction]
  task_ids: [WM-03, WM-06]
  missing_conditions: "不可把小说组织体制当完全准确的明末制度模型。"
  verification_state: STAGE1_RAW_B_PROVISIONAL_C_NOT_RUN
- id: g06
  term: "军功"
  type: term
  source_chapter: "n103/p27;n143/p53"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SHA
  author_definition: ""
  definition_status: SOURCE_CONTEXT_PARAPHRASE_NOT_EXPLICIT_AUTHOR_DEFINITION
  textual_usage: "人物把军事成就看作升迁依据，也会因上级改变其职责安排而重新估算可得功劳。"
  key_distinction: "≠现场表现自动变成官爵与资源，也不等于奖酬分配公平。"
  why_it_matters: "原创小说构思中，≠现场表现自动变成官爵与资源，也不等于奖酬分配公平。避免把小说词汇直接替换成现代字典释义；需回原始场景判明人物信息与组织实际状态。"
  provenance: IN_STORY_RECOGNITION_AND_REWARD
  source_loci:
    - "n103/p27"
    - "n143/p53"
  corpus_occurrences: 140
  source_chapter_hits: 85
  summary: |-
    小说用语：人物把军事成就看作升迁依据，也会因上级改变其职责安排而重新估算可得功劳。
    与通俗理解的关键差异：≠现场表现自动变成官爵与资源，也不等于奖酬分配公平。
    来源身份：IN_STORY_RECOGNITION_AND_REWARD，并非作者发表的独立制度词典定义。
    下游用途：针对WM-03、WM-06任务的概念消歧和事实/主张分层。
    未验证边界：不涉及具体战场行为；史实授功制度、金额和官阶需要独立外证。
  tags: [term, source-scoped, historical-fiction]
  task_ids: [WM-03, WM-06]
  missing_conditions: "不涉及具体战场行为；史实授功制度、金额和官阶需要独立外证。"
  verification_state: STAGE1_RAW_B_PROVISIONAL_C_NOT_RUN
- id: g07
  term: "屯堡"
  type: term
  source_chapter: "n103/p46;n425/p21"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SHA
  author_definition: ""
  definition_status: SOURCE_CONTEXT_PARAPHRASE_NOT_EXPLICIT_AUTHOR_DEFINITION
  textual_usage: "角色设想建立乡村屯住组织，后续故事描写已有基层管理与晋升结构。"
  key_distinction: "≠孤立居住建筑；它在小说中牵连人员、生活、学习及基层权力，但某处方案仍可能停留在提议。"
  why_it_matters: "原创小说构思中，≠孤立居住建筑；它在小说中牵连人员、生活、学习及基层权力，但某处方案仍可能停留在提议。避免把小说词汇直接替换成现代字典释义；需回原始场景判明人物信息与组织实际状态。"
  provenance: IN_STORY_SETTLEMENT_AND_ORGANIZATION
  source_loci:
    - "n103/p46"
    - "n425/p21"
  corpus_occurrences: 597
  source_chapter_hits: 143
  summary: |-
    小说用语：角色设想建立乡村屯住组织，后续故事描写已有基层管理与晋升结构。
    与通俗理解的关键差异：≠孤立居住建筑；它在小说中牵连人员、生活、学习及基层权力，但某处方案仍可能停留在提议。
    来源身份：IN_STORY_SETTLEMENT_AND_ORGANIZATION，并非作者发表的独立制度词典定义。
    下游用途：针对WM-03、WM-08任务的概念消歧和事实/主张分层。
    未验证边界：词频高不代表每个屯堡生活条件相同，历史名称要与小说制度改造分开。
  tags: [term, source-scoped, historical-fiction]
  task_ids: [WM-03, WM-08]
  missing_conditions: "词频高不代表每个屯堡生活条件相同，历史名称要与小说制度改造分开。"
  verification_state: STAGE1_RAW_B_PROVISIONAL_C_NOT_RUN
- id: g08
  term: "屯长"
  type: term
  source_chapter: "n194/p36;n425/p21"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SHA
  author_definition: ""
  definition_status: SOURCE_CONTEXT_PARAPHRASE_NOT_EXPLICIT_AUTHOR_DEFINITION
  textual_usage: "小说中基层屯长被赋予某些治理职责，并被其他人物描述为基层岗位与提升途径。"
  key_distinction: "≠拥有所有资源处置权；名称与实际权限需要连同上级机构与投诉事件分开写。"
  why_it_matters: "原创小说构思中，≠拥有所有资源处置权；名称与实际权限需要连同上级机构与投诉事件分开写。避免把小说词汇直接替换成现代字典释义；需回原始场景判明人物信息与组织实际状态。"
  provenance: IN_STORY_LOCAL_ROLE
  source_loci:
    - "n194/p36"
    - "n425/p21"
  corpus_occurrences: 93
  source_chapter_hits: 33
  summary: |-
    小说用语：小说中基层屯长被赋予某些治理职责，并被其他人物描述为基层岗位与提升途径。
    与通俗理解的关键差异：≠拥有所有资源处置权；名称与实际权限需要连同上级机构与投诉事件分开写。
    来源身份：IN_STORY_LOCAL_ROLE，并非作者发表的独立制度词典定义。
    下游用途：针对WM-03、WM-07任务的概念消歧和事实/主张分层。
    未验证边界：个别人物的职责安排和岗位收益并不是普遍史实法规。
  tags: [term, source-scoped, historical-fiction]
  task_ids: [WM-03, WM-07]
  missing_conditions: "个别人物的职责安排和岗位收益并不是普遍史实法规。"
  verification_state: STAGE1_RAW_B_PROVISIONAL_C_NOT_RUN
- id: g09
  term: "商社"
  type: term
  source_chapter: "n297/p2;n380/p27"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SHA
  author_definition: ""
  definition_status: SOURCE_CONTEXT_PARAPHRASE_NOT_EXPLICIT_AUTHOR_DEFINITION
  textual_usage: "在故事中经营对外商品与相关业务的组织，人物讨论其渠道权限及与生产方的不同利益。"
  key_distinction: "≠单间店铺，也不等于厂房或地方政府；有市场渠道不保证新产品研发及其他主体同意。"
  why_it_matters: "原创小说构思中，≠单间店铺，也不等于厂房或地方政府；有市场渠道不保证新产品研发及其他主体同意。避免把小说词汇直接替换成现代字典释义；需回原始场景判明人物信息与组织实际状态。"
  provenance: NOVEL_COMMERCIAL_ORGANIZATION
  source_loci:
    - "n297/p2"
    - "n380/p27"
  corpus_occurrences: 438
  source_chapter_hits: 123
  summary: |-
    小说用语：在故事中经营对外商品与相关业务的组织，人物讨论其渠道权限及与生产方的不同利益。
    与通俗理解的关键差异：≠单间店铺，也不等于厂房或地方政府；有市场渠道不保证新产品研发及其他主体同意。
    来源身份：NOVEL_COMMERCIAL_ORGANIZATION，并非作者发表的独立制度词典定义。
    下游用途：针对WM-02、WM-04任务的概念消歧和事实/主张分层。
    未验证边界：商社作为小说组织的股权与管理细节不可未经外证当真实明代商制。
  tags: [term, source-scoped, historical-fiction]
  task_ids: [WM-02, WM-04]
  missing_conditions: "商社作为小说组织的股权与管理细节不可未经外证当真实明代商制。"
  verification_state: STAGE1_RAW_B_PROVISIONAL_C_NOT_RUN
- id: g10
  term: "牙行"
  type: term
  source_chapter: "n290/p45;n345/p29"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SHA
  author_definition: ""
  definition_status: SOURCE_CONTEXT_PARAPHRASE_NOT_EXPLICIT_AUTHOR_DEFINITION
  textual_usage: "人物报告客商被交易中间人引导甚至排斥，以及渠道受到本地经营对手影响。"
  key_distinction: "≠现代零售门店；它在小说中指涉买卖中介和获客路径，被不同商人争取与制约。"
  why_it_matters: "原创小说构思中，≠现代零售门店；它在小说中指涉买卖中介和获客路径，被不同商人争取与制约。避免把小说词汇直接替换成现代字典释义；需回原始场景判明人物信息与组织实际状态。"
  provenance: HISTORICAL_MARKET_INTERMEDIARY_IN_FICTION
  source_loci:
    - "n290/p45"
    - "n345/p29"
  corpus_occurrences: 62
  source_chapter_hits: 19
  summary: |-
    小说用语：人物报告客商被交易中间人引导甚至排斥，以及渠道受到本地经营对手影响。
    与通俗理解的关键差异：≠现代零售门店；它在小说中指涉买卖中介和获客路径，被不同商人争取与制约。
    来源身份：HISTORICAL_MARKET_INTERMEDIARY_IN_FICTION，并非作者发表的独立制度词典定义。
    下游用途：针对WM-04任务的概念消歧和事实/主张分层。
    未验证边界：具体垄断、强制或欺骗是小说剧情，不能转成现实不正当竞争教程。
  tags: [term, source-scoped, historical-fiction]
  task_ids: [WM-04]
  missing_conditions: "具体垄断、强制或欺骗是小说剧情，不能转成现实不正当竞争教程。"
  verification_state: STAGE1_RAW_B_PROVISIONAL_C_NOT_RUN
- id: g11
  term: "民事部"
  type: term
  source_chapter: "n307/p12;n425/p35"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SHA
  author_definition: ""
  definition_status: SOURCE_CONTEXT_PARAPHRASE_NOT_EXPLICIT_AUTHOR_DEFINITION
  textual_usage: "小说里的机构分工名号，负责与一般居民生活有关的事项，并存在与其他部门争权的讨论。"
  key_distinction: "≠抽象的民心或单一善政宣言；名为民生部门并不代表资源协调自动结束。"
  why_it_matters: "原创小说构思中，≠抽象的民心或单一善政宣言；名为民生部门并不代表资源协调自动结束。避免把小说词汇直接替换成现代字典释义；需回原始场景判明人物信息与组织实际状态。"
  provenance: NOVEL_ADMINISTRATIVE_DEPARTMENT
  source_loci:
    - "n307/p12"
    - "n425/p35"
  corpus_occurrences: 100
  source_chapter_hits: 51
  summary: |-
    小说用语：小说里的机构分工名号，负责与一般居民生活有关的事项，并存在与其他部门争权的讨论。
    与通俗理解的关键差异：≠抽象的民心或单一善政宣言；名为民生部门并不代表资源协调自动结束。
    来源身份：NOVEL_ADMINISTRATIVE_DEPARTMENT，并非作者发表的独立制度词典定义。
    下游用途：针对WM-02、WM-07、WM-08任务的概念消歧和事实/主张分层。
    未验证边界：不能将故事里的现代部门名称直接写成明代既定真实官署。
  tags: [term, source-scoped, historical-fiction]
  task_ids: [WM-02, WM-07, WM-08]
  missing_conditions: "不能将故事里的现代部门名称直接写成明代既定真实官署。"
  verification_state: STAGE1_RAW_B_PROVISIONAL_C_NOT_RUN
- id: g12
  term: "军饷"
  type: term
  source_chapter: "n305/p4;n494/p4"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SHA
  author_definition: ""
  definition_status: SOURCE_CONTEXT_PARAPHRASE_NOT_EXPLICIT_AUTHOR_DEFINITION
  textual_usage: "角色讨论预计可获军饷及退伍后需要结清的既有收入和待遇。"
  key_distinction: "≠上级许诺就已到账；收入、实际支付与离职结算存在不同时间状态。"
  why_it_matters: "原创小说构思中，≠上级许诺就已到账；收入、实际支付与离职结算存在不同时间状态。避免把小说词汇直接替换成现代字典释义；需回原始场景判明人物信息与组织实际状态。"
  provenance: IN_STORY_FINANCIAL_OBLIGATION
  source_loci:
    - "n305/p4"
    - "n494/p4"
  corpus_occurrences: 135
  source_chapter_hits: 82
  summary: |-
    小说用语：角色讨论预计可获军饷及退伍后需要结清的既有收入和待遇。
    与通俗理解的关键差异：≠上级许诺就已到账；收入、实际支付与离职结算存在不同时间状态。
    来源身份：IN_STORY_FINANCIAL_OBLIGATION，并非作者发表的独立制度词典定义。
    下游用途：针对WM-03、WM-04、WM-08任务的概念消歧和事实/主张分层。
    未验证边界：金额、上级承诺及支付规则是小说叙事事实，不可当现代会计或历史定额。
  tags: [term, source-scoped, historical-fiction]
  task_ids: [WM-03, WM-04, WM-08]
  missing_conditions: "金额、上级承诺及支付规则是小说叙事事实，不可当现代会计或历史定额。"
  verification_state: STAGE1_RAW_B_PROVISIONAL_C_NOT_RUN
- id: g13
  term: "陪审"
  type: term
  source_chapter: "n518/p7;n519/p28"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SHA
  author_definition: ""
  definition_status: SOURCE_CONTEXT_PARAPHRASE_NOT_EXPLICIT_AUTHOR_DEFINITION
  textual_usage: "小说的局部听审试验中由非专业人员参与评价事件，旁边仍有主持与裁断职位。"
  key_distinction: "≠普通人一旦参加就能保证公平；也不能把询问他们意见和其实际解释同一化。"
  why_it_matters: "原创小说构思中，≠普通人一旦参加就能保证公平；也不能把询问他们意见和其实际解释同一化。避免把小说词汇直接替换成现代字典释义；需回原始场景判明人物信息与组织实际状态。"
  provenance: NOVEL_JUDICIAL_EXPERIMENT_TERM
  source_loci:
    - "n518/p7"
    - "n519/p28"
  corpus_occurrences: 30
  source_chapter_hits: 4
  summary: |-
    小说用语：小说的局部听审试验中由非专业人员参与评价事件，旁边仍有主持与裁断职位。
    与通俗理解的关键差异：≠普通人一旦参加就能保证公平；也不能把询问他们意见和其实际解释同一化。
    来源身份：NOVEL_JUDICIAL_EXPERIMENT_TERM，并非作者发表的独立制度词典定义。
    下游用途：针对WM-02、WM-07任务的概念消歧和事实/主张分层。
    未验证边界：不把虚构陪审实验当现实法律意见或成熟法庭制度。
  tags: [term, source-scoped, historical-fiction]
  task_ids: [WM-02, WM-07]
  missing_conditions: "不把虚构陪审实验当现实法律意见或成熟法庭制度。"
  verification_state: STAGE1_RAW_B_PROVISIONAL_C_NOT_RUN
- id: g14
  term: "试点"
  type: term
  source_chapter: "n425/p30;n520/p17"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SHA
  author_definition: ""
  definition_status: SOURCE_CONTEXT_PARAPHRASE_NOT_EXPLICIT_AUTHOR_DEFINITION
  textual_usage: "人物面对重大机构变化选择先限定范围试行，另处许可被明确附上不扩大条件。"
  key_distinction: "≠推广已经批准，更不等于结果经过验证；角色愿意继续试办只是一个阶段状态。"
  why_it_matters: "原创小说构思中，≠推广已经批准，更不等于结果经过验证；角色愿意继续试办只是一个阶段状态。避免把小说词汇直接替换成现代字典释义；需回原始场景判明人物信息与组织实际状态。"
  provenance: CHARACTER_PROPOSED_LIMITED_TRIAL
  source_loci:
    - "n425/p30"
    - "n520/p17"
  corpus_occurrences: 13
  source_chapter_hits: 8
  summary: |-
    小说用语：人物面对重大机构变化选择先限定范围试行，另处许可被明确附上不扩大条件。
    与通俗理解的关键差异：≠推广已经批准，更不等于结果经过验证；角色愿意继续试办只是一个阶段状态。
    来源身份：CHARACTER_PROPOSED_LIMITED_TRIAL，并非作者发表的独立制度词典定义。
    下游用途：针对WM-07任务的概念消歧和事实/主张分层。
    未验证边界：某一试验的价值仍取决于后续受影响者与实际结果，不能凭口头授权称制度成功。
  tags: [term, source-scoped, historical-fiction]
  task_ids: [WM-07]
  missing_conditions: "某一试验的价值仍取决于后续受影响者与实际结果，不能凭口头授权称制度成功。"
  verification_state: STAGE1_RAW_B_PROVISIONAL_C_NOT_RUN
- id: g15
  term: "塘报"
  type: term
  source_chapter: "n102/p64;n285/p5"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SHA
  author_definition: ""
  definition_status: SOURCE_CONTEXT_PARAPHRASE_NOT_EXPLICIT_AUTHOR_DEFINITION
  textual_usage: "原文既有带日期的报告来源，也描写上级经转送塘报获得消息后作出反应。"
  key_distinction: "≠全知叙述者直接证实的事实；报告、传递、接收及验证必须分别标明。"
  why_it_matters: "原创小说构思中，≠全知叙述者直接证实的事实；报告、传递、接收及验证必须分别标明。避免把小说词汇直接替换成现代字典释义；需回原始场景判明人物信息与组织实际状态。"
  provenance: HISTORICAL_REPORTING_CHANNEL_IN_FICTION
  source_loci:
    - "n102/p64"
    - "n285/p5"
  corpus_occurrences: 70
  source_chapter_hits: 42
  summary: |-
    小说用语：原文既有带日期的报告来源，也描写上级经转送塘报获得消息后作出反应。
    与通俗理解的关键差异：≠全知叙述者直接证实的事实；报告、传递、接收及验证必须分别标明。
    来源身份：HISTORICAL_REPORTING_CHANNEL_IN_FICTION，并非作者发表的独立制度词典定义。
    下游用途：针对WM-05、WM-09任务的概念消歧和事实/主张分层。
    未验证边界：文本中引用的塘报日期和所载事实未逐件与外部一手档案交叉核证。
  tags: [term, source-scoped, historical-fiction]
  task_ids: [WM-05, WM-09]
  missing_conditions: "文本中引用的塘报日期和所载事实未逐件与外部一手档案交叉核证。"
  verification_state: STAGE1_RAW_B_PROVISIONAL_C_NOT_RUN
- id: g16
  term: "工坊"
  type: term
  source_chapter: "n088/p23;n437/p7"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SHA
  author_definition: ""
  definition_status: SOURCE_CONTEXT_PARAPHRASE_NOT_EXPLICIT_AUTHOR_DEFINITION
  textual_usage: "小说描写产品制造场所、检查人员与具体管理差异，也涉及不同部门的验收职责。"
  key_distinction: "≠一项想法已被制成产品；工坊生产、质检和资源许可分别对应不同故事状态。"
  why_it_matters: "原创小说构思中，≠一项想法已被制成产品；工坊生产、质检和资源许可分别对应不同故事状态。避免把小说词汇直接替换成现代字典释义；需回原始场景判明人物信息与组织实际状态。"
  provenance: IN_STORY_PRODUCTION_ORGANIZATION
  source_loci:
    - "n088/p23"
    - "n437/p7"
  corpus_occurrences: 206
  source_chapter_hits: 81
  summary: |-
    小说用语：小说描写产品制造场所、检查人员与具体管理差异，也涉及不同部门的验收职责。
    与通俗理解的关键差异：≠一项想法已被制成产品；工坊生产、质检和资源许可分别对应不同故事状态。
    来源身份：IN_STORY_PRODUCTION_ORGANIZATION，并非作者发表的独立制度词典定义。
    下游用途：针对WM-03、WM-04任务的概念消歧和事实/主张分层。
    未验证边界：不抽取小说危险器械与实物制造的实施步骤。
  tags: [term, source-scoped, historical-fiction]
  task_ids: [WM-03, WM-04]
  missing_conditions: "不抽取小说危险器械与实物制造的实施步骤。"
  verification_state: STAGE1_RAW_B_PROVISIONAL_C_NOT_RUN
- id: g17
  term: "评书"
  type: term
  source_chapter: "n166/p25;n571/p64"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SHA
  author_definition: ""
  definition_status: SOURCE_CONTEXT_PARAPHRASE_NOT_EXPLICIT_AUTHOR_DEFINITION
  textual_usage: "作品中前后出现职业说书与公开讲述场景，用于显示后来听众接触事件时的讲述媒介。"
  key_distinction: "≠事件本身；一场演出有选择性叙述与听众期待，无法自动替代此前发生过的所有场景。"
  why_it_matters: "原创小说构思中，≠事件本身；一场演出有选择性叙述与听众期待，无法自动替代此前发生过的所有场景。避免把小说词汇直接替换成现代字典释义；需回原始场景判明人物信息与组织实际状态。"
  provenance: IN_STORY_PUBLIC_RETELLING
  source_loci:
    - "n166/p25"
    - "n571/p64"
  corpus_occurrences: 49
  source_chapter_hits: 20
  summary: |-
    小说用语：作品中前后出现职业说书与公开讲述场景，用于显示后来听众接触事件时的讲述媒介。
    与通俗理解的关键差异：≠事件本身；一场演出有选择性叙述与听众期待，无法自动替代此前发生过的所有场景。
    来源身份：IN_STORY_PUBLIC_RETELLING，并非作者发表的独立制度词典定义。
    下游用途：针对WM-02、WM-09任务的概念消歧和事实/主张分层。
    未验证边界：不得复制原著专属尾声布景或把说书细节认作历史档案。
  tags: [term, source-scoped, historical-fiction]
  task_ids: [WM-02, WM-09]
  missing_conditions: "不得复制原著专属尾声布景或把说书细节认作历史档案。"
  verification_state: STAGE1_RAW_B_PROVISIONAL_C_NOT_RUN
- id: g18
  term: "情报"
  type: term
  source_chapter: "n107/p6;n556/p4"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SHA
  author_definition: ""
  definition_status: SOURCE_CONTEXT_PARAPHRASE_NOT_EXPLICIT_AUTHOR_DEFINITION
  textual_usage: "人物依据他人传回的消息形成判断，后续也出现未曾在先前情报里出现的新参与者。"
  key_distinction: "≠所有人物均已确知的全貌；已收到、角色推测、事后被纠正的范围不同。"
  why_it_matters: "原创小说构思中，≠所有人物均已确知的全貌；已收到、角色推测、事后被纠正的范围不同。避免把小说词汇直接替换成现代字典释义；需回原始场景判明人物信息与组织实际状态。"
  provenance: IN_STORY_PARTIAL_INFORMATION
  source_loci:
    - "n107/p6"
    - "n556/p4"
  corpus_occurrences: 632
  source_chapter_hits: 191
  summary: |-
    小说用语：人物依据他人传回的消息形成判断，后续也出现未曾在先前情报里出现的新参与者。
    与通俗理解的关键差异：≠所有人物均已确知的全貌；已收到、角色推测、事后被纠正的范围不同。
    来源身份：IN_STORY_PARTIAL_INFORMATION，并非作者发表的独立制度词典定义。
    下游用途：针对WM-05、WM-09任务的概念消歧和事实/主张分层。
    未验证边界：仅提取叙事有限视角，不能变成现实军事侦察或规避执行指导。
  tags: [term, source-scoped, historical-fiction]
  task_ids: [WM-05, WM-09]
  missing_conditions: "仅提取叙事有限视角，不能变成现实军事侦察或规避执行指导。"
  verification_state: STAGE1_RAW_B_PROVISIONAL_C_NOT_RUN
```

## 术语筛选边界

- 原版预计每书5—20条核心术语，本轮18条。每条在用户原始EPUB里至少出现3次（同时均核查≥2处原始语境）；`corpus_occurrences`是**非空正文段落中的精确子串总出现次数**，`source_chapter_hits`是至少含词一次的有效章数，不是作者明确下定义的次数。完整统计和哈希在`GLOSSARY_CENSUS.tsv`、`GLOSSARY_EVIDENCE.tsv`。
- `文登营/登州镇`是小说里不同时间/组织层级的称谓；`官身/卫所/军户`必须分开；`屯堡/屯长`是地点与岗位；`商社/牙行`是组织与中介；`塘报/情报/评书`分别涉及官方报告、有限消息和公开再讲述。跨词关系目前仅用于概念消歧，**不在Stage1制作Capability Bundle的Stage3链接**。
- 不额外收入`叙述权`、`组织能力`、`合法性差分`等研究者自造抽象标签，因为无法无误地标作原小说固有术语。历史类名词并未经过外部史料确定具体通行定义；时代表达、现代穿越者的用法及书中制度创新明确隔离。
- WM-01—WM-09九项任务各有词条说明概念来源，**只算Raw候选关联，不是Stage1.5后的任务充分性或原创写作验证**。保留R042针对14条历史旧机制的隔离，旧文学质量债未解封。此文件只执行第五个glossary extractor，未运行三重验证V1/V2/V3、Nuwa后续阶段或密封盲测。
