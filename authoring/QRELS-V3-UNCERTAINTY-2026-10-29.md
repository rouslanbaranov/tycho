# Qrels v3 uncertainty — 2026-10-29

Status: diagnostic on the AI-adjudicated page-level qrels v3. Not human review,
independent review, CI or owner acceptance.

## Method

- 188 paired queries.
- Compare BM25 top-1 with best-mode top-1 against accepted pages (grade >= 1).
- 5,000 paired bootstrap resamples, seed 20261029.
- Exact two-sided McNemar test on discordant pairs.

## Result

| Metric | Value |
|---|---:|
| BM25 top-1 | .8777 |
| best top-1 | .9202 |
| difference | +.0426 |
| 95% bootstrap CI | [.0000, .0851] |
| best-only correct | 12 |
| BM25-only correct | 4 |
| McNemar exact p | .0768 |

## Interpretation

Best mode improves the point estimate by 4.26 points, but the paired interval
includes zero and the exact test does not cross the 0.05 threshold. On this
sample, the improvement is **suggestive, not established**.

This does not justify making best mode the default. It also does not prove
BM25 is better; it only means the current 188-query AI-adjudicated sample does
not resolve the difference at conventional significance.

## Limits

- AI-adjudicated labels; not human or independent review.
- Page-level only; section precision not measured.
- Pool is BM25/best top-10, not exhaustive.
- One bootstrap seed; interval is not a full Bayesian uncertainty model.
- No production, CI, owner acceptance or sufficient coverage claim.
