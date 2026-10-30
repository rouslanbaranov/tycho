# MCP default qrels evaluation — 2026-10-29

Status: actual MCP handler evaluation on AI qrels v3. Not human review,
independent review, CI or sufficient coverage.

## Result

| Split | n | explicit pure BM25 hit@1/3/5 | MCP default hit@1/3/5 |
|---|---:|---|---|
| v2 | 155 | .865/.948/.974 | .916/.961/.974 |
| phase3 | 19 | .895/.947/.947 | .895/.947/.947 |
| V12 | 14 | 1.000/1.000/1.000 | 1.000/1.000/1.000 |
| all | 188 | .878/.952/.973 | **.920/.963/.973** |

Phase3 and V12 page top-1 are preserved. v2 improves by 5.1 points.

## Difference from direct API

The direct margin-gated API measured .931 on corpus v3. The MCP default measures
.920 because the MCP layer disables section rerank early for v12-named queries;
some v2 queries contain v12 wording. This is a real production-path difference,
not a metric typo.

## Limits

- AI labels; candidate pool from both modes.
- No human review, CI, owner acceptance or sufficient coverage.
- No production-client benchmark.
