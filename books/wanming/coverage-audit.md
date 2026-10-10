# R078 UPDATE: 9/9 R057 tasks candidate-linked, 0/9 verified

B075 raw 47+22 diagnostic outputs yield at least one tested candidate associated with each of WM-01..09. This means possible source association only, not full Task acceptance, actual independent C or V3 net benefit. Full 9-row linked candidate list: `v2/v3/B075_STAGE0_19_COVERAGE_AUDIT.tsv`. Old Adler original T01..T10 are ten different contracts: see `gates/R078_STAGE0_ORIGINAL20_TO_R057_19_CROSSWALK.tsv`; the WM-T05 and WM-T09 exact tasks remain partially unmatched to revised R057 9 Task definitions. Do not merge silently. Method decisions: `books/wanming/R078_V2_DECISION_MATRIX.tsv`. Reference 42 sources are at references.md; Stage3 copies are planned, not delivered. Independent C=NOT_RUN, verified=0, no skill compilation.

---

# 《晚明》Stage1.5 coverage-audit（R057）

raw_task_coverage: 9/9
verified_task_coverage: 0/9

|任务|原始候选|待核|参考|verified|R056差值|
|---|---:|---:|---:|---:|---:|
|WM-01 从失去身份到获得他人有条件认可，写新人物入局|11|4|7|0|0|
|WM-02 让两位长期合作者的道德分歧产生真实后果|15|5|10|0|0|
|WM-03 区分纸面军职与组织实际运营条件|38|21|17|0|0|
|WM-04 设计商业收益转供给的延时和竞争|25|15|10|0|-1|
|WM-05 写敌我不共享情报的选择与误判|16|9|7|0|0|
|WM-06 大胜后重新分配功劳和社会成本|18|10|8|0|0|
|WM-07 组织治理改革必须经过质疑、试验、复核|24|16|8|0|0|
|WM-08 跨卷维护普通人和家庭的个人弧线|17|8|9|0|0|
|WM-09 把后世讲述与曾经发生过的事实比较|11|5|6|0|-1|

## 每项Stage0任务的完整任务—来源—去向记录

### WM-01 从失去身份到获得他人有条件认可，写新人物入局
- 原书：`n001/p44、n022/p1、n052/p28`；期望交付：三场不同见证人场面＋合法性变更表；重要性：无入口则穿越优势失真。
- RAW：`WM-f01, WM-f06, WM-p03, WM-p08, WM-c01, WM-c03, WM-ce01, WM-ce03, WM-g01, WM-g02, WM-g03`；待核：`WM-f01, WM-f06, WM-p03, WM-p08`；参考：`WM-c01, WM-c03, WM-ce01, WM-ce03, WM-g01, WM-g02, WM-g03`。
- 所有候选准确原始章节n/p见`R057_DECISION_MATRIX.tsv`；R055输出`tests/v2/results/WM-01.json`；R056同题候选-对照差值0；verified=0。
- 未决：陌生人物与年代、独立试写；同Agent非盲且多方法共用输入，无法由本次结果给单方法V3合格结论。

### WM-02 让两位长期合作者的道德分歧产生真实后果
- 原书：`n034/p18、n064/p55、n468/p44`；期望交付：双视角冲突＋关系债务；重要性：防止配角成为主人公的喇叭。
- RAW：`WM-f02, WM-f12, WM-p01, WM-p02, WM-c02, WM-c12, WM-ce02, WM-ce07, WM-ce17, WM-ce19, WM-g02, WM-g09, WM-g11, WM-g13, WM-g17`；待核：`WM-f02, WM-f12, WM-p01, WM-p02, WM-ce17`；参考：`WM-c02, WM-c12, WM-ce02, WM-ce07, WM-ce19, WM-g02, WM-g09, WM-g11, WM-g13, WM-g17`。
- 所有候选准确原始章节n/p见`R057_DECISION_MATRIX.tsv`；R055输出`tests/v2/results/WM-02.json`；R056同题候选-对照差值0；verified=0。
- 未决：原创新人物选择题；同Agent非盲且多方法共用输入，无法由本次结果给单方法V3合格结论。

### WM-03 区分纸面军职与组织实际运营条件
- 原书：`n052/p28、n070/p36、n494/p17`；期望交付：权限/人力/资金/承诺四账与现场；重要性：扩军缺少代价会断长篇因果。
- RAW：`WM-f01, WM-f03, WM-f04, WM-f05, WM-f06, WM-f09, WM-f11, WM-f15, WM-p05, WM-p08, WM-p09, WM-p10, WM-p12, WM-p13, WM-p15, WM-p17, WM-c03, WM-c06, WM-c08, WM-c10, WM-c11, WM-ce03, WM-ce04, WM-ce08, WM-ce09, WM-ce10, WM-ce13, WM-ce14, WM-ce15, WM-ce18, WM-g01, WM-g04, WM-g05, WM-g06, WM-g07, WM-g08, WM-g12, WM-g16`；待核：`WM-f01, WM-f03, WM-f04, WM-f05, WM-f06, WM-f09, WM-f11, WM-f15, WM-p05, WM-p08, WM-p09, WM-p10, WM-p12, WM-p13, WM-p15, WM-p17, WM-c11, WM-ce08, WM-ce13, WM-ce15, WM-ce18`；参考：`WM-c03, WM-c06, WM-c08, WM-c10, WM-ce03, WM-ce04, WM-ce09, WM-ce10, WM-ce14, WM-g01, WM-g04, WM-g05, WM-g06, WM-g07, WM-g08, WM-g12, WM-g16`。
- 所有候选准确原始章节n/p见`R057_DECISION_MATRIX.tsv`；R055输出`tests/v2/results/WM-03.json`；R056同题候选-对照差值0；verified=0。
- 未决：历史外证和安全审查；同Agent非盲且多方法共用输入，无法由本次结果给单方法V3合格结论。

### WM-04 设计商业收益转供给的延时和竞争
- 原书：`n099/p18、n297/p1、n345/p29`；期望交付：跨章虚构资源时序＋两名商人选择；重要性：供应与现金不能瞬间到账。
- RAW：`WM-f04, WM-f09, WM-f16, WM-f17, WM-p01, WM-p02, WM-p05, WM-p12, WM-p18, WM-p22, WM-c01, WM-c02, WM-c05, WM-c08, WM-c11, WM-ce01, WM-ce06, WM-ce10, WM-ce12, WM-ce14, WM-ce18, WM-g09, WM-g10, WM-g12, WM-g16`；待核：`WM-f04, WM-f09, WM-f16, WM-f17, WM-p01, WM-p02, WM-p05, WM-p12, WM-p18, WM-p22, WM-c05, WM-c11, WM-ce06, WM-ce12, WM-ce18`；参考：`WM-c01, WM-c02, WM-c08, WM-ce01, WM-ce10, WM-ce14, WM-g09, WM-g10, WM-g12, WM-g16`。
- 所有候选准确原始章节n/p见`R057_DECISION_MATRIX.tsv`；R055输出`tests/v2/results/WM-04.json`；R056同题候选-对照差值-1；verified=0。
- 未决：全新交易背景，非现实营销/欺诈；同Agent非盲且多方法共用输入，无法由本次结果给单方法V3合格结论。

### WM-05 写敌我不共享情报的选择与误判
- 原书：`n106/p1、n140/p36、n556/p3`；期望交付：两地有限视角场景＋消息差清单；重要性：防止全知指挥视角。
- RAW：`WM-f07, WM-f08, WM-f15, WM-p06, WM-p07, WM-p15, WM-p19, WM-c05, WM-c06, WM-ce04, WM-ce06, WM-ce07, WM-ce16, WM-g04, WM-g15, WM-g18`；待核：`WM-f07, WM-f08, WM-f15, WM-p06, WM-p07, WM-p15, WM-p19, WM-c05, WM-ce06`；参考：`WM-c06, WM-ce04, WM-ce07, WM-ce16, WM-g04, WM-g15, WM-g18`。
- 所有候选准确原始章节n/p见`R057_DECISION_MATRIX.tsv`；R055输出`tests/v2/results/WM-05.json`；R056同题候选-对照差值0；verified=0。
- 未决：匿名原创事件，禁止实战战术；同Agent非盲且多方法共用输入，无法由本次结果给单方法V3合格结论。

### WM-06 大胜后重新分配功劳和社会成本
- 原书：`n085/p25、n155/p52、n425/p27`；期望交付：战后四方结果网＋未结事项；重要性：高潮之后仍有社会真实。
- RAW：`WM-f03, WM-f04, WM-f08, WM-f10, WM-f14, WM-f17, WM-p04, WM-p09, WM-p22, WM-c04, WM-c07, WM-c09, WM-c13, WM-ce05, WM-ce08, WM-ce11, WM-g05, WM-g06`；待核：`WM-f03, WM-f04, WM-f08, WM-f10, WM-f14, WM-f17, WM-p04, WM-p09, WM-p22, WM-ce08`；参考：`WM-c04, WM-c07, WM-c09, WM-c13, WM-ce05, WM-ce11, WM-g05, WM-g06`。
- 所有候选准确原始章节n/p见`R057_DECISION_MATRIX.tsv`；R055输出`tests/v2/results/WM-06.json`；R056同题候选-对照差值0；verified=0。
- 未决：独立盲评后果连续性；同Agent非盲且多方法共用输入，无法由本次结果给单方法V3合格结论。

### WM-07 组织治理改革必须经过质疑、试验、复核
- 原书：`n425/p27、n519/p70、n520/p17`；期望交付：一场制度争辩＋试点验收表；重要性：防止宣言即公正。
- RAW：`WM-f02, WM-f05, WM-f11, WM-f12, WM-f16, WM-p10, WM-p11, WM-p13, WM-p16, WM-p17, WM-p18, WM-p20, WM-p21, WM-c07, WM-c10, WM-c12, WM-ce09, WM-ce12, WM-ce13, WM-ce17, WM-g08, WM-g11, WM-g13, WM-g14`；待核：`WM-f02, WM-f05, WM-f11, WM-f12, WM-f16, WM-p10, WM-p11, WM-p13, WM-p16, WM-p17, WM-p18, WM-p20, WM-p21, WM-ce12, WM-ce13, WM-ce17`；参考：`WM-c07, WM-c10, WM-c12, WM-ce09, WM-g08, WM-g11, WM-g13, WM-g14`。
- 所有候选准确原始章节n/p见`R057_DECISION_MATRIX.tsv`；R055输出`tests/v2/results/WM-07.json`；R056同题候选-对照差值0；verified=0。
- 未决：真实制度条文须外证；同Agent非盲且多方法共用输入，无法由本次结果给单方法V3合格结论。

### WM-08 跨卷维护普通人和家庭的个人弧线
- 原书：`n540/p33、n568/p44、n569/p21`；期望交付：人物认知/关系/个人意愿连续账；重要性：大战不能消灭私人生活。
- RAW：`WM-f10, WM-f14, WM-f17, WM-p03, WM-p06, WM-p14, WM-p20, WM-c03, WM-c09, WM-c13, WM-ce02, WM-ce11, WM-ce15, WM-g03, WM-g07, WM-g11, WM-g12`；待核：`WM-f10, WM-f14, WM-f17, WM-p03, WM-p06, WM-p14, WM-p20, WM-ce15`；参考：`WM-c03, WM-c09, WM-c13, WM-ce02, WM-ce11, WM-g03, WM-g07, WM-g11, WM-g12`。
- 所有候选准确原始章节n/p见`R057_DECISION_MATRIX.tsv`；R055输出`tests/v2/results/WM-08.json`；R056同题候选-对照差值0；verified=0。
- 未决：全新人物独立选择；同Agent非盲且多方法共用输入，无法由本次结果给单方法V3合格结论。

### WM-09 把后世讲述与曾经发生过的事实比较
- 原书：`n166/p30、n571/p5`；期望交付：事件／见闻／谣说／评书四层对照；重要性：结尾余韵而不推翻已演事实。
- RAW：`WM-f07, WM-f13, WM-p07, WM-p19, WM-p23, WM-c14, WM-ce16, WM-ce19, WM-g15, WM-g17, WM-g18`；待核：`WM-f07, WM-f13, WM-p07, WM-p19, WM-p23`；参考：`WM-c14, WM-ce16, WM-ce19, WM-g15, WM-g17, WM-g18`。
- 所有候选准确原始章节n/p见`R057_DECISION_MATRIX.tsv`；R055输出`tests/v2/results/WM-09.json`；R056同题候选-对照差值-1；verified=0。
- 未决：陌生叙事基线及版权相似性否决；同Agent非盲且多方法共用输入，无法由本次结果给单方法V3合格结论。

## 缺口审计

全部Stage0任务有原始候选，不存在无主RAW任务；但所有任务verified=0。短篇纸面场景无法验证跨卷连续性、史实外证、完整军事财政后果与独立文学审稿。R007—R024历史模板化质量债和14条隔离记录不因任务映射而关闭。参考现阶段真正保存在references.md，后续Stage3仅为计划。

