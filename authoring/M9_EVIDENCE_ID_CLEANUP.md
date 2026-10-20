# Complete M9 evidence identity cleanup — issue #213

Date: 2026-10-20. Bounded contract: remove the temporary alias compatibility layer and remaining abbreviated evidence-row labels while preserving source bindings, statement payloads, formal case/claim/query identities and review declarations. No new external research, technical acceptance or source rights are asserted.

## Identity rules

Sources retain registered `src.` IDs. Ledger rows now use `evidence.m9-<source-token>.<numeric-suffix>` identities, separately from formal `claim.` records. Numeric suffixes are preserved verbatim, including leading zeros: different existing labels must never be collapsed by padding or renumbering. A row's source is the corresponding registered canonical source ID. Existing repetitions in different ledger documents remain distinct definition locations rather than being silently deduplicated.

The temporary compatibility table is removed. Current source lookups go directly to `sources/register.json`; old spellings can be recovered from Git history. No shared history is rewritten. Unrelated pilot query IDs are outside the M9 source/evidence identity namespace and remain unchanged.

## Tests created before replacement

The fixture `tests/fixtures/m9-evidence-migration-baseline.json` was captured from commit `592968cc013181c4b9bdb3b994503e971fd9d4e1` before changing labels. It records 123 definition locations, 116 distinct evidence identities, exact canonical source URLs and SHA-256 fingerprints of every table-row payload excluding its identity cell. It contains hashes, not duplicated source prose or a second claim database. The fixture uses target identities only, not a legacy alias mapping.

Tests were first run against the unmodified ledgers: lossless-current-corpus validation and compatibility-table absence failed as expected, while synthetic guards passed. The migration is accepted only when those checks pass without changing the captured payloads. Negative tests reject a missing row, duplicated definition, changed statement/qualifier hash, wrong source, changed primary URL and suffix renumbering. Canonical source tests no longer load an alias table and reject remaining old labels in M9 content. The normal M9 validator invokes this evidence check as well.

Intentional later edits to these evidence rows require an explicit, reviewed baseline update; do not regenerate fingerprints merely to make an unexplained failure disappear. Hash equality proves preservation through this migration, not correctness of the underlying technical assertions.

## Verification and limits

Regenerate the source catalogue and routing index, run the complete existing Python inventory on the final pinned clean revision, and inspect Markdown navigation/approximate anchors. Browser rendering and live MCP remain excluded per owner direction. Branch-policy wrappers still have their existing manuscript-branch limitation. This change does not alter branch rules, CI triggers, independent-review status, main, PR merge state or milestones.
