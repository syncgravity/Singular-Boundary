# Research navigation — start here

This directory is an **additive navigation and editorial layer**, not a replacement for source proofs, raw data, or the append-only research record. Baseline: `main` commit `a2460cb2b5519d441d5fdaf7e94d6c2400f414da`, November 1/2, 2026.

## Read in this order

1. [Research checkpoint and scope](CURRENT_CHECKPOINT.md): what the recent work establishes and what is still open.
2. [Proof dependency map](PROOF_DEPENDENCIES.md): the P0–P5 tracks, assumptions, correcting documents, and blockers.
3. [All theorem records](THEOREM_INDEX.md): a navigable direct link to **every** currently indexed Markdown theorem file.
4. [Discovery and correction timeline](DISCOVERY_TIMELINE.md): how the research progressed; links to superseded and corrective work.
5. [Source and computation locator](SOURCE_AND_CODE_MAP.md): where scripts, original archives, manifests, and proof bundles belong.
6. [Claim-by-claim ledger](../../research/claims/CLAIM_LEDGER.csv): append-only historical evidence; statuses are *not* inferred from theorem titles.
7. [Evidence and review protocol](EVIDENCE_PROTOCOL.md): exact gates for “read”, “verified”, “reproduced”, and “publication-ready”.
8. [Research handoff](AI_RESEARCH_HANDOFF.md): instructions that prevent a future reader or AI from restarting completed investigations.

## Distinguish authoritative records from interpretation

* **Immutable source:** original transcript files, proofs, data and scripts (content-hash when present).
* **Research claim:** theorem and append-only ledger, scoped to its declared model and assumptions.
* **Navigational interpretation:** the pages in this directory, which may change as reconciliation improves.
* **Publication certification:** **not yet performed**; no independent equation-by-equation audit or universal replay is claimed.

The [November 1 publication proof map](../../research/audits/SINGULAR_BOUNDARY_PUBLICATION_PROOF_MAP_2026-11-01.md) is a dated historical audit. It predates some reconciliation claims; do not treat its P1 contradiction line as the final state. See [the correction chain](DISCOVERY_TIMELINE.md).

## Repository rules

Preserve every earlier theorem, counterexample, failed attempt and historical data byte. Create errata and supersession links rather than overwriting source history. Never cite an index as proof. Name the exact model, operator, dimension, coupling, boundary, sector and normalization with any mathematical claim.

## November 4, 2026 — Current full-tree inventory and research-resumption gate

The earlier 335-record theorem index remains a dated baseline. The [pinned 538-file theorem index](THEOREM_INDEX_SNAPSHOT_2026-11-04.md), [all 2,150 main-tree blobs](FULL_MAIN_TREE_SNAPSHOT_2026-11-04.csv), [claim/index coverage flags](THEOREM_TREE_COVERAGE_2026-11-04.csv), [historical branch-only paths](HISTORICAL_BRANCH_ONLY_TREE_2026-11-04.csv), and [all 11 branch differences](ALL_BRANCH_DIFFERENCES_2026-11-04.csv) are now available. These are **discovery and provenance inventories**, not mathematical proof certification.

Read the [repository-wide audit and selected P0 objective](REPOSITORY_REVIEW_AND_P0_OBJECTIVE_2026-11-04.md) before starting new calculations. The historical certification freeze remains in effect unless explicitly changed by the project owner. Avoid duplicating 202 theorem files and 94 scripts found only on the historical audit branch. Content-level review of all 2,150 tracked file bodies remains unfinished.

## November 4, 2026 — branch consolidation verified

**All 10 historical/non-main branch heads are now merged into `main` (Git ancestry verified; zero commits behind).** The historical audit merge brought 307 previously absent source paths, including 202 theorem files and 94 research scripts, without overwriting original theorem bodies or either conflicting claim ledger. The [current complete theorem index](THEOREM_INDEX_CURRENT.md) and [source-hashed registry](THEOREM_INDEX_LIVE.json) cover **754 of 754 tracked theorem files**. The [historical navigator](THEOREM_INDEX.md) preserves the original **740** records and appends the 14 later records. Source indexing does not certify the underlying mathematical claims. The source-qualified claim collision crosswalk remains intact. **The historical provenance/certification gate remains open, but Git branch merging is complete.** See [verified merge report](BRANCH_CONSOLIDATION_COMPLETED_2026-11-04.md). Branch pointers are retained solely for historical integrity.

## Repository branch consolidation and discoverability

The [branch lifecycle ledger](BRANCH_LIFECYCLE_2026-11-06.md) records the exact reviewed source-integration and remaining separate lines of work. Integrated historical branch refs can be **manually retired** through the ancestry-checking [GitHub Actions workflow](../../.github/workflows/retire-merged-branches.yml) without deleting merged commits. This action is disabled by default, protects open PRs and requires explicit confirmation; unmerged claims are not silently folded into `main`.
