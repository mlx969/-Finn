import sys, json, urllib.request, urllib.error

KEY = sys.argv[1]
Q = sys.argv[2]
url = "https://api.dify.ai/v1/chat-messages"
data = json.dumps({"inputs": {}, "query": Q, "user": "eval-probe", "response_mode": "blocking"}).encode("utf-8")
req = urllib.request.Request(url, data=data, headers={
    "Authorization": "Bearer " + KEY,
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36",
})
try:
    with urllib.request.urlopen(req, timeout=90) as r:
        resp = json.loads(r.read().decode("utf-8"))
    ans = resp.get("answer", "(none)")
    print("ANSWER[:480]:", ans[:480].replace("\n", " "))
except urllib.error.HTTPError as e:
    print("HTTPERROR:", e.code, e.read().decode("utf-8")[:300])
except Exception as e:
    print("ERR:", repr(e))
