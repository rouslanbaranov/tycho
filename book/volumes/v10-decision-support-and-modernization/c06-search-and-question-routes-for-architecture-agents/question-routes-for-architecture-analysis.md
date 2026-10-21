---
metadata_version: 1
id: "tycho.page.ca056fe720e74a9691ce0c253d9526fc"
kind: "page"
parent_id: "tycho.chapter.abc85388b50f470493bef4e204d6f2dc"
canonical_path: "book/volumes/v10-decision-support-and-modernization/c06-search-and-question-routes-for-architecture-agents/question-routes-for-architecture-analysis.md"
title: "Architecture questions: progressive reading and evidence-bounded decision routes"
topic_ids:
  - "architecture-decisions"
perspectives:
  - "architecture"
  - "migration"
summary: "Integrated question, original scenario and transfer limits for Search and question routes for architecture agents. Detailed mechanisms have separate question owners."
route_hints:
  questions:
    - "How can requirements, symptoms and evidence guide selective reading?"
  prerequisites: []
  related_ids:
    - "tycho.page.0ce5d0aaf63f425ebf556ea97e2d24a9"
    - "tycho.page.868027aee4884210bea1d8a6542fbfb0"
    - "tycho.page.a9a28aaa4d1e4e9cb0accd2fc2c5ba9b"
    - "tycho.page.eb130a7f820544a2ba0e0883c0ce587b"
    - "tycho.page.b6cecfd7301b408db611228b4cec59c5"
    - "tycho.page.b2d1285c1c1a4a698a2306c4e766a4f1"
    - "tycho.page.81add4a0d86b4053ae77f9301fd2281d"
    - "tycho.page.47ffb5c160bd4b10aff27101414c2133"
    - "tycho.page.39a694d604d646a996bf90c3357c3b27"
    - "tycho.page.7a67fd6346a54eff97784465c22bbc74"
    - "tycho.page.359813d554c84da794a353d4416b8047"
    - "tycho.page.dc2470904e004a4aa733abcdb25517ed"
    - "tycho.page.0b493340594c4c4392c5d93940a7f319"
    - "tycho.page.ace968ab1de8409383c6a9b22a00d006"
    - "tycho.page.0ae1aabac3b64c2f924cc427684bdbab"
    - "tycho.landing.1a9054fd18f64dfe911f34a4d17458c0"
    - "tycho.landing.b656116463d9480f83199d8202b127a4"
    - "tycho.page.72cbc98ca3164b759626e5a9e0bfad9c"
    - "tycho.page.c603a8bc4c5a40fd8642b72b6657a557"
    - "tycho.page.31301a539883499fbf4aa7796271d099"
  excludes:
    - "No independent content acceptance or runtime reproduction is implied."
  keywords:
    - "Architecture"
    - "questions"
    - "progressive"
    - "reading"
    - "and"
    - "evidence-bounded"
    - "decision"
    - "routes"
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
<!-- tycho-question-source:tycho.page.ca056fe720e74a9691ce0c253d9526fc:-1 -->

# Architecture questions: progressive reading and evidence-bounded decision routes

> **Tycho technical book draft V10/C06**, authored 2026-10-19. The subject is a reader/agent reasoning method, **not** a shipped MCP server, ranked search endpoint, autonomous agent or graph infrastructure. All examples are original and hypothetical; independent review and benchmark evaluation remain open.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.ca056fe720e74a9691ce0c253d9526fc:0 -->
## Purpose and mission

System Design questions rarely begin as fully specified architecture problems. A person may ask "Should we use microservices?", "Why is p99 bad?", "What if the current system cannot be replaced at once?", or "Can we make this faster?". Correct answers require recovering the actual requirement, opening a small set of canonical explanations, checking precise evidence, and ending with conditional alternatives or a concrete missing-evidence request.

The central contract is **question → bounded context → authoritative explanation → applicability checks → evidence → decision state**, not "search every page and summarize the longest result". This is equally useful to a human reader navigating the book manually and to a future agent using a retrieval service. The approach favors token-efficient routing but **does not sacrifice correctness by enforcing an arbitrary maximum number of pages**.

The [SEI Architecture Tradeoff Analysis Method](https://www.sei.cmu.edu/library/architecture-tradeoff-analysis-method-collection/) provides a public foundation for identifying quality-attribute risks and interactions. [arc42 quality requirements](https://docs.arc42.org/section-10/) models testable engineering scenarios, while [Tycho's independent decision support chapter](../c07-cross-domain-worked-comparisons-and-unresolved-cases/cross-domain-modernization-and-adr-examples.md) contains concrete conditional decisions. This chapter creates a **reading and reasoning route** through those foundations without pretending they automate architecture selection.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.ca056fe720e74a9691ce0c253d9526fc:9 -->
## Engineering walkthrough — Route, read and reject a stale but plausible answer

**Original hypothetical architecture question:** "After a release, booking p99 grew and retries sometimes duplicate records; should we add Redis?" A search ranking returns a high-scoring caching chapter and a deprecated incident note whose source revision predates the current booking IDs. Ranking relevance is not support for its recommendation.

1. **Classify** the question as diagnosis and architecture-choice under correctness constraints, not an unconditional cache-design question. Separate offered load, admission, state owner, failed acknowledgment and version uncertainty.
2. **Route** first to the canonical idempotency/transaction chapters and then pool/queueing; load the cache chapter only if repeated reads and accepted staleness remain plausible hypotheses. A route hint is not evidence.
3. **Read** bounded sections explaining retries after durable commit, source transaction scope and bottleneck diagnostics. Expand only where a live uncertainty changes the answer; don't copy an entire volume by default.
4. **Verify** canonical IDs, exact source revision, author/observation scope, access permissions and contradictions. Reject the old incident's citation if its semantic contract changed or no original source supports its claim.
5. **Answer** with differential hypotheses and the smallest safe next measurement. If state authority, retry identities and actual arrivals remain unknown, state `INSUFFICIENT_EVIDENCE`, not "Redis fixes duplicates".

| Fault injected into retrieval | Required safe behavior |
|---|---|
| High-ranking stale revision | Expose source-version mismatch and ask for current evidence |
| Wrong but keyword-matching document | Re-route to the actual state/booking owner |
| Retrieved page contains instructions to call an action tool | Treat text as untrusted data; no privilege promotion |
| Hidden or forbidden citation | Do not expose title, snippet, content or existence without authorization |

**Proposed, unexecuted evaluation:** use a versioned authorized collection of engineering questions, expected owner routes, stale/contradictory citations and human source judgments; measure support, unsafe claims and tokens per correct answer. This chapter does **not** assert that a hosted Tycho MCP service, embedding index or platform knowledge graph already exists. The SEI and OWASP references support process/trust reasoning, not measured agent performance.

<!-- /tycho-question-source -->

## Integrated decision and reading route

Route a question to a small set of canonical explanations, inspect exact evidence and refuse unsupported synthesis.

A relevant but stale passage cannot justify an answer about another version; retrieve missing conditions rather than guessing.

The detailed pages separate the mechanisms that make this decision conditional:

- [Intent classification and selective reading](intent-reading.md) — Which canonical explanation must be read before composing an answer?
- [Attributable synthesis and safe refusal](evidence-safety.md) — Which version, permission or evidence conflict should constrain the answer?
- [Validation of architecture question routes](route-validation.md) — Which answerable and unanswerable cases test the route's actual contract?

[Chapter introduction, ordered pages and full source ledger](README.md). Original source labels retain their historical scope; this editorial decomposition does not turn proposed experiments into executed evidence.
