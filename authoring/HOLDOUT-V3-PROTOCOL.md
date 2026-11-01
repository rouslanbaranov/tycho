# Fresh holdout protocol — v3

Status: protocol only. The v2 holdout is consumed and must not be reused.

## Requirements

1. Create 50 new questions not present in corpus-v2 or corpus-v3.
2. Derive each question from a bounded evidence unit, not from an answer.
3. Curate 3-5 core claims and 1-3 optional claims on the 50 dev questions only.
4. Obtain a human or independent editorial review of at least 20% of claims.
5. Freeze corpus-v3-dev and the prompt before running the new holdout.
6. Run one fresh agent per question with the checklist prompt.
7. Run two independent semantic judge passes.
8. Adjudicate every disagreement with a third pass.
9. Report support, core coverage, agreement, citations and tokens.
10. Do not tune claims or prompt on the new holdout and then reuse it.

## Gate

A new holdout may be reported only when its questions are new, its claims are
frozen, and the human/editorial review record exists. Until then, no quality
comparison with previous runs is valid.
