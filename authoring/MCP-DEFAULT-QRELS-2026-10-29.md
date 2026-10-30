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

The direct production gate and the MCP default both measure **.920**. The earlier
.931 came from a diagnostic evaluator that approximated the margin instead of
calling the production gate. The evaluator is fixed; .920 is the authoritative
number and no open discrepancy remains.

## Limits

- AI labels; candidate pool from both modes.
- No human review, CI, owner acceptance or sufficient coverage.
- No production-client benchmark.
