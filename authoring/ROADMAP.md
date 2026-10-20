# Tycho roadmap

**Updated:** 2026-10-20. See [current state](STATE.md) and [reconciliation](PROJECT_STATUS_RECONCILIATION_2026-10-20.md). This supersedes the October 18 pilot-first work sequence.

## Delivery order

| Phase | Actual state | Gate |
|---|---|---|
| Integrated M1–M9 draft | Merged via PR #216: 69 primary owner drafts, 29 historical cases, six synthetic playbooks | Earlier owner-approved **integrated-draft** acceptance only |
| **1. #213 — substantive 69-chapter completion** | 69/69 deepened, **0/69 independently accepted for final-book scope**. Open PR #218 replaces closed/unmerged #217 | Full bounded engineering explanations, exact public-source/claim verification, alternatives, failure/recovery, contradictions, review disposition for each chapter |
| **2. #214 — book assembly/publication** | Selected 10-volume/69-chapter TOC; no published edition | Real substantive volume/chapter landings, bounded pages, stable ID and source migration, coherent reading paths, rebuilt index, full frozen-tree checks, named release |
| **3. Knowledge retrieval** | Strict JSON Schema and local 136-doc deterministic routing exist; hosted lexical/semantic/hybrid service absent | Independently evaluated relevance, provenance, update consistency and agent token/cost efficiency |
| **4. MCP/Rocinante** | Required later roadmap work, not deployed | Read-only agent search/read/verify, generic onboarding, specialist integration, compatibility, access isolation |
| **5. Deployment/operations** | Planned | Immutable snapshots, security, Ansible/container delivery, monitoring, rollback, evaluations |

## Premerge policy

Keep PR #218 **unmerged** during status-document updates. Preserve correctly named `feature/TYCHO-213-audit-and-complete-all-69-planned-system-design-chapters`, and keep #213/E14 open until independent chapter acceptance exists. Rebuild `generated/route-index.v1.json` whenever any `book/**/*.md` changes, then rerun full local Python/premerge tests at the **exact new HEAD**. Previously passing 215 tests belong to the old pinned revision and cannot be attributed to this documentation update.

Visual rendering and live MCP tests were **cancelled by owner**, not passed. CI is milestone-close-only. No automatic milestone/issue closure, fabricated external review, host/service deployment or benchmark claims.

## Permanent constraints

Tycho is standalone and English, with independently admissible public sources and original synthetic examples. The 29 historical and six synthetic M9 applications are the applied casebook, **not** an eleventh conceptual volume. A curated Tycho knowledge-graph database/pipeline and graph-dependent search/MCP gates are excluded by [ADR](ADR-RETIRE-CURATED-KNOWLEDGE-GRAPH.md), although graph theory remains a book subject. Avoid reimplementing existing schema, metadata, source/provenance and local indexing facilities.

[K01–K30 knowledge-service plan](knowledge-platform-and-mcp-plan.md) remains the long-term *requirements inventory*, not a live implementation-status ledger. Future capability work resumes after substantive book content and final publication.
