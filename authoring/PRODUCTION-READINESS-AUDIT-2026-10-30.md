# Production readiness audit — 2026-10-30

Status: evidence audit only. Not CI, owner acceptance, human review or sufficient
coverage.

## Snapshot

- HEAD: `7edfab8c`
- Section index snapshot: `e7496a664281afd4a1fff483f68780107a9541e3771a44741322751322dfe8fa`
- Qrels v4 page and section: 150 queries, same snapshot, AI-adjudicated.
- Book/atlas/edition/generated unchanged by search work.

## Defaults

| Surface | Default |
|---|---|
| BM25 weights | title 5, heading 2, body 0.5 |
| MCP `section_rerank` | false |
| Core API/CLI | explicit BM25 |
| Margin gate | opt-in; schema default .05 |
| Best mode | opt-in |

## Quality

Global BM25 page/section hit@1/3/5:

- page: .593/.847/.953;
- section: .480/.700/.793.

Layer-scoped:

- atlas v11: 1.000/1.000/1.000;
- V12: .767/.933/1.000 page, .567/.733/.800 section;
- all: .707/.887/.960 page, .593/.740/.800 section.

## Runtime

- warm BM25 p50 **66.7 ms**, p95 **79.7 ms**;
- warm best p50 216.5 ms, p95 420.4 ms;
- in-process concurrency cap **2**;
- 730 tests pass; premerge PASS; boundary PASS.

## Known limits and blockers

- No human review, CI, owner acceptance or sufficient coverage.
- Qrels v4 candidate pools 4–10, pool-relative.
- B01–B03 cover 12 volumes/15 topics but the remaining book is not exhaustive.
- V12 section top-1 is 17/30; V12 guard remains.
- Atlas global top-1 .433; layer volume is the supported path.
- Semantic hybrid (MiniLM and model2vec) is below BM25; opt-in only.
- Artifact-level qrels labels do not exist; only a handoff and self-retrieval
  diagnostic.
- No production-client benchmark; local hardware only.
- No process pool for MCP; thread cap only. A local benchmark shows 4
  processes at 9.3 s and 8 at 8.6 s for 150 queries, so process isolation is
  the preferred next step.

## Verdict

Not complete. Search defaults and latency are production-oriented, but artifact
labels, margin opt-in consistency and external validation remain open.
