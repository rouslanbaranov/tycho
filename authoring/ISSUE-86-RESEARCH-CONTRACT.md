# Issue #86: high-load architecture research contract

Status: authoring plan; not a completed technical chapter.

Question: How do offered RPS, business TPS, concurrency, request cost, skew and growth change the architecture decision under explicit latency, correctness and availability requirements?

Scope: Little's Law and USL; vertical/horizontal scaling; autoscaling lag; admission and overload; retry budgets, bulkheads and load shedding; open/closed test models and coordinated omission. No private systems or performance claims.

Public evidence to verify: Gunther (2008) arXiv:0808.1431; Kubernetes HPA documentation; Envoy versioned circuit-breaker reference; Grafana k6 open/closed model; HdrHistogram coordinated omission; Google SRE overload chapters.

Acceptance: substantial original English pages, Mermaid with text alternatives, exact source-section ledgers, canonical navigation, local link and source-boundary checks. Report absent runtime tests honestly.
