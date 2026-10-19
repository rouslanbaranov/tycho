# M9 E16-08 — Curated Primary Source Link Coverage across Case Drafts

**Date:** 2026-10-19 · **Scope:** static, connected-GitHub case-page source link inspection and portable M9 validator extension, not final claim or publication verification.

## Actual inspection

All **29** existing `book/cases/*.md` pages were read in three bounded GitHub batches and compared against the **43** literal primary URLs from `sources/REAL_WORLD_ARCHITECTURE_CASES.md`.

- **29/29** pages contained at least one **matching registered ID and exact registered HTTPS URL**.
- Some cases mention *additional comparison-source IDs* without embedding their first-party URL locally; e.g. the Netflix Java platform case mentions Shopify SH01 and Netflix N06 as contrasts. These mentions are **not automatically invalid** and should not be silently promoted to independently cited technical claims.
- This check establishes one direct primary-source foothold per case, not full coverage of every factual sentence, historical revision or quoted metric.
- The inspection used connected-GitHub string/ID checks, **not execution of `scripts/validate_m9_cases.py` on a full checkout**.

## Durable validation guard

The existing `read_case_catalog(root)` remains usable for standalone synthetic unit tests; production `check(root)` now supplies the curated `source_id → URL` dictionary to an optional `source_urls` parameter. For every indexed case, the checker requires **at least one exact registered URL whose ID also occurs in the case text**. This supplements the already merged strict portable-claim source URL binding (PR #205) without making the false assumption that every cross-company ID mention must repeat its URL.

The new synthetic regression case creates 20 case pages with matching ID/URL, then changes one URL to an unrelated article **at the same hostname** and verifies that source coverage rejects it.

## Deliberate limitations

- Presence of a URL is **not** proof of publisher identity, reachable content, copyright license or truth of the associated prose.
- A technically unrelated link containing a valid ID elsewhere on the same page could still pass a page-level presence gate. Claim-by-claim provenance and independent technical review remain necessary.
- Original M9 portable records only cover two sample cases; production K18–K23 provenance and MCP contracts remain owned by the core roadmap.
- The Python unit test and full checker are **not recorded as executed** until a pinned checkout run captures actual output and exit code.
- Core Scheduled Tasks, E07 index prototype PR #188 and original M1–M8 issues are not changed by this gate.

Independent E16-08 issue **#121** remains open.
