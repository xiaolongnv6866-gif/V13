# V13 R030｜用户私有《铁血残明》原 EPUB 的真实性复核

- 来源：用户提供EPUB，原始SHA256 `9100bbcdb9f52bcd5458cbda92e16b646489efbc00df5161ed568ebac83ffbaf`，本轮Python独立哈希重算匹配；ZIP `testzip() = None`，全员CRC PASS。
- 通过原OPF与冻结R002元数据确认**40个**有效叙事章序号441—480、原spine458—497。真实路径441为`OEBPS/Text/chapter449.html`、480为`OEBPS/Text/chapter489.html`，中途XHTML文件编号有跳过，必须逐行以R002完整映射为准，不能套单一+8公式。
- 原文接触与字符：**2101个非空`//body//p`正文段落**、157868个可见中文正文字符。原文件字节与40章原SHA匹配；20章CLOSE_READ各首／支持／末三处定位，其余20章FULL_TEXT_READ各一处；合计80个段落原文SHA256。段落规范：`lxml.html.fromstring` / `//body//p` / `text_content().strip()` / UTF8字节SHA256。
- 真实40成员的序列FNV1a32 `754094fe`；80段落定位序列FNV1a32 `3753923f`，本地原EPUB与公开GitHub不可逆收据经第二次独立重算一致。
- 暂存检查发现第461有效叙事章p19的64位SHA末尾有一位抄录遗漏，重新按用户原书算得准确值后修复所有暂存来源文件；此前错误没有推送main。另对468—469章的支撑段落做了跨章动作匹配：468 p46是杨光第依靠坐骑身体的触感，469 p1是次章触觉回响；避免只选机械中点。
- A：本地私有书全文件与位置真实性核验PASS；公开GitHub CI**只能SOURCE_STRUCTURE_ONLY**，不能把哈希字段自动说成对文学掌握的证明。B：40章独立事件、20重点文学解释与六组跨章反向研究，全部PROVISIONAL。C：独立陌生原创任务尚NOT_RUN。
- 原用户EPUB文本、受版权保护的正文或危险行为细节不上传公共GitHub。整书原版Cangjie Adler和R042确认未完成，Nuwa Phase1未启动，R006密封盲测封存；Skill认证仍0。
