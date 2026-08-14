# 乐天知性（安心答）· GOAI 赛道二参赛项目

> 一个面向 **18 岁以上成年人** 的 AI 性健康与亲密关系陪伴助手 + 匿名社区。
> 参赛：GOAI 世界人工智能开源大赛 · 赛道二「无界应用（Boundless Agents）」
> 理念：知识严谨 × 社会学升维 × 18+ 安全护栏。

---

## 一、为什么做这个（差异化）

市面上的性教育要么太教科书、要么太猎奇、要么教 PUA。
我们把一个被忽视的视角做扎实：**用 AI 把"性健康知识 + 原生家庭/阶级/身份处境的升维理解 + 安全社群"三件事，做成普通人能直接用的东西。**

中文开源世界里，心理情感垂类已卷成红海（EmoLLM、SoulChat、MeChat…），
但 **性教育垂类：中文开源项目 = 0，中文专用数据集 = 0**。
国外 5 个相关项目（SafeBubble / TroyHealthLink / sex-education-chatbot-backend / Aarogya_Mitram / SuSastho.AI）全部只做"生理问答"，
**没有社会学升维、没有社区、没有审核**。这三层定位，是全球空白。

---

## 二、项目结构

```
安心答-GOAI/
├── index.html              # 可运行演示原型（18+门 + 聊天 + 论坛 + 展讯）
├── SYSTEM_PROMPT.md        # Agent 系统提示词（可直接粘贴 Dify）
├── KNOWLEDGE_BASE.md       # 知识库权威来源清单（RAG 素材，人读版）
├── kb_index_v0.json        # 知识库机读索引 v0（25 条来源 + 元数据）★Day1
├── FORUM_REVIEW.md         # 社区论坛 + 四层审核机制设计
├── EVAL_REDTEAM.md         # 评测与红队方案
├── eval_testset.csv/json   # 152 条评测测试集
├── redteam_prompts.csv     # 47 条红队攻击
├── gen_eval.py             # 测试集生成器
├── smoke_test.py           # 真模型冒烟测试 + 7 条安全规则自检 ★Day1
├── BRAND.md                # 品牌命名方案（乐天知性 已定稿）
├── DATA_STRATEGY.md        # 数据来源与版权策略
├── ADULT_EXPO_SOURCES.md   # 成人展 / 性文化活动信息源调研
├── adult_expo.html          # 成人展讯页（独立页：二次18+验证 + 列表 + 详情 + 合规区）★Day6
├── ADULT_EXPO_COMPLIANCE.md # 成人展讯合规与边界说明（资质/只聚合不撮合/以官方为准）★Day6
├── REPORT_安心答_分析报告.md  # 12 章正式报告（GOAI 提交用）
├── MVP_TIMELINE.md         # 12 天 MVP 冲刺表
├── OPEN_ISSUES.md          # 待用户核对问题清单
└── README.md               # 本文件
```

---

## 三、四层内容架构

| 层 | 模块 | 内容 |
|---|---|---|
| 知识层 | M3 身体安全 | 避孕/STI/就医，RAG 接入权威源，不代诊 |
| 升维层 | M1 自我认知 / M2 关系模式 | 性羞耻、原生家庭、阶级处境的结构性归因 |
| 多元层 | M4 多元边界 | SM/BDSM/性少数 去污名化科普，consent 前置 |
| 社群层 | 论坛 + 展讯 | 18+ 匿名社区 + 合规成人展资讯 |

---

## 四、安全合规设计（最高优先级）

- **18+ 硬门槛**：任何入口先验证成年，疑似未成年立即终止。
- **四层审核**：关键词 DFA → AI 二审(ShieldLM) → 人工抽审(敏感版块全量) → 用户信用+举报闭环。
- **七条强制安全规则**（见 SYSTEM_PROMPT.md）：AGE_GATE / NO_PORN / CONSENT_FIRST / 自伤转介 / 暴力转介 / 医疗转介 / 来源标注。
- **危机转介**（号码白名单，2026-08-04 已核实）：
  | 号码 | 用途 | 主管 / 依据 |
  |---|---|---|
  | `110` / `120` | 正在发生的危险 / 已受伤已服药 | 公共紧急号码 |
  | `12356` | 心理援助（自伤、轻生念头） | 国家卫生健康委，国卫医政函〔2024〕259 号 |
  | `12338` | 妇女维权（家暴、性侵后维权） | 中华全国妇女联合会，2005 年开通 |
  | `12355` | 青少年服务台（**青少版专用优先**） | 共青团中央，2024 年 6 月三部门意见 |
  > ✅ **C4 已闭环**：核实依据、服务时间口径、四类转介话术骨架见 `KB_CRISIS_HOTLINES.md`。
  > 硬约束：模型**只能复述白名单号码**，不得凭记忆生成其他号码；下次强制复核 2026-08-14。

---

## 五、本地运行演示

直接双击 `index.html` 用浏览器打开即可：
1. 先过 18+ 年龄门；
2. 「安心答助手」默认可**离线演示**（本地智能应答，含升维示例）；
3. 点"切换实时API"粘贴 **阶跃 StepFun Key**（默认 `step-router-v1`），即可接入真实大模型；
4. 浏览「社区论坛」「成人展资讯」「项目说明」了解全貌。展讯为独立页 `adult_expo.html`（从主站顶栏「成人展讯」或页面内链接进入，需二次 18+ 验证）。

### 命令行冒烟测试（验证真模型链路 + 七条安全规则）

```powershell
cd 安心答-GOAI
$env:STEPFUN_API_KEY="你的完整Key"     # 仅环境变量，脚本绝不写入文件
python smoke_test.py                   # 跑 5 条冒烟题，出延迟/得分报告
python smoke_test.py --dry-run         # 不调 API，先验证脚本与规则检测器
```

产出 `smoke_test_report.md` + `smoke_test_result.json`，
报告内 Key 字段恒为 `REDACTED`，可直接截图或随仓库上传。仅需 Python 3，无第三方依赖。

> 演示模式不联网、不收集任何数据；API Key 仅存于本次会话内存，刷新即清空。

---

## 六、夏令营落地路径（Dify / Coze）

1. 注册 goaihz.com 报名 + 加 Datawhale 夏令营群；
2. 把 `SYSTEM_PROMPT.md` 整段粘进 Dify/Coze 的「提示词」；
3. 按 `KNOWLEDGE_BASE.md` 建 RAG 知识库（权威源清洗后入库）；
4. 用 `FORUM_REVIEW.md` 的四层审核做社区模块；
5. 把本项目前端 + 提示词 + 知识库清单开源到 GitHub，作为"开源贡献"证据。

---

## 七、开源协议

本项目代码与文档采用 **MIT License**（知识库内容须遵守各自来源的版权与许可）。

---

## 八、技术栈与时间节点

| 组件 | 选型 |
|---|---|
| 大模型后端 | **阶跃 StepFun step-router-v1**（按需路由，OpenAI 兼容） |
| Agent / RAG | **Dify**（主力，可私有化） + FastGPT（对照实验） |
| 安全护栏 | ShieldLM-6B + Llama Guard S1–S13 + DFA 敏感词 |
| 前端 | 单文件 HTML，零后端依赖 |
| 部署（上线级） | Cloudflare Pages（用户已有自有域名） |
| 许可证 | MIT |

**关键时间**：
- 🟢 **8/15（周五）MVP 冻结**
- 🔴 **8/16（周六）24:00 前 初赛提交**（goaihz.com）
- 详细每日动作见 `MVP_TIMELINE.md`；未决问题见 `OPEN_ISSUES.md`
