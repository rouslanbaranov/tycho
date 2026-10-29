# Guarded section rerank — 2026-10-29

Status: diagnostic guarded evaluation of section_rerank. Not human review,
independent review, CI or owner acceptance. This supersedes pre-guard section
numbers where they differ.

## Guard

- 20 of 188 qrels-v3 queries were guarded and fell back to BM25.
- Guard applies when the query names v12 or the selected top page is v12.
- Explicit volume=v12 is rejected before search.

## Section metrics (guarded)

| Split | n | guarded | BM25 hit@1/3/5 | section_rerank hit@1/3/5 |
|---|---:|---:|---|---|
| v2 | 155 | 4 | .813/.948/.987 | **.897/.948/.974** |
| phase3 | 19 | 2 | .737/.895/.895 | **.842/.895/.895** |
| V12 | 14 | 14 | .786/.929/1.000 | .786/.929/1.000 |
| all | 188 | 20 | .803/.941/.979 | **.883/.941/.968** |

Guarded all top-1: +8.0 points; top-3 unchanged; top-5 -1.1.

## Page metrics (guarded)

| Split | n | BM25 hit@1/3/5 | guarded rerank hit@1/3/5 |
|---|---:|---|---|
| v2 | 155 | .865/.948/.974 | **.916/.961/.974** |
| phase3 | 19 | .895/.947/.947 | **.842/.947/.947** |
| V12 | 14 | 1.000/1.000/1.000 | **1.000/1.000/1.000** |
| all | 188 | .878/.952/.973 | **.915/.963/.973** |

V12 fallback restores its page top-1. Phase3 still loses 5.3 points at top-1
because the guard does not cover phase3.

## Uncertainty (guarded section top-1)

| Split | diff | 95% CI | p |
|---|---:|---|---:|
| all | +.0798 | [.0319, .1330] | .0041 |
| v2 | +.0839 | [.0258, .1419] | .0072 |
| phase3 | +.1053 | [-.1053, .3158] | .6250 |
| V12 | .0000 | [0, 0] | 1.0 |

The all/v2 effect remains significant after the V12 fallback. Phase3 is not.

## Decision

- Keep section_rerank optional.
- Keep BM25 default.
- V12 guard is effective for explicit/query/top-page V12 cases.
- Phase3 still needs a guard or dedicated review before any default decision.

## Limits

- AI labels; candidate pool built from both modes.
- Phase3/V12 samples are small.
- No human review, CI, owner acceptance or sufficient coverage.
