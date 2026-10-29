# V12 section-rerank guard — 2026-10-29

Status: production guard, not default change. AI-adjudicated evidence; not human
review, independent review, CI or owner acceptance.

## Change

- `section_search.search(..., section_rerank=True, volume="v12")` is rejected.
- MCP `tycho_search` rejects the same combination.
- Explicit `volume=v12` requests cannot silently enter the section reranker.
- Default BM25 behavior is unchanged.

## Reason

Page-level qrels v3 showed:

- v2 page top-1: .865 -> .929;
- phase3: .895 -> .789;
- V12: 1.000 -> .857;
- aggregate gain was v2-only.

The guard prevents the known explicit V12 regression. It does not guard queries
that return V12 pages without a volume filter; that requires a separate
query-level gate.

## Limits

- Phase3 has no equivalent explicit volume guard.
- AI labels and a pool built from both modes.
- No human review, CI, owner acceptance or sufficient coverage.
