# Codex prompt — qrels v4.1 batch

Work only in the isolated clone:

```sh
cd ~/Projects/tycho-index-and-search
```

Read:

- `authoring/QRELS-V4.1-EXPANSION-HANDOFF-2026-10-30.md`
- `evaluation/qrels-v4-1/BATCHES.md`
- frozen v4 page/section qrels.

Do not read current search rankings or v3 labels.

## This run: exactly one batch

Operator supplies:

```text
BATCH=<B01|...|B15>
```

Each batch is 10 queries. For every query:

- keep every existing v4 candidate and grade exactly;
- add 5–10 candidates, ending with 10–15;
- add at least 2 new grade-0 candidates;
- add at least one candidate outside the original pool;
- use structural neighbors (same/adjacent chapter, adjacent atlas card, linked V12 page);
- never use current search rankings;
- label new pages/sections 0/1/2;
- keep page/section consistency and at least one direct grade 2.

Outputs:

- `evaluation/qrels-v4-1/batches/<BATCH>.page.json`
- `evaluation/qrels-v4-1/batches/<BATCH>.section.json`
- append to `evaluation/qrels-v4-1/BATCH-REPORT.md`

Do not merge; do not edit v4/book/atlas/generated indexes.

Validate:

```sh
python3 scripts/validate_qrels_v41_batch.py \
  --page evaluation/qrels-v4-1/batches/<BATCH>.page.json \
  --section evaluation/qrels-v4-1/batches/<BATCH>.section.json \
  --batch <BATCH>
```

State AI-adjudicated only; not human review, CI, owner acceptance or sufficient
coverage.
