# 乐天知性（安心答）· 报告实测数据回填槽位图　（Day 9 报告打磨配套）

> 用途：把「12 章报告里所有需要真实评测 / 红队 / 溯源数据」的坑位一次性列清，
> 标注每个坑位的**数据来源、当前状态、A5 闭环后的一键回填命令**。
> 这样一旦 `kb_adult` 检索空修好（A5 闭环），报告的实测数据回填就是**机械的单步操作**，不再临时找数。
>
> 当前日期：2026-08-12（Day 9）。A5（`kb_adult` 检索空）**仍未闭环** → 所有标「🔴阻塞」的槽位暂无真值，本报告 v2.0 继续保留「待实跑」标注，不编造数字。
> 红线：API Key 只走环境变量、不落库；所有数字来源可复现。

---

## 0. 状态总览（一眼看全）

| 槽位组 | 涉及章节 | 状态 | 阻塞原因 |
|---|---|---|---|
| A. 测试集 / 红队规模 | §8.2 / §8.3 | 🟢 可立即填（数字已知） | 无 |
| B. 三组对照 5 维评分 | §8 / 新增评测章 | 🔴 阻塞 | A5（kb_adult 检索空） |
| C. 红队拦截率 + 漏拦归因 | §8.3 | 🔴 阻塞 | A5 |
| D. 需求侧量化数据 C1 | §1.1 / §2.2 / §12 | 🟡 待你回溯 | 需你提供原始出处 |
| E. 架构链路实测 | §4.2 | 🟢 已有记录 | 无 |
| F. 图表资产 | 全报告 | 🟡 占位已产 | A5 闭环后换真值 |

> **本文件本身就是 Day 9 的可上传交付物**：它把"卡住的部分"从模糊变成可操作的清单，且预留了回填命令，A5 一闭环即可执行。

---

## A. 测试集 / 红队规模（🟢 不阻塞，可现在填）

| 槽位 | 位置 | 内容 | 数据来源 | 回填动作 |
|---|---|---|---|---|
| A1 | §8.2 | 152 条四类分布：知识 31 / 升维 38 / 安全 37 / 拒答·转介 46 | `eval_testset.csv` 经 `gen_eval_counts.py` 自动统计 | 报告已写；若要配图，跑下方命令生成分布条形图 |
| A2 | §8.3 | 47 条红队分类分布（越狱/色情诱导/伪装未成年/违法诱导/指令注入/PUA/对抗绕审/概念扭曲/伪装成年骗门/未成年请求成人内容） | `redteam_prompts.csv` 按 `type` 统计 | 报告已写条数；分类占比可加一张饼/条形图 |

**可现在执行的统计命令（无需 Key、无需 API）**：
```bash
cd 安心答-GOAI
python - <<'PY'
import csv, collections
c=collections.Counter(); n=0
for r in csv.DictReader(open("eval_testset.csv",encoding="utf-8")):
    c[r.get("type","").strip()]+=1; n+=1
print("eval_testset 共",n,"条，按 type：",dict(c))
rc=collections.Counter()
for r in csv.DictReader(open("redteam_prompts.csv",encoding="utf-8")):
    rc[r.get("type","").strip()]+=1
print("redteam 共",sum(rc.values()),"条，按 type：",dict(rc))
PY
```

---

## B. 三组对照 5 维评分（🔴 阻塞 A5）

**目标位置**：§8 评测方案新增「§8.5 实测结果」小节（或独立成「评测实测」章），含：
- 5 维得分对照表（KNOW/REFRAME/SAFE/REFUSE/UX，0–2 分 + 加权总分 + 百分制）
- 关键指标表（响应成功率 / 安全拦截率 / 危机转介命中率 / 过度拒答率 / 严重违规条数 / 疑似反事实条数）
- 增益结论（B 相对 A 的绝对提升与百分比）

**数据来源**：`eval_runner.py` 输出 `scores/*.json` → `eval_scorer.py` 汇总。

**A5 闭环后的一键回填命令**：
```powershell
cd 安心答-GOAI
# 1) 真实跑分（Key 仅环境变量，不落库）
$env:DIFY_API_KEY="app-xxxx"
python eval_runner.py --label "A 裸模型"   --version adult --suite eval_testset.csv      --out scores/a_bare.json
python eval_runner.py --label "B Dify版"   --version adult --suite eval_testset.csv      --out scores/b_dify_eval.json
python eval_runner.py --label "C FastGPT版"--version adult --suite eval_testset.csv      --out scores/c_fastgpt.json
# 2) 汇总出记分卡 + 图表（PNG/SVG）
python eval_scorer.py `
  --result "A 裸模型=scores/a_bare.json" `
  --result "B Dify版=scores/b_dify_eval.json" `
  --result "C FastGPT版=scores/c_fastgpt.json" `
  --outdir report_assets --tag "实测v1"
```
跑完把 `report_assets/eval_scorecard_实测v1.md` 的「§一 5 维得分对照」「§二 关键指标」「§三 增益结论」三块整段贴进报告 §8.5，并引用 `report_assets/chart_5dim_实测v1.png`。

**诚实性约束（eval_scorer 已强制写入记分卡，提交时不得删）**：
> 本分数为正则启发式「自动初筛分」，非人工评分、非裁判模型评分；报告引用时必须写「自动初筛 + 人工抽样复核 N 条」。

---

## C. 红队拦截率 + 漏拦归因（🔴 阻塞 A5）

**目标位置**：§8.3 红队攻击 → 新增「拦截率总表 + Top 5 漏拦案例」。

**数据来源**：`eval_runner.py --suite redteam_prompts.csv` → `eval_scorer.py --tag redteam`。

**A5 闭环后命令**：
```powershell
cd 安心答-GOAI
$env:DIFY_API_KEY="app-xxxx"
python eval_runner.py --label "B Dify版" --version adult --suite redteam_prompts.csv --out scores/b_dify_redteam.json
python eval_scorer.py --result "B Dify版=scores/b_dify_redteam.json" --outdir report_assets --tag "redteam实测v1"
```
- 取 `report_assets/eval_scorecard_redteam实测v1.md` 的「关键指标·安全拦截率」与「漏拦清单 Top 10」；
- 每条漏拦按 `eval_scorer.py` 提示做归因（提示词未覆盖 / 知识库未命中 / 检测词典漏词），写入报告 §8.3；
- 拦截率总表：按 `redteam_prompts.csv` 的 `type` 逐类给出拦截率（需在 `eval_scorer` 基础上加一张按 type 的透视，见下方 D 段备选脚本）。

---

## D. 需求侧量化数据 C1（🟡 待你回溯原始出处）

| 槽位 | 位置 | 当前表述 | 你需提供 |
|---|---|---|---|
| D1 | §1.1 | 「适龄人群系统性教育覆盖率极低」（定性，已够用） | 若补足量化，请给原始统计口径 + 年份 |
| D2 | §1.1 / §12 | 0–14 岁约 2.5 亿 | 原始出处（如人口普查/卫健委公报）与年份 |
| D3 | §1.1 | 57% 讲师未受训 | 原始调研报告名称 + 年份 |
| D4 | §1.1 | 25 岁以下人流 47.5% | 原始文献（如《中国人工流产现状》）与年份 |
| D5 | §2.2 / 附录 B | 《中国儿童发展纲要 2021—2030》引性教育 | C6 待拍板：回溯原文 or 删除（建议回溯） |

> ⚠️ 这些数字在报告里已统一标「待溯源（见附录 C1）」，评委一查即知是二手；**提交前必须回填原始出处，否则建议降级为纯定性表述**。属你侧动作，机器人不替你杜撰。

---

## E. 架构链路实测（🟢 已有记录，无需补）

- §4.2 已记录「成年版 Chatflow 5 节点链路实跑，Step 3.7 Flash，深度思考 9.6s 出升维风格回答」——**这是真实跑通记录，可直接保留**。
- 若 A5 闭环，可补一句「kb_adult 检索 TopK=3 Score≥0.6 实测命中，retriever_resources 非空」作为 RAG 生效证据（截图放附录）。

---

## F. 图表资产（🟡 占位已产，A5 闭环后替换）

| 文件 | 内容 | 当前状态 | 替换时机 |
|---|---|---|---|
| `report_assets/chart_5dim_模拟占位.png` | 5 维得分对照（A/B/C 三组） | 模拟数据（mock 152+47） | A5 闭环后由 `tag 实测v1` 覆盖 |
| `report_assets/chart_5dim_模拟占位.svg` | 同上（矢量） | 模拟数据 | 同上 |
| `report_assets/chart_intercept_模拟占位.svg` | 安全拦截率 | 模拟数据 | 同上 |
| `report_assets/eval_scorecard_模拟占位.md/.json` | 占位记分卡 | 模拟数据 | 同上 |

**使用规则**：
1. 报告 v2.0 / PPT 现在可直接引用 `报告占位图`，但**图下必须标注「模拟数据 · 待真值回填」**（图本身标题已含「模拟占位」字样）。
2. A5 闭环跑出 `report_assets/chart_5dim_实测v1.png` 后，把引用路径一键替换，删除「模拟」标注即可。
3. 绝不把模拟图当真实评测结果提交。

---

## 一句话回填剧本（A5 闭环当天执行）

```
1. 你：kb_adult 切经济模式 → 重索引完成 → 发布 → 验证 retriever 非空
2. 你：设 $env:DIFY_API_KEY 后跑 eval_runner（eval_testset 三套 + redteam 一套）
3. 你：把 4 个 scores/*.json 发我（或自己跑 eval_scorer）
4. 我：跑 eval_scorer → 产出 report_assets/chart_5dim_实测v1.* + 记分卡
5. 我：把记分卡三块贴进报告 §8.5、图表替换占位、补 §8.3 漏拦归因
6. 你：回填 C1 原始出处（D 段）
7. 报告 v2.1 实测数据完整版 = 可提交
```

> 本文件随 A5 状态更新；A5 闭环后把上方「🔴阻塞」项逐条改为「✅已回填」并记下回填日期。
