# Qrels v4.1 expansion

Status: **batched handoff**. No final v4.1 labels exist.

- Handoff: `../../authoring/QRELS-V4.1-EXPANSION-HANDOFF-2026-10-30.md`
- Batch plan: [BATCHES.md](BATCHES.md)
- Codex prompt: [CODEX-PROMPT.md](CODEX-PROMPT.md)
- Batch validator: `scripts/validate_qrels_v41_batch.py`
- Merge: `scripts/merge_qrels_v41_batches.py`

15 batches ×10 queries. The failed 6/150 draft is under `partial/` and must not
be used. Target: same 150 v4 queries, 10–15 candidates each, existing v4 labels
preserved. Structural hard negatives; no current search rankings.

This is a separate qrels version, not a replacement for v4 and not a book/atlas
change. AI-adjudicated only; no human review, CI, owner acceptance or sufficient
coverage.
