# Atlas rank prior — 2026-10-30

Status: negative result. AI qrels v4/v3; pool-relative; not human review, CI,
owner acceptance or sufficient coverage.

## Experiment

Apply a stable multiplier to the BM25 rank of atlas (v11) pages, preserving the
base order otherwise. Unlike a score re-sort, this leaves the baseline exactly
unchanged at 1.0.

Boosts 1.0, 1.1, 1.25, 1.5; page/section hit@1/3/5.

| Boost | v4 page | v4 section | v3 page | v3 section |
|---|---|---|---|---|
| 1.0 | .593/.847/.953 | .480/.700/.793 | .920/.984/.989 | .846/.952/.968 |
| 1.1 | .593/.847/.953 | .480/.700/.793 | .920/.984/.989 | .846/.952/.968 |
| 1.25 | .593/.847/.953 | .480/.700/.793 | .920/.984/.989 | .846/.952/.968 |
| 1.5 | .593/.867/.960 | .480/.720/.800 | .920/.984/.989 | .846/.952/.968 |

## Interpretation

A rank-2 atlas page needs a boost greater than 2.0 to overtake a rank-1 book
page; 1.0–1.5 therefore do nothing. At >2.0 the prior would start displacing
correct book pages and is not supported by the cross-qrels evidence.

An earlier score-sort variant was rejected: it changed the 1.0 baseline
(v3 page .872 instead of .920), so its apparent atlas gains were a sorting
artifact.

## Decision

No global atlas prior. Use `volume=v11` for atlas-layer queries, which already
gives 1.000/1.000/1.000. Keep BM25 default.

## Limits

- AI labels; candidate pools 4–10.
- No human review, CI, owner acceptance or sufficient coverage.
- No production-client benchmark.
