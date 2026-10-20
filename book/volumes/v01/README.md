---
metadata_version: 1
id: "tycho.volume.4d10f5c93f3b4356a553c8732e513a38"
kind: "volume"
parent_id: "tycho.book.37c50125355948f1b52ec66229ef59bd"
canonical_path: "book/volumes/v01/README.md"
title: "V01 — Requirements, quality attributes and architecture fundamentals"
topic_ids:
  - "application-architecture"
  - "performance-engineering"
perspectives:
  - "architecture"
  - "evaluation"
summary: "A reasoned requirements contract that distinguishes offered demand, qualities, hard constraints, observed data and speculative improvements."
route_hints:
  questions:
    - "A reasoned requirements contract that distinguishes offered demand, qualities, hard constraints, observed data and speculative improvements."
  prerequisites: []
  related_ids:
    - "tycho.chapter.9d4f989ec9304e418f60f1ad7248094a"
    - "tycho.chapter.316b50ac3db440ae82c0986b896ff468"
    - "tycho.chapter.3d34f0b431814c9fa879a355029af2a9"
    - "tycho.chapter.ee2cd95003ab4018a9d49e2ff0b6b2f4"
    - "tycho.chapter.abcbb298887b49e79525ca00fead8926"
    - "tycho.chapter.bbfd14751d274868b152ba431dc904c9"
  excludes:
    - "No new benchmark, source inspection or independent edition review is asserted."
  keywords:
    - "system-design"
    - "edition-navigation"
evidence_scope:
  source_ids:
    - "src.microservices"
  claim_ids: []
  status: "source-linked"
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

# V01 — Requirements, quality attributes and architecture fundamentals

## Purpose and mission

Translate a problem into observable behavior, constraints and competing qualities without naming a solution prematurely.

The outcome of this volume is: A reasoned requirements contract that distinguishes offered demand, qualities, hard constraints, observed data and speculative improvements.

## A worked cross-chapter synthesis

A fictional reservation service is called slow. The first decision is whether the missing outcome is a rejected request, a committed reservation with a lost response, or an acceptable operation delayed by a queue. Each observation implies a different measurement boundary. Count users, arrival attempts and committed outcomes separately before proposing capacity.

Write a requirements contract containing an outcome, an invariant, a workload distribution, hard operating constraints and at least two competing explanations. Turn each explanation into a discriminating observation. A component diagram is useful only insofar as it locates the owner and dependency responsible for those observations.

## Questions and chapters

| Chapter | Owning question |
|---|---|
| [V01/C01 — Problem framing and system boundaries](c01/README.md) | Which actors, outcomes, interfaces and external failure dependencies define the system? |
| [V01/C02 — Workload and demand models](c02/README.md) | How do active users, offered arrivals, concurrency, operation mix and skew differ? |
| [V01/C03 — Quality attributes and trade-offs](c03/README.md) | How are performance, availability, consistency, cost, security and changeability made measurable? |
| [V01/C04 — Evidence, hypotheses and architecture experiments](c04/README.md) | What do sources, estimates, simulations and measurements actually prove? |
| [V01/C05 — Architecture descriptions and decision records](c05/README.md) | What belongs in diagrams, views, assumptions, ADRs and source-linked evidence? |
| [V01/C06 — Capacity, operational constraints and total cost](c06/README.md) | Which hard gates and team/budget limits invalidate otherwise appealing options? |

## Choosing a reading route

For a first reading, follow the chapter order. For diagnosis, connect the observed outcome to its authority and failure boundary using: [V01/C01](c01/README.md), [V01/C02](c02/README.md), [V01/C03](c03/README.md), [V01/C04](c04/README.md), [V01/C06](c06/README.md). Return to the exact page-local source ledger before making a version-specific claim.

Prerequisite context: None; a concrete user outcome or proposed system boundary is enough.

### Reasoning boundaries

This original conceptual map separates competing inputs rather than promising a universal solution.

~~~mermaid
flowchart TD
    Q["V01/C01 — Problem framing and system boundaries"] --> M["V01/C02 — Workload and demand models"]
    Q --> E["Evidence and unknown inputs"]
    M --> D{"Meets the declared constraints?"}
    E --> D
    D -->|Supported| R["V01/C06 — Capacity, operational constraints and total cost"]
    D -->|Unresolved| U["Measure, revise or retain the baseline"]
~~~

Text alternative: establish problem framing and system boundaries, compare workload and demand models with the available evidence, and either carry a supported result forward or return to unresolved inputs. The figure describes a reasoning route, not observed runtime behavior.

## Counterexample and handoff

Do not carry a synthetic latency or cost estimate into a commitment as if it were measured. A candidate that improves one quality while violating a hard integrity constraint is rejected before preference scoring. Carry the explicitly unknown recovery, load and staffing inputs into the next volume rather than inventing precise values.

## Navigation and source boundaries

| Route | Destination |
|---|---|
| Parent | [Book contents](../../README.md) |
| Next volume | [V02](../v02/README.md) |
| Historical applications | [Casebook and synthetic playbooks](../../cases/README.md) |

## Evidence and known limits

The scenario is original synthetic reasoning. The chapters contain the accepted manuscript and its published evidence; no synthetic number or historical result is a measured prediction for another system. This new synthesis is editorially self-checked, not independently certified. Source-access restrictions, unexecuted technology experiments and original case denominators remain explicit in their owning pages. Product-specific adoption still requires compatible versions and the target workload.
