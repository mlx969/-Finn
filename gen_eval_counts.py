#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
安心答 — 评测集分类计数生成器 (gen_eval_counts.py)

用途：
  把 `eval_testset.csv` 按题型映射为报告使用的四类，输出真实、可复现的分类数量。
  报告 / PPT / PDF 中的数据集数字必须来自本脚本的输出，禁止硬编码旧进度文档里的数字。

分类口径（评委可据此重新核对）：
  知识类（事实问答）      ← KNOWLEDGE
  升维类（结构归因陪伴）  ← EMPOWER
  安全类（边界/同意/防护）← SAFETY
  拒答·转介类（越界/危机/医疗/暴力转介）← REFUSE_PORN, REFUSE_MINOR, REFUSE_MANIP, OOS,
                                           REDIRECT_MED, REDIRECT_VIO, REDIRECT_CRISIS

用法：
  python gen_eval_counts.py                 # 打印四类计数 + 合计 + 红队数
  python gen_eval_counts.py --json          # 仅输出 JSON，便于被其它脚本/CI 引用
"""
import argparse
import csv
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
EVAL_CSV = os.path.join(HERE, "eval_testset.csv")
REDTEAM_CSV = os.path.join(HERE, "redteam_prompts.csv")

# 题型 → 报告四大类
TYPE_TO_CAT = {
    "KNOWLEDGE": "知识",
    "EMPOWER": "升维",
    "SAFETY": "安全",
    "REFUSE_PORN": "拒答·转介",
    "REFUSE_MINOR": "拒答·转介",
    "REFUSE_MANIP": "拒答·转介",
    "OOS": "拒答·转介",
    "REDIRECT_MED": "拒答·转介",
    "REDIRECT_VIO": "拒答·转介",
    "REDIRECT_CRISIS": "拒答·转介",
}
CATEGORIES = ["知识", "升维", "安全", "拒答·转介"]


def count_eval(path=EVAL_CSV):
    counts = {c: 0 for c in CATEGORIES}
    total = 0
    with open(path, encoding="utf-8-sig", newline="") as f:
        for r in csv.DictReader(f):
            t = (r.get("expected_type") or "").strip().upper()
            cat = TYPE_TO_CAT.get(t, "拒答·转介")
            counts[cat] += 1
            total += 1
    return counts, total


def count_redteam(path=REDTEAM_CSV):
    total = expect_intercept = 0
    with open(path, encoding="utf-8-sig", newline="") as f:
        for r in csv.DictReader(f):
            total += 1
            if (r.get("expect_intercept") or "").strip().lower() == "true":
                expect_intercept += 1
    return total, expect_intercept


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true", help="只输出 JSON")
    ap.add_argument("--eval-csv", default=EVAL_CSV)
    ap.add_argument("--redteam-csv", default=REDTEAM_CSV)
    args = ap.parse_args()

    counts, total = count_eval(args.eval_csv)
    rt_total, rt_intercept = count_redteam(args.redteam_csv)
    out = {
        "eval_total": total,
        "categories": counts,
        "redteam_total": rt_total,
        "redteam_expect_intercept": rt_intercept,
        "sum_check": sum(counts.values()),
    }
    if args.json:
        print(json.dumps(out, ensure_ascii=False))
        return
    print(f"评测集总数：{total}")
    for c in CATEGORIES:
        print(f"  · {c}：{counts[c]}")
    print(f"四类合计（应与总数一致）：{out['sum_check']}  {'✅' if out['sum_check'] == total else '❌ 不一致'}")
    print(f"红队集总数：{rt_total}（预期拦截 {rt_intercept}）")


if __name__ == "__main__":
    main()
