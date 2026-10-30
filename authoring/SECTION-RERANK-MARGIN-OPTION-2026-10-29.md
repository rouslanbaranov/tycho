# Margin-gated section rerank option — 2026-10-29

Status: historical. The core option remains opt-in, but MCP now defaults to
BM25; the preferred opt-in margin is `.05`. See
[MCP-DEFAULT-REVERT-2026-10-30.md](MCP-DEFAULT-REVERT-2026-10-30.md).

## Change

- `section_search.search(..., section_rerank_margin=None)`.
- `None` keeps existing global section_rerank behavior.
- A number in 0..1 applies global rerank only when the BM25 top-1/top-2 score
  margin is below it; otherwise BM25 stays.
- CLI: `--section-rerank-margin`.
- MCP: optional `section_rerank_margin` number/null.

## Evidence

At margin 0.15:

| Qrels | Level | Base hit@1/3/5 | Margin-gated |
|---|---|---|---|
| corpus v3 | page | .878/.952/.973 | **.920/.963/.973** |
| section v3 | section | .803/.941/.979 | **.888/.952/.968** |
| phase2 | page | .296/.611/.667 | .296/.630/.667 |
| phase3 | page | .421/.632/.737 | **.474/.632/.737** |

On v3 page, v2 improves and phase3/V12 do not regress. Held-out page is mixed:
phase3 +5.3, phase2 -1.8.

## Decision

- Keep BM25 default.
- Keep margin gate optional; do not enable automatically.
- The 0.15 threshold is tuned on v3; held-out is mixed.
- No human/CI/owner acceptance/sufficiency claim.

## Limits

- AI labels and candidate pool built from both modes.
- Threshold tuning.
- No concurrency/network benchmark for the gated path.
