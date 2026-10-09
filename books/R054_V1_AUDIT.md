# V13 R054｜两书逐候选Stage1.5 V1来源充分性审计

status: V1_COMPLETED_WITH_39_REVIEW_ITEMS
cangjie_pin: a28de55ba881b9928956a55048f743f7a9e3b23e
nuwa_pin: fe0374687037c4cc51a65c1e0c145afe2981dc69
A_private_original_EPUB_SHA_and_CRC: PASS_BOTH
public_ci_scope: SOURCE_STRUCTURE_ONLY

## 实际结果

|来源|RAW候选总数|限定范围PASS|REVIEW需补证|FAIL|原书不同原段SHA|
|---|---:|---:|---:|---:|---:|
|《晚明》|91|68|23|0|145|
|《铁血残明》|96|80|16|0|177|
|**合计**|**187**|**148**|**39**|**0**|**322**|

已用用户原始两份EPUB重新验证全文件SHA256/ZIP CRC，按照R002固定的OPF章节序号读取真实XHTML body/p段落，322个不同源段落SHA256与GitHub全部五路提取器来源TSV逐处一致。私有原书全部来源链按n/p排序连接的SHA256分别为`a03ed960c5278df6b33578d19a8b8483cdba1cb88e9677ee8130117e3c280495`（晚明145个）和`990a8ade5c2e78174bc82b4e7f66d4c40995f9af2e715654c7fcec2634cf6548`（铁血177个）。公开GitHub无EPUB；CI只可复核来源元数据，不能把绿灯当文学B认证。

**本轮V1 PASS只是指定条件内的小说事实/研究者有限结构有原始文本支持；不是可执行性或效用，不是历史制度外证，更不是正式SKILL。** 39条REVIEW均具体指出多场景混接、预期结果提前兑现、同一因果链未闭合等缺口；无法确定直接错误的主张保留REVIEW，不强凑FAIL。逐一证据请见两书`validation/V1_SOURCE.md`与`V1_EVIDENCE.tsv`。

重要反向核查：WM n143/p49—p55实际是提议遭上级另行决定及当事人退让，R013旧误引不恢复；WM n305仅暂行缩减预算，n520限定试点未实测普遍公平，n571茶馆后世讲述不推翻此前全部现场。TX n114官仓缺粮却有临时替代；n315受阻、n485另场有条件合作；n361职级权限有质疑也有当场澄清；n526不实战报数字的建议被明确拒绝，而非已经发布假报；n532写下金额而非未来兑现。

严格保留`B=PROVISIONAL`、`C=NOT_RUN`、`skill_certified_count=0`、`heldout=SEALED_NOT_RUN`及14条R042质量债`NO_DIRECT_PROMOTION_RECONSTRUCT_FROM_SOURCE`。R055原创合法新输入V2、R056增益V3、R057四类分流/用户轻确认全部尚未运行。案例/反例/术语主要为reference素材，未独立验证可执行方法。不得将军事、欺诈、胁迫手法变为现实行动指引；不上传版权长段。
