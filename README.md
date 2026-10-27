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
- [Read-only MCP stdio candidate](authoring/MCP-READ-ONLY-MVP.md)
- [Local HTTP MCP container](authoring/MCP-LOCAL-HTTP-CONTAINER.md)
- [Agent-facing MCP tool contract](authoring/MCP-AGENT-TOOL-CONTRACT.md)
- [Source catalogue](sources/CATALOG.md)
- [Coverage and research questions](sources/COVERAGE.md)
- [Implementation families](sources/IMPLEMENTATIONS.md)
- [Source register](sources/register.json)
- [Research contract template](templates/research-contract.md)

All repository content is written in English. Reading the book must not require access to private repositories, accounts, internal networks, another book, or an external agent service. External citations support verification; essential explanations belong in the book itself. Public source dependencies must be recorded explicitly.

## Readable book directories

Volumes and chapters now use `vNN-<description>/cNN-<description>/` under `book/volumes`. The [directory migration record](authoring/DIRECTORY_MIGRATION_2026-10-20.md) records all ten volumes, 71 chapters and the retained 406 document identities. #214 remains open for substantive acceptance.

## Current enrichment candidate — 2026.10.1-rc.3

**[Read the ten-volume manuscript](book/README.md).** The candidate contains 71 chapters and 406 canonical documents. This pass adds configuration rollout, session consistency, offline conflicts, cells/shuffle sharding and protocol verification, plus complete catalogue, collaboration and multitenant-service projects. It retains the earlier object-storage/network additions, twelve deepened pages and all existing identities/source blocks.

[The second-pass contract](authoring/SECOND_ENRICHMENT_CONTRACT_2026-10-20.md) records the scope. [Executed validation](authoring/PYTHON_MERMAID_VALIDATION_2026-10-20.md) records 16/16 Python check groups, 233/233 tests with zero skips, and 221/221 Mermaid syntax parses. Python reproduced the candidate index byte for byte. The earlier environment block is resolved.

[PR #222](https://github.com/rouslanbaranov/tycho/pull/222) is merged; #214 remains open for integration verification and substantive page acceptance. The historical 2026.10.0 snapshot is unchanged.

## Industry-neutral delivery

Describe deployment and compatibility requirements without naming a specific sector or institution. Use neutral descriptions such as `restricted enterprise environments`, `regulated environments`, and `security-constrained deployments`. This applies to docs, prompts, examples, code, filenames, issues and releases; see [governance/INDEPENDENCE.md](governance/INDEPENDENCE.md) and [AGENTS.md](AGENTS.md) for mandatory contributor rules.

## License

Tycho is authored and maintained by **Ruslan Baranov**
([@rouslanbaranov](https://github.com/rouslanbaranov)) and is released under the
[MIT License](LICENSE).

Copyright © 2026 Ruslan Baranov.

Citation metadata is provided in [CITATION.cff](CITATION.cff).

Third-party sources cited in the book remain subject to their own terms; see the
[source register](sources/register.json).
