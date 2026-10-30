# Title coverage boost — 2026-10-30

Status: negative cross-qrels result. No default change. AI qrels; pool-relative;
not human review, CI, owner acceptance or sufficient coverage.

## Results

| Dataset | Alpha | Page hit@1/3/5 | Section |
|---|---:|---|---|
| v4 | 0 | .593/.847/.953 | .480/.700/.793 |
| v4 | .10 | .600/.853/.960 | .487/.707/.800 |
| v4 | .25 | .600/.847/.953 | .487/.707/.800 |
| v3 | 0 | **.920/.984/.989** | **.846/.952/.968** |
| v3 | .10 | .878/.979/.989 | .761/.947/.968 |
| v3 | .25 | .878/.973/.989 | .761/.941/.968 |

Page metrics are post-hoc; page order changes under the boost.

## Interpretation

- v4 gains ~0.7 points at alpha .10; v3 loses 4.2 page top-1 and 8.5 section
  top-1.
- The gain is not transferable; it overfits the v4 title distribution.
- Reject; keep BM25 title weight 5 without a post-hoc boost.

## Limits

- Simple title token coverage; AI qrels.
- No human review, CI, owner acceptance or sufficient coverage.
