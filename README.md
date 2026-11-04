# The Singular Boundary

**A source-preserving research program investigating Penrose/quasicrystalline geometry, physical SU(2) lattice gauge theory, and the Yang–Mills existence and mass-gap problem.**

> **Scientific status (November 4, 2026): OPEN.** No nontrivial four-dimensional continuum Yang–Mills construction or positive physical mass-gap theorem has been established. Exact finite-graph results, conditional inequalities, numerical archives, and proposed proof paths must be read within their stated assumptions.

## Research Observatory

**[Browse the Research Observatory source (available now)](observatory/)** · [Open the local website entry point](observatory/index.html) · [Read proof-path discovery](observatory/PROOF_PATH_DISCOVERY_2026-11-04.md) · [Public Pages URL (not active)](https://syncgravity.github.io/singular-boundary/)

The Observatory is an interactive research map, not a declaration of a completed proof. It provides a P0–P5 dependency graph, a searchable source-pinned index of **740 theorem Markdown files**, nine typed proof-path connections, explicit obstructions, and historical evidence notes. Only selected records have claim-level editorial annotations. Indexing a theorem path **does not certify the statement**.

**Hosting:** the linked public GitHub Pages URL is **not live**. The deployment workflow failed to enable Pages because the GitHub Actions integration lacks site-creation permission. GitHub Pages activation is intentionally **deferred** until publication is authorized. Deployments are manual-only; the URL is not live. When ready, enable repository **Settings → Pages → Build and deployment → Source: GitHub Actions**. The GitHub Actions publisher is at [`.github/workflows/pages.yml`](.github/workflows/pages.yml).

**Publication boundary:** GitHub Pages publishes the static `observatory/` site publicly even while this repository remains private. The page contains theorem titles, research summaries and source references, but no uploaded raw numerical binaries or credentials. Links to private repository files require GitHub access; the site itself is not independent public access to the underlying evidence.

The latest exact-family investigation is the [three-face nested all-spin theorem and scope audit](research/audits/THREEFACE_ALL_SPIN_NESTED_2026-11-04.md). It preserves the two-shared-link Gauss-invariant physical sector, but does not establish unrestricted tame closure or a mass gap.


The latest analytic step is the [variable-high-spin recoupled PW matrix-sector audit](research/audits/VARIABLE_HIGH_SPIN_RECOUPLED_MATRIX_SECTORS_2026-11-04.md). It establishes a fixed-three-face first-moment bound for arbitrary matrices in two matched degree sectors, while leaving the general all-width nonlinear closure and Borel hypothesis open.

The next fixed-sector step, [four independent PW degrees on overlapping extended histories](research/audits/FOUR_DEGREE_PW_MATRIX_OVERLAP_2026-11-04.md), establishes a conservative first-moment constant 6e^(-κ) for arbitrary Fourier matrices on one three-face overlap. The **unrestricted long-history nonlinear closure remains open**; the conditional Borel-disk result is not upgraded.

## Start here

| Research question | Canonical record |
| --- | --- |
| What is the latest source-certified research priority? | [November 4 P0 regulator review](docs/research/REPOSITORY_REVIEW_AND_P0_OBJECTIVE_2026-11-04.md) |
| What remains to complete the mass-gap proof? | [P0–P5 proof dependencies](docs/research/PROOF_DEPENDENCIES.md) |
| Which theorem or correction already addresses this idea? | [740-file theorem navigator](docs/research/THEOREM_INDEX.md) |
| What did the historical conversations and archives establish? | [Double investigation](observatory/HISTORICAL_DOUBLE_AUDIT_2026-11-04.md) |
| Which proof pathways presently connect or fail? | [Typed proof-path discovery](observatory/PROOF_PATH_DISCOVERY_2026-11-04.md) |
| What counts as mathematical evidence? | [Evidence protocol](docs/research/EVIDENCE_PROTOCOL.md) |
| How should an AI researcher continue without duplicating work? | [AI research handoff](docs/research/AI_RESEARCH_HANDOFF.md) |
| Where are original sources and their custody gaps? | [Source/code map](docs/research/SOURCE_AND_CODE_MAP.md) · [archive intake](sources/source-manifests/ARCHIVAL_INTAKE_REGISTER_2026-10-30.csv) |
| What claims exist and which are contested? | [Append-only claim ledger](research/claims/CLAIM_LEDGER.csv) · [historical identity crosswalk](docs/research/HISTORICAL_FLAG_IDENTITY_CROSSWALK_2026-11-01.csv) |

## Proof frontier: P0–P5

**P0 — Geometry, regulator, and provenance.** Certify one genuinely refining three-dimensional SU(2) spatial regulator, with compatible chain/cochain geometry, original-link electric and magnetic action, Gauss sector, source identity, physical units and temporal specification. Historical Penrose patches, extruded prisms, and the exact dyadic cubic benchmark are **different constructions**; similarity of numerical values does not establish equivalence.

**P1 — Physical operator algebra.** Apply the corrected original-link orientation and shared-link sign conventions. Earlier face-coordinate operators and reduced Wigner models cannot silently replace the original Gauss-invariant Hamiltonian.

**P2 — Nonlinear vacuum score.** Exact low-order Poisson calculations, Peter–Weyl inverse estimates, history-aware reconstruction, source multigrading and local-first tame bounds provide finite-strip ingredients. The newest [conditional Gevrey-1 coefficient majorant](observatory/PROOF_PATH_DISCOVERY_2026-11-04.md) and [uniform local Borel-disk deduction](research/audits/LOCAL_FIRST_BOREL_DISK_2026-11-04.md) are **formal**, not ordinary convergence at coupling one or an interacting spectral gap.

**P3 — Penrose interacting vacuum.** Prove the required Wilson-specific deleted-face current/anti-depletion bound on a certified regulator, or find an alternate completed-cage estimate. The previously recorded `sup_f T_(f,h)=o(h^(-1/4))` is a sufficient condition within one strategy, not an established fact about the interacting vacuum or a necessary condition for every proof.

**P4 — Physical interacting spectrum.** Derive a Gauss-invariant, source-visible, volume/refinement-controlled infrared spectral estimate. The finite cubic strong-coupling gap and small-magnetic stability result do **not** extend directly along the asymptotically free `g0(a)→0` continuum trajectory.

**P5 — Continuum existence and positive mass gap.** Establish nontriviality, physical normalization, appropriate infinite-volume/refinement limits, reflection positivity/OS reconstruction, and a strictly positive mass gap in physical units without circular assumptions.


### November 4, 2026 — Independent nested physical PW audit

The [shared-link two-face calculation](research/audits/NESTED_PW_COEFFICIENTWISE_AUDIT_2026-11-04.md) and [arbitrary-spin nested Wilson family theorem](research/audits/ALL_SPIN_NESTED_WILSON_FAMILY_2026-11-04.md) verify the corrected electric inverse and coefficientwise nuclear PW norms in one structured family; its exact local-first L¹×L² ratio is ≤e^(−κ)/16 and decays as 1/n at high spin. **This does not independently certify the unrestricted arbitrary-history local-first tame estimate or the conditional Borel disk.** [Exact verifier](research/tests/verify_all_spin_nested_family_2026_11_04.py).

## Repository map

| Directory | Role |
| --- | --- |
| [`research/theorems/`](research/theorems/) | Theorem records, exact calculations, conditional results and counterexamples |
| [`research/problems/`](research/problems/) | Open scientific obligations: R3-PRISM, R3-IR, R2, D1 |
| [`research/claims/`](research/claims/) | Claim ledger and proposition-level reconciliation |
| [`research/tests/`](research/tests/) and [`scripts/`](scripts/) | Existing verification and reproducibility programs |
| [`sources/`](sources/) | Historical references, preserved records and archival intake |
| [`docs/research/`](docs/research/) | Proof dependencies, indexes, corrections, handoff and checkpoints |
| [`docs/governance/`](docs/governance/) | Integrity, review, branch and evidence standards |
| [`observatory/`](observatory/) | Static research-map website, indexed catalog, audit and proof-path reports |

## Historical integrity

On November 4, 2026, all ten former non-main historical branch heads were integrated into `main`; the canonical theorem index covers **740 files**. This is a verified **Git ancestry** statement, not proof that all theorem bodies or historical original bytes were independently certified. Historical duplicate claim IDs and original-source custody are still subject to the [acceptance gate](docs/research/HISTORICAL_RECORD_ACCEPTANCE_GATE_2026-11-01.md). [Branch consolidation report](docs/research/BRANCH_CONSOLIDATION_COMPLETED_2026-11-04.md).

The uploaded Stage 26 data checks validate selected recorded hashes and source linkages, not Monte Carlo physics, a true 3D refinement, or a continuum Yang–Mills theorem.

## Research and publication rules

1. Always specify model and dimension, geometry, orientation, Gauss sector, coupling, boundary conditions, source bytes, and physical normalization.
2. Read the source and correction chain before importing a lemma. A theorem filename, verifier count, or archived AI conversation is not independent certification.
3. Keep physical, auxiliary, gauge-reduced, and toy models distinct until equivalence is proved.
4. Preserve source-qualified contradictory claims, failed experiments and binary provenance; never rewrite archived evidence to appear consistent.
5. Label conjectural, conditional, exact finite-volume, numerical, reproduced and publication-ready assertions separately.
6. Keep repository writes reviewed and non-destructive. Do not force-push the canonical research record.
7. Deploy only the curated `observatory/` directory to Pages; never upload the private repository source tree or archival binaries as a website artifact.

**Research objective:** a coherent, independently checkable sequence of implications to a nontrivial continuum SU(2) Yang–Mills theory with a strictly positive physical mass gap.
