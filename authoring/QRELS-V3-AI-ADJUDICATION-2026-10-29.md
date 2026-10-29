# Qrels v3 AI adjudication — 2026-10-29

Status: **AI-adjudicated**, not human review, independent review, CI or owner
acceptance. Not a production-quality claim.

## Artifact

- 188 answerable queries: 155 v2, 19 phase3, 14 V12.
- 2,038 page candidates from BM25 top-10 and best-mode top-10.
- Ten packets; every candidate graded 0/1/2 by a separate AI adjudication
  worker.
- Grades: 791 zero, 770 partial, 477 direct.
- Accepted (grade >= 1): 1,247 page judgments; direct: 477.
- Snapshot: e7496a664281afd4a1fff483f68780107a9541e3771a44741322751322dfe8fa
- File: [corpus-qrels.v3.json](../evaluation/corpus-qrels.v3.json)

## Evaluation

Page-level hit rates. Accepted means grade >= 1; direct means grade == 2.

| Split | n | BM25 hit@1/3/5 | best hit@1/3/5 | best direct hit@1/3/5 |
|---|---:|---|---|---|
| v2 | 155 | .865/.948/.974 | .910/.961/.981 | .697/.865/.916 |
| phase3 | 19 | .895/.947/.947 | .947/.947/.947 | .632/.737/.789 |
| V12 | 14 | 1.000/1.000/1.000 | 1.000/1.000/1.000 | .357/.714/.929 |
| all | 188 | .878/.952/.973 | **.920/.963/.979** | .665/.840/.904 |

Best mode improves page-level accepted top-1 by 4.2 points over BM25 on this
AI-adjudicated pool. The gain is not evidence of production quality because:

- labels are AI, not human or independent;
- the pool is BM25/best top-10, not exhaustive;
- accepted sets are broad (1,247 pages), so recall is easier than under the
  older sparse accepted sets;
- V12 accepted top-1 is 1.000 but direct top-1 is .357;
- no default change is justified.

## Decision

- Keep BM25 as default.
- Keep best mode optional.
- Treat v3 as a diagnostic, not as a replacement for human/owner adjudication.
- Do not train or recalibrate on these labels without a separate decision.
- Do not overwrite qrels v2, phase3 or V12.

## Limits

- AI adjudication from ten session subagents; same vendor.
- Page-level only; section precision is not measured.
- No human review, CI, owner acceptance or sufficient coverage.
- Candidate pool is not exhaustive beyond BM25/best top-10.
