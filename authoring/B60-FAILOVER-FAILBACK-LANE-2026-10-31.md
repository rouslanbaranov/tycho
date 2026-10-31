# B60 — Failover/Failback four-dimension lane

Status: lane-local book edit, self-checked on 2026-10-31. No shared edition
metadata, promotion, generated artifact or owner acceptance is included. The
entry was 1/4 at the parent HEAD: mechanism was supported; invariant,
failure/recovery and alternative were partial. This lane binds all four
dimensions to five public units inspected on 2026-10-31: AWS Route 53
active-active and active-passive failover; Azure Site Recovery failover and
failback; PostgreSQL 17 failover and promotion; and Google SRE "Testing
Disaster". The authority-epoch rule, reconciliation order, user-journey gate
and choice rule are labelled Tycho. The task brief names an inline card at
V11/C07; the registered card is inline in the C07 landing and this lane edits
that block.

## Lane coordinates

- Parent HEAD: `f99e21e78d6239d3573f846cc1ca4e627a3e69f9` (`f99e21e7`).
- Lane label: Tycho.
- Branch: `b60-failover`; worktree:
  `/Users/rbaranov/Projects/tycho-worktrees/b60-failover`.
- Scope: the owner section `### Failover-Failback` in V08/C07, the inline
  `### Failover / Failback` card in V11/C07, and this note. Single-entry lane;
  no other entry, shared JSON, promotion or generated file is changed.
- Owner path (concatenate):

      book/volumes/v08-delivery-deployment-and-recovery/
      c07-multi-region-recovery-and-data-reconciliation/
      authority-failback.md

- Inline card path:
  `book/volumes/v11-pattern-atlas/c07-resilience/README.md`.
- Exactly three files change: the owner page, the inline card host and this
  note. The card-host change includes the chapter's evidence_scope source ids
  and notes; no shared JSON file is edited.
- Existing source ids: `src.postgresql` and `src.sre`.
- New source ids proposed: `src.aws-route53` and
  `src.azure-site-recovery`, used only by the owner and card frontmatter or
  prose until the integrator registers them.
- New ledger records proposed: five, listed below. Retained record:
  `read.batch3-pg-warm.2026-10-21`; it remains the historical PostgreSQL
  record but its revision is not reused for the current representation.
- Baseline and final line-length and boundary checks pass.

## Card location

The task brief names an inline card at V11/C07. The registry records
`atlas_owner.chapter = V11/C07`, section `failover-failback`, and the
card body is inline in the C07 chapter landing. `card-batches.v1.json`
records no `card_path` for this pattern. The C07 landing already contains
the ten card components, so this lane edits the inline block rather than
creating a dedicated page. The chapter frontmatter `evidence_scope.source_ids`
and notes are updated because they describe the cards hosted by that page; the
registry, card batches and atlas manifest are left for the integrator.
Precedent: B45, B51 and B59 edited inline card hosts and their chapter source
lists the same way.

## Baseline and gap

`edition/patterns/owner-units.v1.json` records mechanism as supported and
the other three dimensions as partial. The recorded reasons are:

- mechanism: "Defines the mechanism and its scope."
- invariant: "Local text ends at 26.2.9; 26.3 Failover content is absent."
- failure/recovery: "No failback, DNS repointing or split-authority passage."
- alternative: "No stay-on-promoted or rebuild-old-region comparison."

The base owner page is 170 lines, 1,429 words, SHA-256
`8288b0d9839df2498bb09d57feea5e80179363ce5bfa65bf381ea5b409fcfa87`.
The base owner section (lines 157-170) is 14 lines, 135 words, SHA-256
`27972c239b91ef1b0969ad990677a49438dcb561dd771f3b2ae23850eee2e9e6`.
The base chapter landing is 451 lines, 2,241 words, SHA-256
`4b857991a548afc16657e05c3b67347e600472a92140fef18c77797f2b4f0d37`.
The base card block (lines 395-425) is 31 lines, 170 words, SHA-256
`3870330dc2d0b4f0ed085f731cf3d75155fa6eff66da0e1423ae659d2d3c9fc0`.

The gap was evidential. The owner section already stated the invariants,
failure path and alternative as Tycho guidance, and the retained PostgreSQL
record supported only the mechanism while its local section text ended at
26.2.9. No exact public quote, section and representation hash were bound to
fencing the old primary, DNS-only failback, a source still writing during
failback, rebuild-as-standby or disaster-recovery verification. Shared
metadata still shows 1/4 until the integrator applies the proposals below.

## Candidate evaluation

- AWS Route 53, "Active-active and active-passive failover" (selected).
  Defines health-checked active-passive selection, the standby role, the
  weighted-record caveat and active-active operation. Primary source for the
  traffic-switch mechanism and the boundary that health routing is not data
  authority.
- Azure Site Recovery, "Run a failover from on-premises to Azure" (selected).
  Defines failover direction, recovery-point choice, drill guidance, post-
  failover validation, commit irreversibility and the reprotect prerequisite.
  Primary source for failover execution and verification gates.
- Azure Site Recovery, "Tutorial: Fail back Azure VM to the primary region"
  (selected). Defines source-VM shutdown before failback, synchronization
  completion, reprotect and delta replication. Primary source for failback as
  a new migration and the stale-source failure.
- PostgreSQL 17, "26.3. Failover" (selected). Defines standby failover,
  promotion with pg_ctl or pg_promote(), old-primary notification/STONITH,
  standby recreation and pg_rewind, and regular switching as a test. Primary
  source for promotion, fencing and the rebuild alternative.
- Google SRE, "Testing for Reliability", section "Testing Disaster" (selected).
  Defines offline disaster-recovery tool constraints (checkpoint, loadable,
  clean start), the confidence loss when constraints break, and the race
  between repair and eventually consistent behavior. Primary source for
  verification and reconciliation of divergent state.
- AWS Route 53, "Creating Amazon Route 53 health checks" was considered but not
  bound separately. It defines DNS failover in one sentence; the selected
  active/passive page carries the routing semantics and the weighted caveat.
- Azure Site Recovery, "Tutorial: Fail over Azure VMs to a secondary region" was
  considered but not bound separately. It overlaps the selected failover page;
  the selected page states the drill, validation and commit rules used here.
- PostgreSQL 17, "26.2.4. Setting Up a Standby Server" was retained historical
  evidence, not reused. Its quotation establishes that a standby can work as a
  primary after failover, but it predates the failover and STONITH material.
- Google SRE, "Data Integrity" and DiRT passages were considered but not bound
  again. B59 already binds that chapter for backup and recovery testing; this
  lane needs the disaster-recovery tool constraints and repair race, which are
  in "Testing Disaster".
- Google SRE Workbook incident-response and data-processing chapters, the AWS
  disaster-recovery whitepaper and the Azure Backup overview were considered
  but not bound. They describe drills or backup boundaries; the selected units
  support all four dimensions without duplicating those claims.
- No database, DNS record, failover, failback, reprotect or disaster exercise
  was run.

## Source units and revisions

All fetches were public HTTPS GETs on 2026-10-31. Every unit was fetched twice
and the raw bytes were identical on both fetches. Canonical text for HTML was
extracted with `scripts/source_content_hash.py`; raw HTML bytes and served
headers are recorded separately. HTTP dates are UTC and byte counts are the
downloaded response bodies.

### R1 — AWS Route 53, Active-active and active-passive failover

- Record: `read.aws-route53-failover.2026-10-31` (proposed).
- Source: `src.aws-route53` (proposed).
- URL: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-types.html
- Label/type: "Active-active and active-passive failover — Amazon Route 53
  Developer Guide"; documentation-page.
- Representation: HTTP/1.1 200 on 2026-10-31T20:11:23Z; 22,517-byte
  text/html; Last-Modified 2026-10-31T03:32:47Z; ETag
  `"oHNTDy/uLQdOXvgHdoAHjDtcasw="`; raw HTML SHA-256
  `f846542bada1f375c36dbe3258eac59e00c14e0fc641376cba249804dd4133f2`;
  canonical text 7,020 characters / 1,117 words, SHA-256
  `cbeed64d283f62bee4eea0355236fd8973f1ef114b7e2e40a75a345ef2f4f600`.
  Observed title: "Active-active and active-passive failover - Amazon Route
  53".
- Sections read: "Active-active failover"; "Active-passive failover";
  "Configuring active-passive failover with one primary and one secondary
  resource"; "Configuring active-passive failover with weighted records".
- Sections not read: the multiple-primary procedure detail, linked console
  procedures, routing-policy value pages and navigation chrome.
- Claims supported: Q1, Q3, Q4, Q13, Q20.
- Limits: DNS and health routing only; the page makes no statement about data
  authority, replication position or application consistency. No DNS record was
  changed.

### R2 — Azure Site Recovery, Run a failover from on-premises to Azure

- Record: `read.azure-asr-failover.2026-10-31` (proposed).
- Source: `src.azure-site-recovery` (proposed).
- URL: https://learn.microsoft.com/en-us/azure/site-recovery/site-recovery-failover
- Label/type: "Run a failover from on-premises to Azure — Azure Site Recovery";
  documentation-page.
- Representation: HTTP/2 200 on 2026-10-31T20:13:40Z; 61,805-byte text/html;
  Last-Modified 2026-09-27T05:07:41Z; ETag
  `"sInFmqwKtTGvW4CjqLExS+OwXEY="`; raw HTML SHA-256
  `ef1412edf0da209304f1709d69b96fc57220b1cf456d0fd05a0554cc662da8a2`;
  canonical text 10,289 characters / 1,718 words, SHA-256
  `5b1475e4cdc175e5e5285a55b28bdc92b655f7ecf7f7a5cef6a5bcda42eeccb8`.
  Observed title: "Run a Failover During Disaster Recovery With Azure Site
  Recovery - Azure Site Recovery | Microsoft Learn". The rendered page footer
  says "Last updated on 2026-09-17".
- Sections read: "Before you start"; "Run a failover"; "Track failovers";
  "Next steps".
- Sections not read: connection-preparation tables, planned failover,
  automation, IP addressing, per-platform instructions and linked pages.
- Claims supported: Q9, Q12, Q14, Q21.
- Limits: virtual-machine failover orchestration, not application write
  consistency; no Site Recovery job, recovery point or failover was run.

### R3 — Azure Site Recovery, Tutorial: Fail back Azure VM to the primary region

- Record: `read.azure-asr-failback.2026-10-31` (proposed).
- Source: `src.azure-site-recovery` (proposed).
- URL: https://learn.microsoft.com/en-us/azure/site-recovery/azure-to-azure-tutorial-failback
- Label/type: "Tutorial: Fail back Azure VM to the primary region — Azure Site
  Recovery"; documentation-page.
- Representation: HTTP/2 200 on 2026-10-31T20:13:40Z; 54,789-byte text/html;
  Last-Modified 2026-08-23T22:13:21Z; ETag
  `"Z22Pgtp2ANLMhR1Iwbs9B5lKbKo="`; raw HTML SHA-256
  `408897888573b70ebb6e63c6d9041a011bd2cd034109ac62f6e5b3a3a2a476b3`;
  canonical text 5,667 characters / 970 words, SHA-256
  `dd092294983216ac84f44d8d8a75972cb281fc59cb2f61bb1db0cba60f28eb71`.
  Observed title: "Tutorial to fail back Azure VMs to a primary region during
  disaster recovery with Azure Site Recovery. - Azure Site Recovery |
  Microsoft Learn". The rendered page footer says "Last updated on
  2025-02-11".
- Sections read: "Prerequisites"; "Fail back to the primary region";
  "Reprotect VMs".
- Sections not read: cleanup, next steps, the full-settings networking,
  automation and troubleshooting pages.
- Claims supported: Q7, Q8, Q11, Q19.
- Limits: a virtual-machine failback tutorial, not application-level
  reconciliation; no failback or reprotect was run.

### R4 — PostgreSQL 17, 26.3. Failover

- Record: `read.pg-failover.2026-10-31` (proposed).
- Source: `src.postgresql` (existing).
- URL: https://www.postgresql.org/docs/17/warm-standby-failover.html
- Label/type: "26.3. Failover — PostgreSQL 17 documentation";
  documentation-page.
- Representation: HTTP/2 200 on 2026-10-31T17:41:39Z; 16,566-byte text/html;
  no Last-Modified header; no ETag; raw HTML SHA-256
  `52497994cbef854ec6c5351756e5f5ac262bf0cc17fac11257ec86b767dbef87`;
  canonical text 3,944 characters / 656 words, SHA-256
  `bd1cf093ea7bef538e9bf69234da2a4ca699bd3b722198170b40be14e4167ad9`.
  Observed title: "PostgreSQL: Documentation: 17: 26.3. Failover". The page
  carries a news banner dated 2026-10-15; the banner is part of the canonical
  text and the digest pins the fetched representation, not a release tag.
- Sections read: "26.3. Failover".
- Sections not read: 26.2 standby configuration pages, 26.4 Hot Standby,
  linked sections and version archive.
- Claims supported: Q1, Q2, Q5, Q6, Q17, Q18.
- Limits: a conceptual failover page; it names pg_ctl and pg_promote() but no
  PostgreSQL cluster, promotion or replication test was run.

### R5 — Google SRE, Testing for Reliability, section Testing Disaster

- Record: `read.sre-testing-disaster.2026-10-31` (proposed).
- Source: `src.sre` (existing).
- URL: https://sre.google/sre-book/testing-reliability/
- Label/type: "Testing for Reliability — Site Reliability Engineering, section
  Testing Disaster"; book-chapter.
- Representation: HTTP/2 200 on 2026-10-31T20:13:41Z; 100,430-byte
  text/html; Last-Modified 2026-10-08T04:48:00Z; no ETag; raw HTML SHA-256
  `090d12e171de30b49c4228c54314af1f95e021c00270adcff0e5d5609c8e4c2e`;
  canonical text 55,344 characters / 8,753 words, SHA-256
  `425eb0ec229b85678058f57cb1e4bb1c7b7bacb2e10164d4313d9cf60dc2bed7`.
  Observed title: "Google SRE - Stress Testing: Build Confidence in System";
  the page H1 is "Testing for Reliability".
- Sections read: "Testing Disaster".
- Sections not read: the other chapter sections, figures, linked papers and
  the rest of the book.
- Claims supported: Q10, Q15, Q16.
- Limits: a 2017 book chapter, CC BY-NC-ND 4.0, with contextual production
  examples, not a benchmark or a current product description. No disaster
  exercise was run.

## Selected exact quotes

Quotes reproduce the served prose. Line breaks inside a quote are editorial
wrapping. Every quoted source fragment in the owner and card passed a
whitespace-normalized substring check against the named representation on
2026-10-31: 12 owner spans and 4 card spans, 16 including repeated fragments.
Tycho-labelled sentences in the book are not source quotes.

### Mechanism

- Q1, R4, "26.3. Failover":

      If the primary server fails then the standby server should begin failover procedures.

- Q2, R4, "26.3. Failover":

      To trigger failover of a log-shipping standby server, run pg_ctl promote or call pg_promote()

- Q3, R1, "Active-passive failover":

      Use an active-passive failover configuration when you want a primary resource or group
      of resources to be available the majority of the time and you want a secondary resource
      or group of resources to be on standby in case all the primary resources become
      unavailable.

- Q4, R1, "Configuring active-passive failover with one primary and one secondary resource":

      When the primary resource is unhealthy, Route 53 responds to DNS queries using the
      secondary record.

### Invariant

- Q5, R4, "26.3. Failover":

      If the primary server fails and the standby server becomes the new primary, and then the
      old primary restarts, you must have a mechanism for informing the old primary that it is
      no longer the primary.

- Q6, R4, "26.3. Failover":

      This is sometimes known as STONITH (Shoot The Other Node In The Head), which is necessary
      to avoid situations where both systems think they are the primary, which will lead to
      confusion and ultimately data loss.

- Q7, R3, "Prerequisites":

      Source region VM must be shut down before attempting a failback since, changes are synced
      from failover VM disks to the source region disks during failback.

- Q8, R3, "Fail back to the primary region":

      On the VM overview page, check that the VM is healthy, and that synchronization is
      complete, before you run a failover.

- Q9, R2, "Run a failover":

      After the failover, sign into the VM to validate it.

- Q10, R5, "Testing Disaster":

      Compute a checkpoint state that is equivalent to cleanly stopping the service

### Failure and recovery

- Q11, R3, "Prerequisites":

      If the source VM is powered on then it fails and thus fails the failback operation.

- Q12, R2, "Run a failover":

      If you cancel an in-progress job, failover stops, but the VM doesn't start to replicate.
      You can't start replication again.

- Q13, R1, "Configuring active-passive failover with weighted records":

      All the records with nonzero weights must be unhealthy before Route 53 starts to respond
      to DNS queries using records that have weights of zero. This can make your web
      application or website unreliable if the last healthy resource, such as a web server,
      can't handle all the traffic when other resources are unavailable.

- Q14, R2, "Run a failover":

      When you're ready, you can commit the failover. The Commit action deletes all the
      recovery points available with the service.

- Q15, R5, "Testing Disaster":

      If any of the constraints (offline, checkpoint, loadable, barrier, or clean start) must
      be broken, it’s much harder to show confidence that the associated tool implementation
      will work at any time on short notice.

- Q16, R5, "Testing Disaster":

      One challenge you face in a distributed system is determining if normal behavior, which
      may be eventually consistent by nature, will interact badly with the repair.

- Q21, R2, "Before you start":

      Before you do a full failover, run a disaster recovery drill to ensure that everything is
      working as expected.

### Alternative

- Q17, R4, "26.3. Failover":

      To return to normal operation, a standby server must be recreated, either on the former
      primary system when it comes up, or on a third, possibly new, system.

- Q18, R4, "26.3. Failover":

      The pg_rewind utility can be used to speed up this process on large clusters.

- Q19, R3, "Reprotect VMs":

      The process sends initial data to the target location, and then replicates delta
      information for the VMs to the target.

- Q20, R1, "Active-active failover":

      In active-active failover, all the records that have the same name, the same type (such
      as A or AAAA), and the same routing policy (such as weighted or latency) are active
      unless Route 53 considers them unhealthy.

## Dimension mapping

- Mechanism. Primary: Q1, record `read.pg-failover.2026-10-31`, source
  `src.postgresql`, section "26.3. Failover", revision
  `bd1cf093ea7bef538e9bf69234da2a4ca699bd3b722198170b40be14e4167ad9`.
  Supporting: Q2 (promotion command), Q3 (active-passive standby) and Q4
  (health-based record selection). Tycho reading: health-checked DNS moves
  clients; it does not move data authority, replication position or accepted
  operation history.
- Invariant. Primary: Q6, record `read.pg-failover.2026-10-31`, source
  `src.postgresql`, section "26.3. Failover", revision
  `bd1cf093ea7bef538e9bf69234da2a4ca699bd3b722198170b40be14e4167ad9`.
  Supporting: Q5 (old-primary notification), Q7 (source shutdown), Q8
  (synchronization complete), Q9 (validation sign-in) and Q10 (checkpoint
  state). Tycho rule: record an authority epoch, fencing evidence and a
  reconciled operation ledger before routing; a green health check is not
  fencing.
- Failure and recovery. Primary: Q4, record
  `read.aws-route53-failover.2026-10-31`, source `src.aws-route53`,
  section "Configuring active-passive failover with one primary and one
  secondary resource", revision
  `cbeed64d283f62bee4eea0355236fd8973f1ef114b7e2e40a75a345ef2f4f600`.
  Supporting: Q13 (weighted-record unreliability), Q11 (powered-on source
  fails failback), Q6 (two primaries and data loss), Q12 (cancelled failover
  cannot resume replication), Q14 (commit deletes recovery points), Q15
  (broken offline constraints), Q16 (repair race with eventual consistency)
  and Q21 (drill). Tycho runbook: keep the old writer fenced, reconcile
  accepted and unknown operations, verify a real user journey, and record the
  achieved RPO/RTO and any loss before declaring recovery.
- Alternative. Primary: Q17, record `read.pg-failover.2026-10-31`, source
  `src.postgresql`, section "26.3. Failover", revision
  `bd1cf093ea7bef538e9bf69234da2a4ca699bd3b722198170b40be14e4167ad9`.
  Supporting: Q18 (pg_rewind), Q19 (reprotect delta) and Q20 (active-active
  operation). Tycho choice rule: failback is a new migration, not a rollback;
  if fencing or reconciliation evidence is incomplete, keep serving from the
  promoted region and rebuild the old region as a standby instead.

## Book edits

- Owner page (concatenate):

      book/volumes/v08-delivery-deployment-and-recovery/
      c07-multi-region-recovery-and-data-reconciliation/
      authority-failback.md

  - Frontmatter adds `src.postgresql`, `src.sre`, proposed
    `src.aws-route53` and proposed `src.azure-site-recovery`;
    `evidence_scope.notes` records the five-unit binding;
    `content_review` becomes self-checked with reviewer "Automated authoring
    agent"; `updated_at` and `source_inspection_date` become 2026-10-31.
  - The owner section gains four labelled paragraphs (mechanism, invariant,
    failure/recovery, alternative), a limits paragraph and a bound-source-
    limits paragraph. The Tycho rules are labelled in the paragraphs.
  - Page 231 lines; 1,993 words; owner heading line 166.
  - Section: 66 lines, 667 words, SHA-256
    `e120c3f48c694f7e7aae1315e3bcbbe38d127dd2bdc2506e6df5e92078130c4e`.
  - Page SHA-256:
    `91739f4ddd4177ba55158f9efe99422eb3d7797dabf2ef7908b753b14452f059`.
- Inline card:
  `book/volumes/v11-pattern-atlas/c07-resilience/README.md`.
  - Chapter frontmatter adds proposed `src.aws-route53` and
    `src.azure-site-recovery` to `evidence_scope.source_ids`; the notes
    now record that Failover/Failback binds all four dimensions.
  - The inline card expands "Good-fit conditions", "Hard contraindications",
    "Competing alternative", "Failure and recovery" and "Sources" with the
    same bindings and revisions; the owner link, decision state and related
    entries are unchanged.
  - Card heading line 399; chapter 482 lines; 2,576 words.
  - Card block (heading through related entries): 58 lines, 473 words, SHA-256
    `a11a9a68605723d858387ce71b53e7bb392ac956cb43fa96fcf0ffc9001aa534`.
  - Chapter SHA-256:
    `ddcf43c54fcb9941da7b9794cc44c9239a6f72783cba7361dd1e49c4bde6e3fc`.
- No other book file, edition JSON, promotion or generated file is changed.

## Metadata needs (integrator)

The following changes are not in the lane commit. They are required before the
owner unit can move to 4/4 supported and before atlas hash checks pass.

### Source register sources/register.json

Set `updated` to 2026-10-31; source count moves 326 to 328.

- Update `src.postgresql`: reading status
  `full-public-page-inspected`; access_checked and content_verified
  2026-10-31; version note names the PostgreSQL 17 26.3 Failover unit, URL
  https://www.postgresql.org/docs/17/warm-standby-failover.html, 16,566-byte
  HTML, no Last-Modified or ETag, raw SHA-256 `52497994...`, canonical text
  3,944 characters / 656 words, SHA-256 `bd1cf093...`, HTTP Date
  2026-10-31T17:41:39Z and two byte-identical fetches; verification scope names
  standby failover, pg_ctl/pg_promote() promotion, old-primary notification and
  STONITH, standby recreation and pg_rewind, and regular switching as a test.
  No PostgreSQL cluster or promotion was run.
- Update `src.sre`: reading status `full-public-page-inspected`;
  access_checked and content_verified 2026-10-31; version note names the
  Testing for Reliability chapter, URL
  https://sre.google/sre-book/testing-reliability/, 100,430-byte HTML,
  Last-Modified 2026-10-08T04:48:00Z, no ETag, raw SHA-256 `090d12e1...`,
  canonical text 55,344 characters / 8,753 words, SHA-256 `425eb0ec...`,
  HTTP Date 2026-10-31T20:13:41Z and two byte-identical fetches; verification
  scope names the Testing Disaster section, offline checkpoint/loadable/clean-
  start constraints, broken-constraint confidence and the repair race with
  eventual consistency. No disaster exercise was run.
- Add `src.aws-route53`: title "Active-active and active-passive failover";
  publisher "Amazon Web Services"; kind `official-docs`; URL
  https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-types.html;
  topics failover, DNS and disaster recovery; priority supporting; admission
  `admitted-for-research`; access `public-web-or-author-download`;
  reading status `full-public-page-inspected`; version note pins the
  22,517-byte body, Last-Modified 2026-10-31T03:32:47Z, ETag
  `"oHNTDy/uLQdOXvgHdoAHjDtcasw="`, raw SHA-256 `f846542b...`,
  canonical 7,020 characters / 1,117 words and SHA-256 `cbeed64d...`,
  HTTP Date 2026-10-31T20:11:23Z and two byte-identical fetches; access and
  content-verified dates 2026-10-31; license note "Public documentation; cite
  short excerpts and paraphrase; do not mirror."; observed title
  "Active-active and active-passive failover - Amazon Route 53"; verification
  scope names active/active and active/passive routing, standby selection and
  the weighted-record caveat. No DNS change was made.
- Add `src.azure-site-recovery`: title "Azure Site Recovery failover and
  failback"; publisher "Microsoft"; kind `official-docs`; URL
  https://learn.microsoft.com/en-us/azure/site-recovery/site-recovery-failover;
  topics disaster recovery, failover, failback and virtual machines; priority
  supporting; admission `admitted-for-research`; access
  `public-web-or-author-download`; reading status
  `full-public-page-inspected`; version note names both ASR units, with the
  failover page's 61,805-byte body, Last-Modified 2026-09-27T05:07:41Z, ETag
  `"sInFmqwKtTGvW4CjqLExS+OwXEY="`, raw SHA-256 `ef1412ed...`,
  canonical 10,289 characters / 1,718 words and SHA-256 `5b1475e4...`,
  plus the failback page's 54,789-byte body, Last-Modified
  2026-08-23T22:13:21Z, ETag `"Z22Pgtp2ANLMhR1Iwbs9B5lKbKo="`, raw
  SHA-256 `40889788...`, canonical 5,667 characters / 970 words and
  SHA-256 `dd092294...`; HTTP Dates 2026-10-31T20:13:40Z and two
  byte-identical fetches per page; access and content-verified dates
  2026-10-31; license note "Public documentation; cite short excerpts and
  paraphrase; do not mirror."; observed titles as recorded in R2 and R3;
  verification scope names recovery points, drill, validate, commit, source
  shutdown, synchronization, reprotect and delta replication. No Site Recovery
  job was run.

### Reading ledger edition/patterns/reading-ledger.v1.json

Add five records; records move 286 to 291. Each is status `read`, reviewer
"Automated authoring agent", access_date 2026-10-31 and uses the URL, label,
content_sha256, sections and limitations in R1-R5. R1 uses source_id
`src.aws-route53`; R2 and R3 use `src.azure-site-recovery`; R4 uses
`src.postgresql`; R5 uses `src.sre`. The retained
`read.batch3-pg-warm.2026-10-21` stays unchanged as historical evidence.

### Source plan edition/patterns/source-plan.v1.json

Replace the existing PostgreSQL "Log-Shipping Standby Servers" unit with R4
and append four units for R1, R2, R3 and R5 in record order. Every unit is
status `read` and `blocked_reason` null. Replace the entry notes with
"Four dimensions bound 2026-10-31 to five public units: AWS Route 53
failover routing, Azure Site Recovery failover and failback, PostgreSQL 17
promotion, and Google SRE disaster recovery testing. No runtime test or
sufficiency claim." Summary counters: required_units 329 to 334, read_units 328
to 333, ledger_records 286 to 291; planned_units 0 and blocked_units 1 stay
unchanged.

### Owner units edition/patterns/owner-units.v1.json

For `tycho.pattern.failover-failback`:

- owner.line: 157 to 166.
- mechanism: keep state supported and keep the quote "Failover moves authority
  from region A to a surviving region B under an explicit decision; failback is
  a second migration from B back to A, not the inverse operation."; update the
  primary binding to `read.pg-failover.2026-10-31`, source
  `src.postgresql`, section "26.3. Failover", quote Q1, revision
  `bd1cf093ea7bef538e9bf69234da2a4ca699bd3b722198170b40be14e4167ad9`;
  add supporting bindings Q2 (promotion command), Q3 (active-passive standby)
  and Q4 (health-based selection). Reason: PostgreSQL defines standby failover
  and promotion; Route 53 defines the traffic-level switch.
- invariant: set state supported; keep the quote "Quarantine A, reconcile any
  divergent writes under one selected authority, verify user journeys, then
  reintroduce A as a replica or standby before considering promotion."; primary
  binding Q6, source `src.postgresql`, record
  `read.pg-failover.2026-10-31`, section "26.3. Failover", revision
  `bd1cf093ea7bef538e9bf69234da2a4ca699bd3b722198170b40be14e4167ad9`;
  add supporting bindings Q5, Q7, Q8, Q9 and Q10. Reason: PostgreSQL requires
  old-primary notification and STONITH to avoid two primaries, Azure Site
  Recovery requires source shutdown and synchronization, and Google SRE
  requires a loadable checkpoint; the authority-epoch and reconciliation rules
  are Tycho.
- failure_recovery: set state supported; keep the quote "A failback that merely
  points DNS back can resurrect stale writes and split authority."; primary
  binding Q4, source `src.aws-route53`, record
  `read.aws-route53-failover.2026-10-31`, section "Configuring
  active-passive failover with one primary and one secondary resource",
  revision
  `cbeed64d283f62bee4eea0355236fd8973f1ef114b7e2e40a75a345ef2f4f600`;
  add supporting bindings Q13, Q11, Q6, Q12, Q14, Q15, Q16 and Q21. Reason:
  Route 53 routes on health, not authority; PostgreSQL records data loss when
  two primaries remain; Azure Site Recovery fails failback when the source is
  still powered on and cannot resume replication after a cancelled failover;
  Google SRE warns about broken offline constraints and repair races; the
  runbook order is Tycho.
- alternative: set state supported; keep the quote "Stay on the promoted region
  and rebuild the old region as a standby when failback risk exceeds its
  benefit."; primary binding Q17, source `src.postgresql`, record
  `read.pg-failover.2026-10-31`, section "26.3. Failover", revision
  `bd1cf093ea7bef538e9bf69234da2a4ca699bd3b722198170b40be14e4167ad9`;
  add supporting bindings Q18, Q19 and Q20. Reason: PostgreSQL requires
  standby recreation and names pg_rewind, Azure Site Recovery reprotects with
  delta replication, and Route 53 documents active-active operation; the choice
  rule is Tycho.
- technical_coverage: partial to partial-bounded; decision_coverage stays
  partial-bounded.
- source_support: primary `read.pg-failover.2026-10-31` with auxiliary
  R1, R2, R3 and R5 and the retained old record; notes name the 2026-10-31
  binding.
- Counters: invariant_supported 90 to 91; failure_recovery_supported 85 to 86;
  alternative_supported 90 to 91; mechanism_supported stays 123;
  technical_partial_bounded 15 to 16; technical_partial 57 to 56;
  technical_sufficient 73 stays; decision counters unchanged.

### Registry edition/patterns/registry.v1.json

Replace the single PostgreSQL source unit with the five units R1-R5 and status
`read`; set technical_owner state partial to partial-bounded; coverage
technical partial to partial-bounded and overall partial to partial-bounded;
decision stays partial-bounded; update notes.

### Card batches edition/patterns/card-batches.v1.json

Update the `ledger_record` for
`tycho.pattern.failover-failback` from
`read.batch3-pg-warm.2026-10-21` to `read.pg-failover.2026-10-31`;
`owner_path` and `owner_anchor` stay unchanged; no `card_path` is
added because the card remains inline.

### Other shared metadata

- Registry, card and owner frontmatter: the lane already declares the proposed
  ids; the current `validate_book_metadata.py` "unknown source ID" failure
  is expected until the register includes `src.aws-route53` and
  `src.azure-site-recovery`.
- coverage-map, sufficient-candidates, sufficient-review-records,
  atlas-manifest (`registry_sha256`), content-revisions (owner page and
  chapter historical-view hashes), inventory, page-census, route and section
  indexes, qrels and delivery-evidence: usual recomputation. The existing
  sufficient-candidates review record pins old page hashes and is stale for
  this edit; it cannot be treated as a review pass.
- The owner page's claim_ids stay empty; no claim registry is introduced.

## Validation

- `python3 scripts/check_markdown_line_length.py`: PASS; V11 prose at most
  100 characters, 145 exact owner-link exceptions. Every new owner and lane
  note line is at most 100 characters.
- `python3 scripts/check_boundary.py`: PASS; independent-origin review
  remains required.
- `python3 scripts/validate_pattern_cards.py`: PASS; 11 batches, 145
  entries. The card keeps the retained record citation so the shared
  card-batches record remains cited.
- `python3 scripts/validate_pattern_registry.py`: PASS; 145 entries, 11
  families.
- `python3 scripts/validate_pattern_owner_units.py`: FAIL
  "owner-units-unit-ambiguous: Failover-Failback". The shared record still
  pins owner heading line 157; the edited heading is line 166. Expected until
  the integrator applies the line update above.
- `python3 scripts/validate_book_metadata.py`: FAIL "unknown source ID" for
  the proposed `src.aws-route53` and `src.azure-site-recovery`;
  expected until the integrator registers them.
- `python3 scripts/validate_edition.py`: FAIL
  "directory-baseline-payload-drift". The changed owner page needs a
  content-revisions entry before this baseline check can pass; no shared JSON
  is edited by this lane.
- `python3 scripts/validate_directory_migration.py`: FAIL with the same
  "directory-baseline-payload-drift" condition and the same integration need.
- `python3 scripts/validate_pattern_atlas.py`: FAIL "atlas-document-sha".
  The edited V11/C07 chapter no longer matches the hash pinned in the atlas
  manifest and semantic audit; expected until the integrator refreshes those
  shared records.
- `python3 scripts/validate_book_navigation.py`: FAIL with four unchanged
  missing local anchors in dark-launching-shadow-traffic.md and rbac-abac.md;
  neither file is touched by this lane. The same four issues were recorded in
  the B50, B51 and B59 integration notes.
- `python3 scripts/preflight_sufficient.py --pattern
  tycho.pattern.failover-failback`: FAIL as expected without shared
  metadata; it reports invariant, failure_recovery and alternative still
  partial and no card_path. Inline cards without a dedicated path fail the
  same card_path check; Backup/PITR and other inline cards show the same
  pre-existing condition.
- Quotes: 12 owner spans and 4 card spans passed a whitespace-normalized
  substring check against the five representations. Tycho-labelled sentences
  are not counted.
- `git diff --check`: no whitespace errors.
- Raw SHA-256 after the book edits: owner page
  `91739f4ddd4177ba55158f9efe99422eb3d7797dabf2ef7908b753b14452f059`;
  chapter `ddcf43c54fcb9941da7b9794cc44c9239a6f72783cba7361dd1e49c4bde6e3fc`.
- The lane note has no tab characters and every line is at most 100
  characters.

## Limits

- Shared metadata is not updated. The generated owner units, registry, source
  plan, ledger, card batches and indexes still show the entry as 1/4 or partial
  until an integrator applies the proposals above.
- No promotion, owner acceptance, coverage sufficiency or independent AI
  review is claimed. The book/atlas review gate remains outstanding; the
  existing review hashes are stale for the edited pages.
- No database, DNS record, failover, failback, reprotect, Site Recovery job,
  benchmark or production observation was run. The PostgreSQL, AWS, Azure and
  SRE claims are source statements, not local measurements.
- The PostgreSQL page is living documentation with no Last-Modified header and
  a news banner; the AWS and Azure pages are living documentation with
  Last-Modified timestamps; the SRE chapter is a 2017 book chapter with a
  2026-10-08 page timestamp. Re-fetches must compare the canonical digest
  before reusing a quote.
- The retained PostgreSQL record's revision
  `b89009fc548105bdd0d9f820d09f40a135b3595b9079a6034e066255c31fc09f`
  differs from the fresh digest; the mismatch is recorded rather than resolved
  by assumption.
- Route 53 and Azure Site Recovery describe traffic and VM orchestration, not
  application write reconciliation. The link from DNS-only failback to stale
  writes and split authority is Tycho inference, explicitly labelled; the
  sources support only the routing, fencing and synchronization facts cited.
- The card is inline because that is the registered layout; the task brief's
  "inline card" wording matches the repository structure. No dedicated card
  path exists in card-batches for this pattern.
- The chapter notes and source-id list are edited with the inline card. Other
  chapter metadata, atlas hashes and generation outputs remain for the
  integrator.
