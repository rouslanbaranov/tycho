# Codex prompt — qrels v4

You are the independent external AI evaluator for Tycho. Work read-only on the
book, atlas and V12 artifacts; you may write only the qrels v4 outputs listed
below.

## Mandatory working directory

Work only in the isolated clone:

```sh
cd ~/Projects/tycho-index-and-search
```

Absolute path: `/Users/rbaranov/Projects/tycho-index-and-search`.

Do **not** work in `/Users/rbaranov/Projects/tycho` or any other checkout. All
reads and writes below are relative to the isolated clone.

Read first: `authoring/QRELS-V4-HANDOFF-2026-10-30.md`.

Do **not** read v3/v2/phase qrels, v3 pools, reviewed packets, current search
results/rankings, or author conclusions. Create fresh questions and candidates
from the book pages, atlas cards and V12 artifacts.

Deliver:

- `evaluation/corpus-qrels.v4.json`
- `evaluation/section-qrels.v4.json`
- `evaluation/qrels-v4/REPORT.md`
- `evaluation/qrels-v4/validation.txt`

Target 150 queries: 90 book, 30 atlas, 30 V12. Each query needs 4–10 page
candidates and 4–10 section candidates, grades 0/1/2, at least one direct (2)
answer, and exact `accepted`/`direct` sets.

Use `section_key` from the read-only `generated/sections-fts-v5.sqlite`
`sections` table for section identity. Do not use FTS ranking tables for
candidate selection.

Run:

```sh
python3 scripts/validate_qrels_v4.py \
  --page evaluation/corpus-qrels.v4.json \
  --section evaluation/section-qrels.v4.json
```

Record HEAD and snapshot, query/candidate counts, method, limitations, and
whether any question was rejected. State clearly: AI-adjudicated, not human
review, not CI, not owner acceptance, not sufficient coverage.

Do not edit `book/**`, `edition/**`, `generated/**`, qrels v2/v3, source
catalog or production configuration. If a path or section cannot be resolved,
stop and report it instead of inventing a label.
