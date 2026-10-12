# V13｜原创长篇历史军事小说SKILL（整体能力v1.3.0）

**直接用 [SKILL.md](SKILL.md)。** 统一入口，不需要手工记住几十张方法卡，也不需要重新上传两部原著正文。用户要求先完成实质建设并交付，放弃本次独立V3/Phase4/5、四臂盲评及宿主认证等验证：真实状态 `NOT_RUN_USER_WAIVED`，**并非原版验收已通过**。

## 现在交付了什么
- 1个可供支持Markdown Skill目录的宿主读取的主入口（明确任务触发、12步执行、正文与审稿要求）；9份深入参考，含原创世界/财政/军政/人物/叙事/历史边界。
- 2书187项V1记录逐ID四分流与可追溯来源；64张RIA++结构能力卡（61有限纸面V2支持+3只有V1），附2个Bundle JSON/YAML、Glossary与Digest；没有被证实为V3独立增益的卡。
- Nuwa主题操作作为主SKILL的**内置从属模块**，并非第二个可发现Skill：4个综合判断模型、8条启发式；六维一手研究、每模型三重分析、张力和反例保存在nuwa-theme/TOPIC_OPERATIONS.md。
- 20项Stage0任务均已生成原创多场景正文与状态记录，路径examples/stage0/WM-T01..10、TX-T01..10；另有五章《潮汛账》连续写作样本、卷纲、状态账和编辑记录。**均非原著复制。**
- 完整事件源状态模板、实际可运行的Python校验、负例回归与跨聊天无损交接生成器；打包脚本可生成ZIP。

## V13 v1.3｜所有原有能力共同运行，不因最新文学纠偏而偏科

**统一入口只有`SKILL.md`**。本次没有删减或替换旧有能力：01全书因果、02社会制度与财政、03现场文笔、04人物群像认知、05状态连续性、06历史军事、07文学与AI味、08原著机制和64卡、09跨会话衔接，均由主入口v1.3的“全域扫描→共同策划→实际写作→综合审稿→状态归档”共同调度。`capabilities/INDEX.md`保留完整64卡触发，`nuwa-theme/TOPIC_OPERATIONS.md`保留4模型和8启发式。

- **每次正式创作不再只阅读最近讨论的模块**：先恢复九份参考、索引、女娲模型及项目设定；针对全部本次适用卡做完整深入读取。小说正文里不强行出现每个模块的术语或情节。
- 句法、心理标识、说话人代词、减少解释性旁白、AI味及真实角色行为都是**原有整体能力的表达层组成部分**，不能牺牲权力、财政、历史、军事、长篇结构或资源/人物连续性来单独优化。
- 原本结构门禁中`applied_cards <=12`的硬限制已改为上限全部64卡，避免第13张实际适用卡被暗中遗漏；仍不提倡机械堆卡。回归测试覆盖第13张卡和九域入口保全，但**程序仍不会凭此判断文学作品是否好看**。
- 原Cangjie、Nuwa固定上游流程和已有成果保持版本与证据边界：独立V3、Nuwa Phase4/5及宿主实际自动安装未被虚称完成。
- 《陈启明》第一章目前仍有文学审稿问题，未被作者认可；此次为**SKILL整体运行架构修复，不是第一章已达标声明**。

## V13 v1.2：从形式检查转为真实创作与文学修订（2026-10-12）
- v1.2历史修复入口（现由v1.3整合）：`SKILL.md` v1.3.0；正文文学层的首要操作在`references/03-SCENE_AND_PROSE.md`，不是仅靠64张以制度/信息/状态为主的能力卡。
- 实际审稿与禁止倒造初稿：`references/07-EDITOR_AND_FAILURES.md`；完整64张静态有效性核查：`capabilities/EFFECTIVENESS_AUDIT.md`；结论是所有卡结构完整、E段存在高度同构，**不能据此认定64种独立文学执行效果均已证实**。
- 用真实重写《陈启明》第一章《御案前》检查：`../../novels/chen-qiming/CHAPTER_001_DRAFT.md`（真实先行初稿）→`CHAPTER_001_REVIEW.json`（实质审稿）→`CHAPTER_001.md`（修改）→`STATE.json`与`NEXT_SCENE.md`；仅为创作者自审的可阅读候选，作者尚未批准。
- 结构门禁可拒绝已标记`LITERARY_REVISION_REQUIRED`的稿件，却不能自动判断一篇未被审过的小说好不好看；用户放弃的独立V3/双盲/四臂测试不恢复为阻断。
- **自动生效的真实边界**：只有宿主真正安装并加载此SKILL，正文请求才会按入口自动路由。GitHub仓库链接本身不提供跨会话自动安装或持续运行的魔法。不能虚报。

## 2026-10-12创作门禁修复（v1.1.1）
此前写完《陈启明》第一章试稿才发现跳过全流程；这暴露的是入口只要求「应当做」，**没有在正文发出前强制执行**。现已在主SKILL靠前位置设置必执行链：实际读取项目设定/适用能力卡→填好章节合同→两名有独立选择的人物→初稿→至少两项原句级敌对审稿→真正修订→事件状态/下章压力→执行脚本→再做文学人工否决。
- `scripts/chapter_gate.py` 是结构性发布闸门：拒绝缺少合同、未使用适用卡/女娲模型、初稿与终稿无实质差、缺审稿证据或缺可续写状态的章节；不会给出「文学合格」的虚假结论。
- 一个项目内保存 `PROJECT_BIBLE.md`、`CHAPTER_001_BRIEF.md`、`CHAPTER_001_DRAFT.md`、`CHAPTER_001_REVIEW.json`、`CHAPTER_001.md`、`STATE.json`、`NEXT_SCENE.md`。审稿模板为 `templates/CHAPTER_REVIEW_RECEIPT.json`，输入内容全空时应失败，不可把模板当成验收。
- 在加载过此SKILL且有文件/脚本能力的宿主，**写正文者自己在交付前运行** `python3 scripts/chapter_gate.py --project /path/to/novel --chapter 1`，用户不必每次重发指令。
- **真实边界：**GitHub文件不会自行注入所有新聊天的运行环境；若宿主未安装/未读取主SKILL、无法运行脚本，不能假装自动校验已做，也不能保证跨宿主强制执行。校验输出 `PASS_STRUCTURAL_GATE_ONLY` 仅是结构证据，文学质量仍需实质审读。

## 如何直接使用

在支持Skill目录的写作宿主，载入本目录并指定 `SKILL.md`；普通ChatGPT聊天中，将SKILL.md及本次相关references/状态上传，写“按V13创作”。**GitHub地址本身不会自动安装Skill**。

写新原创世界：先给年代、起点、主角特殊约束、首卷目标（可少量缺省），本Skill按世界→人物→卷弧→章节→正文自动运行。

续写：提供STATE.json、最近两章、NEXT_SCENE，Skill先核对权限和钱粮再写；任务如果只要正文就直接输出正文。

## 命令行（Python3.10+，仅标准库）

```bash
python3 scripts/build_release.py --check
python3 -m unittest discover -s tests -p 'test_*.py' -v
python3 scripts/validate_state.py fixtures/chaoxun_ch05.json
# 章节成品门禁，需有完整小说项目产物后运行：
python3 scripts/chapter_gate.py --project /path/to/novel --chapter 1
python3 scripts/build_handoff.py --out V13_HANDOFF.md
python3 scripts/build_release.py --out V13_HISTORY_MILITARY_SKILL.zip
```

`build_release.py`生成包含全包的确定性ZIP和逐文件SHA；已通过GitHub Actions执行固定版Cangjie原版 `cangjie.py compile --output single` 作为独立的编译结构核查。该原版编译产物**不是**最终融合主SKILL，且编译器所需 `verified.yaml` **不代表通过V3**。Nuwa模型、场景正文及全部源参考均随融合SKILL安装包分发。状态见BUILD_MANIFEST.json。

## 不包括
原著EPUB、作者独特语言模板、实际作战危险流程、未经验证史实保证、第三方文学评分、普通新聊天原生安装证明。原工程历史失败和检查点仍保留在根仓库供追溯，不妨碍用户直接创作。

## 唯一入口与验证证据

正式安装时必须**只使用这一目录**；`nuwa-theme/TOPIC_OPERATIONS.md`为主题参考，不单独安装，不得与原版Cangjie编译结果并列触发。GitHub Actions构建`v13-writing-skill-build.yml`提供完整ZIP及仓颉原版编译日志，日志中可区分编译成功与文学验证未执行。见仓库`v13_e/` 的E01—E08逐轮证明和`BUILD_MANIFEST.json`的明确豁免项。
