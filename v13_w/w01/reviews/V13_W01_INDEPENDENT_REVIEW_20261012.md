# V13｜W01 第一次跨聊天框来源与方法准入复核

- 日期：2026-10-12
- 被审仓库：<https://github.com/xiaolongnv6866-gif/V13>
- 委托合同：[CROSS_CHAT_REVIEW_01_ELIGIBILITY.md](https://github.com/xiaolongnv6866-gif/V13/blob/main/v13_w/w01/CROSS_CHAT_REVIEW_01_ELIGIBILITY.md)
- 方法基准：仓颉 `kangarooking/cangjie-skill@a28de55ba881b9928956a55048f743f7a9e3b23e`，`methodology/03-stage1.5-triple-verify.md`
- 角色：只读证据复核，不是V3独立创作者或两名盲评委；未修改GitHub；不是 W01 PASS/正式认证。
- 重要限制：本次独立从GitHub读取资料，但当前模型可能获得同账户历史聊天上下文；不宣称技术层面的完全背景隔离。本次判断仅依据下述重新读取的文件，不将先前聊天意见当证据。

## 1. 读取清单

|资料|状态与实际覆盖|用途与边界|
|---|---|---|
|[仓颉Stage1.5原文](https://github.com/kangarooking/cangjie-skill/blob/a28de55ba881b9928956a55048f743f7a9e3b23e/methodology/03-stage1.5-triple-verify.md)|已读取全文（原始文本3219字符）|逐条对照V1/V2/V3、四分流、Stage0覆盖及用户轻确认要求|
|[69原始映射](https://github.com/xiaolongnv6866-gif/V13/blob/main/V13_3_V3_69_TO_ROUNDS.tsv)|全部69/69行|唯一repeat_id、候选ID、任务、历史SHA、V3状态|
|[69项预审](https://github.com/xiaolongnv6866-gif/V13/blob/main/v13_w/w01/V3_69_ELIGIBILITY_PREFLIGHT.tsv)|全部69/69行|逐行交叉核对V1/V2|
|[13项例外](https://github.com/xiaolongnv6866-gif/V13/blob/main/v13_w/w01/W01_13_EXCEPTIONS.tsv)|全部13/13行|逐项查禁入原因|
|[晚明V1源记录](https://github.com/xiaolongnv6866-gif/V13/blob/main/v13_3/n17/N17_WM_V1_91.tsv)及[审计](https://github.com/xiaolongnv6866-gif/V13/blob/main/v13_3/n17/N17_WM_V1_SOURCE_AUDIT.md)|全部91/91行，审计全文|检查候选V1类型、出处、限定边界、决定；原著EPUB未取得，不能独立重算哈希|
|[铁血V1源记录](https://github.com/xiaolongnv6866-gif/V13/blob/main/v13_3/n18/N18_TX_V1_96.tsv)及[审计](https://github.com/xiaolongnv6866-gif/V13/blob/main/v13_3/n18/N18_TX_V1_SOURCE_AUDIT.md)|全部96/96行，审计全文|同上|
|[N19预注册](https://github.com/xiaolongnv6866-gif/V13/blob/main/v13_3/n19/N19_WM_V2_PREREG_32.tsv)、[结果](https://github.com/xiaolongnv6866-gif/V13/blob/main/v13_3/n19/N19_WM_V2_RESULTS_32.tsv)、[消融](https://github.com/xiaolongnv6866-gif/V13/blob/main/v13_3/n19/N19_V2_ABLATION_32.tsv)、[审计](https://github.com/xiaolongnv6866-gif/V13/blob/main/v13_3/n19/N19_V2_SOURCE_AND_QUALITY_AUDIT.md)|各32/32行、审计全文；A/B/C/D四份原创输出全部32/32小节|检查预注册、实际章节存在、负例及结果矛盾；不是文学盲评|
|[N20预注册](https://github.com/xiaolongnv6866-gif/V13/blob/main/v13_3/n20/N20_TX_V2_PREREG_32.tsv)、[结果](https://github.com/xiaolongnv6866-gif/V13/blob/main/v13_3/n20/N20_TX_V2_RESULTS_32.tsv)、[消融](https://github.com/xiaolongnv6866-gif/V13/blob/main/v13_3/n20/N20_V2_ABLATION_32.tsv)、[审计](https://github.com/xiaolongnv6866-gif/V13/blob/main/v13_3/n20/N20_V2_SOURCE_AND_QUALITY_AUDIT.md)|各32/32行、审计全文；A/B/C/D四份原创输出全部32/32小节|同上|
|[原47项历史审计](https://github.com/xiaolongnv6866-gif/V13/blob/main/v2/v3/FINAL_47_EVIDENCE_AUDIT.tsv)、[另22项审计](https://github.com/xiaolongnv6866-gif/V13/blob/main/v2/v3/FINAL_22_ADDITIONAL_AUDIT.tsv)及历史JSON目录清单|47+22全部69项旧输出SHA与GitHub目录实际blob SHA一一匹配；**未逐份读69份旧JSON内容**|可验证历史文件身份与SHA存在，不证明旧文学质量；旧结果本来也非盲、非真实V3|
|[公开校准56题](https://github.com/xiaolongnv6866-gif/V13/blob/main/v13_w/w01/V3_56_PUBLIC_CALIBRATION_FROZEN.tsv)|全部56/56行|方法卡、任务增益假说、失败条件及源定位列抽检|
|[W01协议](https://github.com/xiaolongnv6866-gif/V13/blob/main/v13_w/w01/W01_EVAL_PROTOCOL.md)、[11包批准](https://github.com/xiaolongnv6866-gif/V13/blob/main/V13_APPROVED_11_WORKPACKAGES.md)、[运行状态](https://github.com/xiaolongnv6866-gif/V13/blob/main/v13_w/w01/W01_RUN_STATUS.md)|全文|检查保留集、盲审、V3/Stage4区分、质量门|
|[五项新V2补测冻结合同](https://github.com/xiaolongnv6866-gif/V13/blob/main/v13_w/w01/repair_20261012/FROZEN_5_PARTIAL_V2_RETEST.md)、[说明](https://github.com/xiaolongnv6866-gif/V13/blob/main/v13_w/w01/repair_20261012/README.md)及五份补测答卷|冻结合同+说明全文、5/5新补测全文|**这是旧预审表之外的新证据**，必须单独评估；冻结提交 `859afc7...` 早于五答卷提交 `7ba3842...`，已查Git历史|
|用户私有《晚明》《铁血残明》EPUB|**不可访问/未读取原著**|不能独立复核N17/N18声称的145/177原文段落、原文语境充分性或文学原创性|
|不同作者、独立双盲评委、真实宿主Stage4结果|**没有可读的实际执行产物**|不能宣称真实V3、效果提升或最终SKILL认证|

## 2. 总体裁决

**69项可追溯69/69；13项逐条实际检查13/13；56 READY逐行实际核查56/56；准入身份/计数/当前旧状态错配0项；检测到60处记录/试验设计问题（55条错误“原文定位”字段、4处旧正文自判与汇总矛盾、1项新补测消融输入无有效变化）；现有非READY的准入证据缺口13项，真实独立V3证据缺口69项。**

这三个「69/69」「13/13」「56/56」指公开**文件级记录核对**，不代表69个原文断言已经由本审核者从EPUB逐一证实，也不代表56项的文学效果获得外部评价。

逐ID身份核验：69个唯一`repeat_id`，69个唯一`candidate_id`，69个旧SHA均对应47+22审计及GitHub旧JSON真实blob；56 READY均可回溯到V1来源支持与N19/N20原始V2局部PASS，5 PARTIAL均能追到原局部失败，8 INELIGIBLE均回溯到5个V1 needs_review及3个V1 reference。没有漏项、重名候选、书别错配。历史旧输出的评分全部为`NOT_VERIFIED`或`DIAGNOSTIC_ONLY_NOT_VERIFIED`，不得升级为独立增益证据。

### 新证据相对旧状态

五项新补测有先冻结再提交的文件及完整任务记录，但`V3_69_ELIGIBILITY_PREFLIGHT.tsv`仍是**正式冻结的旧 56 READY / 5 PARTIAL / 8 INELIGIBLE**。本审核建议：**4项可考虑将V2有限准入由PARTIAL改为SCOPED_PASS（此处用`WRONG_GATE`表示“当前旧门状态需要按新证据重判”）；1项WM-f10保持需补做有效消融（`CAN_REPAIR_BY_V2`）**。这是供主Agent复核/提交的建议，不是直接更改官方门禁。无论何种处理，真实V3仍是0。

## 3. 13项逐条裁决

源依据行号均为GitHub原始TSV中的1-based行号（含表头）。`SOURCE_AUDIT_REQUIRED`并不表示已有新原文支持；无新证据应继续nonactive。`WRONG_GATE`仅指最新补测可支持**限定V2 walkthrough**，不能代表V3或Stage4认证。

| repeat_id | 原准入 | 本次判断 | 原始依据（文件/行/位置） | 缺口/评估 | 最小下一步 |
|---|---|---|---|---|---|
| B076R-006 / WM-f10 | PARTIAL | **CAN_REPAIR_BY_V2** | `N17_WM_V1_91.tsv:L11` n085/p25,n338/p40,n339/p31；`N19_WM_V2_RESULTS_32.tsv:L9`；新`WM_f10_V2_RETEST.md` | 新补测已写四户与第3/7日三阶段，正向路径明显补足；但消融声称“删掉第7日签认的支付凭证”，题面和正文中本来就没有该支付凭证，实际删除没有改变输入，不是有效负例 | **另行冻结**一条真正移除已有关键事实的消融任务，实际执行后复核；勿改旧答卷/旧PARTIAL |
| B076R-023 / TX-f02 | PARTIAL | **WRONG_GATE**（建议有限V2晋级） | `N18_TX_V1_96.tsv:L3` n030/p33,n055/p30–32；`N20_TX_V2_RESULTS_32.tsv:L3`；新`TX_f02_V2_RETEST.md` | 旧材料缺12笔凭单；新输入列完整12笔应付、11笔有具名回执、缺第7笔回执，明确100=89+11；主考只批准一月有限试用，不把“未证支付”判成“确定未付”；消融真的撤掉第7笔应付单 | 主Agent可按仓颉V2有限可执行性正式复核、保留不确定性，**不作V3提升** |
| B076R-050 / WM-p06 | INELIGIBLE | **SOURCE_AUDIT_REQUIRED** | `N17_WM_V1_91.tsv:L24` n140/p30,p36 | 人物脱身话术无法支撑完整时间优先矩阵与步骤；无V2 | 如要升级方法，重新读原著补全输入/操作/输出证据并走V1；否则保持`needs_review/reference` |
| B076R-053 / WM-f05 | PARTIAL | **WRONG_GATE**（建议有限V2晋级） | `N17_WM_V1_91.tsv:L6` n089/p1,p18,p26及n111/p1；`N19_WM_V2_RESULTS_32.tsv:L6`；新`WM_f05_V2_RETEST.md` | 新尺由非生产者核对，实做6、验收5、失败1，出现完整“异议—调整—再做—实证差异”闭环；工资归属未定属于保留边界，不影响这项限定机制的执行性 | 主Agent按V1的“组织复盘/基层异议反馈”边界复核，最多改SCOPED_V2，不能凭六张试件称长期品质提升 |
| B076R-054 / WM-p10 | INELIGIBLE | **SOURCE_AUDIT_REQUIRED** | `N17_WM_V1_91.tsv:L28` n222/p28,n390/p25 | 小说人物宽慰不是可执行的普遍免责程序；无V2 | 新原文须支持明确责任认定分支后重新V1，否则继续非active |
| B076R-058 / TX-f03 | INELIGIBLE | **SOURCE_AUDIT_REQUIRED** | `N18_TX_V1_96.tsv:L4` n008/p2,n030/p33,n055/p31 | 三个不相干的制度场面不足构成一次完整调解闭环；无V2 | 补读同一完整事件链，确实有原文流程才可重建，否则参考保留 |
| B076R-060 / TX-f15 | PARTIAL | **WRONG_GATE**（建议有限V2晋级） | `N18_TX_V1_96.tsv:L16` n161/p65,n380/p31,n527/p29–30；`N20_TX_V2_RESULTS_32.tsv:L13`；新`TX_f15_V2_RETEST.md` | 新任务出现亲自申诉、具名掌柜批准、同伴自愿、实际工作和第7日少两日工时的反馈；**没有**永久解决收入差；V1本就不要求所有代价被成功补偿 | 可承认“反对者实际处境被连续呈现”有限V2路径；不得写成经济权利和长期保障已解决 |
| B076R-062 / TX-p15 | INELIGIBLE | **KEEP_BLOCKED** | `N18_TX_V1_96.tsv:L33` n386/p39,p45,p49 | 官员不同主张有参考价值，但不构成独立操作方法 | 保持`reference`，进入参考映射而非V3 |
| B076R-064 / TX-f07 | PARTIAL | **WRONG_GATE**（建议有限V2晋级） | `N18_TX_V1_96.tsv:L8` n315/p40,n320/p36等；`N20_TX_V2_RESULTS_32.tsv:L6`；新`TX_f07_V2_RETEST.md` | 新任务有权限机关的具名书面澄清、原粮仓仍封、前两轮实际发放、第三轮仍待审及等待成本；完整有限重规划可见 | 主Agent确认“架空权限”边界与负例处理，限V2通过，不能推广为真实明末救济法规 |
| B076R-065 / TX-f14 | INELIGIBLE | **SOURCE_AUDIT_REQUIRED** | `N18_TX_V1_96.tsv:L15` n285/p5,p6;n490/p28 | 地点条件与另一场战后劳动事件不构成同一个排障算法 | 重新找合法连续原文流程，找不到即非active/参考 |
| B076R-067 / TX-p10 | INELIGIBLE | **KEEP_BLOCKED** | `N18_TX_V1_96.tsv:L28` n175/p23,n531/p25,p26 | 出版费用与编辑争论只具独立场景参考价值 | 保持reference，别拼成未经证明的编辑财务SOP |
| B076R-068 / TX-p16 | INELIGIBLE | **SOURCE_AUDIT_REQUIRED** | `N18_TX_V1_96.tsv:L34` n420/p2,n430/p59,n475/p25 | 发令归属与信息可信度是三个独立事件，未有统一完整流程 | 原著若没有贯穿证据则保持nonactive |
| B076R-069 / TX-p22 | INELIGIBLE | **KEEP_BLOCKED** | `N18_TX_V1_96.tsv:L40` n103/p16,p18 | 个体生存忧虑与宏观风险推测不构成可执行机制 | 保留人物动机参考，不送V3 |

补测入口：[冻结合同](https://github.com/xiaolongnv6866-gif/V13/blob/main/v13_w/w01/repair_20261012/FROZEN_5_PARTIAL_V2_RETEST.md)｜[WM-f05](https://github.com/xiaolongnv6866-gif/V13/blob/main/v13_w/w01/repair_20261012/WM_f05_V2_RETEST.md)｜[WM-f10](https://github.com/xiaolongnv6866-gif/V13/blob/main/v13_w/w01/repair_20261012/WM_f10_V2_RETEST.md)｜[TX-f02](https://github.com/xiaolongnv6866-gif/V13/blob/main/v13_w/w01/repair_20261012/TX_f02_V2_RETEST.md)｜[TX-f07](https://github.com/xiaolongnv6866-gif/V13/blob/main/v13_w/w01/repair_20261012/TX_f07_V2_RETEST.md)｜[TX-f15](https://github.com/xiaolongnv6866-gif/V13/blob/main/v13_w/w01/repair_20261012/TX_f15_V2_RETEST.md)。

## 4. READY风险清单

**覆盖声明：**56/56 READY逐行实际核对了原身份、V1决定/原文坐标哈希及边界、N19/N20预注册行、原结果行、对应A—D场景小节、消融行和公开校准方法卡。**未发现56条中有哪条应因旧V1/V2表错配而直接撤销READY；不表示原著文学方法或输出质量已被独立证实。**

### 风险R1：55条公开校准题的 `original_V1_loci` 字段并非规范定位

真实查询显示56条里只有 `B076R-004` 的该字段含一个完整的`n143/p49`，而其余`55/56`都不含任何完整`nNNN/pNN`坐标，例如 `B076R-001` 填的是“身份求生、合法名分、旁人接纳与可行使”，它是V1叙事观察文字截段，**不是**`n001/p44`一类定位。`B076R-004`虽含一个正确样式坐标，也没有完整列出所有原始位置。

涉及的55个READY ID（按仓库实际校准表逐行枚举）：

`B076R-001,002,003,005,007,008,009,010,011,012,013,014,015,016,017,018,019,020,021,022,024,025,026,027,028,029,030,031,032,033,034,035,036,037,038,039,040,041,042,043,044,045,046,047,048,049,051,052,055,056,057,059,061,063,066`。

**影响：**未来若仅靠公开校准题证明“每一条方法有具体原文位置”，55条链条断裂。上游V1的正确坐标仍然存在，所以这是派生校准字段错误，不能据此将56项V1全部判无效。

**修复：**不要原地改已冻结并签SHA的56题。新建只读补充交叉索引，每条`repeat_id → candidate_id → source_V1_file → source_V1_line → all_original_loci/all_source_loci → source_hash → V1_boundary`；将新索引单独冻结并声明它是**追加引用纠错**而非事后修改试题。盲审者不得看到原著来源字段。

### 风险R2：旧N19四项正文自判PASS，与结果表PARTIAL矛盾

旧原文N19的 `WM-f03`、`WM-f05`、`WM-f10`、`WM-f17` 在[A](https://github.com/xiaolongnv6866-gif/V13/blob/main/v13_3/n19/N19_V2_OUTPUTS_A.md)或[B](https://github.com/xiaolongnv6866-gif/V13/blob/main/v13_3/n19/N19_V2_OUTPUTS_B.md)正文结尾仍有 `` `PASS_SCOPED` `` 表述，而[N19结果表](https://github.com/xiaolongnv6866-gif/V13/blob/main/v13_3/n19/N19_WM_V2_RESULTS_32.tsv)正式判为`V2_PARTIAL_NEEDS_FOLLOWUP`。其中**在69队列中**的是`B076R-053`（f05）和`B076R-006`（f10）；`f03/f17`不在本次69名单，但旧账矛盾应一并保留修正说明。按保守优先级，以结果表PARTIAL为准，不可用正文的PASS词覆盖失败。

**修复：**附加不可变更的“正文早期自判错误/最终结果优先”勘误表，而非静默覆盖历史失败或预注册输出；并在最新补测决议中同时列旧失败和新证据。

### 风险R3：WM-f10新补测的消融没有删除真实存在的输入

[WM-f10新补测](https://github.com/xiaolongnv6866-gif/V13/blob/main/v13_w/w01/repair_20261012/WM_f10_V2_RETEST.md)称删去“第7日有经双方签认的工钱**支付凭证**”，但该任务预设与正文从未提供真实支付凭证，正文结论本就是“应付未支付”；删除一个不存在的条件不会造成输入变化。此例不可作为有效的新`ablation_actual_output`。需重新冻结可真正删减的事实（如第7日某个已经存在的工期核对记录），执行并记录新旧结果，不事后改写旧冻结输入。

## 5. W01协议缺陷与可执行修正

|问题|具体影响|修正|仓颉原版关口|
|---|---|---|---|
|盲审说明要求评委“不见预期方向”，评分第5格又要评`measurable_hypothesis`|若将候选专属增益假说给评委，会暗示B应有的变化，损坏盲评；若不给，评委无法按当前第5项打分|评分分为**评委盲用通用质量指标**与**独立管理员事后按预注册假说核对**；不要把方法特征/预期方向流入盲评包；冻结评分规则与角色权限|Stage1.5 V3要求可检查任务收益；Stage4真实输出比较不能凭自评|
|公开56题已被主执行Agent看见，不能再扮真正保留集；真实保留集准入阈值、每方法最少测试数量仍未锁定|可能根据公共校准结果反复调题、事后定义“通过”，产生选择偏差|由与设计者不同的主体**在创作前**固定保留题数量、题源与哈希、双臂输入差异、主/副指标、通过阈值、缺样分母、盲审解盲时机；保留集在评审前对主Agent与创作者不可见|V3真实任务效用；Stage4同任务基线验证|
|缺实际隔离创作者及两名不同评委，所有69项真实V3=NOT_RUN|不能把校准、同模型自审或GitHub CI当独立实测|先确认3类不同主体可执行、隔离账号/上下文、记录提供商/模型版本/费用边界与日志来源，再执行。若资源不足，W01必须BLOCKED|Stage1.5 V3及Stage4；W01自定更严格双盲合同|
|冻结公开题的55条来源定位字段错误|审计从方法卡不能直接返回原文具体段落|追加不可变交叉索引，保留原冻结hash，分离对审计员可见的源坐标与评委不可见的原著信息|Stage1.5 V1逐规则对应`source_id`及精确位置|
|原版Stage1.5六步还包括Stage0 coverage-audit、高优先任务复核、四分流及用户轻确认，但W01主要是预备V3协议|W01不能自己等同于完整Stage1.5，更不能绕过W02最终裁决|按V5工作包将Stage0 20题→候选→原文→decision→最终交付去向、critical/high缺口，明确交给W02/N28；在执行Stage1.6前做完整用户确认。不要因W01局部完成自动批准后续编译|Stage1.5“执行流程”第4—6步|

已有协议中**做得对、不得撤销**的部分：明确V2 paper walkthrough≠Stage4真实宿主；公开题不能充隐蔽保留集；真实独立创作者及两名盲审员需隔离；失败和缺失样本进入分母；两臂基线与方法卡单因素；不动用未经批准的费用/权限。这些约束比原版更严格，但不冲突。

## 6. 不可证实事项

1. **私有EPUB不可访问。**不能独立复现N17声称的145/145、N18声称177/177的原始段落哈希，不能逐章确认短锚与候选规则在完整原文语境是否恰当。GitHub V1记录完整不等于本审查已真正读过两部作品。
2. 69个旧JSON虽能按blob SHA精确对到历史产物，**此次未逐份读旧JSON正文**；这一步仅用于来源身份验证。旧评分自评不可能证明V3文学增益。
3. 56个有限V2场面都已定位并检查纸面前置和输出结构，但没有不同读者/作者的审美判断，更没有跨章持久故事质量的科学验证。
4. 没有独立创作者、两名独立盲审、隐藏保留集的真实输出/评分/隔离记录；不能认证新SKILL真实优于无方法基线，也不能认证干净宿主调用。
5. 仓库内新的5份补测均为**主Agent自生成的新输入纸面演练**。本审核可判断输入与规则的逻辑一致性，但不能将自己说成第二、第三位独立文学评委。

## 7. 供主执行Agent处理的唯一优先队列（最多5项）

1. **真实V3执行资源门**：确认真正独立创作者与两位相互隔离评委是否能以用户允许的零/确定费用运行；否则W01继续BLOCKED，不推W02 verified或最终认证。
2. **修协议隔离与预注册**：分开盲审中性评价与`measurable_hypothesis`判定；独立主体预先封存隐藏保留集、测试量与判停阈值，原始失败保全。
3. **裁定新V2补测**：由主Agent按V1边界接受4项有限V2补足的审计建议；WM-f10另冻结真正有输入差异的新消融；不擅改现行56/5/8冻结表或擦除旧失败。
4. **修真实出处交叉索引**：给56校准卡附加按ID关联的准确源`n/p`、哈希与边界，不修改原校准冻结blob，也不泄露到盲评包。
5. **清历史冲突并落实Stage1.5完整交接**：留存N19的4项“旧场景PASS/汇总PARTIAL”勘误；W02必须完成Stage0 coverage-audit及四分流/用户确认，不能把W01局部资格当成最终verified。

## 最终限定结论

**当前旧账56 READY / 5 PARTIAL / 8 INELIGIBLE在原N17—N20证据下结构一致，不存在69ID、文件SHA、V1资格或原始V2结果的错配。**但**公开校准来源坐标字段大面积错误、旧输出有四处自判矛盾、WM-f10新消融设计无效**；最新五项补测已产生可审计新证据，其中四项可由主Agent正式复核有限V2资格，仍不得据此给任何一个候选真实V3通过。**W01不得标PASSED；Stage1.5四分流及原著充分性仍有明确未完义务。**