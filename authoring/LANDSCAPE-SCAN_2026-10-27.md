# Landscape scan: public solutions adjacent to Tycho

Date: 2026-10-27. Status: bounded public-source scan for owner review.
It is not a market study, not an acceptance record and not competitive
intelligence on private or unreleased products.

> Issue [#547](https://github.com/rouslanbaranov/tycho/issues/547).
> Companion: [coverage comparison](COVERAGE-COMPARISON_2026-10-27.md).

## Research contract

- Reader: the Tycho owner, deciding positioning, distribution and next work.
- Primary question: do public solutions already cover what Tycho proposes?
- Subquestions: is a curated architecture book already served to agents with
  evidence and citations? Which projects provide only the serving layer? Where
  is the strongest overlap? What should Tycho not compete on?
- Exclusions: paid market reports, private or unreleased products, restricted
  material, answer-quality benchmarks, vendor roadmaps, user interviews.
- Required evidence: a working public link per named solution, repository
  metadata from the GitHub API, an access date and explicit unknowns.
- Completion: every named solution has a public link, a one-line overlap with
  Tycho, and the limits of the scan are recorded.

## What Tycho is in this comparison

A private repository containing an independently authored System Design book
(423 canonical pages), page metadata and evidence records, generated indexes,
a read-only MCP and HTTP service with 11 extractive tools, a qrels-based
lexical evaluation and an independence policy.

## Method

- GitHub repository search through the authenticated API, star-ranked, using
  terms such as documentation server, knowledge base, system design book,
  architecture, llms.txt, deepwiki, ADR and arc42.
- Repository metadata and README reads for every named candidate.
- Landing-page checks for hosted products.
- No crawling of documentation sites and no paid or private material.

## Answer in brief

The individual capabilities already exist publicly in mature form. The exact
combination that Tycho describes was not found in this bounded scan:

- curated, original architecture reasoning;
- per-page evidence, review and freshness states;
- extractive, snapshot-bound agent tools;
- calibrated abstention with unanswerable evaluation items;
- independence and neutrality governance.

The closest structural analogue is a small book-to-MCP project. The closest
serving layers are Context7, the Grounded Docs MCP Server and the first-party
knowledge servers from Microsoft, AWS and Google. The closest method
references are arc42, the C4 model and ADR practice.

Absence of a match is not proof of novelty. See the limits section.

## Properties used for comparison

1. Curated content: authored and edited architecture reasoning, not aggregated
   or generated text.
2. Evidence layer: sources, verification dates, review and freshness states,
   stable evidence identifiers.
3. Agent surface: MCP or HTTP tools that return cited text.
4. Retrieval discipline: calibrated abstention, extractive output, evaluation
   set with unanswerable cases.
5. Governance and identity: neutral origin rules, stable snapshot and
   document identifiers.

Tycho currently has all five in some form: the book and its metadata, the
read-only MCP contract with 11 extractive tools, the qrels set with 220 items
(65 unanswerable), and the independence policy. Its retrieval evaluation is
author-labelled, and independent adjudication is still open.

## Cluster 1: documentation and knowledge MCP servers

These solve "the agent needs current, cited documentation", not "the agent
needs curated architecture reasoning". This cluster is mature and crowded.

- **Context7** - hosted and open-source (MIT) service that serves current,
  version-specific library docs and code examples to agents. 63.8k stars;
  last push 2026-10-27. Overlap: cited, current docs through MCP. Gap:
  aggregated third-party documentation, no architecture synthesis and no
  independent evidence layer.
- **Grounded Docs MCP Server** - self-hosted indexer for websites,
  repositories, npm, PyPI and archives, with per-version indexes, full-text
  plus optional vector search, MCP over stdio and HTTP. 1.8k stars; MIT. It
  presents itself as an open-source alternative to Context7, Nia and Ref.
  Gap: infrastructure without a corpus.
- **GitMCP** - remote MCP that turns any public GitHub project into a
  documentation source. 8.5k stars; Apache-2.0.
- **Microsoft Learn MCP Server** - official remote endpoint with documentation
  search, page fetch and code-sample search over first-party content. 2.0k
  stars on the repository; CC-BY-4.0.
- **AWS Knowledge MCP Server** - hosted remote server over AWS docs, API
  references, What's New posts, blog posts, architectural references and
  Well-Architected guidance. Part of awslabs/mcp (9.8k stars, Apache-2.0).
- **Google Developer Knowledge MCP server** - first-party developer knowledge
  endpoint. Only the landing page was checked in this scan.
- **Ref** - documentation search MCP with token-efficient reads. 1.2k stars;
  MIT. The vendor site now leads with plan review, so the product focus may
  have changed; not verified.
- **docs.page** - serves Markdown from a public GitHub branch as docs with
  MCP, llms.txt and optional AI chat. 677 stars; Apache-2.0. It shows how
  low the cost of publishing a corpus to agents has become.

The documentation platforms moved in the same direction: Mintlify now markets
itself as "the documentation platform for agents", and GitBook as "the
knowledge layer for AI". "Docs for agents" is a product category, not a
novel feature.

## Cluster 2: repository-to-wiki generators

- **DeepWiki** (Cognition) - generated documentation for any public
  repository; the client-side repository has 103 stars. The hosted site
  returned a bot check during this scan, so behaviour was not verified.
- **deepwiki-open** - open-source wiki generator for public repositories.
  18.3k stars; MIT.
- **deepwiki-mcp** - MCP wrapper around the hosted service. 1.4k stars.

Overlap: instant breadth for any repository. Gap: generated text without
editorial ownership, evidence policy or review state. These systems optimise
for coverage, which is the opposite of Tycho's claim.

## Cluster 3: architecture methodology and reference corpora

- **arc42** - free, open template and manual for architecture documentation.
  1.3k stars on the template repository.
- **C4 model and Structurizr** - notation and "models as code" tooling. 503
  stars on Structurizr.
- **ADR practice** - adr.github.io, MADR (2.6k stars), an ADR example
  collection (17.3k) and adr-tools (5.7k). Local decision records, no hosted
  query surface.
- **microservices.io** - maintained pattern catalog on a public site.
- **Azure Architecture Center** (2.0k stars, CC-BY-4.0) and **AWS
  Well-Architected Labs** (2.2k stars) - first-party architecture guidance,
  partly reachable through the vendor MCP servers above.
- **System Design Primer** (375.8k stars), **system-design-101** (90.8k),
  **awesome-scalability** (75.1k), **The Architecture of Open Source
  Applications** (1.4k) - large study corpora. Overlap: reader attention.
  Gap: no agent surface and no evidence model; several are link collections.
- **MCP ADR Analysis Server** - 63 tools to validate project ADRs against
  code, detect drift and keep decision memory. 35 stars. Adjacent problem
  (local decision hygiene), not a knowledge service.
- **Gentleman Book MCP** - an MCP server over an 18-chapter software
  architecture book: list and read chapters, keyword search, optional
  embedding search, prompt templates. 144 stars; MIT; requires a local clone
  of the book. This is the closest structural analogue found.

## Cluster 4: knowledge infrastructure

- **Onyx** - 33.0k stars. Indexes 50+ applications, hybrid retrieval, agentic
  RAG and MCP actions. Bring-your-own corpus.
- **Graphiti** (32.3k), **Cognee** (32.8k), **mem0** (67.9k) - memory and
  knowledge-graph layers for agents.
- **llms.txt** - proposed convention for machine-readable site indexes
  (2.7k stars; directory with 919). An export format, not retrieval.
- **mcpdoc** - exposes llms.txt to editors. 1.0k stars; archived.

Gap across the cluster: no architecture content and no independent evidence
policy. These are substrates Tycho could use rather than rivals.

## Cluster 5: commercial, human-facing learning products

ByteByteGo and Design Gurus sell interview-preparation material. They compete
for reader attention but no agent interface was verified in this scan. They
are a substitute for the reader, not for the integration surface.

## Closest analogues, ranked by structural overlap

### 1. Gentleman Book MCP - closest shape

One book exposed as MCP tools. Overlap: chapter tools, search, semantic
search, prompt templates. Differences: no evidence metadata or review states,
no snapshot and citation contract, no abstention policy, no retrieval
evaluation, local clone required, one book, no governance. Lesson: the
"book as MCP server" pattern is already demonstrated, so the pattern itself
cannot be the differentiator.

### 2. Grounded Docs MCP Server - closest serving layer

Overlap: self-hosted, versioned indexes, MCP over stdio and HTTP, full-text
plus optional vector search. Differences: the corpus is external
documentation; no authored architecture reasoning, no evidence policy and no
refusal calibration.

### 3. Context7 - closest distribution

Overlap: exactly the job "give the agent current, cited context". Differences:
breadth over depth, aggregated sources, no cross-source synthesis, no
independence governance, no decision support. Lesson: generic documentation
retrieval is a red ocean; Tycho should not compete on plumbing or breadth.

### 4. First-party knowledge servers - closest authority

Microsoft Learn, AWS Knowledge and Google Developer Knowledge already put
authoritative architecture and operations guidance in front of agents, free.
Differences: vendor-scoped, no cross-vendor trade-off reasoning, no evidence
model beyond first-party authority. Risk: for vendor-specific questions,
agents will prefer these.

### 5. arc42, C4 and ADR - closest method

Overlap: the vocabulary and structure of architecture documentation.
Differences: templates and local records, not a queryable corpus.
Opportunity: explicit compatibility with arc42 sections and ADR framing would
make Tycho legible to existing practice.

## Comparison: content, evidence, agent surface

| Solution | Content | Evidence | Agent surface |
|---|---|---|---|
| Tycho | authored book | per-page sources | MCP, HTTP |
| Context7 | aggregated docs | source links | MCP |
| Grounded Docs | indexed docs | source URLs | MCP, HTTP, UI |
| GitMCP | repository docs | commits | MCP |
| Microsoft Learn | first-party docs | first-party | MCP |
| AWS Knowledge | first-party docs | first-party | MCP |
| DeepWiki | generated text | file links | MCP wrapper |
| Gentleman Book | one book | none found | MCP |
| Onyx | your connectors | citations | MCP actions |
| arc42, ADR | templates | none | none |

## Comparison: retrieval, governance, identity

| Solution | Retrieval | Governance | Identity |
|---|---|---|---|
| Tycho | BM25, qrels, abstention | independence rules | snapshot, evidence IDs |
| Context7 | search, no public eval | commercial, neutral | library and version |
| Grounded Docs | FTS plus vector | none found | versioned indexes |
| Microsoft Learn | semantic search | first-party only | service-managed |
| AWS Knowledge | search | first-party only | service-managed |
| DeepWiki | generated Q&A | none found | commit-based |
| Gentleman Book | keyword plus embeddings | none found | chapter IDs |
| Onyx | hybrid and agentic RAG | deployment-controlled | document IDs |

## What appears uncommon

In this bounded scan, no public solution combined curated architecture
reasoning, per-claim evidence states, extractive snapshot-bound tools,
calibrated abstention with unanswerable items, and independence governance.
Each property exists separately; the combination was not found.

This is absence of evidence, not evidence of novelty. The scan is bounded,
GitHub search is star-ranked, private and paid products are invisible, and
Tycho is small: 423 canonical pages in the current state record.

## Where analogues are ahead

- Freshness: Context7 and the vendor servers update continuously; Tycho
  depends on recorded re-verification.
- Scale: thousands of libraries and pages versus 423 pages.
- Distribution: marketplace listings and one-click installs. Context7 lists
  clients for Claude, ChatGPT, Cursor and VS Code; the Microsoft and AWS
  endpoints need no key.
- Semantic retrieval: embeddings are standard in the documentation-server
  cluster; Tycho's documented retrieval is lexical (BM25) with evaluation.
- Access control: bearer token only. OAuth and per-client authorization are
  not implemented.
- Generation speed: DeepWiki produces a wiki for any repository without
  authoring.

## Where Tycho is ahead

- Evidence and review states attached to pages, not only links.
- Refusal calibration with unanswerable items and an extractive-only tool
  contract that returns no verdict.
- Explicit independence and neutrality governance with a lexical check.
- Cross-vendor architecture reasoning instead of vendor documentation.
- A readable book that does not require the service.

## Risks

1. "MCP documentation server" is commoditized. A generic launch would be
   compared with Context7 and the vendor servers and would lose on breadth
   and freshness.
2. Discoverability: the name Tycho is already used by Eclipse Tycho (build
   tooling, 204 stars) and by a blockchain indexer (199 stars), which dilutes
   search results.
3. The repository is private with no external users at scan time, so no
   external validation exists.
4. Author-labelled evaluation without independent adjudication limits the
   claims that can be made.

## Options, with trade-offs

- **A. Own the evidence-grounded architecture niche.** Depth, decision
  support and refusal honesty. Cost: slow, small, hard to measure.
- **B. Become a source rather than a server.** Publish llms.txt and
  structured Markdown and let Context7, GitMCP or docs platforms index
  Tycho. Cost: less control and attribution risk.
- **C. Build the decision layer** (pattern atlas, comparison tools) that no
  analogue offers. Cost: the highest authoring effort and unproven demand.
- **D. Treat qrels and refusal policy as the product** - an evaluation
  harness for architecture questions. Cost: narrow audience.

These combine; A plus C with B for distribution is one shape. The choice
belongs to the owner and is not made here.

## Limits of this scan

- Public sources only, accessed 2026-10-27. Star counts and push dates are
  point-in-time.
- GitHub search is star-ranked; long-tail projects are missed by design.
- Vendor claims were read from repositories and landing pages, not exercised.
- No paid reports, private products, user interviews or answer-quality
  benchmarks.
- No claim about market size, adoption or commercial viability.

## Sources

Tycho internal references:

- [Current state](STATE.md)
- [MCP tool contract](MCP-AGENT-TOOL-CONTRACT.md)
- [Qrels evaluation](QRELS-EVALUATION.md)
- [Independence policy](../governance/INDEPENDENCE.md)

Documentation and knowledge servers:

- [Context7 repository](https://github.com/upstash/context7)
- [Context7 site](https://context7.com)
- [Grounded Docs MCP Server](https://github.com/arabold/docs-mcp-server)
- [GitMCP](https://github.com/idosal/git-mcp)
- [Microsoft Learn MCP](https://github.com/MicrosoftDocs/mcp)
- [AWS MCP servers](https://github.com/awslabs/mcp)
- [Google Developer Knowledge MCP](https://developers.google.com/knowledge/mcp)
- [Ref MCP](https://github.com/ref-tools/ref-tools-mcp)
- [docs.page](https://github.com/invertase/docs.page)
- [Mintlify](https://www.mintlify.com)
- [GitBook](https://www.gitbook.com)

Repository wikis:

- [DeepWiki client repository](https://github.com/CognitionAI/deepwiki)
- [deepwiki-open](https://github.com/AsyncFuncAI/deepwiki-open)
- [deepwiki-mcp](https://github.com/regenrek/deepwiki-mcp)

Architecture method and corpora:

- [arc42](https://arc42.org)
- [C4 model](https://c4model.com)
- [Structurizr](https://github.com/structurizr/structurizr)
- [ADR](https://adr.github.io)
- [MADR](https://github.com/adr/madr)
- [ADR examples](https://github.com/architecture-decision-record/architecture-decision-record)
- [adr-tools](https://github.com/npryce/adr-tools)
- [microservices.io](https://microservices.io)
- [Azure Architecture Center](https://github.com/MicrosoftDocs/architecture-center)
- [AWS Well-Architected Labs](https://github.com/awslabs/aws-well-architected-labs)
- [System Design Primer](https://github.com/donnemartin/system-design-primer)
- [system-design-101](https://github.com/ByteByteGoHq/system-design-101)
- [awesome-scalability](https://github.com/binhnguyennus/awesome-scalability)
- [The Architecture of Open Source Applications](https://github.com/aosabook/aosabook)
- [MCP ADR Analysis Server](https://github.com/tosin2013/mcp-adr-analysis-server)
- [Gentleman Book MCP](https://github.com/Alan-TheGentleman/gentleman-book-mcp)

Infrastructure and formats:

- [Onyx](https://github.com/onyx-dot-app/onyx)
- [Graphiti](https://github.com/getzep/graphiti)
- [Cognee](https://github.com/topoteretes/cognee)
- [mem0](https://github.com/mem0ai/mem0)
- [llms.txt](https://github.com/AnswerDotAI/llms-txt)
- [llms.txt hub](https://github.com/thedaviddias/llms-txt-hub)
- [mcpdoc](https://github.com/langchain-ai/mcpdoc)

Commercial learning:

- [ByteByteGo](https://bytebytego.com)
- [Design Gurus](https://www.designgurus.io)

Name collisions:

- [Eclipse Tycho](https://github.com/eclipse-tycho/tycho)
- [Propeller Heads Tycho](https://github.com/propeller-heads/tycho)

GitHub metadata was read through the authenticated GitHub API on 2026-10-27.
Star counts are rounded to one decimal place in thousands.