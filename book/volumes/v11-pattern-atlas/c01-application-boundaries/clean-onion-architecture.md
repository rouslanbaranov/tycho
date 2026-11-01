---
metadata_version: 1
id: "tycho.page.36431dd64c374ff1ad20e2ff69c51c9e"
kind: "page"
parent_id: "tycho.chapter.e996607f707421ca388796732547cafd"
canonical_path: >-
  book/volumes/v11-pattern-atlas/c01-application-boundaries/clean-onion-architecture.md
title: "Clean / Onion Architecture"
topic_ids:
  - "application-architecture"
  - "architecture-decisions"
perspectives:
  - "architecture"
  - "evaluation"
summary: >-
  Decision card for Clean / Onion Architecture; bounded owner evidence and
  explicit limits.
route_hints:
  questions:
    - "Should dependencies point inward toward domain policies, with frameworks
      and delivery mechanisms at the outside?"
  prerequisites:
    - "tycho.chapter.e996607f707421ca388796732547cafd"
  related_ids:
    - "tycho.chapter.e996607f707421ca388796732547cafd"
  excludes:
    - "No owner acceptance is claimed for this card."
  keywords:
    - "pattern atlas"
    - "clean architecture"
    - "onion architecture"
    - "dependency rule"
evidence_scope:
  source_ids:
    - "src.clean-architecture"
    - "src.fowler-layering"
  claim_ids: []
  status: "source-linked"
  notes: "Moved card page; alternative binding remains in the owner unit."
content_review:
  status: "independent-reviewed"
  reviewed_at: "2026-11-01"
  reviewer: "DeepSeek Reviewer"
  proof_uri: "https://github.com/rouslanbaranov/tycho/blob/466d9044/authoring/ai-reviews/2026-11-01-hexagonal-deepseek.md"
authored_at: "2026-10-30"
updated_at: "2026-11-01"
source_inspection_date: "2026-10-30"
content_verified_at: "2026-11-01"
---

# Clean / Onion Architecture

**Identity.** Clean / Onion Architecture; aliases Clean Architecture, Onion
Architecture; family Application architecture and boundaries; kind architecture-style;
priority core.

**Decision question.** Should dependencies point inward toward domain policies, with
frameworks and delivery mechanisms at the outside?

**Good-fit conditions.** Domain rules are the main asset; several delivery mechanisms or
frameworks are plausible; dependency direction can be enforced; tests need to isolate
policy from infrastructure.

**Hard contraindications.** Reject the claim when mapping overhead dominates a small CRUD
application or when ports have no genuinely different implementations; prefer simpler
layering then. Tycho guidance, not a source claim: a framework-centric application or a
team that cannot maintain boundary mapping is also a poor fit, and drawing circles as team
boundaries is not sufficient.

**Competing alternative.** Presentation-domain-data layering: dependencies run top to bottom,
presentation depends on the domain, and the domain depends on its data source. Keeping the
domain independent of its data source is arranged by introducing a mapper between the domain
and data layers, the variation Fowler calls Hexagonal Architecture. Fowler states: “A common
variation is to arrange things so that the domain does not depend on its data sources by
introducing a mapper between the domain and data source layers. This approach is often referred
to as a Hexagonal Architecture.” Hexagonal ports and adapters is a variant of the same inward
rule, not a competing alternative. Reverse the clean/onion choice when that independence is not
the protected boundary, or when the mapper adds no tested change benefit. That reversal is Tycho
guidance, not a source claim.

**Failure and recovery.** Boundary erosion and DTO/mapping complexity are common failure
modes. Tycho guidance, not a source claim: recover with an enforceable dependency test and a
deliberate adapter, not another layer name; the technical owner section states the
remaining limits.

**Technical owner.** [Layered, hexagonal and ports-and-adapters architecture](../../v02-application-boundaries-and-contracts/c01-layered-modular-and-ports-and-adapters-design/layered-hexagonal-ports-and-adapters.md#clean-onion-architecture) — The section owns dependency direction and ports; Clean/Onion vocabulary is bounded to that mechanism.

**Sources.** [src.clean-architecture](../../../../edition/patterns/reading-ledger.v1.json)
read record read.clean-architecture.2026-10-21: The Clean Architecture, sections
"The Dependency Rule", "Entities", "Use Cases", "Interface Adapters", "Frameworks and
Drivers", "Crossing boundaries". The article groups clean, onion and hexagonal as similar,
so it does not support a competing-alternative comparison. The alternative is bound to
[src.fowler-layering](../../../../edition/patterns/reading-ledger.v1.json) read record
read.fowler-layering.2026-10-21: Presentation Domain Data Layering, section "Presentation
Domain Data Layering", which states that dependencies generally run top to bottom through the
layer stack and that the mapper variation is Hexagonal Architecture, quoted in the competing
alternative above. The article is one author's explanation, not a benchmark.

**Decision state.** `applicable-under-conditions`.

**Related entries.** Hexagonal Architecture; Layered Architecture; Modular Monolith;
Domain-Driven Design / Bounded Context.
