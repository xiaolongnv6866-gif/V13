# 能力路由与跨会话实际交接

任务分类→读最少必要模块：规划(01+02)、写正文(03+04+05)、军政制度(02+06)、精修(07+05)、源方法追溯(08+capabilities)、跨会话(05+脚本)。

## 文件约定
一个小说项目最少有 PROJECT_BIBLE.md（终局、章节分卷树、人物关系与世界边界）、STATE.json（事件证据）、CHAPTER_XXX.md正文、NEXT_SCENE.md（下场驱动力）、EDITOR_LOG.md（修订差分）。每次写后更新这几项；未确认事实记UNKNOWN不填想象。

## 跨聊天交接
在用户选择的可用本地Python环境执行：
python3 scripts/validate_state.py examples/chaoxun/STATE.json
python3 scripts/build_handoff.py --state examples/chaoxun/STATE.json --skill SKILL.md --last-chapter examples/chaoxun/CH05.md --out V13_HANDOFF.md
将V13_HANDOFF.md与适用references、最新正文发给新会话。新会话先验证状态，不从独立作品“记忆”里补造事件；不得假称GitHub链接会自动安装到聊天宿主。

## 反滥用
能力路由自动在内部执行：写了正文后不输出“调用了哪条规则”的广告；需研究时才引用V1候选标签。回忆过往项目要以实际正文/状态账为准，不因为同主题就串错不同小说项目。