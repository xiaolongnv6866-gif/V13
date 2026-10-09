# V13 R053｜两书五路候选合并、重复与任务覆盖审计

status: STAGE1_RAW_POOL_MERGED_V1_V2_V3_NOT_STARTED
date: 2026-10-10
cangjie_sha: a28de55ba881b9928956a55048f743f7a9e3b23e
nuwa_sha: fe0374687037c4cc51a65c1e0c145afe2981dc69
wanming_sha256: a8f3b43dcd496822cd384ac8e9aa85f7dc374f8430f06c6f8321c26825093082
tiexuecanming_sha256: 9100bbcdb9f52bcd5458cbda92e16b646489efbc00df5161ed568ebac83ffbaf
public_ci: SOURCE_STRUCTURE_ONLY
literary_B: PROVISIONAL
creative_C: NOT_RUN
certified_skills: 0

## 一、输入和保全总账

R052正式已通过、R053收到用户新的手动「继续」才启动。已复核GitHub原始游标52/89、R053 NOT_STARTED；完整读取Cangjie固定SKILL和`methodology/03-stage1.5-triple-verify.md`及Stage1承接规则、Nuwa固定SKILL、R042获批准两本`BOOK_OVERVIEW.md`和旧14项隔离列表。用户私有两份EPUB真实文件 SHA256均与项目登记匹配；本轮处理Stage1已收候选、原始来源SHA链和独立TASKS覆盖，**不是**自动代替R054逐候选私有正文复核。

- 《晚明》91项（17框架+23原则+14虚构案例+19反例+18术语）；`books/wanming/CANDIDATES_INDEX.md`及完整 `R053_CANDIDATE_MATRIX.tsv` 逐项存储原始ID、文件、书内p定位、任务；文件中私有原章定位145个不同n/p，源坐标在所有五路来源证据TSV中可匹配；**154对**候选共享至少一个相同原段落坐标。
- 《铁血残明》96项（17+22+16+21+20）；`books/tiexuecanming/CANDIDATES_INDEX.md`及完整矩阵逐项记录；候选引用的不同p源坐标177个，覆盖74章，**130对**候选共享至少一个确切原文段落定位。
- 合计**187项原始候选**、两个独立来源池、五种独立提取器视角各2份、WM-01—WM-09和TX-01—TX-10共19项独立文学任务。任务映射覆盖**19/19 RAW**，没有经过独立V1核证的候选数标记为0，C原创增益实验NOT_RUN。任何重复原文段落不能按出现两次算两条独立证据。
- 本轮用户源EPUB_SHA matching、之前GitHub保存的来源坐标格式和所用证据SHA可作A来源结构复审；所有B候选仍是研究假说。非原文真实历史外证的数据和书外作者定义一律不补造。

## 二、重叠审计必须严格分成三类

**A. 确切同一来源位置，不等于重复能力。** `books/{slug}/R053_SOURCE_OVERLAPS.tsv`列出每一对不同候选共享的准确n/p：WM 154对，TX 130对。典型如WM-p12 / WM-c08 / WM-ce10围绕n305不同资源承诺，分别属于规则／案例／反例；TX-f06 / TX-p05 / TX-c06 / TX-ce06共享n114，却有多时态框架、当场记录和失败边界不同用途。所有项目`RETAIN_BOTH_UNTIL_V1_AND_SEMANTIC_ADJUDICATION`，保留相邻不同责任，不能通过自动去重损失反例和限制条件。

**B. 同一书中只在故事主题上相似。** WM-f07的信息传播链与WM-f13的晚年说书后设回看具有不同时间跨度；TX-f13报功文本与TX-f16本书末尾信用承诺不是同一机制。不能因任务ID、关键词近似就抹成同一个原子步骤，不能把不同故事时间尺度变成同场重复。

**C. 跨书相似构思而非同一来源或可复刻情节。** `books/R053_CROSS_BOOK_LINKS.tsv`保存23组手工审核的**暂定类比/同词异义**，不合并两书物理来源，绝不引用另一部的p定位替代本书证据。特别：WM-f13以数年后听众对评书质疑的回看与TX-f13当场书面报功争议不是同种故事终点；WM-f17已展示多阶段债务，而TX-f16目前给定EPUB没有结尾后续履行。三对共享术语（军功/军饷/塘报）只有原词表面相同，小说上下文可指不同制度和立场。

## 三、保留深挖的缺口及源类例外

- V1需逐条核原始章节、反向场面、来源定位是否真正支持候选所写规则；相同段落出现四次绝不是四次独立验证。特高风险：假设正面程序已全部落实（WM临时试点，TX新士官待遇）、把角色受压之下顺从当自愿、把TX n526建议虚写认作实际传播、将TX n532金额落笔当未来兑付。
- V2必须用**全新合法写作输入**实际核候选方法是否能完成清晰任务；V3仍须基线对照证明效用，不因187条候选/19项任务覆盖就假称可执行/有用。
- 未来从`c`案例提取到能力A1时必须裁决`fictional_narrative_case`这个原版枚举外扩展是否合法；`g`术语本身通常仅作为书的参考层，而非独立Skill；无需为了晋级率将无方法的单元包装成SOP。
- WM-09的后世叙述偏差、TX-10的不兑现信用责任、WM-02的长期伙伴伦理分歧、TX-05的组织内部不同意和TX-08的弱势者实际拒绝能力，都是**不可因为粗线条跨书合并而消失的高价值边界**。
- R042曾确认的是BOOK_OVERVIEW研究骨架，不是历史14项旧错引恢复可信。持续`OPEN_QUARANTINED`/ `NO_DIRECT_PROMOTION_RECONSTRUCT_FROM_SOURCE`。前后原著版权不公开粘贴，危险军务、政治影响、强制/融资行为不纳入实施型能力。

## 四、正式关口分工（本次只做Stage1.5第1步及覆盖草案）

- R053：读齐10份原始提取器成果，跨书全体187项保全、按来源坐标列出重复碰撞、类比组留具体区分、核19独立任务RAW来源映射、记录缺口。
- R054：逐项V1实际源充分性判定，PASS/REVIEW/FAIL和冲突来源；当前**NOT_STARTED**。
- R055：V2合法新输入可执行性演练；当前NOT_STARTED。
- R056：V3任务增益比较；当前NOT_STARTED。
- R057：按原版Stage1.5的`verified/reference/needs_review/rejected`完成四路去向和用户轻确认强制门，未用户批准不得越过。
- 更后Stage1.6、RIA++、压力测试、编译/安装均未实施；当前SKILL认证数0，盲测SEALED。

只有GitHub所有Actions绿色和主分支远程回读一致后R053才能PASSED并将R054记为NOT_STARTED。
