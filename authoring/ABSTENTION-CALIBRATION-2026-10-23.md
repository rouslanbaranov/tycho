# Qrels v2 and calibrated abstention — 2026-10-23

Status: author-labelled diagnostic. Not an independent relevance judgment, not a
sufficiency claim and not a benchmark. Human review and CI are not claimed.

## Qrels v2

`evaluation/corpus-qrels.v2.json` contains 220 items:

- 155 answerable and 65 unanswerable;
- 110 dev and 110 held-out;
- 60 new card decision questions mapped to owner pages (54 with page-level
  acceptance after invalid section anchors were cleared);
- 40 new vendor/current-fact questions and 20 out-of-domain questions;
- the original 100 bootstrap items remain, unchanged in v1.

All accepted answers use existing route documents. Section labels are null when
the owner anchor is not an indexed H2 section, so the section metric does not
pretend that a nested H3 anchor is a section hit.

## Refusal policy

`scripts/answerability.py` applies three signals:

1. an explicit out-of-scope intent gate for vendor-specific, current-fact and
   exact-measurement questions;
2. `top_score < 7.5`;
3. `unknown_term_rate >= 0.6`.

Thresholds were selected on the dev split and checked on held-out. The scope
gate is a lexical intent rule, not a semantic answerability model.

## Results

Ranking without abstention (qrels v2, limit 10):

| Metric | Value |
|---|---:|
| nDCG@10 | 0.6091 |
| Page hit@5 | 0.8129 |
| Section hit@5 | 0.7806 |
| Chapter hit@5 | 0.8774 |

Abstention:

| Metric | All | Dev | Held-out |
|---|---:|---:|---:|
| Unanswerable abstained | 58/65 (89.2%) | 25/30 | 33/35 |
| Answerable retained | 147/155 (94.8%) | 75/80 | 72/75 |
| False answers | 7/65 (10.8%) | 5/30 | 2/35 |
| Abstention precision | 0.879 | 0.833 | 0.917 |

Reasons: 45 out-of-scope intent, 14 low lexical score, 7 unknown terms.

The seven false answers are mostly out-of-domain questions whose generic words
still produce a high BM25 score. The gate does not prove absence and does not
catch every in-domain unsupported claim without an explicit scope cue.

## Limits

- Labels are author-labelled; no independent adjudication exists.
- Scope cues were written for the observed out-of-scope intents; they may
  overfit this set.
- The rule is calibrated to one corpus snapshot and one retrieval configuration.
- Refusal is not answer correctness; a retained result can still be incomplete.
- `sufficient` remains 0; no human review, owner acceptance or CI is claimed.

## Reproduction

```sh
python3 scripts/validate_corpus_qrels.py
python3 scripts/evaluate_corpus_qrels.py --qrels evaluation/corpus-qrels.v2.json
python3 scripts/evaluate_abstention.py --qrels evaluation/corpus-qrels.v2.json
```
