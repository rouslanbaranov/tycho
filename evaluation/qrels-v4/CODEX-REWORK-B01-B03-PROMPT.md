# Codex prompt — B01–B03 coverage rework

Work only in the isolated clone:

```sh
cd ~/Projects/tycho-index-and-search
```

Read `authoring/QRELS-V4-HANDOFF-2026-10-30.md` and
`evaluation/qrels-v4/BATCHES.md`.

Do not read v3/v2/phase qrels, current search rankings, author conclusions, or
the old narrow labels. The old B01–B03 files are backed up under
`evaluation/qrels-v4/batches/provisional-narrow-b01-b03/`; do not reuse them.

## Task

Replace the narrow B01–B03 book batches with broad-coverage batches. Produce
exactly these 45 queries:

| Batch | IDs |
|---|---|
| B01 | V4-B001–V4-B015 |
| B02 | V4-B016–V4-B030 |
| B03 | V4-B031–V4-B045 |

Overwrite only the root batch files:

```text
evaluation/qrels-v4/batches/B01.page.json
evaluation/qrels-v4/batches/B01.section.json
evaluation/qrels-v4/batches/B02.page.json
evaluation/qrels-v4/batches/B02.section.json
evaluation/qrels-v4/batches/B03.page.json
evaluation/qrels-v4/batches/B03.section.json
```

Do not create B04–B06, A/V batches or final qrels; do not merge.

## Coverage requirements

Each batch must have:

- 15 queries;
- at least **5 distinct book volumes**;
- at least **5 distinct chapters**;
- no more than **3 queries from one chapter**.

Across B01–B03 together:

- at least **12 distinct volumes**;
- at least **15 distinct chapters**;
- no chapter may contribute more than 3 queries.

Do not concentrate a batch in caching, streams, vectors or any single topic.
Cover architecture, data, reliability, delivery, observability and operations.
At least 12 queries across the 45 must be grounded in concrete case/example
pages; do not make all questions synthetic.

## Labels

For every query:

- 4–10 page candidates;
- 4–10 section candidates;
- grades 0/1/2;
- at least one direct grade 2;
- exact accepted/direct sets;
- page/section consistency;
- section keys from the read-only `generated/sections-fts-v5.sqlite` table.

Read the page/section body. Do not infer labels from titles or from current
search rankings.

Avoid duplicating questions from B04–B06. You may inspect their question text
only to avoid duplicates, not their labels.

## Validate

```sh
python3 scripts/validate_qrels_v4.py \
  --page evaluation/qrels-v4/batches/B01.page.json \
  --section evaluation/qrels-v4/batches/B01.section.json \
  --book 15 --atlas 0 --v12 0
```

Repeat for B02 and B03. If a batch fails, fix and rerun before moving on.

Append a B01–B03 rework entry to `evaluation/qrels-v4/BATCH-REPORT.md` with
volume/chapter counts per batch and overall distinct counts.

## Finish

Do not merge. Record HEAD, snapshot, coverage counts, candidate counts and
limitations. State: AI-adjudicated only; not human review, CI, owner acceptance
or sufficient coverage. If coverage cannot be met, report the concrete shortfall
rather than relabeling the narrow set.
