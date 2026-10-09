# R033 私有原著来源核验，非公众附件

- 原始EPUB SHA256：`a8f3b43dcd496822cd384ac8e9aa85f7dc374f8430f06c6f8321c26825093082`；压缩包CRC和40个原始OPF XHTML均重新核对。
- 有效叙事序号521—560，对应spine537—576、`OEBPS/Text/Chapter_0534.xhtml`—`OEBPS/Text/Chapter_0573.xhtml`；**不能套用纸面分卷印刷章号**。
- 40章连续读完从首到尾全部1892个非空`//body//p`，共147774个可见字符；原文只存在本地私有EPUB，GitHub不含受保护正文。
- 各章成员SHA和82处段落SHA均已用原始文本计算（`lxml.html.fromstring(raw).xpath('//body//p')`, `text_content().strip()`）；20章重点精读，2组跨章FOUND反证。
- 40章成员序列FNV1a32 `21953130`；82段落锚点序列FNV1a32 `a7e0af45`。
- A=PRIVATE_SOURCE_VERIFIED，不等于文学论断已经被独立证实；B=PROVISIONAL，C=NOT_RUN，Stage0全书Adler和R042用户门未完成。
