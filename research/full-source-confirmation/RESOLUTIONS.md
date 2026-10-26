# Full-source claim resolutions

Date: 2026-10-26. Refs #535.

Owner decisions on the completed full-source verification:

1. ASVS FS-22: accepted as `partially-supported`. The leveled, least-privilege,
   authorization and tenant-isolation elements are supported; trust-boundary framing
   remains unconfirmed. No trust-boundary claim may be cited to ASVS 5.0.0.
2. OpenID Federation FS-23: resolved by splitting the claim. The process clause is
   contradicted by Section 11.4. The narrower status-data clause is supported by
   Sections 8.7.2-8.7.3 and 8.4.2. The original removed claim is not reinstated.
3. EIP FS-06, FS-07, FS-08, FS-09, FS-11, FS-12, FS-13, FS-14, FS-15, FS-16 and
   FS-17: accepted as `partially-supported` at clause level, with
   `status_detail: clause-level-support; chapter-4-unavailable`. The original conjunctions
   are not fully supported. The publisher does not serve the complete book pattern text,
   and no substitute copy was used.
4. FS-10 (Pipes and Filters) is separate: its Chapter 3 pattern text is available and the
   claim is `partially-supported` with `status_detail: clause-level-support;
   universal-wording-unconfirmed`. It is not part of the Chapter 4+ range.

These are evidence dispositions, not sufficient coverage, independent AI review, CI or
acceptance of any book claim.
