# B55 — SLI/SLO and error budgets four-dimension lane

Status: lane-local book edit, self-checked on 2026-10-31. No shared edition
metadata, promotion, generated artifact or owner acceptance is included. The
entry was 0/4 at the parent HEAD: all four dimensions were partial. This lane
binds mechanism, invariant, failure/recovery and alternative to six public
units read on 2026-10-31, labels the budget arithmetic, 2xx-only scenario and
action policy as Tycho, and edits the registered card. The task brief called
the card an inline V11/C08 card; the registered card is a dedicated V11/C11
page. This lane follows the registered path and leaves C08 untouched.

## Lane coordinates

- Parent HEAD: `8e4ec21e4cff4c23d282a29269a3803a161bc913` (`8e4ec21e`).
- Branch: `b55-slo`; worktree:
  `/Users/rbaranov/Projects/tycho-worktrees/b55-slo`.
- Scope: the owner section `### SLI-SLO and Error Budgets` in V09/C01 and the
  registered V11/C11 card `# SLI / SLO and Error Budgets`. Single-entry lane;
  no other entry, shared JSON, promotion or generated file is changed.
- Owner path (concatenate):

      book/volumes/v09-observability-security-and-operations/
      c01-slis-slos-and-error-budgets/
      service-level-indicators-objectives-and-alerts.md

- Card path:
  `book/volumes/v11-pattern-atlas/c11-security-operations/sli-slo-and-error-budgets.md`.
- Exactly three files change: the owner page, the card page and this note.
  No shared JSON file is edited.
- Existing source ids: `src.sre`, `src.sre-workbook` and `src.prometheus`.
- New source id proposed: `src.openslo`, used only by the owner and card
  frontmatter until the integrator registers it.
- New ledger records proposed: six, listed below.
- Retained record: `read.batch6-sre-slo.2026-10-21` remains historical. Its
  `content_sha256` is the 2026-10-21 raw HTML hash `60851ff3...`, not the
  canonical text hash used here.
- Baseline and final line-length and boundary checks pass.

## Card location

The task brief names an inline card at V11/C08. The repository's registered
`tycho.pattern.sli-slo-and-error-budgets` card is the dedicated V11/C11 page
above; `edition/patterns/card-batches.v1.json` and the atlas manifest record
that path. The V11/C08 coordination landing has nine unrelated cards and no
SLI/SLO section. This lane edits the registered card and does not add a card to
C08. Precedent: B42 and B49 corrected the same kind of brief/registry mismatch.

## Baseline and gap

`edition/patterns/owner-units.v1.json` records all four dimensions as
`partial`. The 2026-10-27 review finding says the then-bound SRE record
supported the error-budget concept but not the synthetic arithmetic, exclusion
categories or retrospective-change rule; the 2xx scenario had no recovery
action; and the alternative did not establish a reversal condition. The owner
section already stated the four dimensions as Tycho guidance, but bound one SRE
book unit only, with no exact public quote for any dimension.

The four owner-unit quote strings are preserved verbatim:

- mechanism: "A hypothetical target SLO of 99.9% would allow at most 10
  failures among 10,000 intents, while this window has 30, **consuming 300% of
  the target's error allowance**."
- invariant: "Whether user cancellations, blocked abusive traffic, malformed
  requests and legitimate overload rejections count must be agreed before
  measurement; exclusion policy cannot change retrospectively to improve the
  score."
- failure/recovery: "An instrumentation design that counts only HTTP 2xx
  responses among requests **admitted into the service**, excluding 500
  deliberate overload rejections before the handler, can report misleading
  health."
- alternative: "Metrics or a simpler availability check may be preferable when
  the user journey is not measurable."

Base owner page SHA-256:
`e1fab6a37a1d6120a1ce577f8e04bf7b1a90677e484be7f0fed3feea1e7fff5d`.
Base card SHA-256:
`2586787e84fe36931679c902c4e70cff09455f34c859fb517931db3e5daf87eb`.
Base owner section (line 109 through EOF) SHA-256:
`eb282fa277a5fecb11ef01d7f1e2f682dd5867491c65c2798e83c799b2ead349`.
Base card section (heading through EOF) SHA-256:
`46b0b564926cb1eaf5f3974b6801fa6ab8111521093ae5632df5dc0a0329a49d`.

The gap was evidential, not a missing definition. Shared metadata still shows
0/4 until the integrator applies the proposals below.

## Candidate units

- R1, Google SRE Workbook, "Implementing SLOs" (selected). Indicator, ratio,
  error-budget complement, windows and written policy.
- R2, Google SRE Workbook, "Alerting on SLOs" (selected). Burn rate,
  multiwindow multi-burn-rate alerting and reset time.
- R3, Google SRE Book, "Service Level Objectives" (selected). SLI/SLO/SLA
  definitions, aggregation, standard indicators and the control loop.
- R4, Prometheus, "Alerting rules" (selected). Alert rules, `for`,
  `keep_firing_for` and the Alertmanager boundary.
- R5, Prometheus, "Defining recording rules" (selected). Precomputed
  expressions, group limits and skipped evaluations.
- R6, OpenSLO, "Specification" (selected). Open vendor-agnostic SLO
  specification, platform-detail exclusion and the v1 schema.
- Prometheus histograms/query pages, the Workbook monitoring and case-study
  chapters, and the OpenSLO v2alpha draft were considered but not bound:
  adjacent material, draft material, or implementation detail outside the four
  dimensions. Linked pages, examples and images were not read as separate
  units. No source page was executed, deployed or benchmarked.

## Source units and revisions

Public HTTPS GETs on 2026-10-31; two fetches per URL were byte-identical.
Canonical text was extracted with `scripts/source_content_hash.py`. No
article-body marker was matched on the SRE pages, so their canonical digest
covers visible page text including navigation chrome. Quotes were checked as
whitespace-normalized substrings against the named canonical representation.

### R1 — Google SRE Workbook, Implementing SLOs

- Record: `read.sre-workbook-implementing-slos.2026-10-31` (proposed).
- Source: `src.sre-workbook` (existing).
- URL: https://sre.google/workbook/implementing-slos/
- Label/type: "Implementing SLOs — The Site Reliability Workbook, chapter 2";
  book-chapter.
- Representation: HTTP/2 200 on 2026-10-31T17:30:17Z; 104,090-byte text/html;
  Last-Modified 2026-10-08T04:48:00Z; no ETag; raw HTML SHA-256
  `1b02c7f3f640d92ca4357ba3e088fdbd6766274118afac934bede95ea9ea23e9`;
  canonical 54,720 characters / 8,917 words, SHA-256
  `9e2c70003b340d5ae10d9cd40684a2fdf94740be99830a560b0f1a0bafa8da06`.
- Sections read: "What to Measure: Using SLIs"; "Choosing an Appropriate Time
  Window"; "Getting Stakeholder Agreement"; "Establishing an Error Budget
  Policy"; "Decision Making Using SLOs and Error Budgets".
- Limits: living chapter, no published version identifier; canonical digest
  includes page chrome; linked pages and example code excluded; no SLO or
  budget was measured.

### R2 — Google SRE Workbook, Alerting on SLOs

- Record: `read.sre-workbook-alerting-on-slos.2026-10-31` (proposed).
- Source: `src.sre-workbook` (existing).
- URL: https://sre.google/workbook/alerting-on-slos/
- Label/type: "Alerting on SLOs — The Site Reliability Workbook, chapter 5";
  book-chapter.
- Representation: HTTP/2 200 on 2026-10-31T17:30:17Z; 88,545-byte text/html;
  Last-Modified 2026-10-08T04:48:00Z; no ETag; raw HTML SHA-256
  `340f148f65a7a92596c65f0a44828cbc1bcf165291cccf2c33a2b57673dd30b3`;
  canonical 29,456 characters / 4,780 words, SHA-256
  `2defa7d7e3784be2f877b4df4872f4a9e3d2862b38e3edf36315876ed2572b06`.
- Sections read: "Alerting Considerations"; "Ways to Alert on Significant
  Events"; "4: Alert on Burn Rate"; "6: Multiwindow, Multi-Burn-Rate Alerts";
  "Low-Traffic Services and Error Budget Alerting"; "Conclusion".
- Limits: living chapter, no published version identifier; canonical digest
  includes page chrome; linked pages and figures excluded; no alert was run.

### R3 — Google SRE Book, Service Level Objectives

- Record: `read.sre-book-slo.2026-10-31` (proposed).
- Source: `src.sre` (existing).
- URL: https://sre.google/sre-book/service-level-objectives/
- Label/type: "Service Level Objectives — Site Reliability Engineering,
  chapter 4"; book-chapter.
- Representation: HTTP/2 200 on 2026-10-31T17:30:17Z; 67,930-byte text/html;
  Last-Modified 2026-10-08T04:48:00Z; no ETag; raw HTML SHA-256
  `60851ff3487eef695bb59143b5123a79af081091ce8bf2909ad83ad924438365`;
  canonical 25,442 characters / 4,179 words, SHA-256
  `ef9a19e4e27b390f70c01422f4ad93fe6e320af30575ab1872706bcdbf703990`.
- Sections read: "Indicators"; "Objectives"; "Agreements"; "Aggregation";
  "Standardize Indicators"; "Control Measures"; "Choosing Targets".
- Limits: living chapter, no published version identifier; canonical digest
  includes page chrome; linked pages and figures excluded; no service metric
  was measured.
- Retained record: `read.batch6-sre-slo.2026-10-21` has the same raw HTML
  digest but is not replaced by this lane.

### R4 — Prometheus, Alerting rules

- Record: `read.prometheus-alerting-rules.2026-10-31` (proposed).
- Source: `src.prometheus` (existing).
- URL:
  https://prometheus.io/docs/prometheus/latest/configuration/alerting_rules/
- Label/type: "Alerting rules — Prometheus documentation";
  documentation-page.
- Representation: HTTP/2 200 on 2026-10-31T17:30:17Z; 172,244-byte text/html;
  no Last-Modified; no ETag; raw HTML SHA-256
  `d7e715618de655939afabee93a1e677e6179a249f75b0626e0cd4a72f72eb9af`;
  canonical 4,619 characters / 730 words, SHA-256
  `5c41ec67c7b4e8baeb613fc572145c51ccb4e812b659f866fd29b84607e77bbf`.
- Version: page selector "3.15 (latest)"; main-branch source Markdown in
  `prometheus/prometheus` at commit
  `9e28ec50ba751345a1f01a4fdc0d6887f533a37b`, SHA-256
  `92085dedf36ae2a9f16aa008931379815397862a9aee835f888ce087a741b7b5`.
- Sections read: "Defining alerting rules"; "Inspecting alerts during
  runtime"; "Sending alert notifications".
- Limits: living documentation; no Last-Modified or ETag; article body only;
  no Prometheus server was run.

### R5 — Prometheus, Defining recording rules

- Record: `read.prometheus-recording-rules.2026-10-31` (proposed).
- Source: `src.prometheus` (existing).
- URL:
  https://prometheus.io/docs/prometheus/latest/configuration/recording_rules/
- Label/type: "Defining recording rules — Prometheus documentation";
  documentation-page.
- Representation: HTTP/2 200 on 2026-10-31T17:30:18Z; 191,260-byte text/html;
  no Last-Modified; no ETag; raw HTML SHA-256
  `7b2c7443e4f6a2ef5cfffc5e8aeea07255088202b30d118bb0673f0187788f1d`;
  canonical 5,516 characters / 930 words, SHA-256
  `4b472352f06bb5c78d480e4035e9a28dba8af0e543de347a79e67ac4d31e0888`.
- Version: page selector "3.15 (latest)"; main-branch source Markdown in
  `prometheus/prometheus` at commit
  `9e28ec50ba751345a1f01a4fdc0d6887f533a37b`, SHA-256
  `7d9a9264340a9612d7153aba57641555203ad4433ef393a5a4635d0e2a62fda7`.
- Sections read: "Configuring rules"; "Recording rules"; "Limiting alerts and
  series"; "Failed rule evaluations due to slow evaluation".
- Limits: living documentation; no Last-Modified or ETag; article body only;
  no rule was executed.

### R6 — OpenSLO, Specification

- Record: `read.openslo-specification.2026-10-31` (proposed).
- Source: `src.openslo` (proposed).
- URL: https://openslo.com/specification/
- Label/type: "Specification — OpenSLO"; specification-page; v1.
- Representation: HTTP/2 200 on 2026-10-31T17:30:18Z; 157,171-byte text/html;
  Last-Modified 2026-09-24T22:30:05Z; ETag "6ab5a46d-265f3"; raw HTML SHA-256
  `1dea2d73127d61b87d10c4e958910a7af4a54feff504bfa9187f46cf7bd22bde`;
  canonical 26,926 characters / 4,331 words, SHA-256
  `0bc001c9e30e55f5b152865d1b089f4baa235c2cac2cdd1dbeb1cb93316db179`.
- Source revision: `OpenSLO/OpenSLO` commit
  `e0259752f252276485cfa2708dac2db00c2f3464` (2026-09-24T22:28:31Z);
  `website/docs/specification.md` SHA-256
  `ac6ea721628f7a72e7f52ba5619fce049125b24b3d02d5048dabe31a9f4c5ba3`.
- Sections read: "Introduction"; "Specification / Goals"; "General Schema";
  "Custom Data Types"; "Object Types / SLO".
- Limits: living v1 specification; v2alpha draft, SDK pages, examples and
  implementation links excluded; no SLO was validated or executed.

## Selected exact quotes

Quotes reproduce the served prose; line breaks inside a quote are editorial
wrapping. Every quote passed a whitespace-normalized substring check against
the named canonical text. Tycho-labelled sentences in the book are not quotes.

Mechanism:

- Q1, R1, "What to Measure: Using SLIs":

      an SLI is an indicator of the level of service that you are providing.

- Q2, R1, "What to Measure: Using SLIs":

      we generally recommend treating the SLI as the ratio of two numbers: the
      number of good events divided by the total number of events.

- Q3, R1, "What to Measure: Using SLIs":

      the SLO is a target percentage and the error budget is 100% minus the SLO.

- Q4, R3, "Objectives":

      a target value or range of values for a service level that is measured by
      an SLI.

- Q5, R3, "Choosing Targets":

      a rate at which the SLOs can be missed

- Q6, R6, "Object Types / SLO":

      a target value or a range of values for a service level that is described
      by a service level indicator (SLI).

Invariant:

- Q7, R3, "Aggregation":

      we often aggregate raw measurements. This needs to be done carefully.

- Q8, R3, "Standardize Indicators":

      We recommend that you standardize on common definitions for SLIs so that
      you don’t have to reason about them from first principles each time.

- Q9, R3, "Standardize Indicators":

      Which requests are included: “HTTP GETs from black-box monitoring jobs”

- Q10, R1, "Choosing an Appropriate Time Window":

      SLOs can be defined over various time intervals, and can use either a
      rolling window or a calendar-aligned window (e.g., a month).

Failure and recovery:

- Q11, R1, "Establishing an Error Budget Policy":

      once you exhaust your error budget (or come close to exhausting it), you
      should do something in order to restore stability to your system.

- Q12, R1, "Establishing an Error Budget Policy":

      This policy should cover the specific actions that must be taken when a
      service has consumed its entire error budget for a given period of time,
      and specify who will take them.

- Q13, R2, "4: Alert on Burn Rate":

      Burn rate is how fast, relative to the SLO, the service consumes the error
      budget.

- Q14, R2, "Conclusion":

      In most cases, we believe that the multiwindow, multi-burn-rate alerting
      technique is the most appropriate approach to defending your
      application’s SLOs.

- Q15, R2, "Alerting Considerations":

      Long reset times can lead to confusion or to issues being ignored.

- Q16, R4, "Defining alerting rules":

      Alerting rules allow you to define alert conditions based on Prometheus
      expression language expressions and to send notifications about firing
      alerts to an external service.

- Q17, R4, "Defining alerting rules":

      The optional for clause causes Prometheus to wait for a certain duration
      between first encountering a new expression output vector element and
      counting an alert as firing for this element.

- Q18, R4, "Defining alerting rules":

      There is also an optional keep_firing_for clause that tells Prometheus to
      keep this alert firing for the specified duration after the firing
      condition was last met.

- Q19, R4, "Defining alerting rules":

      This can be used to prevent situations such as flapping alerts, false
      resolutions due to lack of data loss, etc.

- Q20, R5, "Failed rule evaluations due to slow evaluation":

      If a rule group hasn't finished evaluating before its next evaluation is
      supposed to start (as defined by the evaluation_interval), the next
      evaluation will be skipped.

- Q21, R5, "Failed rule evaluations due to slow evaluation":

      The rule_group_iterations_missed_total metric will be incremented for each
      missed iteration of the rule group.

- Q22, R3, "Control Measures":

      Monitor and measure the system’s SLIs. Compare the SLIs to the SLOs, and
      decide whether or not action is needed. If action is needed, figure out
      what needs to happen in order to meet the target. Take that action.

Alternative:

- Q23, R6, "Introduction":

      The goal of this project is to provide an open specification for defining
      SLOs to enable a common, vendor–agnostic approach to tracking and
      interfacing with SLOs.

- Q24, R6, "Introduction":

      Platform-specific implementation details are purposefully excluded from
      the scope of this specification.

- Q25, R5, "Recording rules":

      Recording rules allow you to precompute frequently needed or
      computationally expensive expressions and save their result as a new set
      of time series.

## Dimension mapping

- Mechanism. Primary: Q1-Q3, record
  `read.sre-workbook-implementing-slos.2026-10-31`, sections "What to Measure:
  Using SLIs", "Choosing an Appropriate Time Window" and "Establishing an
  Error Budget Policy", revision
  `9e2c70003b340d5ae10d9cd40684a2fdf94740be99830a560b0f1a0bafa8da06`.
  Supporting: Q4-Q5 (SRE Book definitions) and Q6 (OpenSLO definition). Owner
  quote preserved: the 99.9%/300% arithmetic. Tycho reading: the ratio,
  target and complement are a measurement contract; the arithmetic is
  synthetic illustration, not a source claim.
- Invariant. Primary: Q7-Q9, record `read.sre-book-slo.2026-10-31`, sections
  "Aggregation" and "Standardize Indicators", revision
  `ef9a19e4e27b390f70c01422f4ad93fe6e320af30575ab1872706bcdbf703990`.
  Supporting: Q10 (window choice). Owner quote preserved: exclusion policy
  cannot change retrospectively. Tycho rule: fix population, numerator,
  denominator, window, aggregation and exclusions before measurement; publish
  them; treat a change as a new SLO version. The no-retrospective-change rule
  is Tycho governance, not an SRE source sentence.
- Failure and recovery. Primary: Q11-Q12, record
  `read.sre-workbook-implementing-slos.2026-10-31`, section "Establishing an
  Error Budget Policy"; Q13-Q15, record
  `read.sre-workbook-alerting-on-slos.2026-10-31`, sections "4: Alert on Burn
  Rate", "Alerting Considerations" and "Conclusion". Supporting: Q16-Q19,
  record `read.prometheus-alerting-rules.2026-10-31`, section "Defining
  alerting rules"; Q20-Q21, record
  `read.prometheus-recording-rules.2026-10-31`, section "Failed rule
  evaluations due to slow evaluation"; Q22 (control loop). Owner quote
  preserved: the 2xx-only scenario. Tycho reading: a skipped evaluation is a
  blind spot. Tycho runbook: alert on user-visible burn, bound reset, treat
  missed evaluations as a monitoring gap and execute the written policy.
- Alternative. Primary: Q23-Q24, record
  `read.openslo-specification.2026-10-31`, section "Introduction", revision
  `0bc001c9e30e55f5b152865d1b089f4baa235c2cac2cdd1dbeb1cb93316db179`.
  Supporting: Q25 and Q16 (executable recording and alerting rules). Owner
  quote preserved: a simpler availability check may be preferable. Tycho
  choice rule: use OpenSLO for portability; use Prometheus rules for
  executable queries and routing; reverse when translation cost exceeds the
  portability benefit or the platform-specific rule is the contract.

## Book edits

### Owner page

- Path (concatenate):

      book/volumes/v09-observability-security-and-operations/
      c01-slis-slos-and-error-budgets/
      service-level-indicators-objectives-and-alerts.md

- Frontmatter adds src.sre, src.sre-workbook, src.prometheus and src.openslo
  to evidence_scope.source_ids; sets status to source-linked and rewrites the
  notes; sets content_review to self-checked with reviewer "Automated
  authoring agent"; sets reviewed_at, updated_at and source_inspection_date to
  2026-10-31. The top note now describes the 2026-10-31 self-check.
- The "### SLI-SLO and Error Budgets" section keeps all four owner-unit
  quotes verbatim and adds labelled Mechanism, Invariant, Failure and
  recovery, Alternative and Bound source limits paragraphs plus Tycho reading,
  rule, runbook and choice-rule sentences.
- Section: line 117 through EOF, 74 lines, 879 words, SHA-256
  `ca445f45e6b8bf6098a2f872a06f6d95ee4f77d3280841e2fae30466f19d7f29`.
- Page: 190 lines, 1,700 words, SHA-256
  `884db1eaf79fb800911b656ab2c4a14b139f12583eaef3cf5dc39a05c8f9ffd1`.

### Card page

- Path:
  `book/volumes/v11-pattern-atlas/c11-security-operations/sli-slo-and-error-budgets.md`.
- Frontmatter adds src.sre-workbook, src.prometheus and src.openslo to the
  existing src.sre; rewrites the notes; sets reviewed_at, updated_at and
  source_inspection_date to 2026-10-31.
- "Good-fit conditions", "Hard contraindications", "Competing alternative"
  and "Failure and recovery" now bind the six records and label Tycho
  conditions. The "Sources" list names the six proposed records. The owner
  link and anchor are unchanged. The heading remains dedicated, not inline.
- Section: line 49 (heading) through EOF, 65 lines, 526 words, SHA-256
  `ffc94606389c37a886a882864dc48abc3c14258b6aebd71cf2e0706d9a21d5df`.
- Page: 113 lines, 665 words, SHA-256
  `982a44236882a12330a7d5408c1076c17317eb639f790398d3a0fd50bb7aaa87`.
- No other book file, edition JSON, promotion or generated file is changed.

## Metadata needs (integrator)

The following changes are not in the lane commit. They are required before the
entry can move to 4/4 supported and before review hashes can be rebound.

### Source register sources/register.json

Add one source and extend three existing version and verification_scope
entries with the 2026-10-31 representations.

- src.openslo (new): title "Specification"; publisher OpenSLO; kind
  specification; URL https://openslo.com/specification/; topics slos,
  reliability and interoperability; admission admitted-for-research; reading
  status full-public-page-inspected; license note "Public specification; cite
  short excerpts and paraphrase; do not mirror."; version names commit
  e0259752f252276485cfa2708dac2db00c2f3464, page Last-Modified
  2026-09-24T22:30:05Z, ETag "6ab5a46d-265f3", raw HTML SHA-256
  1dea2d73127d61b87d10c4e958910a7af4a54feff504bfa9187f46cf7bd22bde and
  canonical SHA-256
  0bc001c9e30e55f5b152865d1b089f4baa235c2cac2cdd1dbeb1cb93316db179;
  access and content-verified 2026-10-31.
- src.sre: extend the version and verification scope with the 2026-10-31
  chapter representation (67,930 bytes, Last-Modified 2026-10-08T04:48:00Z,
  raw SHA-256 60851ff3..., canonical SHA-256 ef9a19e4...), sections
  "Indicators", "Objectives", "Agreements", "Aggregation", "Standardize
  Indicators" and "Control Measures".
- src.sre-workbook: extend with "Implementing SLOs" (104,090 bytes,
  Last-Modified 2026-10-08T04:48:00Z, raw SHA-256 1b02c7f3..., canonical
  SHA-256 9e2c7000...) and "Alerting on SLOs" (88,545 bytes, Last-Modified
  2026-10-08T04:48:00Z, raw SHA-256 340f148f..., canonical SHA-256
  2defa7d7...).
- src.prometheus: extend with "Alerting rules" (172,244 bytes, no
  Last-Modified or ETag, raw SHA-256 d7e71561..., canonical SHA-256
  5c41ec67..., page version 3.15 latest) and "Defining recording rules"
  (191,260 bytes, no Last-Modified or ETag, raw SHA-256 7b2c7443...,
  canonical SHA-256 4b472352..., page version 3.15 latest), both pinned to
  prometheus/prometheus commit
  9e28ec50ba751345a1f01a4fdc0d6887f533a37b.

### Reading ledger edition/patterns/reading-ledger.v1.json

Add six records. Common fields: access_date 2026-10-31; access_method
"public HTTP fetch on 2026-10-31; two fetches byte-identical; canonical text
extracted with scripts/source_content_hash.py"; license notes "Public
documentation or specification; cite short excerpts and paraphrase; do not
mirror."; tables_figures "tables and figures in the inspected sections were
read in text form; not reproduced"; reviewer "Automated authoring agent";
status "read". Each content_sha256 is the canonical-text SHA-256 named below.

- read.sre-workbook-implementing-slos.2026-10-31 — source src.sre-workbook;
  unit "Implementing SLOs — The Site Reliability Workbook, chapter 2";
  unit_type book-chapter; content_sha256
  9e2c70003b340d5ae10d9cd40684a2fdf94740be99830a560b0f1a0bafa8da06;
  sections_read and limits as R1.
- read.sre-workbook-alerting-on-slos.2026-10-31 — source src.sre-workbook;
  unit "Alerting on SLOs — The Site Reliability Workbook, chapter 5";
  unit_type book-chapter; content_sha256
  2defa7d7e3784be2f877b4df4872f4a9e3d2862b38e3edf36315876ed2572b06;
  sections_read and limits as R2.
- read.sre-book-slo.2026-10-31 — source src.sre; unit "Service Level
  Objectives — Site Reliability Engineering, chapter 4"; unit_type
  book-chapter; content_sha256
  ef9a19e4e27b390f70c01422f4ad93fe6e320af30575ab1872706bcdbf703990;
  sections_read and limits as R3.
- read.prometheus-alerting-rules.2026-10-31 — source src.prometheus; unit
  "Alerting rules — Prometheus documentation"; unit_type documentation-page;
  content_sha256
  5c41ec67c7b4e8baeb613fc572145c51ccb4e812b659f866fd29b84607e77bbf;
  sections_read and limits as R4.
- read.prometheus-recording-rules.2026-10-31 — source src.prometheus; unit
  "Defining recording rules — Prometheus documentation"; unit_type
  documentation-page; content_sha256
  4b472352f06bb5c78d480e4035e9a28dba8af0e543de347a79e67ac4d31e0888;
  sections_read and limits as R5.
- read.openslo-specification.2026-10-31 — source src.openslo; unit
  "Specification — OpenSLO"; unit_type specification-page; content_sha256
  0bc001c9e30e55f5b152865d1b089f4baa235c2cac2cdd1dbeb1cb93316db179;
  sections_read and limits as R6.

### owner-units.v1.json

For tycho.pattern.sli-slo-and-error-budgets set technical_evidence.mechanism,
invariant, failure_recovery and alternative state to "supported" and replace
each partial reason with the Q/record binding note from the dimension mapping.
Keep the four quote strings unchanged. Set technical_coverage to "supported";
keep decision_coverage "partial-bounded" unless a separate decision review
changes it. Set source_support.ledger_record to
read.sre-workbook-implementing-slos.2026-10-31 and record the other five
supporting records in notes. Update the card path/hash and owner line/anchor if
the schema stores them; the card remains dedicated at
book/volumes/v11-pattern-atlas/c11-security-operations/sli-slo-and-error-budgets.md.

### source-plan.v1.json and review metadata

Extend required_units for tycho.pattern.sli-slo-and-error-budgets with R1-R6
and replace the single R3 record status with read.sre-book-slo.2026-10-31.
Keep the existing SRE unit URL and section list, adding the 2026-10-31
revision. The sufficient-candidates, sufficient-rereview-packets and any
owner/card hash rows that still carry e1fab6a3... or 2586787e... are stale for
this edit; they must be rebound by the integrator, not by this lane. The owner
page is now 884db1ea... and the card 982a4423...; review records must not
treat the old hashes as current. No promotion, owner acceptance or independent
review is claimed.

## Limits

- The six units are living public documentation or specification pages, not
  benchmarks, measurement standards or production observations. The digests
  pin the 2026-10-31 representations, not every future revision.
- The SRE page digests include served navigation chrome because no
  article-body marker was matched. Quotes were checked against that canonical
  text and reproduce the prose only.
- Prometheus "latest" identified itself as version 3.15 at retrieval and has
  no Last-Modified or ETag. The main-branch source Markdown was pinned to
  prometheus/prometheus commit 9e28ec50...; the live page can change without a
  version bump.
- OpenSLO is the v1 specification. The v2alpha enhancement draft linked from
  the page is out of scope. A specification is not an implementation; no SLO
  was validated, generated or executed.
- The 99.9%/300% arithmetic, the 2xx-only admission blind spot and the
  action-policy examples are Tycho synthetic guidance, not SRE source claims.
- The no-retrospective-exclusion rule is Tycho governance. The SRE Book
  supports standard templates, aggregation care and request inclusion; it does
  not state the no-retrospective-change rule.
- The owner page is in V09, so the repository's V11 line-length checker does
  not cover it. Its touched range was checked directly and has no line over
  100 characters. The card's only over-100 line is the exact technical-owner
  link exception recognized by the V11 checker.
- The task brief called the card inline V11/C08; this lane edits the
  registered dedicated V11/C11 card and does not touch C08. Promotion still
  requires the independent AI review gate and owner acceptance.
- No SLO, alert rule, recording rule, Prometheus server, Alertmanager or
  monitoring deployment was created or run. No budget, burn rate, alert
  latency or recovery measurement was made.
- The page's claim_ids stay empty; no claim registry is introduced.

## Checks

- python3 scripts/check_markdown_line_length.py — PASS: V11 prose <=100;
  145 exact owner-link exceptions.
- python3 scripts/check_boundary.py — PASS: configured lexical boundary
  checks; independent-origin review still required.
- Direct owner touched-range check — 0 lines over 100 characters in lines
  117-190.
- Direct card touched-range check — only the exact technical-owner link
  exception is over 100 characters.
- Quote verification — 30 quoted strings PASS as whitespace-normalized
  substrings of the named canonical text; owner-unit quote preservation PASS
  for all four strings.
- Frontmatter YAML parse — PASS for owner and card; source ids 4 and 4.
- git diff --check — PASS.
- No unit tests were run for this two-page content lane; the full suite is not
  applicable to a lane-local authoring edit.

## Commit scope

The lane commit contains this note and the two book files only:

- the V09/C01 owner page
  service-level-indicators-objectives-and-alerts.md;
- the V11/C11 card sli-slo-and-error-budgets.md;
- authoring/B55-SLI-SLO-ERROR-BUDGETS-LANE-2026-10-31.md.

No shared JSON, promotion or generated file is in the lane commit.
