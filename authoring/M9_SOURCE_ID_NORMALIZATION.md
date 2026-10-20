# M9 source identity normalization — issue #213

> **Current disposition — 2026-10-20, after PR #218 merge:** The owner confirmed independent substantive/content acceptance of all 69 primary chapter manuscripts at `986b1ddbe985079b7c647182fcf1c2fc8911d96c`. PR #218 merged into main at `f9834ef903fc5808f3a1edede208d82aac08f4e6`; #213 and E14 #15 are completed. #214 is open and ready for ten-volume/69-chapter edition assembly and named publication. The exact accepted-head 13/13 validation groups and 215/215 tests PASS are owner-reported in [PR #218](https://github.com/rouslanbaranov/tycho/pull/218#issuecomment-6294804915), not a new run on a later status commit. Earlier pending/0-of-69/review-open rows and pre-merge instructions below are historical and superseded for the manuscript acceptance gate. Their original observations and evidence limits are retained; no signed per-chapter reviewer records are manufactured. No finished physical edition or deployed service is claimed; visual rendering/live MCP remain owner-cancelled. See [current state](STATE.md) and [reconciliation](PROJECT_STATUS_RECONCILIATION_2026-10-20.md).

Historical checkpoint: this first correction changed frontmatter only. The [canonical M9 source-ID migration](M9_CANONICAL_SOURCE_IDS.md) and [evidence identity cleanup](M9_EVIDENCE_ID_CLEANUP.md) complete the normalization and remove the compatibility layer. Earlier spellings remain available in Git history only.

Date: 2026-10-20. Bounded corrective contract: repair the separation between M9 short source aliases and canonical book source IDs, regenerate derived indexes, and execute the complete existing Python validation inventory.

## Defect and correction

The 29 affected case pages used 33 distinct short aliases from `sources/REAL_WORLD_ARCHITECTURE_CASES.md` in `evidence_scope.source_ids`. That field requires registered global IDs, not page-local labels. Strict metadata scanning therefore stopped before routing-index freshness could be checked.

The initial correction registered exact URLs under permanent global IDs using a temporary identity-only bridge. The bridge has since been removed; the global register owns source records directly. No source is dropped and no similar-title or fuzzy URL match is substituted. Permanent document identities, review status and dates are unchanged; the subsequent evidence cleanup changes ledger labels without changing their payloads.

## Evidence and limits

This is repository metadata normalization, not new external-source research. Imported records retain the inventory's initial discovery date of 2026-10-19. `resolved_url` preserves the recorded URL without claiming a new redirect check. Admission and reading use conservative pending states, with null content verification, because this correction did not reopen the sources. Existing dated source/claim-review ledgers remain authoritative for their bounded historical inspections; they are not erased or replaced by the import flags. Registration does not grant reproduction rights, certify every claim, or establish independent acceptance.

Regression tests reject invalid short source IDs and unregistered prefixed IDs, accept registered IDs, compare the M9 inventory directly with canonical URLs, require those URLs in each mapped page body, and validate the complete corpus against strict schemas and registries. Source catalogue and route index are generated from their canonical inputs.

## Validation and workflow

Run all 12 groups in `premerge_integration_check.commands()` plus `route_index.py check` on an exact clean Git snapshot, recording all exit codes and unit-test totals. Record branch-wrapper observations separately: the existing manuscript branch is not a feature branch and is not the old explicitly allow-listed integration branch. This correction does not loosen branch rules, change GitHub Actions triggers, merge the PR or close issues/milestones.

Visual rendering and live MCP evaluation are excluded per owner direction. Local protocol fixtures remain local unit tests. A mechanical PASS is not whole-book readiness or independent content acceptance. No unrelated attachments or private source material are used.
