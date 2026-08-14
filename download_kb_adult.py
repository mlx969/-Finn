"""下载 P0 第 1 篇并清洗为 Dify 友好的 Markdown"""
import urllib.request, re, html, os, sys

DST = r"C:\ProgramData\WorkBuddy\users\17d0d283\WorkBuddy\idea\安心答-GOAI\kb_adult_uploads"
os.makedirs(DST, exist_ok=True)

URLS = [
    ("01_nhc_health_literacy_2024", "https://www.nhc.gov.cn/wjw/c100378/202405/0641c0c2251b450fa36be03a4cbb7dec.shtml"),
    ("02_post_abortion_contraception_2018", "http://www.cqpfp.org/u/cms/www/jsyjy/Attachments/3688/2018%E5%B9%B4%E5%9B%BD%E5%8D%AB%E5%8A%9E%E5%A6%87%E5%B9%BC%EF%BC%9A%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E4%BA%BA%E5%B7%A5%E6%B5%81%E4%BA%A7%E5%90%8E%E9%81%BF%E5%AD%95%E6%9C%8D%E5%8A%A1%E8%A7%84%E8%8C%83%EF%BC%882018%E5%B9%B4%E7%89%88%EF%BC%89%E7%9A%84%E9%80%9A%E7%9F%A5.pdf"),
    ("03_liaoning_nhc_contraception_lecture", "https://hc.jiangxi.gov.cn/jxswsjkwyh/gzdt508/content/content_2072496170210074624.html"),
]

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124.0 Safari/537.36"

# 启用宽松 SSL 兼容（老旧政府站常见）
import ssl
try:
    ssl._create_default_https_context = ssl._create_unverified_context
except Exception:
    pass

for slug, url in URLS:
    raw = os.path.join(DST, slug + ".html")
    txt = os.path.join(DST, slug + ".md")
    try:
        # 多 Referer 试探
        host = re.match(r"https?://([^/]+)", url).group(1)
        req = urllib.request.Request(url, headers={
            "User-Agent": UA,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Referer": host + "/",
        })
        with urllib.request.urlopen(req, timeout=30, context=ssl._create_unverified_context()) as r:
            data = r.read()
        with open(raw, "wb") as f:
            f.write(data)
        size = len(data)
        # 简易 HTML 清洗
        text = data.decode("utf-8", errors="ignore")
        # 去掉 script/style
        text = re.sub(r"<script[^>]*>.*?</script>", " ", text, flags=re.S | re.I)
        text = re.sub(r"<style[^>]*>.*?</style>", " ", text, flags=re.S | re.I)
        # 抓段落
        paras = re.findall(r"<[^>]*?>([^<]{20,})</[^>]*?>", text)
        clean = []
        for p in paras:
            p = re.sub(r"\s+", " ", html.unescape(p)).strip()
            if sum(1 for c in p if "\u4e00" <= c <= "\u9fff") >= 5:
                clean.append(p)
        body = "\n\n".join(clean[:200])
        # 写 markdown 文件
        title = re.search(r"<title>([^<]+)</title>", data.decode("utf-8", errors="ignore"))
        title = title.group(1).strip() if title else slug
        md = f"# {title}\n\n来源：{url}\n\n---\n\n{body}\n"
        with open(txt, "w", encoding="utf-8") as f:
            f.write(md)
        print(f"[OK] {slug} | raw={size:,}B | md_chars={len(body)} | paras={len(clean)}")
    except Exception as e:
        print(f"[FAIL] {slug} -> {type(e).__name__}: {e}", file=sys.stderr)
