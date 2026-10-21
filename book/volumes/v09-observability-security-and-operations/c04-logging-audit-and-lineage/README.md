---
metadata_version: 1
id: "tycho.chapter.49cb8db3af4e406ea6988c8e5e852acf"
kind: "chapter"
parent_id: "tycho.volume.4a94b1e6f8234841afaa51af14330627"
canonical_path: "book/volumes/v09-observability-security-and-operations/c04-logging-audit-and-lineage/README.md"
title: "V09/C04 — Logging, audit and lineage"
topic_ids:
  - "observability"
perspectives:
  - "architecture"
  - "evaluation"
summary: "How do security audit, event lineage and operational logs differ? The reading route separates 2 detailed questions from the integrated decision."
route_hints:
  questions:
    - "How do security audit, event lineage and operational logs differ?"
  prerequisites:
    - "tycho.chapter.03ec5acf85e043a5a6d552a036bf4659"
  related_ids:
    - "tycho.chapter.03ec5acf85e043a5a6d552a036bf4659"
    - "tycho.page.436c2b22dc9e47acaaca7d18fadb511c"
    - "tycho.page.adde87c9a3a14c508ebd5ddb8fa676a1"
    - "tycho.page.e50b14deb6de4204b9f405942ab0cee8"
  excludes:
    - "No new benchmark, source inspection or independent edition review is asserted."
  keywords:
    - "system-design"
    - "edition-navigation"
evidence_scope:
  source_ids: []
  claim_ids: []
  status: "unknown"
  notes: "Editorial synthesis of the linked accepted manuscript; exact source versions and nonclaims remain in its page-local evidence ledger."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-20"
  reviewer: "Codex editorial assembly"
  proof_uri: null
authored_at: "2026-10-20"
updated_at: "2026-10-20"
source_inspection_date: null
content_verified_at: null
---

# V09/C04 — Logging, audit and lineage

## Purpose and mission

How do security audit, event lineage and operational logs differ? This chapter owns that question within observability, security and operational architecture. Read the mechanism together with its stated invariant, failure assumptions and evidence limits before applying the result to another system.

## Decision and worked result

Separate diagnostic logs, authoritative audit and dataset lineage by identity, durability and retention obligations.

Three records about one operation can legitimately disagree in completeness; a log line alone does not prove an authorized commit. This is an editorial conclusion drawn from the linked manuscript and its original examples, not a newly executed experiment.

## Pages and reasoning route

Begin with the integrated decision, then open the independent question that matches the missing mechanism or observed failure. Read source limits before applying the conclusion.

| Page | Independent question and role |
|---|---|
| [Integrated decision and original walkthrough](logs-audit-and-data-lineage.md) | How do security audit, event lineage and operational logs differ? |
| [Logs, authoritative audit and lineage](record-semantics.md) | Which question is answered by each kind of record? |
| [Retention, integrity and contradictory records](record-integrity.md) | Which record must survive a failure before an authorized effect can be asserted? |

## Boundaries and further reading

- [V09/C03 — Distributed tracing and propagation](../c03-distributed-tracing-and-propagation/README.md) owns the adjacent question; compare assumptions before transferring the conclusion.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V09 — Observability, security and operational architecture](../README.md) |
| Previous | [V09/C03 — Distributed tracing and propagation](../c03-distributed-tracing-and-propagation/README.md) |
| Next | [V09/C05 — Identity, authorization and threat modeling](../c05-identity-authorization-and-threat-modeling/README.md) |
| Prerequisite | [V09/C03 — Distributed tracing and propagation](../c03-distributed-tracing-and-propagation/README.md) |
| Source reading | [Page-local evidence and versions](logs-audit-and-data-lineage.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.

## Chapter source ledger

The following original citation rows, review limits and earlier topical routes are retained once for this chapter. Each question page points here and retains its inline citations. Evidence coverage must be judged at the actual claim and version, not inferred from source-list length.

<!-- tycho-question-source:tycho.page.436c2b22dc9e47acaaca7d18fadb511c:8 -->
## 7. Public source ledger and nonclaims

| Public evidence inspected | Narrow support | Unverified |
|---|---|---|
| [OpenTelemetry Logs Data Model](https://opentelemetry.io/docs/specs/otel/logs/data-model/) | Log event fields, timestamps, trace correlation and attributes | Complete durable business audit |
| [OpenLineage core specification](https://github.com/OpenLineage/OpenLineage/blob/main/spec/OpenLineage.md) | Job/Run/Dataset/Facet distinctions | Correct lineage for invented transforms |
| [OpenLineage job lineage facet](https://openlineage.io/docs/spec/facets/job-facets/lineage/) | Explicit source-target flow edges under declared job | Full traceability for any actual dataset |
| [Tycho tracing manuscript](../c03-distributed-tracing-and-propagation/distributed-tracing-context-and-sampling.md) | Causal/sampling limitations of traces | Audit-complete business history |

All identities, system behavior, logging examples, risk tables, diagram nodes and trial descriptions are independent invented teaching materials. No real logs or customer data used, no records persisted, no security/privacy auditor or technical reviewer accepted this chapter. The former combined [traces/logs/lineage/audit research](../../../observability/trace-context-lineage-and-audit.md) remains available for editorial claim reconciliation.

**Navigation:** proposed owner **V09/C04** in [book outline](../../../PROPOSED-STRUCTURE.md), current [observability landing](../../../observability/README.md); related [Distributed tracing](../c03-distributed-tracing-and-propagation/distributed-tracing-context-and-sampling.md), [Agent-safe knowledge](../c07-safety-isolation-and-privacy-in-agent-accessible-services/safe-agent-access-and-knowledge-isolation.md), [Outbox/idempotency](../../../distributed/transactional-outbox-and-idempotency.md).
<!-- /tycho-question-source -->
