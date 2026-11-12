# Repository handoff and branch lifecycle · 2026-11-11

**Purpose:** this is the single starting point for a new research conversation. The Observatory is the repository's contextual map; use the canonical proof spine and current source dossiers rather than reconstructing context from old chats.

## Start here

1. [Research program map](RESEARCH_PROGRAM_MAP_2026-11-11.md) — repository layout, primary source dossiers, PF-I16 sequence, evidence vocabulary and maintenance rules.
2. [Observatory home](../../observatory/index.html) — navigational entry point.
3. [Canonical spectral-inequality interface](../../observatory/spectral-inequality.html) — one theorem target and six dependency gates.
4. [Canonical proof-program specification](SOURCE_COMPATIBLE_SPECTRAL_INEQUALITY_PROGRAM_2026-11-11.md) — exact statement, route boundaries, equivalence rules and work order.
5. [Proof Atlas](../../observatory/graph.html) — source-linked theorem/evidence graph.
6. [Penrose–Fibonacci primary map](../../observatory/penrose-program.html) — source-native coupled-Z5 / 2+2 program.
7. [Yang–Mills proof interface](../../observatory/yang-mills-proof.html) — legacy interface; defer to the spectral-inequality page for the canonical dependency spine.
8. [Branch lifecycle and retirement protocol](BRANCH_LIFECYCLE_2026-11-11.md) — live branch snapshot, safe-retirement rules and action procedure.

## Mainline preservation update · 2026-11-11

The repository front page now links the [Research Program Map](RESEARCH_PROGRAM_MAP_2026-11-11.md). The PF-I16 divergent branch was not merged wholesale: its 48 candidate paths were reconciled, with 46 source files copied to their original paths on `main` and two theorem dossiers confirmed already present. The original branch remains intact. See the [PF-I16 preservation ledger](PF_I16_BRANCH_PRESERVATION_LEDGER_2026-11-11.md).

The two latest review records are also preserved on `main`: [PF-I16 branch reconciliation](PF_I16_BRANCH_RECONCILIATION_2026-11-11.md) and [Z5 real-structure/helical-observer source audit](Z5_REAL_STRUCTURE_AND_HELICAL_OBSERVER_SOURCE_AUDIT_2026-11-11.md). The theorem registry, historical navigator, current navigator, catalog and both Proof Atlas graph serializations are synchronized at **762 theorem-source paths**, **285 curated nodes**, and **678 typed relationships**. These counts establish inventory/navigation only, not mathematical certification. A fresh CI run has not yet been observed.

The branch and PR counts below are dated historical snapshots, not live state. Check GitHub before any merge or retirement action.

## Live four-PR review board · 2026-11-11

There are **four open PRs**, tracked together in the [Observatory graph v2.74](../../observatory/graph.html) and [standalone review board](FOUR_PR_REVIEW_BOARD_2026-11-11.md). #74, #103 and #106 were reopened after the user clarified that unresolved contributions should remain active rather than archived/closed. The prior archive file records the temporary closure and preservation inventory only; it is not the current disposition.

| PR | Branch / base | Role | Current mergeability |
|---|---|---|---|
| [#107](https://github.com/syncgravity/Singular-Boundary/pull/107) | `architecture/source-compatible-spectral-spine-2026-11-11` → `main` | Canonical S0–S5 integration | Mergeable |
| [#106](https://github.com/syncgravity/Singular-Boundary/pull/106) | `audit/r3-ir-h2-trace-to-k-2026-11-10` → #107 branch | R3-IR finite-strip full-Hessian analysis | Conflict / not mergeable |
| [#74](https://github.com/syncgravity/Singular-Boundary/pull/74) | `audit/2026-11-06-nonabelian-tube-complete-theorem-index` → `main` | Finite non-Abelian tube and theorem-index work | Conflict / not mergeable |
| [#103](https://github.com/syncgravity/Singular-Boundary/pull/103) | `pages-public-ready` → `main` | Observatory publishing configuration | Conflict / not mergeable |

Do not close these PRs as a cleanup shortcut. Resolve each unique content and its overlapping generated artifacts. Do not merge Pages activation into the private research repository. The public delivery target is the Tau-hosted Fly mount at `https://qualion.org/yang-mills`.

## Prior consolidation tranche · 2026-11-11 (historical)

At the time of this earlier snapshot, the initial 12 open PRs had been reduced to one. Per the subsequent instruction, #74, #103 and #106 have been reopened; the current target is four active PRs. Eight research PRs (#55, #56, #79–#84) were merged as separate commits into this integration branch. The temporary closures were reversed. Their exact branch-head SHAs and complete changed-path inventories remain recorded in [the preservation ledger](CONSOLIDATION_ARCHIVE_2026-11-11.md); their branch refs remain intact. The old 12-PR list and 108-ref count below are historical baselines, not current live counts.

The generated theorem catalog and both graph serializations were rebuilt from the Git-blob-verified live registry after the PF-I16 source hash/byte-count correction. The source index itself passed its verifier in the prior CI run; that run then failed because four generated Observatory outputs were stale. The rebuild has now been committed to this branch. A fresh workflow result must still be checked; do not report CI as passing until it is observed.

The Observatory handoff now includes a helical-observer scope audit: Paper 3's 3:5:8 is kinematic sampling, exact Z13 aliasing and H2/H3 two-point reciprocity are controls, and the observer remains a probe rather than a Hamiltonian/time generator. Its source-authenticated 3D lift, clock/metric and matched interacting-vacuum covariance remain open.

The canonical mathematical target is unchanged: a source-compatible, interacting-vacuum, refinement- and volume-uniform gauge-invariant Poincaré inequality, followed by infrared exclusion and nontrivial 4D continuum reconstruction. S0–S5 remain OPEN; no mass-gap proof is claimed.

## Canonical mathematical objective

The single central missing result is the source-compatible, interacting, refinement- and physical-volume-uniform Poincaré inequality for all admissible gauge-invariant functions in the actual physical interacting vacuum:

\[
\operatorname{Var}_{\nu_{h,R}}(f)\le m_*^{-1}
\sum_e\alpha_{e,h,R}\int|\nabla_e f|^2d\nu_{h,R},
\qquad m_*>0,
\]

with one physical m_* independent of refinement h and volume R. The source-native physical Hamiltonian, electric coefficients, metric, time normalization, Gauss law, transfer structure and true vacuum must be the same in every estimate. The exact finite ground-state transform is the common interface, not a uniformity proof.

The canonical gates S0–S5 are all OPEN. The Observatory must never imply that finite exact results, conditional estimates, numerical evidence or auxiliary models establish the continuum mass gap.

## Current repository snapshot

Live GitHub branch enumeration checked 2026-11-11:

- **108 branch refs total:** main plus 107 non-main refs.
- Prefix distribution among non-main refs: architecture 1; audit 44; docs 1; feature 1; fix 1; maintenance 2; pages-public-ready 1; reconcile 3; release 1; research 52.
- **12 open PRs** at snapshot time; see the complete list below.
- The current spectral-inequality architecture is in draft PR #107. It is not merged into main.
- No branch has been deleted or merged as part of this handoff update.
- This snapshot is a naming inventory, not a claim that every branch is active, merged, redundant, or safe to delete. Current head SHAs and ancestry must be evaluated at execution time.

### Open pull requests at snapshot

- [#107 — Establish one source-compatible spectral-inequality proof spine](https://github.com/syncgravity/Singular-Boundary/pull/107)
- [#106 — R3_IR H2 trace-to-K calculation and Observatory audit](https://github.com/syncgravity/Singular-Boundary/pull/106)
- [#103 — Prepare Research Observatory for public GitHub Pages](https://github.com/syncgravity/Singular-Boundary/pull/103)
- [#84 — P2/T2: exact quantum-vacuum pushforward entropy and time-averaged non-Abelian flow force](https://github.com/syncgravity/Singular-Boundary/pull/84)
- [#83 — P2/T2: exact signed center-Hessian obstruction to uniform non-Abelian Wilson-flow contraction](https://github.com/syncgravity/Singular-Boundary/pull/83)
- [#82 — P2/T2: volume-uniform coupled quantum-vacuum mean defect transfers through nonlinear Wilson flow](https://github.com/syncgravity/Singular-Boundary/pull/82)
- [#81 — P2/T2: genuine coupled cubic SU(2) vacuum link-deletion and bare-action cap theorem](https://github.com/syncgravity/Singular-Boundary/pull/81)
- [#80 — Quantum SU(2) one-face vacuum curvature and classical-action transfer audit](https://github.com/syncgravity/Singular-Boundary/pull/80)
- [#79 — Audit: classical Wilson action does not automatically transfer to weak-coupling vacuum probability](https://github.com/syncgravity/Singular-Boundary/pull/79)
- [#74 — P2/T2: finite non-Abelian SU(2) positive-vacuum-probability tube and complete theorem index](https://github.com/syncgravity/Singular-Boundary/pull/74)
- [#56 — P0 refinement compatibility and P4 source-visible spectral-weight audit](https://github.com/syncgravity/Singular-Boundary/pull/56)
- [#55 — Audit: quantitative local SU(2) f-sum bound](https://github.com/syncgravity/Singular-Boundary/pull/55)

The safe retirement script queries GitHub for all open PR head and base branches at runtime. Therefore it protects stacked PR bases as well as heads; do not substitute a stale hand-maintained PR branch list.

## Safe historical branch retirement

The repository already contains:

- [SHA-checked cleanup script](../../scripts/safe_prune_merged_branches.sh)
- [Manual retirement workflow](../../.github/workflows/retire-merged-branches.yml)
- [Historical November 6 ledger](BRANCH_LIFECYCLE_2026-11-06.md), retained as an earlier snapshot.

The cleanup rule is intentionally narrow:

1. main is never eligible.
2. Every open PR head and base is protected.
3. Named independent research branches remain protected.
4. A branch is eligible only if its exact current head commit is an ancestor of origin/main.
5. The script fetches live refs, rechecks ancestry immediately before deletion, and uses a SHA lease. A branch that moved after inspection is not deleted.
6. Merged commits, source files, theorem dossiers and PR discussions remain in main/GitHub history. Deleting a redundant branch ref does not delete the integrated research.
7. A branch whose head is not an ancestor is not automatically merged or deleted. It remains for mathematical reconciliation. Do not merge unrelated or conflicting research just to lower the count.

### Execute the already-installed retirement workflow

After reviewing the live dry-run:

- GitHub repository → **Actions** → **Retire fully merged branch references (manual approval)**.
- Run with operation = dry-run first and inspect the eligible/withheld lists.
- Only if the list is correct, run again with operation = retire and enter DELETE_MERGED_BRANCHES exactly.
- The workflow uses the repository's live PR state and SHA-lease deletion. It does not run on ordinary pushes and does not deploy Pages.

This connector session can inspect and edit repository files and PRs, but it does not expose a branch-delete operation or workflow-dispatch operation. Therefore no deletion is claimed here. The exact safe operation is already installed in the repository and requires the explicit Actions run above. Do not bypass it with force-pushes or branch ref rewrites.

### What to do with non-ancestor historical branches

Non-ancestor branches are not cleanup debris by default. For each one, use the Observatory and source dossiers to decide whether it contains:

- a distinct exact result or obstruction to preserve as a source dossier;
- an open or stacked PR that needs review;
- a superseded experiment whose mathematical content is already represented in main;
- an unreviewed result that should remain quarantined until its assumptions and model boundary are reconciled.

Only after the content is represented in main and reviewed should a branch be merged or retired. A merge is not a substitute for a proof audit. Do not merge all historical branches into one archive branch. That would combine unrelated code histories and could silently mix distinct mathematical models.

## Live branch-name inventory (2026-11-11)

The following is the exact 108-ref name snapshot, including main. Branch names alone do not encode commit ancestry or theorem status.

- architecture/source-compatible-spectral-spine-2026-11-11
- audit/handoff-verifier-security-tests-2026-11-01
- audit/pf-i16-local-interacting-vacuum-2026-11-08
- audit/pf-i16-observatory-2026-11-09
- audit/r3-ir-h2-trace-to-k-2026-11-10
- audit/r3-ir-trace-gradient-bochner-2026-11-10
- audit/source-and-original-inputs-2026-11-01
- audit/source-trace-381-392-2026-11-01
- audit/theorem-source-certification-batch01-2026-11-01
- audit/2026-10-28-independent-reconstruction
- audit/2026-11-04-knowledge-graph
- audit/2026-11-04-p0-heat-kernel-transfer
- audit/2026-11-04-quantitative-local-fsum
- audit/2026-11-04-uniform-continuum-bridge
- audit/2026-11-05-cubic-haar-blocking
- audit/2026-11-05-mathematical-physics-bridge
- audit/2026-11-05-p0-refinement-p4-source-visible
- audit/2026-11-05-penrose-primary-control
- audit/2026-11-05-physical-radius-linearized-cubic-flow
- audit/2026-11-06-cartan-positive-time-cubic-smoothing
- audit/2026-11-06-coupled-cubic-link-deletion
- audit/2026-11-06-cubic-transverse-shell
- audit/2026-11-06-cubic-vacuum-to-flow-mean-defect
- audit/2026-11-06-finite-time-center-residence-tube
- audit/2026-11-06-full-nonabelian-locality-and-index
- audit/2026-11-06-full-wilson-time-memory
- audit/2026-11-06-gauge-orbit-center-stable-residence
- audit/2026-11-06-growing-support-wilson-smeared-curvature
- audit/2026-11-06-local-vacuum-orbit-residence
- audit/2026-11-06-local-wilson-fisher-thermodynamic
- audit/2026-11-06-marginal-harnack-loop-sumrule
- audit/2026-11-06-negative-center-vacuum-cap-basin
- audit/2026-11-06-nonabelian-homogeneous-and-theorem-index
- audit/2026-11-06-nonabelian-tube-complete-theorem-index
- audit/2026-11-06-nonlinear-cubic-physical-energy
- audit/2026-11-06-one-plaquette-vacuum-transfer-gate
- audit/2026-11-06-private-pivot-holonomy-local-marginals
- audit/2026-11-06-quantum-vacuum-curvature-calibration
- audit/2026-11-06-signed-center-hessian-flow-instability
- audit/2026-11-06-true-vacuum-local-bare-curvature-nontightness
- audit/2026-11-06-two-scale-influence-kernel
- audit/2026-11-06-vacuum-flow-entropy-force
- audit/2026-11-06-vacuum-weighted-schur-form
- audit/2026-11-06-weighted-nonabelian-physical-locality
- audit/2026-11-06-wilson-spatial-flow-fisher-gap
- docs/research-navigation-provenance-2026-11-01
- feature/research-observatory-2026-11-04
- fix/reproducible-research-handoff-2026-10-30
- main
- maintenance/2026-11-06-branch-retirement-base-guard
- maintenance/2026-11-06-observatory-754-index-sync
- pages-public-ready
- reconcile/claim-identity-crosswalk-2026-11-01
- reconcile/historical-branches-2026-11-01
- reconcile/immutable-ledger-snapshots-2026-11-01
- release/2026-11-05-observatory-v2-29
- research/arbitrary-four-degree-pw-threeface-2026-11-04
- research/direct-face-nested-casimir-tame-2026-11-04
- research/exact-haar-cubature-frechet-entire-borel-2026-11-04
- research/gauge-balanced-twirl-borel-optimum-2026-11-04
- research/gauss-twirl-spectrum-historywise-borel-2026-11-04
- research/highspin-recoupled-matrix-sectors-2026-11-04
- research/local-first-borel-audit-2026-11-04
- research/local-pw-poisson-two-certified-gates-2026-11-04
- research/nested-physical-pw-regression-2026-11-04
- research/noncharacter-overlapping-traces-2026-11-04
- research/p2-bernstein-thermodynamic-local-measures-2026-11-04
- research/p2-central-binomial-quantum-local-states-2026-11-04
- research/p2-certified-brackets-borel-tails-observatory-version-2026-11-04
- research/p2-chebyshev-first-frequency-2026-11-04
- research/p2-collar-s1-hopf-graph-2026-11-04
- research/p2-electric-depth-positive-frequency-2026-11-04
- research/p2-exact-physical-inverse-fourth-frequency-2026-11-04
- research/p2-extremal-counterexample-borel-germ-2026-11-04
- research/p2-fixed-collar-jacobi-scalar-borel-2026-11-04
- research/p2-fourface-physical-inverse-casimir-c2-obstruction-2026-11-04
- research/p2-full-inverse-dual-factorial-borel-2026-11-04
- research/p2-fusion-dimension-weighted-domain-2026-11-04
- research/p2-gram-dual-history-weight-obstruction-2026-11-04
- research/p2-highrank-thermodynamic-energy-2026-11-04
- research/p2-local-fusion-source-half-casimir-2026-11-04
- research/p2-onehaar-dual-sourceorder-algebra-2026-11-04
- research/p2-rayleigh-witness-cap-finite-real-score-2026-11-04
- research/p2-schur-gram-norm-dynamics-2026-11-04
- research/p2-schur-rank-local-ground-form-2026-11-04
- research/p2-source-mpo-cylinder-dirichlet-2026-11-04
- research/p2-trace-ideal-log-depth-second-time-2026-11-04
- research/p2-wigner-gram-casimir-dynamics-2026-11-04
- research/physical-twirl-response-borel-volterra-2026-11-04
- research/pw-norm-transport-operator-audit-2026-11-04
- research/summed-gauss-sectors-infinite-borel-germ-2026-11-04
- research/tensor-gram-supergaussian-borel-2026-11-04
- research/three-independent-spins-2026-11-04
- research/threeface-nested-pw-2026-11-04
- research/two-extended-histories-2026-11-04
- research/two-highspin-threeface-2026-11-04
- research/twoface-singleton-width2-one-step-2026-11-04
- research/weighted-unbounded-nested-casimir-2026-11-04
- research/width34-feedback-crossing-pw-2026-11-04
- research/2026-11-06-restore-coupled-z5-primary
- research/2026-11-07-conceptual-3d-conway-helical-reconstruction
- research/2026-11-07-helical-observer-gauge-covariance-alias
- research/2026-11-07-helical-triad-quantum-null
- research/2026-11-07-observer-marked-parity-34-55
- research/2026-11-07-paper3-helical-observer-primary-hypothesis
- research/2026-11-07-pf-primary-observatory-atlas-map
- research/2026-11-07-ym-incidence-and-poincare-proof-interface
- research/2026-11-07-z5-quotient-double-spiral-source-fidelity

## Handoff rule for every future chat

Start from the Observatory, then read this handoff and the canonical spectral-inequality program. Verify current main/PR state before changing code. Keep source-native PF and auxiliary cubic/prism/R3-IR/Borel models distinct unless a written equivalence certificate closes the model identity. Preserve all claim states; no theorem promotion without a complete proof dossier.

**This file is a navigation and lifecycle map, not a mathematical proof.**
