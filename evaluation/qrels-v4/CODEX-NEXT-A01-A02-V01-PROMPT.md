# Codex prompt — qrels v4 A01–A02 + V01

Work only in the isolated clone:

```sh
cd ~/Projects/tycho-index-and-search
```

Read `authoring/QRELS-V4-HANDOFF-2026-10-30.md` and
`evaluation/qrels-v4/BATCHES.md`.

Do not read v3/v2/phase qrels, the quarantined partial draft, current search
rankings, or author conclusions.

## This run

Produce exactly these three batches:

| Batch | Split | IDs | Count |
|---|---|---|---:|
| A01 | atlas | V4-A001–V4-A015 | 15 |
| A02 | atlas | V4-A016–V4-A030 | 15 |
| V01 | v12 | V4-V001–V4-V015 | 15 |

Do not produce V02 or merge final files.

## Coverage

- A01/A02: at least 10 distinct atlas cards/owning pages, spanning at least
  5 atlas chapters; no more than 2 queries from one card/chapter.
- V01: at least 5 V12 chapters; no more than 3 queries per chapter.
- Avoid questions already present in B01–B06.
- For each query: 4–10 page candidates, 4–10 section candidates, grades 0/1/2,
  at least one direct answer, exact accepted/direct, page/section consistency.
- Use section keys from the read-only generated/sections-fts-v5.sqlite table.

## Outputs

```text
evaluation/qrels-v4/batches/A01.page.json
evaluation/qrels-v4/batches/A01.section.json
evaluation/qrels-v4/batches/A02.page.json
evaluation/qrels-v4/batches/A02.section.json
evaluation/qrels-v4/batches/V01.page.json
evaluation/qrels-v4/batches/V01.section.json
```

Append one entry per batch to evaluation/qrels-v4/BATCH-REPORT.md.

Validate each:

```sh
# A01 / A02
python3 scripts/validate_qrels_v4.py \
  --page evaluation/qrels-v4/batches/A01.page.json \
  --section evaluation/qrels-v4/batches/A01.section.json \
  --book 0 --atlas 15 --v12 0

# V01
python3 scripts/validate_qrels_v4.py \
  --page evaluation/qrels-v4/batches/V01.page.json \
  --section evaluation/qrels-v4/batches/V01.section.json \
  --book 0 --atlas 0 --v12 15
```

Fix and rerun a batch before moving to the next. Do not merge.

Record HEAD, snapshot, coverage by card/chapter, candidate counts and limits.
AI-adjudicated only; not human review, CI, owner acceptance or sufficient
coverage.
