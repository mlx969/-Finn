# -*- coding: utf-8 -*-
"""Day 10 — proposal.pdf：1 页执行摘要（PPT 的 PDF 备选）。"""
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                TableStyle, HRFlowable)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "proposal.pdf")

# CJK 字体（优先系统雅黑，缺失则回退）
FONT = "Helvetica"
candidates = [
    "C:/Windows/Fonts/msyh.ttc",
    "C:/Windows/Fonts/msyh.ttf",
    "C:/Windows/Fonts/simhei.ttf",
]
for c in candidates:
    if os.path.exists(c):
        try:
            pdfmetrics.registerFont(TTFont("CJK", c))
            FONT = "CJK"
            break
        except Exception:
            pass

CORAL = colors.HexColor("#F2527A")
INK = colors.HexColor("#2E2A33")
PLUM = colors.HexColor("#7A4A57")
GREY = colors.HexColor("#938B97")
CREAM = colors.HexColor("#FFF5F8")

ss = getSampleStyleSheet()
H1 = ParagraphStyle("H1", fontName=FONT, fontSize=20, textColor=INK, leading=24, spaceAfter=2)
SUB = ParagraphStyle("SUB", fontName=FONT, fontSize=10.5, textColor=PLUM, leading=14, spaceAfter=4)
H2 = ParagraphStyle("H2", fontName=FONT, fontSize=12, textColor=CORAL, leading=15, spaceBefore=6, spaceAfter=3)
BODY = ParagraphStyle("BODY", fontName=FONT, fontSize=9.2, textColor=INK, leading=13, spaceAfter=2)
NOTE = ParagraphStyle("NOTE", fontName=FONT, fontSize=8, textColor=colors.HexColor("#B0303A"), leading=11, spaceBefore=2)
FOOT = ParagraphStyle("FOOT", fontName=FONT, fontSize=7.5, textColor=GREY, leading=10)

doc = SimpleDocTemplate(OUT, pagesize=A4,
                        leftMargin=16*mm, rightMargin=16*mm,
                        topMargin=14*mm, bottomMargin=12*mm,
                        title="乐天知性(安心答)·参赛方案执行摘要",
                        author="安心答 GOAI 项目")
E = []

E.append(Paragraph("乐天知性 · 安心答", H1))
E.append(Paragraph("AI + 性健康与亲密关系 · 社会学升维陪伴 + 适龄双版本 &nbsp;|&nbsp; GOAI 世界人工智能开源大赛 · 赛道二 无界应用 &nbsp;|&nbsp; MIT 开源", SUB))
E.append(HRFlowable(width="100%", thickness=1.5, color=CORAL, spaceAfter=6))

def block(title, lines):
    E.append(Paragraph(title, H2))
    for ln in lines:
        E.append(Paragraph("• " + ln, BODY))

block("我们解决什么", [
    "性教育长期「学校不敢讲、家庭不会讲、网络乱讲」；市面只有教科书式(枯燥)或猎奇擦边(无护栏、夹带PUA)两类极端。",
    "视角空白：内容只在「知识」层打转，缺把个体困惑与原生家庭/阶层/身份挂钩的「升维」解释——年轻人最想被理解的维度。",
    "适龄段空白：现有性健康 bot 几乎全 18+ 成人向，未成年版(12–18)全球无人占；青少年早熟≠懂，处于高风险区。",
])
block("差异化定位（核心评分点）", [
    "做「第四类」：知识 + 结构视角 + 适龄分级 + 安全 + 社区；不做教科书/猎奇/PUA 物化。",
    "五层架构：知识 → 升维 → 多元(去污名,consent前置) → 社群(18+论坛+展讯) → 适龄(未成年版动漫/游戏化,物理隔离)。",
    "双版本壁垒：身份/年龄认证分流，后端双应用物理隔离；绝不性化未成年人，未成年版零色情/零性暗示/零SM。",
])
block("系统架构 & 已跑通", [
    "成年版 Chatflow 5 节点链路已在 Dify 实跑：用户输入 → kb_adult 检索(TopK=3) → 条件分支 → 阶跃 Step 3.7 Flash + 7条规则 → 回复(含来源)。",
    "技术栈：阶跃 StepFun + Dify Chatflow(主力,可私有化) + FastGPT(对照) + ShieldLM-6B/LlamaGuard S1–S13/DFA(四层审核) + 单文件 index.html + Cloudflare Pages。",
])
block("安全合规（核心评分点）", [
    "18+ 硬门槛(第一道墙) + 七条强制安全规则(AGE_GATE/NO_PORN/CONSENT_FIRST/SELF_HARM/VIOLENCE/MEDICAL/SOURCE_TAG)。",
    "四层审核 + Llama Guard S4(儿童性剥削)零容忍硬拦；危机转介用已核实热线白名单(12356/12338/12355/110/120)，设过期复核。",
])
block("评测方案（核心评分点）", [
    "三组对照：A 裸模型 / B Dify版(主方案) / C FastGPT版；测试集 152 条(知识37/升维37/安全38/拒答转介40)；红队 47 条。",
    "五维评分 Rubric(0–2)：知识准确/升维质量/安全合规/拒答恰当/引用规范；红队以拦截率为核心指标。",
])
E.append(Paragraph("⚠️ 评测/红队真题图因 kb_adult 检索空(A5)未闭环，仍为「模拟占位」，待 A5 闭环按 REPORT_DATA_SLOTS.md 一键替换为实测 v1；评分器为正则启发式自动初筛分，非人工评分。", NOTE))

block("开源贡献 & 落地", [
    "MIT 开源：index.html 原型 / SYSTEM_PROMPT(+MINOR) / 知识库索引 / 评测红队套件 / 双版本与品牌设计文档；公开升维框架+四层审核+适龄分级范式。",
    "比赛：goaihz.com 报名 → 初赛(8/16截止) → 复赛(8/25–9/3) → 决赛(9/22–23 杭州)。真实上线需 ICP+网文证+内容审查，Key 经密钥管理注入不落库。",
])

E.append(Spacer(1, 4))
E.append(HRFlowable(width="100%", thickness=0.8, color=GREY, spaceAfter=3))
E.append(Paragraph("边界声明：本项目是教育辅助工具，非医疗/心理咨询替代品。关键节点 🟢 8/15 MVP 冻结 ｜ 🔴 8/16 初赛提交。", FOOT))

doc.build(E)
print("SAVED PDF:", OUT)
