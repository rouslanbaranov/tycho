# M9 / E16-08 — Date Format and Cross-Field Semantic Validation Regression

**Date:** 2026-10-19 · **Classification:** M9 portable record validator correctness, not a production K11 schema rollout.

## Defect and impact

The dependency-free Python `iso_date()` used `datetime.date.fromisoformat(value)` alone. Python 3.13.5 accepts ISO basic calendar dates such as `20261019` and ISO week dates such as `2026-W43-1`. The proposed M9 case-record JSON Schema declares `format: date` (RFC 3339 `full-date`), for which the Draft 2020-12 `FormatChecker` rejects both. Hence the fallback could report a malformed source/claim date as valid while the full validator rejected it.

Separately, `valid_from='2026-10-20'` and `valid_until='2026-10-19'` each pass `format: date` even though the ordered interval is invalid. The proposed JSON Schema does **not** express the cross-field comparison. A separate semantic invariant is required; it was already correctly implemented by `validate_record()` in a prior repair.

## Patch in this change

1. Require a strict full-match of the ASCII `[0-9]{4}-[0-9]{2}-[0-9]{2}` calendar-date syntax, then run `datetime.date.fromisoformat` to reject impossible calendar days.
2. Retain the independent semantic check `valid_from <= valid_until` when both values are known.
3. Extend `--self-test` from **10** to **13** negative mutations, adding `basic_date`, `week_date`, and `invalid_calendar_date`.
4. Let the actual Draft 2020-12 engine reject the **12 schema-invalid** mutations; it must **accept** the one reversed-window mutation, which only the semantic check rejects. Do not claim JSON Schema implements cross-field ordering.

## Executed isolated regression probe

In the local execution container (Python **3.13.5**, `jsonschema` **4.26.0**), the exact new regular-expression + `date.fromisoformat` predicate and a real Draft 2020-12 validator were executed against the two previously transferred M9 example records in `/mnt/data/m9_validation`. The probe used copied JSON values, **not an authenticated, byte-verified full repository checkout**.

| Input | Strict Python calendar predicate | Draft 2020-12 + format checker | Interpretation |
|---|---|---|---|
| `2026-10-19` | Accept | Accept | Canonical full-date |
| `20261019` | Reject | Reject | Invalid basic-date format |
| `2026-W43-1` | Reject | Reject | Invalid week-date format |
| `2026-02-30` | Reject | Reject | Invalid calendar day |
| Valid `2026-10-20` start and earlier `2026-10-19` end | Reject by semantic comparison | Accept both date strings | Cross-field invariant, not standard JSON Schema validation |

**Measured outcome of the local probe:** 4/4 expected Python date-classification results and 3/3 JSON Schema invalid-date mutants rejected. The inverted range is, correctly, schema-valid but semantically invalid. The patch's entire `--self-test` and end-to-end repository checker were **not executed** in the local checkout in this session; their outcomes remain unverified.

## Remaining acceptance

To demonstrate the actual GitHub script runs, pin a repository checkout SHA and record exit codes/STDOUT/STDERR from:

```bash
python3 scripts/validate_m9_cases.py --self-test
python3 scripts/validate_m9_cases.py
```

When `jsonschema` is installed, the intended `--self-test` output should independently confirm the **13** fallback rejects, the **12** real JSON Schema violations, and the **1** reversed-interval semantic rejection. Confirm outputs, do not copy these expected values into 'test passed' without a run.

This is an original Tycho M9 test note; it includes no private employer sources, no copied publisher diagrams and no implementation in core Tycho K11/MCP.
