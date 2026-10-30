# BM25 title/heading grid at body 0.5 — 2026-10-30

Status: negative tuning result. AI qrels v4/v3; pool-relative; not human review,
CI, owner acceptance or sufficient coverage.

## Grid

Body fixed at 0.5. Page/section hit@1/3/5, all queries:

| Weights | v4 page | v4 section | v3 page | v3 section |
|---|---|---|---|---|
| 5/2 | .593/.847/.953 | .480/.700/.793 | .920/.984/.989 | .846/.952/.968 |
| 4/2 | .600/.847/.953 | .487/.700/.800 | .920/.984/.989 | .846/.952/.968 |
| 3/2 | **.607/.853/.953** | **.500/.707/.800** | .920/.989/.989 | .851/.936/.963 |
| 5/3 | .587/.840/.927 | .480/.693/.787 | .920/.979/.989 | .856/.947/.973 |
| 6/3 | .580/.833/.927 | .473/.687/.787 | .920/.979/.989 | .856/.947/.973 |
| 8/3 | .560/.833/.920 | .447/.687/.780 | .915/.973/.989 | .856/.952/.968 |
| 5/4 | .587/.833/.907 | .487/.693/.773 | .915/.979/.989 | .867/.941/.963 |

Atlas v4: 5/2 .433/.833/.967; 3/2 .467/.833/.967.

## Decision

Keep **5/2/0.5**. The 3/2 variant gains 1.4 page top-1 and 2.0 section top-1 on
v4, but loses 1.6 section top-3 and 0.5 section top-5 on v3, and the atlas gain
is one query. This is too small and inconsistent to justify another default
change.

The title/heading axis is saturated near 5/2; further tuning risks overfitting
the small v4 atlas split.

## Limits

- AI labels; v4 pools 4–10; v3 is not independent validation.
- No human review, CI, owner acceptance or sufficient coverage.
- No production-client benchmark.
