# Margin eval correction — 2026-10-30

Status: correction of the margin-gated evaluation. AI labels; not human review,
independent review, CI or sufficient coverage.

## Root cause

The earlier `.931` page and `.894` section results came from a diagnostic
evaluator that approximated the margin gate manually. The production gate is
inside `section_search.search` and uses the selected-candidate scores. The
evaluator now calls `section_rerank_margin` directly.

## Authoritative metrics

| Qrels | Level | BM25 hit@1/3/5 | Production gate hit@1/3/5 |
|---|---|---|---|
| corpus v3 | page | .878/.952/.973 | **.920/.963/.973** |
| section v3 | section | .803/.941/.979 | **.888/.952/.968** |
| phase2 | page | .296/.611/.667 | .296/.630/.667 |
| phase3 | page | .421/.632/.737 | **.474/.632/.737** |

Direct production API and MCP default now both give **.920** page top-1.

## Superseded

- .931 page and .894 section are obsolete.
- The open .920/.931 discrepancy is closed.
- Artifacts `section-rerank-margin-page.json` and
  `section-rerank-margin-section.json` are regenerated.

## Limits

- AI labels, threshold tuned on v3.
- No human/CI/owner acceptance/sufficiency claim.
