# V13 R021｜本地私有原著实际核读与公开不可逆定位说明

- 原始用户 EPUB：`/mnt/data/晚明 (柯山梦) (z-library.sk, 1lib.sk, z-lib.sk).epub`；原文件size`17123520`字节，SHA256`a8f3b43dcd496822cd384ac8e9aa85f7dc374f8430f06c6f8321c26825093082`，ZIP CRC完整（testzip None）。该文件以及任何长段正文从未上传GitHub。
- 有效叙事 ordinal281—320 对应原始 OPF spine296—335、原ZIP`OEBPS/Text/Chapter_0293.xhtml`—`Chapter_0332.xhtml`。逐章原字节 SHA256、章内非空正文段落数量和成员路径与 R002 冻结索引逐项完全一致。
- 私有原著解析规则`lxml.html.fromstring(raw).xpath('//body//p')`、`text_content().strip()`去掉空白；40章从第一非空段实际接触至最后一段，正文合计**2223个原非空段**，不以目录、片段检索、生成式摘要或源hash冒充全文阅读。
- 对所选`CLOSE_READ`章281,282,283,285,288,291,293,295,297,299,301,303,305,307,309,311,313,316,318,320，保存原文第1/中/末段SHA256；另外20个`FULL_TEXT_READ`章每章保存原文中间段SHA256。总计40份独立正文全读收据、20份重点精读、**80个**实际原文段落哈希。所有定位仅记录序号和不可逆SHA，不公开原著内容。
- 私有原EPUB和GitHub索引分别独立计算逐章`ordinal|spine|member_path|chapter_sha|nonempty_paragraphs\\n`FNV1a32为 **b69dfa88**；`ordinal/paragraph_index/paragraph_sha256\\n`FNV1a32为 **2fa4eb5f**。
- 文学证据B不仅有SHA：另著40个实际事件和自主目标、六组包含竞争解释、反事实及失效边界的文字研究，另有阶段性的人员、学校、财税、家属与命令长期连续性账。文学机制仍**PROVISIONAL**，未通过整书 Adler 阶段0。GitHub公开 CI 不可读取私有原书，只能做`SOURCE_STRUCTURE_ONLY`校验；CI为绿不能证明真实文学理解或陌生创作能力。
- C原创SKILL测试`NOT_RUN`、证书数0，R006密封盲测`SEALED_NOT_RUN`，原版女娲Phase1仍不可启动。若以后需要原章引句或图片证据须在用户私有空间回查，版权书文不上传。
