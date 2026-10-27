# External AI review reports

This directory preserves verbatim reports from independent external AI reviewers.
Every completed review must be saved here; a review without a saved report is not a
completed review.

Reports are required only for in-scope changes: book content or structure and the pattern
atlas. A review of another artifact may still be recorded here.

## Naming

`YYYY-MM-DD-<scope-slug>-<reviewer-slug>.md`

Examples:

- `2026-10-26-full-unit-reading-chatgpt.md`
- `2026-10-26-pattern-atlas-claude-code.md`

The reviewer runs read-only and does not write this file. The author saves the reviewer
output verbatim. Do not edit the report; add corrections as a separate addendum.

## Index

| Date | Reviewer harness / vendor | Scope | Verdict | Report | SHA-256 |
|---|---|---|---|---|---|
| 2026-10-26 | Codex / OpenAI | #535 full-unit reading and 23 removed claims | reject | `2026-10-26-full-unit-reading-codex.md` | `4e9ed912281f84346dfa11caec0a05b50ef613de461443afb662481f37b0eb90` |
| 2026-10-26 | Codex / OpenAI | #535 remediation R-01–R-08 | reject | `2026-10-26-remediation-rereview-codex.md` | `430d30bbb689e5ad15127f7790eb2a0e0cc4b39fd663602ccde854cc7bfbb2f7` |
| 2026-10-26 | Codex / OpenAI | #535 round-3 focused re-review | pass | `2026-10-26-round3-rereview-codex.md` | `b4ecbb26a1eaf395df439d82a98a21c819ea3d4c428818a6338076955c34dbe1` |
