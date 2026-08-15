# 乐天知性·安心答 — 项目框架说明（供 Codex 评审）

> 本文件用于把项目整体框架、文件位置、当前状态一次性交给另一个 AI Agent（Codex）做交叉评审。
> 项目本身**不含任何密钥**；所有 API Key 仅在运行时由内存/环境变量传入，不落库、不进本仓库。

---

## 0. 一句话定位
GOAI 大赛**赛道二（无界应用 / Boundless Agents）**参赛项目：**18+ AI 性健康与亲密关系助手**。
差异化 = 社会学升维陪伴 + 适龄分级双版本 + 安全社群；核心合规 = 18+ 门 + 7 条安全规则 + 危机转介白名单。
提交截止 **2026-08-16 24:00**（平台 goaihz.com）。当前处于提交前收尾阶段。

## 1. 仓库位置 & 技术栈
- **本地路径**：`C:\ProgramData\WorkBuddy\users\17d0d283\WorkBuddy\idea\安心答-GOAI\`
- **形态**：纯静态交付物（HTML + Markdown + Python 评测脚本），**无前端构建步骤**。`build_deck.py` / `build_pdf.py` 仅用于生成 PPT/PDF 交付物。
- **运行时依赖（云端，非本仓代码）**：Dify Cloud（Chatflow 编排）+ 阶跃 Step 3.7 Flash（LLM）+ 硅基流动 `BAAI/bge-m3`（embedding）+ 双知识库（kb_adult / kb_minor）。
- **Git**：本地仓 3 commit / 82 文件 / MIT License，**尚未 push 远程**（公开仓待确认）。
- 已内置 Agent 协作脚手架：`.github/copilot-instructions.md`、`.vscode/mcp.json`、`AGENTS.md`。

## 2. 目录树（已排除 .git 内部）
```
安心答-GOAI/
├─ index.html                      # 演示原型（18+ 玻璃门 + 离线演示模式 + 双 Tab demo）
├─ adult_expo.html                 # 成人展讯聚合页（二次 18+ 验证，只聚合不撮合）
├─ README.md                       # 项目总览
├─ LICENSE                         # MIT
├─ REPORT_安心答_分析报告.md        # 12 章主报告（v2.2，专家团复核稿）
├─ presentation.pptx               # 方案 PPT（18 页）
├─ proposal.pdf                    # 执行摘要（1 页）
├─ MVP专家团打磨报告.md            # 8 角色联合评审 + 优先级矩阵 + 48h 行动表
├─ OPEN_ISSUES.md                  # 进度/阻塞跟踪（C1–C6、A5 等）
├─ submission_checklist.md         # 初赛提交自检清单
├─ .github/copilot-instructions.md # 给编码 Agent 的指令
├─ .vscode/mcp.json                # MCP 配置
├─ # —— 安全与合规 ——
├─ SYSTEM_PROMPT.md                # 成年版 Agent 提示词（7 条安全规则）
├─ SYSTEM_PROMPT_MINOR.md          # 青少版提示词（规则更严）
├─ KB_CRISIS_HOTLINES.md           # 危机转介白名单（110/120/12356/12338/12355 + 依据）
├─ DUAL_VERSION_DESIGN.md          # 双版本架构设计（年龄门控 + 物理隔离）
├─ ADULT_EXPO_COMPLIANCE.md        # 成人展合规说明
├─ ADULT_EXPO_SOURCES.md           # 成人展来源清单
├─ # —— 架构与配置 ——
├─ DIFY_SETUP.md / DIFY_STEP_BY_STEP.md  # Dify Chatflow 搭建指南（5 节点）
├─ KNOWLEDGE_BASE.md               # 知识库设计
├─ kb_index_v0.json                # 知识库索引（含 KB-CN-005=纲要引文）
├─ knowledge_base_v1.md            # 知识库 v1 文档
├─ # —— 评测与红队 ——
├─ eval_runner.py                  # Dify REST API 评测跑批（断点续跑）
├─ eval_scorer.py                  # 评分器（安全/合规/升维多维度）
├─ gen_eval.py                     # 评测集生成
├─ smoke_test.py / smoke_test_report.md / smoke_test_result.json  # 冒烟测试
├─ EVAL_REDTEAM.md                 # 红队方法论
├─ eval_testset.csv / eval_testset.json   # 评测集 152 条
├─ redteam_prompts.csv             # 红队 47 条
├─ # —— 知识库素材 ——
├─ kb_adult_uploads/               # 成人版待灌文档（已下载 2 篇）
├─ KB_ADULT_UPLOAD_LIST.md / KB_ADULT_REPAIR_GUIDE.md  # 成人库上传/修复指南
├─ KB_MINOR_UPLOAD_LIST.md         # 青少库上传清单
├─ # —— 双版本创意层 ——
├─ E3_COURSE_CARDS.md / e3_cards.json   # 青少版 10 张身体权启蒙卡
├─ E4_DEMO_PAGE_OPTIONS.md         # 演示页方案
├─ # —— 品牌 / 商业 ——
├─ BRAND.md / BUSINESS_VALUE.md / DATA_STRATEGY.md / FORUM_REVIEW.md
├─ # —— 规划与脚本 ——
├─ MVP_TIMELINE.md / MVP_FREEZE_RELEASE.md / REPORT_DATA_SLOTS.md
├─ FRONTEND_POLISH_PROPOSAL.md     # 未采用，留档
├─ build_deck.py / build_pdf.py / rename_brand.py / download_kb_adult.py / probe.py
```

## 3. 架构速览
- **Dify Chatflow（5 节点）**：开始 → 知识检索(kb_adult/kb_minor) → 条件分支(检索不为空→LLM / 空→兜底) → LLM(Step 3.7 Flash + SYSTEM_PROMPT) → 直接回复。
- **双版本分流**：按年龄/身份认证路由未成年版与成年版，后端物理隔离；青少版对成人向话题零容忍拦截。
- **安全设计**：成年版 7 条规则（允许安全性行为教育、禁止动作细节/色情）、青少版更严、危机转介白名单（不替代专业干预）。
- **评测**：152 条评测集 + 47 条红队，评分器链路 `eval_runner.py → eval_scorer.py` 已就绪。

## 4. 当前状态（截至 2026-08-15）
- ✅ 已就绪：演示原型、12 章报告(v2.2)、PPT+PDF、152+47 评测红队集、双版本安全设计、知识库索引、成人展讯页、MIT License、本地 git 仓。
- ✅ **数据溯源已闭环**：C6《中国儿童发展纲要》逐字核入国务院原文；C1 主论据替换为可溯源 78.24%（女童保护 2019 调研）。
- ⚠️ 阻塞/待办（均**不阻塞提交**）：
  - **A5**：`kb_adult` 全文检索命中为空（Dify 侧 embedding=bge-m3 已配但索引未生效），仅影响评测真值，报告已用占位+方法论兜住。
  - **可达性**：`index.html` 是本地文件，评委在 goaihz.com 打不开 → 需部署 Cloudflare Pages 或附"本地运行说明"。
  - **GitHub 公开**：本地仓已建，待确认远程/授权推送。
  - 青少版"怎么做爱"类硬闯建议加前置关键词硬拦截（现靠 LLM 自拒）。

## 5. 建议请 Codex 重点评审的问题
1. **安全门设计**：双版本 + 7 条规则 + 危机白名单，能否挡住红队 47 条硬闯？青少版是否需要前置关键词硬拦截？
2. **报告可信度**：v2.2 中需求侧数据（78.24% 等）与政策引文（纲要原文）是否经得起推敲？
3. **评测科学性**：`eval_scorer.py` 的评分维度/权重是否合理？152+47 覆盖度够吗？
4. **原型质量**：`index.html` 的双 Tab demo 与离线模式是否完整、有无 JS 错误、是否需要"演示免责"提示？
5. **架构健壮性**：Dify 5 节点条件分支（检索不为空→LLM / 空→兜底）是否有边界漏洞？
6. **提交完整性**：对照 `submission_checklist.md`，还差什么能补的？

## 6. 红线（评审/修改时不可动）
- 18+ 门槛绝不为评分妥协；7 条安全规则与危机白名单不得弱化；API Key 绝不写入文件；不复制他人原话。
