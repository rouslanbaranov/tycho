---
metadata_version: 1
id: "tycho.page.4318e542ac7e445b9e8b3150effd2cff"
kind: "page"
parent_id: "tycho.chapter.9d4f989ec9304e418f60f1ad7248094a"
canonical_path: "book/volumes/v01-requirements-and-architecture/c01-problem-framing/problem-framing-and-system-boundaries.md"
title: "Problem framing and system boundaries: architecture begins outside the code"
topic_ids:
  - "application-architecture"
perspectives:
  - "architecture"
summary: "Integrated question, original scenario and transfer limits for Problem framing and system boundaries. Detailed mechanisms have separate question owners."
route_hints:
  questions:
    - "Which actors, outcomes, interfaces and external failure dependencies define the system?"
  prerequisites: []
  related_ids:
    - "tycho.page.868027aee4884210bea1d8a6542fbfb0"
    - "tycho.page.cccbd188936543a2aaf904f4002236d8"
    - "tycho.page.ace968ab1de8409383c6a9b22a00d006"
    - "tycho.page.dde63373c50f4f4a80e727b6e160def5"
    - "tycho.page.c226850223614886b61b7cb36c7d5032"
    - "tycho.page.35d5be6a4e074758afff95bf3ec68bc5"
    - "tycho.page.0ce5d0aaf63f425ebf556ea97e2d24a9"
    - "tycho.landing.1a9054fd18f64dfe911f34a4d17458c0"
    - "tycho.landing.be90d29e1bc04524b2ea41ee9beaab0f"
    - "tycho.page.06b70cb83d4f490ea9ef698a025e7684"
    - "tycho.page.de62a6f0e5a145aea3798ee69715f033"
    - "tycho.page.15ffb7535c424b0eac6445cddaeb4a25"
    - "tycho.page.b6be128c3e714ac68ef3311a30d65141"
  excludes:
    - "No independent content acceptance or runtime reproduction is implied."
  keywords:
    - "Problem"
    - "framing"
    - "and"
    - "system"
    - "boundaries"
    - "architecture"
    - "begins"
    - "outside"
    - "the"
    - "code"
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
<!-- tycho-question-source:tycho.page.4318e542ac7e445b9e8b3150effd2cff:-1 -->

# Problem framing and system boundaries: architecture begins outside the code

> **Tycho V01/C01, original System Design book draft (2026-10-19).** This is a question-led architectural explanation using independently public arc42, C4 and the openly available ISO/IEC/IEEE 42010:2022 abstract. Every example and diagram below is invented. No actual client system, stakeholder interview, verified production boundary or independent architecture assessment is claimed.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.4318e542ac7e445b9e8b3150effd2cff:0 -->
## Purpose and mission

Before selecting a database, architecture style or runtime, define **the system whose success will be judged**. A user wants an outcome, not a particular distribution of classes and processes. A software system owns some decisions and persistent effects, delegates others to neighboring services, and depends on actors it cannot directly control. The wrong boundary can turn a local latency, ownership or authorization decision into an unsolvable distributed problem.

The system boundary has two distinct purposes: (1) frame *which user results and correctness invariants* the proposed solution must provide; and (2) establish *which components, interfaces and effects the design team actually controls*. If these disagree, surface the mismatch as a requirement or ownership question. Do not silently make another team's system a component of your proposed service merely because it appears in a dependency diagram.

[arc42 Context and Scope §3](https://docs.arc42.org/section-3/) expressly separates the in-scope system from neighboring users/systems and distinguishes business exchanges from technical channels. The [C4 system context diagram](https://c4model.com/diagrams/system-context) provides a high-level, non-implementation-focused way to show people and directly connected external systems. These published methods guide the diagram, not the facts of our synthetic scenario.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.4318e542ac7e445b9e8b3150effd2cff:9 -->
## Engineering walkthrough — Third-party outage exposes a missing system boundary

**Original fictional walkthrough.** A booking UI accepts a reservation; an external identity provider established a session earlier, a separate payment provider authorizes a deposit, and the authoritative booking database commits the resource allocation. A context diagram that shows only the UI and database incorrectly hides the two external dependencies and their differing trust domains.

| Boundary | Normal contract | Partial failure and who owns the next action |
|---|---|---|
| Browser → booking API | User identity, scoped operation ID and deadline | Client may retry only against the *same* logical intent; server owns durable outcome lookup |
| API → identity provider | Verify identity/token under documented trust policy | If verification cannot be established, reject rather than infer a valid identity from a cached UI label |
| API → payment provider | External authorization result with a separate key | Timeout may mean authorized-but-unacknowledged; payment reconciliation is owned by the payment integration, not the booking database |
| API → booking state authority | Atomically enforce exclusive allocation | A committed booking remains committed even if the response path fails |

The context **excludes** the provider's internal ledger, other tenants' identity stores and unrelated notification systems from the booking application's direct control. It does **not** exclude their failure modes from the user journey. During a payment outage the system can refuse new bookings, or move into an explicitly designed pending-reservation flow—but cannot silently claim all effects committed. A requirement that deposits must precede allocation changes the order; that is a stakeholder decision, not an automatic consequence of drawing more boxes.

**Reversal test (proposed, not run):** sever payment acknowledgments after authorization, then inspect who can query payment and booking results; compare this with identity-provider unavailability. C4/arc42 context descriptions support the *kind* of boundary modeled, not the fictional external services' actual contracts.

<!-- /tycho-question-source -->

## Integrated decision and reading route

Draw the outcome boundary before selecting a component boundary: name the caller, authoritative effect, external decision owner and recovery lookup.

A third-party timeout can leave an external effect committed while the local request is unresolved; moving the dependency outside a diagram does not remove that obligation.

The detailed pages separate the mechanisms that make this decision conditional:

- [Outcomes and system context](outcomes-context.md) — Which user outcome and external actors define the problem boundary?
- [Authority and external dependencies](authority-dependencies.md) — Who owns each state transition and what can an external dependency leave unknown?
- [Unknowns and boundary validation](evidence-contract.md) — Which missing observation prevents a defensible boundary decision?

[Chapter introduction, ordered pages and full source ledger](README.md). Original source labels retain their historical scope; this editorial decomposition does not turn proposed experiments into executed evidence.
