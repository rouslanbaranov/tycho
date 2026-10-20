---
metadata_version: 1
id: "tycho.page.b42e3ffc4a924b7089d261d0a3dc33b0"
kind: "page"
parent_id: "tycho.chapter.abcbb298887b49e79525ca00fead8926"
canonical_path: "book/volumes/v01/c05/architecture-views-and-decision-records.md"
title: "Architecture descriptions, complementary views and decision records"
topic_ids:
  - "application-architecture"
perspectives:
  - "architecture"
summary: "Integrated question, original scenario and transfer limits for Architecture descriptions and decision records. Detailed mechanisms have separate question owners."
route_hints:
  questions:
    - "What belongs in diagrams, views, assumptions, ADRs and source-linked evidence?"
  prerequisites: []
  related_ids:
    - "tycho.page.ea94649bfd8c4be183f9114618d7ccaa"
    - "tycho.landing.1a9054fd18f64dfe911f34a4d17458c0"
    - "tycho.landing.be90d29e1bc04524b2ea41ee9beaab0f"
    - "tycho.page.4318e542ac7e445b9e8b3150effd2cff"
    - "tycho.page.06b70cb83d4f490ea9ef698a025e7684"
    - "tycho.page.c226850223614886b61b7cb36c7d5032"
    - "tycho.page.f05854fcc406435bbf38a192bc7ab2f1"
    - "tycho.page.13760750168f4e339d5d014e189828af"
    - "tycho.page.629374fc3ed84a848794c0b63c4d4ddf"
  excludes:
    - "No independent content acceptance or runtime reproduction is implied."
  keywords:
    - "Architecture"
    - "descriptions"
    - "complementary"
    - "views"
    - "and"
    - "decision"
    - "records"
evidence_scope:
  source_ids: []
  claim_ids: []
  status: "unknown"
  notes: "Only exact URL matches to the global source register are normalized here. Page-local case and evidence ledger IDs remain in the body; no claim-level mapping or source inspection is inferred."
content_review:
  status: "draft"
  reviewed_at: null
  reviewer: null
  proof_uri: null
authored_at: "2026-10-19"
updated_at: "2026-10-20"
source_inspection_date: null
content_verified_at: null
---
<!-- tycho-question-source:tycho.page.b42e3ffc4a924b7089d261d0a3dc33b0:-1 -->

# Architecture descriptions, complementary views and decision records

> **Tycho manuscript V01/C05**, original explanatory content and fictional diagrams; public arc42 §3, §5–7 and §9 source sections reviewed 2026-10-19. No observed software system, real source scan, deployed infrastructure or independently approved ADR was consulted.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.b42e3ffc4a924b7089d261d0a3dc33b0:0 -->
## Purpose and mission

An architecture description is not one diagram. A static module picture cannot show how a timeout becomes a duplicate external effect, and a sequence diagram cannot show which containers share a failure domain. Engineers should select **the minimum set of complementary views needed to answer explicit stakeholder questions**, with stable identities linking their elements and with decisions that record *why* the architecture has the stated shape.

[arc42 Building Block View §5](https://docs.arc42.org/section-5/) explains hierarchical decomposition of a system into building blocks and dependencies. [Runtime View §6](https://docs.arc42.org/section-6/) focuses on representative interactions and failures; [Deployment View §7](https://docs.arc42.org/section-7/) maps software to infrastructure. Those views answer different questions, not contradictory alternatives.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.b42e3ffc4a924b7089d261d0a3dc33b0:8 -->
## Engineering walkthrough — Reconciling one failure across architectural views

**Original synthetic trace:** an equipment reservation commits in the database, but the HTTP response disappears. In the **context view**, Client, Booking System and External Payment are separate actors; in the **building-block view**, Booking API invokes Booking Domain and Persistence Adapter; in the **runtime view**, operation K42 is committed before transport acknowledgment; in the **deployment view**, two replicas share one authoritative booking store.

A misleading diagram might show the API and database in different containers and infer that a replay on the second replica is a fresh booking. Another might label the payment provider "inside" the application simply because the integration library is included in the build. Both inconsistencies turn diagram layout into an unsupported authority claim.

| Linked artifact | Must say | Contradiction the editor rejects |
|---|---|---|
| Context | Payment is external; business result belongs to Booking | Provider internals are part of Booking authority |
| Component | Persistence Adapter commits under Booking's invariant | Controller-local memory uniquely deduplicates across replicas |
| Sequence | Commit precedes lost response; retry resolves K42 | Timeout proves transaction rollback |
| Deployment | Two API replicas share a durable writer | Replica count implies independent writers or cross-region guarantee |
| ADR | Retain one authoritative writer pending evidence of extraction benefit | Diagram quietly replaces the approved state owner |

**Review gate:** assign stable identifiers to the same components/operations in every view and walk the timeout through them, including caller-visible UNKNOWN and recovery lookup. A context diagram is not an executable access policy, a deployment view is not measured failover behavior, and an ADR is not a running system. The example has no real deployed equivalents.


**Verification status:** The preceding original example and its predicted outcomes are synthetic. No implementation experiment, benchmark or independent technical review was executed for this example.
<!-- /tycho-question-source -->

## Integrated decision and reading route

Use consistent identities across context, runtime, deployment and decision views so a failure can be followed without changing its meaning.

A tidy component view does not establish a working timeout, permission or recovery contract; follow the same ambiguous operation through every relevant view.

The detailed pages separate the mechanisms that make this decision conditional:

- [Concerns and architectural views](concerns-views.md) — Which concern is answered by a context, building-block, runtime or deployment view?
- [Identity and evolving decision records](identity-adrs.md) — How do stable identities and ADRs keep several views coherent through change?

[Chapter introduction, ordered pages and full source ledger](README.md). Original source labels retain their historical scope; this editorial decomposition does not turn proposed experiments into executed evidence.
