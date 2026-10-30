# Qrels v4 — handoff state

Status: **handoff only**. No qrels v4 files exist yet.

Codex must follow [CODEX-PROMPT.md](CODEX-PROMPT.md) and
[QRELS-V4-HANDOFF-2026-10-30.md](../../authoring/QRELS-V4-HANDOFF-2026-10-30.md).

Expected outputs:

- `evaluation/corpus-qrels.v4.json`
- `evaluation/section-qrels.v4.json`
- `evaluation/qrels-v4/REPORT.md`
- `evaluation/qrels-v4/validation.txt`

Validate:

```sh
python3 scripts/validate_qrels_v4.py \
  --page evaluation/corpus-qrels.v4.json \
  --section evaluation/section-qrels.v4.json
```

Target: 150 independent queries (90 book, 30 atlas, 30 V12), 4–10 page and
section candidates each, grades 0/1/2, at least one direct answer per query.

Do not reuse v3 labels or current search rankings. These are AI-adjudicated
qrels, not human review, CI, owner acceptance or sufficient coverage.
