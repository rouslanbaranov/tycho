# Qrels v4 — handoff state

Status: **handoff only**. No final qrels v4 files exist.

Codex must run in `~/Projects/tycho-index-and-search`
(`/Users/rbaranov/Projects/tycho-index-and-search`), not in any other checkout.

Follow [CODEX-PROMPT.md](CODEX-PROMPT.md) and
[QRELS-V4-HANDOFF-2026-10-30.md](../../authoring/QRELS-V4-HANDOFF-2026-10-30.md).

For one run that completes all ten batches, use
[CODEX-ONE-RUN-PROMPT.md](CODEX-ONE-RUN-PROMPT.md).

## Batches

Ten batches of 15 queries; see [BATCHES.md](BATCHES.md). Each Codex run creates
only one page/section batch:

```text
evaluation/qrels-v4/batches/<BATCH>.page.json
evaluation/qrels-v4/batches/<BATCH>.section.json
```

Validate one batch:

```sh
python3 scripts/validate_qrels_v4.py \
  --page evaluation/qrels-v4/batches/B01.page.json \
  --section evaluation/qrels-v4/batches/B01.section.json \
  --book 15 --atlas 0 --v12 0
```

After all ten:

```sh
python3 scripts/merge_qrels_v4_batches.py \
  --batch-dir evaluation/qrels-v4/batches
```

Target: 150 queries (90 book, 30 atlas, 30 V12). These are AI-adjudicated, not
human review, CI, owner acceptance or sufficient coverage.

## Partial draft

The failed one-query Codex draft is quarantined under `partial/`. Do not merge
or evaluate it as qrels v4.
