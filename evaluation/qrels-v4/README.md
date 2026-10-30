# Qrels v4 — AI-adjudicated

Status: **complete**, AI-adjudicated. B01–B03 were reworked for broad coverage
(12 volumes, 15 chapter topics).

- Page: `evaluation/corpus-qrels.v4.json`
- Section: `evaluation/section-qrels.v4.json`
- Report: [REPORT.md](REPORT.md)
- Validation: [validation.txt](validation.txt)

150 queries: 90 book, 30 atlas, 30 V12. Validator PASS.

## Coverage caveat

B01–B03 now span 12 volumes and 15 chapter topics; 12 questions use a case
page as a direct answer. B04–B06 are also broad. Atlas and V12 coverage is
documented in [REPORT.md](REPORT.md).

## Handoff history

- [CODEX-PROMPT.md](CODEX-PROMPT.md) — per-batch prompt
- [CODEX-ONE-RUN-PROMPT.md](CODEX-ONE-RUN-PROMPT.md) — all-batches attempt
- [BATCHES.md](BATCHES.md) — batch plan
- [QRELS-V4-HANDOFF-2026-10-30.md](../../authoring/QRELS-V4-HANDOFF-2026-10-30.md)

The failed one-query draft is under `partial/`; do not use it.

## Limits

AI-adjudicated only; not human review, independent review, CI, owner acceptance
or sufficient coverage. PASS is schema/consistency validation, not judgment
quality.
