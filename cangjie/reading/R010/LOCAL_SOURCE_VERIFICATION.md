# V13 R010｜私有原著来源与公开收据分门审计

- 用户私有《铁血残明》EPUB SHA256 `9100bbcdb9f52bcd5458cbda92e16b646489efbc00df5161ed568ebac83ffbaf`，本轮在同一执行环境完整重新算出，ZIP CRC检查为`None`，与V13 R002固定登记一致。
- OPF真正叙事ordinal 041—080，spine56—95；ZIP文件分别为`OEBPS/Text/chapter47.html`—`chapter86.html`。40个原始内页文件SHA256全部与R002索引一致。
- 使用 `lxml.html.fromstring(raw).xpath('//body//p')` 的去空非空段落总计**2847**；该计数只是审计索引，不等于单凭扫描就叫文学全读；本轮另有40份内容性事件链、人物自主和文本观察，以及重点场景反例。
- 此轮真实逐章查看041—080全部章正文；归档30份FULL_TEXT_READ与10份CLOSE_READ（焦点：041、055、057、060、062、065、067、073、079、080），共60处私有原文段落SHA256定位。不包含任何公开原著长段或现实危险操作说明。
- 独立以私有原书40章相关段落计算的 `ordinal/index/paragraphSHA256` 序列FNV32为**9fd05197**；把Github暂存收据同一顺序计算应得到相同指纹，验证锚点传输一致。FNV32只作源锚点传输核验，不是密码学身份证明，也不代表文学机制已最终通过。
- GitHub Actions中只有R002元数据、真实章路径与chapterSHA、逐章收据、哈希锚点及文学笔记，因公开runner不含私有EPUB，须诚实报告`SOURCE_STRUCTURE_ONLY`。本地用户原件不可得时不能仅依Github文件重新声称已读。
- 所有文学机制为PROVISIONAL，新输入创作改进与整书Adler四步、R042用户门均未完成。
