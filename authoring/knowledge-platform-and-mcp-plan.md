# Knowledge platform and MCP delivery plan

> **Capability-state correction:** K01–K30 remain requirements, but the 2026-10-19 status rows are a historical planning matrix, **not a current audited implementation ledger**. Strict JSON Schema, frontmatter metadata, stable identity registry, source controls, validators and an offline complete 136-doc routing index already exist; the finished physical 10-volume edition, hosted lexical/hybrid retrieval, MCP and deployment do not. Book completion #213 then release #214 take priority. Curated graph infrastructure remains excluded. **Live state (2026-10-20, before merging PR #218):** M1–M9 integrated draft merged via PR #216; PR #217 closed/unmerged and replaced by open/non-draft **unmerged PR #218**. M9 #121 closed under scoped owner acceptance; #213/E14 and final edition #214 remain open. **69/69 primary chapter manuscripts deepened, 0/69 independently accepted for final-book completeness.** The 10-volume edition, hosted MCP and deployment do not exist. Reported 13/13 groups and 215/215 tests passed on prior manuscript SHA `d8d04e0e3c97e9f364607f640faa9f5aee4866f3`, **not** on the subsequently edited status documents. Visual rendering and live MCP were owner-cancelled, not PASSED. See [canonical current state](STATE.md) and [reconciliation](PROJECT_STATUS_RECONCILIATION_2026-10-20.md).


Status: scope revised 2026-10-19. Prior plan dated 2026-10-18.

## Product commitment and independence

Tycho is both a self-contained System Design book and a machine-readable knowledge source for external AI agents through MCP. Agent retrieval, onboarding, provenance, ranked search, evaluation and deployable service delivery are required product capabilities. A separately curated concept/decision knowledge graph is **explicitly excluded** from Tycho's product scope unless its incremental value is demonstrated in a future separately approved experiment.

Implement the full reusable book-building and knowledge-delivery capability set independently. Do not import another corpus, private code, examples, identifiers, repository catalogues, deployment configuration or runtime dependencies. General methods are expressed here as independent product requirements. The book must remain understandable and locally navigable without the hosted service.

Research and authoring take place in the ChatGPT project. The repository stores the book, specifications and independently implemented tooling. Integration with the shared Rocinante specialist is a product deliverable, not delegation of Tycho development.

## Capability inventory and acceptance matrix

Status describes Tycho now. A written plan is not an implementation. Each planned capability must receive an implementation location, owner, acceptance evidence and status update when built.

| ID | Required capability | Current state | Required completion evidence |
|---|---|---|---|
| K01 | Book hierarchy: book, volume, chapter, optional section and bounded page | Partial: root entry only | Coherent navigation, stable owners, local reading routes and applicable page-size checks. |
| K02 | Purpose and Mission on landing pages | Partial: book root only | Every relevant landing page explains purpose, scope, children, outcomes and open work. |
| K03 | Canonical explanations and progressive depth | Method documented; corpus pending | Orientation → Architecture → Evidence; local context without duplicate canonical narratives. |
| K04 | Research contracts, source register, research log and checkpoint | Partial: discovery-stage artifacts exist | Per-slice questions, source-reading scope, contradictions, next action and honest completion states. |
| K05 | Controlled authoring and deepening workflows | Planned | Repeatable bounded research/deepening/review/checkpoint process; no implicit whole-book regeneration. |
| K06 | Risk-based depth, invariants and normal/failure/recovery scenarios | Method documented; corpus pending | Material mechanisms explain guarantees, failure, exceptions and evidence limits. |
| K07 | Claim-to-evidence provenance | Partial: source-level discovery register | Exact document sections or revision/path/symbol references and reasoning for critical claims. |
| K08 | Reproducible public source-code snapshots | Planned | Lock manifest, revision-pinned detached read-only clones, submodule policy, mismatch detection and generated repository catalogue. |
| K09 | Source content/version/access/licensing controls | Partial: discovery metadata | Admitted scope, hashes/revisions where permitted, missing/paid source behavior and bounded reproducible retrieval. |
| K10 | Automatically generated YAML frontmatter | Planned | Stable IDs, kinds, hierarchy, topics, perspectives, summary, routing hints, evidence scope, verification dates and typed relationships. |
| K11 | Strict JSON Schema | Planned | Versioned schemas for metadata, source records, search/snapshot manifests and API payloads; positive/negative validation. No curated-graph schema is required. |
| K12 | Deterministic routing index | Planned | Generated from canonical metadata; stable order, ID/path uniqueness, hierarchy/related links and saved-index freshness. |
| K13 | Unified deterministic validation | Partial: source checks and CI exist | Metadata, hierarchy cycles, references, paths/anchors, fences, navigation completeness, size/snippet limits and **search-index/source consistency**. Missing graph tooling is not a validation failure. |
| K14 | Optional public-code static extraction experiment | Experimental / **not a delivery gate** | If pursued, pin selected public code revisions, report parser/tool scope and provenance; do not couple this experiment to required Tycho search/MCP/release paths. |
| K15 | Curated concept/decision graph | **Removed from Tycho scope** | No manual concept/pattern/decision edges, shard curation, graph lookup or graph maintenance are required; use existing metadata, applicability cards, ADRs and source-to-claim provenance instead. |
| K16 | Graph shards and graph assembly | **Removed from Tycho scope** | No curated-graph schema, shards, aggregate generation or traversal release gate; existing experimental graph contract artifacts are historical and not authoritative product dependencies. |
| K17 | Route → Read → Verify workflow | Method documented; service pending | Bounded relevant reads, explicit expansion, exact evidence resolution and visible unknowns. |
| K18 | Ranked lexical retrieval | Planned; required | Full-text section index, metadata filters, stable snippets/citations, ranking and tested handling of aliases and terminology. |
| K19 | Semantic/vector and hybrid retrieval | Planned evaluation and prototype | Versioned chunk/embedding/index contracts, reproducible comparison and documented deployment decision; never silently omitted from the plan. |
| K20 | Reusable retrieval service | Planned; required | Search/read/evidence and architecture-decision guidance independent of MCP transport, with bounded outputs and snapshot consistency. |
| K21 | Remote read-only MCP service | Planned; required | Verified transport/SDK/client compatibility, schema-described capabilities, safe limits, citations and interoperability tests. |
| K22 | Generic-agent onboarding | Planned; required | Versioned entry capability describing collection, structure, query strategy, evidence, limits, versions and supported operations. |
| K23 | Integration with the shared Rocinante specialist | Planned; required | Versioned provider instructions, lightweight compatibility checks, collection-scoped retrieval and attributable evidence-backed outputs; no separate Tycho specialist. |
| K24 | Immutable knowledge snapshots | Planned; required | Manifest of book, metadata, provenance and approved retrieval indexes; integrity checks, atomic activation, version compatibility and rollback. |
| K25 | Reproducible service deployment | Planned; required | Independent container build and deployment automation, environment configuration, smoke tests, readiness and rollback runbook. |
| K26 | Safe access and source resolution | Planned; required | Explicit audience/auth policy, read-only boundaries, safe ID/path resolution, no arbitrary execution/fetching and no prohibited-source access. |
| K27 | Service observability and capacity | Planned; required | Latency/error/resource metrics, privacy-conscious audit events, limits, alerting and representative multi-client load tests. |
| K28 | Corpus/retrieval/agent evaluation | Planned; required | Evidence-grounded questions, quality/uncertainty/citation/coverage checks and total task cost comparison. |
| K29 | Maintenance, freshness and change impact | Partial: method only | Source → claim/page/section-index impact, potentially-stale states, review responsibility and verified closure without date inflation. |
| K30 | Architecture selection and modernization | Planned | Requirements/legacy profiles, applicability cards, alternatives, ADRs, target/transition states and evidence-insufficient outcomes. |

## Authoritative artifacts and source controls

Book prose and page metadata own explanations and document identity. The public source register and a separate code-revision lock own admitted research references. Indexes, search chunks, onboarding variants and release manifests are generated or validated against declared canonical owners.

Do not mirror paid books or documentation without permission. Store only admitted public material with its access/reuse constraints. Where a source cannot be distributed, the book provides its own essential explanation and precise references; evidence tools report the access limitation instead of pretending source text is available.

Read-only code tooling must prevent accidental edits/pushes, report revision mismatches and validate required submodule revisions. Updating sources is a deliberate operation with impact review; indexing must never reset clones or refresh evidence silently.

## Knowledge model, provenance and quality

Adapt document kinds to a general System Design reference: concepts, patterns, comparisons, applicability, implementations, procedures, examples, evidence and historical research. Do not encode production/current-system classifications that imply a real private architecture.

Use stable IDs independent of numbering and paths. Agree semantics before implementing schemas. Keep observed source evidence, inference, proposals, historical material, unresolved contradictions and unknowns distinguishable. Source reading, explanatory depth, semantic review and freshness are independent dimensions.

**Scope decision, 2026-10-19:** Tycho does **not** build or maintain a curated concept/decision graph. Requirements, patterns, contraindications, trade-offs, sources and decisions remain discoverable through canonical pages, metadata, typed claim provenance, ADRs and ranked section search. Cross-topic reasoning is performed using retrieved, verifiable information rather than maintained duplicate graph edges.

A static code relationship extractor can be useful for independently permitted source-code examples, but it is **optional research**, not a prerequisite for Tycho's retrieval, MCP release, snapshot assembly, change-impact pipeline or acceptance. Keep educational coverage of graph databases/traversal as System Design topics; that content is not a product graph implementation. Existing graph-contract prototypes (#42) are retained as historical artifacts and do not imply an accepted runtime feature.

## Retrieval contract and efficiency

Route using compact metadata; read relevant sections; verify critical claims from exact evidence. Start with up to three relevant canonical pages and expand as needed for correctness. This is an initial routing heuristic, not a limit that suppresses needed evidence.

Required retrieval functions include:

- Lexical ranking over sections and routing metadata.
- Filters for topics, document kind, evidence/review/freshness, implementation/version, workload condition and decision constraints where supported by the agreed model.
- Stable page/section IDs and snapshot-bound citations.
- Short ranked summaries followed by selective section/page reads.
- Provenance lookup and explicit source-access limitations.
- Contradictions, incomplete coverage, stale findings and insufficient-evidence outcomes.
- Budgets, pagination/cursors, truncation indicators and continuation routes; avoid returning the whole corpus.
- Stable snapshot handling across multi-call research, with explicit mismatch behavior.

Implement a lexical baseline and benchmark it. Compare embedded FTS/BM25 approaches with Lucene/Tantivy or service-based engines against corpus size, multilingual/technical-term needs, concurrency, maintenance effort and measured quality. No particular engine is selected by this plan.

Perform a bounded vector/hybrid prototype and evaluation with versioned chunking, embedding model/dimensions, incremental reindexing, filters and fusion/reranking. Production inclusion depends on demonstrated benefit; a documented rejection must preserve required search quality and explain the evidence. The evaluation itself remains required.

Keep corpus generation/deepening, source refresh, indexing and serving as separate operations. Index rebuilds must not trigger research or rewrite book content.

## MCP and onboarding contracts

Design a shared retrieval core and a thin MCP adapter. Verify the protocol version, supported SDK and clients at implementation time. Do not present conceptual names below as existing tools or standardized MCP methods.

| Conceptual operation | Expected output and bounds |
|---|---|
| Capabilities/status | Service/API/schema versions, collection and snapshot IDs, supported operations and limitations. |
| Onboarding/entry | Summary/full/topic guidance, knowledge model, retrieval sequence, evidence policy, limits and compatibility. |
| Search | Ranked IDs, short excerpts, metadata, match context, citations, pagination and snapshot identifier. |
| Read | Specific section/page content, navigation, evidence status, citation anchors and explicit truncation. |
| Evidence lookup | Public source identity, exact version/section/revision, support limits and permitted excerpts only. |
| Decision-method lookup | Relevant requirements/applicability/modernization guidance and missing-input questions; no unsupported automatic architecture verdict. |

Plan one remote MCP transport entry point, for example /mcp, using a supported transport such as Streamable HTTP after compatibility verification. Onboarding must be discoverable through supported MCP instructions/resources and an explicit described operation where needed. A conventional HTTP /onboarding document may supplement this but is not a replacement for MCP discovery or a standard MCP method.

No assumption that every client automatically loads server instructions, resources or prompts is allowed. Test chosen clients and document explicit/manual fallback. Generic clients must be able to discover how to use Tycho efficiently.

## Shared Rocinante specialist integration

There is one external specialist agent: **Rocinante**. It can work with multiple independent knowledge providers, including Tycho. Do not create a separate Tycho expert agent or duplicate the shared specialist's runtime, identity or general operating instructions.

The shared specialist and its common multi-provider routing/instruction package are owned at the platform integration level, outside this book's corpus. Their repository location and deployment are not assumed here. Tycho owns its provider contract: collection identity, versioned onboarding, capabilities, knowledge schema, source/evidence policy, retrieval behavior and compatibility fixtures.

Provide a compact, versioned Tycho instruction module that can be included in Rocinante's existing shared package. Generate the relevant provider guidance from Tycho's authoritative onboarding source rather than maintaining contradictory copies. Rocinante carries general operating guidance and checks provider capabilities, authorization and snapshot/schema compatibility cheaply instead of downloading full onboarding every session. Detailed architecture facts remain dynamic in the appropriate provider.

Route general System Design, pattern applicability and modernization-method questions to Tycho. The shared specialist may combine independently retrieved evidence with other authorized providers at the client/orchestration layer. Keep findings, citations, collection IDs and snapshot IDs attributable to their original provider; distinguish observed facts from general patterns, inferences and proposals. Failure or denial at one provider must not be silently filled with invented facts from another.

Tycho must operate, build, validate, index, release and serve without any other corpus. It must not ingest, persist, embed, index, cache, log or write back another provider's private content. Cross-provider reasoning does not create a shared source register or evidence graph inside Tycho. Test provider routing and isolation using public or synthetic fixtures, never by importing a private corpus.

Generic MCP clients retain standalone access through Tycho onboarding. Rocinante is an optimized shared consumer, not a prerequisite for understanding the book or using its MCP service. Integration tests cover provider identity, missing/incompatible capabilities, unavailable evidence, correct attribution, isolation and response quality.

The shared response contract covers findings, alternatives, constraints, evidence pointers, applicability, risks, inferences, unknowns, contradictions and next evidence needed. Tycho's MCP service remains read-only retrieval; an always-on hosted LLM is not a baseline dependency.

## Snapshots, deployment, access and operations

Build an immutable validated snapshot from permitted book/evidence assets, metadata, and supported retrieval indexes. Include manifest hashes, source revisions, schema/tool versions and compatibility information. Serving activates one complete snapshot atomically and can roll back without rebuilding the book.

Plan independent container images and deployment automation. Assess an Ansible-based deployment recipe as a supported initial path; do not assume any existing external playbooks, hostnames, credentials, registry or infrastructure are available. Select the actual deployment target later from requirements.

Include health/readiness, configuration/secrets boundaries, TLS, an explicit public/authenticated audience decision, authorization hooks if required, rate limits, request/output limits, timeouts and resource budgets. A private Git repository is not authorization to expose its contents through a public service.

Evidence resolution uses admitted IDs and bounded revision-aware paths, never arbitrary caller-provided filesystem paths or outbound URLs. Treat returned documents as untrusted evidence, not executable instructions. Address prompt injection, traversal, unsafe URL fetching and oversized queries. Cross-collection integration must not become a dependency or access route to private corpora.

Metrics and audit events should describe service behavior without logging confidential query content or credentials. Plan p95 latency/error monitoring, resource usage, snapshot freshness, indexing failures, alerts, capacity estimates and representative concurrent-agent tests.

## Evaluation and completion gates

Start with 20–30 evidence-grounded corpus questions, then expand toward 50–100 representative service/agent tasks as coverage grows. Include direct facts, cross-topic reasoning through cited pages, change impact, workload trade-offs, modernization, contradictions, stale evidence and truly unanswerable questions.

Compare local file/index retrieval, MCP lexical retrieval with provenance verification, vector/hybrid prototype, and external use through the shared Rocinante specialist. Measure correctness, exact evidence precision, relevant-context coverage, false confidence, missing-evidence handling, retrieval latency, end-to-end latency, calls and total input/output tokens across all participating agents/tools. Report measured costs rather than assuming delegation saves tokens.

Test reproducible rebuilds, schema/link/section-index failures, snapshot mismatch, compatibility, source-access restrictions, read-only behavior, overload and rollback. Set concrete release thresholds from pilot/baseline observations; do not invent performance numbers in the plan.

Product completion requires validated corpus structure and evidence, working ranked retrieval, working provenance/evidence resolution, generic onboarding, an interoperable remote MCP release, a compatible shared Rocinante integration, reproducible snapshots/deployment, operational checks and measured evaluation. A catalogue, design document, local prototype or running endpoint alone is insufficient.

## Work sequencing

1. Define decision profiles, knowledge semantics, MCP/retrieval requirements and authoritative ownership together.
2. Finalize question-driven book structure and pilot contracts.
3. Build metadata/schema/index/provenance/source-lock validation without new graph contracts.
4. Research and deepen the pilots; populate a small corpus with real evidence and semantic review.
5. Deliver reliable metadata-to-section indexing, traceable provenance and decision-method navigation against the pilot corpus; consider source-code extraction only in independent experiments.
6. Build ranked lexical retrieval and exact provenance/evidence resolution; establish a measured baseline.
7. Implement and evaluate the vector/hybrid prototype and record the production decision.
8. Implement MCP adapter, discovery/onboarding and client interoperability.
9. Integrate Tycho's provider guidance with the existing shared Rocinante specialist and test compatibility, routing, attribution and isolation.
10. Build immutable snapshots, independent deployment automation, access controls and observability.
11. Perform end-to-end quality, concurrency, safety and rollback evaluation; release the service and verified shared-agent integration.
12. Expand the book and indexes incrementally with change-impact/freshness maintenance and regression evaluation.

API/onboarding design starts early; final service acceptance depends on a validated corpus and tested retrieval. Book research can continue in bounded slices without waiting for full hosting infrastructure. All capabilities remain traceable through K01–K30; any proposed change in scope must be recorded explicitly rather than silently deferred.

This task records the revised plan only. It does not implement search, schemas, MCP, an agent runtime, source cloning or deployment.

## Real-world decision evidence extension (proposed M9 / E16; 2026-10-19)

[Real-World Case Study Program](REAL_WORLD_CASE_STUDY_PROGRAM.md) adds independent publicly sourced and version-bound case studies to K03/K06/K07/K30. The [primary source register](../sources/REAL_WORLD_ARCHITECTURE_CASES.md) and [Netflix dossier](../sources/NETFLIX_MODERNIZATION_DOSSIER.md) are discovery inputs, not implementation proof. Accepted case pages must preserve before/after architecture, workload constraints, failed/abandoned alternatives, migration safety, author-reported versus measured outcomes, later changes and when not to generalize. Case IDs/provenance will be integrated through K10–K16 and selective case retrieval through K17–K23 *only after* stable shared contracts exist; this is not a new MCP/graph/search implementation. E14 corpus authoring and full-book deepening continue independently. New M9 is a proposed milestone and must be created in GitHub before issue milestone assignment; no false release/CI completion claims.
