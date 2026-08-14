# 乐天知性（安心答）· MVP v1.0 冻结说明

> GOAI 世界人工智能开源大赛 · 赛道二「无界应用（Boundless Agents）」
> 冻结判定日期：**2026-08-14**（MVP 冻结日 8/15 前一夜心跳收尾）
> 品牌：乐天知性　/　产品：安心答　/　开源协议：MIT

---

## 一、冻结状态

| 项 | 状态 |
|---|---|
| MVP 冻结 | ✅ **v1.0 判定冻结**（可提交态） |
| Git 仓库 | ✅ 本地仓库已建，3 个提交，已打标签 `v1.0-freeze` |
| 初赛提交 | ⏳ 待你侧 8/16 24:00 前在 goaihz.com 完成（非本智能体代操作） |
| 真实评测跑分（A5） | ⚪ 仍卡 Dify 后台，但**不阻塞提交** |

**一句话结论**：整套参赛物料已达「可打包上传」状态。唯一仍未闭环的 A5（kb_adult 真实检索跑分）只影响「评测章真值数字」，不影响任何硬性门槛与提交资格；评委看到的是完整的设计论证 + 152/47 评测框架 + mock 链路证据，必要时以「模拟占位·待真值回填」如实标注，不伪造数据。

---

## 二、v1.0 完整交付物清单

### 🧩 核心：原型 + Agent 系统
| 文件 | 说明 | Day |
|---|---|---|
| `index.html` | 可运行演示原型：18+ 年龄门 + 双 Tab 聊天（演示模式/实时API）+ 社区论坛 + 展讯入口 | 0 |
| `adult_expo.html` | 成人展讯独立页：二次 18+ 验证 + 9 展会卡 + 详情只外链 + 页内合规区 | 6 |
| `SYSTEM_PROMPT.md` | 成年版 Agent 系统提示词（含 7 条强制安全规则，可直接粘 Dify） | 0 |
| `SYSTEM_PROMPT_MINOR.md` | 青少版提示词（成人话题零容忍拦截，不进 LLM） | E 系列 |
| `DUAL_VERSION_DESIGN.md` | 双版本架构草案（未成年版+18+版，合规红线/分级/动漫化/知识库分层） | E |
| `DIFY_SETUP.md` | Dify 照着点搭建文档（含 A5 修复：kb_adult 经济模式 + 验收清单 + 跑分交接） | 8 |
| `DIFY_STEP_BY_STEP.md` | 青少版 5 节点操作细节 | F |

### 📚 知识库（RAG 素材）
| 文件 | 说明 | Day |
|---|---|---|
| `KNOWLEDGE_BASE.md` | 知识库权威来源清单（人读版） | 0 |
| `knowledge_base_v1.md` | 50 个可入库知识块 + 分块策略 + 块↔评测映射 | 2 |
| `kb_index_v0.json` | 知识库机读索引 v0（25 条来源 + 模块/可信度/版权元数据） | 1 |
| `KB_CRISIS_HOTLINES.md` | 危机转介号码白名单（12356/12338/12355/110/120，已核实 + 4 套话术） | 2 |
| `KB_ADULT_REPAIR_GUIDE.md` / `KB_ADULT_UPLOAD_LIST.md` / `KB_MINOR_UPLOAD_LIST.md` | 索引修复与入库清单 | 2/8 |

### 🧪 评测 + 红队
| 文件 | 说明 | Day |
|---|---|---|
| `eval_testset.csv` / `.json` | 152 条评测测试集 | 0 |
| `redteam_prompts.csv` | 47 条红队攻击集 | 0 |
| `gen_eval.py` | 测试集生成器 | 0 |
| `smoke_test.py` | 真模型冒烟测试 + 7 条安全规则自检（Key 仅环境变量，报告恒 REDACTED） | 1 |
| `eval_runner.py` | 评测运行器（含 `--mock` / `--label` / 单条延迟；接真实 Key 跑 152+47） | 3 |
| `eval_scorer.py` | 5 维评分器（安全30/知识20/升维20/拒答20/体验10）+ SVG/PNG 图表 + 漏拦清单 | 3 |
| `EVAL_REDTEAM.md` | 评测与红队方案（含 Rubric） | 0 |
| `scores/` | mock 评测/红队结果 + 占位图表（真值待 A5） | 3 |
| `report_assets/` | 报告图表占位资产（标题含「模拟占位」，A5 闭环后一键替换） | 9 |

### 🏘️ 社区 / 课程 / 前端
| 文件 | 说明 |
|---|---|
| `FORUM_REVIEW.md` | 社区论坛 + 四层审核机制设计 |
| `E3_COURSE_CARDS.md` / `e3_cards.json` | 10 张身体权启蒙信息卡（青少版） |
| `E3_COURSE_LIST_OPTIONS.md` / `E4_DEMO_PAGE_OPTIONS.md` | 课程方向 / demo 页方案三选一记录 |
| `FRONTEND_POLISH_PROPOSAL.md` | 前端轻改造提案（暖珊瑚奶油色板） |

### 📄 报告 / PPT / PDF / 视频
| 文件 | 说明 | Day |
|---|---|---|
| `REPORT_安心答_分析报告.md` | 12 章正式报告（v2.2，C1/C6 已溯源闭环） | 9 |
| `presentation.pptx` | 18 页方案 PPT（评测页嵌占位图，待真值替换） | 10 |
| `proposal.pdf` | 1 页执行摘要 PDF | 10 |
| `demo_video_script.md` | 3–5 分钟演示视频分镜脚本（mp4 待你侧录制） | 7 |
| `REPORT_DATA_SLOTS.md` | 实测数据回填槽位图（A5 闭环当天 7 步剧本） | 9 |
| `MVP专家团打磨报告.md` | 8 角色联合评审 + P0/P1/P2 优先级矩阵 + 48h 行动表 | 8/14 |

### 🏷️ 品牌 / 商业 / 数据 / 合规
| 文件 | 说明 |
|---|---|
| `BRAND.md` | 品牌命名方案（乐天知性，已定稿） |
| `BUSINESS_VALUE.md` | 商业价值论证（founder-market fit + 排除广告变现） |
| `DATA_STRATEGY.md` | 数据来源与版权策略 |
| `ADULT_EXPO_SOURCES.md` / `ADULT_EXPO_COMPLIANCE.md` | 成人展来源调研 / 展讯合规边界说明 |

### 🗂️ 项目管理 + 开源
| 文件 | 说明 |
|---|---|
| `MVP_TIMELINE.md` | 12 天 MVP 冲刺表（本文件为最终态） |
| `OPEN_ISSUES.md` | 待核对问题清单（已闭环项归档底部） |
| `README.md` | 项目说明（结构/架构/安全/运行/开源） |
| `LICENSE` | MIT（Copyright 2026 乐天知性·安心答） |
| `.gitignore` | Python 缓存 / .env / .vscode / 日志 |
| `MVP_FREEZE_RELEASE.md` | 本文件 |

---

## 三、硬性红线合规自检（冻结前必过）

| 红线 | 结论 | 证据 |
|---|---|---|
| ① 18+ 年龄门永不可省 | ✅ 通过 | `index.html` 首屏硬性年龄验证；`adult_expo.html` 二次验证；未成年强制终止/分流，不降级放行 |
| ② 严格遵循 7 条安全规则 | ✅ 通过 | `SYSTEM_PROMPT.md` AGE_GATE / NO_PORN / CONSENT_FIRST / 自伤转介 / 暴力转介 / 医疗转介 / 来源标注；`smoke_test.py` 规则检测器可复验 |
| ③ API Key 绝不落库 | ✅ 干净 | 全仓 grep `sk-/AKIA/api_key/secret/password` 真实密钥模式 **0 命中**；仅 `smoke_test.py` 内 `sk-****` 脱敏占位与 `STEPFUN_API_KEY` 环境变量名；`.gitignore` 已忽略 `.env` |
| ④ 不复制蛇哥等创作者原话 | ✅ 通过 | 全文档原创表达；`DATA_STRATEGY.md` 明令「蛇哥原话不复制」；已约定不搬 PUA/物化框架 |
| ⑤ 仅项目目录内写文件 | ✅ 通过 | 本轮所有产出落在 `安心答-GOAI/`；记忆/日志在 `.workbuddy/`（项目内），未触碰用户个人目录 |
| ⑥ 不对外发消息 / 不自动部署 | ✅ 通过 | 未调用任何消息/部署/提交接口；GitHub 仅本地 commit+tag，未 push；8/16 提交待你手动完成 |

> 危机转介号码白名单（12356/12338/12355/110/120）依 `KB_CRISIS_HOTLINES.md` 核实，模型仅复述白名单、不得凭记忆生成——C4 已闭环；原定 2026-08-14 强制复核日，白名单口径未变，建议 8/16 前由你人工再扫一眼即可（低风险）。

---

## 四、已知缺口与是否阻塞提交

| 缺口 | 阻塞提交？ | 说明 / 处置 |
|---|---|---|
| **A5** kb_adult 真实检索跑分 | ❌ 不阻塞 | 唯一前置=你侧 Dify 切经济模式+重索引+重发布；跑通后我接 `eval_runner.py` 跑 152+47 → `eval_scorer.py` 出真值图回填报告§评测 + 补红队漏拦归因。现以「模拟占位·待回填」如实标注 |
| **Day 4 红队实测 / Day 5 论坛骨架** | ❌ 不阻塞 | 红队评分器链路（Day 3）已就绪；论坛设计文档 `FORUM_REVIEW.md` 已先于实现存在；均随 A5 一并补强 |
| **视频 mp4** | ⚠️ 视表单 | 仅 `demo_video_script.md` 脚本；若 goaihz.com 表单要求视频为必填，需你侧录屏配音，或附豁免说明 |
| **原型可达性** | ⚠️ 建议 | 评委打不开本地 HTML → 建议部署 Cloudflare Pages 自有域名，或提交时附「本地运行说明」 |
| **GitHub 公开仓** | ❌ 不阻塞 | 当前本地仓未 push；如需公开链接提交，需你提供远程/授权 |
| **G1 提交表单字段** | ❌ 不阻塞 | 待你提供 goaihz.com 表单字段清单，我据 `submission_checklist.md` 预先填齐核对 |

---

## 五、8/16 初赛提交剧本（指针）

完整步骤、故障预案、物料核对见 **`submission_checklist.md`**：
1. 登录 goaihz.com（账号 3073812933@qq.com）；
2. 填作品名称/赛道/简介/联系方式/原型链接/GitHub/视频链接/分类标签；
3. 附件：方案 PPT（`presentation.pptx`）+ PDF（`proposal.pdf`）+ 报告（markdown）+ 原型（`index.html`）；
4. 截屏存证。

---

## 六、版本与提交记录

```
v1.0-freeze  ← 本冻结态（2026-08-14 心跳收尾）
  └─ ef53507  docs: MVP开发专家团联合打磨（v2.2）   ← 报告 C1/C6 溯源闭环
  └─ ecd0ca2  docs: 报告打磨至 v2.1
  └─ 2997c55  MVP v1.0 乐天知性·安心答 — GOAI 赛道二参赛交付物（81 文件初建档）
```

> 本地标签 `v1.0-freeze` 已打；未 push（按你 8/14 决策：本地建仓+提交，暂不公开）。

---

## 七、待你拍板 / 提供（提交前）

- [ ] **G1** goaihz.com 初赛提交表单字段清单（截图或列出必填项）
- [ ] **原型可达性**：部署 Cloudflare Pages（需限定域名短效 Token）还是交本地运行说明？
- [ ] **GitHub**：是否 push 公开仓（需远程地址或 gh 授权）？
- [ ] **视频 mp4**：是否需录制（表单是否必填视频）？
- [ ] **A5（可选）**：回 Dify 后台确认 kb_adult 索引已通，发我「kb_adult 已通」即触发真实跑分回填
- [ ] **C4 复核（低风险）**：8/14 复核日，白名单口径未变，建议 8/16 前人工再扫一眼

---

*本说明由持续推进心跳任务（automation-1785770169329）于 2026-08-14 收尾生成，对应 `MVP_TIMELINE.md` Day 12 MVP 冻结。*
