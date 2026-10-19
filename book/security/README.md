# Security architecture and trust-boundary decisions

## Purpose and mission

Connect authenticated identities, authorization, protected business objects and resource isolation to specific, testable system invariants. Security controls must be verified at the authority where the protected effect occurs, not only at ingress.

## Canonical chapter

- [Threat boundaries, identity, authorization and service isolation](identity-authorization-and-isolation.md) — threat worksheet, authentication versus authorization, policy enforcement, object-level access and multi-tenant boundaries, OAuth token audiences, service identity, failure matrix and original synthetic access-control scenario.

## Routes to adjacent material

- [Audit and trace correctness](../observability/trace-context-lineage-and-audit.md) — why best-effort logs and sampled traces do not replace authoritative audit.
- [Cross-domain modernization and ADRs](../decisions/cross-domain-modernization-and-adr-examples.md) — security/isolation constraints as hard architecture gates.
- [Safe release](../delivery/progressive-delivery-and-schema-evolution.md) — policy/config version changes and mixed-version compatibility.

**Status:** original source-linked chapter for E14-12; not a deployed policy, observed threat test, independent audit or proof of complete V09 coverage.
