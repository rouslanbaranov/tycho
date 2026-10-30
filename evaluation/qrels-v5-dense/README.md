# Qrels v5-dense

Status: **complete**, 30 candidates/query, 30/30 batches.

- Base: qrels v4.1, all labels preserved.
- Pool: 10–11 existing + 19–20 new structural/random candidates.
- 4,500 page and 4,500 section judgments.
- 997 accepted page / 996 accepted section.
- Labeled by **30 empty-context DeepSeek subagents**; no Codex.
- No current search rankings used to build candidates.

Files:

- [candidates.json](candidates.json) — unlabeled dense pool.
- [batches/](batches/) — 30 candidate slices.
- [labels/](labels/) — 30 label batches.
- [EVAL.md](EVAL.md)
- [eval.json](eval.json)

This is still **pool-relative and not exhaustive**: 30 candidates from 498 pages and
3,075 sections. AI-adjudicated only; not human review, CI, owner acceptance or
sufficient coverage.
