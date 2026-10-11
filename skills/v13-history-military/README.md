# V13｜原创长篇历史军事小说SKILL（交付建设版）

**直接用 [SKILL.md](SKILL.md)。** 统一入口，不需要手工记住几十张方法卡，也不需要重新上传两部原著正文。用户要求先完成实质建设并交付，放弃本次独立V3/Phase4/5、四臂盲评及宿主认证等验证：真实状态 `NOT_RUN_USER_WAIVED`，**并非原版验收已通过**。

## 现在交付了什么
- 1个可供支持Markdown Skill目录的宿主读取的主入口（明确任务触发、12步执行、正文与审稿要求）；9份深入参考，含原创世界/财政/军政/人物/叙事/历史边界。
- 2书187项V1记录逐ID四分流与可追溯来源；64张RIA++结构能力卡（61有限纸面V2支持+3只有V1），附2个Bundle JSON/YAML、Glossary与Digest；没有被证实为V3独立增益的卡。
- Nuwa主题操作作为主SKILL的**内置从属模块**，并非第二个可发现Skill：4个综合判断模型、8条启发式；六维一手研究、每模型三重分析、张力和反例保存在nuwa-theme/TOPIC_OPERATIONS.md。
- 20项Stage0任务均已生成原创多场景正文与状态记录，路径examples/stage0/WM-T01..10、TX-T01..10；另有五章《潮汛账》连续写作样本、卷纲、状态账和编辑记录。**均非原著复制。**
- 完整事件源状态模板、实际可运行的Python校验、负例回归与跨聊天无损交接生成器；打包脚本可生成ZIP。

## 如何直接使用

在支持Skill目录的写作宿主，载入本目录并指定 `SKILL.md`；普通ChatGPT聊天中，将SKILL.md及本次相关references/状态上传，写“按V13创作”。**GitHub地址本身不会自动安装Skill**。

写新原创世界：先给年代、起点、主角特殊约束、首卷目标（可少量缺省），本Skill按世界→人物→卷弧→章节→正文自动运行。

续写：提供STATE.json、最近两章、NEXT_SCENE，Skill先核对权限和钱粮再写；任务如果只要正文就直接输出正文。

## 命令行（Python3.10+，仅标准库）

```bash
python3 scripts/build_release.py --check
python3 -m unittest discover -s tests -p 'test_*.py' -v
python3 scripts/validate_state.py fixtures/chaoxun_ch05.json
python3 scripts/build_handoff.py --out V13_HANDOFF.md
python3 scripts/build_release.py --out V13_HISTORY_MILITARY_SKILL.zip
```

`build_release.py`生成包含全包的确定性ZIP和逐文件SHA；已通过GitHub Actions执行固定版Cangjie原版 `cangjie.py compile --output single` 作为独立的编译结构核查。该原版编译产物**不是**最终融合主SKILL，且编译器所需 `verified.yaml` **不代表通过V3**。Nuwa模型、场景正文及全部源参考均随融合SKILL安装包分发。状态见BUILD_MANIFEST.json。

## 不包括
原著EPUB、作者独特语言模板、实际作战危险流程、未经验证史实保证、第三方文学评分、普通新聊天原生安装证明。原工程历史失败和检查点仍保留在根仓库供追溯，不妨碍用户直接创作。

## 唯一入口与验证证据

正式安装时必须**只使用这一目录**；`nuwa-theme/TOPIC_OPERATIONS.md`为主题参考，不单独安装，不得与原版Cangjie编译结果并列触发。GitHub Actions构建`v13-writing-skill-build.yml`提供完整ZIP及仓颉原版编译日志，日志中可区分编译成功与文学验证未执行。见仓库`v13_e/` 的E01—E08逐轮证明和`BUILD_MANIFEST.json`的明确豁免项。
