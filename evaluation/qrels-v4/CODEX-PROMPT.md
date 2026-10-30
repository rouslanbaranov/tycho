# Codex prompt — qrels v4 batch

You are the independent external AI evaluator for Tycho. Work read-only on the
book, atlas and V12 artifacts; you may write only one qrels v4 batch.

## Mandatory working directory

Work only in the isolated clone:

```sh
cd ~/Projects/tycho-index-and-search
```

Absolute path: `/Users/rbaranov/Projects/tycho-index-and-search`.

Do **not** work in `/Users/rbaranov/Projects/tycho` or any other checkout.

Read first:

- `authoring/QRELS-V4-HANDOFF-2026-10-30.md`
- `evaluation/qrels-v4/BATCHES.md`

Do **not** read v3/v2/phase qrels, v3 pools, reviewed packets, the quarantined
partial draft, current search results/rankings, or author conclusions. Create
fresh questions and candidates from the book pages, atlas cards and V12.

## This run: exactly one batch

Use the batch id supplied by the operator:

```text
BATCH=<B01|B02|B03|B04|B05|B06|A01|A02|V01|V02>
```

Each batch contains exactly 15 queries at page and section levels. Use the ID
range and split from `BATCHES.md`. Do not create other batches.

Deliver only:

- `evaluation/qrels-v4/batches/<BATCH>.page.json`
- `evaluation/qrels-v4/batches/<BATCH>.section.json`
- append a short entry to `evaluation/qrels-v4/BATCH-REPORT.md`

Do not create final `corpus-qrels.v4.json` or `section-qrels.v4.json`.

## Labels

For each of the 15 queries:

- 4–10 page candidates;
- 4–10 section candidates;
- grades 0/1/2;
- at least one direct grade 2;
- exact `accepted`/`direct` sets;
- page/section consistency.

Use `section_key` from the read-only `generated/sections-fts-v5.sqlite`
`sections` table. Do not use FTS ranking tables for candidate selection.

## Validate

For book batches:

```sh
python3 scripts/validate_qrels_v4.py \
  --page evaluation/qrels-v4/batches/B01.page.json \
  --section evaluation/qrels-v4/batches/B01.section.json \
  --book 15 --atlas 0 --v12 0
```

Use `--book 0 --atlas 15 --v12 0` for A batches and
`--book 0 --atlas 0 --v12 15` for V batches.

Record HEAD, snapshot, counts, method and limitations. State: AI-adjudicated,
not human review, CI, owner acceptance or sufficient coverage.

Do not edit `book/**`, `edition/**`, `generated/**`, qrels v2/v3, source
catalog or production configuration. If a path or section cannot be resolved,
stop and report it instead of inventing a label.
