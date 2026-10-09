# V13 R055｜真实V2新输入原创新场面测试索引

- **先冻结输入**：commit `27fa253c133ad892f67f14c6236716835d7c365d`，JSON blob `dd8ac1d2b110fb22df221c24a2f558d3510c0c96`。冻存后才撰写实际新场面。无需原著情节复现。
- **运行方式**：Stage1.5 V2允许的纸面walkthrough；A/B均为同一Agent在本轮创作，不是新模型独立生成的两次复现；也不是Stage4宿主执行或R056 V3任务增益。
- **真实产物**：19份输入 × 2段不同A/B场面 = 38段；每组还包括状态账、未知条件、逐项原预注册验收片段。每组原输出路径固定，下列均应被脚本逐项读取核验。
- **质检**：精确检查57条预注册条件都保留同名并在实际A/B或状态账能找到被引用的文本证据；重复运行检查器应得到相同SHA，而不是宣称文学质量评分等于机器校验。另提供四个故意破坏输入的负例：缺少B、假片段、引入V1 REVIEW、偷写V3通过，均须被校验器拒绝。

|预注册任务|原创情景|关联V1通过的方法候选|真实walkthrough保存位置|
|---|---|---|---|
|WM-01|身份入口|WM-f01, WM-p08, WM-p03|`tests/v2/results/WM-01.json`|
|WM-02|长期合作者异议|WM-f02, WM-p01|`tests/v2/results/WM-02.json`|
|WM-03|授权与资源|WM-f06, WM-p12, WM-p08|`tests/v2/results/WM-03.json`|
|WM-04|商货与到账|WM-f04, WM-p05, WM-p12|`tests/v2/results/WM-04.json`|
|WM-05|有限知情|WM-f08, WM-p07, WM-p19|`tests/v2/results/WM-05.json`|
|WM-06|功劳与家庭成本|WM-f10, WM-p04|`tests/v2/results/WM-06.json`|
|WM-07|治理试验|WM-f12, WM-p20, WM-p21|`tests/v2/results/WM-07.json`|
|WM-08|普通人独立意愿|WM-f14, WM-p14|`tests/v2/results/WM-08.json`|
|WM-09|亲历与重述|WM-f13, WM-p23|`tests/v2/results/WM-09.json`|
|TX-01|污名与新评价|TX-f01, TX-p01, TX-p11|`tests/v2/results/TX-01.json`|
|TX-02|申请受理审核|TX-f02, TX-p03, TX-p12|`tests/v2/results/TX-02.json`|
|TX-03|属员纠正负责人|TX-f05, TX-p09, TX-p04|`tests/v2/results/TX-03.json`|
|TX-04|账面与在手物资|TX-p05, TX-p21, TX-f16|`tests/v2/results/TX-04.json`|
|TX-05|等级与权限|TX-f08, TX-p08, TX-p07|`tests/v2/results/TX-05.json`|
|TX-06|三方有限协作|TX-f12, TX-p13, TX-p06|`tests/v2/results/TX-06.json`|
|TX-07|对手与平民目标|TX-f09, TX-p14, TX-f10|`tests/v2/results/TX-07.json`|
|TX-08|申请与本人选择|TX-f11, TX-p20, TX-p07|`tests/v2/results/TX-08.json`|
|TX-09|现场与记录版本|TX-f13, TX-p19, TX-p17|`tests/v2/results/TX-09.json`|
|TX-10|留下未履行义务|TX-f16, TX-p21|`tests/v2/results/TX-10.json`|

## 由本轮直接得出的范围

只有以上真实列入并通过本轮状态/判停审计的**47个不同framework/principle**可以记为`V2_WALKTHROUGH_PASS_LIMITED`。其余V1 PASS未入题11个标明未运行；39条V1 REVIEW继续阻断；90项case/ce/term为reference候选。文学B仍PROVISIONAL，原创能力V3未核验，Skill0。不要据此回答“AI已经稳定生成更高水平作品”。
