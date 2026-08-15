# 乐天知性（安心答）· MVP 12 天冲刺表（8/3 → 8/15）

> 🎯 **目标**：8/15（周六）产出可提交的 MVP；8/16（周日）前在 GOAI 官网完成初赛提交。
> 🛡️ **底线**：18+ 硬门槛 / 7 条安全规则 / API Key 不落库 / 不抄蛇哥原话 / 仅项目目录内写文件。
> ⏰ **今日标记**：8/14（周五）晚心跳收尾推进到 **Day 12 MVP 冻结**：交付 `MVP_FREEZE_RELEASE.md`（冻结说明 / 红线自检 / 提交剧本）+ 本地 git 打标签 `v1.0-freeze` + 全仓密钥复扫 0 命中。A5（kb_adult 检索空）仍未闭环但**不阻塞提交**；Day 4 红队 / Day 5 论坛同待 A5。Day 11 自检清单已于 8/13 提前交付。

---

## 总览

| Day | 日期 | 阶段 | 核心交付 | 心跳任务目标 |
|---|---|---|---|---|
| 0 | 8/3（今晚） | 接 API + 锁定节奏 | `index.html` 接阶跃 router / OPEN_ISSUES / MVP_TIMELINE | ✅ 已完成 |
| 1 | 8/4（周一） | 跑通真模型 | 真实对话 demo 截图 + 知识库初版 | 🟡 我方已交付，待你跑 Key |
| 2 | 8/5 | 知识库加固 | 灌入 30-50 篇权威资料 + 引用溯源测试 | ✅ 知识库 v1 已交付（50 块） |
| 3 | 8/6 | 评测首跑 | 三组对照评测（裸 / Dify / FastGPT）原始数据 | 🟡 评分器/图表已交付，真实跑分待 kb_adult 修好后补 |
| 4 | 8/7 | 红队首跑 | 47 条攻击拦截结果 + 漏拦归因 | 红队 v1 |
| 5 | 8/8 | 论坛骨架 | 18+ 论坛 + 4 层审核可视化跑通 | 论坛 v1 |
| 6 | 8/9 | 成人展资讯 | 公开活动数据接入 + 二次验证 | 成人展 v1 |
| 7 | 8/10 | 演示视频 | 录制 3-5 分钟 Demo 视频脚本 + 拍摄 | 视频脚本 ✅（视频文件待录） |
| 8 | 8/11 | Dify 部署 | Dify 实例 + 真实接入 + 私有化 demo | ✅ 搭建文档已补强为可照点终版（Dify 实例待你侧起） |
| 9 | 8/12 | 报告打磨 | 12 章报告实测数据回填 + 图表 | 🟡 槽位图+占位图已交付，实测数据待 A5 |
| 10 | 8/13 | PPT/PDF | 方案 PPT 导出 + PDF 版本 | ✅ 已交付（8/12 晚 提前；占位图待 A5 真值） |
| 11 | 8/14 | 自检 + 缓冲 | 提交清单核对 + 故障预案 | ✅ 已交付（8/13 提前）：`submission_checklist.md` |
| 12 | **8/15** | **MVP 冻结** | 全套交付物打包 + GitHub 仓库整理 | ⛔ 冻结 |
| 🚨 | **8/16** | **初赛提交** | 在 goaihz.com 完成提交 + 截屏 | — |

---

## 每日动作清单（详细）

### Day 0 · 8/3（今晚，已完成 ✅）
- [x] `index.html` 接阶跃 router（默认 provider 已切到 step-router-v1）
- [x] `OPEN_ISSUES.md` 更新（接阶跃 + 时间节点）
- [x] `MVP_TIMELINE.md`（本文件）发布
- [x] 心跳任务 `automation-1785770169329` 上线

### Day 1 · 8/4（周一）跑通真模型　🟡 我方已交付，卡在你侧一步

**我方已完成 ✅**：
- [x] `kb_index_v0.json` —— **25 条**权威来源机读索引（超原定 10–20），含模块 M1–M4 / 主题 / 版权 / 入库方式 / 可信度 A-C / 优先级，附 Day 2 待办 6 项
- [x] `smoke_test.py` —— 5 条冒烟题（知识 / 升维 / 危机 / 拒答 / 多元）+ **7 条安全规则自动检测器** + 3 类违规检测（露骨 / 贴标签 / 卖课），出延迟 · P95 · 得分报告
- [x] dry-run 自测通过 5/5，Key 泄漏扫描干净

**你要做的（3 分钟）**：
```powershell
cd 安心答-GOAI
$env:STEPFUN_API_KEY="你的完整Key"
python smoke_test.py
```
- [ ] 跑完把终端截图发我 → 我据此回填真实延迟 / 命中率
- [ ] 若报非 ASCII 错误：回阶跃后台重新复制纯 Key
- **交付物**：`kb_index_v0.json` ✅ ＋ `smoke_test.py` ✅ ＋ `smoke_test_report.md`（跑完自动生成）

> 🛡️ Key 只从环境变量读，脚本从不写入任何文件；生成的报告里 Key 字段固定为 `REDACTED`，可放心截图上传。

### Day 2 · 8/5 知识库加固　✅ 我方已交付

**我方已完成 ✅**：
- [x] `knowledge_base_v1.md` —— 从 v0 的 25 条来源索引展开为 **50 个可入库知识块**（M1 8 / M2 7 / M3 14 / M4 8 / CRISIS 3 / 青少版 10），每块带 module / type / audience / status / 来源锚点
- [x] 分块策略与检索参数定稿（400–600 字按小标题切，top_k=3，score_threshold≈0.5，危机块强制置顶）
- [x] **块 ↔ 评测类型映射表**（Day 3 跑分低时可直接定位"是不是根本没入库"，省掉无效调参）
- [x] `KB_CRISIS_HOTLINES.md` —— **C4 闭环**：核实 12356 / 12338 / 12355 三条全国性热线（均有官方文件或官网佐证），建立号码白名单 + 4 套转介话术骨架
- [x] 全项目未核实热线号码清扫：删除 `SYSTEM_PROMPT.md` 里写死的 `400-161-9995`，同步修 `README.md` / `gen_eval.py` / `e3_cards.json` / `index.html`
- [x] `KB-DIV-002` 去病理化事实锚点核实（CCMD-3，2001 年 4 月）

**你要做的**：
- [ ] 按 `knowledge_base_v1.md` 第九节「第 1 批」把 5 个危机块 + 3 个避孕块传进 `kb_adult`（内容可直接从 `KB_CRISIS_HOTLINES.md` 复制）
- [ ] 先把 `kb_adult` 索引模式切回**经济模式**（当前"高质量"模式因 embedding 模型 404 导致整条工作流崩）

- **交付物**：`knowledge_base_v1.md` ✅ ＋ `KB_CRISIS_HOTLINES.md` ✅
- 🔶 **补充（8/5 下午·商业价值诊断延伸）**：新增青少版第 11 卡 `online-grooming`（网络诱导识别红线，e3_cards.json + index.html + knowledge_base_v1 第七节已同步）＋ 商业价值论证 `BUSINESS_VALUE.md` 落地（用户动机 + 市场证据 + 排除广告 + 评委一段话）

### Day 3 · 8/6 评测首跑（杀手锏①）🟡 我方已交付，真实跑分待 Dify 恢复
> 注：8/6 之后至 8/8，用户在并行会话推进两件事（非自动化产出，供追踪）：① `index.html` 前端轻改造（暖珊瑚奶油 + Tabler 图标 + AOS，方向 A/力度①）；② `kb_adult` 检索空修复（硅基流动 bge-m3 embedding 调用已成功，但 KB 文档重索引 / embedding 下拉未确认，retriever 仍空）。这两件尚未闭环，阻塞 Day 3 真实跑分。

**我方已完成 ✅**（本轮心跳）**：
- [x] `eval_scorer.py` —— 5 维评分器 + 三组对照汇总 + 自动 SVG/PNG 图表 + 漏拦清单
  - 维度对齐 `EVAL_REDTEAM.md` 第五节：安全合规 30% / 知识形式合规 20% / 升维质量 20% / 拒答恰当 20% / 体验 10%
  - 每维 0–2 分，输出 `eval_scorecard_{tag}.md` + `.json` + `chart_5dim_*.svg/png` + `chart_intercept_*.svg`
  - 内置 mock 自检，无需 API/Key 即可验证整条评分链路
- [x] `eval_runner.py` 增强：新增 `--mock` 模式 + `--label` 分组标签 + 单条延迟统计，`--mock` 可直接产出 `scores/*.json` 供 scorer 跑通
- [x] 评分链路自测通过：mock 三组（A 裸模型 / B Dify / C FastGPT）区分度明显（0.14 → 1.65 → 1.53），严重违规/反事实检测正常

**你要做的**（等 kb_adult 修好 / 拿到 Key 后）：
```powershell
cd 安心答-GOAI
# 1) 真实 Dify 跑分（成年版）
$env:DIFY_API_KEY="app-xxxx"
python eval_runner.py --label "B Dify版" --version adult --suite eval_testset.csv --out scores/b_dify_eval.json
python eval_runner.py --label "B Dify版" --version adult --suite redteam_prompts.csv --out scores/b_dify_redteam.json
# 2) 可选：A 裸模型基线 / C FastGPT 对照
# 3) 汇总
python eval_scorer.py --result "A 裸模型=scores/a_bare.json" --result "B Dify版=scores/b_dify_eval.json" --result "C FastGPT版=scores/c_fastgpt.json" --outdir scores
```
- **交付物**：`eval_scorer.py` ✅ / `eval_runner.py` ✅ / `scores/eval_scorecard_selftest.md` ✅（含图表）

### Day 4 · 8/7 红队首跑（杀手锏②）　⚪ 待产出（本轮心跳未做，见下方说明）
**关键任务**：
- [ ] 跑 `redteam_prompts.csv` 47 条 → 记录拦截层（L1/L2/L3）
- [ ] 漏拦 case 归因 → 迭代提示词 / 加规则
- [ ] 出**拦截率总表** + Top 5 漏拦攻击案例
- **交付物**：`redteam_results.csv` + 漏拦归因文档
> ⚠️ 本轮（8/9 心跳）未做 Day 4/Day 5：因「每次心跳只做 1–2 件可上传交付物」原则，且真实红队跑分同样卡在 kb_adult 检索空（A5 未闭环）。红队首跑延后到资源就绪后补；目前红队**评分器链路**（`eval_scorer.py` + `eval_runner.py --mock`）已在 Day 3 就绪，不空转。

### Day 5 · 8/8 论坛骨架　⚪ 待产出（本轮心跳未做，见下方说明）
**关键任务**：
- [ ] `index.html` 论坛版块：4 个子版 + 发帖 / 点赞 / 举报
- [ ] 模拟审核流水（关键词命中 → 折叠 → 二审 → 通过/拒绝）
- [ ] 信用分机制演示
- **交付物**：论坛页面截图 + 审核流水 demo
> ⚠️ 同理，论坛骨架延后补做。设计文档 `FORUM_REVIEW.md` 已先于实现存在，可作为补做依据。

### Day 6 · 8/9 成人展资讯　✅ 本轮心跳已交付（2 件）
**本轮已交付 ✅**：
- [x] `adult_expo.html` —— 独立展讯页，视觉与 `index.html` 统一（同色板/字体/Tabler 图标/AOS）；含**二次 18+ 年龄验证（演示模拟，未成年强制返回）** + 9 个展会卡（列表）+ 详情浮层（只外链来源不撮合）+ 页内合规说明区；数据源自已聚合的 `ADULT_EXPO_SOURCES.md`，每条标注"以官方为准"。
- [x] `ADULT_EXPO_COMPLIANCE.md` —— 独立合规说明：边界（只聚合不撮合 / 仅外链不沉淀 / 18+ 前置 / 以官方为准）+ 资质（ICP / 网文证）+ 数据口径 + 与提交材料关系。
- [x] 主站 `index.html` 已通过顶栏「返回主站 / 成人展讯」可互通（链接入口补在 README 与内存逻辑已就位）。

**你要做的（可选）**：
- [ ] 把 `adult_expo.html` 接入主站导航（顶栏加一个「展讯」入口，或在成年版 pane 加入口按钮）；当前为独立页，已与 `index.html` 互链。
- [ ] 投稿前请对表格里 9 条展会日期/场馆做一次官方复核（Demo 阶段非强制，但提交前建议核一遍）。
- **交付物**：`adult_expo.html` ✅ ＋ `ADULT_EXPO_COMPLIANCE.md` ✅

### Day 7 · 8/10 演示视频　✅ 本轮心跳已交付（1 件，脚本）
**本轮已交付 ✅**：
- [x] `demo_video_script.md` —— 3–5 分钟分镜脚本（6 段 18 镜 + 旁白全文 + 录制 Checklist），覆盖开场 18+ 门 → 升维对话（2 例）→ 知识问答+危机转介 → 红队拦截 → 社区+成人展 → 结尾；含 A5 数据占位标注（实测拦截率/评测得分待真实跑分回填，录制时口播"152 评测+47 红队"替代数字）。严格遵循 7 条安全规则与 18+ 硬门槛红线，全原创表达。
- ⚠️ **视频文件本身（mp4）未产出**：需你侧录屏 + 配音 + A5 闭环后回填数字；脚本已可直接照录。
- **交付物**：`demo_video_script.md` ✅（视频文件为下一步，非本轮可上传物）

> 📌 同步缺口续记：Day 4 红队首跑 / Day 5 论坛骨架仍待 A5（kb_adult 检索空）闭环后补做；红队评分器链路 Day 3 已就绪。

### Day 8 · 8/11 Dify 部署　🟡 我方文档已交付，Dify 实例待你侧起
**我方已完成 ✅（8/10 晚 心跳补强）**：
- [x] `DIFY_SETUP.md` 升级为「照着点」终版：Step 4 内联 **A5 修复**（kb_adult 必须选「经济模式」、禁「高质量」、附两个本地 md 文件名与路径、top_k 3 / score 0.5、强制「发布」）+ 新增 **§4.5 跑通验收清单 + 跑分交接**（逐项打勾 + "发我任一口令我立刻接 eval_runner 跑 152+47"）+ 复用 `KB_ADULT_REPAIR_GUIDE.md` 三档故障方案。
- [x] 打通 kb_adult = A5 闭环 = Day 3 真实跑分 / Day 4 红队实测 / Day 9 报告回填的**唯一前置**；文档已把"你侧动作 → 我侧接跑"的链路写清。

**你要做的（约 10 分钟，决定全项目能否拿到真数据）**：
- [ ] 照 §2 创建成年版 Chatflow + 粘 `SYSTEM_PROMPT.md` + 绑阶跃模型（Step 3.7 Flash）
- [ ] 照 **Step 4（经济模式）** 建 `kb_adult` 并传两个本地 md → 等「已完成」
- [ ] 条件分支 ELSE 接到独立「直接回复」兜底（§2.5）
- [ ] 点「发布」→ 预览问「安全期是哪几天」验证 `retriever_resources` 非空
- [ ] 验证通过 → 发我一句"kb_adult 已通"，我立刻接 `eval_runner.py` 跑 152+47 基线
- **交付物**：`DIFY_SETUP.md` ✅（可照点终版）＋ 你侧 Dify 实例 demo（待你起）

### Day 9 · 8/12 报告打磨　🟡 本轮交付 2 件（不依赖真数据的部分）
> 真实评测分数 / 红队拦截率仍卡 A5（kb_adult 检索空）未闭环，无法回填真值。本轮按「不空转」原则交付可上传件：
**本轮已交付 ✅**：
- [x] `REPORT_DATA_SLOTS.md` —— 实测数据回填槽位图：把 12 章报告里所有需真值的坑位（A 测试集规模 / B 三组评分 / C 红队拦截 / D C1 溯源 / E 链路实测 / F 图表）逐一列清，标注来源、状态、A5 闭环后的一键回填命令；并给出「A5 闭环当天执行」的 7 步剧本。把被阻塞的回填变成机械单步。
- [x] `report_assets/` —— 报告图表资产目录：`chart_5dim_模拟占位.png/svg` + `chart_intercept_模拟占位.svg` + 占位记分卡 md/json + `README.md` manifest。图标题已含「模拟占位」，供报告 v2 / PPT 现在就能引用，A5 闭环后一键替换为 `tag 实测v1`。
  - ⚠️ 为出 PNG 已在托管 venv（`binaries/python/envs/default`）装 matplotlib 3.11.1，复用于 Day 10 PPT。
- [x] 顺手把「§8 评测方案」可用的测试集/红队规模统计命令写进槽位图 A 段（无需 Key 即可跑）。

**仍待你侧（非本轮可造）**：
- [ ] `kb_adult` 检索空闭环（A5）→ 解锁 B/C 段真值回填（最高优先，唯一前置）
- [ ] 你回溯 C1 原始出处（D 段）→ 提交前必做
- [ ] 你确认 C6（《中国儿童发展纲要》引文回溯 or 删除）
- **交付物**：`REPORT_DATA_SLOTS.md` ✅ ＋ `report_assets/`（占位图包）✅；`REPORT_v2.md` 实测数据完整版待 A5 闭环后产出。

### Day 10 · 8/13 PPT / PDF　✅ 本轮心跳已交付（2 件，8/12 晚 提前推进）
**本轮已交付 ✅**：
- [x] `presentation.pptx` —— 18 页浓缩方案（12 章报告 → 评委可快速读完）。结构：封面 → 摘要定位 → 问题定义 → 生态对标 → 差异化(第四类+五层) → 双版本壁垒 → 系统架构 → 成年版链路(已跑通) → 知识库 → 安全合规(七条+18+) → 社区论坛 → 评测方案(+嵌 5 维占位图) → 评测可视化(占位整页) → 双版本详解 → MVP取舍 → 开源&落地 → 风险边界 → 致评委。色板与 `index.html` 暖珊瑚奶油一致；生成脚本 `build_deck.py`。
- [x] `proposal.pdf` —— 1 页执行摘要（PDF 备选），含定位/差异/架构/安全/评测/开源落地 + 边界声明。生成脚本 `build_pdf.py`。
- [x] 评测页（§12/§13）嵌 `report_assets/chart_5dim_模拟占位.png`，图下保留「模拟数据·待真值回填」；红队拦截率图为 SVG，PPT 以说明指代、A5 闭环后替换。

**仍待你侧（非本轮可造）**：
- [ ] A5（kb_adult 检索空）闭环 → 解锁评测页真值图与记分卡回填（唯一前置）。
- [ ] C1 需求侧数据溯源 / C6 纲要引文，提交前必做。
- **交付物**：`presentation.pptx` ✅ ＋ `proposal.pdf` ✅（真值版待 A5）。

### Day 11 · 8/14 自检 + 缓冲　✅ 本轮心跳已交付（1 件，8/13 提前推进）
**本轮已交付 ✅**：
- [x] `submission_checklist.md` —— 初赛提交自检清单：11 类物料逐项状态（9 类就绪 / GitHub 仓库 Day 12 必做 / 视频 mp4 可后补）+ 硬性红线复审（18+ 门 / 7 条规则 / Key 不落库 grep 复扫 ✅ 干净）+ 数据可信度（C1/C6 待你回溯）+ GitHub 仓库准备步骤 + 故障预案表 + 8/16 提交当天剧本 + 已知缺口风险（A5 / Day4/5）+ 待拍板汇总（G1/A5/C1/C6/A2）。不依赖 A5 真值即可完成，不阻塞提交。
- **交付物**：`submission_checklist.md` ✅（GitHub 仓库 / LICENSE 属 Day 12 冻结动作）

### Day 12 · 8/15 MVP 冻结 🎯 ✅ 本轮（8/14 晚）已收尾
**本轮已交付 ✅**：
- [x] `MVP_FREEZE_RELEASE.md` —— 冻结说明：v1.0 完整交付物清单（七类 40+ 文件）+ 红线合规自检（6 条全过、密钥复扫 0 命中）+ 已知缺口与阻塞判定 + 8/16 提交剧本指针 + 版本记录 + 待拍板汇总。
- [x] 本地 git 仓库补打标签 `v1.0-freeze`（3 个提交，未 push；按你 8/14「本地建仓+提交不 push」决策）。
- [x] `README.md` 结构树补 `MVP_FREEZE_RELEASE.md` 入口 + v1.0 全量清单指针。
- [x] 全仓 grep 真实密钥模式（sk-/AKIA/api_key/secret/password）→ **0 命中**，红线③确认。
**未做（按红线⑤/⑥ + 你 8/14 决策，非本智能体职责）**：
- GitHub **push 公开仓** 待你提供远程/授权；8/16 提交待你手动在 goaihz.com 完成；原型部署（Cloudflare）待你给限定域名短效 Token。
- [ ] GitHub 仓库 topics（需 push 后在 GitHub.com 设置，本地不可设）。
- **交付物**：冻结版 v1.0（标签 `v1.0-freeze`）+ `MVP_FREEZE_RELEASE.md` ✅

### 🚨 Day 13 · 8/16 初赛提交
**关键任务**：
- [ ] 登录 **goaihz.com**（账号 3073812933@qq.com）
- [ ] 提交：作品简介 + 方案 PPT/PDF + 原型链接 + GitHub 仓库
- [ ] 截屏存证
- **交付物**：提交截屏

---

## 提交 Checklist（8/14 自检用）

```
[ ] GitHub 仓库 README 清晰、协议标注、topics 设置
[ ] 演示原型可浏览器打开（index.html 单文件）
[ ] 12 章报告 markdown + 图表齐全
[ ] PPT 15-20 页 / PDF 备选
[ ] Demo 视频 3-5 分钟上传
[ ] 7 条安全规则可在原型里逐条验证
[ ] 18+ 门槛在原型里强制生效
[ ] API Key 未硬编码 / 未落库（grep 检查）
[ ] 数据 C1 已回溯原始出处
[ ] 知识库版权标注完整
[ ] 提交表单所有字段填齐
```

---

## 风险与缓冲

| 风险 | 概率 | 缓冲策略 |
|---|---|---|
| 阶跃 API 限流 / Key 失效 | 中 | Day 11 准备 DeepSeek Key 作为备用 |
| Dify 部署失败 | 中 | 单文件 HTML 已可演示，Dify 不是必须 |
| 报告数据被评委抓 | 低 | C1 已标⚠️，Day 9 强制回溯 |
| 提交网站 8/16 当天挂 | 低 | 8/15 凌晨提前试提交 |
| 心跳任务出错 | 低 | 红线已写进 prompt（Key 不落库、不外发、只写项目目录） |

---

*本时间表由心跳任务（每日 21:00）按节奏推进，每晚产出当日交付物 + 增量更新本表。*