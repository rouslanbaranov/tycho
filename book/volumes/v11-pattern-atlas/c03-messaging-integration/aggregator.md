---
metadata_version: 1
id: "tycho.page.086b4b635be345b7a23ae9a6b86639f5"
kind: "page"
parent_id: "tycho.chapter.a4b31346a691566550633efe0cf2693e"
canonical_path: "book/volumes/v11-pattern-atlas/c03-messaging-integration/aggregator.md"
title: "Aggregator"
topic_ids:
  - "integration-architecture"
  - "architecture-decisions"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Decision card for Aggregator; bounded owner evidence and limits."
route_hints:
  questions:
    - "Should related messages be combined using completion and timeout rules?"
  prerequisites:
    - "tycho.chapter.a4b31346a691566550633efe0cf2693e"
  related_ids:
    - "tycho.chapter.a4b31346a691566550633efe0cf2693e"
  excludes:
    - "No owner acceptance is claimed for this card."
  keywords:
    - "pattern atlas"
    - "aggregator"
    - "message aggregation"
evidence_scope:
  source_ids:
    - "src.enterprise-integration"
    - "src.microservices-patterns"
  claim_ids: []
  status: "source-linked"
  notes: "Dedicated card page; source bindings remain in the owner unit."
content_review:
  status: "self-checked"
  reviewed_at: "2026-11-01"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-11-01"
updated_at: "2026-11-01"
source_inspection_date: "2026-11-01"
content_verified_at: null
---
# Aggregator

**Identity.** Aggregator; family Messaging and event-driven integration; kind
integration-pattern; priority core.

**Decision question.** Should related messages be combined using completion and timeout
rules?

**Good-fit conditions.** Correlation is stable; completion conditions are explicit.
Tycho guidance, not a source claim: partial results are representable, duplicate and late
messages are handled, and a per-participant timeout is available.

**Hard contraindications.** Tycho guidance, not a source claim: reject when responses are
unrelated, when one participant is authoritative, when atomicity across participants is
required, when one slow participant would consume the caller's budget, when no bounded
completion rule exists.

**Competing alternative.** Tycho synthesis: API composition is the alternative when the
caller can invoke the data-owning services and join their responses at query time. The
microservices.io page defines the API Composer and in-memory join but does not compare it
with aggregator; reverse the choice when related results already arrive as messages and
completion must trigger the combined result. Scatter-gather is a related composite, not
this alternative.

**Failure and recovery.** A single missing or delayed message can block the whole
aggregate. The source supports re-request and a timeout retry/exception choice. Tycho
guidance, not a source claim: return a declared partial result or fail as a whole, and
cancel remaining work.

**Technical owner.** [Aggregator](../../v04-distributed-coordination-and-events/c06-messaging-families-and-delivery-contracts/messaging-families-and-durable-workflows.md#aggregator) — aggregation key and timeout are bounded; partial-result policy is Tycho guidance.

**Sources.**
[src.enterprise-integration](../../../../edition/patterns/reading-ledger.v1.json)
read record read.enterprise-integration-aggregator.2026-11-01: section "Aggregator";
canonical text SHA-256
`e1c4a2c4cef8a220390b9bab78851e35d9d473bee3dd0c3e0e2f7f84e925c494` (raw HTML
`15d8640d5ad149a0e54a23c4cfe4a84c0abdcec421de2f9eb301daf21d708f58`). The page is
publisher-abridged, not a benchmark.
[src.microservices-patterns](../../../../edition/patterns/reading-ledger.v1.json)
read record read.microservices-api-composition.2026-11-01: sections "Solution" and
"Resulting context"; canonical text SHA-256
`75fae4c75e4c6d5cc8084bd4a4ecec5fed6aaf9a1816437cecf4950e0d82b4b7` (raw HTML
`7ec014c171b2421f216c3a82ddb60af0104a2f38e6bb3af93e93c8065f04750b`). The page is a
public pattern page, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** API Composition; Gateway Aggregation; Splitter; Scatter-Gather;
Correlation Identifier; Resequencer.

