# M9 E16-08 — Independent Review Status Needs Reviewer Metadata

**Date:** 2026-10-19 · **Scope:** proposed Tycho M9 portable case-record schema and fallback validator; this is **not** proof of any real case's independent acceptance.

## Failure mode

The proposed M9 schema previously allowed `status: independent_reviewed` while `review.reviewer = null` and `review.reviewed_on = null`. Both states satisfy the original optional review fields but contradict the meaning of the review status. A publishing/indexing agent relying on the status alone could mistakenly elevate an authored draft as independently verified.

## Structural remedy

- Draft 2020-12 `if/then` conditional: when `status` equals `independent_reviewed`, require a non-whitespace reviewer name of at least three characters and a calendar-formatted `reviewed_on` date. Existing ordinary draft records with null reviewer/date remain valid.
- Align the no-dependency Python `validate_record()` semantic guard with those necessary conditions.
- Extend `scripts/validate_m9_cases.py --self-test` from **13** to **16** negative mutations: null reviewer, null review date, and whitespace-only reviewer. The full JSON Schema validator must reject **15** malformed schema cases, while the separately enforced reversed date-window is a *schema-valid but semantically invalid* sixteenth mutation.

## Executed isolated evidence (not a full repository test)

Python 3.13.5 and `jsonschema` 4.26.0 ran with two previously transferred case-record samples plus an in-memory copy of the proposed conditional:

- Unchanged `draft` sample: **accepted**.
- All three fabricated `independent_reviewed` cases with empty reviewer/date: **rejected**.
- Across the **16** negative mutants, **15** were rejected by the actual Draft2020-12 + FormatChecker engine, while the reversed date interval correctly passed the base schema and requires the separate semantic check.

**Limitations:** This was an executed **isolated JSON validation** using copied JSON examples and in-memory schema changes, not authenticated full-checkout execution of the updated Python code or a byte-verified GitHub file read. The mere presence of non-empty reviewer metadata does **not** establish that a reviewer is real, independent, qualified, or has actually reviewed the sources and benchmarks. A real reviewer approval, source-by-source verdict and audit record are mandatory before M9 #121 closes.

No restricted-origin/private sources, employer data, new workflow, Scheduled Tasks or core M1–M8 files were used.
