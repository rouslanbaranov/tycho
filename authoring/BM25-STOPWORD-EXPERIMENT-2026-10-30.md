# BM25 stopword query experiment — 2026-10-30

Status: negative query-preprocessing result. No default change. AI qrels;
pool-relative; not human review, CI, owner acceptance or sufficient coverage.

## Results

| Dataset | Mode | Page hit@1/3/5 | Section |
|---|---|---|---|
| v4 | baseline | **.593/.847/.953** | **.480/.700/.793** |
| v4 | stopwords | .560/.880/.933 | .433/.707/.773 |
| v3 | baseline | .920/.984/.989 | **.846/.952/.968** |
| v3 | stopwords | .926/.968/.989 | .824/.915/.947 |

## Interpretation

- v4 top-1 and section quality fall; top-3 rises but top-5 falls.
- v3 page top-1 rises 0.6 points, but section loses 2.2/3.7/2.1.
- Removing stopwords is not a safe default.
- Keep raw query normalization and BM25 5/2/.5.

## Limits

- Fixed stopword list; AI labels.
- No human review, CI, owner acceptance or sufficient coverage.
