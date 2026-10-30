# Codex prompt — qrels v4 V02

Work only in the isolated clone:

```sh
cd ~/Projects/tycho-index-and-search
```

Read `authoring/QRELS-V4-HANDOFF-2026-10-30.md` and
`evaluation/qrels-v4/BATCHES.md`.

Do not read v3/v2/phase qrels, the quarantined partial draft, current search
rankings, or author conclusions.

## This run

Produce exactly V02:

- split `v12`;
- IDs `V4-V016–V4-V030`;
- 15 queries.

Do not produce other batches and do not merge final files.

## Coverage

- at least 5 different V12 chapters;
- no more than 3 queries from one chapter;
- avoid V01 questions;
- 4–10 page candidates and 4–10 section candidates per query;
- grades 0/1/2, at least one direct answer, exact accepted/direct;
- page/section consistency;
- use section keys from the read-only `generated/sections-fts-v5.sqlite`
  table.

## Outputs

```text
evaluation/qrels-v4/batches/V02.page.json
evaluation/qrels-v4/batches/V02.section.json
```

Append V02 to `evaluation/qrels-v4/BATCH-REPORT.md`.

Validate:

```sh
python3 scripts/validate_qrels_v4.py \
  --page evaluation/qrels-v4/batches/V02.page.json \
  --section evaluation/qrels-v4/batches/V02.section.json \
  --book 0 --atlas 0 --v12 15
```

Fix and rerun until PASS. Do not merge.

Record HEAD, snapshot, chapter coverage, candidate counts and limits.
AI-adjudicated only; not human review, CI, owner acceptance or sufficient
coverage.
