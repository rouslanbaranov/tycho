# Qrels v4 margin uncertainty — 2026-10-30

Status: paired uncertainty on AI qrels v4. Pool-relative; not human review, CI,
owner acceptance or sufficient coverage.

## Page top-1

| Split | n | BM25 | margin | diff | 95% CI | p |
|---|---:|---:|---:|---:|---|---:|
| book | 90 | .5000 | .5444 | +.0444 | [-.0556, .1333] | .481 |
| atlas | 30 | .4333 | .3333 | -.1000 | [-.2333, .0333] | .375 |
| V12 | 30 | .6667 | .6667 | .0000 | [0, 0] | 1.0 |
| all | 150 | .5200 | .5267 | +.0067 | [-.0533, .0667] | 1.0 |

## Page top-5

| Split | n | BM25 | margin | diff | 95% CI | p |
|---|---:|---:|---:|---:|---|---:|
| book | 90 | .8667 | .8556 | -.0111 | [-.0333, 0] | 1.0 |
| atlas | 30 | .9333 | .8000 | -.1333 | [-.2667, -.0333] | .125 |
| V12 | 30 | .9333 | .9333 | .0000 | [0, 0] | 1.0 |
| all | 150 | .8933 | .8600 | -.0333 | [-.0667, -.0067] | .0625 |

## Interpretation

- Aggregate top-1 gain is +0.7 points and not distinguishable from zero.
- Aggregate top-5 loses 3.3 points; the bootstrap interval excludes zero, but
  McNemar p is .0625.
- Atlas top-5 loses 13.3 points; the bootstrap interval excludes zero, but n=30
  and McNemar p is .125.
- Book top-1 rises 4.4 points, but not significantly; top-5 slightly falls.
- V12 is unchanged; best mode is worse than BM25 on aggregate page/section.

The v4 evidence does **not** support the current MCP margin default. Recommend
returning BM25 to default and keeping margin gate opt-in.

## Limits

- AI labels and 4–10 candidate pools; pool-relative metrics.
- No human review, CI, owner acceptance or sufficient coverage.
- No production-client benchmark.
