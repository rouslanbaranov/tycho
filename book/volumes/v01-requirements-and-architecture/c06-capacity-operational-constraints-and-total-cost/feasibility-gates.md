---
metadata_version: 1
id: "tycho.page.8284605817fc48dba499425b0d908df0"
kind: "page"
parent_id: "tycho.chapter.bbfd14751d274868b152ba431dc904c9"
canonical_path: "book/volumes/v01-requirements-and-architecture/c06-capacity-operational-constraints-and-total-cost/feasibility-gates.md"
title: "Feasibility before preference scoring"
topic_ids:
  - "application-architecture"
perspectives:
  - "architecture"
summary: "Which hard constraint makes a candidate inadmissible regardless of its score?"
route_hints:
  questions:
    - "Which hard constraint makes a candidate inadmissible regardless of its score?"
  prerequisites:
    - "tycho.page.76244dbe2bd44035b7154f821191f6f2"
  related_ids:
    - "tycho.chapter.bbfd14751d274868b152ba431dc904c9"
    - "tycho.page.76244dbe2bd44035b7154f821191f6f2"
    - "tycho.page.b8d02f9b40c44c729e2b99e01a8b0dbf"
  excludes:
    - "No independent technical approval, runtime experiment or universal applicability is implied."
  keywords:
    - "feasibility"
    - "gates"
evidence_scope:
  source_ids: []
  claim_ids: []
  status: "unknown"
  notes: "Bounded question from tycho.page.76244dbe2bd44035b7154f821191f6f2; exact inherited citation rows and limits remain in the chapter source ledger. New synthetic additions are separately labelled."
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
# Feasibility before preference scoring

**Owning question:** Which hard constraint makes a candidate inadmissible regardless of its score?

This page belongs to [V01/C06 — Capacity, operational constraints and total cost](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.

<!-- tycho-question-source:tycho.page.76244dbe2bd44035b7154f821191f6f2:1 -->
## 1. Constraints must be typed and owned

| Constraint type | What a design must make explicit | What unknown blocks |
|---|---|---|
| Runtime/lifecycle | Supported language, framework, operating system and dependency versions | Unsafe unmaintained component or untested runtime upgrade |
| Deployability | Release window, mixed-version overlap, artifact identity, rollback/forward repair | Big-bang changes with unknown old clients |
| Operations | Monitoring, incident response, on-call skill, maintenance cadence | A design with no sustainable operator |
| Capacity/latency | Defined offered load and business correctness/time SLO | Arbitrary replica, database or queue sizing |
| Recovery | Permitted state loss and restoration time for named failure classes | Selecting stateful topology without recovery evidence |
| Privacy/security | Identity, isolation, retention and authorized effects | Unreviewed shared resource or broad account access |
| Financial/effort | Total operating/transition budget, staffing and acceptable migration risk | Cost scoring unsupported by actual cost scope |
| Environment/quota | Allowed infrastructure, networking, keys, capacity and change-control scope | Design depending on unavailable services or privileges |

Not every preference is mandatory. A hard limit must be **explicitly identified by a valid decision authority**; engineers should not invent permissions or declare an arbitrary cloud price ceiling.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.76244dbe2bd44035b7154f821191f6f2:2 -->
## 2. Separate hard feasibility from preference scoring

The process:
1. Define the user-visible outcome and an actual workload/failure envelope.
2. List non-negotiable correctness, security, data and recovery gates.
3. Identify cost, team/skill, support and change-control constraints with owners.
4. Screen simple baseline and proposed alternatives as **PASS**, **FAIL**, or **UNKNOWN** for each gate.
5. Remove failed candidates unless constraints are renegotiated through appropriate authority.
6. For unknown gates, request the exact source or bounded experiment needed.
7. Only then compare preferences such as flexibility, per-unit cost and convenience.

A weighted selection score cannot override a hard authorization violation, unavailable runtime dependency or an unachievable mandatory RPO. If all contenders fail, report **no feasible design under existing constraints**, not a fabricated winner.

<!-- /tycho-question-source -->

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](operational-constraints-and-total-cost-gates.md) |
| Next | [Continue the reasoning](lifecycle-cost.md) |
| Integrated question | [Original scenario and limits](operational-constraints-and-total-cost-gates.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.
