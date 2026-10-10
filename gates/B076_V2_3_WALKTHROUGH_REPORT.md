# B076｜3项限域V1方法的全新V2演练实测报告
date: 2026-10-10
V2_prereg_git_commit: 84f5988e14a5c5b950e27c5d81c6422b280c62c0
V2_prereg_git_blob: 0356af5c12a7987930a62c9562c24d3a3e9892e8
V2_prereg_path: gates/B076_V2_3_FRESH_TASK_PREREG.json
exact_V2_task_ids: B076-V2-WM-f15 / B076-V2-WM-p09 / B076-V2-WM-p17
V2_actual_output_count: 3
V2_diagnostic_walkthrough_pass: 3
V2_independent_blind_pass: 0
independent_V3: 0
Cangjie_verified: 0
Stage0_original20_independent_C: 0
batch: B076 BLOCKED
B077: NOT_STARTED

## 时序
冻结测试合同的提交 `84f5988e14a5c5b950e27c5d81c6422b280c62c0` 经GitHub main回读与76/76 Actions通过，写作原件不在冻结提交内。本报告所在**后续**提交才包含3份全文原创输出。各题输入、未来未知事实、故事交付形式和硬失败例均来自已经冻结的`gates/B076_V2_3_FRESH_TASK_PREREG.json`。没有取用原书人物情节、原著特殊语言或密封题。

## 三条逐项鉴别

### WM-f15 — V2_WALKTHROUGH_PASS_LIMITED
独立新题：1640虚构临河镇十册账本的旧单A/修订B冲突。出示旧知A的陆霁和先知B的赵平、许穗各自能说出的内容，包含有证实的当面对话更正、改变动作，以及十册最终迁存**未知**的状态账。故意错误例无依据让陆霁提前知B且宣布全数已完成；明确拒绝。输出`tests/b076_v2_3_outputs/WM-f15.md`。

### WM-p09 — V2_WALKTHROUGH_PASS_LIMITED
独立新题：1641虚构义学租银月支12已付、下月拟少4未获准；库银5、纸墨应付8、差额3。场面中先有把预期省费当钱的实际冲突，再由账目和人物回应更正；最终欠款和房东许可仍未决。拒绝把4预测加进当前银袋结清账款的负例。输出`tests/b076_v2_3_outputs/WM-p09.md`。

### WM-p17 — V2_WALKTHROUGH_PASS_LIMITED
独立新题：1642虚构公共书屋的事务、捐款、人员、借入木架四议题。场面安排阿洛本人口头拒绝每日守门，另两人的资金与资产主张均有边界；捐款5未交，现金0；木架仅借用。明确拒绝一位权威者口头宣布四项全部解决的负例。输出`tests/b076_v2_3_outputs/WM-p17.md`。

## 验收含义与不许偷换的边界
这是**同一Agent按新输入完成原创新题实际文本的V2 walkthrough**，其场景、账表和拒绝例都可供检查，确定性CI只核标题/字数/关键事实是否存在，文学场面及内部因果由同一作者初审，不可声称独立盲评。原版Cangjie的V2 walkthrough与Stage4真实宿主测试不同。3个限定V1方法在新题下可按流程生成输出，暂记`WALKTHROUGH_PASS_LIMITED`，不是专业独立效用验证、V3达标、综合verified或独立SKILL晋级。

原69项V3独立双臂盲评仍0，Stage0原20合同真正独立验收0。原R042隔离14、文学B欠审192、旧WM-04/WM-09负结果不冲销。四类仍verified=0/reference=108/needs_review=79/rejected=0。不得进入B077或编译。