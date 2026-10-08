# V13 R003｜Cangjie 原版输入合同（阶段0前置，不是BOOK_OVERVIEW）
**原版事实源**：GitHub `kangarooking/cangjie-skill@a28de55ba881b9928956a55048f743f7a9e3b23e`，cangjie.version=`2.5.0`。每次执行均应打开原版 `SKILL.md`、`methodology/00-overview.md`、`methodology/01-stage0-adler.md`、`templates/BOOK_OVERVIEW.md.template`，不得把此合同代替原文。精确Git blob锁参见 `sources/upstream-lock.json`。

## 原著输入（R002真实EPUB）
|字段|晚明|铁血残明|
|---|---|---|
|作品|《晚明》|《铁血残明》|
|作者（EPUB OPF creator）|柯山梦|柯山梦|
|实际EPUB SHA256|`a8f3b43dcd496822cd384ac8e9aa85f7dc374f8430f06c6f8321c26825093082`|`9100bbcdb9f52bcd5458cbda92e16b646489efbc00df5161ed568ebac83ffbaf`|
|本版叙事ordinal|1—571|1—532|
|OPF date原始值（仅电子书元数据）|`2020`、`2021-11-24`|`2024-04-07`、`2025-01-26`|
|**首次出版年**|**未核实，不能把OPF日期当正式出版年**|**未核实，不能把OPF日期当正式出版年**|
|源头位置|`sources/metadata/wanming_v13_spine.csv`|`sources/metadata/tiexuecanming_v13_spine.csv`|

## 任务与输出目的
- 用途：从两部历史题材小说分析可追溯、可验证的原创长篇叙事创作机制，供新作品策划、正文、修订与压力测试使用；不是复刻作者剧情、人物或专属文风。
- 书籍类型：文学作品（非工具书）。应从真实场景及前后因果中验证可迁移机制；原版所说的“方法论单元”不能凭情节标题臆造。
- 原版两书先行：用户已明确指示研究两本，属于授权的批量项目，仍须对每本独立做Stage0及阶段确认。两本不能共用一个BOOK_OVERVIEW蒙混。
- single/pack：**临时建议**选 `--output auto --purpose workflow` 走跨书实际创作流程；single与pack最终必须等 R068/R069 分别展示输出模式决策再经用户确认。预推荐不是已批准的输出形式。
- 现阶段不得调用 `compile`，因为尚无经过三重验证的 Bundle；不以doctor PASS代替真正可用的SKILL。

## 阶段0所需工作与不可跳过的门
1. 依 `methodology/01-stage0-adler.md` 全文阅读，对每部做 **结构（主旨与3—7骨架）→解释（术语、5—15命题、论证链）→批判（立场盲点、前提与反对意见）→应用（可执行任务、不可执行内容）**，分别写原版 `BOOK_OVERVIEW.md`。
2. 必须建立独立于候选池的原书关键任务表：task_id、任务、可定位文本来源、交付物、重要性依据、缺口。缺证据记未核查，不能先假定机制存在。
3. R007—R035处理全文阅读的1103个叙事章；R036—R042处理Stage0四步和用户关口。此R003只是来源及运行前检验，**文学全文审读0/1103**。
4. Stage0结束展示每书BOOK_OVERVIEW给用户明确确认（R042）后才进入原版阶段1；任何缺少批判、来源、用户确认的情况均不宣告阶段通过。
5. 环境依赖：Python>=3.10、PyYAML必需；tiktoken/jsonschema由原版doctor标记为可选。doctor还检查三份schema是否存在。
6. 多agent：实际环境若无原版要求的并行子agent，则按原版许可串行5个提取器，分别保存各自产物，绝不冒充并行或独立Agent测试。

## 环境边界
- **本地**：Python 3.13.5；PyYAML 6.0.3 可导入；jsonschema 4.26.0 可导入；tiktoken 缺失（原版可选）。此为本地探针，不是原版CLI doctor。
- 本地容器未能解析github.com，无法原样git clone固定版本。为完成“真实doctor”，本轮在V13 GitHub Actions runner上 checkout精确固定commit并执行上游 `python3 scripts/cangjie.py doctor`，原始stdout/exit code另行归档。
- R004 Nuwa Phase0档位/来源/路径决策仍待用户；不得在本轮代替用户作决定。
