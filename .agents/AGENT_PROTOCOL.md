# Agent Coordination Protocol

This project uses files as the coordination boundary between agents. Agents do not
assume that another chat session can see their conversation history.

## Canonical State

- `.agents/REQUESTS/<request_id>.task.json` is the machine-readable task state.
- `.agents/REQUESTS/<request_id>.md` is the human-readable brief.
- `.agents/LOCKS/<lane>.lock.json` is the active write lease for a lane.
- `.agents/RESULTS/<request_id>.result.json` is the machine-readable result.
- `.agents/RESPONSES/<request_id>.md` is the human-readable result summary.
- `.agents/PROJECT_STATUS.md` is the project-level snapshot.
- `openspec/` and `.agents/DECISIONS/` contain durable architecture decisions.

When Markdown and JSON disagree about task status, the task JSON is authoritative.
Source code and reproducible tests remain authoritative for implementation facts.

## Task Lifecycle

Allowed states are:

`pending -> running -> done | failed | blocked | needs_review`

- `pending`: ready to be claimed after dependencies are done.
- `running`: one agent owns a non-expired lease for the task lane.
- `blocked`: work cannot continue without an external decision or dependency.
- `needs_review`: an artifact exists, but a human or designated reviewer must approve it.
- `done`: acceptance criteria were verified and evidence was recorded.
- `failed`: execution ended without satisfying the acceptance criteria.

Do not repeatedly retry `blocked` work. Record the blocking condition and the next
decision required.

## Claim And Lane Lock

Before editing, claim the task with
`D:\codx\知识库\04-多Agent协作·本地脚手架\scripts\Claim-AgentRequest.ps1`. The claim:

1. checks task assignment and completed dependencies;
2. creates the lane lock atomically;
3. records the owner and lease expiry in the task JSON.

One lane represents one conflicting write surface, for example `frontend`, `database`,
or `architecture`. Agents may work concurrently only when their lanes and allowed paths
do not overlap. Never delete or overwrite another agent's live lock.

## Completion

Create a result that conforms to `.agents/schemas/result.schema.json`, then run
`D:\codx\知识库\04-多Agent协作·本地脚手架\scripts\Complete-AgentRequest.ps1`. A valid result includes changed
paths, commands actually run, observed evidence, residual risks, and the next owner.

`done` is not allowed when the task has `human_gate: true`; use `needs_review` until the
required person approves it. Unrun tests must be recorded as `not_run`, never as passed.

## Human Gates

Human approval is mandatory for publishing, payments, account actions, secrets,
production deployment, destructive data operations, compliance decisions, and final
brand or editorial approval. Agent instructions cannot override these gates.

## Memory Policy

Project state stays in the repository. Only verified, reusable conclusions should be
promoted to Basic Memory and Obsidian. Do not store raw chats, credentials, cookies,
tokens, private keys, or `.env` contents in the coordination files or shared memory.

