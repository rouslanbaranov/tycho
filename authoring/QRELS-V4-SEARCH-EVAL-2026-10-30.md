# Qrels v4 search evaluation — 2026-10-30

Status: first evaluation on AI qrels v4. Pool-relative; not human review, CI,
owner acceptance or sufficient coverage.

## Setup

150 queries: 90 book, 30 atlas, 30 V12. Page and section qrels. Candidate pools
4–10 per query. Metrics are hit@1/3/5 inside the v4 pool.

Modes:

- BM25;
- production margin gate (section_rerank=true, margin=.15);
- best mode.

## Page results

| Split | n | BM25 | margin | best |
|---|---:|---|---|---|
| book | 90 | .500/.789/.867 | **.544**/.778/.856 | .533/.800/.867 |
| atlas | 30 | **.433/.800/.933** | .333/.733/.800 | .233/.733/.867 |
| V12 | 30 | .667/.867/.933 | .667/.867/.933 | .667/.867/.933 |
| all | 150 | .520/.807/.893 | .527/.787/.860 | .500/.800/.880 |

## Section results

| Split | n | BM25 | margin | best |
|---|---:|---|---|---|
| book | 90 | .389/.611/.667 | **.433/.656/.722** | .378/.611/.678 |
| atlas | 30 | **.433/.800/.933** | .333/.733/.800 | .233/.733/.867 |
| V12 | 30 | .500/.600/.667 | .500/.600/.667 | .500/.600/.667 |
| all | 150 | .420/.647/.720 | **.427/.660/.727** | .373/.633/.713 |

## Interpretation

The v4 evaluation does **not** support the current MCP margin default:

- page top-1: +0.7 points for margin, but top-3 -2.0 and top-5 -3.3;
- atlas page: top-1 -10.0, top-3 -6.7, top-5 -13.3;
- book page: top-1 +4.4, top-3 -1.1, top-5 -1.1;
- section aggregate: margin is slightly better at all three depths;
- best mode is worse than BM25 on page and section aggregate.

The atlas regression is material on 30 queries. The current production default
should be revisited. This is evidence for BM25 as the safer default, with margin
gate retained as an opt-in.

## Limits

- AI-adjudicated labels; pool-relative 4–10 candidates.
- v4 query distribution differs from v3; not directly comparable.
- No human review, CI, owner acceptance or sufficient coverage.
- No production-client benchmark.
