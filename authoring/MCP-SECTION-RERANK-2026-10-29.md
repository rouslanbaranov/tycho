# MCP section rerank — 2026-10-29

Status: opt-in MCP surface. Not default. AI-adjudicated quality evidence; not
human review, independent review, CI or owner acceptance.

## Change

- `tycho_search` accepts `section_rerank` boolean, default `false`.
- Default remains best-section-per-document BM25.
- Rejected with `retrieval_mode=best` and `all_sections=true`.
- MCP passes the flag to `section_search.search`.

## Evidence

On AI section qrels v3 (188 queries, 1,397 sections):

- BM25 section hit@1/3/5: .803/.941/.979.
- section_rerank: .894/.952/.973.
- Difference +.0904; 95% CI [.0319, .1489]; McNemar p=.0033.

The pool is built from both modes and labels are AI, so this is not a default
switch and not owner acceptance.

## Decision

- Keep section_rerank opt-in in MCP.
- Keep BM25 default.
- No change to best mode.
- Tests: MCP schema, opt-in scope, default scope.

## Limits

- AI labels; same session family.
- No human review, CI, owner acceptance or sufficient coverage.
- Top-5 is slightly lower with rerank.
- No concurrency/network benchmark for this flag.
