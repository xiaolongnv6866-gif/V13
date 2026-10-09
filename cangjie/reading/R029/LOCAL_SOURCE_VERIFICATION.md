# R029｜《晚明》原始用户EPUB私有来源核验记录

- 用户私有原始EPUB完整SHA256：`a8f3b43dcd496822cd384ac8e9aa85f7dc374f8430f06c6f8321c26825093082`；ZIP逐成员CRC `testzip() PASS`；私有文件不上传GitHub。
- 有效OPF叙事序号 **441—480**、spine **456—495**；对应 `OEBPS/Text/Chapter_0453.xhtml`—`Chapter_0492.xhtml`，40个各不重复的原ZIP成员，各原始字节SHA与冻结 `sources/metadata/wanming_v13_spine.csv` 一致。
- 已真正接触40章首至尾实际原文，总 `2050` 个非空XHTML正文段落、`144214` 个可见正文字符；归一化与冻结R006一致：`lxml.html.fromstring(raw)` → `//body//p` → `text_content().strip()` → UTF-8 SHA256，文内若有非P正文也不能以索引代替阅读。
- 20章CLOSE_READ，包括441首章、460中位、480末章，各自**首段／真实关键场景段／末段**三项SHA；另外20章FULL_TEXT_READ各一个中段SHA。共80处私有原文不可逆定位，详细索引及独立收据见R029目录。
- 原章成员SHA序列FNV1a32 **`d05bdb81`**；80段落SHA序列FNV1a32 **`fa6c9f60`**。两者在私有原EPUB重新计算，之后在GitHub收据再独立复算一致。
- 为防止“SHA真实但不支持所写文学主张”，首轮生成后对照原场景把8处重点段落定位改至更有相关性的正文位置，替换前旧聚合校验值 `bfcef788`，替换后新值 `fa6c9f60`；新位置均来自原章原文，不曾更改EPUB字节或冻结R006协议，错误草稿在Git对象暂存并未推送到main。
- 公开GitHub Actions仅验证 `SOURCE_STRUCTURE_ONLY`，**无法读取私有全文**；“来源真实性A私有PASS”取决于本次原文件实际重算，不能由公开CI推断全文理解。**B** 每章叙事解释与反向研究仍 `PROVISIONAL`；**C** 独立原创写作效用 `NOT_RUN`，任何作者意图或文学成效不冒称已通过独立评审。
- Stage0整书Adler四步、R042用户确认与后续女娲Phase1均未执行；R006密封试题未开启，Skill认证0，R007—R024老质量债务仍按风险抽审。
