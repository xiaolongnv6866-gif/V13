# V13 R031｜原始来源私有完整性报告

- 用户提供《晚明》EPUB，整文件SHA256：`a8f3b43dcd496822cd384ac8e9aa85f7dc374f8430f06c6f8321c26825093082`；本次从文件字节重新计算一致。
- ZIP `testzip() = None`（所有成员CRC有效）。
- 按原始OPF叙事序号481—520定位40个XHTML成员，spine496—536，跳过非叙事spine503/Chapter_0500.xhtml。第488个有效叙事章实际是Chapter_0501.xhtml，不可套用卷内显示章号。
- 40章 `//body//p` 非空段落 **1960** 个，正文可见字符 **151789** 个。各章的字节SHA和有效叙事映射另存 `wanming_source_index.csv`。
- 精读章节20章，每章首/真正支持处/末3条锚点；其余20章各1条；跨章FOUND反向锚点2条，合计82条。所有位置使用 `lxml.html.fromstring(raw).xpath('//body//p')` 与 `text_content().strip()`，UTF8编码SHA256，并以私有EPUB原始字节重新计算。
- 40个成员元信息序列FNV1a32 `2289545f`；82个带跨章键的段落定位序列FNV1a32 `39e1af85`。
- 私有来源性A哈希校验完成，不能由此断言模型对每一段都有经过独立认证的文学理解。B文学解释仅 `PROVISIONAL`；C独立原创测试 `NOT_RUN`。
- 确认重点支持位置已回到真实场景：498有效章的职业谈话是p15、501的行军身体负担是p33、520关于陪审制偏私问题是p10。避免选择同章无关段落凑SHA。
- 本地包不含原 EPUB、不含完整章节或原文段落；本地验证不是 GitHub Actions SUCCESS。本轮不可宣称远程 R031 PASSED。
