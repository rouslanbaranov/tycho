# B58 — Distributed Tracing four-dimension lane

Status: lane-local book edit, self-checked on 2026-10-31. No shared edition
metadata, promotion, generated artifact or owner acceptance is included. The
entry was 1/4 at the parent HEAD: mechanism was supported; invariant,
failure/recovery and alternative were partial. This lane binds all four
dimensions to five public units inspected on 2026-10-31: OpenTelemetry
"Traces", "Context propagation" and "Sampling"; W3C "Trace Context"
(Recommendation of 23 November 2021); and Google "Dapper, a Large-Scale
Distributed Systems Tracing Infrastructure" (technical report dapper-2010-1).
The missing-span interpretation, metrics/log choice rule and recovery runbook
are labelled Tycho. The task brief calls the card inline V11/C11; the
registered card is a dedicated V11/C11 page. This lane edits the registered
page and leaves the C11 landing untouched.

## Lane coordinates

- Parent HEAD: `69acde64207d12870edb843761dcf2fe929fb6ce` (`69acde64`).
- Lane label: Tycho.
- Branch: `b58-tracing`; worktree:
  `/Users/rbaranov/Projects/tycho-worktrees/b58-tracing`.
- Scope: the owner section `### Distributed Tracing` in V09/C03 and the
  registered V11/C11 card `# Distributed Tracing`. Single-entry lane; no other
  entry, shared JSON, promotion or generated file is changed.
- Owner path (concatenate):

      book/volumes/v09-observability-security-and-operations/
      c03-distributed-tracing-and-propagation/
      distributed-tracing-context-and-sampling.md

- Card path:
  `book/volumes/v11-pattern-atlas/c11-security-operations/distributed-tracing.md`.
- Exactly three files change: the owner page, the card page and this note. No
  shared JSON file is edited.
- Existing source ids: `src.otel` and `src.trace-context`.
- New source id proposed: `src.dapper`, used only by the owner and card
  frontmatter until the integrator registers it.
- New ledger records proposed: five, listed below. Retained record:
  `read.batch6-otel-traces.2026-10-21`; it is superseded for current claims
  because the served Traces page and its canonical digest changed.
- Baseline and final line-length and boundary checks pass.

## Card location

The task brief names an inline card at V11/C11. The repository's registered
`tycho.pattern.distributed-tracing` card is the dedicated V11/C11 page above;
`edition/patterns/card-batches.v1.json` records that path. The C11 chapter
landing has only a link to the dedicated card and no distributed-tracing card
body to bind. This lane edits the registered card and leaves the landing
untouched. Precedent: B51 and B57 corrected the same kind of brief/registry
mismatch.

## Baseline and gap

`edition/patterns/owner-units.v1.json` records mechanism as supported and the
other three dimensions as partial. The recorded reasons are:

- mechanism: "Explains tracing as reconstructing a selected cross-component
  execution story."
- invariant: "OTel Traces page has no authoritative-record, missing-span or
  metrics/log comparison rule."
- failure/recovery: the same reason string.
- alternative: the same reason string.

The base owner page is the reviewed representation: 105 lines, 624 words,
SHA-256
`74418425f5134a145e21c00caabe0c909ffe744c432c9168bdc0d5b20bdbc204`.
The base owner section (line 90 through EOF) is 16 lines, 158 words, SHA-256
`ea89cf7465958467dcf2e32a3877a6fa78926045f4e7bc457b91ada40b71c653`.
The base card is 70 lines, 263 words, SHA-256
`5a3d698f5cc72ee1bd4b640996d0e00396b53b4beae6301c46354c260f6ceae7`.
The base card section (line 41 through EOF) is 30 lines, 155 words, SHA-256
`c2907b7996e59e2f29629e6a574555f2a4ca10e28f72786ebf77dc2fb29eab5f`.

The gap was evidential: the owner section already stated the invariants,
failure path and alternative as Tycho guidance, but only the older OTel Traces
record supported the mechanism. No exact public quote, section and
representation hash were bound to the non-authoritative trace, missing-span
ambiguity, sampling/instrumentation failure or metrics/structured-log
alternative. Shared metadata still shows 1/4 until the integrator applies the
proposals below.

## Candidate evaluation

- OpenTelemetry, "Traces" (selected). Defines a trace as the path of a request,
  explains span assembly through context propagation, and describes traces as
  structured logs with context and hierarchy. Primary source for the
  mechanism and the structured-log relationship.
- OpenTelemetry, "Context propagation" (selected). States correlation of
  traces, metrics and logs; defines context as correlating information; states
  that propagation is usually handled by instrumentation libraries; warns that
  forged trace headers are untrusted input. Primary source for the propagation
  boundary and the security limit.
- OpenTelemetry, "Sampling" (selected). Defines sampled/not sampled; explains
  head and tail sampling; records the head-sampling blind spot, the
  no-missing-spans property of consistent-probability head sampling, aggregate
  pre-aggregation, and the need to monitor tail-sampling components. Primary
  source for sampling ambiguity and recovery monitoring.
- W3C, "Trace Context" (selected). Defines the traceparent/tracestate
  propagation format; states the sampled flag denotes that the caller may have
  recorded data; requires trace-id generation to target global uniqueness;
  specifies invalid-context and restart behaviour. Primary source for the
  non-authoritative sampled flag and context-restart failure path.
- Google, "Dapper" technical report (selected). Describes trace context as a
  small container of span attributes; records instrumentation fragility and
  omissions; reports low-traffic sampling loss and trace-level sampling;
  records the sampling probability with the trace; notes other debug-log
  systems; states Dapper is not intended to replace all other tools. Primary
  source for instrumentation failure, sampling accounting and the alternative
  boundary.
- Retained `read.batch6-otel-traces.2026-10-21` is not used for current claims.
  Its 2026-10-21 canonical digest
  `e9678cd76218165297a0182a94a79d19a2338d926ea1a5fc0d01c6f11c4a4a98` differs
  from the 2026-10-31 digest `a255b2a8896771371e3b2ef2def8b13308b00af764cec3a6568deecc0b700d74`.
  The record remains historical evidence, not a current page representation.
- W3C Baggage was considered but not bound: it is adjacent context, not needed
  for the invariant or sampling claims. OpenTelemetry Metrics and Logs concept
  pages were considered but not bound as separate units: the alternative
  dimension is supported by statements on the selected Traces, Context
  propagation and Sampling pages. Vendor tracing documentation, tracing
  product pages, Dapper follow-up papers and blog posts were not used.
- No trace, sampler, collector, backend or distributed experiment was run.

## Source units and revisions

All fetches were public HTTPS GETs on 2026-10-31. Canonical text for HTML was
extracted with `scripts/source_content_hash.py`; raw HTML bytes and the served
headers are recorded separately. HTTP dates are UTC and byte counts are the
downloaded response bodies. The OTel pages are living documentation; their
page-level "Last modified" notes and canonical digests pin the inspected
representations, not a release tag.

### R1 — OpenTelemetry, Traces

- Record: `read.otel-traces.2026-10-31` (proposed).
- Source: `src.otel` (existing).
- URL: https://opentelemetry.io/docs/concepts/signals/traces/
- Label/type: "Traces — OpenTelemetry"; documentation-page.
- Representation: HTTP/2 200 on 2026-10-31T19:09:43Z; 433,512-byte
  text/html; ETag `W/"439614aedce30680f5f8c1ceb7dc75cf-ssl-df"`; no
  Last-Modified header; raw HTML SHA-256
  `c66f7efbbe3fa7c469815385f7fc7905f9921f7d7a887b46a766dbb30c152e6b`;
  canonical text 12,603 characters / 2,062 words, SHA-256
  `a255b2a8896771371e3b2ef2def8b13308b00af764cec3a6568deecc0b700d74`.
  Page note: "Last modified January 14, 2026: Convert all `en` page Note
  alerts to markdown syntax (#8894) (6bf06ddb)".
- Sections read: "Traces"; "Tracer Provider"; "Tracer"; "Trace Exporters";
  "Context Propagation"; "Spans"; "Span Context"; "Attributes"; "Span Events";
  "When to use span events versus span attributes"; "Span Links";
  "Span Status"; "Span Kind"; "Client"; "Server"; "Internal"; "Producer";
  "Consumer"; "Specification".
- Sections not read: linked child pages, code examples and navigation chrome.
- Claims supported: Q1, Q2, Q21.
- Limits: one concept page; the page is living documentation, no SDK was
  executed and no trace was exported.

### R2 — OpenTelemetry, Context propagation

- Record: `read.otel-context-propagation.2026-10-31` (proposed).
- Source: `src.otel` (existing).
- URL: https://opentelemetry.io/docs/concepts/context-propagation/
- Label/type: "Context propagation — OpenTelemetry"; documentation-page.
- Representation: HTTP/2 200 on 2026-10-31T19:09:43Z; 415,165-byte
  text/html; ETag `W/"8ea0242ab59aa52868e700d1900a66da-ssl-df"`; no
  Last-Modified header; raw HTML SHA-256
  `6de40e6c0e2a1958b96e7afc38fa3bc7300958c38b23565cc5433886f44b9986`;
  canonical text 6,965 characters / 1,096 words, SHA-256
  `036e40aac0f1617fde082e095d2e34aac4b0f7452aad2b0352c89f0426ae4a08`.
  Page note: "Last modified August 10, 2026: Fix context propagation example
  direction (#11254) (89a269b1)".
- Sections read: "Context"; "Propagation"; "Example"; "Traces"; "Logs";
  "Metrics"; "Custom Context Propagation"; "Security best practices";
  "External services"; "Baggage"; "Support in Language SDKs";
  "Specification".
- Sections not read: linked language SDK pages, the Context specification and
  code samples.
- Claims supported: Q3, Q9, Q20.
- Limits: concept page; it defines propagation, not a sampler or a backend.

### R3 — OpenTelemetry, Sampling

- Record: `read.otel-sampling.2026-10-31` (proposed).
- Source: `src.otel` (existing).
- URL: https://opentelemetry.io/docs/concepts/sampling/
- Label/type: "Sampling — OpenTelemetry"; documentation-page.
- Representation: HTTP/2 200 on 2026-10-31T19:09:44Z; 415,669-byte
  text/html; ETag `W/"44ee09e4ea10856f203d813eb67299a9-ssl-df"`; no
  Last-Modified header; raw HTML SHA-256
  `86947fb372ac750cc565b7dba240f0cdc0dc5021c66822ea1b3403754691e3c9`;
  canonical text 9,116 characters / 1,447 words, SHA-256
  `1895ba9c75cba6a2965b72cd0394cc97ca1c9d15b174b35e00b151d784686b3f`.
  Page note: "Last modified October 16, 2025: Replace OTEP 4673 links by
  reference to OTel spec trace/tracestate-probability-sampling (#8108)
  (6b2e90b3)".
- Sections read: "Terminology"; "Why sampling?"; "When to sample"; "When not
  to sample"; "Head Sampling"; "Tail Sampling"; "Support"; "Collector";
  "Language SDKs"; "Vendors".
- Sections not read: linked Collector processor and language SDK pages.
- Claims supported: Q7, Q11, Q16, Q18, Q19.
- Limits: concept page; it describes sampling policy, not a guarantee that a
  particular deployment samples correctly.

### R4 — W3C, Trace Context

- Record: `read.w3c-trace-context.2026-10-31` (proposed).
- Source: `src.trace-context` (existing).
- URL: https://www.w3.org/TR/2021/REC-trace-context-1-20211123/
- Label/type: "Trace Context — W3C Recommendation 23 November 2021";
  specification.
- Representation: HTTP/2 200 on 2026-10-31T19:09:44Z; 100,612-byte
  text/html; `Content-Location: Overview.html`; Last-Modified
  2021-11-23T13:50:04Z; no ETag; raw HTML SHA-256
  `9e7228d2a91c5aa4bef6e7f610366a2000274ee51699053e10c8ac3f0b8965be`;
  canonical text 44,920 characters / 6,875 words, SHA-256
  `5d5df65d954cbe0347dc6f61b53f7d58bc2c145ef1a27f2ab932a4b0214282f9`.
- Sections read: Abstract; "2.2 Solution"; "2.3 Design Overview";
  "3.2.2 traceparent Header Field Values"; "3.2.2.3 trace-id";
  "3.2.2.4 parent-id"; "3.2.2.5.1 Sampled flag"; "3.2.4 Versioning of
  traceparent"; "3.4 Mutating the traceparent Field"; "4.2 No traceparent
  Received"; "4.3 A traceparent is Received"; "8.1 Uniqueness of trace-id";
  "8.2 Randomness of trace-id".
- Sections not read: appendices, the implementation report, linked errata and
  full privacy/security analysis.
- Claims supported: Q5, Q6, Q14, Q15.
- Limits: dated Recommendation; it standardises propagation, not sampling
  policy, backend completeness or business authority.

### R5 — Google, Dapper technical report

- Record: `read.dapper-tracing.2026-10-31` (proposed).
- Source: `src.dapper` (proposed).
- URL:
  https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/36356.pdf
- Label/type: "Dapper, a Large-Scale Distributed Systems Tracing
  Infrastructure — Google Technical Report dapper-2010-1, April 2010"; paper.
- Representation: HTTP/2 200 on 2026-10-31T19:09:47Z; 1,551,487-byte
  application/pdf; 14 pages; PDF creation 2010-04-16 20:13:21 CEST;
  Last-Modified 2020-03-03T20:15:00Z; no ETag; raw PDF SHA-256
  `41baea09d066e0167ca0943968d44f7f07790be700440427f78c034910e5765d`.
  Extracted with `pdftotext -raw`: 1,251 lines / 10,015 words, text SHA-256
  `4a079899ab68b3fda92942b8af9825070c223b8dc7f529af2229f91c171ae919`.
- Sections read: Abstract; "1 Introduction"; "2.2 Instrumentation points";
  "2.4 Sampling"; "4.4 Adaptive sampling"; "4.5 Coping with aggressive
  sampling"; "4.6 Additional sampling during collection"; "6.1 Using Dapper
  during development".
- Sections not read: "6.2 Addressing long tail latency" through "6.6
  Firefighting with Dapper", "7 Other Lessons Learned", "8 Related Work" and
  the references.
- Claims supported: Q4, Q8, Q10, Q12, Q13, Q17.
- Limits: the public PDF is the authors' technical report, not a benchmark
  reproduction; the text has PDF line-break hyphenation and spacing
  artefacts. No Dapper deployment, trace or sampler was run.

## Selected exact quotes

Quotes reproduce the served prose. Line breaks inside a quote are editorial
wrapping. HTML extraction spaces before punctuation were normalized; PDF
line-end hyphenation was joined for quote checks. Every quoted source fragment
in the owner and card passed a whitespace-normalized substring check against
the named representation on 2026-10-31: 23 owner spans and 14 card spans,
including repeated titles and record labels. Tycho-labelled sentences in the
book are not source quotes.

### Mechanism

- Q1, R1, "Traces":

      The path of a request through your application.

- Q2, R1, "Context Propagation":

      With Context Propagation, Spans can be correlated with each other and
      assembled into a trace, regardless of where Spans are generated.

- Q3, R4, Abstract:

      This specification defines standard HTTP headers and a value format to
      propagate context information that enables distributed tracing
      scenarios.

- Q4, R5, "2.2 Instrumentation points":

      A trace context is a small and easily copyable container of span
      attributes such as trace and span ids.

### Invariant

- Q5, R4, "3.2.2.5.1 Sampled flag":

      When set, the least significant bit (right-most), denotes that the
      caller may have recorded trace data.

- Q6, R4, "8.1 Uniqueness of trace-id":

      The value of trace-id SHOULD be globally unique.

- Q7, R3, "Terminology":

      Not sampled: A trace or span is not processed or exported.

- Q8, R5, "1 Introduction":

      Although Dapper alone is sometimes sufficient for a developer to
      identify the source of a performance anomaly, it is not intended to
      replace all other tools.

- Q9, R2, "Security best practices":

      Malicious actors could send forged trace headers to manipulate your
      tracing data or potentially exploit vulnerabilities in context parsing.

### Failure and recovery

- Q10, R5, "1 Introduction":

      A tracing infrastructure that relies on active collaboration from
      application-level developers in order to function becomes extremely
      fragile, and is often broken due to instrumentation bugs or omissions

- Q11, R3, "Head Sampling":

      The primary downside to head sampling is that it is not possible to make
      a sampling decision based on data in the entire trace.

- Q12, R5, "4.4 Adaptive sampling":

      lower traffic workloads may miss important events at such low sampling
      rates, while tolerating higher sampling rates with acceptable
      performance overheads.

- Q13, R5, "4.6 Additional sampling during collection":

      By depending on the trace id for our sampling decision, we either sample
      or discard entire traces rather than individual spans within traces.

- Q14, R4, "3.4 Mutating the traceparent Field":

      Restart trace: All properties (trace-id, parent-id, trace-flags) are
      regenerated.

- Q15, R4, "4.3 A traceparent is Received":

      If the version cannot be parsed, the vendor creates a new traceparent
      header and deletes tracestate.

- Q16, R3, "Tail Sampling":

      Because of these factors, it is critical to monitor tail-sampling
      components to ensure that they have the resources they need to make the
      correct sampling decisions.

- Q17, R5, "4.4 Adaptive sampling":

      The actual sampling probability used is recorded along with the trace
      itself; this facilitates accurate accounting of trace frequencies in
      analytical tools built around Dapper data.

- Q18, R3, "Head Sampling":

      This ensures that whole traces are sampled - no missing spans - at a
      consistent rate, such as 5% of all traces.

### Alternative

- Q19, R3, "When not to sample":

      You only use observability data in aggregate, and can thus pre-aggregate
      data.

- Q20, R2, "Metrics":

      In the case of metrics, context propagation enables you to aggregate
      measurements in that context.

- Q21, R1, "Traces":

      One way to think of Traces is that they’re a collection of structured
      logs with context, correlation, hierarchy, and more baked in.

- Q22, R5, "1 Introduction": see Q8. The sentence is the source support for
  the alternative boundary; it is not duplicated as a separate quotation.

## Dimension mapping

- Mechanism. Primary: Q2, record `read.otel-traces.2026-10-31`, section
  "Context Propagation", revision
  `a255b2a8896771371e3b2ef2def8b13308b00af764cec3a6568deecc0b700d74`.
  Supporting: Q1 (trace path), Q3 (propagation format) and Q4 (trace-context
  container). Tycho reading: the trace is an assembled, propagated execution
  story, not a transaction log.
- Invariant. Primary: Q8, record `read.dapper-tracing.2026-10-31`, section
  "1 Introduction", revision
  `4a079899ab68b3fda92942b8af9825070c223b8dc7f529af2229f91c171ae919`.
  Supporting: Q5 and Q6 (sampled flag and SHOULD-unique trace-id), Q7
  (not-sampled definition) and Q9 (forged headers). Tycho rule: a missing span
  is ambiguous until instrumentation coverage and sampling policy are known;
  absence is not proof that no effect occurred, and trace/baggage values never
  become an authorization decision.
- Failure and recovery. Primary: Q10, record `read.dapper-tracing.2026-10-31`,
  section "1 Introduction", revision
  `4a079899ab68b3fda92942b8af9825070c223b8dc7f529af2229f91c171ae919`.
  Supporting: Q7 and Q11-Q13 (sampling loss and trace-level discard), Q14-Q15
  (context restart), Q16-Q17 (monitoring and sampling-probability accounting)
  and Q18 (whole-trace head sampling). Tycho runbook: alert on instrumentation
  coverage, sampling changes and context rejection separately; record the
  sampling decision; treat a gap as unknown; restore propagation first.
- Alternative. Primary: Q19, record `read.otel-sampling.2026-10-31`, section
  "When not to sample", revision
  `1895ba9c75cba6a2965b72cd0394cc97ca1c9d15b174b35e00b151d784686b3f`.
  Supporting: Q20 (metrics aggregation), Q21 (structured-log relationship) and
  Q22/Q8 (not a replacement for all tools). Tycho choice rule: metrics for
  aggregate latency or error rates; structured logs or audit for a discrete
  business event; tracing when the cross-component path is the question;
  reverse when trace cost exceeds the diagnostic benefit.

## Book edits

- Owner page (concatenate):

      book/volumes/v09-observability-security-and-operations/
      c03-distributed-tracing-and-propagation/
      distributed-tracing-context-and-sampling.md

  - Frontmatter adds existing ids `src.otel` and `src.trace-context` and
    proposed `src.dapper`; `evidence_scope.notes` records the five-unit
    binding; `content_review` becomes `self-checked` with reviewer
    "Automated authoring agent"; `updated_at` and `source_inspection_date`
    become 2026-10-31. The draft banner now says the evidence was bound on
    2026-10-31 and records a self-check.
  - The owner section gains four labelled paragraphs (mechanism, invariant,
    failure/recovery, alternative) and a bound-source-limits paragraph. The
    Tycho rules are labelled in the paragraphs.
  - Page 169 lines; 1,208 words; owner heading line 101.
  - SHA-256:
    `3c6bd4e2f08da329f03ea43c8e9ba49c9b5d3998d2c0897f331acdc655fcc1f5`.
- Card:
  `book/volumes/v11-pattern-atlas/c11-security-operations/distributed-tracing.md`.
  - Frontmatter fixes the truncated decision question, adds
    `src.trace-context` and proposed `src.dapper`, records the five-unit
    binding, and advances `reviewed_at`, `updated_at` and
    `source_inspection_date` to 2026-10-31.
  - "Good-fit conditions", "Hard contraindications", "Competing alternative",
    "Failure and recovery" and "Sources" are expanded with the same bindings
    and revisions; the owner link and anchor are unchanged.
  - Card heading line 49; chapter 98 lines; 541 words.
  - SHA-256:
    `d91814d30f055516f5d2f9dc40d4ada13f3cb08f1b6984d734039700d5ae00f8`.
- No other book file, edition JSON, promotion or generated file is changed.

## Metadata needs (integrator)

The following changes are not in the lane commit. They are required before the
owner unit can move to 4/4 supported and before atlas hash checks pass.

### Source register sources/register.json

Set updated to 2026-10-31; source count moves 323 to 324.

- Update `src.otel`: reading status `full-public-page-inspected`;
  access_checked and content_verified 2026-10-31; version note names the three
  2026-10-31 units, canonical hashes `a255b2a8...`, `036e40aa...` and
  `1895ba9c...`, raw hashes `c66f7efb...`, `6de40e6c...` and
  `86947fb3...`, and the page last-edit notes; verification scope names
  traces, context propagation, sampling, head/tail sampling and the
  untrusted-context warning. No SDK or exporter was run.
- Update `src.trace-context`: reading status `full-public-page-inspected`;
  access_checked and content_verified 2026-10-31; version note pins the
  2021-11-23 Recommendation, canonical hash `5d5df65d...`, raw hash
  `9e7228d2...` and Last-Modified 2021-11-23T13:50:04Z; verification scope
  names traceparent/tracestate, the sampled flag, trace-id uniqueness and
  restart behaviour.
- Add `src.dapper`: title "Dapper, a Large-Scale Distributed Systems Tracing
  Infrastructure"; publisher "Google"; kind `paper`; URL
  https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/36356.pdf;
  topics traceability, tracing and sampling; priority supporting; admission
  `admitted-for-research`; access `public-web-or-author-download`; reading
  status `full-public-page-inspected`; version note "Google Technical Report
  dapper-2010-1, April 2010; 14 pages; raw PDF SHA-256 41baea09...;
  `pdftotext -raw` text 1,251 lines / 10,015 words, SHA-256 4a079899...;
  HTTP Date 2026-10-31T19:09:47Z; Last-Modified 2020-03-03T20:15:00Z; no
  ETag"; access and content-verified dates 2026-10-31; license note "Public
  technical report; cite short excerpts and paraphrase; do not mirror.";
  verification scope names instrument points, sampling, adaptive sampling,
  sampling accounting and the not-a-replacement statement; observed title
  "Dapper, a Large-Scale Distributed Systems Tracing Infrastructure".

### Reading ledger edition/patterns/reading-ledger.v1.json

Add five records; records move 276 to 281. Each is status `read`, reviewer
"Automated authoring agent", access_date 2026-10-31 and uses the URL, label,
content_sha256, sections and limitations in R1-R5. R1-R3 use source_id
`src.otel`; R4 uses `src.trace-context`; R5 uses `src.dapper`. The retained
`read.batch6-otel-traces.2026-10-21` stays unchanged as historical evidence.

### Source plan edition/patterns/source-plan.v1.json

Replace the existing OTel Traces unit's `read_record_id` with
`read.otel-traces.2026-10-31`, and append four units for R2-R5 in record order.
Every new unit is status `read` and blocked_reason null. Replace the entry
notes with "Mechanism, invariant, failure/recovery and alternative bound
2026-10-31 to five public units: OpenTelemetry traces, context propagation and
sampling; W3C Trace Context; and Google Dapper. No runtime test or sufficiency
claim." Summary counters: required_units 321 to 325, read_units 320 to 324,
ledger_records 276 to 281; planned_units 0 and blocked_units 1 stay unchanged.

### Owner units edition/patterns/owner-units.v1.json

For `tycho.pattern.distributed-tracing`:

- mechanism: keep state supported and quote "Distributed tracing reconstructs
  *a selected execution story*: ..."; update the primary binding to
  `read.otel-traces.2026-10-31`, section "Context Propagation", revision
  `a255b2a8896771371e3b2ef2def8b13308b00af764cec3a6568deecc0b700d74`; add
  supporting bindings Q1, Q3 and Q4. Reason: OpenTelemetry defines the trace
  path and context assembly, W3C defines the propagation format and Dapper
  defines the trace-context container.
- invariant: set state supported; keep quote "A trace can illuminate
  critical-path waiting, retries and failure propagation—but **it is not an
  authoritative record of every business effect**."; primary binding Q8,
  source `src.dapper`, record `read.dapper-tracing.2026-10-31`, section
  "1 Introduction", revision
  `4a079899ab68b3fda92942b8af9825070c223b8dc7f529af2229f91c171ae919`; add
  supporting bindings Q5-Q7 and Q9. Reason: W3C says the sampled flag only
  denotes that the caller may have recorded data and trace-id uniqueness is a
  SHOULD, OpenTelemetry defines not-sampled as unexported, Dapper denies
  replacement of all tools, and OpenTelemetry warns about forged headers; the
  missing-span rule is Tycho.
- failure_recovery: set state supported; keep quote "A missing span may mean
  no work occurred, the instrumentation failed, or the sampling policy
  intentionally discarded it."; primary binding Q10, source `src.dapper`,
  record `read.dapper-tracing.2026-10-31`, section "1 Introduction",
  revision
  `4a079899ab68b3fda92942b8af9825070c223b8dc7f529af2229f91c171ae919`; add
  supporting bindings Q7, Q11-Q18. Reason: Dapper records instrumentation
  fragility and low-traffic sampling loss, OpenTelemetry records the
  head-sampling blind spot and tail-sampling monitoring need, W3C records
  context restart, and Dapper records sampling-probability accounting; the
  runbook order is Tycho.
- alternative: set state supported; keep quote "For aggregate latency or a
  discrete business event, metrics or structured logs may be preferable; use
  tracing when the cross-component path itself is the question."; primary
  binding Q19, source `src.otel`, record
  `read.otel-sampling.2026-10-31`, section "When not to sample", revision
  `1895ba9c75cba6a2965b72cd0394cc97ca1c9d15b174b35e00b151d784686b3f`; add
  supporting bindings Q20, Q21 and Q8. Reason: OpenTelemetry says aggregate
  data can be pre-aggregated, metrics aggregate in context, traces are
  structured logs with context, and Dapper is not a replacement for all
  tools; the choice rule is Tycho.
- technical_coverage: partial to partial-bounded; decision_coverage stays
  partial-bounded.
- source_support: primary new OTel Traces record with auxiliary R2-R5 and the
  retained old record; notes name the 2026-10-31 binding.
- Counters: invariant_supported 88 to 89; failure_recovery_supported 83 to 84;
  alternative_supported 88 to 89; mechanism_supported stays 123;
  technical_partial_bounded 15 to 16; technical_partial 59 to 58;
  technical_sufficient 71 stays.

### Other shared metadata

- Registry: add the five source_units (R1-R5) with status read;
  technical_owner state partial to partial-bounded; coverage technical partial
  to partial-bounded and overall partial to partial-bounded; decision stays
  partial-bounded; update notes.
- Card batches: update the distributed-tracing `ledger_record` from
  `read.batch6-otel-traces.2026-10-21` to
  `read.otel-traces.2026-10-31`; card_path and owner fields stay unchanged.
- Card frontmatter: this lane already declares `src.dapper`; no further source
  id change is needed after registration. The current
  `validate_book_metadata.py` failure "unknown source ID" is expected until
  the register includes `src.dapper`.
- coverage-map, sufficient-candidates, sufficient-review-records,
  atlas-manifest (registry_sha256), content-revisions (owner page and card
  historical-view hashes), inventory, page-census, route and section indexes,
  qrels and delivery-evidence: usual recomputation. The existing
  sufficient-candidates review record pins old page hash
  `2d682afa8da5d712828fd5d9e7e372fab27bbd1a86b04a3735105e36f47e27f3`, already
  stale for the 69acde64 base and further stale after this edit; it cannot be
  treated as a review pass.
- The owner page's claim_ids stay empty; no claim registry is introduced.

## Validation

- `python3 scripts/check_markdown_line_length.py`: PASS; 145 exact owner-link
  exceptions. The owner page is V09 and is not covered by this checker; every
  new owner line is at most 100 characters, and the pre-existing long
  frontmatter, purpose and reading-route lines are unchanged.
- `python3 scripts/check_boundary.py`: PASS; independent-origin review
  remains required.
- `python3 scripts/validate_pattern_cards.py`: PASS; 11 batches, 145 entries.
- `python3 scripts/validate_pattern_registry.py`: PASS; 145 entries,
  11 families.
- `python3 scripts/validate_book_metadata.py`: FAIL "unknown source ID" for
  `src.dapper`; expected until the integrator registers the proposed source.
- `python3 scripts/validate_edition.py`: FAIL
  "directory-baseline-payload-drift". The changed owner page needs a
  content-revisions entry before this baseline check can pass; no shared JSON
  is edited by this lane.
- `python3 scripts/validate_directory_migration.py`: FAIL with the same
  "directory-baseline-payload-drift" condition and the same integration need.
- `python3 scripts/validate_pattern_atlas.py`: FAIL "atlas-document-sha".
  The edited V11/C11 card no longer matches the hash pinned in the atlas
  manifest and semantic audit. This is expected until the integrator refreshes
  those shared records; no atlas JSON is edited by this lane.
- `python3 scripts/validate_book_navigation.py`: FAIL with four unchanged
  missing local anchors in dark-launching-shadow-traffic.md and rbac-abac.md;
  neither file is touched by this lane. The same four issues were recorded in
  the B50 and B51 integration notes.
- `python3 scripts/preflight_sufficient.py --pattern
  tycho.pattern.distributed-tracing`: FAIL as expected without shared
  metadata; it reports invariant, failure_recovery and alternative still
  partial. This is the pre-integration state, not a book defect.
- Quotes: 23 owner spans and 14 card spans passed a whitespace-normalized
  substring check against the five representations; title-only spans and
  repeated fragments are included in those counts.
- `git diff --check`: no whitespace errors.
- Raw SHA-256 after the book edits:
  owner page
  `3c6bd4e2f08da329f03ea43c8e9ba49c9b5d3998d2c0897f331acdc655fcc1f5`;
  card `d91814d30f055516f5d2f9dc40d4ada13f3cb08f1b6984d734039700d5ae00f8`.
- The lane note has no tab characters and every line is at most 100
  characters.

## Limits

- Shared metadata is not updated. The generated owner units, registry, source
  plan, ledger, card batches and indexes still show the entry as 1/4 or
  partial until an integrator applies the proposals above.
- No promotion, owner acceptance, coverage sufficiency or independent AI
  review is claimed. The book/atlas review gate remains outstanding; the
  existing review hash is stale for the edited page.
- No trace, span, sampler, collector, backend, benchmark or production
  observation was run. Dapper's reported deployment statistics are not
  reproduced.
- The OTel pages are living documentation with page-level last-edit notes and
  canonical digests, not release tags. The W3C unit is the dated 2021
  Recommendation; future re-fetches must compare the canonical digest before
  reusing a quote. The Dapper PDF is a 2010 technical report; the quote check
  joins line-end hyphenation and normalizes spacing.
- The card is dedicated, not inline in the C11 landing, because that is the
  registered path. The task brief's "inline" wording is recorded rather than
  silently treated as the repository layout.
