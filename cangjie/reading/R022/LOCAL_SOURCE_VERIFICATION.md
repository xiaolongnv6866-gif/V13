# V13 R022｜用户私有原著来源审计与文学证据边界

- 源EPUB为用户上传的`/mnt/data/铁血残明 (柯山梦) (z-library.sk, 1lib.sk, z-lib.sk).epub`，文件27764568 bytes，完整SHA256 `9100bbcdb9f52bcd5458cbda92e16b646489efbc00df5161ed568ebac83ffbaf`，原ZIP完整`ZipFile.testzip()==None`。不上传版权原书、句段、抄录或可复原文本到GitHub。
- 严格以OPF narrative ordinal281—320主键定位40章，原spine297—336、原ZIP`OEBPS/Text/chapter288.html`—`chapter327.html`；与独立冻结的`sources/metadata/tiexuecanming_v13_spine.csv`逐章核对原成员字节SHA、路径和段落数。
- 每章使用`lxml.html.fromstring(raw).xpath('//body//p')`以及`text_content().strip()`读取从首段至末段真实原XHTML正文，共**2169**个非空段落。原40章元信息序列FNV32 `4981dd11`，本地原书与GitHub冻结索引一致。工具只算哈希不等于全读；本轮另对原章情节逐段审读并撰写每章不同的人物选择和事件链。
- 精读章281,282,283,285,286,289,290,291,293,295,298,300,301,302,303,306,307,311,315,320（20章）各取原首/中/末段SHA256；其余20章FULL_TEXT_READ各取真实中段SHA。**40份实际原章收据、80个不可逆原段落定位**，`ordinal/paragraph_index/paragraph_sha256\\n`FNV32 `47d26b4e`，私有原EPUB与公开索引相符。精读和全读不双计。
- B内容研究另形成40独立逐章观察、六组带竞争解释、失败边界、换叙法损失的案例与连续性角色资源账；仍仅PROVISIONAL。无证据不得宣称“作者每章总这么写”，也不得把虚构历史天候、技术、财政叙述当作一手史料。
- GitHub Actions无法接触私有版权原著，只能验证`SOURCE_STRUCTURE_ONLY`（格式、字段、来源元数据一致性、FNV、非空解释），真实文学理解与原创写作技能尚不可由CI独立证明。A私有原始来源真实性局部PASS，B仍PROVISIONAL，C独立新输入效益NOT_RUN；原版Adler整书质量门未结束、R042用户确认未完成、Nuwa Phase1未启动、认证SKILL0、R006封存盲测`SEALED_NOT_RUN`。
