# V13 R003｜固定仓颉原版 CLI doctor 运行记录

执行方式：GitHub Actions `V13 R003 pinned Cangjie doctor`，在Ubuntu GitHub-hosted runner检出固定上游 commit 后运行原版 `python3 .v13-cangjie-upstream/scripts/cangjie.py doctor`；并执行V13控制器的`python3 scripts/validate_round_integrity.py`。**不是本地原版CLI运行**。
- 实际 Actions 工作流：https://github.com/xiaolongnv6866-gif/V13/actions/runs/37829650448
- GitHub job ID：`113491372280`
- 对应V13 commit：`aa9b98de24ea03c5c6ace95eb571e20818d16c4f`
- 上游SHA实测：`a28de55ba881b9928956a55048f743f7a9e3b23e`
- run status/conclusion：`completed / success`
- 原版 doctor 退出码：0（GitHub step success）
- V13 89轮完整性检查：step success

## GitHub 原版doctor stdout（逐行抄录，去除Action时间戳）
```text
cangjie-tools v2.5.0
python: 3.12.3
  [ok] yaml
  [warn] tiktoken 缺失(可选)
  [ok] jsonschema
  [ok] schemas/capability-bundle.schema.json
  [ok] schemas/registry-entry.schema.json
  [ok] schemas/contracts/source-document.schema.json
doctor: PASS
```

## 真实V13控制器stdout
```text
PASS V13 guardrails: 89 unique rounds, 89 ledger rows, cursor agreement, 29 reading rounds, 1103 non-overlapping chapters, 10 user gates, source fingerprints
```

## 环境分离（本地探针，不冒充原版doctor）
本地容器 Python `3.13.5`，PyYAML `6.0.3`，jsonschema `4.26.0`，tiktoken `MISSING`（可选）；本地git存在但github.com DNS解析失败，未能直接克隆上游。此限制由GitHub Actions原版运行补齐，未来新环境仍需重新doctor。

备注：原版CLI执行了真实固定commit版本，未重新实现/改写原版doctor逻辑；此处归档stdout及可核的GitHub Actions链接，无虚构local doctor日志。历史原著正文阅读=0/1103，非本轮目标。
