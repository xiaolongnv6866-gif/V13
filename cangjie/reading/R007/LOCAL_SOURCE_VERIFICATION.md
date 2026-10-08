# R007 私有EPUB逐章来源核验说明
- 私有EPUB：《晚明》完整SHA256=`a8f3b43dcd496822cd384ac8e9aa85f7dc374f8430f06c6f8321c26825093082`（R002已定版，本轮重新在容器计算一致）。
- 单轮实际查看：ordinal1—40，共40个从第1到最后一段的XHTML正文；完整顺序包含对白、转换场景、专门非叙事脚注等内容。原文不上传GitHub。
- 书内印刷章名只是视觉标题；唯一主键是spine12—51，真实ZIP路径从`OEBPS/Text/Chapter_0009.xhtml`至`Chapter_0048.xhtml`，所有章SHA取私有ZIP原始字节。
- 非空段落索引方法：`lxml.html.fromstring(raw)`，`doc.xpath('//body//p')`遍历，`x.text_content().strip()`过滤非空。公开收据每条`body_paragraph_count`与`observed_paragraph_count`均按本轮实际原文逐章查看，留独立内容性事件链。SHA来自原始非空段落UTF-8字节；不贴原文。
- 额外精研：编号001、020、040是预先设定首/中/末；再补034—035的并列视角差异和039的账目反例。上述6章的假说尚未经全书横向验证，因此`verification_state=PROVISIONAL`，不冒充已被确认的独立SKILL。
- 局限：GitHub自动程序能验证收据格式、R002章节路径/章SHA/计数，不能单独看到私有EPUB的段落SHA。本轮在私有容器中重新散列段落；原文还在用户本会话，后续环境若缺原著不可仅凭收据宣称重新读过。
- 当前40章只为Stage0整书理解建立证据；未进行第041章阅读、不涉及《铁血残明》正文，尚无真正独立的原创技能性能测评。
