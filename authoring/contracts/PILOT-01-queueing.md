# Pilot research 1 — queueing, Little's Law and arrival-rate measurement

- **Contract ID:** TYCHO-PILOT-MECHANISM-v0.1
- **Issue / owner:** [#38](https://github.com/rouslanbaranov/tycho/issues/38), draft V07/C01 in the [proposed structure](../../book/PROPOSED-STRUCTURE.md)
- **Status:** bounded source-reading and authoring contract, **not** a researched chapter.
- **Reader / decision supported:** designer diagnosing whether rising request latency, backlog and concurrency come from arrivals, service demand, resource saturation or measurement artifacts.
- **Primary question:** With an explicit request boundary, when and how does `L = λW` constrain long-run mean in-system work, and why does that identity alone **not** size thread pools, predict tail latency or justify an architecture?
- **Why this pilot first:** provides a mechanism with a mathematically constrained claim, independently specified load-generation semantics and falsifiable examples. It is a prerequisite for later load-driven architecture decisions.
- **Synthetic scenario:** a fictional stateless API with a bounded downstream dependency. Define offered arrivals, completed throughput, waiting+service time, outstanding work and overload/rejection events separately. Specify one stable scenario, one transient burst and one intentionally unanswerable capacity question.

## Inclusion / exclusion

**In:** flow boundary and units; arrival/throughput and in-flight means; queue vs service; finite-window effects; percentile-versus-mean; open-versus-closed load models; failure/saturation and honest unknowns; one original, unit-checked synthetic numeric illustration and counterexample.

**Out:** universal concurrency or RPS thresholds, an empirical throughput benchmark, estimating future production hardware from a single formula, complete queueing theory derivations, validating a specific infrastructure configuration, probabilistic SLO predictions without data.

**Target content pages:** V07/C01 orientation and definitions; Little's Law applicability; overload and measurement protocol. Start with **one coherent canonical technical page** and split only if evidence/complexity makes independent reading necessary.

## Independently public evidence — bounded scope

The following IDs already exist in [the public source register](../../sources/register.json); source discovery does not mean a claim has been verified. Exact sections are **reading targets**; the PR for #38 must record what it actually inspected.

| Source ID | Edition / document | Required exact sections or paragraph scope | Intended claim and limitation |
|---|---|---|---|
| `src.little-law` | Kim & Whitt, *Statistical Analysis with Little's Law*, *Operations Research* 61(4), 2013, DOI 10.1287/opre.2013.1193; [public author PDF](https://www.columbia.edu/~ww2040/LL_OR.pdf) | Abstract; §§1, 1.1–1.2, **§2** finite-time measurement relations and boundary/edge effects | Distinguish long-run/stationary law from finite-window estimators and their edge effects. Do not claim all statistical refinements §§3–7 are read without actual inspection. |
| `src.k6` | Grafana k6 online documentation, page [Open and closed models](https://grafana.com/docs/k6/latest/using-k6/scenarios/concepts/open-vs-closed/); version/retrieval date must be recorded when writing | **Closed Model**, **Drawbacks of using the closed model**, **Open model** | Arrival scheduling can depend on completion or be independently paced; test-model validity and coordinated omission need interpretation. Do not claim target throughput was reached without execution. |
| `src.sre-overload` | Public SRE book, [Handling Overload](https://sre.google/sre-book/handling-overload/) | Rate-limiting / client-side throttling and server-side considerations as actually available | Overload policy changes admitted/completed rates. Do not make detailed control/architecture claims from a landing-page title. |

Only registered, independently public references are permitted. A source URL points to an origin, not an authorization to reproduce full text or charts.

## Research questions and alternative interpretations

1. What is the counted entity and start/end boundary? Is the system steady enough for long-run means?
2. Are arrivals *offered*, admitted or completed? Under timeouts/rejections which of these is `λ` in the stated law?
3. Does `W` count queueing plus service? Is it a **mean** of relevant entities rather than p95/p99?
4. If observed numbers are finite-window averages, is there nonzero in-flight work at the beginning/end? What correction/uncertainty remains?
5. Can a closed-model load generator reduce offered traffic when latency increases? Which open-model experiment exposes the difference?
6. Which measured bottleneck and recovery experiments would be required before proposing more servers, partitioning or a queue?

## Minimum original synthetic tests

- Stable illustrative hypothesis: completed λ=120/s, mean W=0.20s, derive average L=24 at one named boundary. Numbers are not measurements. Compare with a tail-latency statement and show why it is **not** substitutable.
- Hypothetical burst: offered load exceeds service completion for 30s; distinguish backlog, rejected traffic, and mean work; do **not** assume stationary equality during the burst.
- Missing-evidence case: no arrival distribution, service-demand measurements or downstream capacity known. Return **measure first**, with open-arrival test plan, instrumented queue length, response-time distribution, rejection/error rate and confidence/sampling description.

## Acceptance and gate to finish #38

- Correct definitions/units and explicit assumptions, with a source-to-claim ledger citing exact verified sections.
- Mechanism and at least one counterexample; explain normal flow, saturation, overload and recovery limits.
- One unit-checked, **original and labelled synthetic** case; no copied published data.
- Explain why Little's Law alone does not determine resource sizes, concurrency caps or feasibility.
- Record actual reading, source versions/retrieval dates, contradictions, uncertainty and review level.
- Run configured source-boundary/source-inventory checks; manually verify local links; add simple reproducible arithmetic tests where useful. An unresolved primary-source passage is a real blocker for that claim, not an excuse to invent it.
- Stop after one canonical evidence-backed question is answered. **No broad book generation.**
