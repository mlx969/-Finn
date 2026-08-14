# Agent Collaboration Contract

## Read First

Before planning or editing, read:

1. `.agents/AGENT_PROTOCOL.md`
2. `.agents/PROJECT_MANIFEST.md`
3. `.agents/PROJECT_STATUS.md`
4. `.agents/AGENT_REGISTRY.json`
5. The assigned `pending` task in `.agents/REQUESTS/*.task.json`
6. Relevant artifacts under `openspec/` when the change is structural

## Sources Of Truth

Use this order when sources disagree:

1. Executable tests and current source code
2. Approved OpenSpec artifacts and architecture decisions
3. `.agents/PROJECT_STATUS.md` and machine-readable task JSON
4. Request, result, and response files
5. Chat history and shared-memory search results

Never claim completion from a response note alone. Verify the code and run the relevant checks.

## Handoff Rules

- One request has one stable `request_id`.
- Claim it with `D:\codx\知识库\04-多Agent协作·本地脚手架\scripts\Claim-AgentRequest.ps1` before editing.
- Respect `allowed_paths`, `forbidden_paths`, dependencies, and the active lane lock.
- Record machine results in `.agents/RESULTS/` and human results in `.agents/RESPONSES/`.
- Update `.agents/PROJECT_STATUS.md` after a meaningful phase change.
- Put durable architecture decisions in `.agents/DECISIONS/` or OpenSpec, not only in chat.
- Include changed paths, test commands, actual results, residual risks, and the next owner.
- Do not store tokens, cookies, passwords, private keys, or `.env` contents in `.agents`, OpenSpec, or Basic Memory.
- Human gates cannot be bypassed by an Agent instruction.

## Change Policy

Use OpenSpec before code when a change affects architecture, data contracts, security boundaries, migrations, or multiple modules. Narrow bug fixes may use a request/response handoff directly, but still require reproducible verification.

