# MCP end-to-end smoke — 2026-10-30

Status: local stdio smoke; not a production-client test, CI or human review.

## Protocol

- Server accepts protocol **2025-11-25**.
- Legacy 2024-11-05 returns -32602, as intended.
- 11 tools listed.

## Calls

| Request | Result |
|---|---|
| default `nested text` | BM25, best-section-per-document |
| `section_rerank=true`, margin .05 | BM25 (gate not crossed) |
| `volume=v12`, V12 replay | BM25, V12 fallback |
| `section_rerank=true`, margin 1.0 | section-rerank |

The .05 default does not force rerank; it only permits it when the top1/top2
margin is below .05. The forced run proves the opt-in path is wired.

## Layer and artifact checks

| Request | Result | Artifacts |
|---|---|---:|
| atlas `volume=v11` | BM25 | 0 |
| V12 `volume=v12` | BM25 | 0 |
| `include_artifacts=true`, stock-flow | BM25 | 5 |

A volume filter alone no longer returns all 25 artifacts. The volume-only
payload was a separate leak fixed in this change; artifact lookup remains
opt-in and query-aware.

## Verification

- real stdio process, initialize and tools/list;
- no stderr errors;
- 730 tests and premerge PASS;
- default unchanged: BM25.

## Limits

- One local process, one query per mode.
- No production client, concurrency soak or human review.
- AI qrels; no CI, owner acceptance or sufficient coverage.
