# V13.2｜唯一执行、节省GitHub操作与质量门规则

status: ACTIVE_V13_2_APPROVED_2026_10_10
plan: V13_V3_BATCH_PLAN.md
new_cursor: V13_CURRENT_V3.json
new_ledger: V13_LEDGER_V3.csv
legacy_crosswalk: V13_LEGACY_TO_BATCH_V3.tsv
v3_47_assignment: V13_V3_47_METHOD_ALLOCATION_V3.tsv
original_full_contract: V13_REVISED_110_ROUNDS.md (blob SHA1 55256653a7f9359339a5f7a8924e4210ee25203a)
historical_v13_1_snapshot: V13_CURRENT_V2.json + V13_LEDGER_V2.csv
historical_v13_0_snapshot: CURRENT_ROUND.json + ROUND_LEDGER.csv
pinned_cangjie: kangarooking/cangjie-skill@a28de55ba881b9928956a55048f743f7a9e3b23e
pinned_nuwa: alchaincyf/nuwa-skill@fe0374687037c4cc51a65c1e0c145afe2981dc69

## 一、恢复与启动

1. **首先**GitHub读取 START_HERE.md / V13_CURRENT_V3.json / V13_LEDGER_V3.csv / V13_V3_BATCH_PLAN.md / 本规则 / 44旧合同映射 / 原版110轮计划、所需上下游技能原文。确保HEAD、游标、账本、批次原合同及来源材料一致。旧游标显示R067仍NOT_STARTED仅是v13.1历史冻结，不得据此并行执行另一个计划。
2. 当前唯一B067—B096。用户每发送一次“继续”，**只执行一个B批次**；若已经IN_PROGRESS或BLOCKED，从GitHub实际资料与剩余项继续，不从头做、不越批。达到PASSED后停止，等待下一次“继续”。用户确认硬门不能假定已获批准。
3. 读取本批所含原R###合同的**全部**必须操作、必交产物、验收标准、失败处理，逐条照做。旧原R069、R072、R073被按候选分跨批：本批可在自己的候选子集全部通过后PASS，但旧R###要到后一个承接批次补齐所有ID及原始命名产物才算旧合同完成。各条方法不得被合并为单个分数。
4. 原文只用用户授权EPUB（SHA冻结），细读不等于章索引校验；A书源真实性、B文学解读、C原创新任务与独立效用不得混写。严禁上传版权全文/大量原文；不复刻原著人物、情节或作者标志性表达。

## 二、测试与SKILL硬门

- B067必须**先GitHub独立提交并远程回读**同题双臂冻结合同（47条原ID各有新输入、基线/方法、验收/反例/归因），再开始B068—B072中的任意输出。WM21按11+10；TX26按9+9+8。旧R056的201:203混搭实验仅负例，不是47条新V3的效用证明。
- 另将R065/R066有限V2纸面通过的22候选列为新增待评估队列（10 WM、12 TX），本地旧R075/76映射到B073/B074：先逐ID检查适用资格，再独立V3评估或记录未资格的确切理由。不得将其悄悄混入原47分母，也不得跳过可用方法。
- 匹配V3两臂须题干、字数、交付标准与评分相同，**只有单方法卡有差异**。原始输出、状态账、失败例、评价者身份及不同意意见逐个保存。同Agent生成和评分只准 `DIAGNOSTIC_ONLY_NONBLIND`，不授予真正独立增益/verified。
- B075合计审计原47/47真实证据、22新增去向和原19项Stage0任务覆盖。B076继承旧R078**强制用户确认**；verified为0时原版Cangjie禁止继续晋级/编译，必须停在B076 BLOCKED，不能为赶进度编造Skill。
- 另有五个强制用户关口B087/B088/B090/B093/B096，合计6个，完全对应旧R098/R101/R104/R107/R110；Stage5 B082/B083原合同是NOT_CHECKED，若交付方式需真实用户选择则询问，但不虚构原合同额外强制关口。
- Nuwa真实独立研究、Phase1.5/2.5、Phase4完整标准、Phase5两个**真实独立主体**、最终四臂盲测、干净会话真实恢复都保留。若工具环境无法实现独立性，应保留BLOCKED或诊断结论，不假扮分离代理。

## 三、减少重复但不削减测试

- 每批首个GitHub读取 HEAD和必须的当前文件，在同一批中对未变大文件沿用已验证SHA；只按需求回读其余变更，不因行政拆分重复遍历两本书。
- 单批允许合并多个有相同提交时序的**研究产物**到一次Git原子提交。预注册输入/评分规则 **必须先独立冻结提交**，输出提交须在后；批次所有成果+游标的正式封账要远程回读。
- GitHub Actions必须验证相关新产物与未破坏的既有回归门；**当前没有授权减少65项现有回归**，不能为了压缩CI调用而静默禁用关键测试。后续如经逐workflow影响评估证明确实可按路径减少冗余，再以独立验证提交优化触发器；发布前仍全套回归。
- 所有旧R合同必交路径继续保留，另按`runs/B###_V3.md`写批次完整收据（源Hash、上游技能SHA、旧任务覆盖和具体ID、原始输出、方法及对照、失败、原书范围、风险、提交和Actions、远程回读）。合并只影响“轮次管理”，不影响实证数量。
- 一批未完成=IN_PROGRESS/FAILED/BLOCKED；若触及用户硬门，先写待确认账并停下；不以汇总、脚本绿灯或自评代替文学判断。

## 四、版本与推进

V13.1已经完成R001—R066，历史状态66/110。v13.2用这66份已完成历史管理单位+30个后续批次=**96管理单位**，不表示原110任务中任何44项减少。V13_CURRENT_V3.json才是当前权威；V13_CURRENT_V2.json从迁移日起为冻结旧版本快照，保留旧字段供历史GitHub Actions核验。首次开始仅B067 NOT_STARTED。总共完成/剩余数字同时分别展示“行政单位”和“历史原任务覆盖”，不要假装30次就能自然完成47条V3。
