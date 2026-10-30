# Qrels v4.1 expansion — handoff

Status: handoff only. No v4.1 labels exist.

Baseline: qrels v4, 150 queries, frozen. Do not modify v4.

## Goal

Expand every v4 query from 4–5 candidates to **10–15 candidates** while
preserving all existing labels. This reduces the v4 pool bias without changing
book, atlas, indexes or production defaults.

## Files

Inputs (read-only):

- `evaluation/corpus-qrels.v4.json`
- `evaluation/section-qrels.v4.json`
- `generated/sections-fts-v5.sqlite` (section identity only)

Outputs:

- `evaluation/corpus-qrels.v4.1.json`
- `evaluation/section-qrels.v4.1.json`
- `evaluation/qrels-v4-1/REPORT.md`
- `evaluation/qrels-v4-1/validation.txt`

## Requirements

- Keep the same 150 IDs, questions, splits and snapshot.
- Keep every existing candidate and grade exactly unchanged.
- Add 5–10 new candidates per query; final count 10–15.
- At least 2 new grade-0 candidates per query.
- Add at least one new page/section candidate outside the original pool, not
  only accepted pages.
- Page and section files must cover the same query IDs.
- Page and section consistency: accepted/direct agree with grades; at least one
  direct grade 2 per query.
- Section keys from the read-only sections table.

## Candidate sources

Use structural neighbors, not current search results:

- same chapter and adjacent chapters in the same volume;
- adjacent atlas cards in the same family/chapter;
- linked V12 pages for the same model/scenario/run;
- chapter landing pages and overview sections.

Do not use current BM25/margin/best rankings to choose candidates. This keeps the
expansion independent of the systems being evaluated.

## Validator

```sh
python3 scripts/validate_qrels_v41.py \
  --page evaluation/corpus-qrels.v4.1.json \
  --section evaluation/section-qrels.v4.1.json \
  --baseline-page evaluation/corpus-qrels.v4.json \
  --baseline-section evaluation/section-qrels.v4.json
```

The validator checks counts, labels, baseline preservation, 10–15 candidates,
page/section consistency and snapshot.

## Limits

AI-adjudicated only. Not human review, CI, owner acceptance or sufficient
coverage. v4.1 remains pool-relative, but less biased than v4.
