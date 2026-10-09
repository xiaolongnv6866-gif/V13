# V13 R028｜用户私有原EPUB真实性与原文定位核验

- 原书：《铁血残明》，用户提供 EPUB，SHA256 `9100bbcdb9f52bcd5458cbda92e16b646489efbc00df5161ed568ebac83ffbaf`。本轮读取前重新计算整个ZIP的SHA、`ZipFile.testzip()`：**CRC PASS**。
- 原始 OPF有效叙事序号 **401—440**，每章一份独立原文文件，路径 `OEBPS/Text/chapter409.html` 到 `OEBPS/Text/chapter448.html`，原始spine **418—457**；冻结R002 `sources/metadata/tiexuecanming_v13_spine.csv` 与40个实际ZIP字节SHA相对应；不能以卷内印刷章号为主键。
- 本批真正接触原文 **40章／2441个非空XHTML正文段／167071个可见字符**；段落规范 `lxml.html.fromstring(raw)` → `doc.xpath('//body//p')` → `p.text_content().strip()`，非空者按1-based编号。每个原章节全文从开头至末段阅读，不用只读哈希冒充分析。
- 20个选择进行CLOSE_READ的章节，各取首段、真实对应场景段、末段3个SHA256；其余20章FULL_TEXT_READ每章1段定位，总计 **80个私有原文SHA256**。原成员清单FNV1a32 **`91dc7c91`**；私有80段定位序列FNV1a32 **`72e4062f`**。
- 本轮额外执行与文字无关的双重来源自查：先由私有原书直接计算80段哈希及上述两组FNV；再在暂存GitHub证据独立复算，发现有效章416第23段HASH有两位字符对调，已在暂存 `tiexue_private_paragraph_anchor_manifest.tsv`、`tiexue_receipts.jsonl`、`tiexue_source_index.csv` 同时纠正；未将错误版本推进main，正确的FNV `72e4062f` 与真实原文完全一致。这是来源性纠错，不是改写原著内容。
- 公开GitHub仅保存不可逆原文哈希及独立文字分析，不保存用户原EPUB或版权正文。公开Actions中的冻结R006协议在未给 `--source-dir` 时只能说明 **SOURCE_STRUCTURE_ONLY**；用户提供的私有源在本轮实际检查才支持来源真实性A。
- **A** 私有原文件与来源锚点已核验；**B** 40章独立解释和20章精读仍 `PROVISIONAL`、不得冒称整书理解；**C** 原创Skill在陌生测试中的效果 `NOT_RUN`。Stage0、R042用户确认、Nuwa Phase1和原R006密封题库都没有越过。
