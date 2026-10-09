# V13 R050｜《铁血残明》Stage1案例提取器独立原始候选

仅使用用户提供的原始EPUB、R042已经批准的BOOK_OVERVIEW与TX-01—TX-10独立任务。案例是小说虚构情境，原版case-extractor的firsthand / reported_case / worked_example三个身份均不适用；此处在RAW层临时扩展 `fictional_narrative_case`，并标记REQUIRES_STAGE1_5_REVIEW，不假称完全符合原版正式案例枚举。每例都有实际源场景、发生的事与尚未发生的事、bound_to叙事主题、可见outcome及适用限制。

版权小说正文不放进公开GitHub；依原版字段保留source_quote但空置，并用本地原书n/p与不可逆SHA源凭证绑定。公开CI仅SOURCE_STRUCTURE_ONLY；文学B=PROVISIONAL、原创C=NOT_RUN、认证SKILL0。未从R048或R049候选重排复制案例，叙述与情境均经本轮原书邻接复核，允许Stage1.5后来否决候选。

```yaml
- id: c01
  title: "旧身份在街坊围观中先于新主人形成判断"
  type: case
  example_kind: fictional_narrative_case
  source_reality: FICTIONAL_NOVEL_SCENE_NOT_HISTORICAL_EVIDENCE
  example_kind_extension_status: REQUIRES_STAGE1_5_REVIEW
  source_chapter: "《铁血残明》有效叙事n001；n001/p16；n001/p20；n001/p30"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA
  source_loci:
    - "n001/p16"
    - "n001/p20"
    - "n001/p30"
  chunk_ids:
    - "ck-d95eca2bfb27"
  summary: |-
    场景起因：街头突发争执引来众人，围观者先以旧日恶评识别庞家少年。
    角色行动：一名旁观者原本试图表达感谢，其他围观者的反应却沿着旧声誉展开；随后的差役身份被单独说出。
    在所引场景可核的结果：同一现场出现相互冲突的态度，围观者对人的既有判断没有因眼前一件行为自动消失；本场不能证明后续信任已经重建。
    可研究的叙事作用：以相互冲突的当场见证替代叙述者宣布人物身份洗白。
    限制与竞争解释：围观意见不是所有居民的意见；场面含危险冲突，文学提取不转成伤害情节操作。
    来源性质：本例是虚构小说内部场景，不是作者亲历、真实历史事件或演算例题。
    待Stage1.5核对多章节后果与新写作任务增益；不据此创作仿写原著人物及专属情节。
  bound_to:
    - "以相互冲突的当场见证替代叙述者宣布人物身份洗白"
  outcome: "同一现场出现相互冲突的态度，围观者对人的既有判断没有因眼前一件行为自动消失；本场不能证明后续信任已经重建。"
  outcome_scope: ORIGINAL_SCENE_ONLY_NO_UNSEEN_FUTURE
  counterpressure_or_limit: "围观意见不是所有居民的意见；场面含危险冲突，文学提取不转成伤害情节操作。"
  task_ids: [TX-01]
  tags: [fictional-scene, source-anchored, pov, social-memory]
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
- id: c02
  title: "谷小武提出主角没有考虑的另一条道路"
  type: case
  example_kind: fictional_narrative_case
  source_reality: FICTIONAL_NOVEL_SCENE_NOT_HISTORICAL_EVIDENCE
  example_kind_extension_status: REQUIRES_STAGE1_5_REVIEW
  source_chapter: "《铁血残明》有效叙事n051；n051/p26；n051/p29；n051/p30；n051/p40"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA
  source_loci:
    - "n051/p26"
    - "n051/p29"
    - "n051/p30"
    - "n051/p40"
  chunk_ids:
    - "ck-d1eace8d3bba"
  summary: |-
    场景起因：危急局势中庞雨试图劝谷小武远走，前者自以为看清了未来选择。
    角色行动：谷小武把当地盟友和自己过去的忠诚重新提出，追问主角为何从未选择通知对方；主角不得不改变话术。
    在所引场景可核的结果：人物分歧被明确说出，庞雨意识到自己此前排除了对方选择；并未由这段证明谷小武最终接受任何一种方案。
    可研究的叙事作用：给次要人物独立记忆和价值排序来揭露主角认知盲区。
    限制与竞争解释：在强压力与高风险环境中提出方案不表示可自由实现；不抽取原著危险行为细节。
    来源性质：本例是虚构小说内部场景，不是作者亲历、真实历史事件或演算例题。
    待Stage1.5核对多章节后果与新写作任务增益；不据此创作仿写原著人物及专属情节。
  bound_to:
    - "给次要人物独立记忆和价值排序来揭露主角认知盲区"
  outcome: "人物分歧被明确说出，庞雨意识到自己此前排除了对方选择；并未由这段证明谷小武最终接受任何一种方案。"
  outcome_scope: ORIGINAL_SCENE_ONLY_NO_UNSEEN_FUTURE
  counterpressure_or_limit: "在强压力与高风险环境中提出方案不表示可自由实现；不抽取原著危险行为细节。"
  task_ids: [TX-03, TX-06]
  tags: [fictional-scene, source-anchored, information-gap, agency]
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
- id: c03
  title: "抢报功名被幕友的权力现实当场反驳"
  type: case
  example_kind: fictional_narrative_case
  source_reality: FICTIONAL_NOVEL_SCENE_NOT_HISTORICAL_EVIDENCE
  example_kind_extension_status: REQUIRES_STAGE1_5_REVIEW
  source_chapter: "《铁血残明》有效叙事n055；n055/p30；n055/p31；n055/p32"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA
  source_loci:
    - "n055/p30"
    - "n055/p31"
    - "n055/p32"
  chunk_ids:
    - "ck-50a0a3ab62de"
  summary: |-
    场景起因：庞雨担心同一事件的功劳归属被其他机构抢先取得。
    角色行动：他要求先递申详，余先生认可可修改上报，却说明后续认可依赖其他官员的裁量。
    在所引场景可核的结果：呈送文件的安排得到口头接受，但“先到便有首功”的预期被同场质疑；本场没有正式获批结果。
    可研究的叙事作用：用一场文书办理把申请、修改、上送和认定之间的距离演成角色对白。
    限制与竞争解释：小说里对官场制度的解释不构成独立史实证明。
    来源性质：本例是虚构小说内部场景，不是作者亲历、真实历史事件或演算例题。
    待Stage1.5核对多章节后果与新写作任务增益；不据此创作仿写原著人物及专属情节。
  bound_to:
    - "用一场文书办理把申请、修改、上送和认定之间的距离演成角色对白"
  outcome: "呈送文件的安排得到口头接受，但“先到便有首功”的预期被同场质疑；本场没有正式获批结果。"
  outcome_scope: ORIGINAL_SCENE_ONLY_NO_UNSEEN_FUTURE
  counterpressure_or_limit: "小说里对官场制度的解释不构成独立史实证明。"
  task_ids: [TX-02, TX-09]
  tags: [fictional-scene, source-anchored, document-version, authority]
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
- id: c04
  title: "赞助者追问训练理由后主角私下承认知识空缺"
  type: case
  example_kind: fictional_narrative_case
  source_reality: FICTIONAL_NOVEL_SCENE_NOT_HISTORICAL_EVIDENCE
  example_kind_extension_status: REQUIRES_STAGE1_5_REVIEW
  source_chapter: "《铁血残明》有效叙事n081；n081/p51；n081/p55；n081/p59"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA
  source_loci:
    - "n081/p51"
    - "n081/p55"
    - "n081/p59"
  chunk_ids:
    - "ck-4d597315b974"
    - "ck-6c5d8955ecb8"
  summary: |-
    场景起因：一位支持者连续观看演练，却看不出后续安排的逻辑。
    角色行动：庞雨公开解释当前做法并暗示之后有安排，赞助者仍提出进一步问题。
    在所引场景可核的结果：说服性发言没有改变主角尚未决定后续内容的事实；以独白暴露公开权威与私下能力之间的缺口。
    可研究的叙事作用：让人物在别人面前给出的答案与自身真正确定的事项形成可读反差。
    限制与竞争解释：谈话发生并不能证明后续组织长期运转失败；军事技术细节不移植。
    来源性质：本例是虚构小说内部场景，不是作者亲历、真实历史事件或演算例题。
    待Stage1.5核对多章节后果与新写作任务增益；不据此创作仿写原著人物及专属情节。
  bound_to:
    - "让人物在别人面前给出的答案与自身真正确定的事项形成可读反差"
  outcome: "说服性发言没有改变主角尚未决定后续内容的事实；以独白暴露公开权威与私下能力之间的缺口。"
  outcome_scope: ORIGINAL_SCENE_ONLY_NO_UNSEEN_FUTURE
  counterpressure_or_limit: "谈话发生并不能证明后续组织长期运转失败；军事技术细节不移植。"
  task_ids: [TX-03, TX-05]
  tags: [fictional-scene, source-anchored, dialogue-subtext, knowledge-limit]
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
- id: c05
  title: "幕友给出处理申诉的方案，知县接受但后果未示"
  type: case
  example_kind: fictional_narrative_case
  source_reality: FICTIONAL_NOVEL_SCENE_NOT_HISTORICAL_EVIDENCE
  example_kind_extension_status: REQUIRES_STAGE1_5_REVIEW
  source_chapter: "《铁血残明》有效叙事n095；n095/p28；n095/p35；n095/p36"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA
  source_loci:
    - "n095/p28"
    - "n095/p35"
    - "n095/p36"
  chunk_ids:
    - "ck-50e4aeae3448"
  summary: |-
    场景起因：知县偏爱一名得力部属，同时存在尚未处理的申诉和同僚提醒。
    角色行动：幕友提出如何利用拖延维持上下级关系的意见，知县犹疑后口头同意。
    在所引场景可核的结果：幕友对知县决策产生现场影响；这一小段止于同意建议，不证明申诉以后如何了结或建议正当。
    可研究的叙事作用：把权力方案落实为犹豫、说服和临时选择，而不是单方面的官场全知旁白。
    限制与竞争解释：角色建议涉及不公正权力使用，只可用作伦理复杂性的叙事观察，绝非可执行管理建议。
    来源性质：本例是虚构小说内部场景，不是作者亲历、真实历史事件或演算例题。
    待Stage1.5核对多章节后果与新写作任务增益；不据此创作仿写原著人物及专属情节。
  bound_to:
    - "把权力方案落实为犹豫、说服和临时选择，而不是单方面的官场全知旁白"
  outcome: "幕友对知县决策产生现场影响；这一小段止于同意建议，不证明申诉以后如何了结或建议正当。"
  outcome_scope: ORIGINAL_SCENE_ONLY_NO_UNSEEN_FUTURE
  counterpressure_or_limit: "角色建议涉及不公正权力使用，只可用作伦理复杂性的叙事观察，绝非可执行管理建议。"
  task_ids: [TX-02, TX-05]
  tags: [fictional-scene, source-anchored, agency, moral-friction]
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
- id: c06
  title: "预备仓无粮但现场仍有临时供给"
  type: case
  example_kind: fictional_narrative_case
  source_reality: FICTIONAL_NOVEL_SCENE_NOT_HISTORICAL_EVIDENCE
  example_kind_extension_status: REQUIRES_STAGE1_5_REVIEW
  source_chapter: "《铁血残明》有效叙事n114；n114/p27；n114/p29；n114/p31"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA
  source_loci:
    - "n114/p27"
    - "n114/p29"
    - "n114/p31"
  chunk_ids:
    - "ck-4f52a5896754"
  summary: |-
    场景起因：知县发现原有粮库与先前准备要求不符，因危机而提高追责强度。
    角色行动：庞雨评估商铺与民间捐助的现存物资，并试图向知县解释可短暂应付。
    在所引场景可核的结果：本章同时出现官库存粮缺口与民间暂时补救，绝没有显示官库长期修复或责任已经被清理。
    可研究的叙事作用：同一事件并列资源制度故障和短期替代路径，避免单一成功失败判断。
    限制与竞争解释：人物乐观估计不等于库存真实长期足够，不能拿小说内粮数当历史数据。
    来源性质：本例是虚构小说内部场景，不是作者亲历、真实历史事件或演算例题。
    待Stage1.5核对多章节后果与新写作任务增益；不据此创作仿写原著人物及专属情节。
  bound_to:
    - "同一事件并列资源制度故障和短期替代路径，避免单一成功失败判断"
  outcome: "本章同时出现官库存粮缺口与民间暂时补救，绝没有显示官库长期修复或责任已经被清理。"
  outcome_scope: ORIGINAL_SCENE_ONLY_NO_UNSEEN_FUTURE
  counterpressure_or_limit: "人物乐观估计不等于库存真实长期足够，不能拿小说内粮数当历史数据。"
  task_ids: [TX-04]
  tags: [fictional-scene, source-anchored, resource-constraint, counter-evidence]
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
- id: c07
  title: "守城结束后退役请求把荣誉转为现银压力"
  type: case
  example_kind: fictional_narrative_case
  source_reality: FICTIONAL_NOVEL_SCENE_NOT_HISTORICAL_EVIDENCE
  example_kind_extension_status: REQUIRES_STAGE1_5_REVIEW
  source_chapter: "《铁血残明》有效叙事n131；n131/p40；n131/p41；n131/p42；n131/p43"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA
  source_loci:
    - "n131/p40"
    - "n131/p41"
    - "n131/p42"
    - "n131/p43"
  chunk_ids:
    - "ck-ef85215aea3b"
  summary: |-
    场景起因：战事刚缓解，几十名壮班成员希望离开，家属要求兑现先前所承诺的待遇。
    角色行动：庞雨同意结算当月薪银并要求安排家属，但属下立即指出衙门缺钱，主角另提出临时筹付。
    在所引场景可核的结果：结算和救助的指令已下，银款在此段还未被证明全额交付；后续财政来源和谁应负责仍悬而未决。
    可研究的叙事作用：重大事件之后以具体离开者与家属的请求触发下一期资源债务。
    限制与竞争解释：口头允诺不得当已到账；对损失者的描述不转化为现实危险征募实践。
    来源性质：本例是虚构小说内部场景，不是作者亲历、真实历史事件或演算例题。
    待Stage1.5核对多章节后果与新写作任务增益；不据此创作仿写原著人物及专属情节。
  bound_to:
    - "重大事件之后以具体离开者与家属的请求触发下一期资源债务"
  outcome: "结算和救助的指令已下，银款在此段还未被证明全额交付；后续财政来源和谁应负责仍悬而未决。"
  outcome_scope: ORIGINAL_SCENE_ONLY_NO_UNSEEN_FUTURE
  counterpressure_or_limit: "口头允诺不得当已到账；对损失者的描述不转化为现实危险征募实践。"
  task_ids: [TX-04, TX-08]
  tags: [fictional-scene, source-anchored, aftermath, payment-gap]
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
- id: c08
  title: "江帆递交规程并提出安排，庞雨当面要求修改"
  type: case
  example_kind: fictional_narrative_case
  source_reality: FICTIONAL_NOVEL_SCENE_NOT_HISTORICAL_EVIDENCE
  example_kind_extension_status: REQUIRES_STAGE1_5_REVIEW
  source_chapter: "《铁血残明》有效叙事n174；n174/p22；n174/p24；n174/p25"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA
  source_loci:
    - "n174/p22"
    - "n174/p24"
    - "n174/p25"
  chunk_ids:
    - "ck-ed04a60bce49"
  summary: |-
    场景起因：组织扩张后需要把口头指挥变成可供查阅的书面规程。
    角色行动：江帆交来经书办拟写的呈文，随后补充自己的方案，庞雨指出方案可能被基层成员理解为额外负担。
    在所引场景可核的结果：下属提出了真实而具体的新意见，上级要求修改，但修改结果、基层成员反应尚无本场实证。
    可研究的叙事作用：把下属专业主动性和上级否决放在同一份可修改文书上。
    限制与竞争解释：原文包含具体基层控制方案，此处只研究自主提案及反馈，不提供现实组织操控规则。
    来源性质：本例是虚构小说内部场景，不是作者亲历、真实历史事件或演算例题。
    待Stage1.5核对多章节后果与新写作任务增益；不据此创作仿写原著人物及专属情节。
  bound_to:
    - "把下属专业主动性和上级否决放在同一份可修改文书上"
  outcome: "下属提出了真实而具体的新意见，上级要求修改，但修改结果、基层成员反应尚无本场实证。"
  outcome_scope: ORIGINAL_SCENE_ONLY_NO_UNSEEN_FUTURE
  counterpressure_or_limit: "原文包含具体基层控制方案，此处只研究自主提案及反馈，不提供现实组织操控规则。"
  task_ids: [TX-03]
  tags: [fictional-scene, source-anchored, subordinate-agency, revision]
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
- id: c09
  title: "高官褒奖尚未说完，私人控诉打断其正面定论"
  type: case
  example_kind: fictional_narrative_case
  source_reality: FICTIONAL_NOVEL_SCENE_NOT_HISTORICAL_EVIDENCE
  example_kind_extension_status: REQUIRES_STAGE1_5_REVIEW
  source_chapter: "《铁血残明》有效叙事n201；n201/p52；n201/p54；n201/p56"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA
  source_loci:
    - "n201/p52"
    - "n201/p54"
    - "n201/p56"
  chunk_ids:
    - "ck-286a055b5fab"
  summary: |-
    场景起因：一场组织协商使史可法对庞雨给予正面评价。
    角色行动：史可法公开肯定他的德行，庞雨试图答话，另一名人物当场提出相反的私人指控。
    在所引场景可核的结果：权威赞许与外来控诉在连续场景中发生碰撞；控诉尚非司法裁决，也没有证明高官此前全部错误。
    可研究的叙事作用：用不可预告的另一个人的发言制造人物信誉的双重证据层。
    限制与竞争解释：私人指控的真假和对方自主意愿必须留到后续检验。
    来源性质：本例是虚构小说内部场景，不是作者亲历、真实历史事件或演算例题。
    待Stage1.5核对多章节后果与新写作任务增益；不据此创作仿写原著人物及专属情节。
  bound_to:
    - "用不可预告的另一个人的发言制造人物信誉的双重证据层"
  outcome: "权威赞许与外来控诉在连续场景中发生碰撞；控诉尚非司法裁决，也没有证明高官此前全部错误。"
  outcome_scope: ORIGINAL_SCENE_ONLY_NO_UNSEEN_FUTURE
  counterpressure_or_limit: "私人指控的真假和对方自主意愿必须留到后续检验。"
  task_ids: [TX-01, TX-08]
  tags: [fictional-scene, source-anchored, countervoice, scene-cut]
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
- id: c10
  title: "小娃子的去向选择打破对手阵营的单一视角"
  type: case
  example_kind: fictional_narrative_case
  source_reality: FICTIONAL_NOVEL_SCENE_NOT_HISTORICAL_EVIDENCE
  example_kind_extension_status: REQUIRES_STAGE1_5_REVIEW
  source_chapter: "《铁血残明》有效叙事n305；n305/p29；n305/p34；n305/p37；n305/p50"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA
  source_loci:
    - "n305/p29"
    - "n305/p34"
    - "n305/p37"
    - "n305/p50"
  chunk_ids:
    - "ck-e9175b2ca227"
  summary: |-
    场景起因：流动的底层人物谈论过去与将来，彼此对怎样活下去的判断不同。
    角色行动：小娃子质疑循环破坏后还能否生存，并提出自己想去的地方；另一人不能完全解释他的选择。
    在所引场景可核的结果：对手阵营人物出现可区分的记忆、顾虑与目的，但并未真的离开或改变全部行为，结尾仍是去处未知。
    可研究的叙事作用：脱离主角镜头的对话让所谓敌方群体有内部不一致与独立未来。
    限制与竞争解释：人物个人愿望不是安全、合理或获得伦理认可的行为；不重述残酷情节。
    来源性质：本例是虚构小说内部场景，不是作者亲历、真实历史事件或演算例题。
    待Stage1.5核对多章节后果与新写作任务增益；不据此创作仿写原著人物及专属情节。
  bound_to:
    - "脱离主角镜头的对话让所谓敌方群体有内部不一致与独立未来"
  outcome: "对手阵营人物出现可区分的记忆、顾虑与目的，但并未真的离开或改变全部行为，结尾仍是去处未知。"
  outcome_scope: ORIGINAL_SCENE_ONLY_NO_UNSEEN_FUTURE
  counterpressure_or_limit: "人物个人愿望不是安全、合理或获得伦理认可的行为；不重述残酷情节。"
  task_ids: [TX-07]
  tags: [fictional-scene, source-anchored, other-side-pov, future-uncertainty]
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
- id: c11
  title: "战功晋升方案被属官追问指挥界限"
  type: case
  example_kind: fictional_narrative_case
  source_reality: FICTIONAL_NOVEL_SCENE_NOT_HISTORICAL_EVIDENCE
  example_kind_extension_status: REQUIRES_STAGE1_5_REVIEW
  source_chapter: "《铁血残明》有效叙事n361；n361/p30；n361/p34；n361/p35；n361/p36"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA
  source_loci:
    - "n361/p30"
    - "n361/p34"
    - "n361/p35"
    - "n361/p36"
  chunk_ids:
    - "ck-68ca5ccbce7e"
  summary: |-
    场景起因：奖功讨论发现善于完成某项危险任务者未必适合指挥别人。
    角色行动：庞雨提出一项非指挥性的荣誉身份，蒋国用马上指出它与现有军官上下级关系可能冲突。
    在所引场景可核的结果：主角即时说明荣誉待遇和正式命令权限的区别；本章没有验证该制度日后是否顺利落实。
    可研究的叙事作用：用专业属员反问给看似圆满的新规制造真实实施检验口。
    限制与竞争解释：小说内的军衔、奖赏仅用于理解文学冲突，不转成可执行军制。
    来源性质：本例是虚构小说内部场景，不是作者亲历、真实历史事件或演算例题。
    待Stage1.5核对多章节后果与新写作任务增益；不据此创作仿写原著人物及专属情节。
  bound_to:
    - "用专业属员反问给看似圆满的新规制造真实实施检验口"
  outcome: "主角即时说明荣誉待遇和正式命令权限的区别；本章没有验证该制度日后是否顺利落实。"
  outcome_scope: ORIGINAL_SCENE_ONLY_NO_UNSEEN_FUTURE
  counterpressure_or_limit: "小说内的军衔、奖赏仅用于理解文学冲突，不转成可执行军制。"
  task_ids: [TX-05]
  tags: [fictional-scene, source-anchored, rule-objection, open-result]
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
- id: c12
  title: "总督追问号令来源，却只得到部分澄清"
  type: case
  example_kind: fictional_narrative_case
  source_reality: FICTIONAL_NOVEL_SCENE_NOT_HISTORICAL_EVIDENCE
  example_kind_extension_status: REQUIRES_STAGE1_5_REVIEW
  source_chapter: "《铁血残明》有效叙事n420；n420/p2；n420/p9；n420/p11"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA
  source_loci:
    - "n420/p2"
    - "n420/p9"
    - "n420/p11"
  chunk_ids:
    - "ck-43af8800326c"
  summary: |-
    场景起因：跨机构协调陷入多头发令的争执。
    角色行动：卢象升坚持询问真正的授权者，杨嗣昌对部分兵力的归属作出回答，却承认其他方面仍未有确切指示。
    在所引场景可核的结果：会面使分歧获得明确表述，却没有在这些对白中产生可覆盖所有部门的统一许可。
    可研究的叙事作用：让权力范围和消息延迟通过面对面的有限答复而非旁白显现。
    限制与竞争解释：角色争论不证明真实历史情况，不能复刻原军事部署。
    来源性质：本例是虚构小说内部场景，不是作者亲历、真实历史事件或演算例题。
    待Stage1.5核对多章节后果与新写作任务增益；不据此创作仿写原著人物及专属情节。
  bound_to:
    - "让权力范围和消息延迟通过面对面的有限答复而非旁白显现"
  outcome: "会面使分歧获得明确表述，却没有在这些对白中产生可覆盖所有部门的统一许可。"
  outcome_scope: ORIGINAL_SCENE_ONLY_NO_UNSEEN_FUTURE
  counterpressure_or_limit: "角色争论不证明真实历史情况，不能复刻原军事部署。"
  task_ids: [TX-06]
  tags: [fictional-scene, source-anchored, multiple-authorities, partial-answer]
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
- id: c13
  title: "曹变蛟拒绝空泛协作，之后作出有限同意"
  type: case
  example_kind: fictional_narrative_case
  source_reality: FICTIONAL_NOVEL_SCENE_NOT_HISTORICAL_EVIDENCE
  example_kind_extension_status: REQUIRES_STAGE1_5_REVIEW
  source_chapter: "《铁血残明》有效叙事n485；n485/p7；n485/p8；n485/p23"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA
  source_loci:
    - "n485/p7"
    - "n485/p8"
    - "n485/p23"
  chunk_ids:
    - "ck-f8106dc67ad3"
  summary: |-
    场景起因：庞雨需要一个拥有独立部属的协作方参与计划，而对方起初利益不一致。
    角色行动：曹变蛟直接追问其承诺如何兑现，庞雨重新谈条件，之后庞雨从对话判断对方已有所同意。
    在所引场景可核的结果：获得的是具体条件下、仍待更多人响应的局部合作，绝非整个联盟已经完全成立。
    可研究的叙事作用：以拒绝、要求证据和有限条件转变写出有权否决的次要角色。
    限制与竞争解释：本书军事筹划和对价数字均不作为现实谈判或战术教程；庞雨的理解不等同协议最终实现。
    来源性质：本例是虚构小说内部场景，不是作者亲历、真实历史事件或演算例题。
    待Stage1.5核对多章节后果与新写作任务增益；不据此创作仿写原著人物及专属情节。
  bound_to:
    - "以拒绝、要求证据和有限条件转变写出有权否决的次要角色"
  outcome: "获得的是具体条件下、仍待更多人响应的局部合作，绝非整个联盟已经完全成立。"
  outcome_scope: ORIGINAL_SCENE_ONLY_NO_UNSEEN_FUTURE
  counterpressure_or_limit: "本书军事筹划和对价数字均不作为现实谈判或战术教程；庞雨的理解不等同协议最终实现。"
  task_ids: [TX-06]
  tags: [fictional-scene, source-anchored, negotiation, conditional-consent]
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
- id: c14
  title: "功劳记录的虚增建议被当事人撕毁拒绝"
  type: case
  example_kind: fictional_narrative_case
  source_reality: FICTIONAL_NOVEL_SCENE_NOT_HISTORICAL_EVIDENCE
  example_kind_extension_status: REQUIRES_STAGE1_5_REVIEW
  source_chapter: "《铁血残明》有效叙事n526；n526/p82；n526/p85；n526/p87"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA
  source_loci:
    - "n526/p82"
    - "n526/p85"
    - "n526/p87"
  chunk_ids:
    - "ck-2fe7ec8ea640"
  summary: |-
    场景起因：战功经过笔录要被整理成正式可传播的文字。
    角色行动：文书官建议调整不相符的数字以求体面，当事人明确拒绝并毁掉该版本文书。
    在所引场景可核的结果：可确认这份当场记录遭拒而不是已刊发；事实、善意修辞和虚增彼此冲突。
    可研究的叙事作用：让信息版本争议产生不可逆的现场动作与关系后果。
    限制与竞争解释：不能据此判断所有报告皆虚假，也不能将其当作虚报技巧。
    来源性质：本例是虚构小说内部场景，不是作者亲历、真实历史事件或演算例题。
    待Stage1.5核对多章节后果与新写作任务增益；不据此创作仿写原著人物及专属情节。
  bound_to:
    - "让信息版本争议产生不可逆的现场动作与关系后果"
  outcome: "可确认这份当场记录遭拒而不是已刊发；事实、善意修辞和虚增彼此冲突。"
  outcome_scope: ORIGINAL_SCENE_ONLY_NO_UNSEEN_FUTURE
  counterpressure_or_limit: "不能据此判断所有报告皆虚假，也不能将其当作虚报技巧。"
  task_ids: [TX-09]
  tags: [fictional-scene, source-anchored, document-conflict, visible-rejection]
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
- id: c15
  title: "士兵请假接家眷：附条件许可与同袍援助两条线"
  type: case
  example_kind: fictional_narrative_case
  source_reality: FICTIONAL_NOVEL_SCENE_NOT_HISTORICAL_EVIDENCE
  example_kind_extension_status: REQUIRES_STAGE1_5_REVIEW
  source_chapter: "《铁血残明》有效叙事n527；n527/p30；n527/p31；n527/p42；n527/p47"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA
  source_loci:
    - "n527/p30"
    - "n527/p31"
    - "n527/p42"
    - "n527/p47"
  chunk_ids:
    - "ck-744b1d1ff9a3"
  summary: |-
    场景起因：几名成员提出回乡接家属的请求，同时有旅费和岗位担保约束。
    角色行动：主管批准带条件的离队安排，随后同行者在营门外给予当事人钱款和相送。
    在所引场景可核的结果：文本直接呈现当事人携物离营，却没有证明他最终接到了家眷或已如期归队。
    可研究的叙事作用：把上级行政许可和同伴自发帮助交叉呈现，使普通人的生活目标有后续债务。
    限制与竞争解释：制度批准不等于生活顺利；不同人的钱物是个人选择，并非所有成员负有同样义务。
    来源性质：本例是虚构小说内部场景，不是作者亲历、真实历史事件或演算例题。
    待Stage1.5核对多章节后果与新写作任务增益；不据此创作仿写原著人物及专属情节。
  bound_to:
    - "把上级行政许可和同伴自发帮助交叉呈现，使普通人的生活目标有后续债务"
  outcome: "文本直接呈现当事人携物离营，却没有证明他最终接到了家眷或已如期归队。"
  outcome_scope: ORIGINAL_SCENE_ONLY_NO_UNSEEN_FUTURE
  counterpressure_or_limit: "制度批准不等于生活顺利；不同人的钱物是个人选择，并非所有成员负有同样义务。"
  task_ids: [TX-08, TX-07]
  tags: [fictional-scene, source-anchored, subaltern-agency, personal-support]
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
- id: c16
  title: "周月如在账务风险与同事担忧中落笔新责任"
  type: case
  example_kind: fictional_narrative_case
  source_reality: FICTIONAL_NOVEL_SCENE_NOT_HISTORICAL_EVIDENCE
  example_kind_extension_status: REQUIRES_STAGE1_5_REVIEW
  source_chapter: "《铁血残明》有效叙事n532；n532/p39；n532/p43；n532/p46；n532/p49"
  source_quote: ""
  source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA
  source_loci:
    - "n532/p39"
    - "n532/p43"
    - "n532/p46"
    - "n532/p49"
  chunk_ids:
    - "ck-988023f3637e"
  summary: |-
    场景起因：账房同事对前期擅自发行与未来义务表达忧虑，计划上的下一期金额尚空。
    角色行动：周月如先承认责任并犹疑，最后重新坐下在纸上填写一个金额。
    在所引场景可核的结果：给定EPUB版本最后可见的动作是写下一项承诺金额，不包含以后实际发行、偿付或破产结论。
    可研究的叙事作用：以一次可见决策关闭章节，但把结果债务留在未叙述的以后。
    限制与竞争解释：人物的金融估算不是历史事实或可执行方案，不能从未提供的后续剧情推断财务成败。
    来源性质：本例是虚构小说内部场景，不是作者亲历、真实历史事件或演算例题。
    待Stage1.5核对多章节后果与新写作任务增益；不据此创作仿写原著人物及专属情节。
  bound_to:
    - "以一次可见决策关闭章节，但把结果债务留在未叙述的以后"
  outcome: "给定EPUB版本最后可见的动作是写下一项承诺金额，不包含以后实际发行、偿付或破产结论。"
  outcome_scope: ORIGINAL_SCENE_ONLY_NO_UNSEEN_FUTURE
  counterpressure_or_limit: "人物的金融估算不是历史事实或可执行方案，不能从未提供的后续剧情推断财务成败。"
  task_ids: [TX-10, TX-04]
  tags: [fictional-scene, source-anchored, unpaid-obligation, open-end]
  status: RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN
  verification_state: NOT_STARTED_STAGE1_5
```

## 类型边界与覆盖缺口

16条均为`fictional_narrative_case`，属于文学研究时扩展出的故事内案例，而不是作者真实经历或historical case，更不是源书给出的worked_example。严格保留对原版类型契约的偏离，不把16条当作最终可发布的A1技能实例，Stage1.5需要作出明确裁决。全部TX-01—TX-10在RAW层有至少一项来源候选；六段研究弧均有选取证据，并不等于任务执行率100%。

R042历史14条来源及文学错引仍由`R042_OLD_CLAIM_QUARANTINE.tsv`隔离，不能直接晋级，其他Stage0旧结论继续B_PROVISIONAL_UNTIL_SOURCE_CHECK。本轮只执行R050，不启动R051及其后流程，不造新SKILL或计算规则。
