# Tycho<br><sub>From architecture question to cited decision.</sub>

<p align="center">
  <a href="assets/tycho-station/tycho-station.jpg">
    <img src="assets/tycho-station/tycho-station.jpg"
         alt="An industrial ring-shaped construction station in deep space"
         width="100%">
  </a>
</p>

*Independent concept illustration of Tycho Station. Not an official production
asset; see [artwork notes](assets/tycho-station/README.md).*

**Tycho is an independent, source-grounded system-design knowledge product for
engineers and AI agents.** It combines a multi-volume book, a decision-oriented
pattern atlas, and a read-only MCP interface so a question can move from
orientation to a specific route, the trade-offs behind it, and the evidence that
supports it.

Tycho is built for engineers designing distributed systems, architects comparing
alternatives, and agents that need attributable technical context. It is not an
interview-answer mill or a generic chat wrapper: canonical explanations live in
the book, and every route is designed to lead back to public sources and explicit
limits.

<p>
  <a href="book/README.md"><img alt="System Design"
    src="https://img.shields.io/badge/System%20Design-1f6feb"></a>
  <a href="book/README.md"><img alt="Software Architecture"
    src="https://img.shields.io/badge/Software%20Architecture-6e40c9"></a>
  <a href="book/README.md"><img alt="Distributed Systems"
    src="https://img.shields.io/badge/Distributed%20Systems-0f766e"></a>
  <a href="book/volumes/v11-pattern-atlas/README.md"><img alt="Pattern Atlas 145 entries"
    src="https://img.shields.io/badge/Pattern%20Atlas-145-0f766e"></a>
  <a href="sources/CATALOG.md"><img alt="Evidence-Grounded"
    src="https://img.shields.io/badge/Evidence--Grounded-166534"></a>
  <a href="authoring/STATE.md"><img alt="Promoted 95 of 145 entries"
    src="https://img.shields.io/badge/Promoted-95%20of%20145-2ea043"></a>
  <a href="authoring/MCP-READ-ONLY-MVP.md"><img alt="MCP"
    src="https://img.shields.io/badge/MCP-111827"></a>
  <a href="authoring/MCP-AGENT-TOOL-CONTRACT.md"><img alt="AI Agents"
    src="https://img.shields.io/badge/AI%20Agents-c2410c"></a>
  <a href=".python-version"><img alt="Python 3.15.0"
    src="https://img.shields.io/badge/Python-3.15.0-3776ab"></a>
  <a href="sources/CATALOG.md"><img alt="360 admitted sources"
    src="https://img.shields.io/badge/Sources-360-166534"></a>
  <a href="authoring/STATE.md"><img alt="Active development"
    src="https://img.shields.io/badge/Status-active%20development-15803d"></a>
  <a href="LICENSE"><img alt="MIT License"
    src="https://img.shields.io/badge/License-MIT-0f766e"></a>
</p>

## How Tycho compares

Tycho sits between open study guides, commercial interview courses, reference
books, and AI documentation tools. The table reflects public product pages
reviewed on 2026-11-01; it is not an exhaustive market scan.

| Project | Open | Claim evidence | Agent | Coverage | Focus |
|---|---|---|---|---|---|
| **Tycho** | MIT | In progress | MCP candidate | Book + 145 patterns | Decisions |
| System Design Primer | CC BY 4.0 | Link list | No public MCP | Broad guide | Interviews |
| ByteByteGo | Commercial | Not advertised | No public MCP | Course library | Interviews |
| DDIA | Commercial | Bibliography | No public MCP | Data systems | Concepts |
| Hello Interview | Freemium | Not advertised | No public MCP | Interview topics | Interviews |
| Context7 | Open source* | Docs links | MCP | Docs index | Retrieval |

Claim evidence means sources are linked to claims at section or revision level,
not merely that a project has a bibliography. Agent means a public MCP or
comparable agent-facing retrieval interface. Coverage is a positioning label;
Tycho's pattern count is a catalogue count, not a claim that every entry has
passed the same evidence or review gate. Focus reflects public positioning.

\* Context7 is an open-source project with a hosted service; its public surface
is documentation retrieval rather than decision support.

Public pages reviewed: [System Design Primer](https://github.com/donnemartin/system-design-primer),
[ByteByteGo](https://bytebytego.com/),
[Designing Data-Intensive Applications](https://dataintensive.net/),
[Hello Interview](https://www.hellointerview.com/learn/system-design/in-a-hurry/introduction),
and [Context7](https://github.com/upstash/context7).

### Where Tycho is different

- **Broad, structured system-design coverage.** The [book](book/README.md) runs
  from requirements and application boundaries through concurrency, distributed
  coordination, data, retrieval, resilience, delivery, operations, decision
  support and modeling. The
  [pattern atlas](book/volumes/v11-pattern-atlas/README.md) catalogues 145
  patterns across 11 families. These are catalogue counts, not uniform evidence
  or review coverage.
- **Evidence layer, not just a bibliography.** Tycho is designed to bind
  material claims to exact public source sections and revisions, with support
  and limits recorded. This layer is in progress, and the README does not claim
  complete coverage.
- **One product, three surfaces.** The same canonical knowledge powers the
  book, the pattern atlas and the read-only MCP interface, rather than separate
  course notes or a chat-only answer engine.
- **Decision-first, not interview-first.** Tycho explains assumptions,
  alternatives, trade-offs, failure and recovery, and the conditions that
  reverse a choice. It is not optimized for memorized interview answers.
- **Independent and vendor-neutral.** Public sources and original synthetic
  examples; no single vendor's documentation is treated as the authority.
- **Agent-ready and reproducible.** Stable routes, snapshot-bound search and
  local validation make the knowledge usable by agents without a hosted black
  box. The MCP adapter remains a local candidate, not a production service.
- **Visible maturity.** Coverage, review state and known gaps are tracked in
  [Current state](authoring/STATE.md) instead of implied by marketing copy.

## Non-negotiable boundary

Tycho is independent and self-contained. It does not include or redistribute
unlicensed third-party copyrighted material, production assets, proprietary
documents, source code, internal datasets, or confidential information. Public
sources are cited and, where quoted, used only in bounded attributed excerpts
for verification. Explanations, comparisons, and synthetic examples are original
to the project or built from publicly accessible sources.

Tycho is not affiliated with, endorsed by, or derived from any third party's
internal systems. Read [the independence policy](governance/INDEPENDENCE.md)
before contributing. Every contributor must follow [AGENTS.md](AGENTS.md).

## Name and inspiration

The project name is a homage to Tycho Station from *The Expanse*. In the source
material, Tycho Station is the largest mobile construction platform in the Sol
system and the Belt headquarters of Tycho Manufacturing and Engineering
Concern: a shipyard and engineering hub, not a scientific research station. The
name may also echo Tycho Brahe, but the station's described role is industrial.

The project borrows the name as a reference to ambitious, inspectable
engineering. It does not treat the series as a source of technical facts;
Tycho's knowledge base is built from public engineering sources and original
synthetic examples. The project is independent and not affiliated with the
rights holders.

Public references:

- [Tycho Station — The Expanse Wiki](https://expanse.fandom.com/wiki/Tycho_Station)
- [Syfy](https://www.syfy.com/blogs/the-expanse-explore-the-solar-systems-biggest-space-station)

## Start here

- [Read the book](book/README.md)
- [Contributing](CONTRIBUTING.md)
- [Current state and next action](authoring/STATE.md)
- [Roadmap](authoring/ROADMAP.md)
- [Knowledge platform and MCP delivery plan](authoring/knowledge-platform-and-mcp-plan.md)
- [Read-only MCP candidate](authoring/MCP-READ-ONLY-MVP.md)
- [Local HTTP MCP container](authoring/MCP-LOCAL-HTTP-CONTAINER.md)
- [Agent-facing MCP tool contract](authoring/MCP-AGENT-TOOL-CONTRACT.md)
- [Source catalogue](sources/CATALOG.md)
- [Source register](sources/register.json)
- [Coverage and research questions](sources/COVERAGE.md)
- [Implementation families](sources/IMPLEMENTATIONS.md)
- [Authoring methodology](authoring/METHODOLOGY.md)
- [Research contract template](templates/research-contract.md)

All repository content is written in English. Reading the book must not require
access to private repositories, accounts, internal networks, another book, or an
external agent service. External citations support verification; essential
explanations belong in the book itself. Public source dependencies are recorded
explicitly.

## Development environment

Tycho pins **Python 3.15.0** for local validation, the premerge suite, milestone
verification and the container image. Use the version in `.python-version` and
install `requirements-validation.txt` before schema checks.

## Current state

Tycho is in active development. The book and pattern atlas are public; the
read-only MCP adapter is a local candidate; the source-to-claim evidence layer is
being expanded. Coverage, review status and remaining gates are tracked in
[Current state and next action](authoring/STATE.md) and
[Roadmap](authoring/ROADMAP.md).

## Industry-neutral delivery

Describe deployment and compatibility requirements without naming a specific
sector or institution. Use neutral descriptions such as
`restricted enterprise environments`, `regulated environments`, and
`security-constrained deployments`. This applies to docs, prompts, examples,
code, filenames, issues and releases; see
[governance/INDEPENDENCE.md](governance/INDEPENDENCE.md) and [AGENTS.md](AGENTS.md)
for mandatory contributor rules.

## License

Tycho is authored and maintained by **Ruslan Baranov**
([@rouslanbaranov](https://github.com/rouslanbaranov)) and is released under the
[MIT License](LICENSE).

Copyright © 2026 Ruslan Baranov.

Citation metadata is provided in [CITATION.cff](CITATION.cff).

The bundled concept illustration has separate provenance and rights limits; see
[artwork notes](assets/tycho-station/README.md).

Third-party sources cited in the book remain subject to their own terms; see the
[source register](sources/register.json).
