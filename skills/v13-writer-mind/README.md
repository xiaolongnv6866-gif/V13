# V13｜Creative Harness 3.0：InkOS结构驱动的原创小说写作SKILL

**唯一写作入口：[SKILL.md](SKILL.md)**

这是对V13默认写作Skill的**结构性重写**，不是在旧Skill上再增加几十条禁令。借鉴开源 InkOS 的 Profile、Composer、专业Skill、Writer、Reviewer、Reviser、Settler、状态与版本分离的工程思想；保留V13自己的《晚明》《铁血残明》研究、历史军事知识、作者明确决定、原创失败证据。

**重点区别**：InkOS提供软件运行时；本仓现在提供一个兼容AgentSkills标准的Skill入口、按任务加载的专业参考模块与一个使用Python标准库的同题版本留存工具。并**没有**因此自动安装InkOS、获得其多智能体框架、数据库事务、模型后台作业或改变语言模型参数。不要混淆结构借鉴和已有软件能力。

## 结构

```text
skills/v13-writer-mind/
├── SKILL.md                   # 唯一入口：Profile + Composer + 写作/审稿/修订/结算
├── README.md                  # 使用方法和验证边界
├── references/
│   ├── CREATIVE_ENGINE.md     # 实际文学选择与写法，不是评分清单
│   ├── CONTEXT_AND_STATE.md   # Protected/Compressible、Canon/候选分离
│   ├── ITERATION_PROTOCOL.md  # 固定退婚等同题反复实写并累计作者反馈
│   └── HISTORICAL_LONGFORM.md # 陈启明历史军事长篇的专用资料路由
├── scripts/
│   └── scene_lab.py           # 同题锁、不可覆盖的版本、人工反馈与稿间diff
├── knowledge/                # 历史全库研究、来源地图（原材料保留）
└── laboratory/               # 旧的原创练习与失败证据（原材料保留）
```

## 在ChatGPT等对话工具里直接用

先读取完整 [SKILL.md](SKILL.md)，再按任务加载其要求的references及源材料。不需要调用不存在的InkOS后台服务。用户要写退婚就按`same-scene-lab`直接写同一场的下一版本，承接已知前稿和作者评价；只要作品，不用先交流程。要求写《陈启明》时，再加载 `novels/chen-qiming/PROJECT_BIBLE.md` 和批准的正史材料。

跨聊天框必须恢复**相同稿件与反馈**，而非只转述“要精彩、少AI味”。Repo里没有查到的候选/用户反馈不能伪装已保存。

## 同题训练的可运行工具

需要Python 3.10+，无第三方依赖。先把用户批准的场景锁写成 `/path/to/prompt.md`；把完整新稿写成 `/path/to/draft.md`。

```bash
python3 skills/v13-writer-mind/scripts/scene_lab.py init \
  --root training/scene_lab --case tuihun --prompt /path/to/prompt.md

python3 skills/v13-writer-mind/scripts/scene_lab.py submit \
  --root training/scene_lab --case tuihun --draft /path/to/draft.md \
  --hypothesis "让另一个当事人先采取行动，而不是等待主角解释"

python3 skills/v13-writer-mind/scripts/scene_lab.py feedback \
  --root training/scene_lab --case tuihun --version V001 \
  --file /path/to/user-feedback.md --verdict mixed

python3 skills/v13-writer-mind/scripts/scene_lab.py submit \
  --root training/scene_lab --case tuihun --draft /path/to/v2.md \
  --hypothesis "重新安排现场行动与受损关系"

python3 skills/v13-writer-mind/scripts/scene_lab.py compare \
  --root training/scene_lab --case tuihun --before V001 --after V002

python3 skills/v13-writer-mind/scripts/scene_lab.py verify \
  --root training/scene_lab --case tuihun
```

脚本只记录锁定题目、稿件哈希、父版本与人工反馈，不生成作品、不代替作者判断；既不会改写Canon，也不能证明真实文学水平提升。

## 仍使用的V13研究资产

- [全库跨领域研究综述](knowledge/WHOLE_REPO_SYNTHESIS.md)、[源文件地图](knowledge/FULL_REPO_SOURCE_ATLAS.json)
- [真实原著正例索引](../../training/literary_capability_v1/SOURCE_CASE_INDEX.md)
- [陈启明唯一Canon](../../novels/chen-qiming/PROJECT_BIBLE.md)
- 旧 `skills/v13-history-military/`、`skills/v13-storycraft/` 作为资料，不再作为默认写作流程。

## 可核实状态

已完成：重写Skill，拆分专业参考、加入同题训练工具、保留旧材料和历史验收边界。

尚需实际作品证明：退婚同题的用户认可连续提升、新题迁移、千章篇幅历史军事长篇质量。旧试写未经作者认可、非真正陌生盲测；GitHub文本和脚本提交不等于模型获得持久参数能力。

验收以**读起来真正精彩的原创故事**为准，而不是新增多少文件、通过多少次工程测试。
