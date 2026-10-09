# V13 R051｜《铁血残明》原版Cangjie反例提取独立审计

status: RAW_COUNTEREXAMPLE_CANDIDATES_NOT_VERIFIED
CI_CLASSIFICATION: SOURCE_STRUCTURE_ONLY
literary_B: PROVISIONAL
creative_C: NOT_RUN
source_epub_sha256: 9100bbcdb9f52bcd5458cbda92e16b646489efbc00df5161ed568ebac83ffbaf
cangjie_pin: a28de55ba881b9928956a55048f743f7a9e3b23e
nuwa_pin: fe0374687037c4cc51a65c1e0c145afe2981dc69

## 一、真实原始EPUB和检索说明

本轮打开用户原EPUB并重新核对SHA256和zipfile.testzip()无损。以OPF 551项原始spine和R002冻结叙事索引取得**532**个实际叙事XHTML成员（不能用印刷章号代替ordinal）。从原始正文重算全部 **33,278** 段落、**2,087,501**个Unicode字符，已有结构感知分章私有**958**检索chunk/SQLite FTS5 trigram目录位于本会话私有环境（来自R050原文索引，复用其真实源块，而不是复制R050案例结论）。本轮用“反对/没想到/不肯/失望/为难/后悔/不足/未必/没有办法/流言/粮食”等多组独立反向检索重新召回，并按真实邻接段和必要时章节扩大核查，不把关键词命中等同文学证据。上游build_chunks.py/build_index.py未直接执行，复用的是注明兼容性的私有索引；保留原版检索式取块+回原书核查职责。源书不上传到GitHub。

最终记录**21条** ce01—ce21原始反例，**67处**有效原始段落SHA定位，横跨**24个**原叙事章节和R042全部六个研究弧；对应**27个**实际源chunk。与R048框架、R049原则、R050案例三路已登记n/p并集比对，本轮新增**41处**原段落定位；旧位置全部从原EPUB再核，不把先前解释复制为本轮结论。段落SHA不证明文学解释真伪，GitHub Actions公开只能核对来源结构与规则状态，故质量标签SOURCE_STRUCTURE_ONLY。

## 二、观察到的失败与“尚未发生”的风险不得混淆

- **制度与权力**：ce01旧幕后授权被新决策者拆穿（n013/p34、p52→p56）；ce02申详先发却仍可能不获功（n055/p30→p32），后者只是幕友的未定判断；ce12明明有已签名册却因举报缺位，例行简报还漏了相关矛盾（n213/p2、p5、p18、p21）。
- **组织与人性**：ce03报名热烈但报到有限（n080/p19→p67）；ce04领导有命令权却无法立刻获得未知信息，属下竞岗时也相互猜忌（n082/p1、p10、p31）；ce07家仆不愿受新身份约束而遭拒（n161/p65→p66），这不是自由同意。ce08对严密规章潜在反噬的判断尚非已发生溃败。
- **财务与资源**：ce06仓库短缺但商铺及捐助确实临时补救（n114/p27、p29），不得写成完全断供；ce09新经营收入预计和现场成本/商人避让存在冲突（n174/p13、p37、p39）；ce10储蓄产品的赞成与家庭消费需求都有实际人物发声；ce17(n431/p10、p17→p19)承诺折银却拿不到眼前粮食，属原文已经发生的资源错位。
- **角色信誉与授权**：ce11公共官员对主角的态度被私人旧争议影响（n202/p3、p20、p33），但指控没有在此章彻底判定；ce13同一叙事中n315合作未谈成，n485出现一次附条件合作，反驳“所有盟友都必然拒绝”；ce14胜后安置还面临地方接受条件，没有已被证明的终局。
- **提出新规与真实落地**：ce15士官待遇方案遭属官权责质疑且已获口头澄清，缺长期实测；ce16重复请旨和模糊批复浪费当场时间（n424/p9、p11、p25），但不能预言最终战果；ce18既有分工文件仍无法覆盖现场人手与民事摩擦（n490、n505）。
- **信息与后果**：ce19数字“写得合理”的建议被目击人否决（n526/p82、p85、p87），不可谎称不实报功已发表；ce20批准请假与费用到手、家属接回并非一回事（n527/p30→p39）；ce21(n531/p8、n532/p47→p49)只是当前提供版本的金额落笔，不能杜撰已经兑付或失败。

## 三、来源身份、反证、质量债与下游判停

原版 counter-example-extractor 面向非虚构作者所提出的警示，但这里是文学作品。每项以evidence_kind区分OBSERVED_FAILURE / OBSERVED_CONTRADICTION / ANTICIPATED_RISK / CHARACTER_DISAGREEMENT / PARTIAL_SUCCESS / OUTCOME_NOT_SHOWN等，视点是研究者的**小说内部**可证伪解释，不把角色台词称作者法则。failure_mode、mechanism、warning_signs、bound_to与确切n/p/chunk均存原始候选；原文版权不公开贴句，source_quote保留空字段，后续Stage1.5 V1必须重新打开私有原著核查。所有10项TX-01—TX-10有至少一条候选关联，只证明RAW映射，不是任务能力已验收。

R042的14项历史claim继续NO_DIRECT_PROMOTION_RECONSTRUCT_FROM_SOURCE，其他旧文学主张不自动升B VERIFIED。A私有原著SHA/CRC以及选中段落原文核查通过；B=PROVISIONAL；C=NOT_RUN；已认证Skill 0，密封盲测未开启。军事、政治胁迫及金融欺诈细节不转化成现实可操作策略。本轮只负责R051，R052 glossary不得启动。Github专项公开CI仅SOURCE_STRUCTURE_ONLY，且要保证提交后各项旧CI仍绿、三文件正式原子推进后才可PASSED。
