# M9 E16-08 — Curated Source ID to Primary URL Integrity Gate

**Date:** 2026-10-19 · **Issue:** #121 · **Scope:** Portable M9 `case-record` proposal, not production Rocinante/Adro provenance replacement.

## Defect

The M9 record validator previously required a syntactically HTTPS `claims[].primary_url` and a registered `claims[].source_ref_id`, but did **not** verify that they referred to the same first-party publication. An invalid record could cite source N11 while embedding Stripe ST01's URL, or another article at the same publisher. A future agent could then carry the wrong claim/URL pairing into retrieval or review, even if JSON Schema validation and basic source-ID membership both succeeded.

## Change and deliberately strict URL policy

- Parse all **43 unique** entries in the existing [public M9 source register](../../sources/REAL_WORLD_ARCHITECTURE_CASES.md) to a `source ID → exact primary HTTPS URL` lookup. Fail on duplicate IDs, absent HTTPS Markdown link or changes that make a candidate unparseable.
- `validate_record` now checks `claim.primary_url == registered_sources[claim.source_ref_id]`, in addition to existing case→source membership and strict shape/date checks. Both existing portable sample records (**N11**, **ST01**) use the same literal URL as the curated register.
- Deliberately require the **exact registered URL**, not just matching domain or suffix. Canonical URL changes and publisher redirects must be reviewed and updated explicitly in the source register and affected case records; no network lookup or silent normalization may change provenance.
- Existing independent-review metadata and snapshot-root protections remain unchanged.
- Extend the offline `--self-test` from **16 to 18 negative mutations**: different publisher's registered URL and an invented same-host URL. These two are valid URL strings for the *base* Draft 2020-12 JSON Schema but invalid source-provenance relationships. Together with the inverted date-window, three errors require semantic/cross-record validation rather than JSON Schema alone.

## Checks performed in the connected GitHub research environment

The original public source register was parsed and checked: **43 URL-bearing rows**, **43 distinct IDs**, **0 missing primary URLs**, and the N11/ST01 sample claim URLs **equal** their corresponding registered entries.

The new Python source code and its two unittest methods were added in GitHub. The full repository `--self-test`, the 14 unittest methods and deployed MCP retrieval were **not executed** in this environment. The source identity checks above were executed as a direct JS parsing/lookup analysis of GitHub-returned source text, not as a Python script execution.

## Limits and required follow-up

This gate detects local **reference consistency**. It does not prove that a remote URL still resolves, an article was written by the asserted company, or a particular paragraph supports a claim. Those need independent primary-source/claim/temporal verification. M9 case pages may still contain multiple source links; this checks the **portable sample claim records**, not all prose citations across 29 drafts.

To reproduce on the exact pinned checkout:

```bash
python3 -m unittest discover -s tests -p 'test_m9_validator*.py' -v
python3 scripts/validate_m9_cases.py --self-test --root .
python3 scripts/validate_m9_cases.py --root .
```

Preserve command outputs and revision SHA, run `jsonschema`'s optional FormatChecker where installed, and treat new errors as reviewable source-catalog discrepancies, not grounds to invent a different primary URL. Issue #121 must remain open for independent source/technical review and actual MCP evaluation or authorized dependency disposition.

No employer/Adro sources, core M1–M8 features, Scheduled Tasks or GitHub Actions modifications were introduced.
