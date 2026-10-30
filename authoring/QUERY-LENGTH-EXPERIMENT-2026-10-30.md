# Query length limit — 2026-10-30

Status: negative. No default change. AI qrels; pool-relative; not human review,
CI, owner acceptance or sufficient coverage.

## Results

| Dataset | Limit | Page hit@1/3/5 | Section |
|---|---:|---|---|
| v4 | none | **.593/.847/.953** | **.480/.700/.793** |
| v4 | 12 | .527/.793/.887 | .413/.600/.700 |
| v4 | 16 | .580/.847/.940 | .467/.700/.780 |
| v4 | 24 | .593/.847/.953 | .480/.700/.793 |
| v3 | none | **.920/.984/.989** | **.846/.952/.968** |
| v3 | 12 | .872/.979/.984 | .660/.872/.910 |
| v3 | 16 | .910/.979/.989 | .798/.926/.952 |
| v3 | 24 | .910/.984/.989 | .846/.952/.968 |

## Interpretation

- Truncation drops meaningful tail terms; section quality falls sharply.
- 24 terms is effectively no-op for v4 and slightly hurts v3 top-1.
- Keep full queries.

## Limits

- Whitespace token truncation; AI labels.
- No human review, CI, owner acceptance or sufficient coverage.
