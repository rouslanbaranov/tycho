---
metadata_version: 1
id: "tycho.page.436c2b22dc9e47acaaca7d18fadb511c"
kind: "page"
parent_id: "tycho.chapter.49cb8db3af4e406ea6988c8e5e852acf"
canonical_path: "book/volumes/v09-observability-security-and-operations/c04-logging-audit-and-lineage/logs-audit-and-data-lineage.md"
title: "Structured logging, authoritative audit and data lineage"
topic_ids:
  - "observability"
perspectives:
  - "architecture"
  - "operations"
summary: "Integrated question, original scenario and transfer limits for Logging, audit and lineage. Detailed mechanisms have separate question owners."
route_hints:
  questions:
    - "How do security audit, event lineage and operational logs differ?"
  prerequisites: []
  related_ids:
    - "tycho.page.f921597aae854c6996459fc025a9bca3"
    - "tycho.page.6b9a3f5c7bae455ab4f56f151f17b406"
    - "tycho.landing.1a9054fd18f64dfe911f34a4d17458c0"
    - "tycho.landing.b7ea8fb13ebb4079af2333e475f97106"
    - "tycho.page.0ae1aabac3b64c2f924cc427684bdbab"
    - "tycho.page.ace968ab1de8409383c6a9b22a00d006"
    - "tycho.page.adde87c9a3a14c508ebd5ddb8fa676a1"
    - "tycho.page.e50b14deb6de4204b9f405942ab0cee8"
  excludes:
    - "No independent content acceptance or runtime reproduction is implied."
  keywords:
    - "Structured"
    - "logging"
    - "authoritative"
    - "audit"
    - "and"
    - "data"
    - "lineage"
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
updated_at: "2026-10-29"
source_inspection_date: "2026-10-29"
content_verified_at: null
---
<!-- tycho-question-source:tycho.page.436c2b22dc9e47acaaca7d18fadb511c:-1 -->

# Structured logging, authoritative audit and data lineage

> **Tycho original System Design manuscript V09/C04, 2026-10-19.** Public OpenTelemetry Logs Data Model and OpenLineage specifications support narrow data representation claims. All cases are invented, with no real logs, private identifiers, audit store, workflow run or compliance approval used.
>
> The content_review field retains the decomposition-era draft state; no independent
> acceptance is asserted.

<!-- /tycho-question-source -->

> **Pattern atlas:**
> [Structured Logging](../../v11-pattern-atlas/c11-security-operations/structured-logging.md#structured-logging) — decision conditions and contraindications.
> [Audit Trail](../../v11-pattern-atlas/c11-security-operations/audit-trail.md#audit-trail) — decision conditions and contraindications.

<!-- tycho-question-source:tycho.page.436c2b22dc9e47acaaca7d18fadb511c:0 -->
## Purpose and mission

Logs explain what software *reported*. Traces help correlate execution. A durable business audit record states what an authorized domain operation actually committed. Data lineage describes how datasets or outputs depend on inputs and processing jobs. These are different evidence products with different completeness, identity, privacy and retention requirements.

A sampled trace or best-effort log **cannot** become a trustworthy ledger of all authorized changes merely by being stored for years. An audit trail needs an explicit integrity, access, ordering and completeness contract. A lineage graph describes declared or observed data flows, not automatically a proof that every input/output transformation executed correctly.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.436c2b22dc9e47acaaca7d18fadb511c:7 -->
## Engineering walkthrough — One approved business change, three incompatible records

**Original fictional request:** an authorized operator changes a booking from PENDING to CONFIRMED. The application emits a diagnostic log, persists a business audit entry and updates a derived analytics dataset with a lineage event. All three may carry the same operation correlation ID; they still prove different things.

| Record type | Source of truth for | Cannot prove by itself |
|---|---|---|
| Application log/span | Diagnostic execution observations | Every relevant event was captured when telemetry sampling/export failed |
| Durable business audit | Who attempted/authorized which object mutation and resulting authoritative state, under a specified tamper/retention policy | That a downstream data warehouse is fresh |
| OpenLineage job/run event | Which source/target datasets and transformation run are related | That business approval or row-level correctness was achieved |

**Partial failure:** the booking state and required audit entry are committed under a chosen domain transaction/obligation, then telemetry export fails and lineage processing stalls. The correct user outcome may still be committed; a missing log is not proof that booking disappeared. Conversely, a successful log write preceding a rolled-back transaction cannot certify a durable business mutation. If legal obligations require atomic audit recording, architect the local commit or durable audit handoff explicitly; arbitrary asynchronous logs are insufficient.

**Recovery:** replay or reconstruct lineage from versioned source change positions and job IDs, while preserving independent business audit completeness; never silently regenerate an "approved" event merely because a process ran. [OpenTelemetry Logs Data Model](https://opentelemetry.io/docs/specs/otel/logs/data-model/) and the chapter's OpenLineage references support separate record semantics, not tamper-proof implementation.

**Proposed negative tests, not executed:** drop the collector, rerun a lineage job, change authorization mid-flight and roll back a transaction; require correct audit/lineage distinctions and minimal confidential data retention. If there is no mandatory forensic retention, costly immutable business audit infrastructure may be unnecessary for ordinary verbose debug logs.

<!-- /tycho-question-source -->

## Integrated decision and reading route

Separate diagnostic logs, authoritative audit and dataset lineage by identity, durability and retention obligations.

Three records about one operation can legitimately disagree in completeness; a log line alone does not prove an authorized commit.

The detailed pages separate the mechanisms that make this decision conditional:

- [Logs, authoritative audit and lineage](record-semantics.md) — Which question is answered by each kind of record?
- [Retention, integrity and contradictory records](record-integrity.md) — Which record must survive a failure before an authorized effect can be asserted?

[Chapter introduction, ordered pages and full source ledger](README.md). Original source labels retain their historical scope; this editorial decomposition does not turn proposed experiments into executed evidence.

## Bounded pattern ownership notes

These notes define the decision boundary for atlas cards whose mechanism is not the main subject of
this page. They are synthetic design guidance, not measured evidence, and they do not create a new
source claim.

### Structured Logging

Structured logging emits events with stable field names and types so records can be queried and
compared without parsing free text. Sensitive values must be excluded, or hashed or masked to
their protection level, when they are recorded. Unstructured text parsed at query
time is cheaper to start; adopt structured events when consistent querying, correlation or
retention obligations justify the schema.

**Invariant.** When sensitive data is logged, the application enforces the data's protection
level: data that may not be logged is excluded, and allowed sensitive values are hashed or
masked, in full or partially. Events also follow a consistent, machine-readable schema so the
log processor can read and correlate them. Requirement 16.2.5 states: "Verify that when logging
sensitive data, the application enforces logging based on the data’s protection level. For
example, it may not be allowed to log certain data, such as credentials or payment details.
Other data, such as session tokens, may only be logged by being hashed or masked, either in full
or partially." A schema-version and compatibility-window policy, and a build-failing redaction
test, are Tycho design guidance; the bound source states a common format and correlation
requirement, not a versioning or build-gate policy.

**Failure and recovery.** Logging sensitive personal data without a legal basis, or failing to
protect logs as a high-value asset, can compromise privacy or system security; a schema that
varies across emitters also needs normalization before reliable analysis. Protect logs from
unauthorized access and modification, and transmit them securely to a separate system for
analysis, detection, alerting and escalation. The control objective states: "Logs should not
include sensitive personal data unless legally required, and any logged data must be protected
as a high‑value asset. Logging must not compromise privacy or system security." Requirement
16.4.3 states: "Verify that logs are securely transmitted to a logically separate system for
analysis, detection, alerting, and escalation. The aim is to ensure that if the application is
breached, the logs are not compromised." Tycho recovery guidance, not an ASVS requirement:
stop emission, rotate exposed credentials, purge or redact retained records and notify.

**Limits.** A field allowlist, retention policy and redaction owner are costs; structured fields
can still encode sensitive values, and a schema without a migration path becomes query debt.
Log volume is not free, and sampling must preserve security events.

**Source boundary.** The invariant and failure/recovery claims are bound to `src.owasp-asvs`,
ledger record `read.batch6-asvs.2026-10-21`, section "V16 Security Logging and Error Handling",
requirements 16.2.4, 16.2.5, 16.4.2 and 16.4.3. The pinned PDF SHA-256 is
`a2fa1bbe38f12cac86d3a0f0023327e9772201f65a7f741f282f5e785d268fc5` (reverified 2026-10-29).
The mechanism and alternative remain bound to `src.otel`, ledger record
`read.batch6-otel-logs.2026-10-21`. ASVS is a verification standard: it does not define a schema
versioning policy or a purge/rotation/notification procedure, and those parts are Tycho
synthesis.

### Audit Trail

A durable business audit records who attempted or authorized which object mutation and the resulting
authoritative state, under a specified tamper and retention policy. It is a controlled business
record, not a debug log with a longer retention setting. The cited OpenLineage unit supports
dataset/job/run lineage events, not tamper-proof audit records; the audit controls here are
synthetic design guidance.

If legal obligations require atomic audit recording, architect the local commit or durable audit
handoff explicitly; arbitrary asynchronous logs are insufficient. The booking state and required
audit entry are committed under a chosen domain transaction/obligation, then telemetry export fails
and lineage processing stalls. The correct user outcome may still be committed; a missing log is not
proof that booking disappeared.

If there is no mandatory forensic retention, costly immutable business audit infrastructure may be
unnecessary for ordinary verbose debug logs. Audit is a fit when an external obligation defines the
record, its retention and its access path; otherwise a normal log with a retention policy is cheaper.
