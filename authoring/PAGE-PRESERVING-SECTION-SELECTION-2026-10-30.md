# Page-preserving section selection — 2026-10-30

Status: negative result. No default change. AI qrels; pool-relative; not human
review, CI, owner acceptance or sufficient coverage.

## Method

Keep the BM25 page order exactly. Within each of the top five pages, rescore all
sections by query-term hits plus heading hits and select the best section.

## Section results

| Dataset | Baseline | Reselected |
|---|---|---|
| qrels v4 | **.480/.700/.793** | .433/.660/.767 |
| qrels v3 | **.846/.952/.968** | .814/.952/.963 |

Page metrics are unchanged by construction.

## Interpretation

- Reselection loses section top-1 on both datasets.
- v4 top-3/top-5 also fall; v3 top-3 is unchanged but top-1/top-5 fall.
- BM25's existing best-section selection is better than the simple term-hit
  selector.
- Keep the current section display; no page-preserving reselector.

## Limits

- Simple term-hit scoring; no learned selector.
- AI labels; no human review, CI, owner acceptance or sufficient coverage.
