# Product overview

Tycho is an independent, source-grounded system-design knowledge product for
engineers and AI agents. It combines a multi-volume book, a decision-oriented
pattern atlas, an evidence and promotion layer, a deterministic modelling volume,
and a read-only MCP interface.

The product is designed to answer a narrower question than a general chatbot:

> Given a system-design decision, which canonical explanation, pattern,
> evidence and decision record should I read, and what remains unknown?

Canonical explanations live in the book. The atlas provides decision-oriented
entry points. The evidence layer connects claims to public sources. V12 turns a
small set of assumptions into explicit model runs and conditional decisions. The
MCP layer exposes the same knowledge as bounded, read-only tools.

## The problem

System-design material is usually one of four things:

1. a broad study guide with links but no claim-level evidence;
2. a commercial course or book with a bibliography but no machine-readable
   evidence graph;
3. vendor documentation that is authoritative for its own interface but not
   neutral across alternatives;
4. a chat interface that produces plausible prose without stable citations.

Tycho's target is different: **a decision support surface whose claims can be
traced to public sources and explicit limits, while remaining readable as a
book.** It is not an interview-answer mill and does not claim to replace
engineering judgment.

## Audience

- Engineers designing or reviewing distributed systems.
- Architects comparing alternatives under explicit constraints.
- Technical writers and researchers who need claim-level provenance.
- AI agents that need bounded, attributable context rather than a generated
  final answer.

## Three surfaces, one canon

| Surface | Role | Canonical artifact |
|---|---|---|
| Book | Explains mechanisms, trade-offs, failure and recovery | `book/volumes/` |
| Pattern atlas | Routes a decision to an entry and owner section | `v11-pattern-atlas/` |
| MCP | Exposes bounded search, read, evidence and pattern tools | `mcp/` |

The surfaces are not separate corpora. Search and MCP resolve the same canonical
book paths, metadata and source IDs. V12 adds a modelling layer whose artifacts
are exposed through the search index and MCP without rewriting the book.

## What is in the product

| Capability | What exists now | Evidence |
|---|---|---|
| Book | 12 volumes, 89 chapters, 612 Markdown documents | [Book](../book/README.md) |
| Pattern atlas | 145 entries across 11 families | [Atlas](pattern-atlas.md) |
| Evidence layer | 104 entries technically and decision sufficient | [Evidence](evidence-layer.md) |
| Owner acceptance | 94 of 104 promotions accepted | `sufficient-owner-acceptance.v1.json` |
| Sources | 366 registered public sources | [Register](../sources/register.json) |
| V12 | 3 models, 10 scenarios, 10 runs, 2 decisions | [Modelling](modelling-and-simulation.md) |
| Route index | 612 documents, 3,190 citable sections | [Index](index-and-search.md) |
| MCP | 11 read-only tools, stdio and HTTP | [MCP](mcp-layer.md) |
| Tests | 709 core and 123 MCP test definitions | [Tests](tests-and-coverage.md) |
| Benchmarks | Qrels, retrieval and V12 evaluation suites | [Benchmarks](benchmarks.md) |

Counts are catalogue counts. They do not imply that every entry has the same
review depth or that the whole corpus has been read.

## Features

### Source-grounded explanation

Material claims are connected to admitted public sources, exact sections or
revisions, and stated limitations. The evidence layer records source support
separately from Tycho synthesis. See [Evidence layer](evidence-layer.md).

### Decision-first atlas

Each atlas entry has an owner unit, a decision card, applicability conditions,
contraindications, related entries and a source note. Promotion to `sufficient`
requires technical and decision evidence plus independent review. See
[Pattern atlas](pattern-atlas.md).

### Reproducible modelling

V12 provides deterministic, seeded discrete-event and stock-and-flow models.
Runs record provenance, convergence, invariants, uncertainty and result hashes.
Decision records distinguish `decision-supported` from `insufficient-evidence`.
See [Modelling and simulation](modelling-and-simulation.md).

### Bounded retrieval

The route index and section index provide stable IDs, snapshots, citations and
bounded reads. The default search layer is lexical; semantic and hybrid
experiments are documented separately. See [Index and search](index-and-search.md).

### Read-only MCP

The MCP server exposes search, outline, page, read, context, compare, batch,
pattern and evidence tools. It returns evidence, not final answers, and keeps a
snapshot ID on results. See [MCP layer](mcp-layer.md).

### Explicit validation

Validators cover source records, metadata, book navigation, edition inventory,
V12 contracts, qrels and MCP schemas. The test suite covers both core and MCP
surfaces. See [Tests and coverage](tests-and-coverage.md).

## How Tycho compares

The comparison is about public product surfaces, not a claim that competitors
are deficient. The table is adapted from the README and should be rechecked
before publication.

| Project | Open | Claim evidence | Agent | Focus |
|---|---|---|---|---|
| **Tycho** | MIT | In progress | MCP candidate | Decisions |
| System Design Primer | CC BY 4.0 | Link list | No public MCP | Interviews |
| ByteByteGo | Commercial | Not advertised | No public MCP | Interviews |
| DDIA | Commercial | Bibliography | No public MCP | Concepts |
| Hello Interview | Freemium | Not advertised | No public MCP | Interviews |
| Context7 | Open source* | Docs links | MCP | Retrieval |

Tycho's differentiators are the combination of:

- a book and a decision atlas under one canonical model;
- an evidence and promotion layer with explicit review records;
- deterministic V12 models with recorded uncertainty and limits;
- a read-only MCP surface over the same canonical paths;
- public, reproducible validators and generated indexes.

The differentiators are not claims of complete coverage. The evidence layer is
still expanding, V12 is uncalibrated, and the MCP service is a local candidate
rather than a hardened production deployment.

## Source base

| Reading status | Sources |
|---|---:|
| Full public page inspected | 137 |
| Landing page or abstract inspected | 180 |
| Fetch incomplete | 49 |
| **Total** | **366** |

Content verification is recorded for 153 sources; 213 have no complete-content
verification. These are source-level states, not a claim that every section of a
verified source was used.

## Maturity and limits

- The book is public and substantial, but evidence coverage is uneven.
- 104 of 145 atlas entries are sufficient; 41 remain partial.
- 94 promotions are owner-accepted; 10 remain acceptance-pending.
- V12 models are synthetic and uncalibrated.
- MCP is read-only and locally verified; it is not a production service.
- CI is milestone-only; a passing local check is not CI.
- No claim of independent human review or complete source reading is made.

## Start reading

- [README](../README.md) for the public entry point.
- [Evidence layer](evidence-layer.md) for how claims become trustworthy.
- [Pattern atlas](pattern-atlas.md) for the decision catalogue.
- [Book creation](book-creation.md) for the construction history.
- [MCP layer](mcp-layer.md) for the machine interface.
