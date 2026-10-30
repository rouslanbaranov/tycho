# MCP default reverted to BM25 — 2026-10-30

Status: production default change based on qrels v4. AI-adjudicated evidence; not
human review, CI, owner acceptance or sufficient coverage.

## Decision

- MCP `tycho_search` default is `section_rerank=false` (BM25).
- Margin-gated section rerank remains opt-in:
  `section_rerank=true, section_rerank_margin=0.15`.
- Best mode remains optional.
- V12/all_sections/best fallbacks stay.

## Evidence

Qrels v4 page:

| Split | n | BM25 | margin |
|---|---:|---|---|
| book | 90 | .500/.789/.867 | .544/.778/.856 |
| atlas | 30 | .433/.800/.933 | .333/.733/.800 |
| V12 | 30 | .667/.867/.933 | .667/.867/.933 |
| all | 150 | .520/.807/.893 | .527/.787/.860 |

Paired uncertainty:

- top-1 diff +.0067, CI [-.0533, .0667], p=1.0;
- top-5 diff -.0333, CI [-.0667, -.0067], p=.0625;
- atlas top-5 diff -.1333, CI [-.2667, -.0333], p=.125.

The v3 margin default is not supported by v4. BM25 is restored as default.

## Tests

- 728 tests pass; MCP default/opt-in/V12/all_sections tests updated.
- Book/atlas/index unchanged.

## Limits

- AI labels and pool-relative 4–10 candidates.
- No human review, CI, owner acceptance or sufficient coverage.
- No production-client benchmark.
