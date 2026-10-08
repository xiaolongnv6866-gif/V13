# R015｜私有EPUB来源性验证

- 来源：用户当前会话原始EPUB，《晚明》全文件长度17123520字节，SHA256 `a8f3b43dcd496822cd384ac8e9aa85f7dc374f8430f06c6f8321c26825093082`，ZIP.testzip()为None。
- 原版原文阅读入口：`/mnt/data/晚明 (柯山梦) (z-library.sk, 1lib.sk, z-lib.sk).epub`（**本地私有路径，不存在于公开GitHub**）。
- 有效叙事ordinal161—200映射到spine175—214，原ZIP成员 `OEBPS/Text/Chapter_0172.xhtml` 至 `Chapter_0211.xhtml`；按R002冻结CSV核对40章sha。
- 原始XHTML `lxml.html.fromstring(raw)`，`doc.xpath('//body//p')` 非空段落逐个正文阅览，总计2137段；逐段 SHA256按 `xhtml_visible_text_trim_whitespace_v1`。40份收据，18个CLOSE_READ，22个FULL_TEXT_READ，76原段不可逆SHA锚点；FNV32按 `ordinal/paragraph_index/paragraph_sha256\\n` 次序得 `cf341ba9`，原始私有重算与公开收据核对。该一致性检查单独不证明机器真正理解每个段落，须结合逐章分析和反证。
- 源真实性A：私有原EPUB全文件校验和ZIP/成员SHA/段落SHA通过；GitHub Actions公开部分必须声明`SOURCE_STRUCTURE_ONLY`。
- 文学解释B：逐章情节、人物自主目标、作者叙法、反例及失败边界为PROVISIONAL。C原创能力任务增益NOT_RUN。
- R006密封测试题未查看；未经同意没有外部付费；没有复制受版权保护小说正文。
