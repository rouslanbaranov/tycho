# MCP margin default — 2026-10-29

Status: historical; superseded on 2026-10-30. Qrels v4 showed top-5 and atlas
regressions, so MCP default returned to BM25. See
[MCP-DEFAULT-REVERT-2026-10-30.md](MCP-DEFAULT-REVERT-2026-10-30.md).

## Owner decisions

1. Enable `section_rerank_margin=0.15` in the production default.
2. No separate human/independent section/phase3 review.
3. No production-client benchmark before the default switch.

## Behavior

- `tycho_search` defaults:
  - `section_rerank: true`;
  - `section_rerank_margin: 0.15`.
- Explicit `section_rerank=false` returns pure BM25.
- Explicit `section_rerank_margin=null` keeps global section rerank.
- Best mode disables section rerank.
- V12 query/volume and `all_sections` fall back to BM25.
- Core `section_search.search` keeps explicit defaults so evaluation and tests
  remain stable.

## Evidence

At margin 0.15:

| Qrels | Level | Base hit@1/3/5 | Margin-gated |
|---|---|---|---|
| corpus v3 | page | .878/.952/.973 | **.920/.963/.973** |
| section v3 | section | .803/.941/.979 | **.888/.952/.968** |
| phase2 | page | .296/.611/.667 | .296/.630/.667 |
| phase3 | page | .421/.632/.737 | **.474/.632/.737** |

Held-out page effect is mixed; threshold was tuned on v3.

## Verification

- 727 tests pass.
- MCP tests cover default true, margin 0.0 gating, and V12 fallback.
- Parser rejects margin outside 0..1.
- Local premerge checks pass; milestone acceptance is separate.

## Limits

- AI labels, not human review.
- Threshold tuning and mixed held-out page result.
- No concurrency/network benchmark.
- Book/atlas/cards unchanged.
