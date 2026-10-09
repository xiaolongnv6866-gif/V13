# V13 R042｜Stage0两书整书研究框架：用户明确批准原始记录

status: EXPLICIT_USER_APPROVAL_RECEIVED
date: 2026-10-09
project: V13
approval_target: Cangjie original Stage0, two BOOK_OVERVIEW.md documents
baseline_commit: 9375f2d57925064ba798a87f1e01cb38f11f1e39
upstream_cangjie: a28de55ba881b9928956a55048f743f7a9e3b23e
upstream_nuwa: fe0374687037c4cc51a65c1e0c145afe2981dc69

## 用户本轮明确授权原话

> 批准R042两份BOOK_OVERVIEW研究框架，保留历史质量债按原文继续核查

这是用户在本会话直接作出的明确决策，不是从先前反复“继续”推测出来的确认。作为R042 Stage0 用户审阅门的范围记录；用户没有要求启动R043。

## 两份已经确认的成果

- `books/wanming/BOOK_OVERVIEW.md`（六段结构、10条核心解释、批判边界、WM-01—WM-09独立来源任务）。
- `books/tiexuecanming/BOOK_OVERVIEW.md`（六段研究者叙事弧、10条核心解释、批判边界、TX-01—TX-10任务；提供版本止于第532有效叙事章）。
- `cangjie/reading/R042_APPROVAL_BRIEF.md`作为此次审阅简报，原版方法论与固定模板仍为最高门槛。

## **许可**和**非许可**的边界

- **已批准**：两份 Stage0 全书研究框架可作为未来阶段1五路提取的**有保留的研究输入**；R042用户明确确认门满足，前提是原文、质量审计和GitHub正式状态检查完成。
- **没有批准**：对早期R007—R024共296条机制判断全部升B VERIFIED；确认14条隔离机制可直接晋级；替代逐章阅读；视小说为真实历史或金融/军政实操；开启封存盲测；仿写原作者专有表达；提前启动R043、Nuwa Phase1或任何后台自动任务。
- **必须保留**：`cangjie/reading/STAGE0_QUALITY_DEBT_AUDIT.md`和`cangjie/reading/R042_OLD_CLAIM_QUARANTINE.tsv`的历史质量债。14条具体旧`claim_id`保持`NO_DIRECT_PROMOTION_RECONSTRUCT_FROM_SOURCE`；其余旧候选只保留`B_PROVISIONAL_UNTIL_SOURCE_CHECK`资格。抽样核查不可自动推断所有旧研究已合格。
- **A/B/C分门**：A原EPUB SHA及对应位置是真本核验；公开Actions仅`SOURCE_STRUCTURE_ONLY`；B整书研究结论`PROVISIONAL`、个别坏证据`REJECTED/SUPERSEDED`；C原创陌生任务`NOT_RUN`，SKILL已认证0。

## 正式管理动作（必须完成后方能宣布R042 PASSED）

- 在同一GitHub正式状态提交中将`ROUND_LEDGER.csv` R042设PASSED、`CURRENT_ROUND.json`设`last_passed_round=R042`、`rounds_completed=42`、`current_round=R043`且`round_status=NOT_STARTED`，保留两书真实571/532阅读计数。
- 将`cangjie_stage0_gate`设`PASSED`，并在单独字段保留`legacy_quality_debt_status=OPEN_QUARANTINED`、`literary_interpretation_status=PROVISIONAL`、`original_output_test_status=NOT_RUN`及上述审阅边界。Stage0的“通过”只表示原版四步与用户确认已满足，不是已认证Skill。
- R042的正式PASS还需全部适用GitHub Actions验收和`main`远程读回核对；未做到不能对用户宣称通过。
- 停止在R043`NOT_STARTED`，用户下次独立输入“继续”才可启动新一轮。
