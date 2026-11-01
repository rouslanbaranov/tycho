# B53 — Index Table four-dimension lane

Status: lane-local book edit, self-checked on 2026-10-31. No shared edition
metadata, promotion, generated artifact or owner acceptance is included. The
entry was 0/4 at the parent HEAD: mechanism, invariant, failure/recovery and
alternative were all partial. This lane binds all four dimensions to public
PostgreSQL 17, Microsoft SQL Server, Use The Index Luke and Amazon DynamoDB
units, labels the application-owned lookup-table, single-key, repair and choice
rules as Tycho, and keeps the card inline in V11/C06. The lane commit edits only
the two book files and this note.

## Lane coordinates

- Parent HEAD: 3139b632a72227660e557001dbc0e806d1177473 (3139b632).
- Branch: b53-index-table; worktree:
  /Users/rbaranov/Projects/tycho-worktrees/b53-index-table.
- Scope: the owner section "### Index Table" in the V05/C03 page and the inline
  V11/C06 card "### Index Table".
- Owner path (concatenate):

      book/volumes/v05-data-models-engines-and-lifecycle/
      c03-query-planning-indexes-and-access-paths/
      plan-lifecycle.md

- Card path: book/volumes/v11-pattern-atlas/c06-database-storage/README.md.
- Exactly three files change: the owner page, the inline card and this note. No
  shared JSON file is edited.
- Existing source id used: src.postgresql.
- New source ids proposed: src.microsoft-sql-server, src.use-the-index-luke and
  src.aws-dynamodb-gsi. They are not added to the shared register.
- New ledger records proposed: four, listed below.
- Retained record reused unchanged: read.batch3-pg-indexes.2026-10-21.
- Baseline and final line-length and boundary checks pass.

## Baseline and gap

edition/patterns/owner-units.v1.json records all four dimensions as partial with
the same reason:

- mechanism: "Local representation is only the chapter landing plus 11.1
  Introduction (274 words), not the recorded 19-section unit."
- invariant: the same representation-gap reason.
- failure_recovery: the same representation-gap reason.
- alternative: the same representation-gap reason.

The base owner page is the reviewed representation: SHA-256
5ed6aead9933fb5fcd4a39a653f6172cac4c254739af3495218f6ddb594a4c3c. It matches
the page_sha256 in the sufficient-candidates re-review record. The base card
SHA-256 is 74a283fc42fe468cada73d4ce1ad4c82d4cfa4a973849d7baf1da1e0c090378b.

The gap was evidential. The owner section already stated the mechanism,
invariant, failure modes and alternative as Tycho guidance, but no exact public
quote, section and representation hash were bound to the four dimensions. The
PostgreSQL chapter record was also a broad chapter landing, not a bounded
index-only-scan unit. Shared metadata still shows 0/4 until the integrator
applies the proposals below.

## Candidate evaluation

- PostgreSQL 17, "11.9. Index-Only Scans and Covering Indexes" (selected). The
  section defines secondary indexes as separately stored structures, explains
  index-only scans and the visibility map, documents the INCLUDE clause and
  payload columns, and states that uniqueness applies to the key columns only.
  Primary source for mechanism and the invariant side of payload columns.
- Microsoft Learn, "Create indexes with included columns" (selected). The page
  defines included (nonkey) columns, covering behavior, key-size accounting,
  wide-index update cost and the limitation that nonkey columns cannot be
  dropped independently. Primary source for the invariant and a failure bound.
- Markus Winand, "Index-Only Scan: Avoiding Table Access" from Use The Index,
  Luke (selected). The chapter explains covering indexes, index-only scans, the
  effect of clustering and row count, the silent regression when a filter adds a
  non-indexed column, and the warning that covering indexes are an aggressive
  indexing strategy. Primary source for failure/recovery and an alternative
  bound.
- Amazon DynamoDB Developer Guide, "Overloading Global Secondary Indexes in
  DynamoDB" (selected). The page states the default 20-GSI quota and shows one
  overloaded GSI serving several query shapes. Primary source for the
  alternative.
- Rejected or bounded: the retained PostgreSQL chapter landing record is used
  only as the card citation, not as a new dimension binding. No benchmark,
  production report, vendor performance claim or DynamoDB paper is used for the
  GSI overloading mechanism. No database, index, GSI or query was created or
  executed.

## Source units and revisions

All fetches were public HTTPS GETs on 2026-10-31. Canonical text was extracted
with scripts/source_content_hash.py; the four pages expose no article-body
marker, so the script falls back to visible page text including navigation
chrome. Raw HTML SHA-256 is over the decoded response body. Quotes were checked
as whitespace-normalized substrings; spaces before punctuation introduced by
link extraction were normalized (for example "scans , which" is read as
"scans, which"). HTTP dates are the served Date header; no value is a local
stopwatch measurement.

### R1 — PostgreSQL 17, Index-Only Scans and Covering Indexes

- Record: read.pg17-index-only-scans.2026-10-31 (proposed).
- Source: src.postgresql (existing).
- URL: https://www.postgresql.org/docs/17/indexes-index-only-scans.html
- Label/type: "11.9. Index-Only Scans and Covering Indexes — PostgreSQL 17
  documentation"; documentation-page.
- Representation: HTTP/2 200 on 2026-10-31; served Date
  2026-10-31T13:54:03Z; 24,559-byte decoded text/html; no Last-Modified; no
  ETag; raw HTML SHA-256
  9a4d31c2a01359d953c3e3171e7686dc88f40e2f0f27dbf4df2cd6e430e67f1e;
  canonical text 10,059 characters / 1,722 words, SHA-256
  770597607e655863d637486b44c7169fb547dba3cd3c40acd1320866a754e3c4.
- Sections read: 11.9. Index-Only Scans and Covering Indexes (the whole
  section, including the visibility-map discussion, INCLUDE columns,
  uniqueness, payload cost and expression/partial-index interactions).
- Sections not read: other PostgreSQL chapters, linked pages and examples not
  executed.
- Claims supported: Q1, Q2, Q6, Q11, Q12 and Q22.
- Limits: a versioned documentation page, not a release note or benchmark. The
  served Date header was 13:54:03Z while the retrieval ran later; the raw and
  canonical digests, not the Date, pin the representation. No PostgreSQL
  server was run and no index-only scan was executed.

### R2 — Microsoft Learn, Create indexes with included columns

- Record: read.microsoft-included-columns.2026-10-31 (proposed).
- Source: src.microsoft-sql-server (proposed).
- URL: https://learn.microsoft.com/en-us/sql/relational-databases/indexes/
  create-indexes-with-included-columns?view=sql-server-ver17
- Label/type: "Create indexes with included columns — SQL Server"; 
  documentation-page.
- Representation: HTTP/2 200 on 2026-10-31T16:30:47Z; 55,904-byte text/html;
  ETag "jet+Bu9B39m1/QU+O/vLmS2pNcE="; Last-Modified Mon, 19 Oct 2026
  17:42:42 GMT; footer last updated 2026-07-20; raw HTML SHA-256
  73db9cef7521a21dc200519d2f4d7f7bb064005966fd67c4f64eaec953bf1372;
  canonical text 5,943 characters / 992 words, SHA-256
  90861625c10dd5cf1892aeb32f98619b65ffcd0a43b2d1c9183f1d63da4da394.
- Sections read: In this article; Design Recommendations; Limitations.
- Sections not read: Security; Permissions; the SQL Server Management Studio and
  Transact-SQL procedures; related content; linked pages. Code samples were read
  as text, not executed.
- Claims supported: Q4, Q5, Q13, Q14, Q15, Q23 and Q24.
- Limits: the page applies to several SQL Server-family products and the
  sql-server-ver17 view; it is documentation, not a version-specific
  measurement. The canonical fallback includes page chrome. No engine was run,
  no index was created and no query plan was captured.

### R3 — Use The Index, Luke, Index-Only Scan: Avoiding Table Access

- Record: read.luke-index-only-scan.2026-10-31 (proposed).
- Source: src.use-the-index-luke (proposed).
- URL: https://use-the-index-luke.com/sql/clustering/
  index-only-scan-covering-index
- Label/type: "Index-Only Scan: Avoiding Table Access — Use The Index, Luke";
  book-chapter.
- Representation: HTTP/2 200 on 2026-10-31T16:30:43Z; 29,603-byte text/html;
  Last-Modified Mon, 05 Oct 2026 10:33:44 GMT; no ETag; raw HTML SHA-256
  08d3fd30c8700760109bc87614b3f008f826702305b5504a0af5e20d84e80175;
  canonical text 14,583 characters / 2,391 words, SHA-256
  5e1204b9cdd0f25a712894869d80126abbbd39132706c80357908693dc24a95b.
- Sections read: Index-Only Scan: Avoiding Table Access; INCLUDE: Non-key
  Columns (including the per-database notes).
- Sections not read: linked chapters, the book's other pages and the author
  pages beyond the article footer. SQL examples were read as text, not executed.
- Claims supported: Q3, Q7, Q8, Q9, Q10, Q16, Q19, Q20 and Q21.
- Limits: a practitioner book chapter, not vendor documentation, a
  specification or a benchmark. The page is a living web representation pinned
  by digest; the Last-Modified header varied between fetches while the raw
  digest stayed identical. No database was run.

### R4 — Amazon DynamoDB, Overloading Global Secondary Indexes in DynamoDB

- Record: read.aws-dynamodb-gsi-overloading.2026-10-31 (proposed).
- Source: src.aws-dynamodb-gsi (proposed).
- URL: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/
  bp-gsi-overloading.html
- Label/type: "Overloading Global Secondary Indexes in DynamoDB — Amazon
  DynamoDB Developer Guide"; documentation-page.
- Representation: HTTP/1.1 200 on 2026-10-31; served Date
  2026-10-31T16:26:01Z; 14,724-byte text/html; ETag
  "J+g4lUOI5/E1P2eXEIX/oCVjykI="; Last-Modified Sat, 31 Oct 2026 03:33:02
  GMT; raw HTML SHA-256
  cd118a484b63c775e8dee9e2782085afab7471c6faa013fe2cc046c0300b70e4;
  canonical text 2,069 characters / 357 words, SHA-256
  1d1a982b843ee7d8cca03b06eecb19efc0c67a135acd020fb91a8d35da32fc1a.
- Sections read: Overloading Global Secondary Indexes in DynamoDB (the whole
  short topic, including the employee, warehouse and recent-hire examples).
- Sections not read: linked DynamoDB topics, the markdown alternate of the page
  and service-quota pages.
- Claims supported: Q17 and Q18.
- Limits: one short official topic. It states the default quota and the
  overloading idea, not item-collection limits, capacity behavior or a
  production workload. No table, GSI, partition key or query was created.

## Selected exact quotes

Quotes reproduce the served prose. Line breaks inside a quote are editorial
wrapping. Every quote below passed the whitespace-normalized substring check
against the named canonical representation; punctuation-space normalization was
applied only for link-extraction artifacts. Tycho-labelled sentences in the book
are not source quotes.

### Mechanism

- Q1, PostgreSQL, section 11.9:

      All indexes in PostgreSQL are secondary indexes, meaning that each index
      is stored separately from the table's main data area

- Q2, PostgreSQL, section 11.9:

      PostgreSQL supports index-only scans, which can answer queries from an
      index alone without any heap access.

- Q3, Use The Index, Luke, section "Index-Only Scan: Avoiding Table Access":

      It not only avoids accessing the table to evaluate the where clause, but
      avoids accessing the table completely if the database can find the
      selected columns in the index itself.

- Q4, Microsoft Learn, section "In this article":

      By including nonkey columns, you can create nonclustered indexes that
      cover more queries.

### Invariant

- Q5, Microsoft Learn, section "Design Recommendations":

      The Database Engine doesn't consider nonkey columns when calculating the
      number of index key columns or index key size.

- Q6, PostgreSQL, section 11.9:

      the uniqueness condition applies to just column x, not to the combination
      of x and y

- Q7, Use The Index, Luke, section "INCLUDE: Non-key Columns":

      They are—other than the key columns, which we discussed so far—only
      stored in the leaf nodes and can thus not be used for access predicates.

- Q24, Microsoft Learn, section "Design Recommendations":

      The order of nonkey columns in the index definition doesn't affect the
      performance of queries that use the index.

### Failure and recovery

- Q8, Use The Index, Luke, section "Index-Only Scan: Avoiding Table Access":

      The table access increases the response time although the query selects
      fewer rows.

- Q9, Use The Index, Luke, section "Index-Only Scan: Avoiding Table Access":

      The relevant factor is not how many rows the query delivers but how many
      rows the database must inspect to find them.

- Q10, Use The Index, Luke, section "Index-Only Scan: Avoiding Table Access":

      Extending the where clause can cause “illogical” performance behavior.
      Check the execution plan before extending queries.

- Q11, PostgreSQL, section 11.9:

      If it's not set, the heap entry must be visited to find out whether it's
      visible, so no performance advantage is gained over a standard index
      scan.

- Q12, PostgreSQL, section 11.9:

      An index-only scan, after finding a candidate index entry, checks the
      visibility map bit for the corresponding heap page.

- Q13, Microsoft Learn, section "Design Recommendations":

      Avoid very wide nonclustered indexes where the included columns don't
      represent a narrow enough subset of the underlying table columns.

- Q14, Microsoft Learn, section "Design Recommendations":

      If adding wide indexes, always verify if the cost of updating one extra
      wide index offsets the cost of reading directly from the table.

- Q15, Microsoft Learn, section "Limitations":

      Nonkey columns can't be dropped from a table unless that table's index is
      dropped first.

- Q16, Use The Index, Luke, section "Index-Only Scan: Avoiding Table Access":

      In this case we should remove the unneeded columns from the other index
      again.

### Alternative

- Q17, DynamoDB, section "Overloading Global Secondary Indexes in DynamoDB":

      Although Amazon DynamoDB has a default quota of 20 global secondary
      indexes per table, in practice, you can index across far more than 20
      data fields.

- Q18, DynamoDB, section "Overloading Global Secondary Indexes in DynamoDB":

      If you create a global secondary index for the table that uses the
      table's sort key as its partition key and the Data attribute as its sort
      key, you can make a variety of different queries using that single global
      secondary index.

- Q19, Use The Index, Luke, section "Index-Only Scan: Avoiding Table Access":

      The index-only scan is an aggressive indexing strategy.

- Q20, Use The Index, Luke, section "Index-Only Scan: Avoiding Table Access":

      Do not design an index for an index-only scan on suspicion only because
      it unnecessarily uses memory and increases the maintenance effort needed
      for update statements.

- Q21, Use The Index, Luke, section "Index-Only Scan: Avoiding Table Access":

      In practice, you should first index without considering the select clause
      and only extend the index if needed.

- Q22, PostgreSQL, section 11.9:

      Before PostgreSQL had the INCLUDE feature, people sometimes made covering
      indexes by writing the payload columns as ordinary index columns

- Q23, Microsoft Learn, section "Design Recommendations":

      Make all other columns that cover the query into nonkey columns.

## Dimension mapping

- Mechanism. Primary: Q2, record read.pg17-index-only-scans.2026-10-31,
  section "11.9. Index-Only Scans and Covering Indexes", revision
  770597607e655863d637486b44c7169fb547dba3cd3c40acd1320866a754e3c4.
  Supporting: Q1 (separately stored index), Q3 (covering index avoids table
  access) and Q4 (nonkey columns cover more queries). Owner quote: "the index
  table is the application-owned variant of that secondary access path". Tycho
  reading: the index table is the application-owned variant of a secondary
  access path; the base row is authoritative and the lookup row is derived
  state the write path maintains.
- Invariant. Primary: Q5, record read.microsoft-included-columns.2026-10-31,
  section "Design Recommendations", revision
  90861625c10dd5cf1892aeb32f98619b65ffcd0a43b2d1c9183f1d63da4da394.
  Supporting: Q6 (uniqueness applies to key only), Q7 (non-key columns are leaf
  payload, not access predicates) and Q24 (nonkey order does not affect query
  performance). Owner quote: "keep exactly one lookup key; payload columns must
  never become a second key". Tycho rule: one lookup key defines what a row
  locates and what a duplicate means; payload columns never become a second key
  or a second source of truth, and the mapping plus base write commit together
  or publish a durable repair intent.
- Failure and recovery. Primary: Q10, record
  read.luke-index-only-scan.2026-10-31, section "Index-Only Scan: Avoiding Table
  Access", revision
  5e1204b9cdd0f25a712894869d80126abbbd39132706c80357908693dc24a95b.
  Supporting: Q8 and Q9 (a filter can raise response time), Q11 and Q12
  (visibility-map miss forces heap access), Q13-Q15 (wide-index update cost and
  schema coupling) and Q16 (remove unneeded columns). Owner quote: "reconcile
  with a repair job, keep the lookup key immutable, bound rebuild time". Tycho
  runbook: dual-write ambiguity, partial backfill, duplicate lookup keys and
  stale rows are design-time failure modes; repair, keep the key immutable,
  bound rebuild time and re-check the plan after every query-shape change.
- Alternative. Primary: Q18, record
  read.aws-dynamodb-gsi-overloading.2026-10-31, section "Overloading Global
  Secondary Indexes in DynamoDB", revision
  1d1a982b843ee7d8cca03b06eecb19efc0c67a135acd020fb91a8d35da32fc1a.
  Supporting: Q17 (default GSI quota), Q19-Q21 (covering indexes are
  aggressive; index first, extend only if needed), Q22 (payload as ordinary key
  columns before INCLUDE) and Q23 (make covering columns nonkey). Owner quote:
  "keep an application-owned index table when the write path can own its
  repair". Tycho choice rule: prefer a native covering index, materialized
  view, query-time join or overloaded managed secondary index; keep an
  application-owned table only when the write path can own repair and the
  added write/repair cost is below the scan or drift cost removed; reverse when
  key drift or maintenance cost exceeds the lookup benefit.

Supporting-binding sections for the integrator: Q1, Q6, Q11, Q12 and Q22 use
"11.9. Index-Only Scans and Covering Indexes"; Q3, Q8, Q9, Q10, Q16, Q19, Q20
and Q21 use "Index-Only Scan: Avoiding Table Access"; Q7 uses "INCLUDE: Non-key
Columns"; Q4 uses "In this article"; Q5, Q13, Q14, Q23 and Q24 use "Design
Recommendations"; Q15 uses "Limitations"; Q17 and Q18 use "Overloading Global
Secondary Indexes in DynamoDB". Every one is present in the corresponding
proposed record's sections_read.

## Book edits

- Owner page (concatenate):

      book/volumes/v05-data-models-engines-and-lifecycle/
      c03-query-planning-indexes-and-access-paths/
      plan-lifecycle.md

  - Frontmatter adds src.microsoft-sql-server, src.use-the-index-luke and
    src.aws-dynamodb-gsi to evidence_scope.source_ids, updates the evidence
    note, sets reviewed_at, updated_at and source_inspection_date to
    2026-10-31, and sets reviewer to "Automated authoring agent".
  - The Index Table section replaces the earlier three paragraphs with
    labelled mechanism, invariant, failure/recovery, alternative, source-limit
    and source-unit paragraphs. The section is 89 lines and 793 words; the
    "### Index Table" heading is line 107.
  - Page 205 lines; 1,526 words.
  - SHA-256:
    c4a96c72831636cc0df664788ad82f7983ace39e7d5f7e722e20195d0325315a.
- Inline card: book/volumes/v11-pattern-atlas/c06-database-storage/README.md.
  - Frontmatter adds the same three proposed source ids and rewrites the
    evidence note as a folded block naming the Index Table binding.
  - "Good-fit conditions", "Hard contraindications", "Competing alternative",
    "Failure and recovery" and "Sources" are expanded with the same bindings
    and revisions; the owner link and anchor are unchanged. The card section is
    54 lines and 355 words; the "### Index Table" heading is line 193.
  - Card 404 lines; 1,911 words.
  - SHA-256:
    31a8a582e15d3e0cd0005c9e2ef14c59036d40d9fb2ab5e2a22c567706e9f489.
- No other book file, edition JSON, promotion or generated file is changed.

## Metadata needs (integrator)

The following changes are not in the lane commit. They are required before the
owner unit can move to 4/4 supported and before atlas hash checks pass.

### Source register sources/register.json

Set updated to 2026-10-31; the source count moves 315 to 318. Add three sources
and extend the existing src.postgresql record.

- Add src.microsoft-sql-server: title "Create indexes with included columns";
  category databases; publisher "Microsoft Learn"; kind official-docs; URL
  https://learn.microsoft.com/en-us/sql/relational-databases/indexes/
  create-indexes-with-included-columns?view=sql-server-ver17; topics sql-server,
  indexes, covering-index and included-columns; priority core; admission
  admitted-for-research; access public-web-or-author-download; reading status
  full-public-page-inspected; version note with the 2026-10-31 representation:
  55,904 bytes, ETag "jet+Bu9B39m1/QU+O/vLmS2pNcE=", Last-Modified
  2026-10-19T17:42:42Z, footer last updated 2026-07-20, raw HTML SHA-256
  73db9cef7521a21dc200519d2f4d7f7bb064005966fd67c4f64eaec953bf1372 and
  canonical text 5,943 characters / SHA-256
  90861625c10dd5cf1892aeb32f98619b65ffcd0a43b2d1c9183f1d63da4da394; access
  and content-verified dates 2026-10-31; license note "Public Microsoft Learn
  documentation; cite short excerpts and paraphrase; do not mirror.";
  verification scope names In this article, Design Recommendations and
  Limitations and excludes linked pages and executed code; observed title
  "Create indexes with included columns - SQL Server | Microsoft Learn".
- Add src.use-the-index-luke: title "Index-Only Scan: Avoiding Table Access";
  category databases; publisher "Markus Winand"; kind book-chapter; URL
  https://use-the-index-luke.com/sql/clustering/
  index-only-scan-covering-index; topics indexing, covering-index,
  index-only-scan and sql; priority core; admission admitted-for-research;
  reading status full-public-page-inspected; version note with the 2026-10-31
  representation: 29,603 bytes, Last-Modified 2026-10-05T10:33:44Z, no ETag,
  raw HTML SHA-256
  08d3fd30c8700760109bc87614b3f008f826702305b5504a0af5e20d84e80175 and
  canonical text 14,583 characters / SHA-256
  5e1204b9cdd0f25a712894869d80126abbbd39132706c80357908693dc24a95b; access
  and content-verified dates 2026-10-31; license note "Public online book
  chapter; cite short excerpts and paraphrase; do not mirror."; verification
  scope names the index-only-scan and INCLUDE sections and excludes linked
  chapters and executed SQL; observed title "Covering index: an index
  containing all queried columns".
- Add src.aws-dynamodb-gsi: title "Overloading Global Secondary Indexes in
  DynamoDB"; category databases; publisher "Amazon Web Services"; kind
  official-docs; URL
  https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/
  bp-gsi-overloading.html; topics dynamodb, global-secondary-index,
  index-overloading and nosql; priority core; admission admitted-for-research;
  reading status full-public-page-inspected; version note with the 2026-10-31
  representation: 14,724 bytes, ETag "J+g4lUOI5/E1P2eXEIX/oCVjykI=",
  Last-Modified 2026-10-31T03:33:02Z, raw HTML SHA-256
  cd118a484b63c775e8dee9e2782085afab7471c6faa013fe2cc046c0300b70e4 and
  canonical text 2,069 characters / SHA-256
  1d1a982b843ee7d8cca03b06eecb19efc0c67a135acd020fb91a8d35da32fc1a; access
  and content-verified dates 2026-10-31; license note "Public AWS
  documentation; cite short excerpts and paraphrase; do not mirror.";
  verification scope names the whole overloading topic and excludes linked
  service-quota and capacity pages; observed title "Overloading Global
  Secondary Indexes in DynamoDB - Amazon DynamoDB".
- Extend src.postgresql: keep reading_status landing-or-abstract-inspected and
  append the PostgreSQL 17 11.9 2026-10-31 representation to version: 24,559
  bytes, no Last-Modified or ETag, raw HTML SHA-256
  9a4d31c2a01359d953c3e3171e7686dc88f40e2f0f27dbf4df2cd6e430e67f1e,
  canonical text 10,059 characters / SHA-256
  770597607e655863d637486b44c7169fb547dba3cd3c40acd1320866a754e3c4; set
  access_checked and content_verified to 2026-10-31; extend verification scope
  with the 11.9 section and note that no server was run.

### Reading ledger edition/patterns/reading-ledger.v1.json

Add four records; records move 253 to 257. Each record is status read,
reviewer "Automated authoring agent", access_date 2026-10-31.

- read.pg17-index-only-scans.2026-10-31.
  - source_id: src.postgresql.
  - unit_url: https://www.postgresql.org/docs/17/indexes-index-only-scans.html.
  - unit_label: "11.9. Index-Only Scans and Covering Indexes — PostgreSQL 17
    documentation".
  - unit_type: documentation-page.
  - access_method: public HTTPS GET on 2026-10-31; HTTP/2 200; served Date
    2026-10-31T13:54:03Z; 24,559-byte decoded text/html; no Last-Modified; no
    ETag; raw HTML SHA-256
    9a4d31c2a01359d953c3e3171e7686dc88f40e2f0f27dbf4df2cd6e430e67f1e;
    canonical text 10,059 characters; SHA-256
    770597607e655863d637486b44c7169fb547dba3cd3c40acd1320866a754e3c4.
  - sections_read: ["11.9. Index-Only Scans and Covering Indexes"].
  - sections_not_read: linked pages; other PostgreSQL chapters; examples not
    executed.
  - tables_figures: none used; code examples were read as text.
  - license_notes: "Public PostgreSQL documentation; cite short excerpts and
    paraphrase; do not mirror."
  - claims_supported: Q1, Q2, Q6, Q11, Q12, Q22.
  - claims_not_supported: planner or executor behavior in a running server; a
    benchmark or production observation; linked pages.
  - limitations: "Versioned documentation page; the digest pins the 2026-10-31
    representation. No PostgreSQL server was run."
  - content_sha256:
    770597607e655863d637486b44c7169fb547dba3cd3c40acd1320866a754e3c4.
  - read_scope: the whole 11.9 section, excluding linked pages and executed
    examples.
- read.microsoft-included-columns.2026-10-31.
  - source_id: src.microsoft-sql-server.
  - unit_url: the R2 URL including ?view=sql-server-ver17.
  - unit_label: "Create indexes with included columns — SQL Server".
  - unit_type: documentation-page.
  - access_method: public HTTPS GET on 2026-10-31T16:30:47Z; HTTP/2 200;
    55,904-byte text/html; ETag "jet+Bu9B39m1/QU+O/vLmS2pNcE=";
    Last-Modified 2026-10-19T17:42:42Z; footer last updated 2026-07-20; raw
    HTML SHA-256
    73db9cef7521a21dc200519d2f4d7f7bb064005966fd67c4f64eaec953bf1372;
    canonical text 5,943 characters; SHA-256
    90861625c10dd5cf1892aeb32f98619b65ffcd0a43b2d1c9183f1d63da4da394.
  - sections_read: ["In this article", "Design Recommendations",
    "Limitations"].
  - sections_not_read: Security; Permissions; the procedure sections; related
    content; linked pages.
  - tables_figures: none used; code samples were read as text.
  - license_notes: "Public Microsoft Learn documentation; cite short excerpts
    and paraphrase; do not mirror."
  - claims_supported: Q4, Q5, Q13, Q14, Q15, Q23, Q24.
  - claims_not_supported: a specific engine build's behavior; a benchmark or
    production observation; linked pages.
  - limitations: "Documentation, not a release-specific measurement; no index
    was created and no plan was captured."
  - content_sha256:
    90861625c10dd5cf1892aeb32f98619b65ffcd0a43b2d1c9183f1d63da4da394.
  - read_scope: the article introduction, Design Recommendations and
    Limitations, excluding procedures and linked pages.
- read.luke-index-only-scan.2026-10-31.
  - source_id: src.use-the-index-luke.
  - unit_url: the R3 URL.
  - unit_label: "Index-Only Scan: Avoiding Table Access — Use The Index, Luke".
  - unit_type: book-chapter.
  - access_method: public HTTPS GET on 2026-10-31T16:30:43Z; HTTP/2 200;
    29,603-byte text/html; Last-Modified 2026-10-05T10:33:44Z; no ETag; raw
    HTML SHA-256
    08d3fd30c8700760109bc87614b3f008f826702305b5504a0af5e20d84e80175;
    canonical text 14,583 characters; SHA-256
    5e1204b9cdd0f25a712894869d80126abbbd39132706c80357908693dc24a95b.
  - sections_read: ["Index-Only Scan: Avoiding Table Access", "INCLUDE:
    Non-key Columns"].
  - sections_not_read: linked chapters; other book pages; author pages beyond
    the article footer.
  - tables_figures: execution-plan text blocks were read as text; no figure was
    reproduced.
  - license_notes: "Public online book chapter; cite short excerpts and
    paraphrase; do not mirror."
  - claims_supported: Q3, Q7, Q8, Q9, Q10, Q16, Q19, Q20, Q21.
  - claims_not_supported: a universal performance rule; a benchmark or
    production observation; linked chapters.
  - limitations: "Practitioner book chapter, not vendor documentation or a
    benchmark; the Last-Modified header varied between fetches while the raw
    digest stayed identical. No database was run."
  - content_sha256:
    5e1204b9cdd0f25a712894869d80126abbbd39132706c80357908693dc24a95b.
  - read_scope: the index-only-scan and INCLUDE sections, excluding linked
    chapters and executed SQL.
- read.aws-dynamodb-gsi-overloading.2026-10-31.
  - source_id: src.aws-dynamodb-gsi.
  - unit_url: the R4 URL.
  - unit_label: "Overloading Global Secondary Indexes in DynamoDB — Amazon
    DynamoDB Developer Guide".
  - unit_type: documentation-page.
  - access_method: public HTTPS GET on 2026-10-31; HTTP/1.1 200; served Date
    2026-10-31T16:26:01Z; 14,724-byte text/html; ETag
    "J+g4lUOI5/E1P2eXEIX/oCVjykI="; Last-Modified 2026-10-31T03:33:02Z; raw
    HTML SHA-256
    cd118a484b63c775e8dee9e2782085afab7471c6faa013fe2cc046c0300b70e4;
    canonical text 2,069 characters; SHA-256
    1d1a982b843ee7d8cca03b06eecb19efc0c67a135acd020fb91a8d35da32fc1a.
  - sections_read: ["Overloading Global Secondary Indexes in DynamoDB"].
  - sections_not_read: linked DynamoDB topics; the markdown alternate; service
    quota and capacity pages.
  - tables_figures: none used; example query descriptions were read as text.
  - license_notes: "Public AWS documentation; cite short excerpts and
    paraphrase; do not mirror."
  - claims_supported: Q17, Q18.
  - claims_not_supported: item-collection limits; capacity or throttling
    behavior; a production workload.
  - limitations: "Short official topic; it states the overloading idea and
    default quota, not a measured evaluation. No table or GSI was created."
  - content_sha256:
    1d1a982b843ee7d8cca03b06eecb19efc0c67a135acd020fb91a8d35da32fc1a.
  - read_scope: the whole short topic, excluding linked pages.

### Source plan edition/patterns/source-plan.v1.json

Append four units to tycho.pattern.index-table after the existing PostgreSQL
chapter unit, in R1-R4 order. Every unit is status read and blocked_reason null.
Use the R1-R4 URLs, labels and sections above.

Summary changes: required_units 301 to 305; read_units 300 to 304;
ledger_records 253 to 257; planned_units 0 and blocked_units 1 unchanged;
updated 2026-10-31. Recompute registry_sha256 after saving the registry.

Replace the entry notes with: "Four public units read 2026-10-31; all four
technical dimensions bound to PostgreSQL 17 index-only scans, SQL Server
included columns, Use The Index Luke and DynamoDB GSI overloading; no runtime
test or sufficiency claim."

### Owner units edition/patterns/owner-units.v1.json

For tycho.pattern.index-table:

- mechanism: set state supported; owner quote "the index table is the
  application-owned variant of that secondary access path"; primary binding Q2,
  source src.postgresql, record read.pg17-index-only-scans.2026-10-31, section
  "11.9. Index-Only Scans and Covering Indexes", quote "PostgreSQL supports
  index-only scans, which can answer queries from an index alone without any
  heap access.", revision
  770597607e655863d637486b44c7169fb547dba3cd3c40acd1320866a754e3c4; add
  supporting Q1, Q3 and Q4. Reason: PostgreSQL defines a secondary index as a
  separately stored structure and an index-only scan as answering from the index
  alone; Luke and SQL Server describe the covering variant; the
  application-owned reading is Tycho.
- invariant: set state supported; owner quote "keep exactly one lookup key;
  payload columns must never become a second key"; primary binding Q5, source
  src.microsoft-sql-server, record
  read.microsoft-included-columns.2026-10-31, section "Design Recommendations",
  quote "The Database Engine doesn't consider nonkey columns when calculating
  the number of index key columns or index key size.", revision
  90861625c10dd5cf1892aeb32f98619b65ffcd0a43b2d1c9183f1d63da4da394; add
  supporting Q6, Q7 and Q24. Reason: SQL Server keeps nonkey columns out of the
  key accounting and order, PostgreSQL applies uniqueness to the key only, and
  Luke says non-key columns are leaf payload; the one-key and repair rules are
  Tycho.
- failure_recovery: set state supported; owner quote "reconcile with a repair
  job, keep the lookup key immutable, bound rebuild time"; primary binding Q10,
  source src.use-the-index-luke, record read.luke-index-only-scan.2026-10-31,
  section "Index-Only Scan: Avoiding Table Access", quote "Extending the where
  clause can cause “illogical” performance behavior. Check the execution plan
  before extending queries.", revision
  5e1204b9cdd0f25a712894869d80126abbbd39132706c80357908693dc24a95b; add
  supporting Q8, Q9, Q11, Q12, Q13, Q14, Q15 and Q16. Reason: Luke shows a
  filter defeating an index-only scan and raising response time, PostgreSQL
  requires visibility-map bits, and SQL Server warns about wide-index update
  cost and schema coupling; the repair runbook is Tycho.
- alternative: set state supported; owner quote "keep an application-owned index
  table when the write path can own its repair"; primary binding Q18, source
  src.aws-dynamodb-gsi, record
  read.aws-dynamodb-gsi-overloading.2026-10-31, section "Overloading Global
  Secondary Indexes in DynamoDB", quote "If you create a global secondary index
  for the table that uses the table's sort key as its partition key and the Data
  attribute as its sort key, you can make a variety of different queries using
  that single global secondary index.", revision
  1d1a982b843ee7d8cca03b06eecb19efc0c67a135acd020fb91a8d35da32fc1a; add
  supporting Q17, Q19, Q20, Q21, Q22 and Q23. Reason: DynamoDB shows one
  overloaded GSI serving several query shapes, Luke recommends indexing without
  the select clause first and calls covering indexes aggressive, and PostgreSQL
  and SQL Server show payload columns as non-key; the choice rule is Tycho.
- technical_coverage: partial to partial-bounded; decision_coverage stays
  partial-bounded.
- source_support: keep the primary card citation read.batch3-pg-indexes.2026-10-21
  under src.postgresql; add auxiliary records read.pg17-index-only-scans.2026-10-31,
  read.microsoft-included-columns.2026-10-31, read.luke-index-only-scan.2026-10-31
  and read.aws-dynamodb-gsi-overloading.2026-10-31 with the revisions above;
  notes name the 2026-10-31 binding.
- Counters: mechanism_supported 118 to 119; invariant_supported 83 to 84;
  failure_recovery_supported 78 to 79; alternative_supported 83 to 84;
  technical_partial_bounded 15 to 16; technical_partial 64 to 63;
  technical_sufficient stays 66.

### Pattern registry edition/patterns/registry.v1.json

For tycho.pattern.index-table:

- Set technical_owner.state to partial-bounded.
- Set coverage.technical and coverage.overall to partial-bounded; coverage.decision
  and atlas_owner.state stay partial-bounded.
- Append four source_units after the existing PostgreSQL chapter unit in R1-R4
  order: src.postgresql / "11.9. Index-Only Scans and Covering Indexes —
  PostgreSQL 17 documentation"; src.microsoft-sql-server / "Create indexes with
  included columns — SQL Server"; src.use-the-index-luke / "Index-Only Scan:
  Avoiding Table Access — Use The Index, Luke"; src.aws-dynamodb-gsi /
  "Overloading Global Secondary Indexes in DynamoDB — Amazon DynamoDB Developer
  Guide". All status read; unit count 1 to 5.
- Set notes to: "Phase 3 C06 inline card; bounded owner section and backlink are
  self-checked, not independent-reviewed or sufficient. All four technical
  dimensions bound 2026-10-31 to PostgreSQL 17 index-only scans, SQL Server
  included columns, Use The Index Luke and DynamoDB GSI overloading; coverage
  partial-bounded."
- Set updated_at to 2026-10-31.

### Card registration edition/patterns/card-batches.v1.json

The card remains inline in V11/C06; no card_path is added. Keep the existing
entry ledger_record read.batch3-pg-indexes.2026-10-21 as the retained primary
citation; the new records are additional source_units in the registry and
ledger, not a replacement of the historical card citation.

### Content revisions edition/content-revisions.json

Add one entry:

- issue: 540.
- authorized_at: 2026-10-31.
- authorization: "B53 index table four-dimension source binding; metadata
  integration, no promotion or owner acceptance."
- directory_documents:
  - Owner path, previous_sha256
    5ed6aead9933fb5fcd4a39a653f6172cac4c254739af3495218f6ddb594a4c3c
    (parent HEAD), current_sha256
    c4a96c72831636cc0df664788ad82f7983ace39e7d5f7e722e20195d0325315a.
  - Card path, previous_sha256
    74a283fc42fe468cada73d4ce1ad4c82d4cfa4a973849d7baf1da1e0c090378b
    (parent HEAD), current_sha256
    31a8a582e15d3e0cd0005c9e2ef14c59036d40d9fb2ab5e2a22c567706e9f489.
- Empty source_blocks, enrichment_documents, enrichment_additions and
  enrichment_baselines.

### Other shared metadata

- Registry and source-plan hashes: recompute registry_sha256 and the atlas
  document hashes after the registry and book edits.
- Coverage map, sufficient candidates, sufficient review records,
  sufficient-review reconciliation, atlas manifest, inventory, page census,
  route and section indexes, qrels and delivery evidence: usual recomputation.
- Owner and card frontmatter: after the three proposed source ids are
  registered, the declared evidence_scope.source_ids resolve; preflight requires
  every binding source to be declared. This lane adds only the already-registered
  src.postgresql as a binding source and declares the proposed ids for the
  integrator.
- The existing sufficient-candidates review record pins page hash
  5ed6aead9933fb5fcd4a39a653f6172cac4c254739af3495218f6ddb594a4c3c; it is
  stale for the edited page and cannot be treated as a review pass.
- The owner page claim_ids stay empty; no claim registry is introduced.

## Validation

In the lane worktree after the two book edits, before this note was added:

    PASS: V11 prose <=100; 145 exact owner-link exceptions
    PASS: configured lexical boundary checks; independent-origin review still required.
    PASS: pattern cards 11 batch(es), 145 entries
    PASS: pattern registry 145 entries, 11 families

    FAIL: book/volumes/v11-pattern-atlas/c06-database-storage/README.md: unknown source ID
    FAIL: owner-units-unit-ambiguous: Index Table
    FAIL: atlas-document-sha
    FAIL: tycho.pattern.index-table
      - mechanism: state 'partial', not supported
      - invariant: state 'partial', not supported
      - failure_recovery: state 'partial', not supported
      - alternative: state 'partial', not supported
      - card_path missing or absent
    0/1 entries preflight clean

    Checked 507 book pages; issues 4
    V08/C04 dark-launching-shadow-traffic.md: lines 52 and 83:
      missing-local-anchor
    V09/C05 rbac-abac.md: lines 53 and 81:
      missing-local-anchor

    PASS: git diff --check (no whitespace errors)

The metadata, owner-units, atlas and preflight failures are the expected
pre-integration state: shared JSON is not edited by this lane, the owner page
and card hashes are not yet in content-revisions, and the card remains inline
without a card_path. The four missing local anchors are unchanged from the
B50/B51/B52 notes and are outside this lane. They are not book defects
introduced by this lane.

- Quotes: 24 exact quotes checked as whitespace-normalized substrings of the
  four named representations; 24/24 passed. The owner page contains 14 of the
  quoted fragments and the card contains four; both passed the same check. The
  full quote set is reproduced above.
- Owner page: every added line is at most 100 characters. Existing long
  frontmatter, section-2 table and navigation lines are unchanged.
- V11 card: checker PASS; only the existing "**Technical owner.**" lines are
  exempt.
- Lane note: every line is at most 100 characters; 837 lines.
- Raw SHA-256: owner
  c4a96c72831636cc0df664788ad82f7983ace39e7d5f7e722e20195d0325315a;
  card 31a8a582e15d3e0cd0005c9e2ef14c59036d40d9fb2ab5e2a22c567706e9f489.
- git status: exactly three files, the owner page, the card and this note.
- The full test suite is deferred to the batch end under the batch rule; no
  test results are claimed here.

## Limits

- Shared metadata is not updated. Owner units, registry, source plan, ledger,
  card batches, content revisions and indexes still show 0/4 or partial until
  an integrator applies the proposals above.
- No promotion, owner acceptance, coverage sufficiency or independent AI review
  is claimed. The book/atlas review gate remains outstanding, and the existing
  sufficient-candidates review hash is stale for the edited page.
- No benchmark, production observation, query-plan capture, index build, GSI
  creation or database execution was performed. The workload wording in the
  page remains synthetic design guidance.
- PostgreSQL and Microsoft Learn pages are living or version-selected
  documentation; the digests pin the 2026-10-31 representations, not release
  tags. The PostgreSQL served Date header predates the retrieval wall time; the
  content digests are the binding evidence.
- The Use The Index, Luke page is a practitioner book chapter, not vendor
  documentation or a benchmark. Its Last-Modified header varied between fetches
  while the raw digest was stable.
- The DynamoDB topic is short and does not cover item-collection limits,
  capacity behavior or production operation. It supports the overloading idea
  and the default quota only.
- The canonical-text extraction uses the repository script's fallback whole-page
  text because these four pages expose no article-body marker; the digest
  therefore covers page chrome as well as article prose.
- Two source quotes (Q2 and Q6) contain extraction spaces before punctuation in
  the canonical text; the book quotes the normalized prose and this note records
  the normalization.
- The owner page is in V05, so the repository's V11 line-length checker does not
  cover it; its added lines were checked directly.
- The card remains inline in V11/C06, matching the task brief and the registered
  atlas_section index-table.
- The page's claim_ids stay empty; no claim registry is introduced.

## Commit scope

The lane commit contains this note and the two book files only:

- the V05/C03 owner page plan-lifecycle.md;
- the V11/C06 inline card README.md;
- authoring/B53-INDEX-TABLE-LANE-2026-10-31.md.

Exact repository paths appear in the lane diff. No shared JSON, promotion or
generated file is in the lane commit.
