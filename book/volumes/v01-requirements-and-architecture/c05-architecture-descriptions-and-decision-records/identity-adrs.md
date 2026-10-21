---
metadata_version: 1
id: "tycho.page.629374fc3ed84a848794c0b63c4d4ddf"
kind: "page"
parent_id: "tycho.chapter.abcbb298887b49e79525ca00fead8926"
canonical_path: "book/volumes/v01-requirements-and-architecture/c05-architecture-descriptions-and-decision-records/identity-adrs.md"
title: "Identity and evolving decision records"
topic_ids:
  - "application-architecture"
perspectives:
  - "architecture"
summary: "How do stable identities and ADRs keep several views coherent through change?"
route_hints:
  questions:
    - "How do stable identities and ADRs keep several views coherent through change?"
  prerequisites:
    - "tycho.page.13760750168f4e339d5d014e189828af"
  related_ids:
    - "tycho.chapter.abcbb298887b49e79525ca00fead8926"
    - "tycho.page.b42e3ffc4a924b7089d261d0a3dc33b0"
  excludes:
    - "No independent technical approval, runtime experiment or universal applicability is implied."
  keywords:
    - "identity"
    - "adrs"
evidence_scope:
  source_ids: []
  claim_ids: []
  status: "unknown"
  notes: "Bounded question from tycho.page.b42e3ffc4a924b7089d261d0a3dc33b0; exact inherited citation rows and limits remain in the chapter source ledger. New synthetic additions are separately labelled."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-20"
  reviewer: "Codex editorial decomposition"
  proof_uri: null
authored_at: "2026-10-20"
updated_at: "2026-10-20"
source_inspection_date: null
content_verified_at: null
---
# Identity and evolving decision records

**Owning question:** How do stable identities and ADRs keep several views coherent through change?

This page belongs to [V01/C05 — Architecture descriptions and decision records](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.

<!-- tycho-question-source:tycho.page.b42e3ffc4a924b7089d261d0a3dc33b0:4 -->
## 4. Stable identities link views without making a knowledge graph mandatory

A component named ReservationAuthority in a static chart should be referable from runtime interactions and a deployment allocation, ideally through a stable ID and a versioned description. That can be a simple Markdown table or cross-reference:

| Stable ID | Responsibility | Runtime scenario role | Deployment mapping | Evidence state |
|---|---|---|---|---|
| A-01 | Client API and command validation | A | Unknown / design choice pending | Proposed |
| D-01 | Exclusive state authority | D | Same process or external store unknown | Proposed |
| N-01 | Optional notification | No critical-path guarantee | Unknown | Proposed |

This cross-view mapping is **ordinary documentation**. It does not require building a manually curated concept graph as Tycho infrastructure. Links should have clear semantics; a cross-reference to an architecture item is not proof of runtime presence.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.b42e3ffc4a924b7089d261d0a3dc33b0:5 -->
## 5. One decision record, multiple views

**Original ADR-SYN-08 — preserve a single reservation authority.**

- **Status:** PROPOSED; not approved for a real system.
- **Context:** exclusivity and lost-response recovery matter. Load, deployment cadence and read/write skew are unknown.
- **Alternatives:** A single deployable with clear internal modules; a separately deployed reservation service; independently accepting data replicas.
- **Decision:** keep one explicit authority in the *conceptual* design. Defer runtime splitting until data ownership and quality scenarios support it.
- **Consequences:** simpler invariant reasoning; potential shared deployment and scale limits; a future extraction still needs safe authority transfer.
- **Evidence:** architecture sources explain representations, not workload feasibility; no benchmark exists.
- **Review trigger:** confirmed independent ownership, measured capacity/deployment constraint, or incompatible operational boundary.

[arc42 §9](https://docs.arc42.org/section-9/) supports contextual decision rationale, alternatives and consequences. A diagram illustrating ADR-SYN-08 cannot be substituted for the written rejection rationale, and documentation approval cannot be inferred from a merge.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.b42e3ffc4a924b7089d261d0a3dc33b0:6 -->
## 6. Keep descriptions correct through change

A useful publication process rechecks:
1. Every actor/interface in context has a declared information or effect contract.
2. Every building block has a readable responsibility and dependency direction.
3. Runtime scenarios use actual building-block identities and include significant errors/cancellations.
4. Deployment allocations name software/runtime versions and failure-domain assumptions when known.
5. The data authority is consistent between static, runtime and migration models.
6. Contradictions are recorded rather than masked; proposed targets never become observed facts by a filename rename.
7. ADR statuses, rejected options and revisit triggers remain readable across revisions.
8. Source links, revisions and known unknowns survive documentation reshuffling.

For a changed interface, update the behavior and the rationale, not only a single arrow. A view can be accurate at one revision and stale at the next, so immutable evidence/version identity matters.

<!-- /tycho-question-source -->

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](concerns-views.md) |
| Next | [Continue the reasoning](README.md) |
| Integrated question | [Original scenario and limits](architecture-views-and-decision-records.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.
