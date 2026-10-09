# 《铁血残明》｜R053 Stage1.5候选保全索引（仅合并与重复审查草案）

status: COMPLETE_96_RAW_UNITS_V1_V2_V3_NOT_STARTED
source_epub_sha256: 9100bbcdb9f52bcd5458cbda92e16b646489efbc00df5161ed568ebac83ffbaf
upstream_cangjie_sha: a28de55ba881b9928956a55048f743f7a9e3b23e
source: `books/tiexuecanming/candidates/{frameworks,principles,cases,counter-examples,glossary}.md`

## 基线和删除禁令

独立保留96条，五类数量framework17、principle22、case16、counter-example21、term20。各候选的`TX-<原id>`跨书唯一标识不改变来源原始ID，`130`对项目共享原文段落坐标，不构成独立来源；共有`177`个候选指向的不同私有原段落n/p位置，涉及`74`章（无额外语义认证）。本轮**没有自动删去任何一条候选**；疑似重复登记为场景关系，真正内容去重/verified必须等R054来源核证与R055/R056的合法执行、任务效用审查后处理。所有96项`RETAIN_RAW_PENDING_V1_V2_V3`。

## 全体候选原始出处和任务映射

|稳定ID|提取器|标题|独立Stage0任务|源书坐标|原文坐标重叠候选|初始流向|
|---|---|---|---|---|---|---|
|TX-f01|framework|旧名声、当场能力、外部评价的三层身份连续性|TX-01, TX-08|n001/p20; n002/p36; n201/p54; n201/p56|TX-p01, TX-p11, TX-c01, TX-c09|RAW/V1待核|
|TX-f02|framework|办事从会背文书到得到第三方认可的多级路径|TX-02, TX-03|n030/p33; n055/p30; n055/p31; n055/p32|TX-f03, TX-p02, TX-p03, TX-c03, TX-ce02|RAW/V1待核|
|TX-f03|framework|地方调解与官署利益交错的制度现场|TX-01, TX-02|n008/p2; n030/p33; n055/p31|TX-f02, TX-p02, TX-p03, TX-c03, TX-ce02|RAW/V1待核|
|TX-f04|framework|名义官职与跨部门实际约束的不等式|TX-02, TX-06|n145/p29; n315/p40; n420/p2; n485/p23|TX-f07, TX-p13, TX-p16, TX-c12, TX-c13, TX-ce13, TX-g14|RAW/V1待核|
|TX-f05|framework|首领的知识缺口如何交给专业属员修正|TX-03, TX-05|n081/p59; n165/p1; n174/p23; n174/p24|TX-f17, TX-p04, TX-p08, TX-p09, TX-c04, TX-c08, TX-ce08, TX-g08|RAW/V1待核|
|TX-f06|framework|账面储备、临时替代与后来对账的三段资源链|TX-04, TX-10|n114/p27; n114/p29; n531/p8|TX-f16, TX-p05, TX-p21, TX-c06, TX-ce06, TX-ce21|RAW/V1待核|
|TX-f07|framework|外来上级命令与本地原方案相撞的局部重规划|TX-05, TX-06|n315/p40; n320/p36; n420/p2; n485/p23|TX-f04, TX-p13, TX-p16, TX-c12, TX-c13, TX-ce13, TX-g14|RAW/V1待核|
|TX-f08|framework|岗位待遇、实际权限与专业承认之间的区分|TX-03, TX-05|n361/p34; n361/p35; n361/p36; n380/p31|TX-f15, TX-f17, TX-p07, TX-p08, TX-c11, TX-ce15, TX-g11|RAW/V1待核|
|TX-f09|framework|对立阵营与弱势人物的独立利益空间|TX-06, TX-07|n250/p31; n305/p50; n350/p69|TX-f10, TX-p13, TX-p14, TX-c10|RAW/V1待核|
|TX-f10|framework|公共事件的成果与普通人战后生活双后果账|TX-04, TX-07, TX-08|n350/p69; n490/p28; n505/p8|TX-f09, TX-f14, TX-p14, TX-p18, TX-ce18|RAW/V1待核|
|TX-f11|framework|家户与属员是否同意须脱离命令单独审视|TX-01, TX-08|n015/p49; n161/p65; n370/p19; n527/p30; n527/p31|TX-f15, TX-f17, TX-p07, TX-p20, TX-c15, TX-ce07, TX-ce20|RAW/V1待核|
|TX-f12|framework|把猜测、对方未知和事后判断分成有限视角|TX-06, TX-07|n430/p58; n430/p59; n500/p24; n500/p25|TX-p16|RAW/V1待核|
|TX-f13|framework|现场事件、报功文本与编辑再传播的层级差|TX-02, TX-09|n175/p23; n175/p24; n244/p30; n526/p82; n526/p87; n531/p25; n531/p26|TX-p10, TX-p19, TX-c14, TX-ce19|RAW/V1待核|
|TX-f14|framework|地点技术条件与计划外现场障碍的回写|TX-03, TX-04|n285/p5; n285/p6; n490/p28|TX-f10, TX-p18, TX-ce18|RAW/V1待核|
|TX-f15|framework|制度扩大后反对者的真实生存空间|TX-05, TX-08|n161/p65; n380/p31; n527/p29; n527/p30|TX-f08, TX-f11, TX-f17, TX-p07, TX-p20, TX-c15, TX-ce07, TX-ce20|RAW/V1待核|
|TX-f16|framework|信誉想象到新承诺形成，不能直接跳至兑现|TX-04, TX-09, TX-10|n530/p41; n531/p8; n532/p47; n532/p49|TX-f06, TX-p21, TX-c16, TX-ce21|RAW/V1待核|
|TX-f17|framework|属员提案—首领裁量—未来责任归属的会商机制|TX-03, TX-05, TX-08|n174/p23; n174/p24; n361/p35; n361/p36; n527/p30; n527/p31|TX-f05, TX-f08, TX-f11, TX-f15, TX-p08, TX-p09, TX-p20, TX-c08, TX-c11, TX-c15, TX-ce15, TX-ce20|RAW/V1待核|
|TX-p01|principle|旧声誉与新帮助可以同时存在|TX-01|n001/p20; n012/p28|TX-f01, TX-c01|RAW/V1待核|
|TX-p02|principle|背会制度文件不能等同实际运用|TX-02|n030/p33; n055/p32|TX-f02, TX-f03, TX-p03, TX-c03, TX-ce02|RAW/V1待核|
|TX-p03|principle|报文先发未必赢得正式确认|TX-02, TX-09|n055/p30; n055/p31; n055/p32|TX-f02, TX-f03, TX-p02, TX-c03, TX-ce02|RAW/V1待核|
|TX-p04|principle|公开训话不能替代领导实际知识|TX-03, TX-04|n081/p29; n081/p59|TX-f05, TX-c04|RAW/V1待核|
|TX-p05|principle|仓库账面计划与实际物资分开|TX-04|n114/p27; n114/p29|TX-f06, TX-c06, TX-ce06|RAW/V1待核|
|TX-p06|principle|调查所得和亲见证人区别|TX-06|n127/p11; n127/p44|—|RAW/V1待核|
|TX-p07|principle|屈从压力与自愿选择不同|TX-05, TX-08|n161/p65; n380/p31|TX-f08, TX-f11, TX-f15, TX-ce07|RAW/V1待核|
|TX-p08|principle|制度条文允许被专业下属质疑|TX-05|n165/p1; n361/p35; n361/p36|TX-f05, TX-f08, TX-f17, TX-c11, TX-ce08, TX-ce15, TX-g08|RAW/V1待核|
|TX-p09|principle|属员方案不能写成上司复读机|TX-03|n174/p23; n174/p24|TX-f05, TX-f17, TX-c08|RAW/V1待核|
|TX-p10|principle|出版的费用与编辑异议分别保留|TX-09|n175/p23; n531/p25; n531/p26|TX-f13|RAW/V1待核|
|TX-p11|principle|公共表扬与私人控诉互不注销|TX-01, TX-08|n201/p54; n201/p56|TX-f01, TX-c09|RAW/V1待核|
|TX-p12|principle|正式签任命册不等于顺利履职|TX-02, TX-05|n213/p2; n213/p5; n213/p17|TX-ce12|RAW/V1待核|
|TX-p13|principle|不同权力方有各自同意边界|TX-06|n250/p31; n315/p40; n485/p23|TX-f04, TX-f07, TX-f09, TX-c13, TX-ce13, TX-g14|RAW/V1待核|
|TX-p14|principle|普通人的遭遇不能被大事件抹掉|TX-07|n305/p50; n350/p69; n505/p8|TX-f09, TX-f10, TX-p18, TX-c10, TX-ce18|RAW/V1待核|
|TX-p15|principle|对立官员主张不得冒充作者一致立场|TX-05, TX-06|n386/p39; n386/p45; n386/p49|—|RAW/V1待核|
|TX-p16|principle|发令归属和情报准确是两项不确定|TX-06|n420/p2; n430/p59; n475/p25|TX-f04, TX-f07, TX-f12, TX-c12, TX-g14|RAW/V1待核|
|TX-p17|principle|传闻中的身份与正式公告区分|TX-09, TX-06|n475/p8; n475/p10|—|RAW/V1待核|
|TX-p18|principle|预制方案不能取消现场劳动摩擦|TX-03, TX-07|n490/p28; n505/p8|TX-f10, TX-f14, TX-p14, TX-ce18|RAW/V1待核|
|TX-p19|principle|实绩核对不可被文书虚增建议代替|TX-09|n526/p82; n526/p87|TX-f13, TX-c14, TX-ce19|RAW/V1待核|
|TX-p20|principle|请求清单各项都需要独立答复|TX-08, TX-05|n527/p30; n527/p31|TX-f11, TX-f15, TX-f17, TX-c15, TX-ce20|RAW/V1待核|
|TX-p21|principle|信用估价与兑现结果不得混同|TX-04, TX-10|n530/p41; n531/p8; n532/p49|TX-f06, TX-f16, TX-c16, TX-ce21|RAW/V1待核|
|TX-p22|principle|个人生存焦虑与大范围风险推测并列|TX-07, TX-06|n103/p16; n103/p18|—|RAW/V1待核|
|TX-c01|case|旧身份在街坊围观中先于新主人形成判断|TX-01|n001/p16; n001/p20; n001/p30|TX-f01, TX-p01|RAW/V1待核|
|TX-c02|case|谷小武提出主角没有考虑的另一条道路|TX-03, TX-06|n051/p26; n051/p29; n051/p30; n051/p40|—|RAW/V1待核|
|TX-c03|case|抢报功名被幕友的权力现实当场反驳|TX-02, TX-09|n055/p30; n055/p31; n055/p32|TX-f02, TX-f03, TX-p02, TX-p03, TX-ce02|RAW/V1待核|
|TX-c04|case|赞助者追问训练理由后主角私下承认知识空缺|TX-03, TX-05|n081/p51; n081/p55; n081/p59|TX-f05, TX-p04|RAW/V1待核|
|TX-c05|case|幕友给出处理申诉的方案，知县接受但后果未示|TX-02, TX-05|n095/p28; n095/p35; n095/p36|—|RAW/V1待核|
|TX-c06|case|预备仓无粮但现场仍有临时供给|TX-04|n114/p27; n114/p29; n114/p31|TX-f06, TX-p05, TX-ce06|RAW/V1待核|
|TX-c07|case|守城结束后退役请求把荣誉转为现银压力|TX-04, TX-08|n131/p40; n131/p41; n131/p42; n131/p43|—|RAW/V1待核|
|TX-c08|case|江帆递交规程并提出安排，庞雨当面要求修改|TX-03|n174/p22; n174/p24; n174/p25|TX-f05, TX-f17, TX-p09|RAW/V1待核|
|TX-c09|case|高官褒奖尚未说完，私人控诉打断其正面定论|TX-01, TX-08|n201/p52; n201/p54; n201/p56|TX-f01, TX-p11|RAW/V1待核|
|TX-c10|case|小娃子的去向选择打破对手阵营的单一视角|TX-07|n305/p29; n305/p34; n305/p37; n305/p50|TX-f09, TX-p14|RAW/V1待核|
|TX-c11|case|战功晋升方案被属官追问指挥界限|TX-05|n361/p30; n361/p34; n361/p35; n361/p36|TX-f08, TX-f17, TX-p08, TX-ce15, TX-g11|RAW/V1待核|
|TX-c12|case|总督追问号令来源，却只得到部分澄清|TX-06|n420/p2; n420/p9; n420/p11|TX-f04, TX-f07, TX-p16, TX-g14|RAW/V1待核|
|TX-c13|case|曹变蛟拒绝空泛协作，之后作出有限同意|TX-06|n485/p7; n485/p8; n485/p23|TX-f04, TX-f07, TX-p13, TX-ce13|RAW/V1待核|
|TX-c14|case|功劳记录的虚增建议被当事人撕毁拒绝|TX-09|n526/p82; n526/p85; n526/p87|TX-f13, TX-p19, TX-ce19|RAW/V1待核|
|TX-c15|case|士兵请假接家眷：附条件许可与同袍援助两条线|TX-08, TX-07|n527/p30; n527/p31; n527/p42; n527/p47|TX-f11, TX-f15, TX-f17, TX-p20, TX-ce20|RAW/V1待核|
|TX-c16|case|周月如在账务风险与同事担忧中落笔新责任|TX-10, TX-04|n532/p39; n532/p43; n532/p46; n532/p49|TX-f16, TX-p21, TX-ce21|RAW/V1待核|
|TX-ce01|counter-example|后台倚赖被人事变动打断|TX-02|n013/p34; n013/p52; n013/p56|—|RAW/V1待核|
|TX-ce02|counter-example|先递报文不保证取得功劳|TX-02, TX-09|n055/p30; n055/p31; n055/p32|TX-f02, TX-f03, TX-p02, TX-p03, TX-c03|RAW/V1待核|
|TX-ce03|counter-example|现场应募热度不等于真实到岗|TX-03, TX-04|n080/p19; n080/p67; n080/p68|—|RAW/V1待核|
|TX-ce04|counter-example|职位威压不能解决知情不足|TX-03, TX-06|n082/p1; n082/p10; n082/p31|—|RAW/V1待核|
|TX-ce05|counter-example|有限物证不能被政治压力自动补足|TX-06, TX-09|n102/p2; n102/p6; n102/p10|—|RAW/V1待核|
|TX-ce06|counter-example|预备仓落空但替代供给有限存在|TX-04|n114/p27; n114/p29; n114/p31|TX-f06, TX-p05, TX-c06|RAW/V1待核|
|TX-ce07|counter-example|从属者的服从未必出于自愿|TX-05, TX-08|n161/p5; n161/p65; n161/p66|TX-f11, TX-f15, TX-p07|RAW/V1待核|
|TX-ce08|counter-example|严密军律的内部张力不是已发生崩溃|TX-05, TX-08|n165/p1; n165/p5; n165/p80|TX-f05, TX-p08, TX-g08|RAW/V1待核|
|TX-ce09|counter-example|资源收入预估无法抹掉真实现金流压力|TX-03, TX-04|n174/p13; n174/p37; n174/p39|—|RAW/V1待核|
|TX-ce10|counter-example|高回报说辞不能消灭家庭现金需求|TX-04, TX-08|n180/p12; n180/p20; n180/p29|—|RAW/V1待核|
|TX-ce11|counter-example|公众赞誉不能清除私人关系旧债|TX-01, TX-08|n202/p3; n202/p20; n202/p33|—|RAW/V1待核|
|TX-ce12|counter-example|签了任命册也有尚未核清的职位空缺|TX-02, TX-03, TX-05|n213/p2; n213/p5; n213/p18; n213/p21|TX-p12|RAW/V1待核|
|TX-ce13|counter-example|共同军事目的不能取代盟友独立同意|TX-06|n315/p35; n315/p40; n485/p8; n485/p23|TX-f04, TX-f07, TX-p13, TX-c13, TX-g14|RAW/V1待核|
|TX-ce14|counter-example|胜利发生不表示战后责任已经关闭|TX-04, TX-07|n357/p49; n357/p58; n357/p60|—|RAW/V1待核|
|TX-ce15|counter-example|新士官饷等会制造新的权责歧义|TX-05|n361/p34; n361/p35; n361/p36|TX-f08, TX-f17, TX-p08, TX-c11, TX-g11|RAW/V1待核|
|TX-ce16|counter-example|请旨中的责任推让会产生实际时间差|TX-02, TX-06|n424/p9; n424/p11; n424/p25|—|RAW/V1待核|
|TX-ce17|counter-example|有银不能当即兑换出需要的粮食|TX-04, TX-06|n431/p10; n431/p17; n431/p18; n431/p19|—|RAW/V1待核|
|TX-ce18|counter-example|纸面后勤方案无法覆盖实际劳动现场|TX-03, TX-07|n490/p28; n490/p30; n505/p8|TX-f10, TX-f14, TX-p14, TX-p18|RAW/V1待核|
|TX-ce19|counter-example|把文书写得合理可能扭曲真实发生的事|TX-09|n526/p82; n526/p85; n526/p87|TX-f13, TX-p19, TX-c14|RAW/V1待核|
|TX-ce20|counter-example|离队许可不能消除家眷和结保责任|TX-08, TX-10|n527/p30; n527/p31; n527/p38; n527/p39|TX-f11, TX-f15, TX-f17, TX-p20, TX-c15|RAW/V1待核|
|TX-ce21|counter-example|写下财务承诺不等于履行与兑付|TX-04, TX-10|n531/p8; n532/p47; n532/p49|TX-f06, TX-f16, TX-p21, TX-c16|RAW/V1待核|
|TX-g01|term|皂隶|TX-01, TX-08|n001/p8; n239/p69|—|RAW/V1待核|
|TX-g02|term|申明亭|TX-02, TX-08|n008/p1; n009/p3|—|RAW/V1待核|
|TX-g03|term|申详|TX-02, TX-06, TX-09|n055/p11; n523/p8|—|RAW/V1待核|
|TX-g04|term|报功|TX-02, TX-09|n139/p34; n526/p22|—|RAW/V1待核|
|TX-g05|term|班头|TX-01, TX-03|n080/p13; n407/p57|—|RAW/V1待核|
|TX-g06|term|壮班|TX-03, TX-07|n080/p8; n308/p5|—|RAW/V1待核|
|TX-g07|term|守备|TX-02, TX-03, TX-06|n145/p27; n161/p3|—|RAW/V1待核|
|TX-g08|term|军律|TX-05, TX-08|n165/p1; n440/p8|TX-f05, TX-p08, TX-ce08|RAW/V1待核|
|TX-g09|term|工食|TX-04, TX-07, TX-08|n058/p13; n356/p30|—|RAW/V1待核|
|TX-g10|term|军饷|TX-04, TX-07|n302/p8; n481/p34|—|RAW/V1待核|
|TX-g11|term|士官|TX-03, TX-05|n361/p34; n443/p30|TX-f08, TX-c11, TX-ce15|RAW/V1待核|
|TX-g12|term|百总|TX-03, TX-05|n160/p26; n443/p21|—|RAW/V1待核|
|TX-g13|term|勤王|TX-06, TX-04|n425/p4; n430/p47|—|RAW/V1待核|
|TX-g14|term|军令|TX-02, TX-06|n315/p40; n420/p2|TX-f04, TX-f07, TX-p13, TX-p16, TX-c12, TX-ce13|RAW/V1待核|
|TX-g15|term|战报|TX-09|n244/p6; n486/p10|—|RAW/V1待核|
|TX-g16|term|时刊|TX-09, TX-03|n175/p1; n185/p49|—|RAW/V1待核|
|TX-g17|term|银庄|TX-04, TX-10|n408/p15; n530/p6|—|RAW/V1待核|
|TX-g18|term|贴票|TX-04, TX-10|n388/p46; n532/p20|—|RAW/V1待核|
|TX-g19|term|军功|TX-01, TX-09|n266/p5; n505/p30|—|RAW/V1待核|
|TX-g20|term|塘报|TX-06, TX-09|n352/p78; n437/p27|—|RAW/V1待核|

## 候选碰撞不能当确认重复

- `f`框架可能把数场重新安排为叙事工艺；`p`原则来自小说人物或研究者推断；`c`案例标记`fictional_narrative_case`暂时枚举扩展；`ce`失败/担忧/未知结果须不同分类；`g`历史词汇仅是书中含义，不自动真实。
- 例：`TX-f06 / TX-p05 / TX-c06 / TX-ce06`在n114涉及同一仓储现场，但框架的多时态流程、原则的存量区分、案例的当场行动和反例的边界不等于四份独立证据；保留层次待R054。
- `TX-f08 / TX-c11 / TX-ce15`在n361涉及岗位待遇/权限争论：出现当场解释不等于长期有效，不能把反例标题的“可能风险”写成已发生失败。
- `TX-p19 / TX-c14 / TX-ce19`共同讨论n526的记录分歧，实际不实建议在当前书中被拒绝；绝不能把这个反例当历史上确实发表的失实战报。
- `TX-f16 / TX-p21 / TX-c16 / TX-ce21`涉及期末信用义务，源版本停止于落笔，继续兑现/失败均未见。
- 场景锚点共用不会自动覆盖TX-01—TX-10全部陌生输入要求；`R053_SOURCE_OVERLAPS.tsv`逐对保留源位置，后续核真实性与意义范围。
- 所有术语中的`author_definition`空字段不许被当作作者亲自授课。禁止用文学解读生成可实施军务、胁迫、金融策略。旧14错引与未解决的Stage0文学质量债原样保存。

## 后续输入缺口与关口

本轮仅完成**准备工作：候选合并、追踪、共享段落重复标注、阶段0任务覆盖草案**；不写V1/V2/V3决定（R054—R056）；不输出`verified.md`、`rejected`、正式术语词典或能力卡，不启动Nuwa。R054必须重新复核原始人物行动、意见归属与原书结果，历史制度须外证；R055合法新题，R056基线增益。所有内容B PROVISIONAL、C NOT_RUN、Skill0。
