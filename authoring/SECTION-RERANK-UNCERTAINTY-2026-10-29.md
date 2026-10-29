# Section rerank uncertainty — 2026-10-29

Status: diagnostic on agent-adjudicated phase2+phase3 section qrels. Not human
review, independent review, CI or owner acceptance.

## Result

| Metric | Value |
|---|---:|
| n | 73 |
| base top-1 | .1644 |
| section_rerank top-1 | .2192 |
| difference | +.0548 |
| 95% bootstrap CI | [-.0548, .1644] |
| rerank-only correct | 10 |
| base-only correct | 6 |
| McNemar exact p | .4545 |

## Interpretation

The point estimate is +5.5 points, but the interval includes zero and the exact
test is far from 0.05. On 73 queries the section rerank effect is **not
established**.

This is consistent with the earlier warning: the phase2/phase3 samples are
small, and the feature was selected after inspecting phase3. Keep section
rerank optional and experimental; do not change the default.

## Limits

- Agent-adjudicated labels; not human.
- 73 queries; no power for a 5-point effect.
- One feature set; no held-out independent section review.
- No CI, owner acceptance or sufficient coverage.
