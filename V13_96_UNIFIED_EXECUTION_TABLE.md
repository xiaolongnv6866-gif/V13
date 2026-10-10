# V13｜统一96轮执行总表（不增加任何轮次）
date: 2026-10-11
status: SCHEDULE_RECONCILED_ONLY_NO_QUALITY_PROMOTION
base_main_sha: 747c3e92349111a5707eb0d74f224469ac347add
authoritative_plan: V13_V3_BATCH_PLAN.md
authoritative_original_contracts: V13_REVISED_110_ROUNDS.md (git blob 55256653a7f9359339a5f7a8924e4210ee25203a)
existing_management_rounds: 66 historical R001-R066 + existing B067-B096 (30) = **96**
new_batches_added: **0**
current_cursor: 75/96 B076 BLOCKED; B077-B096 20 NOT_STARTED
original_legacy_tasks: R067-R110 44/44 mapped with no deleted contract, 33 R078-R110 still outstanding
user_B076_decision: Plan A confirmed; no permission to pretend V3 independence
current_187_four_way: verified=0 / reference=108 / needs_review=79 / rejected=0
skill_certified: 0

## 统一分母与不准重复加总
- 冻结历史 **426个issue** = Stage0文学B 296 + R042隔离旧14 + V1初审39 + V2旧未测11 + 原V3 47 + R057任务19。逐ID同原冻结名与来源映射，`gates/V13_96_ISSUE_426_ROUTING.tsv` 每行归于**当前B076**而不自创子轮次。
- Stage0文学B **296=已受限复核104＋尚未逐项复核192**。104不代表B真正认证；192要逐行回查真实小说场景、叙事机制、另一叙法会损失什么、反证，不能拿SHA冒充解读完成。原R007的六项旧`nundefined`需要验证重定位；R024弱锚点必须具体审查。
- **R042隔离14** 已有分书R060/R061旧证，但其旧ID全部不得直接放行；和296项存在研究来源重合，仍在冻结426内另列14个隔离问题，不是独立的14个187候选。
- **初始V1的39**：历史11已有限域来源支持，18经实际源核查转为参考，新增3个窄V1来源支持且仅同Agent V2有限演练，余7继续V1 REVIEW。此39是原426里39，不是又新增39；新旧候选总数仍187。
- **原V2旧11**历史限域演练可用作候选资格线索，必须逐ID查输出与硬反例；不能冒充独立V3。
- **原V3 47 + 额外22 = 69不同ID**，额外22属187内候选，不是追加到426或187里的全新方法。69已有138臂非盲输出（50持平、19同Agent自评+1），实际独立创作者隔离、双匿名评审及新题复制仍**0/69**；队列 `gates/V13_96_V3_69_ROUTING.tsv`。
- **Stage0原20完整任务**是WM-T01..10与TX-T01..10；R057新版19任务只是候选关联、不是20/20完整C验收。WM-T05三级命令知识、WM-T09跨卷seen/heard/confirmed/unknown以及每项原产物不能挤掉；20项独立C均NOT_RUN，原合同清单 `gates/V13_96_ORIGINAL_STAGE0_20_ROUTING.tsv`。
- WM-04、WM-09两个原R056负样本、14个隔离、版权和历史事实来源界限、Stage4/5真实宿主验证、Nuwa真实独立主体与最终四臂盲测的义务保留。以上队列**互相有交叉，不能简单加成“问题个数”**。

## B076当前必须并行整理的同源事项（只是工作组，不是轮次）
|B076内工作组|尚欠事项|与其他工作的并行合并|退出条件|
|---|---|---|---|
|STAGE0_SOURCE_B_QUALITY|192未核文学B；104限域旧结果留边界|与隔离14、V1待核7共享EPUB场景阅读|逐条真实A/B证据、反例、场景变化的文学生成价值或明确否定，不仅目录覆盖|
|LEGACY14_SOURCE_AND_ISOLATION|14个旧隔离不能直接复活|与Stage0同源章节按书与故事弧合读|旧ID各有决议，必要新候选重新过V1/V2/V3|
|CANGJIE_V1_REPAIR|7项真实尚缺因果/方法证据；3项限域勿扩大；18参考真实归档|和Stage0 B/隔离共享原文查核但每ID单独裁决|现有39 V1逐行来源边界与四分流准确|
|CANGJIE_V2_REAL_EXECUTION|旧11的限域结果核实、新3仅有限自测|可同批先冻结输入/接受指标后分题执行|真实可执行输出、反例、拒绝条件，不能把自评变成V3|
|CANGJIE_V3_TRUE_INDEPENDENCE|69/69缺真正隔离独立复制|仅在新冻题完成后允许真实分离主体并行测试各ID|真正独立A/B生成记录、>=2名盲评、预注册阈值和负例全留痕；缺主体则BLOCKED|
|STAGE0_ORIGINAL20_C_AND_R057_19|原20全任务C=0，新19只映射|与V2共享基础状态账模板，但不得把简短两幕当完整任务|20项逐条真实交付及独立验收、明确不等价的旧20→新19映射|
|R078最终来源与质量门|187分类0/108/79/0，认证0|完成前六组后统一核对两书矩阵/参考、负样本、任务覆盖和用户确认|用户A批准已记录；**verified=0必须停止B077/Stage1.6/编译**|

每次用户说“继续”，必须读取游标和本表，只能留在当前B076处理上述未完成工作；资料阅读、不同书问题可合并一次原子提交，**不得新增B076.1或任何额外轮次**。真实独立写作者/至少两位匿名盲评目前未证实，不能扮演多Agent。GitHub CI全部成功只说明结构一致。

## 固定30批次完整次序（含9个已完成、21个当前及后续批次）
|唯一批次与状态|原合同|同批合并完成的事项（原合同一项不减）|
|---|---|---|
|B067 PASSED|R067|HISTORICAL_NO_RESTART|
|B068 PASSED|R068;R069|HISTORICAL_NO_RESTART|
|B069 PASSED|R069;R070|HISTORICAL_NO_RESTART|
|B070 PASSED|R071;R072|HISTORICAL_NO_RESTART|
|B071 PASSED|R072;R073|HISTORICAL_NO_RESTART|
|B072 PASSED|R073;R074|HISTORICAL_NO_RESTART|
|B073 PASSED|R075|HISTORICAL_NO_RESTART|
|B074 PASSED|R076|HISTORICAL_NO_RESTART|
|B075 PASSED|R077|HISTORICAL_NO_RESTART|
|B076 BLOCKED|R078|Stage1.5 quality-gate evidence plus old reading debt and 69 independent V3/20 Stage0 full tasks|
|B077 NOT_STARTED|R079;R080;R081|Stage1.6 promotion then WM/TX RIA++ Bundle|
|B078 NOT_STARTED|R082;R083|Both books references, glossary and Zettelkasten|
|B079 NOT_STARTED|R084;R086|WM trigger-route then actual Stage4 output|
|B080 NOT_STARTED|R085;R087|TX trigger-route then actual Stage4 output|
|B081 NOT_STARTED|R088|Both books Stage4 failure repair/regression, retain WM04 and WM09 negatives|
|B082 NOT_STARTED|R089|WM Stage5 DIGEST, compile, validate|
|B083 NOT_STARTED|R090|TX Stage5 DIGEST, compile, validate|
|B084 NOT_STARTED|R091|Nuwa 3–5 independent viewpoint school source map|
|B085 NOT_STARTED|R092;R093;R094|Nuwa independent schools 1–3 jointly researched but separately sourced|
|B086 NOT_STARTED|R095;R096|Nuwa schools 4–5 or evidence-based N/A|
|B087 NOT_STARTED|R097;R098|Nuwa research synthesis and Phase1.5 user confirmation|
|B088 NOT_STARTED|R099;R100;R101|Nuwa mental models/heuristics/DNA and Phase2.5 user confirmation|
|B089 NOT_STARTED|R102|Nuwa Phase3 SKILL and Agentic Protocol|
|B090 NOT_STARTED|R103;R104|Nuwa Phase4 real independent tests, six checks, user confirmation|
|B091 NOT_STARTED|R105|Nuwa Phase5 real independent optimization Agent A|
|B092 NOT_STARTED|R106|Nuwa Phase5 separate independent optimization Agent B|
|B093 NOT_STARTED|R107|Nuwa A/B diff/regression and user confirmation|
|B094 NOT_STARTED|R108|Cangjie+Nuwa original SKILL fusion and provenance|
|B095 NOT_STARTED|R109|Four-arm genuine independent blind trials and long-novel continuity|
|B096 NOT_STARTED|R110|Clean-chat restore, install/trigger checks, release and user acceptance|

## 后续合同的准确边界
- B077先原R079 Stage1.6合法晋级，再同批两书R080/R081 RIA++ Bundle；B078两书术语、参考资料、Zettelkasten共同整合。**B076无verified绝不启动B077。**
- B079、B080分别是晚明/铁血Stage4触发→真实任务对照，可复用指标但不同书真实输出须保留；B081合并处理两书失败回归；B082与B083分别执行完整Stage5编译和安装验证，绝不能合成一个不做真实脚本的“交付”。
- B084—B086是真实Nuwa研究学派3—5来源：第1—3组可在B085同批共享采集方式、第4—5组在B086据源决定或合理N/A；B087研究质量+用户确认；B088认知模型/启发式/表达DNA+用户确认；B089生成主题Skill。
- B090 Nuwa Phase4独立测试、六项门及用户确认；B091/B092必须分别由真正互不假扮的独立优化主体A/B完成，B093才合并差异/回归并取得用户确认。
- B094统一Cangjie/Nuwa原创SKILL与来源优先级；B095按原R109进行真正四臂盲测及多章人物、时间、财政、信息连续性，复验WM-04/WM-09等负例；B096真实新对话恢复、部署测试、版本与最终用户批准。
- B087、B088、B090、B093、B096等原强制用户关口一项不减。现有Cangjie前置门、源证、V3独立和Nuwa Phase5也不能通过“行政归组”跳过。
- 历史R057的426行、旧R042用户批准的两份Overview、旧Cangjie/Nuwa固定SKILL、密封测试与旧V3冻结输出均只读；本执行表只新增**具体问题归属与验收索引**。

## 下一次“继续”的唯一工作入口
继续B076，先对未逐项复核的192条文学B，按冻结原始风险与书籍来源合并批量审查；关联的14个隔离和7个V1不足的**同一原著章节**一起核，但每条分别记录自己的A/B证据和拒绝理由。任何一组尚未闭合均不能说整轮完成；无真正独立评审时保留硬BLOCKED，而不为了前进B077削减要求。
