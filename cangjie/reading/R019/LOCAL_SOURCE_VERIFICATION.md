# V13 R019｜私有原始《晚明》EPUB真实性及非叙事卷界复核

- 用户私有源EPUB：`/mnt/data/晚明 (柯山梦) (z-library.sk, 1lib.sk, z-lib.sk).epub`。原字节长度17,123,520，完整SHA256 `a8f3b43dcd496822cd384ac8e9aa85f7dc374f8430f06c6f8321c26825093082`；ZIP `testzip()==None`。原始版权全文仅保留私有，不上传GitHub。
- 依原OPF实际非叙事过滤规则，ordinal241—271对应spine255—285、ZIP`OEBPS/Text/Chapter_0252.xhtml`—`Chapter_0282.xhtml`。其后spine286的`Chapter_0283.xhtml`是**非正文卷标题**，不能算有效章；ordinal272—280对应spine287—295、ZIP`Chapter_0284.xhtml`—`Chapter_0292.xhtml`。因此“241—280”绝不可直接选择40个连续电子书文件。
- 从用户原EPUB取各有效原始XHTML字节，SHA256逐章与冻结的`sources/metadata/wanming_v13_spine.csv`中`chapter_sha256`对齐；40章`spine_index/path/chapter_sha256/nonempty_paragraphs`的序列FNV1a-32为`b7f9732c`，私有源和GitHub冻结索引独立核算一致。
- 全文读取口径为`lxml.html.fromstring(raw).xpath('//body//p')`，逐段`text_content().strip()`后丢弃纯空白；原始40章共**2133个非空正文段落**。逐章真实阅读原文，从第一段到末段，并在被输出截断时单独复核，不用目录、模型记忆或生成性摘要代替。
- **20章CLOSE_READ**各记录首、中、末3个`sha256(UTF8段落原文)`，另外**20章FULL_TEXT_READ**各记录原章中段1个SHA，不交叉重复计入章数，总计**80**不可逆定位。按`n/paragraph_index/paragraph_sha256\\n`顺序FNV1a-32摘要`3b82a082`，本地原EPUB与公开收据一致。
- **三门边界**：A=私有原著来源完整性PASS；B=本批章节分析有局部反证，但仅PROVISIONAL；C=独立写作新题效益NOT_RUN。GitHub Runner没有用户的私有EPUB，只能进行`SOURCE_STRUCTURE_ONLY`的结构和序列比对，不能以绿色Actions代替文学理解。
- 原版Cangjie Adler整书Stage0与用户确认门尚未完成；Nuwa Phase1尚未执行；正式原创SKILL认证0；R006预留盲测保持`SEALED_NOT_RUN`。仅研究文学机制、不传播版权书文或危险现实操作方法。
