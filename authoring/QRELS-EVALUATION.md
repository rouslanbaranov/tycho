# Corpus-level relevance judgments and lexical evaluation

> Issue [#298](https://github.com/rouslanbaranov/tycho/issues/298), M4. Capabilities K18 and
> K28. **Status 2026-10-22:** bootstrap author-labelled set with 24 items, a 12/12
> development/held-out split and 48 accepted answers. Target is 50–100 items. This is not
> independent ground truth and does not establish search quality.

## Why this set exists

The earlier [pilot questions](../evaluation/pilot-questions.json) name one canonical page
per question and were written for three pilot pages. The [M9 case queries](../tests/fixtures/m9-case-queries.json)
cover 29 case pages. Both are in-sample, single-target and author-labelled. They are useful
diagnostics but cannot support a search-quality claim.

This set introduces three missing properties:

- accepted-answer sets rather than one required page;
- an explicit development/held-out split;
- labels pinned to one route-index snapshot.

## Artifacts

| Artifact | Purpose |
|---|---|
| [corpus-qrels.v1.schema.json](../schemas/corpus-qrels.v1.schema.json) | Strict Draft 2020-12 structure for items, splits and accepted answers. |
| [corpus-qrels.v1.json](../evaluation/corpus-qrels.v1.json) | The bootstrap questions and accepted answers. |
| [validate_corpus_qrels.py](../scripts/validate_corpus_qrels.py) | Schema, snapshot, ID/path and uniqueness checks. |
| [evaluate_corpus_qrels.py](../scripts/evaluate_corpus_qrels.py) | Pure metric functions and a CLI over the section search layer. |
| [test_tycho_qrels.py](../tests/test_tycho_qrels.py) | Offline validation and metric tests. |

The dataset is pinned to route snapshot
`6684db8339ef674b6270b697872deb4f466c629882f06508028d20917e232bb9` (423 documents).

## How labels were constructed

Questions were written from domain questions, not copied from page titles or summaries.
Candidate pages were found with the metadata route index, then accepted or rejected by
reading the page summary and section structure. Search output was **candidate discovery**,
not evidence for a label. Every accepted answer carries a grade and a short rationale:

- grade 2: directly explains the requested mechanism or decision;
- grade 1: supporting context needed for a complete answer.

The bootstrap uses page-level labels (`section_id` is null). The schema and evaluator
already support a specific section ID when a later batch needs it.

Unanswerable items have no accepted page. The evaluator reports how often search returned
no results for them; it does **not** score whether an agent correctly refused the premise.
That requires a separate answer-level evaluation.

## Composition and split

| Category | Items |
|---|---:|
| fact | 7 |
| failure | 6 |
| synthesis | 4 |
| trade-off | 4 |
| change impact | 1 |
| contradiction | 1 |
| unanswerable | 1 |
| **Total** | **24** |

Split: 12 development and 12 held-out. The held-out items are not used for tuning, query
expansion, threshold selection or ranker comparison. No tuning has been performed yet.

Known gaps: only one change-impact and one contradiction item, no answer-quality labels,
and no independent adjudication. Expansion to 50 items should add those categories and at
least one section-level label per volume.

## Metrics

The evaluator reports page-level, chapter-level and section-level hit@1/3/5, mean reciprocal
rank and nDCG@10 for each split, category and the full set.

- **page:** any accepted page appears in the result list;
- **chapter:** any result shares the accepted page's `parent_id`;
- **section:** an accepted section ID matches exactly; a null section ID accepts any section
  of the accepted page;
- **nDCG@10:** grades 2 and 1 are gains; paths not listed are zero.

A no-result answer is not treated as a miss for answerable items; it is reported separately.
The evaluator uses limit 10 by default and refuses a run when the search snapshot changes
between questions.

## Local diagnostic baseline — 2026-10-22

The set was run once on the #50 search branch against index snapshot
`448b35fef9e7bcea60d59c775c6390e74f1271ffa4f89363dd834f716c86bbaf`. The #298 branch
alone cannot reproduce this until #50 merges.

| Scope | hit@1 | hit@3 | hit@5 | MRR |
|---|---:|---:|---:|---:|
| page | 0.304 | 0.652 | 0.739 | 0.482 |
| chapter | 0.435 | 0.783 | 0.870 | 0.625 |
| section | 0.304 | 0.652 | 0.739 | 0.482 |

nDCG@10 was 0.473 over 23 answerable items. The single unanswerable item returned
results, so its no-result rate was 0/1 and refusal quality is not measured. This is a
diagnostic on a small bootstrap set, not a threshold, acceptance result or confidence
claim. Split-level output exists in the evaluator but was not used to tune the ranker.

## Operation

~~~sh
python3 scripts/validate_corpus_qrels.py
python3 scripts/evaluate_corpus_qrels.py --split dev
python3 scripts/evaluate_corpus_qrels.py --split heldout
~~~

The evaluator imports `section_search` lazily. On a branch without the merged search layer
it returns `not-available`; on the #50 branch it runs against the published index. This
document records the bootstrap structure, not a measured baseline.

## Staleness and review limits

The validator fails when the route snapshot or document count changes. A book edit therefore
requires deliberate label revalidation: fix affected accepted answers, rerun the validator,
and record the new snapshot. It must not be repaired by silently editing the pinned hash.

No independent review exists. The dataset must stay labelled `bootstrap-author-labelled`
until a separate reviewer adjudicates the questions and accepted answers. Passing schema and
metric tests proves only structure and arithmetic, not relevance.

## Next gates

1. Expand to 50 items, then 100, with more change-impact and contradiction cases.
2. Add section-level labels and a second reviewer for a sample.
3. Record the first real baseline on the #50 snapshot and set thresholds before tuning.
4. Compare lexical, hybrid and future rankers on the same held-out split.
