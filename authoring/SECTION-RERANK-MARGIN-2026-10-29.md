# Margin-gated section rerank — 2026-10-29

Status: diagnostic, not integrated. AI-adjudicated labels; not human review,
independent review, CI or owner acceptance.

## Rule

Apply global section_rerank only when the BM25 top-1/top-2 score margin is below
0.15; otherwise keep BM25 order. V12 guard still applies.

## Result

| Qrels | Level | Base hit@1/3/5 | Rerank hit@1/3/5 | Margin-gated hit@1/3/5 |
|---|---|---|---|---|
| corpus v3 | page | .878/.952/.973 | .915/.963/.973 | **.931/.963/.973** |
| section v3 | section | .803/.941/.979 | .883/.941/.968 | **.894/.952/.968** |
| phase2 | section | .130/.315/.352 | .185/.370/.426 | .185/.370/.407 |
| phase3 | section | .263/.368/.526 | .263/.526/.684 | .263/.421/.632 |

On qrels v3:

- page v2: .865 -> .929;
- page phase3: .895 unchanged;
- page V12: 1.000 unchanged;
- section all: +9.1 points top-1, +1.1 top-3, -1.1 top-5.

## Interpretation

The margin gate removes the phase3/V12 page regression while retaining most of
the v2 page gain. It does not improve held-out phase2/phase3 section top-1,
though it improves their top-3/top-5 versus BM25.

The 0.15 threshold was selected on qrels v3; this is a tuning risk. Do not make
it default without a held-out independent review.

## Decision

- Keep BM25 default.
- Keep section_rerank optional.
- Margin-gated mode is a candidate, not integrated.

## Limits

- AI labels; same session family.
- Threshold tuned on v3.
- No human review, CI, owner acceptance or sufficient coverage.
