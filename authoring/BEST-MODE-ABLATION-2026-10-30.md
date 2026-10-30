# Best-mode hybrid/rerank ablation — 2026-10-30

Status: negative opt-in result on AI qrels v4. BM25 remains default. Pool-
relative; not human review, CI, owner acceptance or sufficient coverage.

## Ablation

Page/section hit@1/3/5, all 150:

| Mode | Page | Section |
|---|---|---|
| BM25 | **.593/.847/.953** | **.480/.700/.793** |
| hybrid RRF .1 | .553/.833/.947 | .447/.693/.787 |
| BM25 + top1 rerank | .593/.853/.953 | .480/.707/.800 |
| hybrid + top1 rerank | .573/.840/.940 | .460/.693/.787 |

Splits:

- hybrid page: book .578/.856/.944; atlas .267/.700/.900; V12 unchanged;
- BM25+rerank page: book .611/.844/.933; atlas .367/.833/.967;
- rerank section: all .480/.707/.800, +0.7 top-3/5 only.

## Interpretation

- Semantic RRF with MiniLM hurts page top-1 and atlas badly.
- top1 logistic rerank is neutral: top-1 unchanged, top-3/5 +0.6/+0.7.
- Combining both is worse than either alone.
- V12 is unaffected because both paths skip it.
- Best mode remains optional; no default change.

## Decision

Keep BM25 default and best mode opt-in. Do not ship hybrid RRF as a default.
The current embedding/RRF combination does not satisfy the hybrid hypothesis on
v4.

## Limits

- AI labels; candidate pools 4–10; qrels atlas uses global scope for this table.
- No human review, CI, owner acceptance or sufficient coverage.
- No production-client benchmark.
