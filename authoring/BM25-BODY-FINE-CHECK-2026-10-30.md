# Fine BM25 body-weight check — 2026-10-30

Status: no default change. AI/author qrels; pool-relative; not human review, CI,
owner acceptance or sufficient coverage.

## Results

| Dataset | Body | Page | Section |
|---|---:|---|---|
| v4 | .4 | .560/.833/.920 | .460/.687/.773 |
| v4 | .5 | .593/.847/.953 | .480/.700/.793 |
| v4 | .6 | **.607/.867/.967** | **.493/.727/.820** |
| v3 | .5 | .920/.984/.989 | **.846/.952/.968** |
| v3 | .6 | **.931/.989/.989** | .830/.941/.957 |
| v2 | .5 | **.419/.665/.787** | — |
| v2 | .6 | .413/.658/.768 | — |

## Interpretation

- .6 improves v4 and v3 page but loses v3 section and v2 page.
- .5 is the best cross-qrels compromise.
- Keep 5/2/0.5; no default change.

## Limits

- Author/AI labels; simple grid.
- No human review, CI, owner acceptance or sufficient coverage.
