# V13｜新版唯一执行轮次表 v13.1（110轮）
 
status: EFFECTIVE_BY_EXPLICIT_USER_INSTRUCTION
user_approval_date: 2026-10-10
plan_version: v13.1-rebased-110
current_round: R057
passed_rounds: 56
total_rounds: 110
original_plan: V13_FIXED_89_ROUNDS.md (READ_ONLY_HISTORICAL)
historical_ledger: ROUND_LEDGER.csv (READ_ONLY_HISTORICAL)
authoritative_cursor: V13_CURRENT_V2.json
authoritative_ledger: V13_LEDGER_V2.csv
legacy_to_new: V13_ROUND_REMAP_V2.tsv
restoration: START_HERE.md → V13_CURRENT_V2.json → V13_LEDGER_V2.csv → 本文件 → 原版SKILL
execution_trigger: MANUAL_USER_TRIGGER_ONLY_ONE_ROUND

## 修订授权与范围

用户明确提出「前面还有几个冻结的轮次也需要处理，这里也需要处理，现在需要你把所有要处理的和后面还没有开始的，重新整理成一个新的轮次表，按找轮次表进行，这样才不会乱」。此指令授权**改动V13原管理轮次表**而非改变Cangjie/Nuwa原版校验标准。新版固定**110轮**：R001—R056原完成状态保持；新插入21个R057—R077正式修复轮；旧R057归入新版R078作最终四类分流；旧R058—R089依序变为新版R079—R110（+21）。旧89轮编号原文件和老运行收据全部保留供审计，但不再作为未来启动依据。

**绝不因此称重复阅读/旧方法已证实**。两书1103个叙事章旧阅读账不清零；旧质量债需逐项定向核证、尚存不足据实隔离。47个原V1/V2有限通过候选全部逐方法V3复核，不是首条成功就停；39个V1 REVIEW全部来源复查，11个V2 NOT_TESTED全测，但不要求全部PASS。14旧隔离额外逐项处置；其他历史B质量风险按风险分层实审。已完成R054/R055/R056的原始研究产物不覆盖，只写新版delta和补证输出。

**证据门**：A原文SHA/支持位置≠B文学机制解释≠C陌生原创输出。V1/V2/V3各项严格据实，只有合格的进入verified；用户批准轮次变更或GitHub Actions结构全绿，都不替代文学与独立创作效用。新版R078若verified=0须据原版仓颉停止编译并向用户展示缺口，不能将参考/待核伪造为R079可用输入。Nuwa Phase1—5和R109四臂密封盲测保持原版实证要求；独立人/模型资源实际不存在时标NOT_RUN，不可单Agent假装双盲。

## 全部110轮唯一执行顺序

|新版轮次|阶段|工作包|状态|原旧轮|
|---|---|---|---|---|
|R001|A 准备|建立V13清洁仓库与权威状态|PASSED|R001|
|R002|A 准备|V13原著SHA/EPUB叙事章映射|PASSED|R002|
|R003|A 准备|仓颉原版输入和环境自检|PASSED|R003|
|R004|A 准备|女娲Phase0正式范围与档位|PASSED|R004|
|R005|A 准备|女娲Phase0.5独立目录|PASSED|R005|
|R006|A 准备|冻结Stage0阅读证据合同和保留盲测|PASSED|R006|
|R007|B Cangjie Stage0原著阅读|《晚明》全文第001—040章|PASSED|R007|
|R008|B Cangjie Stage0原著阅读|《铁血残明》全文第001—040章|PASSED|R008|
|R009|B Cangjie Stage0原著阅读|《晚明》全文第041—080章|PASSED|R009|
|R010|B Cangjie Stage0原著阅读|《铁血残明》全文第041—080章|PASSED|R010|
|R011|B Cangjie Stage0原著阅读|《晚明》全文第081—120章|PASSED|R011|
|R012|B Cangjie Stage0原著阅读|《铁血残明》全文第081—120章|PASSED|R012|
|R013|B Cangjie Stage0原著阅读|《晚明》全文第121—160章|PASSED|R013|
|R014|B Cangjie Stage0原著阅读|《铁血残明》全文第121—160章|PASSED|R014|
|R015|B Cangjie Stage0原著阅读|《晚明》全文第161—200章|PASSED|R015|
|R016|B Cangjie Stage0原著阅读|《铁血残明》全文第161—200章|PASSED|R016|
|R017|B Cangjie Stage0原著阅读|《晚明》全文第201—240章|PASSED|R017|
|R018|B Cangjie Stage0原著阅读|《铁血残明》全文第201—240章|PASSED|R018|
|R019|B Cangjie Stage0原著阅读|《晚明》全文第241—280章|PASSED|R019|
|R020|B Cangjie Stage0原著阅读|《铁血残明》全文第241—280章|PASSED|R020|
|R021|B Cangjie Stage0原著阅读|《晚明》全文第281—320章|PASSED|R021|
|R022|B Cangjie Stage0原著阅读|《铁血残明》全文第281—320章|PASSED|R022|
|R023|B Cangjie Stage0原著阅读|《晚明》全文第321—360章|PASSED|R023|
|R024|B Cangjie Stage0原著阅读|《铁血残明》全文第321—360章|PASSED|R024|
|R025|B Cangjie Stage0原著阅读|《晚明》全文第361—400章|PASSED|R025|
|R026|B Cangjie Stage0原著阅读|《铁血残明》全文第361—400章|PASSED|R026|
|R027|B Cangjie Stage0原著阅读|《晚明》全文第401—440章|PASSED|R027|
|R028|B Cangjie Stage0原著阅读|《铁血残明》全文第401—440章|PASSED|R028|
|R029|B Cangjie Stage0原著阅读|《晚明》全文第441—480章|PASSED|R029|
|R030|B Cangjie Stage0原著阅读|《铁血残明》全文第441—480章|PASSED|R030|
|R031|B Cangjie Stage0原著阅读|《晚明》全文第481—520章|PASSED|R031|
|R032|B Cangjie Stage0原著阅读|《铁血残明》全文第481—520章|PASSED|R032|
|R033|B Cangjie Stage0原著阅读|《晚明》全文第521—560章|PASSED|R033|
|R034|B Cangjie Stage0原著阅读|《铁血残明》全文第521—532章|PASSED|R034|
|R035|B Cangjie Stage0原著阅读|《晚明》全文第561—571章|PASSED|R035|
|R036|C Adler与确认|《晚明》Stage0结构分析|PASSED|R036|
|R037|C Adler与确认|《晚明》Stage0解释分析|PASSED|R037|
|R038|C Adler与确认|《晚明》Stage0批判与应用|PASSED|R038|
|R039|C Adler与确认|《铁血残明》Stage0结构分析|PASSED|R039|
|R040|C Adler与确认|《铁血残明》Stage0解释分析|PASSED|R040|
|R041|C Adler与确认|《铁血残明》Stage0批判与应用|PASSED|R041|
|R042|C Adler与确认|两书BOOK_OVERVIEW与Stage0用户关口|PASSED|R042|
|R043|D Stage1五提取器|《晚明》框架提取器独立执行|PASSED|R043|
|R044|D Stage1五提取器|《晚明》原则提取器独立执行|PASSED|R044|
|R045|D Stage1五提取器|《晚明》案例提取器独立执行|PASSED|R045|
|R046|D Stage1五提取器|《晚明》反例提取器独立执行|PASSED|R046|
|R047|D Stage1五提取器|《晚明》术语提取器独立执行|PASSED|R047|
|R048|D Stage1五提取器|《铁血残明》框架提取器独立执行|PASSED|R048|
|R049|D Stage1五提取器|《铁血残明》原则提取器独立执行|PASSED|R049|
|R050|D Stage1五提取器|《铁血残明》案例提取器独立执行|PASSED|R050|
|R051|D Stage1五提取器|《铁血残明》反例提取器独立执行|PASSED|R051|
|R052|D Stage1五提取器|《铁血残明》术语提取器独立执行|PASSED|R052|
|R053|E Stage1.5三重验证|两书候选合并、去重与任务覆盖|PASSED|R053|
|R054|E Stage1.5三重验证|Stage1.5 V1来源充分性|PASSED|R054|
|R055|E Stage1.5三重验证|Stage1.5 V2合法新输入可执行|PASSED|R055|
|R056|E Stage1.5三重验证|Stage1.5 V3任务增益|PASSED|R056|
|R057|I 审计恢复|遗留冻结问题全量锁定与风险分层|NOT_STARTED|NEW|
|R058|I 旧源风险|R008—R015及R017高风险文学证据定向补审|NOT_STARTED|NEW|
|R059|I 旧源风险|R007、R016、R018—R024纠正与中风险文学证据补审|NOT_STARTED|NEW|
|R060|I 旧源隔离|《晚明》R042历史隔离旧主张7条逐项处置|NOT_STARTED|NEW|
|R061|I 旧源隔离|《铁血残明》R042历史隔离旧主张7条逐项处置|NOT_STARTED|NEW|
|R062|I 文学汇总|两书BOOK_OVERVIEW与任务清单的质量债闭合映射|NOT_STARTED|NEW|
|R063|J V1补证|《晚明》23条V1 REVIEW逐项复核|NOT_STARTED|NEW|
|R064|J V1补证|《铁血残明》16条V1 REVIEW逐项复核|NOT_STARTED|NEW|
|R065|J V2补证|《晚明》5条原V2未测及新V1通过方法演练|NOT_STARTED|NEW|
|R066|J V2补证|《铁血残明》6条原V2未测及新V1通过方法演练|NOT_STARTED|NEW|
|R067|K V3合同|V3逐方法对照冻结与47条全量任务分配|NOT_STARTED|NEW|
|R068|K V3逐项核验|《晚明》V3逐方法对照 第1/3批（7条）|NOT_STARTED|NEW|
|R069|K V3逐项核验|《晚明》V3逐方法对照 第2/3批（7条）|NOT_STARTED|NEW|
|R070|K V3逐项核验|《晚明》V3逐方法对照 第3/3批（7条）|NOT_STARTED|NEW|
|R071|K V3逐项核验|《铁血残明》V3逐方法对照 第1/4批（7条）|NOT_STARTED|NEW|
|R072|K V3逐项核验|《铁血残明》V3逐方法对照 第2/4批（7条）|NOT_STARTED|NEW|
|R073|K V3逐项核验|《铁血残明》V3逐方法对照 第3/4批（6条）|NOT_STARTED|NEW|
|R074|K V3逐项核验|《铁血残明》V3逐方法对照 第4/4批（6条）|NOT_STARTED|NEW|
|R075|K V3补充|《晚明》新获V2合格方法的V3闭环与边界补证|NOT_STARTED|NEW|
|R076|K V3补充|《铁血残明》新获V2合格方法的V3闭环与边界补证|NOT_STARTED|NEW|
|R077|K 质量审计|两书全部47条V3证据及新增方法独立性、反例、任务覆盖总审计|NOT_STARTED|NEW|
|R078|L Stage1.5验收|更新四类分流、coverage-audit与新版用户确认|NOT_STARTED|R057|
|R079|F Stage1.6—Stage5|Stage1.6独立Skill晋级门|NOT_STARTED|R058|
|R080|F Stage1.6—Stage5|《晚明》RIA++与Bundle|NOT_STARTED|R059|
|R081|F Stage1.6—Stage5|《铁血残明》RIA++与Bundle|NOT_STARTED|R060|
|R082|F Stage1.6—Stage5|《晚明》Zettelkasten依赖与术语|NOT_STARTED|R061|
|R083|F Stage1.6—Stage5|《铁血残明》Zettelkasten依赖与术语|NOT_STARTED|R062|
|R084|F Stage1.6—Stage5|《晚明》Stage4触发/路由压测|NOT_STARTED|R063|
|R085|F Stage1.6—Stage5|《铁血残明》Stage4触发/路由压测|NOT_STARTED|R064|
|R086|F Stage1.6—Stage5|《晚明》Stage4真实任务输出压测|NOT_STARTED|R065|
|R087|F Stage1.6—Stage5|《铁血残明》Stage4真实任务输出压测|NOT_STARTED|R066|
|R088|F Stage1.6—Stage5|Stage4失败回炉与回归|NOT_STARTED|R067|
|R089|F Stage1.6—Stage5|《晚明》Stage5编译与DIGEST|NOT_STARTED|R068|
|R090|F Stage1.6—Stage5|《铁血残明》Stage5编译与DIGEST|NOT_STARTED|R069|
|R091|G Nuwa Phase1—5|主题3—5独立学派/代表选择与来源边界|NOT_STARTED|R070|
|R092|G Nuwa Phase1—5|主题路径第1个独立观点来源研究|NOT_STARTED|R071|
|R093|G Nuwa Phase1—5|主题路径第2个独立观点来源研究|NOT_STARTED|R072|
|R094|G Nuwa Phase1—5|主题路径第3个独立观点来源研究|NOT_STARTED|R073|
|R095|G Nuwa Phase1—5|主题路径第4个独立观点来源研究|NOT_STARTED|R074|
|R096|G Nuwa Phase1—5|主题路径第5个独立观点来源研究|NOT_STARTED|R075|
|R097|G Nuwa Phase1—5|Nuwa Phase1维度汇总与冲突账|NOT_STARTED|R076|
|R098|G Nuwa Phase1—5|Phase1.5调研质量审查与用户关口|NOT_STARTED|R077|
|R099|G Nuwa Phase1—5|Phase2心智模型独立提炼|NOT_STARTED|R078|
|R100|G Nuwa Phase1—5|Phase2启发式、表达DNA与诚实边界|NOT_STARTED|R079|
|R101|G Nuwa Phase1—5|Phase2.5模型与DNA用户确认|NOT_STARTED|R080|
|R102|G Nuwa Phase1—5|Phase3主题SKILL与Agentic Protocol|NOT_STARTED|R081|
|R103|G Nuwa Phase1—5|Phase4独立已知/边缘/表达实测|NOT_STARTED|R082|
|R104|G Nuwa Phase1—5|Phase4质量脚本、迭代上限和用户关口|NOT_STARTED|R083|
|R105|G Nuwa Phase1—5|Phase5独立优化主体A|NOT_STARTED|R084|
|R106|G Nuwa Phase1—5|Phase5独立优化主体B|NOT_STARTED|R085|
|R107|G Nuwa Phase1—5|Phase5合并改动、回归与用户确认|NOT_STARTED|R086|
|R108|H V13创作融合|统一创作技能路由/契约|NOT_STARTED|R087|
|R109|H V13创作融合|四臂盲测与长篇连续性压力|NOT_STARTED|R088|
|R110|H V13创作融合|GitHub出厂、干净会话恢复与用户验收|NOT_STARTED|R089|

## R057—R110未开始轮次的完整合同

每轮必须按`V13_CURRENT_V2.json`唯一游标，由用户明确输入「继续」后执行；先读冻结原版Cangjie/Nuwa本轮SKILL及所有适用依赖；执行新轮真实工作、记录来源证据、评估、提交GitHub、Actions与主分支回读；成功才PASS并推进游标，但**不在同一用户指令自动开始下一轮**。失败标FAILED/IN_PROGRESS/BLOCKED并保留同一轮检查点。第R078/R089/R090/R098/R101/R104/R107/R110等继承的用户关口仍须真实批准；任何模型/服务额外付费需另获明确同意。

### R057 · 遗留冻结问题全量锁定与风险分层
- 来源：用户2026-10-10明确新增的修复轮；继承原版Cangjie/Nuwa方法与已核来源
- **必须操作**：重新合并R007—R024的296条历史机制声明及18批次风险、14条R042隔离旧主张、39条V1 REVIEW、11条V2未测、47条V3未证增益与19项任务；对照原EPUB SHA/章节索引；预注册质量抽审与V3评估合同；冻结各对象的唯一ID、阶段归属与不能自动升级字段。
- **必须产物**：runs/R057_V2.md; v2/BASELINE_LOCK.json; v2/ISSUE_REGISTRY.tsv
- **验收标准**：所有14+39+11+47逐ID无遗漏无重复、296条旧机制保留高低风险清单、19任务全部映射；仅冻结责任无自动PASS；Actions及远程回读
- **硬门/状态**：AUTO
- **依据/备注**：旧R007—R024、R042、R054—R057；R006原文证据合同
- **失败处理**：不足则当前轮IN_PROGRESS/FAILED/BLOCKED，写`runs/R057_V2.md`，不把单条假PASS计入verified；GitHub CI只能验结构与溯源，内容需真实核验。

### R058 · R008—R015及R017高风险文学证据定向补审
- 来源：用户2026-10-10明确新增的修复轮；继承原版Cangjie/Nuwa方法与已核来源
- **必须操作**：以源R008—R015、R017的模板化风险为高优先，不重做9轮全部旧阅读；按故事弧/人物/叙述视角/反例类型冻结样本抽审真实EPUB上下文；核验每条被抽源结论和反例搜索；发现批次共性错误按风险政策扩大到相关机制。
- **必须产物**：v2/stage0/HIGH_RISK_SOURCE_AUDIT.md; runs/R058_V2.md
- **验收标准**：九个高风险原轮均有真实抽审范围/证据/保留缺口或修订决定；不得仅SHA字段证明文学质量
- **硬门/状态**：AUTO
- **依据/备注**：cangjie/reading/STAGE0_QUALITY_DEBT_AUDIT.md; STAGE0_QUALITY_CONTROL_POLICY.md
- **失败处理**：不足则当前轮IN_PROGRESS/FAILED/BLOCKED，写`runs/R058_V2.md`，不把单条假PASS计入verified；GitHub CI只能验结构与溯源，内容需真实核验。

### R059 · R007、R016、R018—R024纠正与中风险文学证据补审
- 来源：用户2026-10-10明确新增的修复轮；继承原版Cangjie/Nuwa方法与已核来源
- **必须操作**：复核R007和R024已有定向修订的有效性；对R016、R018—R023分层核对支持锚点及反例，不对历史阅读章数重新计数；归档仍未核的B主张和失效边界。
- **必须产物**：v2/stage0/MEDIUM_REPAIRED_SOURCE_AUDIT.md; runs/R059_V2.md
- **验收标准**：包括旧R007/R016/R018—R024的所有指定轮，每批有真实审计记录；只在证据充分处标窄PASS，未核内容仍B PROVISIONAL
- **硬门/状态**：AUTO
- **依据/备注**：R007、R016、R018—R024原章证据和质量债
- **失败处理**：不足则当前轮IN_PROGRESS/FAILED/BLOCKED，写`runs/R059_V2.md`，不把单条假PASS计入verified；GitHub CI只能验结构与溯源，内容需真实核验。

### R060 · 《晚明》R042历史隔离旧主张7条逐项处置
- 来源：用户2026-10-10明确新增的修复轮；继承原版Cangjie/Nuwa方法与已核来源
- **必须操作**：按gates/R057_LEGACY_QUARANTINE.tsv中wanming七个原ID逐条复读原书定位，区分现场动作/人物判断/未兑现结果，搜索反例；决定保留隔离/证实后重建新候选/有证据拒绝；禁止直接复活旧主张。
- **必须产物**：v2/legacy/WANMING_7_DECISIONS.tsv; runs/R060_V2.md
- **验收标准**：精确7/7有来源、反例与单条去向；未解决标OPEN_QUARANTINED而非假称已认证
- **硬门/状态**：AUTO
- **依据/备注**：R042_OLD_CLAIM_QUARANTINE.tsv; gates/R057_LEGACY_QUARANTINE.tsv
- **失败处理**：不足则当前轮IN_PROGRESS/FAILED/BLOCKED，写`runs/R060_V2.md`，不把单条假PASS计入verified；GitHub CI只能验结构与溯源，内容需真实核验。

### R061 · 《铁血残明》R042历史隔离旧主张7条逐项处置
- 来源：用户2026-10-10明确新增的修复轮；继承原版Cangjie/Nuwa方法与已核来源
- **必须操作**：按gates/R057_LEGACY_QUARANTINE.tsv中tiexuecanming七个原ID逐条核章、人物认知与结果时态；由原始证据支持新主张则重新走V1/V2/V3，不直接晋级。
- **必须产物**：v2/legacy/TIEXUE_7_DECISIONS.tsv; runs/R061_V2.md
- **验收标准**：精确7/7有真实复核与去向；旧隔离不因排到本轮即自动解除
- **硬门/状态**：AUTO
- **依据/备注**：R042_OLD_CLAIM_QUARANTINE.tsv; gates/R057_LEGACY_QUARANTINE.tsv
- **失败处理**：不足则当前轮IN_PROGRESS/FAILED/BLOCKED，写`runs/R061_V2.md`，不把单条假PASS计入verified；GitHub CI只能验结构与溯源，内容需真实核验。

### R062 · 两书BOOK_OVERVIEW与任务清单的质量债闭合映射
- 来源：用户2026-10-10明确新增的修复轮；继承原版Cangjie/Nuwa方法与已核来源
- **必须操作**：交叉比对R058—R061的复核结果、两书BOOK_OVERVIEW和19个Stage0写作任务，形成“源A真实性/文学B解释/原创C效用”三层状态；修订须以delta/附录形式保存历史R042批准稿，不沉默覆盖。
- **必须产物**：v2/stage0/BOOK_OVERVIEW_DELTA.md; v2/stage0/QUALITY_DEBT_ROUTING.tsv; runs/R062_V2.md
- **验收标准**：14条旧隔离、早期风险和19任务各有真实去向与源引用；不宣称整本书的全部文学B已独立证实
- **硬门/状态**：AUTO
- **依据/备注**：R042批准原overview、R058-R061单轮审计
- **失败处理**：不足则当前轮IN_PROGRESS/FAILED/BLOCKED，写`runs/R062_V2.md`，不把单条假PASS计入verified；GitHub CI只能验结构与溯源，内容需真实核验。

### R063 · 《晚明》23条V1 REVIEW逐项复核
- 来源：用户2026-10-10明确新增的修复轮；继承原版Cangjie/Nuwa方法与已核来源
- **必须操作**：逐条以R054原理由及本轮原EPUB现场反例复核23个原ID；可收窄V1限定PASS、继续REVIEW或确证REJECTED；案例/反例不因引用价值自动变执行方法。
- **必须产物**：v2/v1/WANMING_23_RESULTS.tsv; runs/R063_V2.md
- **验收标准**：23/23有真实审核、证据范围、负例/边界、最终V1结论，不能先挑有利样本
- **硬门/状态**：AUTO
- **依据/备注**：gates/R057_REPAIR_V1_39_QUEUE.tsv; books/wanming/validation/V1_EVIDENCE.tsv
- **失败处理**：不足则当前轮IN_PROGRESS/FAILED/BLOCKED，写`runs/R063_V2.md`，不把单条假PASS计入verified；GitHub CI只能验结构与溯源，内容需真实核验。

### R064 · 《铁血残明》16条V1 REVIEW逐项复核
- 来源：用户2026-10-10明确新增的修复轮；继承原版Cangjie/Nuwa方法与已核来源
- **必须操作**：核验R054原缺口与跨章因果、人物计划/结果、反例和史实外证边界；逐项给出来源窄PASS/REVIEW/有据REJECTED，非方法项目不硬转成Skill。
- **必须产物**：v2/v1/TIEXUE_16_RESULTS.tsv; runs/R064_V2.md
- **验收标准**：16/16保留原ID与真实可回看判定；合并两书39/39无遗漏
- **硬门/状态**：AUTO
- **依据/备注**：gates/R057_REPAIR_V1_39_QUEUE.tsv; books/tiexuecanming/validation/V1_EVIDENCE.tsv
- **失败处理**：不足则当前轮IN_PROGRESS/FAILED/BLOCKED，写`runs/R064_V2.md`，不把单条假PASS计入verified；GitHub CI只能验结构与溯源，内容需真实核验。

### R065 · 《晚明》5条原V2未测及新V1通过方法演练
- 来源：用户2026-10-10明确新增的修复轮；继承原版Cangjie/Nuwa方法与已核来源
- **必须操作**：对原5条WM-f11/f16/p06/p13/p18，及R063新认定可执行方法，先冻结独立合法新输入和条件，后真正产出可核纸面演练，记录不适用/失败。
- **必须产物**：v2/v2/WANMING_FROZEN_INPUTS.json; v2/v2/WANMING_RESULTS.tsv; runs/R065_V2.md
- **验收标准**：原5/5均有真实V2结果，所有新V1升级且可执行方法有V2去向；纸面walkthrough不冒充宿主Stage4
- **硬门/状态**：AUTO
- **依据/备注**：R055历史19新任务；R063结果
- **失败处理**：不足则当前轮IN_PROGRESS/FAILED/BLOCKED，写`runs/R065_V2.md`，不把单条假PASS计入verified；GitHub CI只能验结构与溯源，内容需真实核验。

### R066 · 《铁血残明》6条原V2未测及新V1通过方法演练
- 来源：用户2026-10-10明确新增的修复轮；继承原版Cangjie/Nuwa方法与已核来源
- **必须操作**：对TX-f03/f04/f15/p02/p15/p18六条与R064获窄V1通过可执行方法先冻结新题再演练，保留输出/未知/适用范围。
- **必须产物**：v2/v2/TIEXUE_FROZEN_INPUTS.json; v2/v2/TIEXUE_RESULTS.tsv; runs/R066_V2.md
- **验收标准**：原6/6真实V2测试及所有新增可执行方法的V2去向，失败不自动PASS
- **硬门/状态**：AUTO
- **依据/备注**：R055历史任务；R064结果
- **失败处理**：不足则当前轮IN_PROGRESS/FAILED/BLOCKED，写`runs/R066_V2.md`，不把单条假PASS计入verified；GitHub CI只能验结构与溯源，内容需真实核验。

### R067 · V3逐方法对照冻结与47条全量任务分配
- 来源：用户2026-10-10明确新增的修复轮；继承原版Cangjie/Nuwa方法与已核来源
- **必须操作**：冻结原47方法（21晚明+26铁血）逐项完整ID/任务/验收指标/失败判据，保证同题有方法与无方法两臂除单方法操作卡外输入一致；对R065—R066新增V2通过的方法另开队列，未通过者留待核；先提交冻结输入再写输出。
- **必须产物**：v2/v3/FROZEN_TEST_CONTRACT.json; v2/v3/V3_TASK_ALLOCATIONS.tsv; runs/R067_V2.md
- **验收标准**：47/47均有唯一单方法测试合同、同题基线和可检效用假说；新增候选也全部已分流；独立评审条件如实标可用性；未写输出时不能伪称完成
- **硬门/状态**：AUTO
- **依据/备注**：R056已知201:203负例；gates/R057_FULL47_V3_EXECUTION.md
- **失败处理**：不足则当前轮IN_PROGRESS/FAILED/BLOCKED，写`runs/R067_V2.md`，不把单条假PASS计入verified；GitHub CI只能验结构与溯源，内容需真实核验。

### R068 · 《晚明》V3逐方法对照 第1/3批（7条）
- 来源：用户2026-10-10明确新增的修复轮；继承原版Cangjie/Nuwa方法与已核来源
- **必须操作**：依R067冻结合同，对本轮7条 WM-f01、WM-f02、WM-f04、WM-f06、WM-f08、WM-f10、WM-f12 分别生成独立原创新输入下的候选/普通对照，保存真实输出和预定义评判指标；单方法隔离防止旧R056混搭归因。
- **必须产物**：v2/v3/results/R68_WM_7.tsv; v2/v3/outputs/R68/; runs/R68_V2.md
- **验收标准**：精确本批7/7均有双臂原始输出、差值、反例及候选级初判；不要求7条都PASS；同Agent非盲须如实标局限
- **硬门/状态**：AUTO
- **依据/备注**：R067合同，原V1/V2 R054/R055记录；确切ID WM-f01,WM-f02,WM-f04,WM-f06,WM-f08,WM-f10,WM-f12
- **失败处理**：不足则当前轮IN_PROGRESS/FAILED/BLOCKED，写`runs/R068_V2.md`，不把单条假PASS计入verified；GitHub CI只能验结构与溯源，内容需真实核验。

### R069 · 《晚明》V3逐方法对照 第2/3批（7条）
- 来源：用户2026-10-10明确新增的修复轮；继承原版Cangjie/Nuwa方法与已核来源
- **必须操作**：依R067冻结合同，对本轮7条 WM-f13、WM-f14、WM-p01、WM-p03、WM-p04、WM-p05、WM-p07 分别生成独立原创新输入下的候选/普通对照，保存真实输出和预定义评判指标；单方法隔离防止旧R056混搭归因。
- **必须产物**：v2/v3/results/R69_WM_7.tsv; v2/v3/outputs/R69/; runs/R69_V2.md
- **验收标准**：精确本批7/7均有双臂原始输出、差值、反例及候选级初判；不要求7条都PASS；同Agent非盲须如实标局限
- **硬门/状态**：AUTO
- **依据/备注**：R067合同，原V1/V2 R054/R055记录；确切ID WM-f13,WM-f14,WM-p01,WM-p03,WM-p04,WM-p05,WM-p07
- **失败处理**：不足则当前轮IN_PROGRESS/FAILED/BLOCKED，写`runs/R069_V2.md`，不把单条假PASS计入verified；GitHub CI只能验结构与溯源，内容需真实核验。

### R070 · 《晚明》V3逐方法对照 第3/3批（7条）
- 来源：用户2026-10-10明确新增的修复轮；继承原版Cangjie/Nuwa方法与已核来源
- **必须操作**：依R067冻结合同，对本轮7条 WM-p08、WM-p12、WM-p14、WM-p19、WM-p20、WM-p21、WM-p23 分别生成独立原创新输入下的候选/普通对照，保存真实输出和预定义评判指标；单方法隔离防止旧R056混搭归因。
- **必须产物**：v2/v3/results/R70_WM_7.tsv; v2/v3/outputs/R70/; runs/R70_V2.md
- **验收标准**：精确本批7/7均有双臂原始输出、差值、反例及候选级初判；不要求7条都PASS；同Agent非盲须如实标局限
- **硬门/状态**：AUTO
- **依据/备注**：R067合同，原V1/V2 R054/R055记录；确切ID WM-p08,WM-p12,WM-p14,WM-p19,WM-p20,WM-p21,WM-p23
- **失败处理**：不足则当前轮IN_PROGRESS/FAILED/BLOCKED，写`runs/R070_V2.md`，不把单条假PASS计入verified；GitHub CI只能验结构与溯源，内容需真实核验。

### R071 · 《铁血残明》V3逐方法对照 第1/4批（7条）
- 来源：用户2026-10-10明确新增的修复轮；继承原版Cangjie/Nuwa方法与已核来源
- **必须操作**：依R067冻结合同，对 TX-f01、TX-f02、TX-f05、TX-f08、TX-f09、TX-f10、TX-f11 分别做单候选有/无方法等条件的原创任务、双臂输出、适用边界、失败/回退与评分证据，避免外推作者语言。
- **必须产物**：v2/v3/results/R71_TX_7.tsv; v2/v3/outputs/R71/; runs/R71_V2.md
- **验收标准**：本批7/7全部真实生成两臂新输出并有可审判定，未证净增益不能记verified
- **硬门/状态**：AUTO
- **依据/备注**：R067合同，来源R055 TX已有26方法；确切ID TX-f01,TX-f02,TX-f05,TX-f08,TX-f09,TX-f10,TX-f11
- **失败处理**：不足则当前轮IN_PROGRESS/FAILED/BLOCKED，写`runs/R071_V2.md`，不把单条假PASS计入verified；GitHub CI只能验结构与溯源，内容需真实核验。

### R072 · 《铁血残明》V3逐方法对照 第2/4批（7条）
- 来源：用户2026-10-10明确新增的修复轮；继承原版Cangjie/Nuwa方法与已核来源
- **必须操作**：依R067冻结合同，对 TX-f12、TX-f13、TX-f16、TX-p01、TX-p03、TX-p04、TX-p05 分别做单候选有/无方法等条件的原创任务、双臂输出、适用边界、失败/回退与评分证据，避免外推作者语言。
- **必须产物**：v2/v3/results/R72_TX_7.tsv; v2/v3/outputs/R72/; runs/R72_V2.md
- **验收标准**：本批7/7全部真实生成两臂新输出并有可审判定，未证净增益不能记verified
- **硬门/状态**：AUTO
- **依据/备注**：R067合同，来源R055 TX已有26方法；确切ID TX-f12,TX-f13,TX-f16,TX-p01,TX-p03,TX-p04,TX-p05
- **失败处理**：不足则当前轮IN_PROGRESS/FAILED/BLOCKED，写`runs/R072_V2.md`，不把单条假PASS计入verified；GitHub CI只能验结构与溯源，内容需真实核验。

### R073 · 《铁血残明》V3逐方法对照 第3/4批（6条）
- 来源：用户2026-10-10明确新增的修复轮；继承原版Cangjie/Nuwa方法与已核来源
- **必须操作**：依R067冻结合同，对 TX-p06、TX-p07、TX-p08、TX-p09、TX-p11、TX-p12 分别做单候选有/无方法等条件的原创任务、双臂输出、适用边界、失败/回退与评分证据，避免外推作者语言。
- **必须产物**：v2/v3/results/R73_TX_6.tsv; v2/v3/outputs/R73/; runs/R73_V2.md
- **验收标准**：本批6/6全部真实生成两臂新输出并有可审判定，未证净增益不能记verified
- **硬门/状态**：AUTO
- **依据/备注**：R067合同，来源R055 TX已有26方法；确切ID TX-p06,TX-p07,TX-p08,TX-p09,TX-p11,TX-p12
- **失败处理**：不足则当前轮IN_PROGRESS/FAILED/BLOCKED，写`runs/R073_V2.md`，不把单条假PASS计入verified；GitHub CI只能验结构与溯源，内容需真实核验。

### R074 · 《铁血残明》V3逐方法对照 第4/4批（6条）
- 来源：用户2026-10-10明确新增的修复轮；继承原版Cangjie/Nuwa方法与已核来源
- **必须操作**：依R067冻结合同，对 TX-p13、TX-p14、TX-p17、TX-p19、TX-p20、TX-p21 分别做单候选有/无方法等条件的原创任务、双臂输出、适用边界、失败/回退与评分证据，避免外推作者语言。
- **必须产物**：v2/v3/results/R74_TX_6.tsv; v2/v3/outputs/R74/; runs/R74_V2.md
- **验收标准**：本批6/6全部真实生成两臂新输出并有可审判定，未证净增益不能记verified
- **硬门/状态**：AUTO
- **依据/备注**：R067合同，来源R055 TX已有26方法；确切ID TX-p13,TX-p14,TX-p17,TX-p19,TX-p20,TX-p21
- **失败处理**：不足则当前轮IN_PROGRESS/FAILED/BLOCKED，写`runs/R074_V2.md`，不把单条假PASS计入verified；GitHub CI只能验结构与溯源，内容需真实核验。

### R075 · 《晚明》新获V2合格方法的V3闭环与边界补证
- 来源：用户2026-10-10明确新增的修复轮；继承原版Cangjie/Nuwa方法与已核来源
- **必须操作**：对R063→R065中新获得合法V1+V2资格的晚明可执行方法，及从历史14隔离中重建且真正有依据的新候选，若存在逐项同题V3评估；没有新增资格则用零样本有据N/A；另审查WM-04/WM-09既有回退是否有真实修复证据。
- **必须产物**：v2/v3/results/WANMING_ADDITIONAL.tsv; runs/R075_V2.md
- **验收标准**：所有本轮新增eligible WM候选均得到V3实测/明确未能测试并BLOCKED，绝不假装零样本通过；如需较多样本在本轮真实续做
- **硬门/状态**：AUTO
- **依据/备注**：R063、R065与隔离来源复核
- **失败处理**：不足则当前轮IN_PROGRESS/FAILED/BLOCKED，写`runs/R075_V2.md`，不把单条假PASS计入verified；GitHub CI只能验结构与溯源，内容需真实核验。

### R076 · 《铁血残明》新获V2合格方法的V3闭环与边界补证
- 来源：用户2026-10-10明确新增的修复轮；继承原版Cangjie/Nuwa方法与已核来源
- **必须操作**：对R064→R066新符合V1+V2的TX可执行方法和真正重新构建的旧隔离方法，逐ID独立V3验证；无新候选则列有据N/A，防止漏测11条V2原未测中转化的方法。
- **必须产物**：v2/v3/results/TIEXUE_ADDITIONAL.tsv; runs/R076_V2.md
- **验收标准**：新增eligible TX候选全部真实核验并有去向，无增益就是未通过，不能利用别的候选借分
- **硬门/状态**：AUTO
- **依据/备注**：R064、R066与隔离来源复核
- **失败处理**：不足则当前轮IN_PROGRESS/FAILED/BLOCKED，写`runs/R076_V2.md`，不把单条假PASS计入verified；GitHub CI只能验结构与溯源，内容需真实核验。

### R077 · 两书全部47条V3证据及新增方法独立性、反例、任务覆盖总审计
- 来源：用户2026-10-10明确新增的修复轮；继承原版Cangjie/Nuwa方法与已核来源
- **必须操作**：合并R068—R076全量结果，47个原ID必须各有可复核V3结论及双臂输出；判定单方法隔离、同题输入公平性、独立评审是否真实可用，失败可定位；交叉核19项原著任务，质量不足的维持needs_review而非伪PASS。
- **必须产物**：v2/v3/FINAL_47_EVIDENCE_AUDIT.tsv; v2/v3/QUALITY_FINDINGS.md; runs/R077_V2.md
- **验收标准**：固定47/47完成真实V3逐项审计；未经真实独立评价不得称独立C合格；证据错误回到本轮真实修正直到通过检查；缺项BLOCKED
- **硬门/状态**：AUTO
- **依据/备注**：R067—R076真实研究输出、R056不公平基线诊断
- **失败处理**：不足则当前轮IN_PROGRESS/FAILED/BLOCKED，写`runs/R077_V2.md`，不把单条假PASS计入verified；GitHub CI只能验结构与溯源，内容需真实核验。

### R078 · 更新四类分流、coverage-audit与新版用户确认
- 来源：原R057 Stage1.5最终分流关口，结合新版R057—R077的真实新增结果复核
- **必须操作**：对应旧R057历史审计门但重做的是**分流聚合与本轮用户关口**而不是重做V1/V2；按R057—R077的新增真实证据更新原187加合法新增候选的去向，分别记录legacy14，完善reference到Stage3计划，向用户展示verified/reference/needs_review/rejected并确认。
- **必须产物**：books/*/{verified.md,references.md,needs-review.md,coverage-audit.md,rejected/}; gates/CANGJIE_STAGE15_V2.md; runs/R078_V2.md
- **验收标准**：全体可溯源、19任务覆盖与用户明确确认；若0 verified则交付缺口并按仓颉原版停止编译，**不假通过下一轮**
- **硬门/状态**：MANDATORY_USER_CONFIRM
- **依据/备注**：旧R057文件及本新版R057—R077全部证据
- **失败处理**：不足则当前轮IN_PROGRESS/FAILED/BLOCKED，写`runs/R078_V2.md`，不把单条假PASS计入verified；GitHub CI只能验结构与溯源，内容需真实核验。

### R079 · Stage1.6独立Skill晋级门
- 来源：原R058；完整原文合同仍可追溯，映射见V13_ROUND_REMAP_V2.tsv
- **必须操作**：按独立意图/契约/运行3个必过+复用或评测至少1个，给所有候选明确promoted/router去向
- **必须产物**：`books/*/.cangjie/capabilities/destinations.json`
- **验收标准**：不漏去向、active恰好一条路径
- **硬门/状态**：NOT_CHECKED
- **依据/备注**：旧R058 `V13_FIXED_89_ROUNDS.md`；自动核验。必须保存 `runs/R058.md`，包括输入SHA、真实执行、全部检查、未过项、GitHub提交、远程回读。
- **失败处理**：不足则当前轮IN_PROGRESS/FAILED/BLOCKED，写`runs/R079_V2.md`，不把单条假PASS计入verified；GitHub CI只能验结构与溯源，内容需真实核验。

### R080 · 《晚明》RIA++与Bundle
- 来源：原R059；完整原文合同仍可追溯，映射见V13_ROUND_REMAP_V2.tsv
- **必须操作**：为每个verified建立R/I/A1/A2/E/B完整6段，区别原书例与合成例，稳定capability_id
- **必须产物**：`books/wanming/.cangjie/capabilities/verified.yaml + cards/*.md`
- **验收标准**：原版schema校验通过，非verified不得混入
- **硬门/状态**：NOT_CHECKED
- **依据/备注**：旧R059 `V13_FIXED_89_ROUNDS.md`；自动核验。必须保存 `runs/R059.md`，包括输入SHA、真实执行、全部检查、未过项、GitHub提交、远程回读。
- **失败处理**：不足则当前轮IN_PROGRESS/FAILED/BLOCKED，写`runs/R080_V2.md`，不把单条假PASS计入verified；GitHub CI只能验结构与溯源，内容需真实核验。

### R081 · 《铁血残明》RIA++与Bundle
- 来源：原R060；完整原文合同仍可追溯，映射见V13_ROUND_REMAP_V2.tsv
- **必须操作**：为每个verified建立R/I/A1/A2/E/B完整6段，区别原书例与合成例，稳定capability_id
- **必须产物**：`books/tiexuecanming/.cangjie/capabilities/verified.yaml + cards/*.md`
- **验收标准**：原版schema校验通过
- **硬门/状态**：NOT_CHECKED
- **依据/备注**：旧R060 `V13_FIXED_89_ROUNDS.md`；自动核验。必须保存 `runs/R060.md`，包括输入SHA、真实执行、全部检查、未过项、GitHub提交、远程回读。
- **失败处理**：不足则当前轮IN_PROGRESS/FAILED/BLOCKED，写`runs/R081_V2.md`，不把单条假PASS计入verified；GitHub CI只能验结构与溯源，内容需真实核验。

### R082 · 《晚明》Zettelkasten依赖与术语
- 来源：原R061；完整原文合同仍可追溯，映射见V13_ROUND_REMAP_V2.tsv
- **必须操作**：处理also_read、GLOSSARY、近邻区别及reference正式交付去向
- **必须产物**：`books/wanming/GLOSSARY.md + also_read`
- **验收标准**：无死链、参考不冒充active
- **硬门/状态**：NOT_CHECKED
- **依据/备注**：旧R061 `V13_FIXED_89_ROUNDS.md`；自动核验。必须保存 `runs/R061.md`，包括输入SHA、真实执行、全部检查、未过项、GitHub提交、远程回读。
- **失败处理**：不足则当前轮IN_PROGRESS/FAILED/BLOCKED，写`runs/R082_V2.md`，不把单条假PASS计入verified；GitHub CI只能验结构与溯源，内容需真实核验。

### R083 · 《铁血残明》Zettelkasten依赖与术语
- 来源：原R062；完整原文合同仍可追溯，映射见V13_ROUND_REMAP_V2.tsv
- **必须操作**：处理also_read、GLOSSARY、近邻区别及reference正式交付去向
- **必须产物**：`books/tiexuecanming/GLOSSARY.md + also_read`
- **验收标准**：无死链、参考不冒充active
- **硬门/状态**：NOT_CHECKED
- **依据/备注**：旧R062 `V13_FIXED_89_ROUNDS.md`；自动核验。必须保存 `runs/R062.md`，包括输入SHA、真实执行、全部检查、未过项、GitHub提交、远程回读。
- **失败处理**：不足则当前轮IN_PROGRESS/FAILED/BLOCKED，写`runs/R083_V2.md`，不把单条假PASS计入verified；GitHub CI只能验结构与溯源，内容需真实核验。

### R084 · 《晚明》Stage4触发/路由压测
- 来源：原R063；完整原文合同仍可追溯，映射见V13_ROUND_REMAP_V2.tsv
- **必须操作**：每个promoted Skill用3—5正例、2—3负例、1—3边缘和近邻冲突真实触发测试
- **必须产物**：`books/wanming/tests/trigger-prompts.json + results.md`
- **验收标准**：逐个测试有真实输出、分母、失败
- **硬门/状态**：NOT_CHECKED
- **依据/备注**：旧R063 `V13_FIXED_89_ROUNDS.md`；自动核验。必须保存 `runs/R063.md`，包括输入SHA、真实执行、全部检查、未过项、GitHub提交、远程回读。
- **失败处理**：不足则当前轮IN_PROGRESS/FAILED/BLOCKED，写`runs/R084_V2.md`，不把单条假PASS计入verified；GitHub CI只能验结构与溯源，内容需真实核验。

### R085 · 《铁血残明》Stage4触发/路由压测
- 来源：原R064；完整原文合同仍可追溯，映射见V13_ROUND_REMAP_V2.tsv
- **必须操作**：同等正例、负例、边缘与近邻路由实际测试
- **必须产物**：`books/tiexuecanming/tests/trigger-prompts.json + results.md`
- **验收标准**：不能以触发即成功
- **硬门/状态**：NOT_CHECKED
- **依据/备注**：旧R064 `V13_FIXED_89_ROUNDS.md`；自动核验。必须保存 `runs/R064.md`，包括输入SHA、真实执行、全部检查、未过项、GitHub提交、远程回读。
- **失败处理**：不足则当前轮IN_PROGRESS/FAILED/BLOCKED，写`runs/R085_V2.md`，不把单条假PASS计入verified；GitHub CI只能验结构与溯源，内容需真实核验。

### R086 · 《晚明》Stage4真实任务输出压测
- 来源：原R065；完整原文合同仍可追溯，映射见V13_ROUND_REMAP_V2.tsv
- **必须操作**：独立原创任务有/无Skill对照，核叙事质量、遗漏和边界
- **必须产物**：`books/wanming/tests/output-results.md + cases/`
- **验收标准**：真实结果与失败回炉建议
- **硬门/状态**：NOT_CHECKED
- **依据/备注**：旧R065 `V13_FIXED_89_ROUNDS.md`；自动核验。必须保存 `runs/R065.md`，包括输入SHA、真实执行、全部检查、未过项、GitHub提交、远程回读。
- **失败处理**：不足则当前轮IN_PROGRESS/FAILED/BLOCKED，写`runs/R086_V2.md`，不把单条假PASS计入verified；GitHub CI只能验结构与溯源，内容需真实核验。

### R087 · 《铁血残明》Stage4真实任务输出压测
- 来源：原R066；完整原文合同仍可追溯，映射见V13_ROUND_REMAP_V2.tsv
- **必须操作**：独立原创任务有/无Skill对照，核叙事质量、遗漏和边界
- **必须产物**：`books/tiexuecanming/tests/output-results.md + cases/`
- **验收标准**：真实结果与失败回炉建议
- **硬门/状态**：NOT_CHECKED
- **依据/备注**：旧R066 `V13_FIXED_89_ROUNDS.md`；自动核验。必须保存 `runs/R066.md`，包括输入SHA、真实执行、全部检查、未过项、GitHub提交、远程回读。
- **失败处理**：不足则当前轮IN_PROGRESS/FAILED/BLOCKED，写`runs/R087_V2.md`，不把单条假PASS计入verified；GitHub CI只能验结构与溯源，内容需真实核验。

### R088 · Stage4失败回炉与回归
- 来源：原R067；完整原文合同仍可追溯，映射见V13_ROUND_REMAP_V2.tsv
- **必须操作**：把两书触发/路由/输出失败按源追责，退回RIA++修复并重测，不只修改评分
- **必须产物**：`cangjie/FAILURE_REPAIR_LOG.md + regression-results.md`
- **验收标准**：失败已修正或明确不通过
- **硬门/状态**：NOT_CHECKED
- **依据/备注**：旧R067 `V13_FIXED_89_ROUNDS.md`；自动核验。必须保存 `runs/R067.md`，包括输入SHA、真实执行、全部检查、未过项、GitHub提交、远程回读。
- **失败处理**：不足则当前轮IN_PROGRESS/FAILED/BLOCKED，写`runs/R088_V2.md`，不把单条假PASS计入verified；GitHub CI只能验结构与溯源，内容需真实核验。

### R089 · 《晚明》Stage5编译与DIGEST
- 来源：原R068；完整原文合同仍可追溯，映射见V13_ROUND_REMAP_V2.tsv
- **必须操作**：按原版生成DIGEST、compile(single/pack/auto)、validate_skill_pack，报告生成目录及用户交付选择
- **必须产物**：`books/wanming/DIGEST.md + dist/wanming/ + BUILD_MANIFEST`
- **验收标准**：脚本实际通过且用户确认输出形式
- **硬门/状态**：NOT_CHECKED
- **依据/备注**：旧R068 `V13_FIXED_89_ROUNDS.md`；强制用户确认。必须保存 `runs/R068.md`，包括输入SHA、真实执行、全部检查、未过项、GitHub提交、远程回读。
- **失败处理**：不足则当前轮IN_PROGRESS/FAILED/BLOCKED，写`runs/R089_V2.md`，不把单条假PASS计入verified；GitHub CI只能验结构与溯源，内容需真实核验。

### R090 · 《铁血残明》Stage5编译与DIGEST
- 来源：原R069；完整原文合同仍可追溯，映射见V13_ROUND_REMAP_V2.tsv
- **必须操作**：按原版生成DIGEST、compile(single/pack/auto)、validate_skill_pack，报告生成目录及用户交付选择
- **必须产物**：`books/tiexuecanming/DIGEST.md + dist/tiexuecanming/ + BUILD_MANIFEST`
- **验收标准**：脚本实际通过且用户确认输出形式
- **硬门/状态**：NOT_CHECKED
- **依据/备注**：旧R069 `V13_FIXED_89_ROUNDS.md`；强制用户确认。必须保存 `runs/R069.md`，包括输入SHA、真实执行、全部检查、未过项、GitHub提交、远程回读。
- **失败处理**：不足则当前轮IN_PROGRESS/FAILED/BLOCKED，写`runs/R090_V2.md`，不把单条假PASS计入verified；GitHub CI只能验结构与溯源，内容需真实核验。

### R091 · 主题3—5独立学派/代表选择与来源边界
- 来源：原R070；完整原文合同仍可追溯，映射见V13_ROUND_REMAP_V2.tsv
- **必须操作**：沿R004用户确认的Nuwa主题路径，选择3—5个各有真实来源的观点流派/学者；若R004实际选人物路径，不得静默沿用主题计划，需在原编号暂停修订
- **必须产物**：`nuwa/references/research/00-school-map.md`
- **验收标准**：至少3个彼此独立真实可核观点；资料边界符合用户授权
- **硬门/状态**：NOT_CHECKED
- **依据/备注**：旧R070 `V13_FIXED_89_ROUNDS.md`；范围核验。必须保存 `runs/R070.md`，包括输入SHA、真实执行、全部检查、未过项、GitHub提交、远程回读。
- **失败处理**：不足则当前轮IN_PROGRESS/FAILED/BLOCKED，写`runs/R091_V2.md`，不把单条假PASS计入verified；GitHub CI只能验结构与溯源，内容需真实核验。

### R092 · 主题路径第1个独立观点来源研究
- 来源：原R071；完整原文合同仍可追溯，映射见V13_ROUND_REMAP_V2.tsv
- **必须操作**：完整遵守Nuwa Phase1主题变体：针对已选第1独立流派用1—2隔离调研任务收集原始观点、论据、反对意见及时间变化；若实际只确认3—4个来源，剩余轮次标有理据的NOT_APPLICABLE而非伪造
- **必须产物**：`nuwa/references/research/school_01.md`
- **验收标准**：来源可核、没有将同作者两本书冒充两个派别；N/A不影响至少3个真实流派
- **硬门/状态**：NOT_CHECKED
- **依据/备注**：旧R071 `V13_FIXED_89_ROUNDS.md`；自动核验。必须保存 `runs/R071.md`，包括输入SHA、真实执行、全部检查、未过项、GitHub提交、远程回读。
- **失败处理**：不足则当前轮IN_PROGRESS/FAILED/BLOCKED，写`runs/R092_V2.md`，不把单条假PASS计入verified；GitHub CI只能验结构与溯源，内容需真实核验。

### R093 · 主题路径第2个独立观点来源研究
- 来源：原R072；完整原文合同仍可追溯，映射见V13_ROUND_REMAP_V2.tsv
- **必须操作**：完整遵守Nuwa Phase1主题变体：针对已选第2独立流派用1—2隔离调研任务收集原始观点、论据、反对意见及时间变化；若实际只确认3—4个来源，剩余轮次标有理据的NOT_APPLICABLE而非伪造
- **必须产物**：`nuwa/references/research/school_02.md`
- **验收标准**：来源可核、没有将同作者两本书冒充两个派别；N/A不影响至少3个真实流派
- **硬门/状态**：NOT_CHECKED
- **依据/备注**：旧R072 `V13_FIXED_89_ROUNDS.md`；自动核验。必须保存 `runs/R072.md`，包括输入SHA、真实执行、全部检查、未过项、GitHub提交、远程回读。
- **失败处理**：不足则当前轮IN_PROGRESS/FAILED/BLOCKED，写`runs/R093_V2.md`，不把单条假PASS计入verified；GitHub CI只能验结构与溯源，内容需真实核验。

### R094 · 主题路径第3个独立观点来源研究
- 来源：原R073；完整原文合同仍可追溯，映射见V13_ROUND_REMAP_V2.tsv
- **必须操作**：完整遵守Nuwa Phase1主题变体：针对已选第3独立流派用1—2隔离调研任务收集原始观点、论据、反对意见及时间变化；若实际只确认3—4个来源，剩余轮次标有理据的NOT_APPLICABLE而非伪造
- **必须产物**：`nuwa/references/research/school_03.md`
- **验收标准**：来源可核、没有将同作者两本书冒充两个派别；N/A不影响至少3个真实流派
- **硬门/状态**：NOT_CHECKED
- **依据/备注**：旧R073 `V13_FIXED_89_ROUNDS.md`；自动核验。必须保存 `runs/R073.md`，包括输入SHA、真实执行、全部检查、未过项、GitHub提交、远程回读。
- **失败处理**：不足则当前轮IN_PROGRESS/FAILED/BLOCKED，写`runs/R094_V2.md`，不把单条假PASS计入verified；GitHub CI只能验结构与溯源，内容需真实核验。

### R095 · 主题路径第4个独立观点来源研究
- 来源：原R074；完整原文合同仍可追溯，映射见V13_ROUND_REMAP_V2.tsv
- **必须操作**：完整遵守Nuwa Phase1主题变体：针对已选第4独立流派用1—2隔离调研任务收集原始观点、论据、反对意见及时间变化；若实际只确认3—4个来源，剩余轮次标有理据的NOT_APPLICABLE而非伪造
- **必须产物**：`nuwa/references/research/school_04.md`
- **验收标准**：来源可核、没有将同作者两本书冒充两个派别；N/A不影响至少3个真实流派
- **硬门/状态**：NOT_CHECKED
- **依据/备注**：旧R074 `V13_FIXED_89_ROUNDS.md`；自动核验。必须保存 `runs/R074.md`，包括输入SHA、真实执行、全部检查、未过项、GitHub提交、远程回读。
- **失败处理**：不足则当前轮IN_PROGRESS/FAILED/BLOCKED，写`runs/R095_V2.md`，不把单条假PASS计入verified；GitHub CI只能验结构与溯源，内容需真实核验。

### R096 · 主题路径第5个独立观点来源研究
- 来源：原R075；完整原文合同仍可追溯，映射见V13_ROUND_REMAP_V2.tsv
- **必须操作**：完整遵守Nuwa Phase1主题变体：针对已选第5独立流派用1—2隔离调研任务收集原始观点、论据、反对意见及时间变化；若实际只确认3—4个来源，剩余轮次标有理据的NOT_APPLICABLE而非伪造
- **必须产物**：`nuwa/references/research/school_05.md`
- **验收标准**：来源可核、没有将同作者两本书冒充两个派别；N/A不影响至少3个真实流派
- **硬门/状态**：NOT_CHECKED
- **依据/备注**：旧R075 `V13_FIXED_89_ROUNDS.md`；自动核验。必须保存 `runs/R075.md`，包括输入SHA、真实执行、全部检查、未过项、GitHub提交、远程回读。
- **失败处理**：不足则当前轮IN_PROGRESS/FAILED/BLOCKED，写`runs/R096_V2.md`，不把单条假PASS计入verified；GitHub CI只能验结构与溯源，内容需真实核验。

### R097 · Nuwa Phase1维度汇总与冲突账
- 来源：原R076；完整原文合同仍可追溯，映射见V13_ROUND_REMAP_V2.tsv
- **必须操作**：按主题路径可获得的著作/论述/表达/评价/决策/时间线各维汇总；如资料缺失标缺，不编造访谈
- **必须产物**：`nuwa/references/research/RESEARCH_SUMMARY.md + contradictions.md`
- **验收标准**：核来源数量、一手比例、冲突与缺口
- **硬门/状态**：NOT_CHECKED
- **依据/备注**：旧R076 `V13_FIXED_89_ROUNDS.md`；自动核验。必须保存 `runs/R076.md`，包括输入SHA、真实执行、全部检查、未过项、GitHub提交、远程回读。
- **失败处理**：不足则当前轮IN_PROGRESS/FAILED/BLOCKED，写`runs/R097_V2.md`，不把单条假PASS计入verified；GitHub CI只能验结构与溯源，内容需真实核验。

### R098 · Phase1.5调研质量审查与用户关口
- 来源：原R077；完整原文合同仍可追溯，映射见V13_ROUND_REMAP_V2.tsv
- **必须操作**：展示调研强弱、矛盾和缺口，并让用户决定可否进入提炼
- **必须产物**：`nuwa/gates/PHASE15_REVIEW.md`
- **验收标准**：资料达到实际适用门且用户明确审查通过
- **硬门/状态**：MANDATORY_USER_CONFIRM
- **依据/备注**：旧R077 `V13_FIXED_89_ROUNDS.md`；强制用户确认。必须保存 `runs/R077.md`，包括输入SHA、真实执行、全部检查、未过项、GitHub提交、远程回读。
- **失败处理**：不足则当前轮IN_PROGRESS/FAILED/BLOCKED，写`runs/R098_V2.md`，不把单条假PASS计入verified；GitHub CI只能验结构与溯源，内容需真实核验。

### R099 · Phase2心智模型独立提炼
- 来源：原R078；完整原文合同仍可追溯，映射见V13_ROUND_REMAP_V2.tsv
- **必须操作**：依原版extraction-framework作跨域复现、生成力和排他性验证；保留共识与分歧
- **必须产物**：`nuwa/synthesis/MENTAL_MODELS.md`
- **验收标准**：3—7个证据充足模型，含条件反例
- **硬门/状态**：NOT_CHECKED
- **依据/备注**：旧R078 `V13_FIXED_89_ROUNDS.md`；自动核验。必须保存 `runs/R078.md`，包括输入SHA、真实执行、全部检查、未过项、GitHub提交、远程回读。
- **失败处理**：不足则当前轮IN_PROGRESS/FAILED/BLOCKED，写`runs/R099_V2.md`，不把单条假PASS计入verified；GitHub CI只能验结构与溯源，内容需真实核验。

### R100 · Phase2启发式、表达DNA与诚实边界
- 来源：原R079；完整原文合同仍可追溯，映射见V13_ROUND_REMAP_V2.tsv
- **必须操作**：提炼5—10 if/then启发式、专业中性写作DNA、内在张力、反模式与知识来源边界
- **必须产物**：`nuwa/synthesis/HEURISTICS_DNA_BOUNDARIES.md`
- **验收标准**：不模仿原作者专属措辞，所有条目可回查
- **硬门/状态**：NOT_CHECKED
- **依据/备注**：旧R079 `V13_FIXED_89_ROUNDS.md`；自动核验。必须保存 `runs/R079.md`，包括输入SHA、真实执行、全部检查、未过项、GitHub提交、远程回读。
- **失败处理**：不足则当前轮IN_PROGRESS/FAILED/BLOCKED，写`runs/R100_V2.md`，不把单条假PASS计入verified；GitHub CI只能验结构与溯源，内容需真实核验。

### R101 · Phase2.5模型与DNA用户确认
- 来源：原R080；完整原文合同仍可追溯，映射见V13_ROUND_REMAP_V2.tsv
- **必须操作**：展示模型、反例、启发式、表达及局限，允许用户指出错误
- **必须产物**：`nuwa/gates/PHASE25_REVIEW.md`
- **验收标准**：用户明确同意具体成果
- **硬门/状态**：MANDATORY_USER_CONFIRM
- **依据/备注**：旧R080 `V13_FIXED_89_ROUNDS.md`；强制用户确认。必须保存 `runs/R080.md`，包括输入SHA、真实执行、全部检查、未过项、GitHub提交、远程回读。
- **失败处理**：不足则当前轮IN_PROGRESS/FAILED/BLOCKED，写`runs/R101_V2.md`，不把单条假PASS计入verified；GitHub CI只能验结构与溯源，内容需真实核验。

### R102 · Phase3主题SKILL与Agentic Protocol
- 来源：原R081；完整原文合同仍可追溯，映射见V13_ROUND_REMAP_V2.tsv
- **必须操作**：按原版skill-template建立自包含Skill，路由问题→证据研究→模型选择→输出；主题不是扮演作者
- **必须产物**：`nuwa/skill/SKILL.md + references + sources`
- **验收标准**：触发及边界明确、全部依赖可恢复
- **硬门/状态**：NOT_CHECKED
- **依据/备注**：旧R081 `V13_FIXED_89_ROUNDS.md`；自动核验。必须保存 `runs/R081.md`，包括输入SHA、真实执行、全部检查、未过项、GitHub提交、远程回读。
- **失败处理**：不足则当前轮IN_PROGRESS/FAILED/BLOCKED，写`runs/R102_V2.md`，不把单条假PASS计入verified；GitHub CI只能验结构与溯源，内容需真实核验。

### R103 · Phase4独立已知/边缘/表达实测
- 来源：原R082；完整原文合同仍可追溯，映射见V13_ROUND_REMAP_V2.tsv
- **必须操作**：独立上下文做3个已知案例、1个边缘案例及短表达测试，保存真实输入输出
- **必须产物**：`nuwa/tests/SANITY_EDGE_VOICE_RESULTS.md`
- **验收标准**：测试主体与提炼隔离、案例确实执行
- **硬门/状态**：NOT_CHECKED
- **依据/备注**：旧R082 `V13_FIXED_89_ROUNDS.md`；自动核验。必须保存 `runs/R082.md`，包括输入SHA、真实执行、全部检查、未过项、GitHub提交、远程回读。
- **失败处理**：不足则当前轮IN_PROGRESS/FAILED/BLOCKED，写`runs/R103_V2.md`，不把单条假PASS计入verified；GitHub CI只能验结构与溯源，内容需真实核验。

### R104 · Phase4质量脚本、迭代上限和用户关口
- 来源：原R083；完整原文合同仍可追溯，映射见V13_ROUND_REMAP_V2.tsv
- **必须操作**：运行原版6项硬门和测试脚本，一手来源>50%等源标准据实检验；失败最多两次回炉并披露
- **必须产物**：`nuwa/FIDELITY.md + nuwa/tests/QUALITY_CHECK.md + gates/PHASE4.md`
- **验收标准**：用户明确确认已达门；没有虚报独立通过
- **硬门/状态**：MANDATORY_USER_CONFIRM
- **依据/备注**：旧R083 `V13_FIXED_89_ROUNDS.md`；强制用户确认。必须保存 `runs/R083.md`，包括输入SHA、真实执行、全部检查、未过项、GitHub提交、远程回读。
- **失败处理**：不足则当前轮IN_PROGRESS/FAILED/BLOCKED，写`runs/R104_V2.md`，不把单条假PASS计入verified；GitHub CI只能验结构与溯源，内容需真实核验。

### R105 · Phase5独立优化主体A
- 来源：原R084；完整原文合同仍可追溯，映射见V13_ROUND_REMAP_V2.tsv
- **必须操作**：按原版Agent A从8个结构维度和3项干跑检测弱点，提出有diff的修改
- **必须产物**：`nuwa/optimization/AGENT_A.md`
- **验收标准**：真实独立主体或明确说明独立性限制
- **硬门/状态**：NOT_CHECKED
- **依据/备注**：旧R084 `V13_FIXED_89_ROUNDS.md`；自动核验。必须保存 `runs/R084.md`，包括输入SHA、真实执行、全部检查、未过项、GitHub提交、远程回读。
- **失败处理**：不足则当前轮IN_PROGRESS/FAILED/BLOCKED，写`runs/R105_V2.md`，不把单条假PASS计入verified；GitHub CI只能验结构与溯源，内容需真实核验。

### R106 · Phase5独立优化主体B
- 来源：原R085；完整原文合同仍可追溯，映射见V13_ROUND_REMAP_V2.tsv
- **必须操作**：按原版Agent B审触发/路由/防漂移/信息缺口，提出2—3可操作修改
- **必须产物**：`nuwa/optimization/AGENT_B.md`
- **验收标准**：不让同一假扮双独立审稿者
- **硬门/状态**：NOT_CHECKED
- **依据/备注**：旧R085 `V13_FIXED_89_ROUNDS.md`；自动核验。必须保存 `runs/R085.md`，包括输入SHA、真实执行、全部检查、未过项、GitHub提交、远程回读。
- **失败处理**：不足则当前轮IN_PROGRESS/FAILED/BLOCKED，写`runs/R106_V2.md`，不把单条假PASS计入verified；GitHub CI只能验结构与溯源，内容需真实核验。

### R107 · Phase5合并改动、回归与用户确认
- 来源：原R086；完整原文合同仍可追溯，映射见V13_ROUND_REMAP_V2.tsv
- **必须操作**：比对A/B冲突和改动，保留真实差异，复测并交用户决定
- **必须产物**：`nuwa/optimization/FINAL_DIFF.md + gates/PHASE5.md`
- **验收标准**：用户认可且正式测试复验
- **硬门/状态**：MANDATORY_USER_CONFIRM
- **依据/备注**：旧R086 `V13_FIXED_89_ROUNDS.md`；强制用户确认。必须保存 `runs/R086.md`，包括输入SHA、真实执行、全部检查、未过项、GitHub提交、远程回读。
- **失败处理**：不足则当前轮IN_PROGRESS/FAILED/BLOCKED，写`runs/R107_V2.md`，不把单条假PASS计入verified；GitHub CI只能验结构与溯源，内容需真实核验。

### R108 · 统一创作技能路由/契约
- 来源：原R087；完整原文合同仍可追溯，映射见V13_ROUND_REMAP_V2.tsv
- **必须操作**：保留仓颉可执行任务与女娲认知/表达的独立来源和优先级，建原创技能路由
- **必须产物**：`v13-creative/SKILL.md + FUSION_MAP.md`
- **验收标准**：不会把长Prompt或人物模仿包装成可检验SKILL
- **硬门/状态**：NOT_CHECKED
- **依据/备注**：旧R087 `V13_FIXED_89_ROUNDS.md`；自动核验。必须保存 `runs/R087.md`，包括输入SHA、真实执行、全部检查、未过项、GitHub提交、远程回读。
- **失败处理**：不足则当前轮IN_PROGRESS/FAILED/BLOCKED，写`runs/R108_V2.md`，不把单条假PASS计入verified；GitHub CI只能验结构与溯源，内容需真实核验。

### R109 · 四臂盲测与长篇连续性压力
- 来源：原R088；完整原文合同仍可追溯，映射见V13_ROUND_REMAP_V2.tsv
- **必须操作**：同原创输入评无Skill/仅仓颉/仅女娲/融合；盲评情节因果、人物行动、对白、叙事感、阅读留存和持续状态
- **必须产物**：`tests/FINAL_BLIND_TRIALS.md + CONTINUITY.md`
- **验收标准**：真实隔离输出和失败回归，不能凭自评发布
- **硬门/状态**：NOT_CHECKED
- **依据/备注**：旧R088 `V13_FIXED_89_ROUNDS.md`；自动核验。必须保存 `runs/R088.md`，包括输入SHA、真实执行、全部检查、未过项、GitHub提交、远程回读。
- **失败处理**：不足则当前轮IN_PROGRESS/FAILED/BLOCKED，写`runs/R109_V2.md`，不把单条假PASS计入verified；GitHub CI只能验结构与溯源，内容需真实核验。

### R110 · GitHub出厂、干净会话恢复与用户验收
- 来源：原R089；完整原文合同仍可追溯，映射见V13_ROUND_REMAP_V2.tsv
- **必须操作**：在新对话只依据V13仓库+授权原文恢复，执行正负触发和陌生续写，给版本证据与用户验收
- **必须产物**：`README_RELEASE.md + BUILD_MANIFEST + RESTORE_TEST_REPORT.md`
- **验收标准**：所有原版门通过、实际可调用、用户最后确认
- **硬门/状态**：MANDATORY_USER_CONFIRM
- **依据/备注**：旧R089 `V13_FIXED_89_ROUNDS.md`；强制用户确认。必须保存 `runs/R089.md`，包括输入SHA、真实执行、全部检查、未过项、GitHub提交、远程回读。
- **失败处理**：不足则当前轮IN_PROGRESS/FAILED/BLOCKED，写`runs/R110_V2.md`，不把单条假PASS计入verified；GitHub CI只能验结构与溯源，内容需真实核验。


## 迁移及旧新状态严禁混淆

`CURRENT_ROUND.json`、`ROUND_LEDGER.csv`、`V13_FIXED_89_ROUNDS.md`保存原v13.0历史快照；其中仍可见旧R057 BLOCKED、56/89——这是**版本v13.0截面**，不是v13.1当前游标。恢复时只读**唯一v13.1权威游标`V13_CURRENT_V2.json`**及`V13_LEDGER_V2.csv`；之后再查历史以追溯来源，不得依据旧快照启动或恢复。历史R057交付物存在但由于新增研究要求，其最终分流必须在新版R078再次核对；用户此前批准审计方案A并不能替代新版R078时对新增证据的确认。实际新R057尚未启动，56/110。

所有旧R058—R089未完成工作的功能、必备产物和原版硬门**整体保留，仅编号+21**。旧R004/R042等历史用户确认有效，不因新表自动清零。新项目完结必须R110通过真实安装/恢复测试及用户确认。
