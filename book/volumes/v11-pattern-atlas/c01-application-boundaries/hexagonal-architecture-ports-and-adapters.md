---
metadata_version: 1
id: "tycho.page.04834d836a4a5a5a8e8da37612a599f4"
kind: "page"
parent_id: "tycho.chapter.e996607f707421ca388796732547cafd"
canonical_path: "book/volumes/v11-pattern-atlas/c01-application-boundaries/\
  hexagonal-architecture-ports-and-adapters.md"
title: "Hexagonal Architecture / Ports and Adapters"
topic_ids:
  - "application-architecture"
  - "architecture-decisions"
perspectives:
  - "architecture"
  - "evaluation"
summary: >-
  Decision card for Hexagonal Architecture / Ports and Adapters; bounded owner
  evidence and explicit limits.
route_hints:
  questions:
    - >-
      Should domain logic be isolated from input/output technology through
      explicit ports and adapters?
  prerequisites:
    - "tycho.chapter.e996607f707421ca388796732547cafd"
  related_ids:
    - "tycho.chapter.e996607f707421ca388796732547cafd"
  excludes:
    - >-
      No owner acceptance is claimed for this card.
  keywords:
    - "pattern atlas"
    - "hexagonal architecture"
    - "ports and adapters"
    - "application architecture and boundaries"
evidence_scope:
  source_ids:
    - "src.aws-hexagonal"
  claim_ids: []
  status: "source-linked"
  notes: >-
    Card cites read.aws-hexagonal.2026-10-21; owner section and limits are
    bounded.
content_review:
  status: "independent-reviewed"
  reviewed_at: "2026-11-01"
  reviewer: "DeepSeek Reviewer"
  proof_uri: "https://github.com/rouslanbaranov/tycho/blob/466d9044/authoring/ai-reviews/2026-11-01-hexagonal-deepseek.md"
authored_at: "2026-11-01"
updated_at: "2026-11-01"
source_inspection_date: "2026-10-21"
content_verified_at: "2026-11-01"
---
# Hexagonal Architecture / Ports and Adapters

**Identity.** Hexagonal Architecture / Ports and Adapters; aliases Ports and Adapters;
family Application architecture and boundaries; kind architecture-style; priority core.

**Decision question.** Should domain logic be isolated from input/output technology
through explicit ports and adapters?

**Good-fit conditions.** The domain has behavior worth protecting; more than one adapter
or technology is plausible; tests need to run without external systems; a legacy or
vendor boundary is being replaced incrementally.

**Hard contraindications.** Reject the claim for a trivial CRUD surface with one stable
adapter; when no domain behavior exists to isolate; when the team cannot own mapping and
contract tests; or when ports are used to justify a distributed service split without
operational need.

**Competing alternative.** Layered architecture without ports, or a modular monolith
with direct adapters. Reverse the choice when adapter variability disappears or the
abstraction cost exceeds the isolation benefit.

**Failure and recovery.** Mapping layers add latency overhead and can translate adapter errors
inconsistently; **Tycho guidance:** contract tests and explicit error translation keep the
boundary honest. Ports can leak technology types; that is a review finding, not a source claim.

**Technical owner.** [Hexagonal Architecture / Ports and Adapters](../../v02-application-boundaries-and-contracts/c01-layered-modular-and-ports-and-adapters-design/layered-hexagonal-ports-and-adapters.md#hexagonal-architecture-and-ports-and-adapters).

**Sources.** [src.aws-hexagonal](../../../../edition/patterns/reading-ledger.v1.json)
read record `read.aws-hexagonal.2026-10-21`: all sixteen served headings read.
This is a vendor pattern
page, not a comparative study.

**Decision state.** `applicable-under-conditions`.

**Related entries.** Layered Architecture; Clean / Onion Architecture; Anti-Corruption
Layer; Modular Monolith.
