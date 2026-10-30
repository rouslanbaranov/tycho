# Tokenizer comparison — 2026-10-30

Status: negative alternative-index result. Canonical porter index remains. AI
qrels; pool-relative; not human review, CI, owner acceptance or sufficient
coverage.

## Method

Built a temporary `unicode61` FTS5 index alongside the canonical
`porter unicode61` index, same snapshot and books. Evaluated page/section qrels
at body 0.5; canonical index untouched.

## Results

| Dataset | Index | Page hit@1/3/5 | Section |
|---|---|---|---|
| v4 | porter | .593/.847/.953 | **.480/.700/.793** |
| v4 | unicode61 | .600/.880/.927 | .460/.733/.760 |
| v3 | porter | **.920/.984/.989** | **.846/.952/.968** |
| v3 | unicode61 | .894/.963/.973 | .755/.894/.920 |

## Interpretation

- unicode61 gains v4 top-1/top-3 but loses v4 top-5 and section top-1.
- v3 regresses on page and section.
- Porter stemming is the better cross-qrels choice; keep canonical index.
- No tokenizer change.

## Limits

- One temporary index; AI labels.
- No human review, CI, owner acceptance or sufficient coverage.
