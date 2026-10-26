# Accepted residual gaps

Date: 2026-10-26. Refs #535.

Owner decisions:

1. DDIA is accepted as blocked. No open full text was found; the Internet Archive copy is
   controlled digital lending and was not used. The unit remains `blocked-current`.
2. PostgreSQL Failover / Failback is accepted as partial. Section 26.3 was read, but the
   PostgreSQL 18 manual contains no failback procedure. A full-text search of the 18 A4 PDF
   (185,110 lines / 1,111,161 words) found zero occurrences of failback, RPO, RTO,
   recovery point objective, recovery time objective, restore verification or restore drill.
3. EIP Chapter 4+ remains `source-unavailable`. The author-hosted Chapter 3 PDF covers
   only Message Channel, Message, Pipes and Filters, Message Router, Message Translator
   and Message Endpoint. The full book or a legal Chapter 4+ copy is still required.
4. The five public-web claims FS-01, FS-02, FS-03, FS-19 and FS-20 are accepted as final
   `unconfirmed`. Their complete public pages (and the full PostgreSQL 18 manual for FS-20)
   do not state them; no further public text search is planned.
5. FS-21 is reclassified as `partially-supported` after external review. External probing,
   geographic probe locations, false-positive confirmation, browser probes and artificial
   activity are supported; the exact definition and the explicit-design rule remain
   unconfirmed.
6. The eleven EIP claims whose patterns are in Chapter 4 or later are accepted as final
   `partially-supported` at clause level. The publisher withholds Chapter 4+, so the original
   conjunctions are not fully supported; Chapter 3 and the public pattern pages support only
   the clauses listed in each claim record. No open authorized mirror was found.
7. FS-10 (Pipes and Filters) is separate: its Chapter 3 text is available and the claim is
   `partially-supported` with `status_detail: clause-level-support;
   universal-wording-unconfirmed`.

No sufficient coverage, independent AI review, CI or acceptance of a book claim is
implied.
