---
metadata_version: 1
id: "tycho.page.31301a539883499fbf4aa7796271d099"
kind: "page"
parent_id: "tycho.chapter.abc85388b50f470493bef4e204d6f2dc"
canonical_path: "book/volumes/v10/c06/route-validation.md"
title: "Validation of architecture question routes"
topic_ids:
  - "architecture-decisions"
perspectives:
  - "architecture"
  - "migration"
summary: "Which answerable and unanswerable cases test the route's actual contract?"
route_hints:
  questions:
    - "Which answerable and unanswerable cases test the route's actual contract?"
  prerequisites:
    - "tycho.page.c603a8bc4c5a40fd8642b72b6657a557"
  related_ids:
    - "tycho.chapter.abc85388b50f470493bef4e204d6f2dc"
    - "tycho.page.ca056fe720e74a9691ce0c253d9526fc"
  excludes:
    - "No independent technical approval, runtime experiment or universal applicability is implied."
  keywords:
    - "route"
    - "validation"
evidence_scope:
  source_ids: []
  claim_ids: []
  status: "unknown"
  notes: "Bounded question from tycho.page.ca056fe720e74a9691ce0c253d9526fc; exact inherited citation rows and limits remain in the chapter source ledger. New synthetic additions are separately labelled."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-20"
  reviewer: "Codex editorial decomposition"
  proof_uri: null
authored_at: "2026-10-20"
updated_at: "2026-10-20"
source_inspection_date: null
content_verified_at: null
---
# Validation of architecture question routes

**Owning question:** Which answerable and unanswerable cases test the route's actual contract?

This page belongs to [V10/C06 — Search and question routes for architecture agents](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.

<!-- tycho-question-source:tycho.page.ca056fe720e74a9691ce0c253d9526fc:8 -->
## 8. Validation cases for this chapter's reasoning method

Run an independent corpus question evaluation *when such a service exists*. For now, the following cases are **proposed fixtures**, not executed benchmark results:

| Test question | Expected safe route | Failure to detect |
|---|---|---|
| "RPS from 100k users?" | Requirements/workload → queueing → measure offered arrivals | Converting users to RPS with a universal constant |
| "Should we use virtual threads?" | Execution model → downstream capacity → CPU/I/O profile | Claiming threads increase CPU or DB throughput |
| "Is a replica enough for DR?" | Failure classes → data authority → restore and fencing | Equating redundancy with recoverability |
| "Why did p99 jump?" | Tail latency → traces/GC/pools → hypothesis experiment | Selecting cache/queue without root cause |
| "Rewrite the monolith?" | Legacy baseline → patterns → transition gates | Recommending distribution without safe data ownership |
| "Which database for semantic search?" | Lexical vs vector vs hybrid → relevance benchmark | Assuming all similarity scores mean the same thing |

A future evaluation should test source attribution, uncertainty, safe refusals, alternate terms, version/temporal contradictions and **total task cost**, not only whether the correct chapter was returned. Results are unavailable because this page implements a method, not an index or MCP service.

<!-- /tycho-question-source -->

## Original route acceptance matrix

Use paired questions that differ in a material input. One pair asks for a mechanism under a named version and then under an unavailable version. Another changes an ordinary caller into one without permission to inspect the candidate page. A third supplies a measured bottleneck and then removes the observation supporting that diagnosis. The expected route should change when the evidence changes.

For answerable cases, require the route to open the canonical mechanism, preserve its preconditions and cite the exact supporting passage. For unknown-version, denied-scope and missing-observation cases, require a bounded missing-evidence or refusal result. A relevant title alone must not make the case pass. Include a stale but plausible page to test whether the answer preserves snapshot identity.

Record the full reading path and the participating tool calls if this evaluation is later executed. A short final answer can still have an expensive or ungrounded route, so answer length is not the measurement of total work. The matrix is a proposed synthetic evaluation contract; no retrieval runtime or answer-quality benchmark was executed for this page.

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](evidence-safety.md) |
| Next | [Continue the reasoning](README.md) |
| Integrated question | [Original scenario and limits](question-routes-for-architecture-analysis.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.
