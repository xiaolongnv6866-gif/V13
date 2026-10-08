# R017｜仅公开校验说明，不含原著原文

- 私有原EPUB路径：`/mnt/data/晚明 (柯山梦) (z-library.sk, 1lib.sk, z-lib.sk).epub`，原文件共17,123,520字节，SHA256 `a8f3b43dcd496822cd384ac8e9aa85f7dc374f8430f06c6f8321c26825093082`，ZIP CRC完整（testzip None）。此路径是用户本次私有环境，不是GitHub可下载路径。
- 有效叙事 ordinal 201—240，原OPF spine215—254，ZIP 章路径 `OEBPS/Text/Chapter_0212.xhtml`至 `Chapter_0251.xhtml`；40个原ZIP成员 SHA256与 R002 冻结元数据完全一致。
- 私有源 `lxml.html.fromstring(raw).xpath('//body//p')`，对 `text_content().strip()` 非空正文段自首至末完整查看，40章1920段，20章重点近景研究，其余20章完整阅读，去重后40章。80个段落 SHA256来自对应实际原文UTF-8归一化内容，不公开原句。
- 原文计算的段落SHA顺序摘要：对每一原文 `ordinal/paragraph_index/paragraph_sha256\\n` 依阅读序号施行32位 FNV1a，结果 `da1bad61`。初次将本地数值转为GitHub不可逆来源锚点时发现两处手工抄录差异（ordinal229、237），以私有源重新逐行核对后修正，公开记录保存的是修正后的真实 SHA。
- A通过只意味着来源、ZIP完整性与位置可查；自动化测试不证明文学解释（B），而任何B假说也不能代替原创写作SKILL在陌生题上的独立效益测量（C）。GitHub Actions无法读取用户私有EPUB，只能验证公开SOURCE_STRUCTURE_ONLY。研究B为PROVISIONAL；C=NOT_RUN，R006 sealed heldout未开启。
- 版权原著文字和危险场景执行细节均不上传仓库。
