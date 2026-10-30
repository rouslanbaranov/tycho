# Release candidate dossier — 2026-10-30

Status: release-candidate evidence, not owner acceptance, CI, human review or
sufficient coverage.

## Candidate

- Repository: isolated `tycho-index-and-search` clone.
- HEAD: `40e21821`.
- Section index snapshot:
  `e7496a664281afd4a1fff483f68780107a9541e3771a44741322751322dfe8fa`.
- Qrels v4 page/section: 150 queries, same snapshot, AI-adjudicated.
- Canonical book/atlas/index untouched by search work.

## Defaults

| Surface | Value |
|---|---|
| BM25 weights | title 5, heading 2, body 0.5 |
| MCP `section_rerank` | false |
| MCP opt-in margin | 0.05 |
| Core API/CLI | explicit BM25 |
| Best mode | opt-in only |

## Quality

Global BM25 page/section hit@1/3/5:

- page: .593/.847/.953;
- section: .480/.700/.793.

Opt-in margin .05:

- page: .620/.833/.940;
- section: .513/.700/.800.

Best mode:

- page: .567/.833/.947;
- section: .453/.687/.787.

Layer-scoped:

- atlas v11: 1.000/1.000/1.000;
- V12: .767/.933/1.000 page; .567/.733/.800 section;
- all: .707/.887/.960 page; .593/.740/.800 section.

## Runtime

- warm BM25 p50 66.7 ms, p95 79.7 ms;
- margin .05 p50 60.2 ms;
- best p50 216.5 ms, p95 420.4 ms;
- in-process concurrency cap 2;
- 4-process benchmark 9.3 s for 150 queries;
- 730 tests; premerge and boundary PASS.

## Evidence

- [QRELS-V4-PRODUCTION-BODY05-2026-10-30.md](QRELS-V4-PRODUCTION-BODY05-2026-10-30.md)
- [MARGIN05-UNCERTAINTY-2026-10-30.md](MARGIN05-UNCERTAINTY-2026-10-30.md)
- [BEST-MODE-ABLATION-2026-10-30.md](BEST-MODE-ABLATION-2026-10-30.md)
- [ATLAS-V12-LAYER-SCOPE-2026-10-30.md](ATLAS-V12-LAYER-SCOPE-2026-10-30.md)
- [SEARCH-LATENCY-2026-10-30.md](SEARCH-LATENCY-2026-10-30.md)
- [SEARCH-CONCURRENCY-2026-10-30.md](SEARCH-CONCURRENCY-2026-10-30.md)
- [MCP-END-TO-END-SMOKE-2026-10-30.md](MCP-END-TO-END-SMOKE-2026-10-30.md)

## Open blockers

- Artifact qrels now exist (30 queries, 5 candidates, external Codex); it is
  small and scenario/run top-1 is weak.
- No production-client benchmark.
- No MCP process pool; only an in-process semaphore.
- No human review, independent review, CI, owner acceptance or sufficient
  coverage.
- V12 section top-1 remains 17/30; guard retained.
- Qrels v4 candidate pools are 4–10, not exhaustive.

## Operations

See [SEARCH-OPERATIONS-2026-10-30.md](SEARCH-OPERATIONS-2026-10-30.md).

## Verdict

Search default and runtime are release-candidate ready for further external
evaluation. Artifact qrels exist, but production-client/external validation and
sufficient coverage are still missing.
