# Canonical historical record: verification acceptance gate

**Date:** 2026-11-01  
**Status:** BLOCKED — not yet a single verified historical record.

The canonical `main` research ledger must not be treated as a single reconciled history until every condition below is satisfied. The historical source branches are retained, and no conflicting claim is silently chosen or deleted.

## Source-preserving ledger snapshots

These two independent copies were retrieved through GitHub and reread after commit. Their Git blob SHA-1 and full fetched text were identical to the original source files.

| Source at retrieval | Immutable Git blob | Archival copy |
| --- | --- | --- |
| `audit/2026-10-28-independent-reconstruction:research/claims/CLAIM_LEDGER.csv` | `e8ebdd08af49cc7bf4bb0230a402b9fec895515e` | [Audit ledger](../../research/evidence/ledger_snapshots/CLAIM_LEDGER_AUDIT_2026-11-01.csv) |
| `main:research/claims/CLAIM_LEDGER.csv` before archive commit | `29fec994bd0f9c65ba0c0be91cea374f51763985` | [Main ledger](../../research/evidence/ledger_snapshots/CLAIM_LEDGER_MAIN_2026-11-01.csv) |

A Git blob SHA-1 identity proves bytes copied unchanged **within this Git record**, not the truth of any mathematical assertion or the availability of cited external datasets. The branch with these copies must itself be merged and reread before treating the copy as canonical preservation.

## Acceptance conditions: all required

- [ ] Full commit and file-tree inventory of every historical branch, not the truncated 300-file comparison; include branch head SHAs and a three-way merge-base analysis.
- [ ] Immutable originals preserved with hashes, explicit provenance and retrieval audit; identify missing/ephemeral original binary datasets, transcripts, script dependencies and attached proof bundles.
- [ ] All collided IDs (including distinct propositions using the same `R3-IR-373`–`390` labels) mapped to separate canonical immutable IDs; preserve original names as aliases with source refs.
- [ ] Each historical claim independently classified as identical, superseded/corrected, distinct, conditional, numerical, retracted, unsupported, or open. No deletion of contrary evidence.
- [ ] A machine-validated canonical registry with no ambiguous canonical IDs, supporting provenance links for both historical sources and audit decisions.
- [ ] All branch-only theorem files, scripts and data manifests either integrated through reviewed PRs, recorded as duplicate byte-identical objects, or explicitly quarantined as missing/unverified with concrete reasons.
- [ ] Historical ZIP/NPZ originals independently hashed and retrieved from durable storage. Library-only or conversation-only assets cannot count as verified in Git.
- [ ] Reproducibility verifier subjected to malicious ZIP path, duplicate, missing, length, hash, symlink, and bundle-specific manifest tests; CI/test results recorded.
- [ ] Canonical README, current checkpoint, research navigator, correction chain and claim registry updated to refer to the same verified sources.
- [ ] Fresh independent checkout/readback validates tree, claim identity uniqueness, source-manifest links and representative scientific regression scripts.
- [ ] Final historical-record reconciliation report signed off with explicit remaining unavailable originals; if any required original is missing, certification remains BLOCKED.

## Work freeze

No new theorem should be advanced as part of the main proof program until this gate is completed or the project owner explicitly changes the criterion. Repository preservation, provenance reconstruction, identity fixes and verification tests are in scope. Existing historical records remain untouched.

## Existing inventory

The [collision inventory](../../docs/research/CLAIM_LEDGER_BRANCH_COLLISIONS_2026-11-01.csv) is a **line-level comparison**, not a mathematical reconciliation. It identified 246 nonidentical or branch-exclusive claim IDs and 12 extra repeated-ID rows across the two compared ledgers. It does not independently validate theorem documents, and the source ledger includes unquoted CSV content whose semantic fields need strict parser validation before canonical normalization.

## Critical safeguard

A single verified historical record means **one canonical navigable history with immutable, correctly attributed multiple sources**, not deleting history or pretending two genuinely different propositions with the same old claim number are one proposition. Historical branch refs may remain as immutable evidence even after selected files are imported.
