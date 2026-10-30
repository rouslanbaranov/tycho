# Atlas/V12 layer scope — qrels v4

Status: diagnostic on AI qrels v4. Pool-relative; not human review, CI, owner
acceptance or sufficient coverage.

## Finding

Global atlas top-1 is .433 because canonical book pages with the same topic
outrank the atlas cards. The qrels atlas split intends the atlas layer.

With `volume=v11`, atlas retrieval is perfect:

| Scope | Atlas page | Atlas section |
|---|---|---|
| global | .433/.833/.967 | .433/.833/.967 |
| layer v11 | **1.000/1.000/1.000** | **1.000/1.000/1.000** |

Atlas first-accepted rank globally: 1 (13), 2 (10), 3 (2), 4 (3), 5 (1),
7 (1). Every top-1 miss is a canonical book page in v04/v08/v09/v10.

## Layer-scoped BM25

| Split | n | Page | Section |
|---|---:|---|---|
| book | 90 | .589/.833/.933 | .467/.656/.733 |
| atlas v11 | 30 | **1.000/1.000/1.000** | **1.000/1.000/1.000** |
| V12 | 30 | .767/.933/1.000 | .567/.733/.800 |
| all | 150 | **.707/.887/.960** | **.593/.740/.800** |

Global all remains .593/.847/.953 page and .480/.700/.793 section.

## Decision

- Report global and layer-scoped metrics separately; do not mix them.
- For atlas-layer queries use `volume=v11`; for V12 use `volume=v12`.
- Global default remains BM25; no automatic layer classifier.
- The atlas weakness is a routing/cross-layer issue, not an atlas-card ranking
  failure.

## Limits

- AI labels; candidate pools 4–10; qrels atlas split built from atlas cards.
- Layer scope is an evaluation/usage choice, not a default.
- No human review, CI, owner acceptance or sufficient coverage.
