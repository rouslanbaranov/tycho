# Tycho roadmap

Updated: 2026-10-18.

1. **Foundation — established.** Preserve project independence, agent rules and boundary checks.
2. **Public-source discovery — first pass complete.** Maintain the source register, coverage map, implementation map, access limitations and research gaps. Discovery is not full reading.
3. **Architecture decision layer — planned; next design step.** Define requirements/workload and legacy profiles, pattern applicability cards, candidate comparison, target and transition architecture models, evidence-backed ADRs and decision routes. Follow [the detailed work plan](architecture-decision-layer-plan.md).
4. **Book and pilot design — planned.** Propose audience, question-driven table of contents and three bounded pilot contracts. Use the decision-layer models to connect knowledge to practical choices.
5. **Knowledge contracts and tooling — planned.** Implement and exercise strict metadata/source schemas, a generated chapter index, structural/link validation and minimal graph integrity checks where a graph is justified. Preserve existing source checks.
6. **Pilot research and evaluation — planned.** Research one mechanism, one end-to-end process and one recovery scenario. Evaluate both explanation and decision quality, including a case where evidence is insufficient to recommend a change.
7. **Book authoring — planned.** Adapt the methodology from pilot findings, then author in dependency order with bounded checkpoints and canonical ownership.
8. **Retrieval and delivery — deferred until justified.** Evaluate actual questions before selecting lexical search, embeddings or MCP delivery.

## Dependencies and completion boundaries

Decision-model design precedes pilot finalization. Source research and exact version/section pinning provide the evidence for applicability claims. Agree metadata semantics before encoding them in schemas or graphs. Validate the decision process in the pilots before broad population.

The next deliverable is a proposed model and usable templates, not an automatic architecture selector. Proposed relations, sample decisions and templates do not establish that the full decision layer has been implemented or evidence-reviewed. No whole-book generation, benchmark execution, migration of a real system or infrastructure deployment is authorized by this roadmap alone.
