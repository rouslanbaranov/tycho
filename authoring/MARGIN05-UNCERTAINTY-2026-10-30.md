# Margin .05 uncertainty — qrels v4

Status: paired uncertainty for the final opt-in. AI qrels; no human review, CI,
owner acceptance or sufficient coverage.

## Page

| Split | n | BM25 | margin .05 | diff | 95% CI | p |
|---|---:|---:|---:|---:|---|---:|
| book | 90 | .5889 | .6333 | +.0444 | [.0000, .1000] | .219 |
| atlas | 30 | .4333 | .4333 | .0000 | [-.1000, .1000] | 1.0 |
| V12 | 30 | .7667 | .7667 | .0000 | [0, 0] | 1.0 |
| all | 150 | .5933 | .6200 | +.0267 | [-.0067, .0667] | .289 |

Top-5:

| Split | BM25 | margin | diff | 95% CI | p |
|---|---:|---:|---:|---|---:|
| book | .9333 | .9222 | -.0111 | [-.0333, 0] | 1.0 |
| atlas | .9667 | .9333 | -.0333 | [-.1000, 0] | 1.0 |
| V12 | 1.0000 | 1.0000 | 0 | [0, 0] | 1.0 |
| all | .9533 | .9400 | -.0133 | [-.0333, 0] | .5 |

## Interpretation

- .05 is not a significant improvement over BM25.
- It trades a small top-1 gain for a small top-5 loss.
- Atlas top-1 is unchanged; top-5 falls.
- Keep BM25 default; .05 remains opt-in.
