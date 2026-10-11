# V13｜交给另一聊天框的第一次独立复核任务（W01）
version: 2026-10-12-a
review_type: SOURCE_AND_METHOD_ELIGIBILITY_AUDIT
blind_literary_evaluation: NO
official_package_change: NONE
approval_or_certification_requested: NO

## 用途与边界

主执行Agent负责V13仓颉/女娲SKILL研究、编译和原创写作；另一**全新、不共享工作背景**的聊天框只负责此处的独立证据复核，结果回传后由主执行Agent执行修正。此任务**不是**正式V3双盲文学效果检验；单个新聊天不能自动充当“独立创作者+两名独立评委”。不要求付费外部API，不向外传任何私有EPUB。不要替主Agent写更多小说。

原版仓颉Stage1.5必须区分：V1原文充分性、V2合法新输入的可执行演练、V3给任务带来具体增益；通过后按 `verified/reference/needs_review/rejected` 四类处置。W01官方锁：69候选、56 READY、5 PARTIAL、8 INELIGIBLE；全部真实独立V3=0，不因复核报告改变。

## 必须实际核查的资料（GitHub只读）

1. 原仓颉 [Stage1.5全文](https://github.com/kangarooking/cangjie-skill/blob/a28de55ba881b9928956a55048f743f7a9e3b23e/methodology/03-stage1.5-triple-verify.md)，不能只凭总结理解；
2. [原69候选身份与任务来源](https://github.com/xiaolongnv6866-gif/V13/blob/main/V13_3_V3_69_TO_ROUNDS.tsv)；
3. [69项W01预审结论](https://github.com/xiaolongnv6866-gif/V13/blob/main/v13_w/w01/V3_69_ELIGIBILITY_PREFLIGHT.tsv)；
4. [13项阻断和缺口详情](https://github.com/xiaolongnv6866-gif/V13/blob/main/v13_w/w01/W01_13_EXCEPTIONS.tsv)；
5. [晚明原N19 V2结果32行](https://github.com/xiaolongnv6866-gif/V13/blob/main/v13_3/n19/N19_WM_V2_RESULTS_32.tsv)与[作品A—D目录](https://github.com/xiaolongnv6866-gif/V13/tree/main/v13_3/n19)及[来源质量审核](https://github.com/xiaolongnv6866-gif/V13/blob/main/v13_3/n19/N19_V2_SOURCE_AND_QUALITY_AUDIT.md)；
6. [铁血残明原N20 V2结果32行](https://github.com/xiaolongnv6866-gif/V13/blob/main/v13_3/n20/N20_TX_V2_RESULTS_32.tsv)与[作品A—D目录](https://github.com/xiaolongnv6866-gif/V13/tree/main/v13_3/n20)及[来源质量审核](https://github.com/xiaolongnv6866-gif/V13/blob/main/v13_3/n20/N20_V2_SOURCE_AND_QUALITY_AUDIT.md)；
7. [W01拟定V3协议](https://github.com/xiaolongnv6866-gif/V13/blob/main/v13_w/w01/W01_EVAL_PROTOCOL.md)；[V5批准的11工作包](https://github.com/xiaolongnv6866-gif/V13/blob/main/V13_APPROVED_11_WORKPACKAGES.md)。

**不要求**阅读后续20项已写诊断故事，它们是W02项目，不能替代W01 V3。若无法访问关键资料，必须将该项标 `CANNOT_VERIFY`，不得装作全部已读；只见结论表而没看正文时不可自行证明文艺质量。

## 本次只回答四个实际问题

A. 69项是否全数可回溯到真实唯一ID与对应V2/上游依据？逐项核对重复、遗漏、改名错配。回报READY/PARTIAL/INELIGIBLE数量是否与证据一致，发现不一致列具体ID。

B. 核对全部13项当前非READY候选。每行请给一个结果：`KEEP_BLOCKED`（确实还缺关键V1/V2）、`CAN_REPAIR_BY_V2`（来源够，但需要明确哪组新输入和观察）、`SOURCE_AUDIT_REQUIRED`（需要重读书中具体位置）、`WRONG_GATE`（已有证据足以改准入）。只能根据读到的资料判，不要为了凑69通过率降低标准。

C. 对56 READY逐行做**来源与V2准入完整性核对**，至少对所有发现可疑的ID列具体反证；无法全面逐行回读也应精确报告审核覆盖数量，例如 `CHECKED 12/56`，不可写“都没问题”。

D. 检查当前W01协议是否比仓颉原版缺任何**适用的**步骤，或错误把“可执行性的纸面演练”当成“真实独立宿主测试”。特别检查保留集泄漏、盲审隔离、错误/失败留存、最低限度的实际任务收益证据。

## 必须返回的格式

1. `读取清单`：逐资料“已读取全部/部分/不可访问”，列读取量和引用文件；不准凭标题冒充。
2. `总体裁决`：`69项可追溯 X/69；13项逐条实际检查 X/13；56 READY 逐行实际核查 X/56；发现错误N项；证据不足N项`。
3. `13项裁决表`，每个ID一行，列`repeat_id | 原准入 | 本次判断 | 原始证据文件+行/明确章节 | 缺口 | 最小下一步`。
4. `READY风险清单`，列有问题的ID和来源证据（没问题不必挨个复制）。
5. `协议缺陷及建议`：只列有真正质量影响的问题、具体改法、违反哪项原版要求。
6. `不可证实事项`：清楚说明需原著/更多文件/不同主体的部分。
7. `供主执行Agent处理的唯一优先队列`：最多5项，按阻断解除价值排序。

审查报告仅给建议，不能私改GitHub、不能宣称W01通过，也不能把同一聊天框的先后发言伪造成两名独立盲审。
