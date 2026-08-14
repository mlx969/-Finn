# kb_adult 检索全空 · 修复适配教程（含两条路）

> 写在前面：**优先走修法 A（删 KB 重建 + 选经济模式）**，30 秒见效、零配置、零 key，最稳。
> 修法 B 是真的配不起 embedding key 或想高质量长期用的备选。

---

## 症状

- 所有问题（包括"你好"）返回**空回答**或**"暂无权威资料"兜底**
- 元数据：`retriever_resources: []`、`usage: {tokens:0, time_to_generate:0}`
- 报错（如果开了 Debug）：`[models] Connection Error, 404 NOT_FOUND. Model is not found: models/embedding-001`

根本原因：你之前把 `kb_adult` 索引模式切成「**高质量**」，高质量要求一个 embedding 模型把 query 转向量再去库内检索。Dify 默认配的是 **Google Gemini 的 `models/embedding-001`**（你 Dify 里没配 / v1beta 接口找不到）→ 整个工作流崩。

青少版没事，因为它用的是「**经济模式**」（Dify 自带免费 embedding）。

---

## ✅ 修法 A · 推荐（5-10 分钟）

**原理**：Dify 禁止 KB"降级"，但可以删了重建。新 KB 默认让你重新选模式，**这次选经济**就行。

### 步骤

1. **左下保存配置**（截图两个 KB 文档的位置：Dify 知识库 → `kb_adult` → 看一眼两个文件名，等会儿重传要）。文件名：

   - `01_zhongguo_gongmin_jiangkang_suyang_2024.md`
   - `03_liaoning_nhc_kexue_biyun_jiangzuo.md`

2. **Dify 左侧 → 知识库 → 点 `kb_adult` → 右上角 ⋯ → 删除知识库**
   - 弹窗确认 → 输入 `kb_adult` 或点「确认删除」

3. **回知识库列表 → 创建知识库**
   - 名称：`kb_adult`（必须同名，否则 Chatflow 节点绑定会断）
   - **索引模式：勾"经济"**（默认就是经济，确认一下别勾到高质量）
   - 嵌入模型自动锁定 "embedding-3-small" 或"Dify 自带"——不要碰
   - 检索设置：`top_k` 默认 5 / `score_threshold` 默认 0.5，不用改
   - 点「创建」

4. **进新 kb_adult → 「新增文档」**
   - 把刚才那两个 md 文件拖进去（路径 `C:\ProgramData\WorkBuddy\users\17d0d283\WorkBuddy\idea\安心答-GOAI\kb_adult_uploads\`）
   - 文件名不带 `.md` 后缀的标记一下源文档，方便审计
   - 处理模式保持「自动」

5. **等 3-5 分钟**（状态从"索引中"变"已完成"）

6. **回成年版 Chatflow → 双击「知识检索」节点**
   - 重新在「知识库」下拉选 `kb_adult`（同名会自动出现在前几行）
   - top_k 设 **3**、score_threshold 设 **0.5**
   - 保存

7. **改完必须重新点右上「发布」**（预览不刷新，老 bug）

### 验证

在 Chatflow「预览」输入 `安全期是哪几天`，期望：
- ✅ 回答中出现「《中国公民健康素养 2024》」「根据第 22 条」这类引用
- ✅ 元数据 `retriever_resources` 显示非空（含 `01_zhongguo_gongmin_jiangkang_suyang_2024`）

---

## 🛠 修法 B · 完整 step-by-step（次选）

> 适用场景：你想保留"高质量"索引的语义精度，或者你之前**已经折腾过设置报错**——这种情况 B 的成功率要看你 Dify 是否能配到下表的 provider。

### 第一步 · 看 Dify 里有哪些 embedding provider

Dify 右上角「**设置**」→「**模型供应商**」→ 看左侧列表里**有没有下面任一项**，点进去看状态：

| Provider | 是否需要 Key | Key 获取难度 | 推荐度 |
|---|---|---|---|
| **Jina AI** | ✅ 要 Jina API Key | 🟢 简单（jina.ai 免费注册送 1M tokens） | ⭐⭐⭐ |
| **OpenAI** | ✅ 要 OpenAI Key | 🟠 需科学上网 + 余额 | ⭐ |
| **Cohere** | ✅ 要 Cohere Key | 🟡 可邮箱注册试额度 | ⭐⭐ |
| **Hugging Face Hub** | ✅ 要 HF Key | 🟡 部分模型需同意条款 | ⭐⭐ |
| **硅基流动 SiliconFlow** | ✅ 要 SF Key | 🟢 国内厂商，免费额度 | ⭐⭐⭐ |
| **Google Gemini** | ❌ 不要 key（如果你能访问 Google） | 🔴 你 Dify 里就是这个坏的 | ❌ |
| **阶跃 StepFun** | 插件支持 LLM，不确定 embedding | 🟡 看 1.2 节 | ⚠️ |

> **国内用户最稳的免费 embedding**：**硅基流动 SiliconFlow**。
> 注册送 2000 万 tokens，足够 kb_adult 索引 + 跑 152+47 测试。
> 链接：https://siliconflow.cn/
>
> **更省事**：直接走**修法 A**（经济模式），不需要任何 provider 配 key。

### 第二步 · 配置 provider（以 Jina 为例）

> 如果你选硅基流动，步骤一样。

1. 去 provider 官网注册 → 创建 API Key → **复制**（例如 Jina: `jina_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`）
2. 回 Dify 「设置 → 模型供应商」→ 点「Jina AI」（或你选的 provider）
3. 填 API Key → 保存 → 旁边会出现「**测试连接**」按钮 → 点一下确认绿灯
4. 列表里这个 provider 状态从「未配置」变「**已配置**」

⚠️ **Key 别贴在聊天里**——Dify 的 UI 框直接粘就行，粘完视觉不可见回显，安全。

### 第三步 · 改 KB 的 embedding 模型

1. **知识库 → 点 `kb_adult`**（不用删！）
2. 右上角「**设置**」图标（齿轮）→ 在「Embedding 模型」下拉里**找一个不是你现在的** provider
3. 我推荐选 `text-embedding-3-small`（OpenAI）或 `BAAI/bge-m3`（硅基流动，中文友好）—— 选你能配成功的那一个
4. 点「保存」→ Dify 自动**重新索引**所有已有文档（5-15 分钟）

> ⚠️ 重新索引过程里如果再报同款 404，就是这个新 embedding 也没配好，立刻看「模型供应商」里状态，必要时删除 KB 重建（修法 A）。

### 第四步 · 重绑 + 发布

1. 回成年版 Chatflow → 双击「**知识检索**」节点
2. 「知识库」选 `kb_adult`（应该自动保持）→ top_k 3 → score_threshold 0.5 → 保存
3. **重新点「发布」**

### ⚠️ 第 3 步最容易漏（配好 embedding 后 retriever 仍空的根因）

很多人在「模型供应商」里加完 embedding 就以为完了，但 **KB 默认还在用旧的（404 的）embedding 配置**。必须回到 KB 设置手动切过去 + 重索引，否则检索仍会走失效的旧配置返回空：

1. 知识库 → 点 `kb_adult` → 右上「设置」(齿轮)
2. 找「**Embedding 模型**」下拉 → **必须手动选 `BAAI/bge-m3`**（或你加的那个），不能留空 / 留旧的
3. 点「保存」→ 弹「确定重索引吗」→ **点确定**
4. 等状态从「索引中」变「**已完成**」（2 个小 md 约 2-5 分钟）
5. 回 Chatflow 重新「发布」

**30 秒自检 3 点**（配完还是空时查）：
- ① KB 文档状态是「**已完成**」还是「处理中」？→ 处理中 = 重索引没跑完，等 5 分钟再测
- ② KB 设置里 Embedding 模型是不是 `BAAI/bge-m3`？→ 不是就切过去 + 重索引
- ③ 成年版 Chatflow 重新点「**发布**」了吗？→ Dify 不自动感知 embedding 变化

### 验证

跟修法 A 的验证一样：发「安全期是哪几天」，`retriever_resources` 应非空，回答里出现引用。

---

## 🩹 如果又报错（兜底方案）

### 报错 A：`404 NOT_FOUND` 还是老 Gemini 名

→ 你没改成功。回去 kb_adult 的「设置」，确认 Embedding 下拉里**真的不是 Gemini embedding-001**。如果是空的，请「模型供应商」里装好你选的 provider 再回来。

### 报错 B：`Connection Error` / `timeout`

→ Provider 的 endpoint 不通。你的供应商 key 有问题或国内访问受限：
- 国内用户用 Jina 可能被墙，改用 **硅基流动**
- 硅基流动还 timeout，看是不是网络问题，直接回**修法 A**

### 报错 C：`Dimension mismatch`（向量维度对不上）

→ 你换了 provider 但 KB 还是按旧向量。务必让 Dify 自动**完整重索引**所有文档（不要复用旧向量）。等索引状态变「已完成」再测。

### 报错 D：啥都没报，但回答还是空

→ 检查条件分支：看你成年版那版是不是被我之前修的 "知识检索 result 为空 → 直接回复 2" 兜底，**先把 ELSE 那条「直接回复 2」先临时清空**，跑一条测试；如果清空后能回 LLM 答案 = 条件分支正常工作，可以把兜底话术重新填回去。

---

## ⚠️ 终极回滚：还是不行就回到「直接对话 + 不挂知识库」

如果上面都失败，最省事方案：
- 把成年版 Chatflow 的「知识检索」节点**完全删掉**
- 让条件分支只有**一条路：用户输入 → LLM**
- LLM 节点 SYSTEM 里加一句「如遇需权威数据问题，可基于常识回答并注明『以下回答基于训练知识，非实时文献；若需最新窗口期口径建议咨询当地疾控中心』」
- 先跑通链路，**先把 152+47 基线分数拿到手**再说优化

**这样最差也能跑基线**，等评委看分再补 kb_adult（基线本身就是评审硬通货）。

---

## 🚀 修好后下一步（告诉你即可我接着跑）

告诉我以下任一信号：
- "已删重建" → 我立刻复测检索 → 跑成年版 152+47 基线
- "已配 Jina / 硅基流动" → 我先看 setting 截图确认 → 再跑基线
- "我懒得配，还是回退到 直接对话模式" → 我帮你改 Chatflow + 把 prompt 里加免责声明

立刻给一份完整 step-by-step 加 fallback + 回滚，不再让你像我昨天那样"凭印象猜路径"。
