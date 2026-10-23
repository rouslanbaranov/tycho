# Corpus-level relevance judgments and lexical evaluation

> Issue [#298](https://github.com/rouslanbaranov/tycho/issues/298), M4. Capabilities K18 and
> K28. **Status 2026-10-22:** bootstrap author-labelled set with 100 items, a 50/50
> development/held-out split, 156 accepted answers and 10 section-level labels. Independent
> adjudication, broader section-level labels and a refusal metric remain. This is not
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
| [corpus-qrels.v1.json](../evaluation/corpus-qrels.v1.json) | The bootstrap questions, accepted answers and section labels. |
| [validate_corpus_qrels.py](../scripts/validate_corpus_qrels.py) | Schema, snapshot, ID/path and uniqueness checks. |
| [evaluate_corpus_qrels.py](../scripts/evaluate_corpus_qrels.py) | Pure metric functions and a CLI over the section search layer. |
| [test_tycho_qrels.py](../tests/test_tycho_qrels.py) | Offline validation and metric tests. |

The dataset is pinned to route snapshot
`f742ba6af5d628fc59bb5f192fca181aeb3a4f2504e16261065b72f9fa931764` (423 documents).
Earlier pins were replaced after source remediations, label/owner fixes, Phase A fixes,
Cache-Aside fixes, Phase B integrity, blocker/high and medium card/owner fixes; no accepted
answer pointed at a V11 page.

## How labels were constructed

Questions were written from domain questions, not copied from page titles or summaries.
Candidate pages were found with the metadata route index, then accepted or rejected by
reading the page summary and section structure. Search output was **candidate discovery**,
not evidence for a label. Every accepted answer carries a grade and a short rationale:

- grade 2: directly explains the requested mechanism or decision;
- grade 1: supporting context needed for a complete answer.

The bootstrap mixes 10 section-level labels with page-level labels (`section_id` is null).
The validator checks structure; section IDs were verified against the published section index
at authoring time.

Unanswerable items have no accepted page. The evaluator reports how often search returned
no results for them; it does **not** score whether an agent correctly refused the premise.
That requires a separate answer-level evaluation.

## Composition and split

| Category | Items |
|---|---:|
| fact | 23 |
| failure | 21 |
| synthesis | 15 |
| trade-off | 15 |
| change impact | 13 |
| contradiction | 8 |
| unanswerable | 5 |
| **Total** | **100** |

Split: 50 development and 50 held-out. The held-out items are not used for tuning, query
expansion, threshold selection or ranker comparison. No tuning has been performed yet.

Known gaps: most labels are still page-level, five unanswerable items have no refusal
metric, and there is no independent adjudication or answer-quality label.

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

## Merged-main baseline — 2026-10-22

Run on merged main at `b534eb6` with search snapshot
`448b35fef9e7bcea60d59c775c6390e74f1271ffa4f89363dd834f716c86bbaf` and qrels snapshot
`6684db8339ef674b6270b697872deb4f466c629882f06508028d20917e232bb9`:

| Scope | hit@1 | hit@3 | hit@5 | MRR |
|---|---:|---:|---:|---:|
| page | 0.379 | 0.642 | 0.758 | 0.539 |
| chapter | 0.579 | 0.790 | 0.884 | 0.707 |
| section | 0.337 | 0.600 | 0.716 | 0.495 |

nDCG@10 was 0.558 over 95 answerable items. Dev page hit@5 was 0.740 and chapter hit@5
0.880; held-out was 0.778 and 0.889 (reported once, not tuned). Dev page hit@5 by category:
failure 0.800, fact 0.900, change impact 0.857, synthesis 0.667, contradiction 0.600,
trade-off 0.556. All five unanswerable items returned results, so refusal is not measured.

Re-pin 2026-10-23: source/label/owner fixes, Phase A fixes, Phase B integrity, blocker/high
content fixes and medium card/owner coverage moved the route snapshot to
`f742ba6af5d628fc59bb5f192fca181aeb3a4f2504e16261065b72f9fa931764` and the section
snapshot to `5631b3e52670…`; nDCG@10 is 0.5626.

## Provisional acceptance thresholds

Fixed before ranker tuning on the 100-item set. The current baseline does not meet all of
them; they are targets, not claims.

| Metric | Threshold |
|---|---:|
| page hit@5 | >= 0.80 |
| chapter hit@3 | >= 0.80 |
| chapter hit@5 | >= 0.90 |
| nDCG@10 | >= 0.55 |
| dev metric regression after a ranker change | <= 0.03 absolute |
| held-out use | once per candidate; never for tuning |

Current page hit@5 is 0.758 and chapter hit@3 is 0.790, both below their thresholds;
chapter hit@5 is 0.884, below 0.90; nDCG@10 is 0.558, above 0.55. No refusal threshold is set
because no refusal metric exists.

## Operation

~~~sh
python3 scripts/validate_corpus_qrels.py
python3 scripts/evaluate_corpus_qrels.py --split dev
python3 scripts/evaluate_corpus_qrels.py --split heldout
~~~

The evaluator imports `section_search` lazily and runs against the published section index.
It returns `not-available` when the search layer or index is absent. The measured baseline
above belongs to the named merged commit and snapshots; rerun it after a book or index
change instead of carrying the numbers forward.

## Staleness and review limits

The validator fails when the route snapshot or document count changes. A book edit therefore
requires deliberate label revalidation: fix affected accepted answers, rerun the validator,
and record the new snapshot. It must not be repaired by silently editing the pinned hash.

No independent review exists. The dataset must stay labelled `bootstrap-author-labelled`
until a separate reviewer adjudicates the questions and accepted answers. Passing schema and
metric tests proves only structure and arithmetic, not relevance.

## Next gates

1. Obtain independent adjudication for a sample; keep the bootstrap label until then.
2. Expand section-level labels beyond the current 10 items.
3. Add a refusal metric for the five unanswerable items.
4. Tune only on the dev split; compare lexical, hybrid and future rankers on held-out.
5. Revalidate labels after any book change and record the new snapshot.
