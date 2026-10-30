# Codex prompt — qrels v4.1 expansion

Work only in the isolated clone:

```sh
cd ~/Projects/tycho-index-and-search
```

Read `authoring/QRELS-V4.1-EXPANSION-HANDOFF-2026-10-30.md` and the frozen v4
qrels.

Do not read current search rankings, v3 labels or author conclusions.

## Task

Create v4.1 page/section qrels for all 150 v4 queries.

For each query:

- keep every existing candidate and grade exactly;
- add 5–10 new candidates, ending with 10–15;
- add at least 2 new grade-0 candidates;
- add at least one candidate outside the original pool;
- use structural neighbors: same/adjacent chapter, adjacent atlas card, linked
  V12 page; never current search results;
- label new pages/sections 0/1/2;
- keep page/section consistency and at least one direct grade 2.

Do not edit book, atlas, edition, generated indexes or production config.
Do not modify v4.

Outputs:

- `evaluation/corpus-qrels.v4.1.json`
- `evaluation/section-qrels.v4.1.json`
- `evaluation/qrels-v4-1/REPORT.md`
- `evaluation/qrels-v4-1/validation.txt`

Validate:

```sh
python3 scripts/validate_qrels_v41.py \
  --page evaluation/corpus-qrels.v4.1.json \
  --section evaluation/section-qrels.v4.1.json \
  --baseline-page evaluation/corpus-qrels.v4.json \
  --baseline-section evaluation/section-qrels.v4.json
```

State AI-adjudicated only; not human review, CI, owner acceptance or sufficient
coverage.
