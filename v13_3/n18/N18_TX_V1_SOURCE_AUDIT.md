# V13.3 N18｜《铁血残明》96项 Cangjie Stage1.5 V1原文资格终审（证据提交，非封账）
source_git_head: 5a92f6e35bf83ba0d79836a646f368d6b4d8f4ad
private_epub_sha256: 9100bbcdb9f52bcd5458cbda92e16b646489efbc00df5161ed568ebac83ffbaf
standard: kangarooking/cangjie-skill@a28de55ba881b9928956a55048f743f7a9e3b23e
status: EVIDENCE_ONLY_NOT_FORMAL_PASSED

## V1原版过程
1. 按锁定原版 `SKILL.md`、`methodology/02-stage1-parallel-extract.md` 与 `methodology/03-stage1.5-triple-verify.md` 核实际候选，不把Stage1分文件等同于五真正独立Agent；逐候选区分可重建的文学规则、书内具体例子、反例/Boundaries和术语。
2. 读取用户原始《铁血残明》EPUB字节，文件SHA256与冻结值相等；五张原始证据表合计**264**条记录，去重后**177**个独立n/p段落、**74**个原始XHTML章节；实际从私有EPUB按`epub_path`逐个解析出段落并重算hash，**177/177 MATCH**，不是仅引用历史SHA记录。临时私有核验不上传原文到GitHub。
3. 真实段落与候选的文学观察对照，明确“作者叙述和角色台词”“已发生结果与预测”“小说事实与真实明末史实”“多章互不相干的主题相似与真正前后因果”。所有96项保留来源位置、章/段完整SHA256、简短直接引证、适用/反例边界和去向，见`N18_TX_V1_96.tsv`。
4. **来源支持但还没V2/V3**：32项；**来源不足或拼接过度，非active`needs_review`**：4项；**参考例子、Boundary、词典和不能独立执行的观点**：60项。没有任何真实V2测试/独立V3/verified提升。
5. 16项小说场景案例的`fictional_narrative_case`不是原版案例的`firsthand/reported_case/worked_example`之一。不能扮演作者亲历或把虚构事件当史实；仅用作小说研究的A1参考候选，必须等后来验证过的独立能力才能绑定。21反例与20术语同为参考资源，N28之后按Stage3入Bundle时需要实际映射，不能丢。
6. 具体的4项不充分源方法：`f03`（不同机关场景被拼成一个完整调解机制）、`f06`（不同时代库存缺口和交货争论并非同一条闭环资源链）、`f14`（环境风险与人力现场阻碍并非统一完整排障流程）、`p16`（指挥归属争论和另外两次信息可信度事件不能直接拼成完整方法）。在本轮终审为**V1不合格**，保留原ID和详细理由，到N28总审为非active `needs_review`；新证据需重走V1，不能自动进入N20。
7. 另外`p10,p15,p22`保留为**有来源价值但不足以单独执行的参考**。其余支持项的范围受到每条字段限定，例如`f16/p21`所说信用、票据和现金**并未证明真实兑付**，不生成现实金融或军事行动说明。
8. TX-01—TX-10十个冻结原Stage0任务的候选来源覆盖分流见`N18_TX_STAGE0_10_V1_COVERAGE.tsv`；**原20个（WM10+TX10）独立原创C仍未执行**，不能用这里的来源覆盖冒充。
9. R042老14条继续隔离；296条文学B旧强主张否决不得在本轮复活。原187候选旧四类全局快照（0 verified/108 reference/79 needs_review/0 rejected）只允许N28重算，新96裁决不改全局资格数。N19/N20是V2，真正独立V3门仍在后面且须独立资源。

## 真正独立性与版权
- 本轮V1只是原著来源充分性，不是独立评委认证创作能力；结构GitHub Actions只验证引用和记录，**不会访问私有EPUB**。私有源重算需在允许存取原始EPUB的环境中按 `scripts/verify_v13_n18_epub.py` 复跑。
- 本轮每候选最多10个汉字的原文短引，只服务定位，最终Skill绝不模仿人物、情节或独特表达。无法证明历史制度和原创小说真正增益的项需以后独立验证。
