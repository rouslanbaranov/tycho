# M9 E16-08 — Executed Draft 2020-12 Case Schema Sample Validation

**Execution date:** 2026-10-19 (UTC); **scope:** two portable M9 case evidence records only. This is a **real executed local JSON Schema validation**, not the full repository command, an MCP retrieval test or independent engineering case review.

## Origin and reproducibility boundary

- Source was read through the connected GitHub integration from private `rouslanbaranov/tycho` at recursive `main` tree `544c3ffca1b9c96b7c253afcaf4f64ecbcceff7d` (not truncated).
- Source files used for validation were **manually transferred as JSON values** into the isolated Python execution container:
  - `authoring/cases/case-record.schema.json` (Git blob `cf6c15b6aafcd43b73bf18145e26d37d95b87a40`).
  - `authoring/cases/examples/case-records.json` (Git blob `4387cf0641553c0ff0c211c78ce8a70bd1c92b91`).
- **Not** an authenticated checkout of the repository. Git-blob SHA was recorded for the GitHub origin; the manual transfer was **not automatically byte-for-byte checked** against those Git blobs. Validate from a real checkout again before calling the repository itself tested.
- Local Python **3.13.5**, `jsonschema` **4.26.0**; `Draft202012Validator.check_schema(schema)`, `Draft202012Validator(schema, format_checker=FormatChecker())`.
- Local copies: schema SHA-256 `b685d7082e75b60bb765c6d234f566a236789fff396ed61fec6aadde2515f9e9`, example records SHA-256 `af220274661a6e780886ee1ce9a16039554bc84cce526d4d523e46b2559b9630`. These digests identify the **transferred test inputs**, not the raw GitHub blobs.

## Actual local executed checks

| Test | Result | Scope |
|---|---|---|
| Draft 2020-12 schema meta-validation | **PASS** | Two-file portable schema contract, not canonical K11 |
| `case.netflix.casspactor-to-analytics` | **PASS** | One company-reported claim record, no full source-semantic review |
| `case.stripe.online-subscriptions` | **PASS** | One company-reported claim record, no full source-semantic review |
| 10 deliberately malformed copies of Netflix record | **10/10 rejected** | Fails on wrong title type, short statement, wrong source-ref array type, non-string pattern/limitations, invalid ISO date, extra property, private collection name, non-HTTPS primary link, unknown review status |
| Tested production M9 schema in core K11 | **NOT RUN** | This is an independent *proposed M9 portable schema* |
| Full `python3 scripts/validate_m9_cases.py --self-test` in repository checkout | **NOT RUN** | No authenticated checkout; future command below |
| Full `python3 scripts/validate_m9_cases.py` in repository checkout | **NOT RUN** | Case index, source register, 60 fixtures not materialized in local container |
| 60 deployed MCP/search retrieval queries | **NOT RUN** | External K18–K23 runtime and results not available |
| Independent semantic, numerical or reuse-rights review | **NOT RUN** | Human/independent review gate remains open |

The ten adversarial mutations test only a representative subset of JSON Schema rules. Two passing sample records cannot certify the remaining 29 case drafts, all source claims or the implementation of the proposed schema by the future knowledge platform.

## Permanent regression protection proposed in this PR

`scripts/validate_m9_cases.py --self-test` currently verifies ten negative mutations using its dependency-free record validator. This PR updates it to **also** run `Draft202012Validator.check_schema`, the real format-checked draft validator on the good sample and the same ten negative samples **when the optional `jsonschema` package is installed**. When unavailable, it reports `NOT RUN` for the JSON Schema engine rather than claiming its fallback is full Draft2020-12 compliance.

## Commands for independent acceptance and future platform integration

After obtaining a clean real checkout at a pinned SHA:

```bash
python3 -m pip install 'jsonschema>=4.18,<5'
python3 scripts/validate_m9_cases.py --self-test
python3 scripts/validate_m9_cases.py
```

Capture real STDOUT, STDERR, process exit code, Python/jsonschema versions, repository SHA and any library/OS dependencies. If either command fails, keep the milestone open; report the specific missing source or schema issue. Once K18–K23 actual search/MCP is available, run all 60 retrieval fixtures and record citation fidelity, negative-claim refusal, temporal qualifiers, token cost and latency separately. The current result supports **only** the two copied, executed schema examples and 10 negative tests.

**Acceptance:** E16-08 #121 remains **open**, because this is a *partially executed validation slice*, not independently accepted production documentation.
