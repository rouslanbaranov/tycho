---
metadata_version: 1
id: "tycho.page.b8d02f9b40c44c729e2b99e01a8b0dbf"
kind: "page"
parent_id: "tycho.chapter.bbfd14751d274868b152ba431dc904c9"
canonical_path: "book/volumes/v01/c06/lifecycle-cost.md"
title: "Lifecycle cost and sensitivity"
topic_ids:
  - "application-architecture"
perspectives:
  - "architecture"
summary: "Which migration, dual-running and rollback costs can reverse a cost comparison?"
route_hints:
  questions:
    - "Which migration, dual-running and rollback costs can reverse a cost comparison?"
  prerequisites:
    - "tycho.page.8284605817fc48dba499425b0d908df0"
  related_ids:
    - "tycho.chapter.bbfd14751d274868b152ba431dc904c9"
    - "tycho.page.76244dbe2bd44035b7154f821191f6f2"
    - "tycho.page.f3b4041502a7403bbc63bb2611eb5c0f"
  excludes:
    - "No independent technical approval, runtime experiment or universal applicability is implied."
  keywords:
    - "lifecycle"
    - "cost"
evidence_scope:
  source_ids: []
  claim_ids: []
  status: "unknown"
  notes: "Bounded question from tycho.page.76244dbe2bd44035b7154f821191f6f2; exact inherited citation rows and limits remain in the chapter source ledger. New synthetic additions are separately labelled."
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
# Lifecycle cost and sensitivity

**Owning question:** Which migration, dual-running and rollback costs can reverse a cost comparison?

This page belongs to [V01/C06 — Capacity, operational constraints and total cost](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.

<!-- tycho-question-source:tycho.page.76244dbe2bd44035b7154f821191f6f2:3 -->
## 3. Original synthetic case: a community plant catalogue

A fictional cataloguing site serves public plant descriptions and permits moderated updates. Engineers propose a distributed event-driven design with several separately deployed services.

The site has a hypothetical small operating team, intermittent update traffic, strict moderation and a requirement to restore approved changes after an instance loss. No real staffing budget or cloud provider has been selected.

Three proposals:
- **A: modular single deployable with one authoritative database.** Fewer deployables; may still need multiple replicas, correct backup/recovery and module boundary tests.
- **B: independent services with an event broker.** Useful if measured release/data autonomy and failure isolation justify remote boundaries; adds broker operations, retries and cross-service invariants.
- **C: managed read-only catalogue with a separate authorized moderation workflow.** May simplify the public access path if moderation and publication semantics can be clearly separated; external service limits/lock-in need evaluation.

| Hard gate | A | B | C |
|---|---|---|---|
| Moderation/authorization cannot be bypassed | Must enforce at write authority | Same, now across more interfaces | Separate publish gate must be verified |
| Durable approved content recoverable | Requires tested backup and restore | Requires multi-store/event recovery | Depends on storage and export guarantee |
| Small available operation skill | Plausibly lower surface; must test | Unknown: broker/runbook staffing | Unknown: managed-service/provider constraints |
| Existing clients compatible during change | Local change may be bounded | More versioned interfaces | Potential contract changes |
| Total cost <= owner-approved budget | Unknown until quantified | Unknown until complete run/incident cost | Unknown until prices and migration effort |

Every cell here is a **candidate research state**, not acceptance or price estimate. Because operational and cost evidence is missing, the appropriate result is **MEASURE_FIRST/INSUFFICIENT_EVIDENCE**, not universal preference for A or rejection of B.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.76244dbe2bd44035b7154f821191f6f2:4 -->
## 4. Operating cost is a lifecycle, not a monthly instance fee

Include:
- recurring compute/storage/network/replication and idle redundancy;
- event, audit and trace retention/transfer;
- CI, dependency update, security scanning and test environment capacity;
- scheduled change/release effort and support of old clients;
- incident detection, restoration drills, credential/key rotation;
- migration double-running, data reformatting and rollback/repair;
- staff training and long-lived maintenance of bespoke control mechanisms;
- decommissioning and data retention after features are retired.

The [AWS cost principles](https://docs.aws.amazon.com/wellarchitected/latest/framework/cost-dp.html) encourage relating expense to business output; a product can pay less for idle resources and still incur more cost from outages or manual maintenance. A credible comparison uses the **same horizon**, workload mix and mandatory service levels. “Managed service” shifts responsibilities but does not remove recovery/access/lifecycle obligations.

<!-- /tycho-question-source -->

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](feasibility-gates.md) |
| Next | [Continue the reasoning](operating-capacity.md) |
| Integrated question | [Original scenario and limits](operational-constraints-and-total-cost-gates.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.
