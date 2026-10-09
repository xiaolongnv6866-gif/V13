# 《晚明》Stage1案例提取器｜R045原始候选

本文件严格使用Cangjie v2.5案例提取器的独立职责（原书具体例子、明确bound_to、真实可见outcome），源于用户私有小说正文检索与邻接段复查，不从R043/R044候选生成。**类型兼容性声明**：原版example_kind只有firsthand/reported_case/worked_example，都是说明作者真实案例或专门演示；纯虚构小说人物情节不属于这三种，故明确登记`fictional_narrative_case`为原始候选的未核准扩展，不冒充作者亲历或历史事实。Stage1.5须单独裁决其能否用于A1；此前B PROVISIONAL、C NOT_RUN。版权原文仅在私有EPUB，source_quote原版字段留空并附SHA定位。

```yaml
- id: c01
  title: "账房应聘作为学习市场的入口"
  type: case
  example_kind: fictional_narrative_case
  source_reality: FICTIONAL_NOVEL_SCENE_NOT_HISTORICAL_EVIDENCE
  example_kind_extension_status: REQUIRES_STAGE1_5_REVIEW
  source_chapter: "《晚明》n010/p18;n010/p21;n010/p37"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA
  source_loci:
    - "n010/p18"
    - "n010/p21"
    - "n010/p37"
  chunk_ids:
    - "ck-2f9e2e835d0c"
  summary: |-
    场景起因与行动：谋生者观察到店铺招聘，在缺少交易经验的条件下提出先进入现有经营场所学习；他以恭敬和师徒关系争取一名掌柜指导。
    当场结果：掌柜接受了请教和进一步接触的安排；当事人尚须通过另一关面试，因此不能把本场写成最终正式录用。
    可分析的叙事方法：当人物缺乏本地生存资格时，用一场具体应聘展示知识与社会承认之间的距离。
    限制与竞争解释：就业尝试和录用结果必须分开；人物能言善辩也不等于专业能力已获验证。
    此案例不是作者的现实经历，是否可进入A1仍需Stage1.5验证。
  bound_to:
    - "当人物缺乏本地生存资格时，用一场具体应聘展示知识与社会承认之间的距离。"
  outcome: "掌柜接受了请教和进一步接触的安排；当事人尚须通过另一关面试，因此不能把本场写成最终正式录用。"
  outcome_scope: ON_SCENE_ONLY
  counterpressure_or_limit: "就业尝试和录用结果必须分开；人物能言善辩也不等于专业能力已获验证。"
  task_ids: [WM-01,WM-04]
  tags: [fictional-scene, source-anchored, narrative-example]
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
- id: c02
  title: "一笔报酬引出三个合作人的不同底线"
  type: case
  example_kind: fictional_narrative_case
  source_reality: FICTIONAL_NOVEL_SCENE_NOT_HISTORICAL_EVIDENCE
  example_kind_extension_status: REQUIRES_STAGE1_5_REVIEW
  source_chapter: "《晚明》n034/p18;n034/p20;n034/p43"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA
  source_loci:
    - "n034/p18"
    - "n034/p20"
    - "n034/p43"
  chunk_ids:
    - "ck-0fe8a47c63e1"
  summary: |-
    场景起因与行动：一名经营者以钱表达谢意，刘民有明确拒绝其获利方式；同行者则以当时急需银钱为由接受了另一种名义的款项。后来同场提出代售建议，商人又按自身渠道重算利益。
    当场结果：款项由另一人实际接下，刘民有未表示对其伦理立场的改变；卖衣建议被讨论，不能宣称最后方案已获所有人无条件执行。
    可分析的叙事方法：同一事件中分别展示伦理拒绝、现实筹资与渠道商个人目标。
    限制与竞争解释：不要把拿到银钱解释为所有参与者共同认可获利手段。
    此案例不是作者的现实经历，是否可进入A1仍需Stage1.5验证。
  bound_to:
    - "同一事件中分别展示伦理拒绝、现实筹资与渠道商个人目标。"
  outcome: "款项由另一人实际接下，刘民有未表示对其伦理立场的改变；卖衣建议被讨论，不能宣称最后方案已获所有人无条件执行。"
  outcome_scope: ON_SCENE_ONLY
  counterpressure_or_limit: "不要把拿到银钱解释为所有参与者共同认可获利手段。"
  task_ids: [WM-02,WM-04]
  tags: [fictional-scene, source-anchored, narrative-example]
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
- id: c03
  title: "店铺东家离开前安排新掌柜"
  type: case
  example_kind: fictional_narrative_case
  source_reality: FICTIONAL_NOVEL_SCENE_NOT_HISTORICAL_EVIDENCE
  example_kind_extension_status: REQUIRES_STAGE1_5_REVIEW
  source_chapter: "《晚明》n065/p23;n065/p24;n065/p25"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA
  source_loci:
    - "n065/p23"
    - "n065/p24"
    - "n065/p25"
  chunk_ids:
    - "ck-7bc7f1c7317a"
  summary: |-
    场景起因与行动：东家宣布长期离开但店铺继续经营，当众安排原裁缝承担管事职责；被任命者先推辞后接受，另一位老员工则对职位及收入管理提出疑虑。
    当场结果：新掌柜当场接受，原有分工被宣布继续；现金收付及内部的不满没有在此一段自动全部结清。
    可分析的叙事方法：从宣布授权到员工实际接受之间，让不同员工反应形成有后果的场面。
    限制与竞争解释：名义任命不能证明后续店铺一切事务运转无误。
    此案例不是作者的现实经历，是否可进入A1仍需Stage1.5验证。
  bound_to:
    - "从宣布授权到员工实际接受之间，让不同员工反应形成有后果的场面。"
  outcome: "新掌柜当场接受，原有分工被宣布继续；现金收付及内部的不满没有在此一段自动全部结清。"
  outcome_scope: ON_SCENE_ONLY
  counterpressure_or_limit: "名义任命不能证明后续店铺一切事务运转无误。"
  task_ids: [WM-01,WM-03,WM-08]
  tags: [fictional-scene, source-anchored, narrative-example]
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
- id: c04
  title: "一场功劳结算被多种尺度拉扯"
  type: case
  example_kind: fictional_narrative_case
  source_reality: FICTIONAL_NOVEL_SCENE_NOT_HISTORICAL_EVIDENCE
  example_kind_extension_status: REQUIRES_STAGE1_5_REVIEW
  source_chapter: "《晚明》n085/p25;n085/p27;n085/p29"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA
  source_loci:
    - "n085/p25"
    - "n085/p27"
    - "n085/p29"
  chunk_ids:
    - "ck-64574098eea7"
  summary: |-
    场景起因与行动：多个参会者分别依据先前受损资产、投入人数和参与风险提出互相排斥的收益分配标准；拥有裁量权的人逐一听取，争论升级。
    当场结果：场内出现公开的不同计算理由，但本组场景没有形成各方公认的最终公平分配；部分发言者的说法带有明显自身利益。
    可分析的叙事方法：重大集体事件结束后，换到承担不同损失者的争议现场。
    限制与竞争解释：争吵本身不是合理分配原则的证明，也不可直接继承原书金额或身份结构。
    此案例不是作者的现实经历，是否可进入A1仍需Stage1.5验证。
  bound_to:
    - "重大集体事件结束后，换到承担不同损失者的争议现场。"
  outcome: "场内出现公开的不同计算理由，但本组场景没有形成各方公认的最终公平分配；部分发言者的说法带有明显自身利益。"
  outcome_scope: ON_SCENE_ONLY
  counterpressure_or_limit: "争吵本身不是合理分配原则的证明，也不可直接继承原书金额或身份结构。"
  task_ids: [WM-06]
  tags: [fictional-scene, source-anchored, narrative-example]
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
- id: c05
  title: "交易伙伴归来暴露单一资金来源风险"
  type: case
  example_kind: fictional_narrative_case
  source_reality: FICTIONAL_NOVEL_SCENE_NOT_HISTORICAL_EVIDENCE
  example_kind_extension_status: REQUIRES_STAGE1_5_REVIEW
  source_chapter: "《晚明》n099/p18;n099/p19"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA
  source_loci:
    - "n099/p18"
    - "n099/p19"
  chunk_ids:
    - "ck-35cf27b3b35b"
  summary: |-
    场景起因与行动：角色见到合作方的货船状况后担心对方是否平安，意识到自身后续经营和人员供养高度依赖这名外部伙伴。
    当场结果：亲眼见到合作方本人后暂时松了一口气，但运输兑现和长期替代渠道尚未在这里得到证明。
    可分析的叙事方法：把风险落在人物等待、远处船只与其情绪变化上，而非抽象资源讲解。
    限制与竞争解释：当事人的推测不能代替完整的货物验收或后续实际收入。
    此案例不是作者的现实经历，是否可进入A1仍需Stage1.5验证。
  bound_to:
    - "把风险落在人物等待、远处船只与其情绪变化上，而非抽象资源讲解。"
  outcome: "亲眼见到合作方本人后暂时松了一口气，但运输兑现和长期替代渠道尚未在这里得到证明。"
  outcome_scope: ON_SCENE_ONLY
  counterpressure_or_limit: "当事人的推测不能代替完整的货物验收或后续实际收入。"
  task_ids: [WM-04,WM-05]
  tags: [fictional-scene, source-anchored, narrative-example]
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
- id: c06
  title: "公开提议被上级改变并使当事人退让"
  type: case
  example_kind: fictional_narrative_case
  source_reality: FICTIONAL_NOVEL_SCENE_NOT_HISTORICAL_EVIDENCE
  example_kind_extension_status: REQUIRES_STAGE1_5_REVIEW
  source_chapter: "《晚明》n143/p49;n143/p52;n143/p55"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA
  source_loci:
    - "n143/p49"
    - "n143/p52"
    - "n143/p55"
  chunk_ids:
    - "ck-65040e382e4e"
  summary: |-
    场景起因与行动：参与会议的下级提出调整分工，上级已有不同安排并直接宣布；提议者意识到个人预期利益将改变，最终当场接受决定。
    当场结果：本场的决定和退让得到展示，但无法据此证明整项计划在随后的事件中全部落实。
    可分析的叙事方法：让正式权力、人物当场利益和公众面前的服从产生具体差异。
    限制与竞争解释：本组证据替代旧R013误引n143/p29的人员到席段，不得恢复那个错误锚点。
    此案例不是作者的现实经历，是否可进入A1仍需Stage1.5验证。
  bound_to:
    - "让正式权力、人物当场利益和公众面前的服从产生具体差异。"
  outcome: "本场的决定和退让得到展示，但无法据此证明整项计划在随后的事件中全部落实。"
  outcome_scope: ON_SCENE_ONLY
  counterpressure_or_limit: "本组证据替代旧R013误引n143/p29的人员到席段，不得恢复那个错误锚点。"
  task_ids: [WM-03,WM-05]
  tags: [fictional-scene, source-anchored, narrative-example]
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
- id: c07
  title: "官方正当说辞与地方执行者的真实压力"
  type: case
  example_kind: fictional_narrative_case
  source_reality: FICTIONAL_NOVEL_SCENE_NOT_HISTORICAL_EVIDENCE
  example_kind_extension_status: REQUIRES_STAGE1_5_REVIEW
  source_chapter: "《晚明》n265/p21;n265/p22;n265/p29"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA
  source_loci:
    - "n265/p21"
    - "n265/p22"
    - "n265/p29"
  chunk_ids:
    - "ck-956f575fa961"
  summary: |-
    场景起因与行动：权力人物以保护受影响百姓的说辞要求地方官调整财产手续，转而又让旁观者察觉要求并非普通公开补偿。地方官听出隐含利益、权力差和自身风险。
    当场结果：地方官当场承诺办理相关事项，但文件完成、真正权利人有无申辩以及长期结果均未在所选段落证明。
    可分析的叙事方法：用相互冲突的公开语言和另一人的心中理解揭示制度伦理张力。
    限制与竞争解释：这是虚构权力不对称的批判性案例，不提供可执行的行政规避或侵权方法。
    此案例不是作者的现实经历，是否可进入A1仍需Stage1.5验证。
  bound_to:
    - "用相互冲突的公开语言和另一人的心中理解揭示制度伦理张力。"
  outcome: "地方官当场承诺办理相关事项，但文件完成、真正权利人有无申辩以及长期结果均未在所选段落证明。"
  outcome_scope: ON_SCENE_ONLY
  counterpressure_or_limit: "这是虚构权力不对称的批判性案例，不提供可执行的行政规避或侵权方法。"
  task_ids: [WM-06,WM-07]
  tags: [fictional-scene, source-anchored, narrative-example]
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
- id: c08
  title: "账册冲突后形成阶段缩减方案"
  type: case
  example_kind: fictional_narrative_case
  source_reality: FICTIONAL_NOVEL_SCENE_NOT_HISTORICAL_EVIDENCE
  example_kind_extension_status: REQUIRES_STAGE1_5_REVIEW
  source_chapter: "《晚明》n305/p29;n305/p32;n305/p36"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA
  source_loci:
    - "n305/p29"
    - "n305/p32"
    - "n305/p36"
  chunk_ids:
    - "ck-2dee35e976d6"
  summary: |-
    场景起因与行动：一方提出更大规模的部门扩张，另一方拿出现有各部门花销并逐项质疑；双方当场尝试重新计算和缩减。
    当场结果：反对者勉强同意阶段草案，倡议者作出暂时退让；财政未来是否兑现、双方是否继续满意未被证明。
    可分析的叙事方法：把资源争论写成改变决定的现场，而不是两位主角口头宣布“钱已解决”。
    限制与竞争解释：算出的只是角色方案，且作品中的具体金额不能当成历史或现实计算标准。
    此案例不是作者的现实经历，是否可进入A1仍需Stage1.5验证。
  bound_to:
    - "把资源争论写成改变决定的现场，而不是两位主角口头宣布“钱已解决”。"
  outcome: "反对者勉强同意阶段草案，倡议者作出暂时退让；财政未来是否兑现、双方是否继续满意未被证明。"
  outcome_scope: ON_SCENE_ONLY
  counterpressure_or_limit: "算出的只是角色方案，且作品中的具体金额不能当成历史或现实计算标准。"
  task_ids: [WM-03,WM-04]
  tags: [fictional-scene, source-anchored, narrative-example]
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
- id: c09
  title: "返乡者发现家庭荣誉与教育负担并存"
  type: case
  example_kind: fictional_narrative_case
  source_reality: FICTIONAL_NOVEL_SCENE_NOT_HISTORICAL_EVIDENCE
  example_kind_extension_status: REQUIRES_STAGE1_5_REVIEW
  source_chapter: "《晚明》n339/p9;n339/p10;n339/p31;n339/p34"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA
  source_loci:
    - "n339/p9"
    - "n339/p10"
    - "n339/p31"
    - "n339/p34"
  chunk_ids:
    - "ck-312a7425ee02"
  summary: |-
    场景起因与行动：返乡者发现母亲替妹妹决定婚事，自己对此提出疑虑；后来又听到一个孩子因家庭失去劳力、无法继续读书的困难。
    当场结果：他作出有限资助，孩子当场高兴，但家中长远收入和妹妹的意愿没有因此得到完整解决。
    可分析的叙事方法：从集体荣誉转场到家庭的非自愿责任和下一代个人目标。
    限制与竞争解释：一次捐赠不是教育制度或贫困的结构性解决，家长说话不等于当事人认同。
    此案例不是作者的现实经历，是否可进入A1仍需Stage1.5验证。
  bound_to:
    - "从集体荣誉转场到家庭的非自愿责任和下一代个人目标。"
  outcome: "他作出有限资助，孩子当场高兴，但家中长远收入和妹妹的意愿没有因此得到完整解决。"
  outcome_scope: ON_SCENE_ONLY
  counterpressure_or_limit: "一次捐赠不是教育制度或贫困的结构性解决，家长说话不等于当事人认同。"
  task_ids: [WM-06,WM-08]
  tags: [fictional-scene, source-anchored, narrative-example]
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
- id: c10
  title: "基层投诉揭出部门分权的未决事项"
  type: case
  example_kind: fictional_narrative_case
  source_reality: FICTIONAL_NOVEL_SCENE_NOT_HISTORICAL_EVIDENCE
  example_kind_extension_status: REQUIRES_STAGE1_5_REVIEW
  source_chapter: "《晚明》n425/p25;n425/p27;n425/p35;n425/p40"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA
  source_loci:
    - "n425/p25"
    - "n425/p27"
    - "n425/p35"
    - "n425/p40"
  chunk_ids:
    - "ck-507de61e85d6"
  summary: |-
    场景起因与行动：一位治理负责人报告基层干部涉嫌不当处置资源，主张收回某些裁量事项；随后地方管理者与职能部门人员为新的职责界限争执。
    当场结果：已经有人被处理且另有调查；新的权责边界在会议结束前尚未共同谈妥，只布置了继续拟订方案。
    可分析的叙事方法：由具体投诉进入制度调整，再展示各方对职位和资源的实际顾虑。
    限制与竞争解释：人物提出改善并不证明试点已实施，更不能推导出现实行政组织最优形式。
    此案例不是作者的现实经历，是否可进入A1仍需Stage1.5验证。
  bound_to:
    - "由具体投诉进入制度调整，再展示各方对职位和资源的实际顾虑。"
  outcome: "已经有人被处理且另有调查；新的权责边界在会议结束前尚未共同谈妥，只布置了继续拟订方案。"
  outcome_scope: ON_SCENE_ONLY
  counterpressure_or_limit: "人物提出改善并不证明试点已实施，更不能推导出现实行政组织最优形式。"
  task_ids: [WM-03,WM-07]
  tags: [fictional-scene, source-anchored, narrative-example]
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
- id: c11
  title: "一个新设想被否定之后又有采购争论"
  type: case
  example_kind: fictional_narrative_case
  source_reality: FICTIONAL_NOVEL_SCENE_NOT_HISTORICAL_EVIDENCE
  example_kind_extension_status: REQUIRES_STAGE1_5_REVIEW
  source_chapter: "《晚明》n437/p6;n437/p29;n437/p31"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA
  source_loci:
    - "n437/p6"
    - "n437/p29"
    - "n437/p31"
  chunk_ids:
    - "ck-dff261ebc036"
  summary: |-
    场景起因与行动：工坊曾提出一项新制品设想，但评议认为不适合而否决；后续其他产品的交付争执又促使上级宣布调整签约责任。
    当场结果：前一个新设想没有进入正式新任务；新合同安排被当场宣布，但不能据此声称竞争制度已经产生实际成效。
    可分析的叙事方法：把创新失败、用户抱怨与权责调整作为相邻但不可混同的剧情结果。
    限制与竞争解释：只抽取文学叙事中的审核与失败分支，不提取现实危险设备、生产或采购技术。
    此案例不是作者的现实经历，是否可进入A1仍需Stage1.5验证。
  bound_to:
    - "把创新失败、用户抱怨与权责调整作为相邻但不可混同的剧情结果。"
  outcome: "前一个新设想没有进入正式新任务；新合同安排被当场宣布，但不能据此声称竞争制度已经产生实际成效。"
  outcome_scope: ON_SCENE_ONLY
  counterpressure_or_limit: "只抽取文学叙事中的审核与失败分支，不提取现实危险设备、生产或采购技术。"
  task_ids: [WM-03,WM-04]
  tags: [fictional-scene, source-anchored, narrative-example]
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
- id: c12
  title: "陪审者给出的理由改变两位主角预期"
  type: case
  example_kind: fictional_narrative_case
  source_reality: FICTIONAL_NOVEL_SCENE_NOT_HISTORICAL_EVIDENCE
  example_kind_extension_status: REQUIRES_STAGE1_5_REVIEW
  source_chapter: "《晚明》n519/p67;n519/p69;n519/p70;n520/p17"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA
  source_loci:
    - "n519/p67"
    - "n519/p69"
    - "n519/p70"
    - "n520/p17"
  chunk_ids:
    - "ck-a7e713d93ef2"
    - "ck-9cf793319d6f"
    - "ck-d005282755fd"
  summary: |-
    场景起因与行动：在一场试办的听审中，原本握有裁判经验的人预期某种结论，普通成员却给出不同判断；主持者要求说明理由，发言者以自己的生活经验解释。
    当场结果：参与者当场听到出乎预料的结论，后续讨论承认价值观差异并仅同意有限继续试办。没有证明该判定合法或制度可以全面推广。
    可分析的叙事方法：将事先自信、独立表达和附条件复盘组成一次完整的价值冲突案例。
    限制与竞争解释：所涉法律责任与被影响人权益须独立核查，绝不把小说虚构庭审当现实法律范例。
    此案例不是作者的现实经历，是否可进入A1仍需Stage1.5验证。
  bound_to:
    - "将事先自信、独立表达和附条件复盘组成一次完整的价值冲突案例。"
  outcome: "参与者当场听到出乎预料的结论，后续讨论承认价值观差异并仅同意有限继续试办。没有证明该判定合法或制度可以全面推广。"
  outcome_scope: CROSS_CHAPTER_LIMITED
  counterpressure_or_limit: "所涉法律责任与被影响人权益须独立核查，绝不把小说虚构庭审当现实法律范例。"
  task_ids: [WM-02,WM-07]
  tags: [fictional-scene, source-anchored, narrative-example]
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
- id: c13
  title: "人物拒绝被荣誉交换的婚事而保留私人选择"
  type: case
  example_kind: fictional_narrative_case
  source_reality: FICTIONAL_NOVEL_SCENE_NOT_HISTORICAL_EVIDENCE
  example_kind_extension_status: REQUIRES_STAGE1_5_REVIEW
  source_chapter: "《晚明》n540/p32;n540/p33;n569/p20;n569/p21"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA
  source_loci:
    - "n540/p32"
    - "n540/p33"
    - "n569/p20"
    - "n569/p21"
  chunk_ids:
    - "ck-4e72eec2ce6f"
    - "ck-3c984ed5a591"
  summary: |-
    场景起因与行动：一名人物面对将职业成就当作婚事筹码的求婚者时，当场说清不同意，另一人随后带着长期愿望与实际经历继续生活。
    当场结果：故事后段再次出现两人接触并作出新的情感表达；这不等于前一场拒绝从来没有发生，也不使危险争取荣誉成为合理选择。
    可分析的叙事方法：用跨章个人愿望与两次不同态度表现关系变化，而不让集体功绩直接决定私人生活。
    限制与竞争解释：不能将求取荣誉当作获得他人同意的方式；不复刻小说的专属人物及场面。
    此案例不是作者的现实经历，是否可进入A1仍需Stage1.5验证。
  bound_to:
    - "用跨章个人愿望与两次不同态度表现关系变化，而不让集体功绩直接决定私人生活。"
  outcome: "故事后段再次出现两人接触并作出新的情感表达；这不等于前一场拒绝从来没有发生，也不使危险争取荣誉成为合理选择。"
  outcome_scope: CROSS_CHAPTER_LIMITED
  counterpressure_or_limit: "不能将求取荣誉当作获得他人同意的方式；不复刻小说的专属人物及场面。"
  task_ids: [WM-06,WM-08]
  tags: [fictional-scene, source-anchored, narrative-example]
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
- id: c14
  title: "多年后的故事讲述受到听众逐项挑战"
  type: case
  example_kind: fictional_narrative_case
  source_reality: FICTIONAL_NOVEL_SCENE_NOT_HISTORICAL_EVIDENCE
  example_kind_extension_status: REQUIRES_STAGE1_5_REVIEW
  source_chapter: "《晚明》n571/p3;n571/p5;n571/p25"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA
  source_loci:
    - "n571/p3"
    - "n571/p5"
    - "n571/p25"
  chunk_ids:
    - "ck-e9d40a8c080f"
  summary: |-
    场景起因与行动：多年后，一名与事件相关的讲述者为听众演绎旧事，席间不同人对讲述是否准确、应突出什么人物及如何安排情节提出互相冲突的意见。
    当场结果：说书继续成为公开讨论对象，人物对于旧事的想象互不一致；没有统一证据证明每个传说细节都真实，也未宣布前面已叙写的场景全部无效。
    可分析的叙事方法：以再叙述和现场听众的分歧收束长期历史故事的记忆层次。
    限制与竞争解释：不能复制原书特定尾声结构或依靠听众偏好否认原先被文本确实展示的事件。
    此案例不是作者的现实经历，是否可进入A1仍需Stage1.5验证。
  bound_to:
    - "以再叙述和现场听众的分歧收束长期历史故事的记忆层次。"
  outcome: "说书继续成为公开讨论对象，人物对于旧事的想象互不一致；没有统一证据证明每个传说细节都真实，也未宣布前面已叙写的场景全部无效。"
  outcome_scope: ON_SCENE_ONLY
  counterpressure_or_limit: "不能复制原书特定尾声结构或依靠听众偏好否认原先被文本确实展示的事件。"
  task_ids: [WM-09]
  tags: [fictional-scene, source-anchored, narrative-example]
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
```

## 类型边界与覆盖缺口

- 原版`firsthand`是作者亲历真实案例；`reported_case`是作者转述真实他人案例；`worked_example`是作者提供的练习或演算。本书为长篇虚构小说，故**全部14项明确是`fictional_narrative_case`，并标为非原版枚举的待审核扩展**，不虚报任何小说事件为真实历史。
- 这些案例只为小说场面和写作机制分析提供源内事实，**不是作者在教读者某套管理法的真实案例**。缺乏明示方法论意图时，`bound_to`是研究者说明其可能帮助的叙事问题，需在Stage1.5 V1/V2/V3核验能否真正服务原创工作；目前没有晋级权。
- 阶段0九项原书关键任务WM-01—WM-09均获至少一例关联；按OPF有效章六段S1—S6都有具体见证位置。但这仅是Raw coverage，不能宣称九项任务已通过独立创作试验。
- 本轮只使用已批准的BOOK_OVERVIEW与原始私有EPUB及独立建立的chunk检索。R043的框架候选、R044的原则候选均非本次案例判断的事实输入；重复原文不能算两个代理独立证据。
- 旧R013误引用的n143/p29不得作为上级定案证据；R042 14条问题旧claim仍`NO_DIRECT_PROMOTION_RECONSTRUCT_FROM_SOURCE`，其余旧文学结论也不自动升级。材料A来源可追溯，B PROVISIONAL，C NOT_RUN，Skill认证0。
