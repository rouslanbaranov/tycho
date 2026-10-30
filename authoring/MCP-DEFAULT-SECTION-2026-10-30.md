# MCP default section qrels — 2026-10-30

Status: actual MCP handler on AI section-qrels v3. Not human review, independent
review, CI or sufficient coverage.

## Result

| Split | n | explicit BM25 hit@1/3/5 | MCP default hit@1/3/5 |
|---|---:|---|---|
| v2 | 155 | .813/.948/.987 | .897/.961/.974 |
| phase3 | 19 | .737/.895/.895 | .895/.895/.895 |
| V12 | 14 | .786/.929/1.000 | .786/.929/1.000 |
| all | 188 | .803/.941/.979 | **.888/.952/.968** |

The actual MCP phase3 section top-1 is .895, higher than the direct-gate
diagnostic .842. V12 is unchanged. Top-5 is slightly lower (.968 vs .979).

## Limits

- AI labels and a pool built from both modes.
- Threshold tuned on v3.
- No human review, CI, owner acceptance or sufficient coverage.
- No production-client benchmark.
