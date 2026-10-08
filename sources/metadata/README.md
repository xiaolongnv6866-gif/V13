# V13 EPUB 叙事目录元数据

R002 已在本独立 V13 项目使用用户真实提供的两本 EPUB，重建完整 OPF spine→叙事 ordinal CSV；正式审计见 [R002](../../runs/R002.md) 和 [SOURCE_MANIFEST](../../SOURCE_MANIFEST.md)。

- `wanming_v13_spine.csv`：588个spine项目、571个叙事章、17个非叙事项目。
- `tiexuecanming_v13_spine.csv`：551个spine项目、532个叙事章、19个非叙事项目。
- 字段包含真实ZIP内部路径、title、逐文件SHA256、字符数、段落数、叙事布尔值与零缺失连续ordinal。
- 卷界、年表、序、引子、插图及空白占位都保留为非叙事项目，不能丢失。
- 这些仅是结构元数据，**不代表已完成全文阅读**；不在公开GitHub存小说原文。

后续阅读必须使用叙事 `narrative_ordinal` 和 `epub_path` 双重定位，按章节范围真实读取正文。
