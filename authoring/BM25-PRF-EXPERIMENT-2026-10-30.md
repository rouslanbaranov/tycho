# BM25 pseudo-relevance feedback — 2026-10-30

Status: negative query-expansion result. No default change. AI qrels; pool-
relative; not human review, CI, owner acceptance or sufficient coverage.

## Results

| Dataset | Mode | Page hit@1/3/5 | Section |
|---|---|---|---|
| v4 | baseline | **.593/.847/.953** | **.480/.700/.793** |
| v4 | PRF 3 | .487/.867/.920 | .373/.673/.753 |
| v4 | PRF 5 | .453/.847/.920 | .353/.647/.740 |
| v4 | PRF 8 | .473/.827/.913 | .367/.633/.727 |
| v3 | baseline | **.920/.984/.989** | **.846/.952/.968** |
| v3 | PRF 3 | .883/.957/.989 | .734/.883/.931 |
| v3 | PRF 5 | .856/.947/.984 | .691/.856/.915 |
| v3 | PRF 8 | .867/.952/.973 | .718/.840/.904 |

## Interpretation

- PRF harms top-1 and section quality on both datasets.
- v4 top-3 rises slightly at 3 terms, but top-1/top-5 fall.
- Expansion drifts toward generic top-5 vocabulary.
- Keep raw BM25 queries; no PRF.

## Limits

- Fixed top-5 PRF and simple term counts; no tuning against qrels.
- AI labels; no human review, CI, owner acceptance or sufficient coverage.
