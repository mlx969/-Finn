# GitHub Copilot Project Instructions

This repository participates in a local multi-agent workflow. Do not rely on chat
history as project state.

Before planning or editing:

1. Read `.agents/AGENT_PROTOCOL.md`.
2. Read `.agents/PROJECT_MANIFEST.md` and `.agents/PROJECT_STATUS.md`.
3. Read `.agents/AGENT_REGISTRY.json`.
4. Find the assigned `pending` task under `.agents/REQUESTS/*.task.json`.
5. For architecture or cross-module work, read the linked OpenSpec change first.

Before changing files, claim the request with:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File "D:\codx\知识库\04-多Agent协作·本地脚手架\scripts\Claim-AgentRequest.ps1" -ProjectPath "C:\ProgramData\WorkBuddy\users\17d0d283\WorkBuddy\idea\安心答-GOAI" -RequestId "<request_id>" -Agent "github-copilot"
```

Work only inside the task's `allowed_paths`. Do not touch `forbidden_paths`, secrets,
or another agent's locked lane. Preserve unrelated user changes.

At completion, create a JSON result conforming to
`.agents/schemas/result.schema.json`, then finalize it with:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File "D:\codx\知识库\04-多Agent协作·本地脚手架\scripts\Complete-AgentRequest.ps1" -ProjectPath "C:\ProgramData\WorkBuddy\users\17d0d283\WorkBuddy\idea\安心答-GOAI" -RequestId "<request_id>" -Agent "github-copilot" -ResultPath "<result.json>"
```

Never report a test as passing unless it was actually run. Publishing, payments,
account operations, credentials, production deployment, destructive data changes,
compliance decisions, and final editorial approval always require a human gate.

