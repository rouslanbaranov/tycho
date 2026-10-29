# V12 query-level section-rerank guard — 2026-10-29

Status: production guard, not default change. AI-adjudicated evidence; not human
review, independent review, CI or owner acceptance.

## Change

- `section_search.search(..., section_rerank=True)` now rejects:
  - a query containing v12;
  - a top selected page with volume v12.
- Explicit `volume="v12"` was already rejected.
- Default BM25 is unchanged.

## Reason

Page-level qrels v3 showed V12 top-1 falling from 1.000 to .857 with section
rerank. The guard prevents both explicit V12 filters and V12-named/top-page
queries from entering the risky path.

## Limits

- A general query can still retrieve a V12 page at a lower rank; only the top
  selected page is checked.
- Phase3 has no equivalent query-level guard.
- AI labels and a pool built from both modes.
- No human review, CI, owner acceptance or sufficient coverage.
