---
metadata_version: 1
id: "tycho.page.ddc98233f12643a287ccd6bd0b92b4d6"
kind: "page"
parent_id: "tycho.chapter.691463ecbf6f44af84274ab3ff798b3d"
canonical_path: "book/volumes/v09-observability-security-and-operations/c06-incident-response-and-operational-change/incident-evidence.md"
title: "Incident chronology and competing explanations"
topic_ids:
  - "observability"
perspectives:
  - "architecture"
  - "operations"
summary: "Which observation separates containment from restored state correctness?"
route_hints:
  questions:
    - "Which observation separates containment from restored state correctness?"
  prerequisites:
    - "tycho.page.62e3dca94bf647b98da7394d98232f88"
  related_ids:
    - "tycho.chapter.691463ecbf6f44af84274ab3ff798b3d"
    - "tycho.page.d87f9ba3852b49ee8188d150bb679716"
    - "tycho.page.1810c1f1f11648bdba66aafa5da60d33"
  excludes:
    - "No independent technical approval, runtime experiment or universal applicability is implied."
  keywords:
    - "incident"
    - "evidence"
evidence_scope:
  source_ids: []
  claim_ids: []
  status: "unknown"
  notes: "Bounded question from tycho.page.d87f9ba3852b49ee8188d150bb679716; exact inherited citation rows and limits remain in the chapter source ledger. New synthetic additions are separately labelled."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-20"
  reviewer: "Codex editorial decomposition"
  proof_uri: null
authored_at: "2026-10-20"
updated_at: "2026-10-21"
source_inspection_date: null
content_verified_at: null
---
# Incident chronology and competing explanations

**Owning question:** Which observation separates containment from restored state correctness?

This page belongs to [V09/C06 — Incident response and operational change](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.

<!-- tycho-question-source:tycho.page.d87f9ba3852b49ee8188d150bb679716:4 -->
## 4. Original fictional incident: search index diverges from stored truth

Consider an invented public index of local hiking trails. The authoritative trail repository is correct, but its asynchronous search index stopped consuming updates after a configuration change. Some searches return outdated trail conditions. A second proposed fix is to delete and rebuild the index while updates continue.

**Detect:** a version-lag alarm and user report show stale search entries; neither yet proves the cause. The response team compares authoritative record version/time with index offset and timestamp for a bounded sample. The impact could include unsafe or unavailable trail information, so a stale result must not be represented as verified current truth.

**Contain:** if current data accuracy is critical, disable stale search for affected partitions or present explicit stale/partial status, while retaining safe authoritative reads. Do not re-enable a broken index solely because the search server responds HTTP 200.

**Investigate:** compare connector offset, source update order, schema version, failed records and deployment/config revision. Competing hypotheses: consumer paused, poison message blocking partition, changed mapping rejecting new field, backend index quota or unrelated request cache. Each requires a different discriminator.

**Recover:** restart only after identifying safe replay position and applying stable record identity; rebuild in a separate index generation with source snapshot/offset semantics, reconcile counts and sampled critical fields, then atomically switch readers under a freshness gate. A live rebuild that permanently misses updates during the scan would not satisfy the invariant.

**Verify:** prove that a known subset of trail edits becomes searchable at an accepted freshness window, no revoked entries are exposed, alerts correctly identify lag, and the ability to revert/forward repair is documented. An index green status is insufficient proof of these user-level checks.

Everything here is a **fictional design and drill plan**, not a performed response. The general need to distinguish authoritative data, derived indexes, failover and freshness is independently described in [Tycho retrieval architecture](../../v06-caching-indexing-and-retrieval/c03-lexical-full-text-indexing-and-ranking/lexical-indexing-bm25-and-sql-fts.md), [CDC/stateful streaming](../../v04-distributed-coordination-and-events/c08-stateful-event-time-stream-processing/stateful-stream-processing-and-cdc.md) and [safe release](../../../delivery/progressive-delivery-and-schema-evolution.md).

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.d87f9ba3852b49ee8188d150bb679716:5 -->
## 5. A usable incident log separates observation from explanation

| Time/event class | What belongs in the log | Why |
|---|---|---|
| Detection | Timestamp, source, scope, first symptom and detection uncertainty | Distinguish occurrence from discovery |
| Observation | Trace/sample/record revision, window, metric definition, access limitations | A graph or quote must be re-verifiable |
| Hypothesis | Candidate cause, contrary evidence, test and owner | Stop guesses from becoming retrospective facts |
| Intervention | Approver, exact version/config/action, expected outcome and rollback plan | Avoid unsafe concurrent changes |
| Result | What actually changed, user journey checks, side effects and failed tests | Green process status is not full recovery |
| Communication | Audience, confirmed impact, unknowns, next update trigger | Prevent false confidence |
| Follow-up | Remaining risks, prevention, owner and evidence for eventual closure | Preserve learning rather than merely writing a report |

Avoid pasting sensitive request bodies, tokens, private user identifiers or raw diagnostic dumps into broad incident communications. Use safe references with controlled access and retention. Incident systems are themselves data products subject to integrity, privacy and access constraints.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.d87f9ba3852b49ee8188d150bb679716:7 -->
## 7. After-action analysis: avoid a single invented root cause

The [SRE Postmortem Culture](https://sre.google/sre-book/postmortem-culture/) emphasizes documenting impact, timeline, contributing conditions and follow-up actions rather than blaming individuals. A correct after-action record may show multiple contributing causes: one bad config, an untested schema interaction, monitoring blind spots and inadequate failover verification.

For the synthetic index scenario, a useful **hypothesis for prevention** is that the ingest consumer should reject an unrecognized mapping before publication; an independent source-to-index freshness invariant might detect lag; a repair procedure needs stable replay positions. These are *possible controls*, not proven fixes. Every action must have a responsible reviewer, reproducible acceptance test and residual-risk statement.

Postmortem publication itself does not ensure issues were remedied; track closure evidence and re-evaluate when source versions, workflow or demand changes.

When an action changes architecture, link it to the decision record owner in
`V10/C04` (`tycho.chapter.809c2f1d12e544b38af2460b80d6d24e`). A prevention
action without a design owner and acceptance test is a wish, not a control.

<!-- /tycho-question-source -->

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](incident-contract.md) |
| Next | [Continue the reasoning](incident-practice.md) |
| Integrated question | [Original scenario and limits](incident-response-and-operational-change.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.
