# Editorial actions from high-severity comparisons

Research-only note. The book was not edited under #225.

## C384 and C386 — recovered

The GC article was recovered from a Wayback Machine snapshot dated 2025-05-16.
The archived full text confirms the 36% worst-case CPU result, the nearly 10%
generational-ZGC improvement, the 6-8% Parallel throughput gain with an hour
saved, the ~3% heap-size native-memory overhead and the huge-page discussion.
Both comparisons are reclassified as supported; no book edit is needed.

## C399 and C412 — still blocked

No lawful full text was obtained for the Java 21 pinning article:

- live publisher and Medium both return HTTP 403;
- Wayback holds only redirects to a Medium login flow;
- archive.today returned HTTP 429;
- reader mirrors provide generated summaries or derived copies, not the
  published article, and were not treated as the source of record.

Proposed editorial action, not applied here:

1. Replace the incident-specific account with the general JDK 21 pinning risk
   supported by JEP 444 and JEP 491.
2. Remove the four-carrier count, the CLOSE_WAIT socket detail, the six
   contenders, the reporter-lock observation and the 2024-07-29 date.
3. Keep the workload-dependent caution and the pointer to the unresolved
   publisher article as an open citation, not as verified evidence.

This requires a separate editorial branch because #225 is research-only and
must not change book content.
