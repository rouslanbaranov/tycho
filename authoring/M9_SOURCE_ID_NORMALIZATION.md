# M9 source identity normalization — issue #213

Historical checkpoint: this first correction changed frontmatter only. The subsequent [canonical M9 source-ID migration](M9_CANONICAL_SOURCE_IDS.md) supersedes its statements about retaining active short source labels in the table and page bodies. Old labels now remain only for legacy lookup and distinct historical claim-row identities.

Date: 2026-10-20. Bounded corrective contract: repair the separation between M9 short source aliases and canonical book source IDs, regenerate derived indexes, and execute the complete existing Python validation inventory.

## Defect and correction

The 29 affected case pages used 33 distinct short aliases from `sources/REAL_WORLD_ARCHITECTURE_CASES.md` in `evidence_scope.source_ids`. That field requires registered global IDs, not page-local labels. Strict metadata scanning therefore stopped before routing-index freshness could be checked.

The correction registers the exact URLs under permanent global IDs and records the identity-only bridge in `sources/m9-source-aliases.json`. The bridge contains alias-to-ID mappings, not a second source or claim database. The global register owns source records; the existing M9 table retains historical discovery labels. Each affected page retains its complete body, short labels, permanent document identity, review status and dates. No source is dropped and no similar-title or fuzzy URL match is substituted.

## Evidence and limits

This is repository metadata normalization, not new external-source research. Imported records retain the inventory's initial discovery date of 2026-10-19. `resolved_url` preserves the recorded URL without claiming a new redirect check. Admission and reading use conservative pending states, with null content verification, because this correction did not reopen the sources. Existing dated source/claim-review ledgers remain authoritative for their bounded historical inspections; they are not erased or replaced by the import flags. Registration does not grant reproduction rights, certify every claim, or establish independent acceptance.

Regression tests reject a short alias, reject an unregistered prefixed ID, accept a registered ID, compare bridge URLs exactly with the M9 table, require those URLs in each mapped page body, and validate the complete corpus against the unchanged strict schema and registries. Source catalogue and route index are generated from their canonical inputs.

## Validation and workflow

Run all 12 groups in `premerge_integration_check.commands()` plus `route_index.py check` on an exact clean Git snapshot, recording all exit codes and unit-test totals. Record branch-wrapper observations separately: the existing manuscript branch is not a feature branch and is not the old explicitly allow-listed integration branch. This correction does not loosen branch rules, change GitHub Actions triggers, merge the PR or close issues/milestones.

Visual rendering and live MCP evaluation are excluded per owner direction. Local protocol fixtures remain local unit tests. A mechanical PASS is not whole-book readiness or independent content acceptance. No unrelated attachments or private source material are used.
