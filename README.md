# Tycho

An independent, self-contained System Design book and planned MCP knowledge service for external AI agents.

Tycho explains engineering principles, architectural trade-offs, failure modes, and practical design reasoning through independently sourced public knowledge and original synthetic examples. It is not a description of any employer's systems.

## Non-negotiable boundary

References to employer-specific documents, sources, source code, internal technology usage, architectural decisions, or component names are strictly prohibited. This includes copied, paraphrased, translated, renamed, anonymized, reconstructed, or indirectly linked material. Employer names and abbreviations must not appear anywhere, including governance, examples, scanner rules, fixtures, or metadata.

Read [the independence policy](governance/INDEPENDENCE.md) before contributing. Every agent must follow [AGENTS.md](AGENTS.md).

## Start here

- [Book mission](book/README.md)
- [Authoring methodology](authoring/METHODOLOGY.md)
- [Current state and next action](authoring/STATE.md)
- [Roadmap](authoring/ROADMAP.md)
- [Knowledge platform and MCP delivery plan](authoring/knowledge-platform-and-mcp-plan.md)
- [Source catalogue](sources/CATALOG.md)
- [Coverage and research questions](sources/COVERAGE.md)
- [Implementation families](sources/IMPLEMENTATIONS.md)
- [Source register](sources/register.json)
- [Research contract template](templates/research-contract.md)

All repository content is written in English. Reading the book must not require access to private repositories, accounts, internal networks, another book, or an external agent service. External citations support verification; essential explanations belong in the book itself. Public source dependencies must be recorded explicitly.

## Current implementation

The repository contains governance, authoring rules, independently admitted public sources, technical System Design research drafts, generated catalogues, strict metadata/schema foundations and deterministic index/validation tooling. It is **not** a publication-complete ten-volume book: [the proposed 69-chapter contents](book/PROPOSED-STRUCTURE.md) and [living coverage audit](authoring/BOOK_COMPLETENESS_AUDIT.md) distinguish directly addressed questions from partial content and independent-review gaps. [Issue #213](https://github.com/rouslanbaranov/tycho/issues/213) owns completing the manuscript, and [Issue #214](https://github.com/rouslanbaranov/tycho/issues/214) owns the final volume/chapter/page edition assembly. The hosted ranked/semantic retrieval, MCP and shared specialist are later roadmap work. A manually curated concept graph is **not** part of Tycho's planned infrastructure. Source evidence and drafts do not certify independent editorial review, measured performance or deployment.

Run `python3 scripts/check_boundary.py` from the repository root. A successful scan detects none of the configured patterns; it does not certify independent origin or semantic correctness.

## Industry-neutral delivery

Describe deployment and compatibility requirements without naming a specific sector or institution. Use neutral descriptions such as `restricted enterprise environments`, `regulated environments`, and `security-constrained deployments`. This applies to docs, prompts, examples, code, filenames, issues and releases; see [governance/INDEPENDENCE.md](governance/INDEPENDENCE.md) and [AGENTS.md](AGENTS.md) for mandatory contributor rules.
