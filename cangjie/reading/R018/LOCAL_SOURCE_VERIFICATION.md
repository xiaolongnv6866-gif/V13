# V13 R018 私有原著与GitHub不可逆段落定位验证

- 用户原始 EPUB 文件：`/mnt/data/铁血残明 (柯山梦) (z-library.sk, 1lib.sk, z-lib.sk).epub`，完整原文件大小 **27,764,568字节**，SHA256 `9100bbcdb9f52bcd5458cbda92e16b646489efbc00df5161ed568ebac83ffbaf`，ZIP.testzip()结果 **None**，OPF spine长度551。
- 本轮以OPF叙事有效键 `tiexuecanming:201..240` 定位：spine217—256，原ZIP `OEBPS/Text/chapter208.html`—`chapter247.html`。从原私有EPUB逐章 `lxml.html.fromstring(raw).xpath('//body//p')` 取 `text_content().strip()` 非空段共 **2650**。不存在通过目录标题代替正文的计数。
- 对每章原始ZIP成员逐个计算 SHA256，并按有效序号、spine index、ZIP path、member SHA、paragraph count 拼接生成FNV32 = `2fd10f8d`，与仓库冻结 `sources/metadata/tiexuecanming_v13_spine.csv` 独立重算 **相同**。
- 40章确实在本轮打开原文供逐段文学研究，包含此前输出过长导致的完整补核章节210和214；重点精研20章在私有原文首段、正文中段、末段各设SHA256，其他20章在正文中段各设不可逆SHA256，一共**80个**源段位置。私有EPUB与GitHub递交的锚点 `ordinal/index/sha\\n` FNV32 = `095e5bfb`。
- 用户原版权EPUB正文**没有**上传GitHub。本地材料（源文件/片段）与公开研究/定位标识分离，公开 Actions 只能检验 `SOURCE_STRUCTURE_ONLY` 和内容分析字段，不能读取私有EPUB，也不能用绿色CI证明本模型已理解全文。
- 本批文学假说PROVISIONAL；原创SKILL在陌生原创新输入上的独立实际质量提升 NOT_RUN；认证SKILL 0；R006密封题库SEALED_NOT_RUN，Cangjie原版Adler bookwide质量门/用户确认及Nuwa Phase1都未提前执行。
