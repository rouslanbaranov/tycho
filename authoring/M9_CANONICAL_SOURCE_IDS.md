# Canonical source IDs throughout M9 — issue #213

Date: 2026-10-20. Bounded contract: use the global source-ID convention consistently in the M9 inventory, book references, evidence ledgers, portable records, retrieval fixtures, schema and validators. This is identity normalization, not new source research or technical acceptance.

All 43 M9 sources now use the global `src.` namespace and the unchanged global pattern `^src\.[a-z0-9]+(?:-[a-z0-9]+)*$`. Existing canonical identities are retained. Ten remaining candidate identities are registered by exact existing URL, under the same conservative pending-access/null-verification policy as the previous 33 identity imports. No external source access, new redirect validation or license grant is asserted.

`sources/m9-source-aliases.json` retains all 43 old-to-canonical mappings solely for legacy lookup. Active source references do not use the old keys. Existing case IDs, formal claim IDs, query IDs and historical claim-row labels are separate identity spaces and are not reminted. In particular, an old claim-row label with a numeric suffix is not an active source ID. Historical provenance notes may record an old alias as migration evidence.

The portable proposed case schema advances to `m9-case-1.1-proposal` and URN revision 2 because the source-ID contract changes incompatibly. It rejects the old short source format rather than accepting two conventions. The dependency-free validator uses the same pattern as global book metadata, and the M9 inventory ID/URL pairs must equal the canonical global register exactly. Regression tests cover both validation engines and a mismatched global URL. Source rights, review declarations, dates, source URLs, measured values and technical conclusions are preserved.

This stage supersedes the earlier frontmatter-only normalization: short labels are no longer the active source-reference convention in page bodies or the M9 table. The earlier correction remains a historical checkpoint, not a second convention.

Regenerate the source catalogue and route index, then execute all 12 integration-inventory Python groups plus explicit routing-index freshness validation at a clean pinned revision. Branch-policy wrapper limitations, visual-rendering exclusions and live-MCP exclusions remain separate and unchanged. No merge, milestone closure, whole-book acceptance or GitHub Actions execution is claimed.
