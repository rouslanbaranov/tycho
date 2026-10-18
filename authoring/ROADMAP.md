# Tycho roadmap

Updated: 2026-10-18.

## Product outcome

Tycho is a self-contained System Design book and a machine-readable knowledge service for external AI agents through MCP. Knowledge infrastructure, effective retrieval, onboarding, the shared Rocinante integration and deployable service delivery are mandatory parts of the product.

The full capability inventory, current-state matrix, dependencies and acceptance gates are in the [knowledge platform and MCP delivery plan](knowledge-platform-and-mcp-plan.md). Its K01–K30 requirements cover the complete reusable authoring, evidence, graph, retrieval and agent-delivery scope. All implementation is independent and uses admitted public evidence only.

## Phases

1. **Foundation — established.** Preserve independence, English artifacts, source controls and repository-wide agent instructions.
2. **Source discovery — first pass complete.** Maintain the public register, coverage and implementation maps, access limitations and research gaps. Discovery is not full reading.
3. **Book structure and bounded pilot contracts — next.** After the completed requirements/workload baseline (#17), propose and review the question-driven book structure (#23), minimal authoring/templates (#24), bounded methodology (#25), and three pilot research contracts (#26). Do not gate them on completing the whole architecture decision layer.
4. **First technical chapters — immediately after minimal contracts.** Research, source-pin and author one mechanism, one end-to-end process and one recovery scenario (#38–#40). Apply available source checks and manual claim/link checks; finish comprehensive validators as a parallel infrastructure task, not as a reason to postpone all writing.
5. **Research tooling and evidence infrastructure — parallel.** Build strict schemas, automatic frontmatter, deterministic routing index, source-revision locks/read-only clones, repository catalogue and structural/link/provenance validators (#27–#37). Fold pilot feedback into these tools.
6. **Evidence-grounded architecture decision layer — after the first meaningful corpus.** Refine applicability cards (#19), legacy/modernization baseline (#18), option comparison and ADRs (#20), target/transition templates (#21), and decision navigation (#22) using actual researched mechanisms and synthetic cases. Requirements model (#17) is implemented; its presence does not complete K30.
7. **Ranked search — required; planned.** Build section-level lexical retrieval, filters, stable citations, progressive reads, graph traversal and evidence resolution. Separate index builds from authoring/deepening.
8. **Semantic/hybrid evaluation — required; planned.** Prototype and benchmark vectors/hybrid ranking against lexical and graph baselines; record the measured production decision and versioning/update requirements.
9. **MCP and generic onboarding — required; planned.** Deliver a read-only remote service, verified client/SDK/transport compatibility, discoverable entry/onboarding and bounded search/read/graph/evidence operations.
10. **Shared Rocinante integration — required; planned.** Supply Tycho's versioned provider instructions and compatibility checks to the existing multi-provider specialist. Test routing, evidence attribution and corpus isolation; do not create a separate Tycho agent.
11. **Snapshots, deployment and operations — required; planned.** Build immutable validated snapshots, independent container/deployment automation, audience/auth policy, safe source resolution, observability, capacity tests and rollback.
12. **End-to-end release evaluation — required; planned.** Expand the corpus question set into representative MCP/agent tasks; measure answer/evidence quality, uncertainty, latency and total agent/tool cost; test compatibility, access boundaries and rollback.
13. **Incremental expansion and maintenance — ongoing after pilots.** Author/deepen in dependency order, update graphs/indexes, track source change impact and re-verification, and rerun regression evaluations.

## Dependencies and boundaries

Define essential semantics for pilot authoring without blocking book content on a complete schema/graph/API. Use validated pilot content to test retrieval. Design MCP/onboarding early; accept the service only after evidence, interoperability and operational checks. Research and authoring can progress without waiting for full hosting infrastructure.

Specific engine, hosting target, vector model and client adapters require evidence-based selection. Those choices do not make MCP delivery, onboarding, graphs or evaluation optional. The book remains locally usable without the hosted service.

Current work records the plan. It does not claim implementation of chapters, schemas, graphs, ranked search, embeddings, MCP, the shared Rocinante integration, hosted infrastructure or benchmarks. Research and implementation continue here; no coding-assistant delegation is configured.
