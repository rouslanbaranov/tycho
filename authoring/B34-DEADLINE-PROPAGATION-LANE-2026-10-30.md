# B34 — Deadline Propagation mechanism and failure/recovery lane

Status: lane-local book edit, self-checked on 2026-10-30. No shared edition
metadata, promotion, generated artifact or owner acceptance is included. The
entry was 2/4 at the parent HEAD: invariant and alternative were supported;
mechanism and failure/recovery were partial. This lane binds the
source-supported parts of both dimensions to the public gRPC Deadlines guide,
the public gRPC over HTTP2 specification and Google SRE's "Addressing Cascading
Failures". Unsupported claims are labelled Tycho guidance, not source claims.
The metadata patch was exercised in a detached scratch copy: preflight passes
1/1, owner units, registry, cards, sources, source plan, book metadata,
directory migration, decomposition and enrichment pass. The patch is not in the
lane commit; promotion is not claimed or ready.

## Lane coordinates

- Parent HEAD: `8fd1a0a35428e5f23a5a7f7bb28e61a3f3d3b5bd` (`8fd1a0a3`).
- Branch: `b34-deadline`; worktree:
  `/Users/rbaranov/Projects/tycho-worktrees/b34-deadline`.
- Scope: the owner section `### Deadline Propagation` in the V02/C05 owner
  page and the inline V11/C07 card `### Deadline Propagation`. Single-entry
  lane; no other entry, shared owner page, promotion or generated file is
  changed.
- Owner path (concatenate the three lines):

      book/volumes/v02-application-boundaries-and-contracts/
      c05-public-apis-http-rpc-and-compatibility/
      deadlines-retries.md

- Card path:
  `book/volumes/v11-pattern-atlas/c07-resilience/README.md`.
- Path discrepancy: the parent brief named V11/C02 as the card location. At
  this HEAD the Deadline Propagation card is inline in V11/C07; V11/C02 has 12
  unrelated API-communication cards, and the registry names V11/C07 as the
  atlas owner. The parent confirmed C07 and no C02 card was created.
- The card remains inline; the integrator owns any split and `card_path`
  registration.

## Candidate evaluation

- gRPC, "Deadlines" (proposed source `src.grpc-deadlines`). Selected for the
  absolute-to-relative conversion, elapsed-time deduction, clock-skew
  shielding, automatic server cancellation, application responsibility for
  spawned work and the `DEADLINE_EXCEEDED`/`CANCELLED` outcomes. The guide
  does not define a numeric skew bound, test an implementation or prove that
  all gRPC implementations propagate by default.
- gRPC, "gRPC over HTTP2" (proposed source `src.grpc-protocol`). Selected for
  the `grpc-timeout` relative value/unit grammar and the rule that an omitted
  Timeout header means an infinite timeout. Only the Requests section was
  read; linked RFCs, implementations and examples were not verified.
- Google SRE, "Addressing Cascading Failures" (existing source
  `src.sre-cascading`, record `read.batch4-sre-cascading.2026-10-21`).
  Selected for the per-stage deadline check, the absolute-deadline
  description, the remaining-seconds worked example and the ignored-expiry
  consequence. The chapter does not discuss clock synchronization or define a
  skew tolerance.
- gRPC, "Cancellation" and "Retry" guides (already linked from the owner page)
  were considered but not selected: they add no distinct binding for the two
  dimensions. No selected source tests clock-skew behavior or a propagated
  deadline in a running system.

## Source binding

Quotes reproduce the served prose; Markdown inline-code and bold markers are not
repeated. The binding revision always identifies the exact representation.

### gRPC Deadlines

- Source id: `src.grpc-deadlines` (new).
- Proposed record: `read.grpc-deadlines.2026-10-30`.
- URL: `https://grpc.io/docs/guides/deadlines/`.
- Unit label: "Deadlines — gRPC guide"; unit type `documentation-page`;
  access date 2026-10-30.
- Access: public HTTPS GET; served HTML 72,634 bytes; HTTP Date
  2026-10-30T17:56:43Z; no Last-Modified or ETag; raw HTML SHA-256
  `879c69cdb7370ebcd5fbb6bd06ab95853378681381010c3d10f7a17ee6d7d776`.
  The binding revision is the pinned source Markdown at grpc/grpc.io commit
  `78db5a6f78ee0d3426cf53cee07739196d962ea2` (last modified 2025-07-07,
  "Add link to C++ deadline example (#1445)"): 4,703 bytes, 114 lines,
  SHA-256
  `e310a0e5a4bdc8f353ef04a641336d9a51176ffaa0ba0ee8b8b1aad98263a900`.
- Sections used: "Overview", "Deadlines on the Client", "Deadlines on the
  Server", "Deadline Propagation".
- Exact quotes used:

      A deadline is used to specify a point in time past which a client is
      unwilling to wait for a response from a server.

      A timeout is the max duration of time that the call can take. A timeout
      can be converted to a deadline by adding the timeout to the current
      time when the application starts a call.

      If a server has gone past the deadline when processing a request, the
      client will give up and fail the RPC with the DEADLINE_EXCEEDED status.

      A gRPC server deals with this situation by automatically cancelling a
      call (CANCELLED status) once a deadline set by the client has passed.

      Please note that the server application is responsible for stopping any
      activity it has spawned to service the RPC.

      Automatically propagating the deadline from an incoming RPC to an
      outgoing one is supported by some gRPC implementations. In some
      languages this behavior needs to be explicitly enabled (e.g. C++) and in
      others it is enabled by default (e.g. Java and Go).

      Since a deadline is set point in time, propagating it as-is to a server
      can be problematic as the clocks on the two servers might not be
      synchronized. To address this gRPC converts the deadline to a timeout
      from which the already elapsed time is already deducted. This shields
      your system from any clock skew issues.

- Limits: a living documentation page pinned by commit and digest, not an
  implementation test. The guide does not prescribe monotonic clocks, a skew
  tolerance or a durable cleanup path.

### gRPC over HTTP2

- Source id: `src.grpc-protocol` (new).
- Proposed record: `read.grpc-protocol.2026-10-30`.
- URL: GitHub blob `doc/PROTOCOL-HTTP2.md` at commit
  `36a2ae2930d02c392e6e471c0d95d9d6e0c62dc9`; the exact URL is
  `https://github.com/grpc/grpc/blob/` + that commit + the path.
- Unit label: "gRPC over HTTP2 — protocol specification"; unit type
  `specification`; access date 2026-10-30.
- Access: public HTTPS GET; pinned raw Markdown at grpc/grpc commit
  `36a2ae2930d02c392e6e471c0d95d9d6e0c62dc9`; 16,105 bytes, 266 lines;
  SHA-256
  `b51ea1b8cee67ad3477e73152bb60ac3ebf6e164962b46ba79434e980739256f`.
- Section used: "Requests".
- Exact quotes used:

      Timeout → "grpc-timeout" TimeoutValue TimeoutUnit

      TimeoutValue → {positive integer as ASCII string of at most 8 digits}

      TimeoutUnit → Hour / Minute / Second / Millisecond / Microsecond /
      Nanosecond

      If Timeout is omitted a server should assume an infinite timeout. Client
      implementations are free to send a default minimum timeout based on
      their deployment requirements.

- Limits: a protocol grammar and one omission rule, not evidence that a
  particular implementation detects or reports a lost header.

### Google SRE — Addressing Cascading Failures

- Source id: `src.sre-cascading` (existing).
- Existing record: `read.batch4-sre-cascading.2026-10-21`.
- URL: `https://sre.google/sre-book/addressing-cascading-failures/`.
- Unit label: "Addressing Cascading Failures — public chapter"; unit type
  `book-chapter`; access date 2026-10-21; re-read 2026-10-30.
- Recheck 2026-10-30: served HTML 104,870 bytes; HTTP Date
  2026-10-30T17:56:44Z; Last-Modified 2026-10-08T04:48:00Z; raw HTML SHA-256
  `d67024d52d72a1254c830d3c29e6d1b2afade88e133ffcff64b94711c2aaa11a`,
  equal to the record's `content_sha256`.
- Section used: "Latency and Deadlines".
- Exact quotes used:

      If handling a request is performed over multiple stages (e.g., there
      are a few callbacks and RPC calls), the server should check the deadline
      left at each stage before attempting to perform any more work on the
      request.

      With deadline propagation, a deadline is set high in the stack (e.g.,
      in the frontend). The tree of RPCs emanating from an initial request
      will all have the same absolute deadline.

      For example, if server A selects a 30-second deadline, and processes the
      request for 7 seconds before sending an RPC to server B, the RPC from A
      to B will have a 23-second deadline.

      Had server B used deadline propagation, server C could immediately give
      up on the request because the 2-second deadline was exceeded.

      You may want to reduce the outgoing deadline a bit (e.g., a few hundred
      milliseconds) to account for network transit times and post-processing
      in the client.

      There are some exceptions for which servers may wish to continue
      processing a request after the deadline has elapsed.

- Limits: the chapter describes an absolute deadline and then gives each hop
  the remaining seconds; this lane records that tension as a Tycho
  reconciliation, not as a resolved source statement. The chapter does not
  discuss clock skew or a numeric tolerance.

## Book edits

### Owner section

- Frontmatter: only `updated_at` moves to 2026-10-30. `evidence_scope` and
  `content_review` remain byte-identical to the decomposition baseline;
  `source_inspection_date` and `content_verified_at` stay `null`.
- The mechanism paragraph binds the relative-duration claim to gRPC's
  absolute-to-timeout conversion and elapsed-time deduction, and records the
  SRE absolute-deadline description with its remaining-seconds example. The
  reconciliation to an ingress-fixed deadline is labelled Tycho.
- The invariant sentence remains "The ingress sets the budget and each hop
  checks expiry before starting work." Enforcement is described as split
  between automatic server cancellation and application checks; monotonic
  clocks and the hint-without-enforcement rule are labelled Tycho.
- The failure/recovery paragraph names clock skew, a lost timeout header and
  ignored expiry; it quotes the omitted-header infinite timeout, the
  application responsibility and the client/server outcomes. Ingress deadline
  requirements, bounded skew and durable cleanup are labelled Tycho.
- A source boundary lists the three records and their exact revisions.
- The heading stays at line 207; the page is 259 lines.
- Raw SHA-256:
  `4123740bb19b96c22241eec2b86644aa434d1d06056094f90aaf26b939ad0f91`.
- Historical-view SHA-256:
  `1c5f5588d1c8f177a16faf4a663dcf83e46ee29e94da77cb9841771860d8bdde`.

### V11/C07 inline card

- Frontmatter adds `src.grpc-deadlines` and `src.grpc-protocol` to
  `evidence_scope.source_ids`. The review, update and inspection dates move
  to 2026-10-30; `content_verified_at` stays `null`.
- **Good-fit conditions** now require a relative remaining budget, per-hop
  enforcement and observable expiration.
- **Failure and recovery** now states the gRPC conversion, the omitted-header
  infinite timeout, automatic cancellation, application responsibility and the
  Tycho-only requirements for ingress deadlines, bounded skew and outcome
  recording.
- **Technical owner** and **Sources** name the three records and their
  sections. The owner link is unchanged.
- The heading moves from line 237 to line 239 because of the two added source
  ids. The chapter page is 624 lines.
- Raw SHA-256:
  `cc3f0534eaad92c156a98877827bad8ace9a09c9e8dcd23fa4b4eec62ef2cb27`.
- Historical-view SHA-256:
  `281886de150b086403ec7cdfee6571fbe02c4f000663b45560fdc3ad838914a9`.

No other book file is changed by this lane.

## Metadata needs (integrator)

The following patch is not in the lane commit. It was exercised in a detached
scratch copy of this worktree with the two book files, the source register,
ledger, source plan, registry, owner units, card batches, content revisions and
route index. The scratch results are in the Validation section.

### Source register `sources/register.json`

Add two source records. Set `updated` to 2026-10-30. The source count moves
from 291 to 293.

- `src.grpc-deadlines` — title "Deadlines"; category "contracts"; publisher
  "gRPC authors"; kind "official-docs"; URL
  `https://grpc.io/docs/guides/deadlines/`; topics
  `["rpc", "deadlines", "clock-skew"]`; priority "core"; planned use
  "Deadline propagation, remaining-budget conversion and server cancellation
  semantics for the Deadline Propagation entry."; admission
  "admitted-for-research"; access "public-web-or-author-download"; reading
  status "full-public-page-inspected"; version records the 2026-10-30 access,
  the 72,634-byte served HTML with SHA-256 `879c69cd...`, the pinned source
  Markdown at commit `78db5a6...` with 4,703 bytes and SHA-256
  `e310a0e5...`, HTTP Date 2026-10-30T17:56:43Z and no Last-Modified or
  ETag; `access_checked` 2026-10-30; `content_verified` 2026-10-30; license
  note "Public gRPC documentation; cite short excerpts and paraphrase; do not
  mirror."; verification scope covers the full public page, excluding the
  linked language examples and the deadlines blog post; observed title
  "Deadlines | gRPC".
- `src.grpc-protocol` — title "gRPC over HTTP2"; category "contracts";
  publisher "gRPC authors"; kind "specification"; URL
  `https://github.com/grpc/grpc/blob/` + commit
  `36a2ae2930d02c392e6e471c0d95d9d6e0c62dc9` + `/doc/PROTOCOL-HTTP2.md`;
  resolved URL the matching raw URL; topics
  `["rpc", "http2", "deadlines"]`; priority "supporting"; planned use
  "grpc-timeout wire representation and the omitted-header timeout rule for
  the Deadline Propagation entry."; admission "admitted-for-research"; access
  "public-web-or-author-download"; reading status
  "full-public-page-inspected"; version records the pinned commit, 16,105
  bytes, 266 lines and SHA-256 `b51ea1b8...`, accessed 2026-10-30, with no
  published version tag; `access_checked` 2026-10-30;
  `content_verified` 2026-10-30; license note "Public gRPC protocol
  specification; cite short excerpts and paraphrase; do not mirror.";
  verification scope covers the Requests and Responses sections and the
  protocol outline, excluding linked RFCs, implementations and examples;
  observed title "gRPC over HTTP2".

### Reading ledger `edition/patterns/reading-ledger.v1.json`

Add two records. Set `updated` to 2026-10-30. Records move from 170 to 172.

- `read.grpc-deadlines.2026-10-30` — source `src.grpc-deadlines`; unit
  label "Deadlines — gRPC guide"; type `documentation-page`; URL the gRPC
  Deadlines URL; access 2026-10-30; sections read "Overview", "Deadlines on
  the Client", "Deadlines on the Server" and "Deadline Propagation";
  `content_sha256` `e310a0e5...`; status `read`; reviewer "Automated
  authoring agent". Claims supported: the absolute-to-relative conversion
  with elapsed time deducted; clock-skew shielding; automatic server
  cancellation; application responsibility for spawned work; client
  `DEADLINE_EXCEEDED` and server `CANCELLED`. Claims not supported: a
  numeric skew bound, implementation behavior, a tested deployment. Limit:
  full guide page, linked examples and implementation not verified.
- `read.grpc-protocol.2026-10-30` — source `src.grpc-protocol`; unit label
  "gRPC over HTTP2 — protocol specification"; type `specification`; URL the
  pinned GitHub blob URL; access 2026-10-30; section read "Requests";
  `content_sha256` `b51ea1b8...`; status `read`; reviewer "Automated
  authoring agent". Claims supported: `grpc-timeout` carries a relative
  value and unit; an omitted Timeout header means an infinite timeout. Claims
  not supported: lost-header detection by an implementation. Limit: Requests
  section only; linked RFCs and implementations not verified.

Keep `sections_read` exactly equal to the source-plan sections below.

### Source plan `edition/patterns/source-plan.v1.json`

Append two units to `tycho.pattern.deadline-propagation` after the existing
SRE unit:

- `src.grpc-deadlines`: unit "Deadlines — gRPC guide", type
  `documentation-page`, URL the gRPC Deadlines URL, sections
  `["Overview", "Deadlines on the Client", "Deadlines on the Server",
  "Deadline Propagation"]`, status `read`, record
  `read.grpc-deadlines.2026-10-30`.
- `src.grpc-protocol`: unit "gRPC over HTTP2 — protocol specification", type
  `specification`, URL the pinned GitHub blob URL, sections
  `["Requests"]`, status `read`, record
  `read.grpc-protocol.2026-10-30`.

Replace the entry notes with: "The relative timeout, clock-skew conversion and
server cancellation use gRPC Deadlines; the omitted-header infinite timeout
uses gRPC over HTTP2; per-stage checks and the absolute-deadline example use
Google SRE. Monotonic-clock use, bounded skew and durable cleanup remain Tycho
guidance."

Set `updated` to 2026-10-30. Summary: `required_units` 207 -> 209;
`read_units` 206 -> 208; `ledger_records` 170 -> 172. Recompute
`registry_sha256` after saving the registry and refresh
`route_index_snapshot` from the rebuilt route index.

### Registry `edition/patterns/registry.v1.json`

For `tycho.pattern.deadline-propagation`:

- Set `technical_owner.state` to `partial-bounded`.
- Set `coverage.technical` and `coverage.overall` to
  `partial-bounded`; keep `coverage.decision` at `partial-bounded`.
- Replace `source_units` with, in order: the existing SRE unit "Addressing
  Cascading Failures — public chapter"; "Deadlines — gRPC guide"; "gRPC over
  HTTP2 — protocol specification". All three have status `read`.
- Replace `notes` with: "Mechanism and failure/recovery bound 2026-10-30 to
  gRPC Deadlines, gRPC over HTTP2 and Google SRE; monotonic clocks, bounded
  skew and durable cleanup remain Tycho guidance. Coverage partial-bounded; no
  promotion."
- Keep `review_status` `self-checked` and `atlas_owner` at V11/C07.

### Owner units `edition/patterns/owner-units.v1.json`

Entry `tycho.pattern.deadline-propagation`:

- Keep `owner.line` at 207, the heading and the four unit terms unchanged.
- Mechanism:
  - `state`: `supported`.
  - `quote`: "Deadline propagation carries the caller's remaining budget as a
    relative duration."
  - `reason`: "gRPC converts an absolute deadline to a timeout with elapsed
    time deducted before propagation, which supports a relative
    remaining-budget form; Google SRE's worked example states the remaining
    seconds at each hop. The reconciliation to an absolute ingress deadline
    and the monotonic-clock rule are Tycho guidance."
  - `binding`: `src.grpc-deadlines`, record
    `read.grpc-deadlines.2026-10-30`, section "Deadline Propagation", the
    "Since a deadline is set point in time ..." passage, revision
    `e310a0e5...`.
  - Supporting bindings: Google SRE, record
    `read.batch4-sre-cascading.2026-10-21`, section "Latency and Deadlines",
    the "With deadline propagation ..." passage, revision `d67024d5...`;
    gRPC Deadlines, record `read.grpc-deadlines.2026-10-30`, section
    "Deadlines on the Server", the "A gRPC server deals with this situation
    ..." passage, revision `e310a0e5...`.
- Failure/recovery:
  - `state`: `supported`.
  - `quote`: "Clock skew, a lost timeout header and a hop that ignores expiry
    are the common failures."
  - `reason`: "The gRPC guide says propagating an absolute deadline is
    problematic because clocks may not be synchronized, and that an
    elapsed-adjusted timeout shields against clock skew. The protocol says an
    omitted Timeout header means an infinite timeout, so a lost header removes
    the bound. The gRPC server cancels automatically, but the application must
    stop spawned work; Google SRE shows a hop wasting work after the client
    deadline. Bounded skew, ingress deadline requirements and outcome
    recording are Tycho guidance."
  - `binding`: the same gRPC Deadlines "Deadline Propagation" passage and
    revision `e310a0e5...`.
  - Supporting bindings: gRPC over HTTP2, record
    `read.grpc-protocol.2026-10-30`, section "Requests", "If Timeout is
    omitted a server should assume an infinite timeout.", revision
    `b51ea1b8...`; gRPC Deadlines, record
    `read.grpc-deadlines.2026-10-30`, section "Deadlines on the Server",
    "Please note that the server application is responsible ...", revision
    `e310a0e5...`; Google SRE, record
    `read.batch4-sre-cascading.2026-10-21`, section "Latency and Deadlines",
    "Had server B used deadline propagation ...", revision `d67024d5...`.
- Keep invariant and alternative states, quotes and bindings unchanged.
- `source_support`: keep the SRE main record and add auxiliary records for
  `read.grpc-deadlines.2026-10-30` (revision `e310a0e5...`) and
  `read.grpc-protocol.2026-10-30` (revision `b51ea1b8...`).
- Set `technical_coverage` to `partial-bounded`; set `notes` to the
  registry notes above.
- Shared page (`deadlines-retries.md` under V02/C05):
  `bounded_entries` 0 -> 1. Keep `pattern_count` 4,
  `unit_count` 4, `dedicated_units` 4 and `decision` "deepen".
- Summary counters: `mechanism_supported` 110 -> 111;
  `failure_recovery_supported` 62 -> 63; `technical_partial_bounded`
  19 -> 20; `technical_partial` 79 -> 78. No other counter changes.

### Card registration `edition/patterns/card-batches.v1.json`

Add `card_path`:
`book/volumes/v11-pattern-atlas/c07-resilience/README.md` to the
`tycho.pattern.deadline-propagation` entry. This is the same file as the
chapter, not a split. Without it, `preflight_sufficient.py` reports
`card_path missing or absent`. Keep `ledger_record`
`read.batch4-sre-cascading.2026-10-21`.

### Content revisions `edition/content-revisions.json`

Add one issue-540 revision with `authorized_at` 2026-10-30 and authorization
"B34 deadline-propagation mechanism and failure/recovery source binding; no
promotion or owner acceptance." The historical-view hashes are:

- Owner path previous `f8cc5a52...` (migration baseline), current
  `1c5f5588...`.
- Card path previous `539ad3a2...` (migration baseline), current
  `281886de...`.

Leave `source_blocks`, `enrichment_documents`, `enrichment_additions` and
`enrichment_baselines` empty. The owner page is retained and no split is
performed. These are historical-view hashes, not the raw file hashes in the
Book edits section.

### Derived artifacts

The book edit changes one canonical page and one atlas chapter. The source
register gains two records, so regenerate `sources/CATALOG.md` (scratch count
293). The card and registry changes make the route index, atlas registry hash,
edition inventory and related coverage/census/reverse-map artifacts stale.
Those are derived-hash refreshes for batch end; do not treat a stale derived
hash as a lane content failure.

The 2026-10-27 external review recorded in
`edition/patterns/sufficient-candidates.v1.json` predates this edit and no
longer covers the changed owner page or card bytes. The book/atlas independent
review gate applies; do not update the recorded hash without a fresh review.
The prior review is historical evidence, not acceptance of this lane.

## Validation

Checker output in the lane worktree after the two book edits:

    PASS: V11 prose <=100; 145 exact owner-link exceptions
    PASS: configured lexical boundary checks; independent-origin review still
    required.

Targeted validator results with the book edits only, in the lane worktree:

- `python3 scripts/check_markdown_line_length.py` — PASS.
- `python3 scripts/check_boundary.py` — PASS.
- `python3 scripts/validate_pattern_owner_units.py` — FAIL
  `owner-units-quote-not-verbatim: tycho.pattern.deadline-propagation:
  failure_recovery` because the metadata still carries the old failure quote;
  integrator work.
- `python3 scripts/preflight_sufficient.py --pattern
  tycho.pattern.deadline-propagation` — FAIL: mechanism and failure/recovery
  still partial, card_path missing; integrator metadata work.

In the detached scratch copy with the metadata patch above:

    PASS: tycho.pattern.deadline-propagation
    1/1 entries preflight clean

    PASS: owner units 145 entries, 145 units, 30 shared pages
    PASS: pattern registry 145 entries, 11 families
    PASS: pattern cards 11 batch(es), 145 entries
    PASS: source plan 145 entries; 208 read; 172 ledger records
    PASS: 293 source records, mandatory IDs, cross-references and catalogue
    freshness
    PASS: 487 documents, structural metadata and registry references
    PASS: directory migration; 487 canonical documents, 339 moved documents
    PASS: decomposition; 739 preserved source blocks, 174 new question pages
    PASS: enrichment; explicit membership and byte conservation

The scratch tree still fails `validate_edition.py`
(`edition-inventory-drift`) and `validate_pattern_atlas.py`
(`atlas-registry-hash`); these are derived-hash refreshes for batch end, not
lane content failures. The full unit suite is not run; batch-end tests remain
with the integrator.

## Limits

The binding uses two public gRPC representations and one public Google SRE
chapter. The gRPC guide is living documentation pinned by commit and digest;
the protocol specification is pinned by commit and digest. Google SRE describes
one absolute deadline for the request tree and then gives each hop the
remaining seconds; this lane records that tension as a Tycho reconciliation
rather than claiming the source resolves it. The sources do not test an
implementation, measure clock skew or define a numeric skew bound. Monotonic
clocks, bounded skew, ingress deadline requirements, outcome recording and
durable cleanup are labelled Tycho guidance. The `mechanism` and
`failure_recovery` states are `supported` only because the claims separate
the source-supported conversion, cancellation and omitted-header behavior from
those Tycho additions; a reviewer that requires every word to be source-quoted
should treat the dimensions as partial instead.

The card is inline in V11/C07, not V11/C02; this lane did not create a second
card. No independent AI review, owner acceptance, promotion or production
observation is claimed.

## Commit scope

The lane commit contains this note and the two book files only:

- the owner path listed under Lane coordinates;
- the card path
  `book/volumes/v11-pattern-atlas/c07-resilience/README.md`.

No shared JSON, promotion, test or generated file is in the lane commit.
