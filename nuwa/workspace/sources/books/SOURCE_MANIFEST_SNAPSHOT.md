# V13 原著唯一来源清单（R002 正式校验通过；不含版权正文）

| 作品 | 原始完整 EPUB SHA256 | EPUB字节 | ZIP项 | OPF路径 | manifest项 | spine项 | 叙事序号范围 | 非叙事项 | ZIP CRC |
|---|---|---:|---:|---|---:|---:|---|---:|---|
| 《晚明》 | `a8f3b43dcd496822cd384ac8e9aa85f7dc374f8430f06c6f8321c26825093082` | 17,123,520 | 610 | `OEBPS/content.opf` | 607 | 588 | 1—571 | 17 | PASS |
| 《铁血残明》 | `9100bbcdb9f52bcd5458cbda92e16b646489efbc00df5161ed568ebac83ffbaf` | 27,764,568 | 611 | `OEBPS/content.opf` | 609 | 551 | 1—532 | 19 | PASS |

## R002 正式来源索引

- `sources/metadata/wanming_v13_spine.csv`：588个真实OPF spine项目，其中571个叙事章；原样UTF-8/CRLF文件SHA256：`4c927d36439b6c26421bbe6fa85e0e6f975f4da8c245d61c3316e6f02f153f8b`。
- `sources/metadata/tiexuecanming_v13_spine.csv`：551个真实OPF spine项目，其中532个叙事章；原样UTF-8/CRLF文件SHA256：`39c7db42cba0437e4624315f746e3f9fe3401fe5898feec9a2f461b98e4e2af4`。
- 每行含 `spine_index`、真实EPUB ZIP内部路径、章节标题、正文字符数、非空段落数、内部文件完整SHA256、`is_narrative_chapter`、`narrative_ordinal`；仅上传元数据，不上传小说正文、原始EPUB、图片。
- 实际直接读取原EPUB `META-INF/container.xml` 定位OPF，验证 OPF manifest idref—spine 映射、ZIP路径存在、路径不重复、每个目标文件可读取且CRC通过。两个叙事 ordinal均逐个连续且无重漏。

## 卷界与特殊条目

- 《晚明》卷界spine索引：11（第1卷后接ordinal 1）、63（第2卷后接52）、118（第3卷后接106）、169（第4卷后接156）、286（第5卷后接272）、503（第6卷后接488）。卷界文件的章节标题为空且为非叙事项。
- 《晚明》spine 4—9为卷前技术/附录类内容，spine 10为序、11为卷界；不是叙事ordinal 1。全书打印章号按卷重置；部分标题采用汉字大写章号。
- 《铁血残明》spine 0—15为封面、插图、地图、年表、引子等，spine 145、403为插图；spine 550标题“第535章”只有20个正文字符，为空壳/占位，**不算已存在的第533个叙事章**。
- 《铁血残明》可见印刷章号重复、跳号及回跳，故 `narrative_ordinal`（原书spine依次识别）是唯一研究定位码；印刷“第N章”只作为标题元数据，不能据此证明文本缺章。
- 非叙事项并不等于后续Stage0完全不读：原书序、引子、年表等仍须在相应阅读阶段检查其理解价值；此处仅定义1103个叙事章节计数。

**重要限制**：R002只验证文件真实性、结构与章节位置；并没有完成任意一章的深入文学审读或建立创作SKILL。V10—V12旧成果未进入此次索引。原著本体仅保留在用户会话的私有附件中。
