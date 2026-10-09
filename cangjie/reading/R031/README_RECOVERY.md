# V13 R031 本地可复核研究检查点（非 GitHub 正式 PASS）

本包服务于现有唯一仓库 https://github.com/xiaolongnv6866-gif/V13 ，不得建立新仓库、不得从R001重来。

目标：原用户《晚明》有效叙事第481—520章。已产出40份正文事件与来源收据、20篇独立重点场景精读、82处原始段落SHA、2处跨章相反证据和人物/财政/组织/司法连续性账；内容质量审计与本地验证脚本在本包中。用户的受版权保护EPUB不包含在包内。

一、读取正式远程 CURRENT_ROUND.json/ROUND_LEDGER.csv/PROGRESS.md；若R031仍NOT_STARTED，则从此包按原始用户EPUB继续核验并提交证据，不得直接增加40章。若远程状态已变化，先检查差异并合并，不覆盖。

二、可在拥有原始《晚明》EPUB的环境里运行：

    python3 scripts/validate_r031_reading.py --source-dir /path/to/private_epub_directory

不提供 --source-dir 只检查字段结构，不可宣称实际段落真实匹配。需要同时运行原冻结 `scripts/validate_r006_protocol.py --receipts cangjie/reading/R031/wanming_receipts.jsonl --source-dir /path/to/private_epub_directory`（该脚本在正式V13仓库中）。

三、整理正式证据提交。待该提交所有R006/R031/全部历史GitHub Actions完成SUCCESS后，原子更新CURRENT_ROUND、ROUND_LEDGER、PROGRESS和两本PIPELINE_STATE，推进到R031 PASSED/R032 NOT_STARTED。正式PASS提交触发的Actions仍需全部成功，随后远程回读。若任何门失败，R031应保持未通过状态。

四、文学B仍PROVISIONAL、原创C NOT_RUN、已认证Skill0；后续整书Adler、R042用户门与Nuwa Phase1不得提前触发。保留之前R007—R024旧质量债务风险抽审。

**尚未执行远程提交是实际阻断，并非已完成待后台自动运行。** 用户下一次“继续”仍应优先恢复R031，不能启动R032。
