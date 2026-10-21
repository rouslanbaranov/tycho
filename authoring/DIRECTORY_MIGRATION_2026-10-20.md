# Readable directory migration — 2026-10-20

Refs #214. Baseline main commit: `60ddcda6d82fa59cd39a660261b0846973ad5c0b`; tree: `686632d19757b2587c2536ff0681ccaee9cccda5`.

## Delivered layout

All **ten volumes and 71 chapters** have readable numbered English directory names. **339 canonical files move**; all **406 opaque document IDs**, parent relationships and reading order remain. No duplicate numbered-only directory tree remains. The [machine-readable map](../edition/directory-migration.json) lists all 81 directory mappings and every document's old/new path and baseline SHA-256. The [current outline](../edition/outline.json) owns the selected active paths.

| Volume | Directory |
| --- | --- |
| V01 | `v01-requirements-and-architecture` |
| V02 | `v02-application-boundaries-and-contracts` |
| V03 | `v03-execution-concurrency-and-flow-control` |
| V04 | `v04-distributed-coordination-and-events` |
| V05 | `v05-data-models-engines-and-lifecycle` |
| V06 | `v06-caching-indexing-and-retrieval` |
| V07 | `v07-performance-scale-and-resilience` |
| V08 | `v08-delivery-deployment-and-recovery` |
| V09 | `v09-observability-security-and-operations` |
| V10 | `v10-decision-support-and-modernization` |

The first chapter is [V01/C01](../book/volumes/v01-requirements-and-architecture/c01-problem-framing/README.md). Chapter names are derived from the existing English titles, with the established two-digit local chapter ordinal retained. Page filenames and `README.md` landing names remain.

## Conservation and historical evidence

The migration changes directory path segments, local navigation destinations and current `canonical_path` values. It introduces no new technical explanation, evidence reading, diagram, source verification or acceptance declaration. External URLs, query strings and fragments retain their spelling.

For **all 406 canonical documents**, applying the inverse directory transform reproduces the entire baseline file byte for byte, including frontmatter, source blocks, prose, code and citations. This is stronger than comparing only page counts or rendered text. Active identity records change their paths while preserving IDs, origin and migration-body hashes.

The original `edition/migration.json`, `edition/decomposition-plan.json`, `edition/decomposition-manifest.json` and `edition/enrichment-manifest.json` are byte-identical to the baseline. Their hashes are protected by the new directory record. The decomposition and enrichment validators read the migrated files through an inverse historical path view; they still execute their original payload, owner, provenance and insertion checks. They do not replace historical hashes with hashes of rewritten content. The original 739 source blocks and 839 fragment routes retain their historical assertions.

Current outline and identity paths, book/supporting-page navigation, local links in earlier editorial reports, pilot routes, and test path adapters are reconciled. Immutable HTTP links to earlier commits and archived execution logs remain historical references. One-time assembly/decomposition scripts retain their original inputs and guards. They are not rerun as current-layout generators.

## Validation

The dedicated naming/conservation validator and all nine new migration tests passed, together with the unchanged thirteen decomposition tests and five enrichment adversarial tests. New negative cases reject prose drift, missing map membership, colliding destinations, duplicate legacy copies, historical-manifest changes and names without descriptions. A separate case preserves external URLs/query/fragment spelling, and strict-runner coverage is asserted.

Actual execution passed **17/17 Python groups, 242/242 tests with zero skips, and 221/221 Mermaid syntax parses**. Required feature premerge separately passed its 221-test subset, including the naming boundary and all nine new tests; repeated tests are not added to the full-suite total. All 4,243 local links in 393 changed Markdown files resolved, including 200 fragment checks. One earlier edition link with a renderer-dependent fragment now targets the stable book landing. [Exact commands and results](validation/2026-10-20-directories/results.json), [full unittest log](validation/2026-10-20-directories/all-tests.log), [Mermaid parser rows](validation/2026-10-20-directories/mermaid.json) and [link results](validation/2026-10-20-directories/links.json) retain the evidence. Final postflight results and the exact delivered tree are recorded in the PR. The index and inventory are rebuilt deliberately after reviewing the path-only delta. This record does not transfer the earlier rc.3 execution report onto a different tree.

## Remaining acceptance

The physical directory migration is implemented. #214 remains **open** for substantive page acceptance and final edition disposition, as instructed by the owner. No milestone closure, scheduled or PR/push CI, hosted service, final release or independent certification is implied. Existing example-execution waivers and cancelled browser/live MCP gates remain unchanged.
