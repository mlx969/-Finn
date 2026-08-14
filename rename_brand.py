import os, io

BASE = r"C:/ProgramData/WorkBuddy/users/17d0d283/WorkBuddy/idea/安心答-GOAI"

reps = {
    "EVAL_REDTEAM.md": [
        ("# 安心答 · 评测方案与红队测试（EVAL & RED TEAM）",
         "# 乐天知性（安心答）· 评测方案与红队测试（EVAL & RED TEAM）"),
    ],
    "FORUM_REVIEW.md": [
        ("# 安心答 · 社区论坛与四层审核机制设计",
         "# 乐天知性（安心答）· 社区论坛与四层审核机制设计"),
        ('AI 助手在论坛内以"安心答"身份置顶',
         'AI 助手在论坛内以"安心答"（乐天知性）身份置顶'),
    ],
    "KNOWLEDGE_BASE.md": [
        ("# 安心答 · 知识库权威来源清单（RAG Knowledge Base Sources）",
         "# 乐天知性（安心答）· 知识库权威来源清单（RAG Knowledge Base Sources）"),
        ("构建「安心答」RAG 知识库",
         "构建「安心答」（乐天知性）RAG 知识库"),
    ],
    "MVP_TIMELINE.md": [
        ("# 安心答 · MVP 12 天冲刺表（8/3 → 8/15）",
         "# 乐天知性（安心答）· MVP 12 天冲刺表（8/3 → 8/15）"),
    ],
    "README.md": [
        ("# 安心答（AnXinDa）· GOAI 赛道二参赛项目",
         "# 乐天知性（安心答）· GOAI 赛道二参赛项目"),
    ],
    "REPORT_安心答_分析报告.md": [
        ("# 安心答（AnxinDa）· GOAI 世界人工智能开源大赛 项目分析报告",
         "# 乐天知性（安心答）· GOAI 世界人工智能开源大赛 项目分析报告"),
        ("「安心答」是一个面向 **18 岁以上人群**的性健康与亲密关系 AI 助手",
         "「安心答」是「乐天知性」旗下、面向 **18 岁以上人群**的性健康与亲密关系 AI 助手"),
    ],
    "SYSTEM_PROMPT.md": [
        ("# 安心答 · Agent System Prompt（可直接粘贴到 Dify / Coze / FastGPT）",
         "# 乐天知性（安心答）· Agent System Prompt（可直接粘贴到 Dify / Coze / FastGPT）"),
        ("> 用途：作为「安心答」AI 性健康与亲密关系陪伴助手的核心系统提示词。",
         "> 用途：作为「安心答」（乐天知性旗下）AI 性健康与亲密关系陪伴助手的核心系统提示词。"),
        ("你是「安心答」——一个面向",
         "你是「安心答」（乐天知性旗下 AI 陪伴助手）——一个面向"),
    ],
    "gen_eval.py": [
        ("安心答 · 评测测试集 + 红队攻击表 生成器",
         "乐天知性（安心答）· 评测测试集 + 红队攻击表 生成器"),
    ],
    "index.html": [
        ("<title>安心答 · AI 性健康与亲密关系陪伴（GOAI 演示原型）</title>",
         "<title>乐天知性（安心答）· AI 性健康与亲密关系陪伴（GOAI 演示原型）</title>"),
        ("<h1>🔞 安心答 · 仅限成年人</h1>",
         "<h1>🔞 乐天知性 · 安心答 | 仅限成年人</h1>"),
        ("💬 安心答助手", "💬 安心答（乐天知性）"),
        ('<div class="topbar" id="topbar">安心答 · AI 性健康与亲密关系陪伴</div>',
         '<div class="topbar" id="topbar">乐天知性 · 安心答 | AI 性健康与亲密关系陪伴</div>'),
        ("chat:'安心答 · AI 性健康与亲密关系陪伴'",
         "chat:'乐天知性 · 安心答 | AI 性健康与亲密关系陪伴'"),
        ("你是「安心答」——面向18岁以上成年人",
         "你是「安心答」（乐天知性旗下 AI 陪伴助手）——面向18岁以上成年人"),
        ("📌 安心答 · 项目说明", "📌 乐天知性 · 项目说明（安心答）"),
    ],
}

for fn, lst in reps.items():
    p = os.path.join(BASE, fn)
    with io.open(p, "r", encoding="utf-8") as f:
        txt = f.read()
    total = 0
    for old, new in lst:
        c = txt.count(old)
        if c == 0:
            print(f"[WARN] not found in {fn}: {old[:40]}")
        txt = txt.replace(old, new)
        total += c
    with io.open(p, "w", encoding="utf-8") as f:
        f.write(txt)
    print(f"[OK] {fn}: {total} replacements")
print("DONE")
