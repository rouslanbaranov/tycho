# Section rerank split uncertainty — 2026-10-29

Status: diagnostic on AI section qrels v3. Not human review, independent review,
CI or owner acceptance.

## Result

| Split | n | BM25 top-1 | rerank top-1 | diff | 95% CI | p |
|---|---:|---:|---:|---:|---|---:|
| v2 | 155 | .8129 | .9097 | +.0968 | [.0387, .1548] | .0026 |
| phase3 | 19 | .7368 | .8421 | +.1053 | [-.1053, .3158] | .6250 |
| V12 | 14 | .7857 | .7857 | .0000 | [-.2857, .2857] | 1.0 |
| all | 188 | .8032 | .8936 | +.0904 | [.0319, .1489] | .0033 |

## Interpretation

The aggregate effect is driven by v2. Phase3 has a positive point estimate but
only 19 queries and is not significant. V12 shows no top-1 change; its
candidates were already well ranked.

This means section rerank is not established uniformly across query families.
Keep it optional; do not enable by default. A phase3/V12-specific section review
is still needed before any default decision.

## Limits

- AI-adjudicated labels and a candidate pool built from both modes.
- Phase3/V12 samples are very small.
- No human review, CI, owner acceptance or sufficient coverage.
