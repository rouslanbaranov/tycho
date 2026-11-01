# Judge rubric v2.1 — claim-level semantic support

This rubric applies to the next corpus (v8+). v7 is consumed; do not tune it.
The judge receives: question, answer, claims, evidence quotes, citations,
mechanical citation_resolution and required_anchor_coverage.

## One verdict per core claim

For every core claim emit a verdict:

```json
{
  "claim_id": "C1",
  "core": true,
  "verdict": "supported",
  "quote_id": "C1-E1",
  "reason": "the quote states the same unit, scope and threshold"
}
```

Verdict values:

- `supported`: the supplied quote entails the claim as stated, including
  number, unit, scope and direction.
- `partial`: the quote supports part of the claim, a weaker version, or only
  an adjacent fact; the missing part must be named.
- `unsupported`: the quote contradicts the claim, states a different number or
  unit, is only a topic mention, or is absent.

Every claim must have one verdict. A "pass" without a verdict row is invalid.

## Aggregate fields

- `semantic_support`:
  - 2: every core claim is `supported`;
  - 1: no core claim is `unsupported`, at least one is `partial`;
  - 0: any core claim is `unsupported`.
- `core_coverage`:
  - 2: every core claim has an answer statement and a verdict;
  - 1: one or more core claims are absent or verdictless;
  - 0: the answer does not address the question.
- `pass`: true only if `semantic_support == 2` and `core_coverage == 2`.
- `citation_resolution` and `required_anchor_coverage`: copy the supplied
  mechanical values. Do not reinterpret them as support.

## Entailment checks

Ask, in order:

1. Is the quote present and verbatim in the evidence ledger?
2. Does it state the same entity, action and direction as the claim?
3. Does it state the same number, unit and threshold?
4. Does it have the same scope: time window, population, boundary, failure class?
5. Does the claim add a causal or universal word ("always", "never", "prevents")
   that the quote does not license?
6. If the answer synthesizes multiple sources, does at least one quote entail
   each atomic part, or is the synthesis marked inference?

A topic mention is not support. A nearby number is not support. A correct main
mechanism does not cover a missing contraindication or branch.

## Calibration cases

These are rubric examples, not v7 tuning data.

1. Claim: "16->17 modulo retains 1/272 of keys." Quote states the modulo rule.
   Verdict: unsupported; the correct retention is 1/17. A surrounding correct
   explanation does not rescue it.
2. Claim: "The timeout is a local wait bound, not proof of failure." Quote says
   timeout may leave the effect committed. Verdict: supported.
3. Claim: "The cache removes the origin bottleneck." Quote says the cache
   reduces read load but not write load. Verdict: partial; name the missing
   write path.
4. Claim: "The system prevents duplicate effects." Quote says dedup has a
   bounded retention window. Verdict: partial; "prevents" exceeds the quote.
5. Claim: "The run converged." Quote reports relative error below 0.02.
   Verdict: supported for convergence, not for validity.

## Adjudication

Adjudication must use the same claim matrix. It may change a verdict only by
naming the quote and the missing or contradicted element. A task-level verdict
without a claim matrix is not accepted.

## Output rule

No `citation_valid` field. No single blended score. Report the four fields and
the claim matrix. The mechanical validator checks shape; the judge checks
entailment; a human or different-vendor reviewer checks calibration.
