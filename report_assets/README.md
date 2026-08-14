# report_assets/ · 报告图表资产目录

> 本目录存放**报告 v2 与 PPT/PDF 直接引用**的图表。Day 9（2026-08-12）由心跳任务产出。

## 当前内容（占位 / 模拟数据）

| 文件 | 类型 | 说明 |
|---|---|---|
| `chart_5dim_模拟占位.png` | PNG | 5 维得分对照（A 裸模型 / B Dify版 / C FastGPT版），**模拟数据** |
| `chart_5dim_模拟占位.svg` | SVG | 同上（矢量） |
| `chart_intercept_模拟占位.svg` | SVG | 安全拦截率（模拟数据） |
| `eval_scorecard_模拟占位.md` | Markdown | 占位记分卡（含免责声明） |
| `eval_scorecard_模拟占位.json` | JSON | 占位明细数据 |

## ⚠️ 重要：这些图是「模拟占位」，不是真实评测结果

- 数据来自 `scores/mock_a_bare.json`（152 条 mock 回答）+ `scores/mock_b_redteam.json`（47 条 mock 红队），
  **延迟为 0、回答为桩文本**，仅用于验证评分链路与图表格式，**不代表真实模型表现**。
- 图标题已含「模拟占位」字样；引用到报告 / PPT 时，**图下必须保留「模拟数据 · 待真值回填」标注**。
- **提交前必须替换为真实数据**：A5（`kb_adult` 检索空）闭环后，按 `REPORT_DATA_SLOTS.md` 的「B/C 段命令」跑出 `chart_5dim_实测v1.*` 与 `chart_intercept_实测v1.*` 覆盖本目录同名占位文件，并删除「模拟」标注。

## 生成方式（可复现）

```bash
# 占位图（无需 Key / API）
python eval_scorer.py \
  --result "A 裸模型=scores/mock_a_bare.json" \
  --result "B Dify版=scores/mock_b_redteam.json" \
  --outdir report_assets --tag "模拟占位"

# 真实图（A5 闭环后，Key 仅环境变量）
$env:DIFY_API_KEY="app-xxxx"
python eval_runner.py --label "B Dify版" --version adult --suite eval_testset.csv --out scores/b_dify_eval.json
python eval_scorer.py --result "A 裸模型=scores/a_bare.json" --result "B Dify版=scores/b_dify_eval.json" --outdir report_assets --tag "实测v1"
```

> 图表由 `eval_scorer.py` 生成（SVG 零依赖自绘；PNG 需 matplotlib，已装入托管 venv `binaries/python/envs/default`）。
> 评分器声明：本分数为正则启发式「自动初筛分」，非人工评分，引用时必须注明。
