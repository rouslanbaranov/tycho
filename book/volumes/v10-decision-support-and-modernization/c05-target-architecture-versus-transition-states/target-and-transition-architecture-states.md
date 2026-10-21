---
metadata_version: 1
id: "tycho.page.cf0ce38c73e44950aec5a9c2869bee63"
kind: "page"
parent_id: "tycho.chapter.0a5e430b39094337aa6a211d9b5b4bd0"
canonical_path: "book/volumes/v10-decision-support-and-modernization/c05-target-architecture-versus-transition-states/target-and-transition-architecture-states.md"
title: "Target architecture versus transition states: coexistence, reversibility and recovery"
topic_ids:
  - "architecture-decisions"
perspectives:
  - "architecture"
  - "migration"
summary: "Integrated question, original scenario and transfer limits for Target architecture versus transition states. Detailed mechanisms have separate question owners."
route_hints:
  questions:
    - "What is safe during coexistence, migration, rollback and recovery?"
  prerequisites: []
  related_ids:
    - "tycho.page.81efb7e6d72349768b6f202845cbe35e"
    - "tycho.page.31c8e450f78c451d90cb6090df330c5a"
    - "tycho.landing.b656116463d9480f83199d8202b127a4"
    - "tycho.page.b2d1285c1c1a4a698a2306c4e766a4f1"
    - "tycho.page.cccbd188936543a2aaf904f4002236d8"
    - "tycho.page.4681b3ba9e234c46bdb4b5993634b0e3"
    - "tycho.page.f05854fcc406435bbf38a192bc7ab2f1"
    - "tycho.page.1e89567050974052b13ba62b3b44484f"
    - "tycho.page.ca056fe720e74a9691ce0c253d9526fc"
    - "tycho.page.78d0f89ac4184b19bfef3a72e8b4f2cc"
    - "tycho.page.47b67ebf3dbf477e818e83f9e1683ffe"
    - "tycho.page.ea1c3ca31f974bcbb6a432c55e56bc03"
  excludes:
    - "No independent content acceptance or runtime reproduction is implied."
  keywords:
    - "Target"
    - "architecture"
    - "versus"
    - "transition"
    - "states"
    - "coexistence"
    - "reversibility"
    - "and"
    - "recovery"
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
<!-- tycho-question-source:tycho.page.cf0ce38c73e44950aec5a9c2869bee63:-1 -->

# Target architecture versus transition states: coexistence, reversibility and recovery

> **Independent Tycho manuscript draft V10/C05, 2026-10-19.** Original fictional case and decision tables. This chapter applies, but does not replace or copy, the reusable [target/transition authoring model](../../../../authoring/models/target-transition-architecture.md). No real migration, data movement, approval or restore drill occurred.

<!-- /tycho-question-source -->

> **Pattern atlas:**
> [Strangler Fig](../../v11-pattern-atlas/c10-deployment-modernization/README.md#strangler-fig) — decision conditions and contraindications.

<!-- tycho-question-source:tycho.page.cf0ce38c73e44950aec5a9c2869bee63:0 -->
## Purpose and mission

A target architecture describes what a system should *eventually be*. It cannot explain how existing clients, stored data, deployments and external effects survive the change. The **transition architecture** is a sequence of real operating configurations in which old and new software may coexist, data ownership is transferred or deliberately retained, and some steps cannot simply be rolled back.

The fundamental reader question is: **What may happen between the old and target designs without violating an invariant?** An attractive future-state diagram has no answer unless it specifies compatibility, authority, evidence and recovery at intermediate steps.

[Fowler's 2024 Strangler Fig explanation](https://martinfowler.com/bliki/StranglerFigApplication.html) motivates gradual replacement rather than assuming a wholesale rewrite is well understood. [Microsoft's Strangler Fig guidance](https://learn.microsoft.com/en-us/azure/architecture/patterns/strangler-fig) describes façade-based incremental routing, coexistence cost and conditions where the pattern is unsuitable. Neither guarantees a safe migration for a particular data model.

**Strangler mechanism.** Intercept requests at a façade or route and send one capability at
a time to the new implementation while the old path remains available. The façade is a
temporary routing and compatibility layer, not a permanent second architecture.

**Invariant and failure.** Keep one authoritative writer for each invariant and define
routing plus data compatibility during coexistence. Interception may be impossible,
internal callers may bypass the façade, and old/new state can diverge. Detect bypass and
divergence, hold the cutover, and route back to the compatible path until the new capability
is proven. Branch by abstraction, parallel run or a big-bang replacement may be preferable
when interception is impossible or the system is small enough to replace whole.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.cf0ce38c73e44950aec5a9c2869bee63:10 -->
## Engineering walkthrough — New-only persisted effects turn image rollback into forward repair

**Original fictional migration:** a catalogue has one legacy identity field and an external API that still serves old clients. The target separates models from physical units. An engineer plans to introduce new binaries and treat container image rollback as the recovery strategy even after clients start writing new-only identity states.

| Transition | Authority and compatibility | Reversible response |
|---|---|---|
| S0 baseline | Old writer, old schema/decoder, recorded snapshot and operation horizon | Restore pinned baseline under actual data policy |
| S1 expand | Old writer authoritative; new decoder reads old representation | Disable new reads without changing durable business meaning |
| S2 shadow | New model is a projection with versioned mappings/checkpoints | Rebuild projection; old writer still accepts mutations |
| S3 fenced cutover | Exactly one authorized writer, mixed-version readers covered by tests | Return to old compatible reads only before new-only effects |
| S4 new-only writes | New persisted state old binary cannot understand | **No automatic image-only rollback**; stop further incompatible writes and forward-repair or restore with approved loss/reconciliation |
| S5 retire | Proved no required legacy replay/consumer remains | Explicit irreversible approval; retain audit/restore records |

**Failure:** one S4 write reaches durable storage, then a canary alarm fires. Rolling pods back to the S0 image makes some records unreadable. Even a previously successful shadow row-count comparison does not prove old-client semantic compatibility or reversibility. An idempotent replay also needs stable logical intent identity and a single authoritative operation/result record.

**Decision:** delay the no-return stage until every necessary old reader is removed or a verified compatible forward path exists. The Strangler Fig sources describe incremental replacement, not a proof that each phase supports rollback. This chronology is a proposed synthetic contract; no cutover, recovery or code-path compatibility test was executed.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.cf0ce38c73e44950aec5a9c2869bee63:11 -->
## Applied M9 evidence: what transfers and what does not

These examples connect the chapter's conditional mechanism to published experiences or synthetic decision exercises. A historical company report is **first-party, time-scoped evidence**, not a controlled Tycho benchmark; an M9 decision playbook is **original synthetic analysis**, not a company decision.

**Case lens — [Shopify — Helix migration gates](../../../cases/shopify-helix-checkpoint-gated-native-migration.md)**. **Relevant mechanism or architectural contrast:** Small migration checkpoints with behavior and human-review gates reduce unbounded AI-change scope. **Not established by this report/playbook:** An opt-in autonomous mode and company report are not evidence of zero escaped defects or safe unsupervised database migration.

**Case lens — [Spotify — Long-tail platform migration](../../../cases/spotify-tech-migration-long-tail.md)**. **Relevant mechanism or architectural contrast:** Fleet modernization fails without ownership, adoption telemetry and managing the long tail. **Not established by this report/playbook:** A governance report does not prove one automation tactic guarantees 100% fleet adoption or any technical runtime improvement.

**Case lens — [Data migration correctness](../../../cases/decisions/data-migration-correctness.md)**. **Relevant mechanism or architectural contrast:** Synthetic ADR contrasts transactional cutover, shadow-equality and client-version migration contracts. **Not established by this report/playbook:** Stripe, Netflix and Meta operated different data authorities; no shared company-endorsed proof or universal checksum.

**Case lens — [Build and delivery migration](../../../cases/decisions/build-delivery-migration.md)**. **Relevant mechanism or architectural contrast:** Synthetic ADR separates build reproducibility from adoption governance using Airbnb and Spotify. **Not established by this report/playbook:** Historical publisher outcomes do not establish the invented organization's savings or a single canonical CI tool.

**Transfer test:** before applying the lesson to another legacy system, identify the exact workload, source date, relevant runtime/protocol versions, state authority, failure/recovery gate and the new observation that would reverse the choice. Follow the case's public evidence ledger rather than treating its link as independent proof.
<!-- /tycho-question-source -->

## Integrated decision and reading route

Plan coexistence, authority transfer, no-return conditions and recovery as real intermediate operating states.

Rolling back an image cannot undo new-only durable effects; transition safety requires a separate forward-repair path.

The detailed pages separate the mechanisms that make this decision conditional:

- [State authority and coexistence transitions](authority-states.md) — Which owner is authoritative in every real intermediate configuration?
- [Rollback limits and semantic reconciliation](rollback-data.md) — Which durable differences survive reverting the deployed binary?
- [Migration mechanisms and no-return gates](cutover-gates.md) — What evidence permits a transition to cross an irreversible boundary?

[Chapter introduction, ordered pages and full source ledger](README.md). Original source labels retain their historical scope; this editorial decomposition does not turn proposed experiments into executed evidence.
