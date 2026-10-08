# V13 R014｜原著私有全文来源校验及异常处理

- 《铁血残明》用户提供的私有原始 EPUB 路径：`/mnt/data/铁血残明 (柯山梦) (z-library.sk, 1lib.sk, z-lib.sk).epub`；大小 **27764568字节**，整书SHA256=`9100bbcdb9f52bcd5458cbda92e16b646489efbc00df5161ed568ebac83ffbaf`，ZIP CRC `None`。
- V13 R002真实OPF叙事ordinal121—160=40个有效章，**原spine136—144，146—176**，中间**spine145**是`OEBPS/Text/chapter136.html`空正文分隔文件，不能当第130章。121—129内页`chapter127.html`—`chapter135.html`；130—160内页`chapter137.html`—`chapter167.html`。原40个ZIP member byte SHA与R002均逐一对应。
- **本轮实际侦测并修正来源错位**：原始阅读辅助脚本早期曾对130之后按简单文件号顺推，看到空白后重新检查R002，发现从ordinal130起真实章节路径多偏移一位；已经修正脚本并从实际原著补读真正152—160、按正确有效叙事序号复核各章。没有将空白页计作阅读；此错误在研究报告中保留以便后续审计。
- 40章原件用`lxml.html.fromstring(raw).xpath('//body//p')`逐段取`text_content().strip()`后总计**2426非空段落**，章节SHA、段落数与R002完全一致。逐章有独立的事件因果、参与者自主选择、叙述信息差、后续问题研究材料，而不是自动计算原文SHA就叫全文阅读。
- 重点精读 **14章（121、122、127、129、130、135、140、142、148、152、153、155、157、160）**，其余26章`FULL_TEXT_READ`。来源SHA256 paragraph anchors **68处**，一章至少1处，重点章首/中/末各3处，按`SHA256(xhtml_visible_paragraph.trim().encode('utf8'))`与私有原件定位。校验码：按每章ordinal/index/SHA逐项计算FNV32为`cd98332d`，仅用于比较私有源和传输记录，不等于文学理解证明。
- GitHub公开runner无法访问原书 EPUB，故只能`SOURCE_STRUCTURE_ONLY`核对R002路径/成员SHA/收据/源目录；私人原文SHA/语义阅读在本轮独立执行，文学假说全部`PROVISIONAL`。
- 本批未做R042整书Adler用户确认、Nuwa Phase1或R006保留盲测，原创写作Skill仍0认证；不发布版权原句长段，危险冲突仅分析叙事后果。
