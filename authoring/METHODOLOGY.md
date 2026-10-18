# Authoring methodology

## Question before prose

Begin each bounded slice with a research contract: reader, primary question, practical significance, subquestions, exclusions, required evidence, and completion criteria. Apply depth according to consequences of error, coupling, and uncertainty. Word counts and diagram counts are not quality targets.

## Orientation → Architecture → Evidence

Explain purpose and constraints before mechanisms. Each significant concept has one canonical owner; consumers retain enough local context to explain their particular consequences. Landing pages state Purpose and Mission, scope, reading routes, child-page questions, and unresolved work.

For a design, explain assumptions, normal flow, state and data ownership, interfaces, concurrency, consistency, security, performance and cost, deployment, observability, and testing where relevant. Include partial failure, retries, replay, recovery, and invariants with enforcement boundaries. Mark inapplicable aspects through scope rather than empty boilerplate.

## Claims and evidence

Separate published claims, independently reproduced observations, inference, proposals, and unknowns. Record source basis, reasoning, applicability/version, freshness, and review separately. A test proves only the exercised scenario. A paper or official claim is not evidence of a local reproduction. Never imply production verification.

For material claims about correctness, security, consistency, recovery, compatibility, or performance, explain how the exact source supports the claim. Prefer public primary sources; attach section/page anchors or repository revision/path/symbol. State workload and methodology for measurements. Record disagreements and conditions instead of hiding contradictions. Record licensing and avoid copying protected material.

## Original examples

Define synthetic requirements from first principles, with explicit invented workloads and constraints. Do not base synthetic examples on restricted systems. Clearly label illustrative numbers and unmeasured expectations. Compare alternatives and conditions that would reverse the choice.

## Metadata and graph design

Before technical authoring, agree stable IDs, document kinds, parent/related links, source references, verification dates, and a versioned strict JSON Schema. Validate types, enumerations, date syntax, and unexpected properties. Validate referential integrity, parent cycles, paths and anchors separately. Schemas cannot prove truth.

Frontmatter will own document metadata; the routing index will be generated. A later curated directed multigraph will own explicit concept relationships and their evidence. Do not duplicate narrative claims into a mandatory per-sentence database. Introduce claim IDs only where traceability benefits justify maintenance. Graph generation and semantic relationship review are separate tasks. No graph or schema is implemented by this document.

## Feature branches and review workflow

Every implementation/research sub-issue is developed in one dedicated branch from `main`: `feature/TYCHO-<issue-number>-<task-desc-slug>`. The `<issue-number>` is the decimal GitHub issue number, not the epic/subtask code. Generate `<task-desc-slug>` from the sub-issue title **after** the `[E##-##]` prefix: ASCII lowercase alphanumeric words, joined by one hyphen, no leading/trailing hyphens. For example, issue #17 becomes `feature/TYCHO-17-requirements-and-workload-profile`. Reuse an existing matching issue branch instead of creating competing branches; a later corrective commit for the same issue belongs to that branch before merge.

Never commit issue delivery directly to `main`. Keep the branch limited to the bounded issue (including associated process rules explicitly requested during it). Open a PR to `main` labelled by the issue number and reference `Refs #17` rather than silently closing it. Document tests, evidence, unresolved unknowns and review status. Merge and close only after relevant checks and intended approval; keeping the issue open for review is correct. CI validates naming and issue alignment on PR; it does **not** replace repository branch protection or independent review.

## Work cycle

Route through the checkpoint and, once implemented, index. Initially load up to three directly relevant canonical pages; expand when evidence or the question requires. Admit public sources, investigate, write, review, validate, then update source register, research log, and checkpoint. Token savings must preserve correctness, exceptions, and uncertainty.

## Readiness and maintenance

Track research coverage, explanatory sufficiency, evidence support, review, and freshness separately. Draft, mechanically valid, evidence-reviewed, and human-reviewed are distinct conditions. Do not claim human review without a named review event.

A source change flags potential staleness of affected claims, pages, and graph relationships; it does not automatically invalidate them. Keep content verification dates distinct from formatting dates. Record the reviewer role and re-verification evidence required to close the flag.

Before broad authoring, pilot one mechanism, one cross-component scenario, and one recovery scenario. Curate 20–30 evidence-grounded evaluation questions covering facts, synthesis, trade-offs, failure, change impact, contradictions, and unanswerable cases. Compare answer quality, traceability, uncertainty, navigation effort, and total agent cost. Do not fabricate baseline measurements.

## Planned architecture decision support

The [decision-layer plan](architecture-decision-layer-plan.md) defines the next methodology extension: explicit requirements and legacy profiles, evidence-backed applicability and contraindications, comparison with alternatives, testable ADRs, and separate target/transition architecture. Integrate these conventions after model design and pilot evaluation. Recording the plan does not establish implemented decision support or authorize a broad rewrite.

## Required machine-readable delivery

The [knowledge-platform plan](knowledge-platform-and-mcp-plan.md) is the complete capability and release checklist. Authoring must support stable IDs/sections, generated metadata/indexes, exact provenance, independently reviewed graphs and Route → Read → Verify. Ranked retrieval, vector/hybrid evaluation, MCP onboarding, shared Rocinante integration guidance and snapshot/deployment evaluation are required workstreams. Keep authoring/deepening, source updates, indexing and serving separate; none silently triggers a whole-book rewrite. Record actual implementation and acceptance evidence against the capability matrix.
