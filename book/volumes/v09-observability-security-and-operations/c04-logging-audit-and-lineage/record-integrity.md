---
metadata_version: 1
id: "tycho.page.e50b14deb6de4204b9f405942ab0cee8"
kind: "page"
parent_id: "tycho.chapter.49cb8db3af4e406ea6988c8e5e852acf"
canonical_path: "book/volumes/v09-observability-security-and-operations/c04-logging-audit-and-lineage/record-integrity.md"
title: "Retention, integrity and contradictory records"
topic_ids:
  - "observability"
perspectives:
  - "architecture"
  - "operations"
summary: "Which record must survive a failure before an authorized effect can be asserted?"
route_hints:
  questions:
    - "Which record must survive a failure before an authorized effect can be asserted?"
  prerequisites:
    - "tycho.page.adde87c9a3a14c508ebd5ddb8fa676a1"
  related_ids:
    - "tycho.chapter.49cb8db3af4e406ea6988c8e5e852acf"
    - "tycho.page.436c2b22dc9e47acaaca7d18fadb511c"
  excludes:
    - "No independent technical approval, runtime experiment or universal applicability is implied."
  keywords:
    - "record"
    - "integrity"
evidence_scope:
  source_ids: []
  claim_ids: []
  status: "unknown"
  notes: "Bounded question from tycho.page.436c2b22dc9e47acaaca7d18fadb511c; exact inherited citation rows and limits remain in the chapter source ledger. New synthetic additions are separately labelled."
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
# Retention, integrity and contradictory records

**Owning question:** Which record must survive a failure before an authorized effect can be asserted?

This page belongs to [V09/C04 — Logging, audit and lineage](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.

<!-- tycho-question-source:tycho.page.436c2b22dc9e47acaaca7d18fadb511c:4 -->
## 4. Security, retention and integrity boundaries

Storing logs and audit records can create security and privacy risks:
- Raw HTTP bodies, access tokens, emails or other sensitive fields may be too broad for operational log sinks.
- A shared audit service must enforce subject/object/tenant permissions and safe access histories.
- Tamper evidence and complete event capture require independent engineering controls; encrypting at rest alone does not prove integrity.
- Retention must balance actual business/legal requirements against minimization, deletion and incident needs. A backup archive or search index can retain data after a primary record is removed.
- A log with a malicious embedded instruction or fabricated identity should be treated as untrusted content, not as a privileged command to downstream agents.

Log redaction at a central collector may occur **after** sensitive bytes have already traversed insecure intermediate paths. Prefer limiting exposure at emission and verifying the whole ingestion chain.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.436c2b22dc9e47acaaca7d18fadb511c:5 -->
## 5. Failure chronology and negative evidence

**Fictional failure:** the application emits "booking accepted", then its database transaction fails; the log sink persists the line. Another request commits a booking while the log collector is down. The operations team cannot reconstruct authoritative acceptance from logs alone.

A designed response:
1. Query authoritative effect identities and committed revisions under authorized access.
2. Reconcile telemetry and trace observations against those records rather than redefining truth.
3. Identify dropped/duplicated log windows and missing dataset/lineage events.
4. Rebuild derived views from a versioned state source if their replay contract allows it.
5. Report uncertain results as uncertain, and preserve the investigation's access/retention policy.

Do not claim an audit is durable without a tested commit boundary and safe identity/corruption model.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.436c2b22dc9e47acaaca7d18fadb511c:6 -->
## 6. A source-led acceptance test

Proposed fixture only:
- Force a rollback after an operational "requested" log and ensure authoritative audit says no accepted effect.
- Commit a booking during log export failure and ensure audit remains complete under its own contract.
- Retry a committed logical operation and verify effect identity rather than duplicating state/audit.
- Run a transformation with two inputs and two outputs but only a subset of true data-flow edges; verify lineage does not invent false edges.
- Revoke a user's access and check both audit querying and derived indexes respect authorization.
- Exercise retention expiry and restore; verify no surprising recreated unauthorized data paths.

**No test ran** for any of these cases.

<!-- /tycho-question-source -->

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](record-semantics.md) |
| Next | [Continue the reasoning](README.md) |
| Integrated question | [Original scenario and limits](logs-audit-and-data-lineage.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.
