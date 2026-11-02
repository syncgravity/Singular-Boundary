# Historical claim identity reconciliation — 2026-11-01

## Scope and evidence

The initial 246 flagged **legacy claim IDs** have all received explicit dispositions in [the flag crosswalk](HISTORICAL_FLAG_IDENTITY_CROSSWALK_2026-11-01.csv). Each corresponding occurrence in either snapshot is uniquely identified in [the source entry aliases](HISTORICAL_SOURCE_ENTRY_ALIASES_2026-11-01.csv).

The 246 flagged IDs represent **276 historical source ledger rows**. The 276 source-qualified aliases use `AUDIT:<legacy-id>:ROW<n>` or `MAIN:<legacy-id>:ROW<n>`; the row number is the *original CSV line*, and every alias points to a specific archived Git blob. This is identity reconciliation only. Namespaced aliases prevent accidental conflation even when a legacy claim ID was assigned to two unrelated results. Legacy records remain byte-for-byte intact.

## Evidence-preserving decision

- **15 conflicting single-entry IDs:** retain both rows as distinct attributed statements, pending theorem-body adjudication.
- **3 conflicted IDs with extra rows on main:** retain every occurrence individually; cannot choose authoritative claim text without source-level reading.
- **213 audit-only IDs:** preserve original branch-only identity and provenance; they are neither automatically new true theorems nor already integrated.
- **15 main-only IDs:** preserve the canonical main identity and document absence from the historical branch.

Duplicate occurrence flags within audit-only IDs are also separately indexed with row-qualified identities. The previous audit counted 12 additional repeated rows across the full datasets. This crosswalk records every flagged row rather than collapsing duplicate IDs.

## Important boundary

**246/246 identifiers now have a mechanical crosswalk, but 0/246 are certified here as mathematically reconciled.** The `SOURCE_UNVERIFIED` review status is intentional: no theorem content, numerical input, verifier run, commit graph, or external binary was independently certified by generating these tables.

This step cannot satisfy the [historical certification gate](HISTORICAL_RECORD_ACCEPTANCE_GATE_2026-11-01.md) alone. It prevents a dangerous data merge by giving unique identities to distinct claims.

## Next steps before single-main certification

1. Parse both preserved CSVs with a strict standard CSV reader and verify row structure; these preliminary source-qualified aliases are built from raw ledger rows and their initial column. Repair malformed records non-destructively, retaining original line locations.
2. For each alias resolve the primary-source path to an existing Git blob at the correct historical commit and read its mathematical content.
3. Build an explicit proposition-equivalence/supersession graph; substantiate every equal/changed assertion with source excerpts or proof.
4. Inventory *all* branch-only Git tree paths and commit ancestors, not just the limited 300-file GitHub comparison.
5. Validate the handoff verifier and its dependencies, original binaries and manifests, Git LFS remote readback, and fresh-clone scientific regressions.
6. Only after review, produce a unique, authoritative canonical ledger with alias backreferences, provenance and independent evidence statuses. Do not delete branch refs until their unique evidence has been preserved and verified.
