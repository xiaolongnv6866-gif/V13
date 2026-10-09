# R056｜V3比较评分事先冻结的合同

本合同冻结先于R056无候选对照场景创作。两组均为**19个完全相同的R055真实原创输入**，每题输出双场景A/B、状态账和未知；候选组直接采用R055原提交内容，不能事后重写。基线提示词不给候选ID、冻结评价细则或候选输出，但由**同一Agent**写作，无法保证真正不知研究机制，因此是非盲/非独立的探索性对比，不许声称因果归功已经成立。

|维度|满分|评分标准|
|---|---:|---|
|frozen_criteria|3|For each of 3 R055 frozen output criteria, 1 iff actual A/B scene or ledger provides specific, semantically consistent evidence. Quote ≤25 Chinese chars per proof; no proof yields 0.|
|causal_chain|2|0 no meaningful action-consequence; 1 visible action and response but consequence uncertain/untracked; 2 concrete action->other character response->changed situation/next constraint without invented result.|
|character_agency_continuity|2|0 others merely echo lead; 1 one other has independent preference/choice OR meaningful time continuation; 2 two distinct preferences and traceable progression across A/B, or explicit informed refusal and preserved downstream impact.|
|epistemic_boundaries|2|0 unearned omniscience or falsely claimed outcome; 1 unknown/unverified limitation stated only loosely; 2 separates witnessed/rumor/approval/estimate/promise as appropriate and explicitly leaves outcome not observed unknown.|
|deliverable_traceability|2|0 state/outcome incoherent with scenes; 1 ledger exists but leaves important ambiguity/contradiction; 2 compact state_contract and unknowns accurately track scene claims, distinguish completed/pending/undetermined.|

满分11分=原冻结条件3分+因果2分+角色能动/连续2分+知情边界2分+实际交付一致2分。每项须引用自己输出中的短证据，不可按来源作者声望或写作长度加分。总体比较必须报告胜/负/平、负增益反例、评分偏差和可替代解释；方法候选共同使用，不能把场景收益无条件分摊给每个方法ID。真正独立盲评及Stage4宿主后续另做。R056不操作R057四分流/用户门。
