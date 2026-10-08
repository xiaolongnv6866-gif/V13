# V13 R012｜《铁血残明》原文来源真实性说明
- 用户私有EPUB完整SHA256=`9100bbcdb9f52bcd5458cbda92e16b646489efbc00df5161ed568ebac83ffbaf`，本轮对原用户文件直接计算，ZIP `testzip()`无坏成员；原文件27764568字节。
- 有效叙事ordinals 081—120、OPF spine96—135、ZIP内部`OEBPS/Text/chapter87.html`至`chapter126.html`。全部40个ZIP成员原始字节SHA与R002源登记相同。
- 实际查看每个章节的全部原文XHTML段落及从第一到最后的场面叙事；固定lxml `//body//p`非空段落总数**2745**；40个不同的具体事件-人物选择-叙述作用收据，12章CLOSE_READ（081,083,088,091,094,100,103,105,109,110,116,120，包含首、中、末章），另28章FULL_TEXT_READ，全文阅读不重复计算。
- 64处原著真实非空段落的SHA256位置可在用户私有原文件按`text_content().strip()`逐项复核；按`ordinal/index/paragraphSHA256\\n`串接的私有SHA256链校验值=`606e899616a0a1b7a6943ae6cb2f26c629e72b1ba88232a00f3f2c0098c5b0ff`。链摘要仅作传输一致性验证，不能替代文学理解。
- 公开GitHub不存用户原著长段、整章或受版权保护的故事表述，仅保存本次原创抽象叙事研究和SHA，公开GitHub Actions仅可核对`SOURCE_STRUCTURE_ONLY`、R002原字节chapter SHA/路径/段数/收据内部一致性，不能声称其获得用户私有小说文本。
- 所有机制只PROVISIONAL，整书Stage0的Adler四步与R042用户审核还未发生，Nuwa Phase1尚未开展，密封R006盲测未打开，不宣称原创写作SKILL的独立质量。
