# Coverage comparison: sources and patterns, Tycho versus public catalogues

Date: 2026-10-27. Status: bounded, reproducible count for owner review.
Not an acceptance record and not a like-for-like market benchmark.

> Issue [#547](https://github.com/rouslanbaranov/tycho/issues/547).
> Companion: [landscape scan](LANDSCAPE-SCAN_2026-10-27.md).

## Research contract

- Reader: the Tycho owner, judging breadth and depth claims against public work.
- Primary question: how many sources and how many system design patterns do the
  compared catalogues actually present, and how deep is each entry?
- Subquestions: which counts are comparable? Where is Tycho broader, where is
  it shallower, and what does no competitor publish at all?
- Exclusions: paid reports, private products, answer-quality measurement,
  purchased course content, unverified chapter counts.
- Method: read the public artefact of each catalogue and count a defined unit;
  record the exact file or page and the counting rule.
- Completion: every number has a source and a counting rule; non-comparable
  units are marked; limits are stated.

## Counting rules

- Pattern entry: one named pattern or mechanism listed by the catalogue.
- Section: a top-level documentation section, not a pattern.
- Source: one distinct public work registered or cited by the corpus, counted
  once even when several patterns use it.
- Link: one distinct external URL. A link list is not a source register: it has
  no admission state, reading state or per-claim binding.

The units differ by design. Numbers below compare scale and traceability, not
editorial quality.

## Tycho baseline

| Metric | Value |
|---|---|
| Canonical documents | 423 |
| Volumes / chapters | 11 / 82 |
| Pattern entries | 145 (123 core, 22 advanced) |
| Pattern families (V11) | 11 |
| Registered sources | 275 |
| Admitted for research | 220 |
| Pending content access | 45 |
| Bibliography only | 10 |
| Distinct sources in full-unit reading plan | 64 |
| Full-read plan entries | 143 (1 partial, 11 blocked) |
| Patterns with at least one evidence binding | 116 of 145 |
| Distinct sources bound to pattern evidence | 49 |
| Pattern owner pages | 69 (33 shared) |

Pattern families and entry counts:

| Family | Entries |
|---|---|
| Application architecture and boundaries | 12 |
| API and service communication | 12 |
| Messaging and event-driven integration | 20 |
| Data consistency, transactions and event sourcing | 14 |
| Caching and retrieval | 14 |
| Database and storage architecture | 13 |
| Resilience and fault tolerance | 16 |
| Distributed coordination | 9 |
| Scalability and load distribution | 10 |
| Deployment and legacy modernization | 12 |
| Security, isolation and operational architecture | 13 |

Evidence state per pattern (from the owner-unit audit):

| Dimension | Supported |
|---|---|
| Mechanism | 109 of 145 (75%) |
| Invariant | 51 of 145 (35%) |
| Failure and recovery | 37 of 145 (26%) |
| Alternative and reversal | 48 of 145 (33%) |
| Technical coverage | 46 partial-bounded, 99 partial, 0 sufficient |

Sources by kind (275 total): official documentation 135, public practitioner
reference 43, implementation repository 12, author article 11, standard 11,
commercial book 10, public reference 10, paper 10, free book 9, specification 7,
and 10 smaller kinds. The register carries 260 distinct topic tags.

## Competitor counts

| Catalogue | Pattern entries | Counting basis |
|---|---|---|
| microservices.io | 54 | unique pattern page links on the index |
| Azure Architecture Center | 44 | table rows in the patterns index |
| Tycho | 145 | registry catalogue entry_count |

Structural frameworks, not pattern catalogues:

| Framework | Units | Counting basis |
|---|---|---|
| arc42 | 12 sections | site states twelve sections |
| C4 model | 7 diagram types | 4 core plus 3 supplementary |
| AWS Well-Architected | 6 pillars | framework page |
| Google Cloud Architecture Framework | 5 pillars | framework page |

Learning corpora, not pattern catalogues:

| Corpus | Units | Counting basis |
|---|---|---|
| System Design Primer | 29 sections, 82 subsections, 15 topic areas, 8 designs | README headings |
| System Design Primer, links | 335 | unique external URLs |
| awesome-scalability | 12 categories, 921 links | README headings and URLs |
| Gentleman Book MCP | 18 chapters | server README |

Agent-facing services without a countable pattern corpus: Context7 (library
documentation, indexed set not published), GitMCP and DeepWiki (any public
repository), Microsoft Learn, AWS Knowledge and Google Developer Knowledge
(first-party documentation, page counts not published).

## Source traceability

| Corpus | Registered sources | Reading state | Per-claim binding |
|---|---|---|---|
| Tycho | 275 | 64 read, 45 pending | yes, 116 patterns |
| System Design Primer | 0 (335 links) | none | no |
| awesome-scalability | 0 (921 links) | none | no |
| microservices.io | 0 register (54 pages) | none | inline references |
| Azure Architecture Center | 0 register (44 pages) | none | first-party authority |
| arc42, C4, ADR | 0 register | none | manual references |
| Gentleman Book MCP | 0 register (18 chapters) | none | no |
| Context7 | libraries, not published | none | source links |

Only Tycho publishes an admission state, a reading ledger and a per-pattern
evidence binding. No other compared corpus does, so this column cannot be
scored for them; it is "not published", not "zero".

## Normalised comparison

| Metric | Tycho | microservices.io | Azure |
|---|---|---|---|
| Pattern entries | 145 | 54 | 44 |
| Dedicated pages per entry | 0.48 owner page | 1.0 | 1.0 |
| Sources per entry | 1.9 registered | not published | not published (1 page) |
| Evidence dimensions per entry | 4 | 0 | 0 |
| Failure and recovery verified | 37 of 145 | not measured | not measured |
| Agent surface | MCP, HTTP | none | via Learn MCP |

Reading of the ratios:

- Tycho has the widest pattern list: 2.7x microservices.io and 3.3x Azure.
- Tycho has the least page space per pattern: about two patterns share one
  owner page, while the other two catalogues give each pattern its own page.
- Tycho is the only catalogue that reports which share of entries has verified
  invariants (35%) and failure and recovery (26%). That is a depth statement
  the others cannot make because they do not measure it.
- Tycho's source register is larger than its evidence base: 275 registered,
  64 with a full reading record, 49 bound to pattern evidence. Register breadth
  is not coverage; the catalogue itself says pending records are not evidence.

## Findings

1. On pattern breadth, Tycho is the largest of the compared public catalogues
   by raw count. The count is not like-for-like: Tycho includes mechanisms and
   tactics such as timeout, TTL expiration and health probes, which Azure and
   microservices.io would not list as patterns. A conservative core-only
   comparison is 123 against 54 and 44.
2. On per-pattern prose, the two public catalogues are deeper: one page per
   pattern with context, solution, considerations and related patterns. Tycho
   keeps roughly two patterns per owner page and four evidence dimensions.
3. On source traceability, Tycho is alone among the compared corpora: 275
   registered sources with admission states and 116 patterns with at least one
   bound evidence source.
4. On verified depth, Tycho is thin where it matters most for decisions: 26%
   of patterns have supported failure and recovery, and no pattern is
   classified sufficient. The pattern count should not be marketed as 145
   complete treatments.
5. On reach, the link corpora dwarf everyone: 335 and 921 external links
   against Tycho's 275 sources. But links are not admitted sources, and neither
   corpus binds a source to a claim.
6. No compared pattern catalogue is agent-accessible as structured, cited
   content except Tycho and the 18-chapter Gentleman Book server. Vendor
   frameworks are reachable only through first-party documentation servers.

## What this means for claims

- "145 patterns" is supportable as a catalogue count if the unit is defined.
- "145 patterns with evidence" is not supportable: 116 have any binding, 37
  have verified failure and recovery, and all remain partial.
- "275 sources" is supportable as register breadth; 220 are admitted, 64 have
  a full reading record and 49 are bound to pattern evidence.
- Compared with 54 and 44 pattern pages, Tycho's breadth is real; compared with
  their one-page-per-pattern treatment, Tycho's per-pattern depth is lower.

## Limits

- Counts are a snapshot of 2026-10-27 and of the repository at HEAD.
- Counting rules are mechanical but unit definitions are editorial; a different
  rule would move the numbers by a few entries.
- Vendor page counts are not published, so no vendor corpus is scored.
- No measurement of answer quality, reader comprehension or maintenance cost.
- Commercial books and courses were excluded where chapter counts could not be
  verified.

## Reproduce

- Tycho: sources/register.json, edition/patterns/registry.v1.json,
  edition/patterns/owner-units.v1.json, edition/patterns/page-census.v1.json,
  edition/patterns/full-unit-reading-plan.v1.json.
- microservices.io: https://microservices.io/patterns/index.html, unique
  /patterns/*.html links excluding the index.
- Azure: MicrosoftDocs/architecture-center docs/patterns/index.md, table rows.
- arc42: https://arc42.org/overview. C4: https://c4model.com.
- AWS: https://aws.amazon.com/architecture/well-architected/.
- Google: https://cloud.google.com/architecture/framework.
- System Design Primer and awesome-scalability: raw README files on GitHub.
- Gentleman Book MCP: repository README.

Counts were produced with grep and the GitHub API on 2026-10-27.