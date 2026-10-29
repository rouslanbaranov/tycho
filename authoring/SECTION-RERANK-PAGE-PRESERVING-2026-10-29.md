# Page-preserving section rerank — 2026-10-29

Status: negative diagnostic result. Not human review, independent review, CI or
owner acceptance.

## Question

Can section reranking avoid the phase3/V12 page regression by keeping the BM25
page order and only replacing the section within each page?

## Result

Section qrels v3, 188 queries:

| Mode | section hit@1/3/5 |
|---|---|
| BM25 | .803/.941/.979 |
| page-preserving rerank | .750/.936/.963 |
| global section rerank (guarded) | .883/.941/.968 |

Page-preserving keeps page order but **loses** section top-1 and top-5 relative
to BM25. It avoids the page reorder that hurt phase3/V12, but it does not
improve section retrieval enough to be useful.

## Decision

- Do not integrate page-preserving rerank.
- Keep global section_rerank optional and guarded for V12.
- Phase3 page regression remains an open reason not to change the default.

## Limits

- AI section labels; pool built from both modes.
- 188 queries; phase3/V12 small.
- No human/owner/CI/sufficiency claim.
