# Codex prompt — qrels v4 next three batches

Work only in the isolated clone:

```sh
cd ~/Projects/tycho-index-and-search
```

Read `authoring/QRELS-V4-HANDOFF-2026-10-30.md` and
`evaluation/qrels-v4/BATCHES.md`.

Do not read v3/v2/phase qrels, the quarantined partial draft, current search
rankings, or author conclusions.

## This run

Produce exactly B04, B05, B06 — 45 book queries:

| Batch | IDs |
|---|---|
| B04 | V4-B046–V4-B060 |
| B05 | V4-B061–V4-B075 |
| B06 | V4-B076–V4-B090 |

Do not produce other batches and do not merge the final files.

## Coverage requirement

Each batch must span at least **5 different volumes** and **5 different
chapters**. Do not put more than 3 queries from the same chapter in a batch.
Use distinct examples and avoid duplicating B01–B03 questions.

For each query: 4–10 page candidates, 4–10 section candidates, grades 0/1/2,
at least one direct answer, exact `accepted`/`direct`, page/section consistency.
Use section keys from the read-only `generated/sections-fts-v5.sqlite` table.

## Outputs

```text
evaluation/qrels-v4/batches/B04.page.json
evaluation/qrels-v4/batches/B04.section.json
evaluation/qrels-v4/batches/B05.page.json
evaluation/qrels-v4/batches/B05.section.json
evaluation/qrels-v4/batches/B06.page.json
evaluation/qrels-v4/batches/B06.section.json
```

Append one entry per batch to `evaluation/qrels-v4/BATCH-REPORT.md`.

Validate each:

```sh
python3 scripts/validate_qrels_v4.py \
  --page evaluation/qrels-v4/batches/B04.page.json \
  --section evaluation/qrels-v4/batches/B04.section.json \
  --book 15 --atlas 0 --v12 0
```

Fix and rerun a batch before moving to the next. Do not merge.

State HEAD, snapshot, coverage by volume/chapter, candidate counts and limits.
AI-adjudicated only; not human review, CI, owner acceptance or sufficient
coverage.
