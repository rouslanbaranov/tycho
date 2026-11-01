# B59 — Backup, PITR and restore four-dimension lane

Status: lane-local book edit, self-checked on 2026-10-31. No shared edition
metadata, promotion, generated artifact or owner acceptance is included. The
entry was 1/4 at the parent HEAD: mechanism was supported; invariant,
failure/recovery and alternative were partial. This lane binds all four
dimensions to five public units inspected on 2026-10-31: PostgreSQL 17
continuous archiving/PITR; the AWS Backup overview and restore-testing pages;
the Azure Backup overview; and Google SRE "Data Integrity: What You Read Is
What You Wrote". The chain-completeness check, application-validation rule,
runbook order and choice rule are labelled Tycho. The task brief names an
inline card at V11/C06; the registered card is inline in the C06 landing and
this lane edits that block.

## Lane coordinates

- Parent HEAD: `b4b66090994486785f6033f34b899aeb1c7148fd` (`b4b66090`).
- Lane label: Tycho.
- Branch: `b59-backup`; worktree:
  `/Users/rbaranov/Projects/tycho-worktrees/b59-backup`.
- Scope: the owner section `### Backup, PITR and Restore` in V05/C07, the
  inline `### Backup, PITR and Restore` card in V11/C06, and this note.
  Single-entry lane; no other entry, shared JSON, promotion or generated file
  is changed.
- Owner path (concatenate):

      book/volumes/v05-data-models-engines-and-lifecycle/
      c07-replication-backups-and-restore-drills/
      backup-restore-pitr-and-recovery-drills.md

- Inline card path:
  `book/volumes/v11-pattern-atlas/c06-database-storage/README.md`.
- Exactly three files change: the owner page, the inline card host and this
  note. The card-host change includes the chapter's evidence_scope source ids
  and the one-line chapter summary; no shared JSON file is edited.
- Existing source id: `src.postgresql` and `src.sre`.
- New source ids proposed: `src.aws-backup` and `src.azure-backup`, used
  only by the owner and card frontmatter or prose until the integrator
  registers them.
- New ledger records proposed: five, listed below. Retained record:
  `read.batch3-pg-archiving.2026-10-21`; it remains the historical PostgreSQL
  record but its revision is not reused for the current representation.
- Baseline and final line-length and boundary checks pass.

## Card location

The task brief names an inline card at V11/C06. The registry records
`atlas_owner.chapter = V11/C06`, section `backup-pitr-and-restore`, and the
card body is inline in the C06 chapter landing. `card-batches.v1.json` records
no `card_path` for this pattern. The C06 landing already contains the ten card
components, so this lane edits the inline block rather than creating a
dedicated page. The chapter frontmatter `evidence_scope.source_ids` and notes
are updated because they describe the cards hosted by that page; the registry,
card batches and atlas manifest are left for the integrator. Precedent: B45 and
B51 edited inline card hosts and their chapter source lists the same way.

## Baseline and gap

`edition/patterns/owner-units.v1.json` records mechanism as supported and the
other three dimensions as partial. The recorded reasons are:

- mechanism: "Defines a base backup plus archived WAL restored to a chosen
  point in time."
- invariant: "External review 2026-10-27: binding does not support the full
  owner claim."
- failure/recovery: the same reason string.
- alternative: the same reason string.

The base owner page is 105 lines, 615 words, SHA-256
`d6e6ffece4259cbc5472dc3c5c92eed7a5ed14abf518cb58bc2760cd48b9eaee`.
The base owner section (lines 91-105) is 15 lines, 132 words, SHA-256
`5f4d2d5df013047d1cb0b4647a07f0af1e18a54ae562dd0eef2b357046cdf0f3`.
The base chapter landing is 351 lines, 1,559 words, SHA-256
`cec0559914457314e578715d7e03f69e12ad5493e859478c9f5eced4cf3a63aa`.
The base card block (lines 294-324) is 31 lines, 150 words, SHA-256
`850a0ea54e79cfa5e28f96514ffc3b2392a5095c1dbc67d8c43f08057020c6a9`.

The gap was evidential: the owner section already stated the invariants,
failure path and alternative as Tycho guidance, and the PostgreSQL unit
supported only the mechanism. No exact public quote, section and
representation hash were bound to chain completeness, a validated recovery
target, a corrupt or missing segment, restore drills or the replica-versus-
backup alternative. Shared metadata still shows 1/4 until the integrator
applies the proposals below.

## Candidate evaluation

- PostgreSQL 17, "Continuous Archiving and Point-in-Time Recovery (PITR)"
  (selected). Defines a base backup plus archived WAL, requires a continuous
  WAL sequence, permits a stop point by time, named restore point or
  transaction ID, and records corrupt-WAL and inaccessible-archive recovery
  behaviour. Primary source for mechanism, chain completeness and segment
  failure.
- AWS Backup, "What is AWS Backup?" (selected). Defines centralized,
  policy-based backup management, cross-Region copies and backup activity
  monitoring. Primary source for managed policy centralization and the
  cross-Region copy alternative.
- AWS Backup, "Restore testing" (selected). Defines automated and periodic
  restore viability evaluation, restore job duration monitoring and
  compliance evidence from restore tests. Primary source for restore drills
  and the validated restore result.
- Azure Backup, "What is the Azure Backup service?" (selected). Defines
  policy-based backup and restore, protection from deletion, corruption and
  ransomware, soft delete, immutable recovery points, and the boundary
  between backup and Site Recovery failover orchestration. Primary source for
  immutable recovery points and the availability-versus-history alternative.
- Google SRE, "Data Integrity: What You Read Is What You Wrote" (selected).
  Distinguishes backups from archives, records that replication and redundancy
  are not recoverability, requires continuous recovery testing, and describes
  a DiRT exercise. Primary source for restore drills and the replication
  alternative.
- PostgreSQL 17 "Backup and Restore" chapter was considered but not bound as
  a separate unit: the continuous-archiving page states the chain and recovery
  rules used here, and a second PostgreSQL unit would duplicate the same
  claims without adding a dimension.
- AWS "Disaster Recovery of Workloads on AWS" whitepaper, Azure Site Recovery
  and the SRE Workbook incident-response chapter were considered but not
  bound. They describe broader regional failover or incident practice; the
  four dimensions are supported by the selected units. Azure Site Recovery is
  named only through the Azure Backup boundary statement.
- AWS Backup Audit Manager, AWS Backup vault-lock material and Azure Backup
  soft-delete detail pages were considered but not bound separately. The
  overview pages state the selected claims at the required depth.
- Retained `read.batch3-pg-archiving.2026-10-21` used
  `/docs/current/` and revision
  `0c5f4cb3a63b500ad55966358d7ae0253939fd650daca3083b9ff413358ee31f`.
  The 2026-10-31 PostgreSQL 17 representation yields canonical digest
  `3aeddd67e051548889c4ee59e3a056378d0df53d772ef47f9072b22631216b76`.
  The digests differ; the retained record is historical evidence and is not
  treated as the current page representation.
- No database, backup set, archive, restore, failover or disaster exercise was
  run.

## Source units and revisions

All fetches were public HTTPS GETs on 2026-10-31. Every unit was fetched
twice and the raw bytes were identical on both fetches. Canonical text for
HTML was extracted with `scripts/source_content_hash.py`; raw HTML bytes and
served headers are recorded separately. HTTP dates are UTC and byte counts are
the downloaded response bodies.

### R1 — PostgreSQL 17, Continuous Archiving and PITR

- Record: `read.pg-pitr.2026-10-31` (proposed).
- Source: `src.postgresql` (existing).
- URL: https://www.postgresql.org/docs/17/continuous-archiving.html
- Label/type: "Continuous Archiving and Point-in-Time Recovery (PITR) —
  PostgreSQL 17 documentation"; documentation-page.
- Representation: HTTP/2 200 on 2026-10-31T13:39:38Z; 75,080-byte text/html;
  no Last-Modified header; no ETag; raw HTML SHA-256
  `67d74dba3e22345bfb9d9205bb9177a5fc9326b4d9c7977d6678fe602c4882f2`;
  canonical text 43,672 characters / 7,303 words, SHA-256
  `3aeddd67e051548889c4ee59e3a056378d0df53d772ef47f9072b22631216b76`.
  Observed title: "PostgreSQL: Documentation: 17: 25.3. Continuous Archiving
  and Point-in-Time Recovery (PITR)". The page carries a news banner dated
  2026-10-15; the news banner is part of the canonical text and the digest
  pins the fetched representation, not a release tag.
- Sections read: "25.3. Continuous Archiving and PITR";
  "25.3.1. Setting Up WAL Archiving"; "25.3.2. Making a Base Backup";
  "25.3.3. Making an Incremental Backup"; "25.3.4. Making a Base Backup Using
  the Low Level API"; "25.3.4.1. Backing Up the Data Directory";
  "25.3.5. Recovering Using a Continuous Archive Backup"; "25.3.6. Timelines";
  "25.3.7. Tips and Examples"; "25.3.7.1. Standalone Hot Backups";
  "25.3.7.2. Compressed Archive Logs"; "25.3.7.3. archive_command Scripts";
  "25.3.8. Caveats".
- Sections not read: linked child pages, the version archive, navigation and
  unrelated chrome; examples were not reproduced.
- Claims supported: Q1, Q2, Q3, Q5, Q7, Q8.
- Limits: one documentation page; the page gives no RPO/RTO values and no
  deployment drill evidence. No restore was executed.

### R2 — AWS Backup, What is AWS Backup?

- Record: `read.aws-backup.2026-10-31` (proposed).
- Source: `src.aws-backup` (proposed).
- URL: https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html
- Label/type: "What is AWS Backup? — AWS Backup Developer Guide";
  documentation-page.
- Representation: HTTP/1.1 200 on 2026-10-31T19:41:32Z; 32,867-byte text/html;
  Last-Modified 2026-10-31T03:36:35Z; ETag
  `"R67di9+YX7VPCoLjD3Ib76bA+hY="`; raw HTML SHA-256
  `78a255fb80d0377a14cec1b5dd3fc0740597e4bdd91e3eb5e9dd4661da56ef0d`;
  canonical text 13,450 characters / 2,097 words, SHA-256
  `edbc0b590a3be072a14ec7fa65a527bd02f360efd56e75bb2c96f09c65817aca`.
  Observed title: "What is AWS Backup? - AWS Backup".
- Sections read: "What is AWS Backup?"; "Feature overview"; "Centralized
  backup management"; "Policy-based backup"; "Cross-Region backup"; "Backup
  activity monitoring"; "Secure your data in backup vaults".
- Sections not read: service-specific backup pages, pricing detail, quotas,
  linked API references and console procedures.
- Claims supported: Q6, Q19.
- Limits: service overview; no AWS account, backup plan, vault, copy job or
  restore was created.

### R3 — AWS Backup, Restore testing

- Record: `read.aws-backup-restore-testing.2026-10-31` (proposed).
- Source: `src.aws-backup` (proposed).
- URL: https://docs.aws.amazon.com/aws-backup/latest/devguide/restore-testing.html
- Label/type: "Restore testing — AWS Backup Developer Guide";
  documentation-page.
- Representation: HTTP/1.1 200 on 2026-10-31T19:40:33Z; 64,992-byte text/html;
  Last-Modified 2026-10-31T03:36:36Z; ETag
  `"noWl4i/Rxa3AwOroZaFIFOgksEo="`; raw HTML SHA-256
  `d252c4f53418e6b7e678c783bbe4336e18916e364a8ecc1986bbab16b9cf8aa8`;
  canonical text 26,247 characters / 4,150 words, SHA-256
  `8a0be467ae54c840fc0bdbab5b5aed4a2620bd3564f988d48b648c5dc475078f`.
  Observed title: "Restore testing - AWS Backup".
- Sections read: "Overview"; "Restore testing compared with restore process";
  "Restore testing management"; "Restore testing validation"; "Audit restore
  testing"; "Restore testing quotas and parameters".
- Sections not read: console walkthroughs, CLI command references, inferred
  metadata detail, troubleshooting and quotas tables.
- Claims supported: Q9, Q10, Q21.
- Limits: feature documentation; no testing plan, restore job, validation or
  compliance evaluation was run.

### R4 — Azure Backup, What is the Azure Backup service?

- Record: `read.azure-backup.2026-10-31` (proposed).
- Source: `src.azure-backup` (proposed).
- URL: https://learn.microsoft.com/en-us/azure/backup/backup-overview
- Label/type: "What is the Azure Backup service? — Microsoft Learn";
  documentation-page.
- Representation: HTTP/2 200 on 2026-10-31T19:41:32Z; 61,791-byte text/html;
  Last-Modified 2026-09-30T08:26:14Z; ETag
  `"EwmgQgbaPpygrNXJ2SWAfV/oTtQ="`; raw HTML SHA-256
  `24d36fba16d76fb419fae9113891160471dce476e01bd813f5b212419b3a2400`;
  canonical text 10,814 characters / 1,644 words, SHA-256
  `628a67342bd04649ae9367d502aa6980a344ffcfbb88a900fff736ae8faf5df6`.
  Observed title: "What is Azure Backup? - Azure Backup | Microsoft Learn".
  The rendered page footer says "Last updated on 2026-09-16".
- Sections read: "What is the Azure Backup service?"; "When to use Azure
  Backup"; "What can I back up?"; "How Azure Backup works"; "Key components
  in Azure Backup"; "Why use Azure Backup?"; "Security and ransomware
  protection by Azure Backup"; "Design considerations for workload
  protection".
- Sections not read: per-workload backup articles, vault architecture detail,
  backup types and tiers, pricing and linked tutorials.
- Claims supported: Q4, Q14, Q15, Q18.
- Limits: service overview; no vault, policy, recovery point or restore was
  created.

### R5 — Google SRE, Data Integrity

- Record: `read.sre-data-integrity.2026-10-31` (proposed).
- Source: `src.sre` (existing).
- URL: https://sre.google/sre-book/data-integrity/
- Label/type: "Data Integrity: What You Read Is What You Wrote — Site
  Reliability Engineering"; book-chapter.
- Representation: HTTP/2 200 on 2026-10-31T19:42:04Z; 129,915-byte text/html;
  Last-Modified 2026-10-08T04:48:00Z; no ETag; raw HTML SHA-256
  `b92a15e5121f9e4a8788e46edccae31ea0eb7d6d377d9493335cd878824172b2`;
  canonical text 77,403 characters / 12,240 words, SHA-256
  `8afec3878de75392885e447c8dca9d97376ea34c27d4c8959dc2b88e7d0a1f1a`.
  Observed title: "Google SRE - Data Integrity: Principles and Best
  Practices".
- Sections read: "Backups Versus Archives"; "Delivering a Recovery System,
  Rather Than a Backup System"; "Challenges of Maintaining Data Integrity Deep
  and Wide"; "Knowing That Data Recovery Will Work"; "Hope Is Not a
  Strategy"; "Conclusion".
- Sections not read: the 24 failure-mode combinations, the Gmail case study,
  validation implementation detail, linked papers and the rest of the book.
- Claims supported: Q11, Q12, Q13, Q16, Q17, Q20.
- Limits: a 2016 book chapter with contextual case studies, not a benchmark
  or a current product description. No recovery or DiRT exercise was run.

## Selected exact quotes

Quotes reproduce the served prose. Line breaks inside a quote are editorial
wrapping. Every quoted source fragment in the owner and card passed a
whitespace-normalized substring check against the named representation on
2026-10-31: 13 owner spans and 8 card spans, including repeated fragments.
Tycho-labelled sentences in the book are not source quotes.

### Mechanism

- Q1, R1, "25.3. Continuous Archiving and PITR":

      you need a continuous sequence of archived WAL files that extends back
      at least as far as the start time of your backup.

- Q2, R1, "25.3. Continuous Archiving and PITR":

      it is possible to restore the database to its state at any time since
      your base backup was taken.

### Invariant

- Q3, R1, "25.3.5. Recovering Using a Continuous Archive Backup":

      either by date/time, named restore point or by completion of a specific
      transaction ID.

- Q4, R4, "Security and ransomware protection by Azure Backup":

      Immutable backup: Locks recovery points to prevent modification or
      deletion, ensuring data integrity.

- Q5, R1, "25.3.5. Recovering Using a Continuous Archive Backup":

      as close as possible given the available WAL segments

- Q6, R2, "What is AWS Backup?":

      AWS Backup is a fully-managed service that makes it easy to centralize
      and automate data protection across AWS services, in the cloud, and on
      premises.

### Failure and recovery

- Q7, R1, "25.3.5. Recovering Using a Continuous Archive Backup":

      If recovery finds corrupted WAL data, recovery will halt at that point
      and the server will not start.

- Q8, R1, "25.3.5. Recovering Using a Continuous Archive Backup":

      If recovery fails for an external reason, such as a system crash or if
      the WAL archive has become inaccessible, then the recovery can simply be
      restarted and it will restart almost from where it failed.

- Q9, R3, "Overview":

      provides automated and periodic evaluation of restore viability, as well
      as the ability to monitor restore job duration times.

- Q10, R3, "Overview":

      After the restore test plan completes its run, you can use the results to
      show compliance for organizational or governance requirements such as
      the successful completion of restore test scenarios or the restore job
      completion time.

- Q11, R5, "Knowing That Data Recovery Will Work":

      you only know that you can recover your recent state if you actually do
      so

- Q12, R5, "Knowing That Data Recovery Will Work":

      Continuously test the recovery process as part of your normal operations

- Q13, R5, "Hope Is Not a Strategy":

      This procedure is also periodically tested by a DiRT exercise to ensure
      that we can restore users’ annotations from backups within the time set
      by the SLO.

- Q14, R4, "When to use Azure Backup":

      Protect data against accidental deletion, corruption, or ransomware

- Q15, R4, "Security and ransomware protection by Azure Backup":

      Soft delete: Retains deleted backup data for a defined period to protect
      against accidental or malicious deletion.

- Q21, R3, "Restore testing compared with restore process":

      Restore testing runs restore jobs in the same way as on-demand restores
      and uses the same recovery points (backups) as an on-demand restore.

### Alternative

- Q16, R5, "Challenges of Maintaining Data Integrity Deep and Wide":

      Replication provides many benefits, including locality of data and
      protection from a site-specific disaster, but it can’t protect you from
      many sources of data loss.

- Q17, R5, "Challenges of Maintaining Data Integrity Deep and Wide":

      Datastores that automatically sync multiple replicas guarantee that a
      corrupt database row or errant delete are pushed to all of your copies,
      likely before you can isolate the problem.

- Q18, R4, "When to use Azure Backup":

      Azure Backup focuses on data protection (backup and restore). For
      disaster recovery and failover orchestration, use Azure Site Recovery

- Q19, R2, "Cross-Region backup":

      Cross-Region backup is particularly valuable if you have business
      continuity or compliance requirements to store backups a minimum
      distance away from your production data.

- Q20, R5, "Backups Versus Archives":

      what people really want are restores

## Dimension mapping

- Mechanism. Primary: Q2, record `read.pg-pitr.2026-10-31`, section
  "25.3. Continuous Archiving and PITR", revision
  `3aeddd67e051548889c4ee59e3a056378d0df53d772ef47f9072b22631216b76`.
  Supporting: Q1 (continuous WAL sequence) and Q6 (managed centralization).
  Tycho reading: the recoverable unit is the chain, not the newest artifact.
- Invariant. Primary: Q1, record `read.pg-pitr.2026-10-31`, section
  "25.3. Continuous Archiving and PITR", revision
  `3aeddd67e051548889c4ee59e3a056378d0df53d772ef47f9072b22631216b76`.
  Supporting: Q3 (stop-point selection), Q4 (immutable recovery points),
  Q5 (available segments bound the target) and Q6 (policy centralization).
  Tycho rule: a validated target must satisfy business invariants, not merely
  be reachable.
- Failure and recovery. Primary: Q7, record `read.pg-pitr.2026-10-31`,
  section "25.3.5. Recovering Using a Continuous Archive Backup", revision
  `3aeddd67e051548889c4ee59e3a056378d0df53d772ef47f9072b22631216b76`.
  Supporting: Q8 (restart), Q5 (segment bound), Q9-Q10 and Q21 (AWS restore
  testing), Q11-Q13 (SRE continuous testing and DiRT), Q14-Q15 (Azure
  protection). Tycho runbook: isolate, restore separately, verify and record
  the achieved point before cutover.
- Alternative. Primary: Q16, record `read.sre-data-integrity.2026-10-31`,
  section "Challenges of Maintaining Data Integrity Deep and Wide", revision
  `8afec3878de75392885e447c8dca9d97376ea34c27d4c8959dc2b88e7d0a1f1a`.
  Supporting: Q17 (replicated deletion), Q18 (backup versus Site Recovery),
  Q19 (cross-Region copies) and Q20 (restores are the goal). Tycho choice
  rule: a replica serves availability; a backup chain serves historical state.

## Book edits

- Owner page (concatenate):

      book/volumes/v05-data-models-engines-and-lifecycle/
      c07-replication-backups-and-restore-drills/
      backup-restore-pitr-and-recovery-drills.md

  - Frontmatter adds `src.postgresql`, proposed `src.aws-backup` and
    `src.azure-backup`, and `src.sre`; `evidence_scope.notes` records the
    five-unit binding; `content_review` becomes `self-checked` with reviewer
    "Automated authoring agent"; `updated_at` and `source_inspection_date`
    become 2026-10-31. The draft banner says the evidence was bound on
    2026-10-31 and records a self-check.
  - The owner section gains four labelled paragraphs (mechanism, invariant,
    failure/recovery, alternative) and a bound-source-limits paragraph. The
    Tycho rules are labelled in the paragraphs.
  - Page 163 lines; 1,145 words; owner heading line 104.
  - Section: 60 lines, 619 words, SHA-256
    `f2582eb8839015f31146e411a2ee98ff26e43f082cf8900cee0115d8f7782884`.
  - Page SHA-256:
    `cbd13b0bf356b0aceee83a3e4ca69aedddb9eff3d484a3da673ab108671003f1`.
- Inline card:
  `book/volumes/v11-pattern-atlas/c06-database-storage/README.md`.
  - Chapter frontmatter adds `src.sre`, proposed `src.aws-backup` and
    `src.azure-backup` to `evidence_scope.source_ids`; the notes line now
    records that Index Table and Backup/PITR bind all four dimensions.
  - The inline card expands "Good-fit conditions", "Hard contraindications",
    "Competing alternative", "Failure and recovery" and "Sources" with the
    same bindings and revisions; the owner link, decision state and related
    entries are unchanged.
  - Card heading line 297; chapter 375 lines; 1,852 words.
  - Card block: 53 lines, 436 words, SHA-256
    `db9bc698ca7625c9ec64b24f769f1ff726c97b657a98572679a1a475616ea586`.
  - Chapter SHA-256:
    `53786669a3152f16dd640d86060215970ad6d3f3ee06580001de67e0082a0b41`.
- No other book file, edition JSON, promotion or generated file is changed.

## Metadata needs (integrator)

The following changes are not in the lane commit. They are required before the
owner unit can move to 4/4 supported and before atlas hash checks pass.

### Source register sources/register.json

Set `updated` to 2026-10-31; source count moves 324 to 326.

- Update `src.postgresql`: reading status `full-public-page-inspected`;
  access_checked and content_verified 2026-10-31; version note names the
  PostgreSQL 17 continuous-archiving unit, URL
  https://www.postgresql.org/docs/17/continuous-archiving.html, 75,080-byte
  HTML, no Last-Modified or ETag, raw SHA-256 `67d74dba...`, canonical text
  43,672 characters / 7,303 words, SHA-256 `3aeddd67...`, HTTP Date
  2026-10-31T13:39:38Z and two byte-identical fetches; verification scope
  names base backups, WAL archiving, recovery targets, corrupt-WAL halt and
  recovery restart. No database or restore was run.
- Update `src.sre`: reading status `full-public-page-inspected`;
  access_checked and content_verified 2026-10-31; version note names the
  Data Integrity chapter, URL https://sre.google/sre-book/data-integrity/,
  129,915-byte HTML, Last-Modified 2026-10-08T04:48:00Z, no ETag, raw SHA-256
  `b92a15e5...`, canonical text 77,403 characters / 12,240 words, SHA-256
  `8afec387...`, HTTP Date 2026-10-31T19:42:04Z and two byte-identical
  fetches; verification scope names backups versus archives, recovery
  testing, replication limits and DiRT. No recovery exercise was run.
- Add `src.aws-backup`: title "What is AWS Backup?"; publisher "Amazon Web
  Services"; kind `official-docs`; URL
  https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html;
  topics backup, recovery and compliance; priority supporting; admission
  `admitted-for-research`; access `public-web-or-author-download`; reading
  status `full-public-page-inspected`; version note names both AWS Backup
  units, with the overview's 32,867-byte body, Last-Modified
  2026-10-31T03:36:35Z, ETag `"R67di9+YX7VPCoLjD3Ib76bA+hY="`, raw SHA-256
  `78a255fb...`, canonical 13,450 characters / 2,097 words and SHA-256
  `edbc0b59...`, plus the restore-testing page's 64,992-byte body,
  Last-Modified 2026-10-31T03:36:36Z, ETag
  `"noWl4i/Rxa3AwOroZaFIFOgksEo="`, raw SHA-256 `d252c4f5...`, canonical
  26,247 characters / 4,150 words and SHA-256 `8a0be467...`; access and
  content-verified dates 2026-10-31; license note "Public documentation; cite
  short excerpts and paraphrase; do not mirror."; observed titles "What is AWS
  Backup? - AWS Backup" and "Restore testing - AWS Backup"; verification scope
  names centralized plans, cross-Region copies, restore testing and
  compliance results. No restore test was run.
- Add `src.azure-backup`: title "What is the Azure Backup service?";
  publisher "Microsoft"; kind `official-docs`; URL
  https://learn.microsoft.com/en-us/azure/backup/backup-overview; topics
  backup, recovery and ransomware protection; priority supporting; admission
  `admitted-for-research`; access `public-web-or-author-download`; reading
  status `full-public-page-inspected`; version note pins the 61,791-byte HTML,
  Last-Modified 2026-09-30T08:26:14Z, ETag
  `"EwmgQgbaPpygrNXJ2SWAfV/oTtQ="`, raw SHA-256 `24d36fba...`, canonical
  text 10,814 characters / 1,644 words, SHA-256 `628a6734...`, HTTP Date
  2026-10-31T19:41:32Z and two byte-identical fetches; access and
  content-verified dates 2026-10-31; license note "Public documentation; cite
  short excerpts and paraphrase; do not mirror."; observed title "What is
  Azure Backup? - Azure Backup | Microsoft Learn"; verification scope names
  policy-based backup, soft delete, immutable recovery points and the Site
  Recovery boundary. No vault or restore was created.

### Reading ledger edition/patterns/reading-ledger.v1.json

Add five records; records move 281 to 286. Each is status `read`, reviewer
"Automated authoring agent", access_date 2026-10-31 and uses the URL, label,
content_sha256, sections and limitations in R1-R5. R1 uses source_id
`src.postgresql`; R2 and R3 use `src.aws-backup`; R4 uses
`src.azure-backup`; R5 uses `src.sre`. The retained
`read.batch3-pg-archiving.2026-10-21` stays unchanged as historical evidence.

### Source plan edition/patterns/source-plan.v1.json

Replace the existing PostgreSQL unit's `read_record_id` with
`read.pg-pitr.2026-10-31`, and append four units for R2-R5 in record order.
Every new unit is status `read` and blocked_reason null. Replace the entry
notes with "Four dimensions bound 2026-10-31 to five public units: PostgreSQL
17 PITR, AWS Backup overview and restore testing, Azure Backup overview, and
Google SRE data integrity. No runtime test or sufficiency claim." Summary
counters: required_units 325 to 329, read_units 324 to 328, ledger_records
281 to 286; planned_units 0 and blocked_units 1 stay unchanged.

### Owner units edition/patterns/owner-units.v1.json

For `tycho.pattern.backup-pitr-and-restore`:

- mechanism: keep state supported and quote "A base backup plus a continuous
  archive of write-ahead records lets an operator restore the data to a
  chosen point in time before an incident."; update the primary binding to
  `read.pg-pitr.2026-10-31`, section "25.3. Continuous Archiving and PITR",
  revision
  `3aeddd67e051548889c4ee59e3a056378d0df53d772ef47f9072b22631216b76`;
  add supporting bindings Q1 and Q6. Reason: PostgreSQL defines base backup
  plus WAL replay to a target and AWS centralizes managed backup policy.
- invariant: set state supported; keep quote "The backup chain must be
  complete and restorable, and a recovery target must be validated against
  the application's consistency requirements, not only produced."; primary
  binding Q1, source `src.postgresql`, record
  `read.pg-pitr.2026-10-31`, section "25.3. Continuous Archiving and PITR",
  revision
  `3aeddd67e051548889c4ee59e3a056378d0df53d772ef47f9072b22631216b76`;
  add supporting bindings Q3-Q6. Reason: PostgreSQL requires a continuous WAL
  sequence and permits time, named-point or transaction-ID targets, Azure
  locks immutable recovery points, available segments bound the reachable
  target, and AWS centralizes policy; the application-validation rule is
  Tycho.
- failure_recovery: set state supported; keep quote "A missing or corrupt
  archive segment makes the target unreachable; run restore drills on a
  schedule and verify checksums and recovery completion."; primary binding
  Q7, source `src.postgresql`, record `read.pg-pitr.2026-10-31`, section
  "25.3.5. Recovering Using a Continuous Archive Backup", revision
  `3aeddd67e051548889c4ee59e3a056378d0df53d772ef47f9072b22631216b76`;
  add supporting bindings Q5, Q8-Q15 and Q21. Reason: PostgreSQL halts on
  corrupt WAL and can restart after an inaccessible archive, AWS restore
  testing and SRE require periodic restore tests, and Azure protects deleted
  backup data with soft delete; the runbook order is Tycho.
- alternative: set state supported; keep quote "Promote a replica for
  availability, but it does not protect against replicated deletion or
  corruption; use backups when recovery point and retained history matter.";
  primary binding Q16, source `src.sre`, record
  `read.sre-data-integrity.2026-10-31`, section "Challenges of Maintaining
  Data Integrity Deep and Wide", revision
  `8afec3878de75392885e447c8dca9d97376ea34c27d4c8959dc2b88e7d0a1f1a`;
  add supporting bindings Q17-Q20. Reason: SRE says replication is not
  recoverability and errant deletes replicate, Azure separates backup from
  Site Recovery failover, AWS copies backups across Regions, and restores are
  the goal; the choice rule is Tycho.
- technical_coverage: partial to partial-bounded; decision_coverage stays
  partial-bounded. Note: the earlier Distributed Tracing integration flipped
  technical and decision coverage to sufficient during a separate promotion
  commit; this lane does not claim a promotion or that transition.
- source_support: primary `read.pg-pitr.2026-10-31` with auxiliary R2-R5 and
  the retained old record; notes name the 2026-10-31 binding.
- Owner heading line: 91 to 104.
- Counters: invariant_supported 89 to 90; failure_recovery_supported 84 to
  85; alternative_supported 89 to 90; mechanism_supported stays 123;
  technical_partial_bounded 15 to 16; technical_partial 58 to 57;
  technical_sufficient 72 stays; decision counters unchanged.

### Other shared metadata

- Registry: replace the single PostgreSQL source unit with the five units
  R1-R5 and status read; set technical_owner state partial to
  partial-bounded; coverage technical partial to partial-bounded and overall
  partial to partial-bounded; decision stays partial-bounded; update notes.
- Card batches: update the `ledger_record` for
  `tycho.pattern.backup-pitr-and-restore` from
  `read.batch3-pg-archiving.2026-10-21` to `read.pg-pitr.2026-10-31`;
  `owner_path` and `owner_anchor` stay unchanged; no `card_path` is added
  because the card remains inline.
- Card and owner frontmatter: the lane already declares the proposed ids;
  the current `validate_book_metadata.py` "unknown source ID" failure is
  expected until the register includes `src.aws-backup` and
  `src.azure-backup`.
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
- `python3 scripts/validate_book_metadata.py`: FAIL "unknown source ID" for
  the proposed `src.aws-backup` and `src.azure-backup`; expected until the
  integrator registers them.
- `python3 scripts/validate_edition.py`: FAIL
  "directory-baseline-payload-drift". The changed owner page needs a
  content-revisions entry before this baseline check can pass; no shared JSON
  is edited by this lane.
- `python3 scripts/validate_directory_migration.py`: FAIL with the same
  "directory-baseline-payload-drift" condition and the same integration need.
- `python3 scripts/validate_pattern_atlas.py`: FAIL "atlas-document-sha".
  The edited V11/C06 chapter no longer matches the hash pinned in the atlas
  manifest and semantic audit; expected until the integrator refreshes those
  shared records.
- `python3 scripts/validate_book_navigation.py`: FAIL with four unchanged
  missing local anchors in dark-launching-shadow-traffic.md and rbac-abac.md;
  neither file is touched by this lane. The same four issues were recorded in
  the B50 and B51 integration notes.
- `python3 scripts/preflight_sufficient.py --pattern
  tycho.pattern.backup-pitr-and-restore`: FAIL as expected without shared
  metadata; it reports invariant, failure_recovery and alternative still
  partial and no card_path. Inline cards without a dedicated path fail the
  same card_path check; Expand-and-Contract and Online Data Migration show the
  same pre-existing condition.
- Quotes: 13 owner spans and 8 card spans passed a whitespace-normalized
  substring check against the five representations. Tycho-labelled sentences
  are not counted.
- `git diff --check`: no whitespace errors.
- Raw SHA-256 after the book edits: owner page
  `cbd13b0bf356b0aceee83a3e4ca69aedddb9eff3d484a3da673ab108671003f1`;
  chapter `53786669a3152f16dd640d86060215970ad6d3f3ee06580001de67e0082a0b41`.
- The lane note has no tab characters and every line is at most 100
  characters.

## Limits

- Shared metadata is not updated. The generated owner units, registry, source
  plan, ledger, card batches and indexes still show the entry as 1/4 or
  partial until an integrator applies the proposals above.
- No promotion, owner acceptance, coverage sufficiency or independent AI
  review is claimed. The book/atlas review gate remains outstanding; the
  existing review hashes are stale for the edited pages.
- No database, backup set, archive, restore, failover, benchmark or
  production observation was run. The PostgreSQL, AWS, Azure and SRE claims
  are source statements, not local measurements.
- The PostgreSQL page is living documentation with no Last-Modified header and
  a news banner; the AWS and Azure pages are living documentation with
  Last-Modified timestamps; the SRE chapter is a book chapter with a
  2026-10-08 page timestamp. Re-fetches must compare the canonical digest
  before reusing a quote.
- The retained PostgreSQL record's revision differs from the fresh digest;
  the mismatch is recorded rather than resolved by assumption.
- The card is inline because that is the registered layout; the task brief's
  "inline card" wording matches the repository structure. No dedicated card
  path exists in card-batches for this pattern.
- The chapter summary line and source-id list are edited with the inline card.
  Other chapter metadata, atlas hashes and generation outputs remain for the
  integrator.
