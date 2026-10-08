# V13 R008｜私人原著锚点校验边界
- 私有EPUB完整SHA256=`9100bbcdb9f52bcd5458cbda92e16b646489efbc00df5161ed568ebac83ffbaf`，于本轮重新计算，ZIP CRC检查未发现坏项。
- OPF实体spine16—55；叙事 ordinal 001—040；ZIP内部chapter7.html—chapter46.html；40份真实原文独立章sha与R002记录相同。
- 逐章XHTML原始 `lxml.html` `//body//p` 非空段落总数**2712**，净段落文字**163896**字符。章节正文已按段落逐章阅读，后附40个事件/选择/世界变化记录。对含插图或标题的其他body文本仍应查看，不把 `p` 文本等同绝对全部正文范围。
- 本地原著顺序的 `ordinal|spine|path|chapterSHA|paragraphs\n` 全40行组合 SHA256为 `862eb3543852b9e4f645eedcf5e33d2536e848a36e8f485e7a9b5e7a3dc68478`；本地全部2712条段落哈希清单合并SHA256为 `715edfae89bb2c9ed67de9985db092e807c22ea35a513c6a56f0feeba5e962f9`。此摘要是对私有文本的来源完整性说明，不是公开保存的小说正文。
- 逐章收据40份，`FULL_TEXT_READ`30份、`CLOSE_READ`10份；重点编号1/20/29/31/32/33/35/37/39/40；公开存60处段落SHA，均来源于私有原文。重点机制皆为`PROVISIONAL`，不存在已认证SKILL。
- GitHub公开runner只能核对R002元数据和收据结构，不能直接取得原著私人EPUB；若新会话私有原件缺失，不得声称重新直接审读章节。要私有核验可使用 `scripts/validate_r006_protocol.py --receipts cangjie/reading/R008/tiexue_receipts.jsonl --source-dir /mnt/data`。 
