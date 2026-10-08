# R020｜私有原始EPUB与公开不可逆锚点独立核查

- 输入源：用户上传的`/mnt/data/铁血残明 (柯山梦) (z-library.sk, 1lib.sk, z-lib.sk).epub`，大小`27764568`字节，整文件SHA256`9100bbcdb9f52bcd5458cbda92e16b646489efbc00df5161ed568ebac83ffbaf`，ZIP `testzip() == None`。
- 从原ZIP读取实际有效叙事`241—280`四十个原成员`OEBPS/Text/chapter248.html`至`chapter287.html`，原OPF spine257—296。逐章取原字节SHA并以独立GitHub冻结`sources/metadata/tiexuecanming_v13_spine.csv`核对，`n|spine|path|original_member_sha|paragraph_count\\n`累积FNV32 = **4371963e**（两边相同）。
- 逐章通过原`lxml.html.fromstring(raw).xpath('//body//p')`读取`text_content().strip()`非空段，从每一原章第1至末段完整审读，共**40章、2512非空正文段**。生成私有本地按原段标号的文本查看文件供核验，未经授权未进入GitHub。
- 重点CLOSE_READ的20章为`241,242,243,246,248,250,251,253,254,255,256,258,261,262,263,266,267,268,272,280`，每章首、中、末三个段落SHA256；另外20章FULL_TEXT_READ各取中段一个SHA，**共80个可追溯定位，40章不重复计数**。对`n/paragraph_index/paragraph_sha256\\n`按序FNV1a-32核查得 **93f49811**，私人原段和公开收据相同。
- 研究附逐章独立事件和自主选择记录、六个具有反证/替代叙述损失的专题以及跨章人物/财产/公共法律连续性。公开GitHub Actions只查`SOURCE_STRUCTURE_ONLY`，无法获得用户版权原EPUB，绿色CI本身不是原文语义理解证明。
- 状态门：A用户私有来源真实性PASS；B局部文学解释**PROVISIONAL**，整书Adler和R042用户审核未做；C原创SKILL陌生任务增益**NOT_RUN**，认证SKILL0，Nuwa Phase1未执行；R006封存盲测`SEALED_NOT_RUN`。不得以小说暴力叙事生产现实危险的实施教程。
