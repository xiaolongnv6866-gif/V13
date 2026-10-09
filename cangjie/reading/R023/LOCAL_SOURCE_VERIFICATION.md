# R023｜私有用户原版《晚明》来源性A与内容性B分开核验

- 文件`/mnt/data/晚明 (柯山梦) (z-library.sk, 1lib.sk, z-lib.sk).epub`，真实17123520 bytes、SHA256`a8f3b43dcd496822cd384ac8e9aa85f7dc374f8430f06c6f8321c26825093082`、ZIP `testzip() == None`。
- 按原版OPF effective narrative ordinal321—360，对应spine336—375、原ZIP`OEBPS/Text/Chapter_0333.xhtml`到`Chapter_0372.xhtml`。40个原member SHA256逐条对上冻结R002`sources/metadata/wanming_v13_spine.csv`，独立序列FNV1a32`9a726633`。
- 对每个原XHTML采用`lxml.html.fromstring(raw).xpath('//body//p')`取`text_content().strip()`非空段，真实**2129段**；已逐章阅读321—360第一至最后原文段落，并对输出截断的322—325分批重读。保存私有原章全文分段文件于`/mnt/data/v13_r023_private`（不提交）。阅读总正文约**170069中文可见字符**，不是仅靠检查SHA或题目表。
- 20个CLOSE_READ章节为`321,322,323,325,329,331,333,334,337,338,339,340,341,343,344,346,349,351,356,360`，每章留真实原文第一／中间／最后段SHA；另外20个FULL_TEXT_READ章节各保存真实原文中段SHA。总40个去重全文阅读凭据／80原段不可逆SHA256，FNV1a32 `aeabbd4c`，私有原书段落与公开GitHub定位完全一致。
- 本轮以40条独立事件及当事人目标笔记、六组近景比较、反证和替代写法损失、人物财政与民事权利长账进行内容性B审查。B仅PROVISIONAL，未经整书Adler四步骤及独立抽检，不得自称verified。
- GitHub Actions Runner不能访问私有版权原EPUB；公开仓库只提交不可逆摘要和独立文学分析，CI在机器环境最多证明`SOURCE_STRUCTURE_ONLY`（schema、路径、章SHA索引和解释字段逻辑），不能凭绿灯证明真正理解40章或者自称已认证原创SKILL。
- C尚未测试陌生原创任务，`NOT_RUN`。Cangjie Stage0整书和R042用户确认未完成，女娲Phase1未开展，正式skill_certified_count=0、R006密封题库`SEALED_NOT_RUN`，按用户要求每次只执行一轮。
