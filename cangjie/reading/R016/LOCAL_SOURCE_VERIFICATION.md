# V13 R016｜私有来源真实性检查记录

- 原始用户EPUB：`/mnt/data/铁血残明 (柯山梦) (z-library.sk, 1lib.sk, z-lib.sk).epub`（只存在于私有执行环境）。全文件大小27764568字节，SHA256 `9100bbcdb9f52bcd5458cbda92e16b646489efbc00df5161ed568ebac83ffbaf`，ZIP CRC `testzip=None`。
- 实际OPF有效叙事章161—200，对应spine177—216，ZIP原成员 chapter168.html—chapter207.html，原章bytes SHA与R002 `sources/metadata/tiexuecanming_v13_spine.csv`一致；两次“第197章”印刷标题分别是有效ordinal197和198。
- 按冻结 `xhtml_visible_text_trim_whitespace_v1`：`lxml.html.fromstring(raw)` → `//body//p` → `text_content().strip()`，剔除空白，40章共2510非空正文段。每章逐段阅读原始文字，记录独立人物目标、场面和应回收的责任，不依赖题名或AI生成摘要。
- 原文选段UTF-8 SHA256定位总数80：CLOSE_READ 20章各3锚点，FULL_TEXT_READ 20章各1锚点。按序 `ordinal/paragraph_index/paragraph_sha256\\n` 的FNV32核查 `4c010a0b`，由私有原著重算与公开收据一致。该结构性一致性本身**不能**当文学理解证明，必须另看40章独立内容审查。
- GitHub Actions平台无原著私有EPUB，来源性检查最多只能标记`SOURCE_STRUCTURE_ONLY`，不能声称远程公开Runner逐句阅读。文学机制均仅PROVISIONAL，新原创SKILL增益测试NOT_RUN。R006密封盲测未接触。
- 本文件不包含原著任何长引文或危险现实操作细节。
