# Tycho roadmap

**Updated:** 2026-10-20, after manuscript acceptance and merge. See [current state](STATE.md) and [reconciliation](PROJECT_STATUS_RECONCILIATION_2026-10-20.md).

## Delivery order

| Phase | Actual state | Next gate |
|---|---|---|
| Integrated M1–M9 draft | Merged through PR #216 | Historical baseline retained |
| #213 — 69-chapter manuscript | Owner-confirmed substantive acceptance at `986b1ddbe985079b7c647182fcf1c2fc8911d96c`; PR #218 merged; #213/E14 completed | Content baseline available for assembly |
| **#214 — edition assembly/publication** | Edition 2026.10.0 assembled: ten volumes, 69 primary chapters/pages, 215 canonical documents; frozen inventory and publication PR control delivery | Substantive volume/chapter landings, bounded pages, reversible identity/path migration, synthesis/navigation, fresh index, full frozen-tree checks and named release |
| Knowledge retrieval | Strict schema and complete 215-document offline routing exist; hosted lexical/semantic/hybrid service absent | Evaluated relevance, provenance, consistency and total agent cost |
| MCP/Rocinante | Subsequent roadmap work, not deployed | Read-only search/read/verify, onboarding, specialist integration and isolation |
| Deployment/operations | Planned | Immutable snapshots, Ansible/container delivery, monitoring and rollback |

## Validation and delivery policy

The owner's accepted-head test report records 13/13 groups and 215/215 tests, zero skips, at `986b1ddbe985079b7c647182fcf1c2fc8911d96c`. Do not attribute it to later documentation commits. Indexed-page edits require a deterministic index rebuild/check and relevant local premerge validation, with results recorded against the actual checked tree.

Keep issue-specific feature branches and PR review. Visual rendering and live MCP remain owner-cancelled; milestone-only CI remains unchanged. Milestone verification, service deployment and book publication are separate events.

## Permanent constraints

Tycho is standalone and English, using independently admitted public sources and original synthetic material. The 29 historical cases and six synthetic playbooks are one applied reading layer, not an eleventh volume. Curated graph infrastructure remains excluded by [ADR](ADR-RETIRE-CURATED-KNOWLEDGE-GRAPH.md). Preserve existing metadata, provenance, schema and indexing facilities.

The [K01–K30 plan](knowledge-platform-and-mcp-plan.md) is a requirements inventory, not proof of delivered services. Retrieval, MCP and deployment resume after final edition publication.
