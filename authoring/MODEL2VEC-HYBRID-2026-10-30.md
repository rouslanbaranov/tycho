# Model2vec hybrid — 2026-10-30

Status: negative opt-in result on AI qrels v4. BM25 remains default. Pool-
relative; not human review, CI, owner acceptance or sufficient coverage.

## Setup

Built model2vec `minishlab/potion-base-8M` H2 index: 2,577 sections, snapshot
`e7496a66...`. Tested page RRF weights .05/.1/.2; V12 stays BM25.

## Page/section hit@1/3/5, all

| Mode | Page | Section |
|---|---|---|
| BM25 | **.593/.847/.953** | **.480/.700/.793** |
| model2vec .05 | .567/.847/.953 | .453/.700/.793 |
| model2vec .1 | .560/.820/.953 | .447/.673/.800 |
| model2vec .2 | .547/.807/.933 | .433/.660/.780 |

Atlas page:

| Mode | Atlas |
|---|---|
| BM25 | **.433/.833/.967** |
| .05 | .267/.767/.967 |
| .1 | .233/.633/.967 |
| .2 | .233/.567/.867 |

Book page at .05 is .600/.856/.933, but the atlas collapse outweighs it.

## Decision

- Model2vec hybrid does not improve the global default.
- Best/hybrid remains opt-in.
- No default change.
- Atlas layer BM25 is already 1.000; semantic cannot improve it.

## Limits

- AI labels; pools 4–10; atlas global scope in this table.
- No human review, CI, owner acceptance or sufficient coverage.
- No production-client benchmark.
