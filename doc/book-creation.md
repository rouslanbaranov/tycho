# How the book was built

Tycho did not start as a finished 12-volume book. It started as a System Design
reference candidate with a small set of research contracts, then grew through a
sequence of bounded decisions about evidence, structure, review and modelling.

This document is a construction history, not a claim that the book is complete.
It describes the major phases, the obstacles that shaped them and the decisions
that remain visible in the repository.

## The starting point

The original product direction was a self-contained System Design book that
could also serve as a machine-readable knowledge source. The project deliberately
avoided building a second corpus, importing a private source base or treating a
vendor's documentation as universal authority.

The early structure was a bounded set of research contracts, a source register
and chapter manuscripts. The source register established public origin,
publisher, version and access notes. The research log recorded what was read and
what remained unknown.

## Phase 1: the 69-manuscript baseline

The first major milestone was a set of 69 primary chapter manuscripts across ten
volumes. The owner confirmed substantive acceptance at
`986b1ddbe985079b7c647182fcf1c2fc8911d96c`; PR #218 recorded the merged
baseline. This did not mean every source was fully read or every claim had
section-level evidence. It meant the manuscript set was accepted as a content
baseline.

The same period added 29 public historical case studies and six synthetic
decision playbooks. These became an applied reading layer rather than an
eleventh volume.

## Phase 2: readable structure and the atlas

The next problem was navigability. A large book with numeric paths and
inconsistent landings is hard to use and hard to validate. The project performed
a readable directory migration while preserving document identity, historical
paths and inverse mapping.

The pattern atlas became a separate volume (V11). It started as a catalogue of
patterns and grew into a decision-oriented layer with:

- 145 entries across 11 families;
- owner units and decision cards;
- shared-page classification;
- coverage states and promotion records;
- source and decision evidence for each entry.

The atlas is not a second book. It routes decisions to canonical owners.

## Phase 3: the evidence and promotion program

The hardest problem was not writing more prose. It was deciding when a pattern
entry was actually supported.

The project introduced:

- a source register and reading ledger;
- a source plan per entry;
- technical and decision dimensions;
- one-entry-at-a-time promotion;
- independent AI review with saved reports;
- hash-bound owner pages and cards;
- owner acceptance as a separate decision;
- timing and forecast bookkeeping.

This phase changed the unit of progress from "a chapter was written" to "an
entry passed a bounded gate." It also created a visible queue: 104 of 145 entries
are currently sufficient; 41 remain.

The current promotion records have 104 entries, 94 owner-accepted entries and 80
saved review reports. The promotion timing record covers 84 cycles with a mean of
57.0 minutes, a median of 34.5 minutes and a range of 6-406 minutes.

## Phase 4: V12 modelling

V12 added an executable modelling layer rather than more prose. It introduced:

- three models (checkout, order intake, modernization path);
- ten scenarios and ten seeded runs;
- two decision records;
- a deterministic engine with replay hashes;
- convergence, uncertainty and invariant checks.

The checkout decision recommends candidate B under declared synthetic
constraints. The modernization decision returns `insufficient-evidence` because
rollback and dual-write assumptions are not measured. Both outcomes are
deliberately conditional.

V12 is isolated: it does not rewrite existing book pages or promotion records.

## Current shape

| Volume | Chapters | Markdown documents |
|---|---:|---:|
| V01 Requirements and architecture | 6 | 30 |
| V02 Application boundaries and contracts | 7 | 31 |
| V03 Execution, concurrency and flow control | 6 | 29 |
| V04 Distributed coordination and events | 8 | 48 |
| V05 Data models, engines and lifecycle | 8 | 37 |
| V06 Caching, indexing and retrieval | 7 | 35 |
| V07 Performance, scale and resilience | 7 | 32 |
| V08 Delivery, deployment and recovery | 8 | 43 |
| V09 Observability, security and operations | 7 | 35 |
| V10 Decision support and modernization | 7 | 37 |
| V11 Pattern atlas | 11 | 157 |
| V12 Modelling and simulation | 7 | 31 |
| **Total** | **89** | **612** |

The 69-manuscript baseline is a historical milestone, not the current chapter
count. Structural pages, landings, case pages and the atlas/V12 volumes were
added later.

## Obstacles and how they were handled

### Independence and restricted-origin material

The project had to remain independent of private systems and non-public sources.
The response was a source admission policy, a public source register, a
clean-creation boundary and a lexical boundary check. When restricted-origin
references were found, they were removed from the current tree and the affected
contract was retired. History remains a separate owner decision.

### Review capacity

A single reviewer cannot review every page at once. The project moved to bounded
packets, one entry at a time, saved reports and hash-bound artifacts. The cost is
visible: review and integration waits dominate the timing distribution. The
benefit is that a promotion is inspectable.

### Evidence depth

A bibliography does not support a decision. The four technical dimensions and
the decision fields forced the project to distinguish source claims, synthesis,
inference and missing evidence. Some entries remained partial rather than being
declared complete.

### Generated-artifact drift

Routes, indexes, inventory, qrels and V12 artifacts can go stale silently. The
project added deterministic builders, freshness checks and premerge validation.
The recurring lesson is that a generated count must be rebuilt, not edited by
hand.

### V12 replay stability

Committed runs must replay to the same hash. That property is sensitive to the
interpreter and to generator drift. The project pinned Python 3.15.0, regenerated
the runs and recorded provenance. The remaining lesson is that reproducibility
is an environmental property, not only a code property.

### Documentation drift

As the project grew, old status banners, counts and Russian report templates
survived longer than the facts they described. The production documentation pass
replaced stale banners, updated the current counts and translated the promotion
templates to English. Historical records remain historical.

## Decisions that still matter

- **Book first, but not book only.** The book is the canonical explanation; the
  atlas and MCP are routing surfaces.
- **Evidence before coverage.** A pattern is not sufficient because it exists.
- **One entry at a time.** Parallel promotion makes review and hashes ambiguous.
- **Public sources and synthetic examples.** No private corpus enters the product.
- **Generated indexes are disposable.** Canonical content is not.
- **Models are conditional.** A simulation result is not a production measurement.
- **No silent CI claim.** Milestone verification is separate from local checks.

## What remains

- 41 entries are still partial.
- 10 promotions are acceptance-pending.
- 213 of 366 sources lack complete-content verification.
- V12 is uncalibrated.
- MCP is a local candidate, not a production service.
- The current tree still contains historical review reports and broken links in
  archived artifacts; these are evidence records, not current guidance.
- Source catalogue freshness remains a known premerge blocker on the current
  baseline.

The project's production standard is therefore not "everything is complete". It
is "the current state, evidence, review and limits are visible, and no claim is
stronger than its record."
