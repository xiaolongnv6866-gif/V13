# V13 R024｜私有原版《铁血残明》来源验证与限制

- 用户上传的完整EPUB 2026-10-09再次核验：SHA256 9100bbcdb9f52bcd5458cbda92e16b646489efbc00df5161ed568ebac83ffbaf；ZIP testzip None。
- 本轮原ZIP effective narrative 321—360 = OPF spine 337—376，原ZIP OEBPS/Text/chapter328.html 至 chapter367.html，40个member SHA与冻结R002 mapping对应，叙事序号不按书内印刷章号（本范围334印为324、336印为236、339印为389）。
- 逐个原XHTML body非空p均完整读出及核验，40章2220段，约153035原p文本字符；正文仅保存于不可公开私有工作区 /mnt/data/v13_r024_private，公开仓库不含小说句段。
- CLOSE_READ: 321,324,328,329,331,333,336,337,340,341,343,344,345,346,347,350,352,355,357,360 (20章，各锚定首/中/末3段)；另外20章各留一原中段SHA。80个私有原文段落SHA FNV1a32 12642d3d；40章member索引FNV1a32 8dd29619。本地原member逐字节校验与原段hash计算，公开CI只有 SOURCE_STRUCTURE_ONLY。
- A私有来源真实核验PASS；B文学解释仅PROVISIONAL，仍需整书Adler与独立反向抽审；C独立原创任务增益NOT_RUN；skill认证0；R006密封测试SEALED_NOT_RUN；Nuwa Phase1 NOT_STARTED。
