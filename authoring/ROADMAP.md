# Tycho roadmap

> **Historical planning record, last updated 2026-10-20.** Current counts and
> gates live in [current state](STATE.md). See also the dated
> [reconciliation](PROJECT_STATUS_RECONCILIATION_2026-10-20.md).

The delivery table below records the plan at that date.

## Delivery order

| Phase | Actual state | Next gate |
|---|---|---|
| Integrated M1–M9 draft | Merged through PR #216 | Historical baseline retained |
| #213 — 69-chapter manuscript | Owner-confirmed substantive acceptance at `986b1ddbe985079b7c647182fcf1c2fc8911d96c`; PR #218 merged; #213/E14 completed | Content baseline available for assembly |
| **#214 — edition assembly/publication** | Open: enrichment candidate rc.3 has 71 chapters/406 canonical documents, including five additional mechanisms and three complete worked projects after the first-pass additions; readable directory migration is implemented; Python/Mermaid execution passed (16 groups, 233 tests, 221 diagrams); substantive acceptance remains pending | Substantive volume/chapter landings, bounded pages, reversible identity/path migration, synthesis/navigation, fresh index, full frozen-tree checks and named release |
| Knowledge retrieval | Offline routing infrastructure exists; candidate index extends to 406 documents and Python regeneration/check passed; hosted lexical/semantic/hybrid service absent | Evaluated relevance, provenance, consistency and total agent cost |
| MCP/external agent | Subsequent roadmap work, not deployed | Read-only search/read/verify, onboarding, integration and isolation |
| Deployment/operations | Planned | Immutable snapshots, Ansible/container delivery, monitoring and rollback |

## Validation and delivery policy

The owner's accepted-head test report records 13/13 groups and 215/215 tests, zero skips, at `986b1ddbe985079b7c647182fcf1c2fc8911d96c`. Do not attribute it to later documentation commits. Indexed-page edits require a deterministic index rebuild/check and relevant local premerge validation, with results recorded against the actual checked tree.

Keep issue-specific feature branches and PR review. Visual rendering and live MCP remain owner-cancelled; milestone-only CI remains unchanged. Milestone verification, service deployment and book publication are separate events.

## Permanent constraints

Tycho is standalone and English, using independently admitted public sources and original synthetic material. The 29 historical cases and six synthetic playbooks are one applied reading layer, not an eleventh volume. Curated graph infrastructure remains excluded by [ADR](ADR-RETIRE-CURATED-KNOWLEDGE-GRAPH.md). Preserve existing metadata, provenance, schema and indexing facilities.

The [K01–K30 plan](knowledge-platform-and-mcp-plan.md) is a requirements inventory, not proof of delivered services. Retrieval, MCP and deployment resume after final edition publication.
