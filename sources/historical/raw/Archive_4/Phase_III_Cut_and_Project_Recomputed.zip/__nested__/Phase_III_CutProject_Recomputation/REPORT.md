# The Singular Boundary — Phase III: cut-and-project recomputation

**Executed:** 11 October 2026. **Status:** Corrected 2D Penrose construction validated; independent \(\beta=0\) and interacting \(\beta=1,2\) Wilson computations executed; computational sampling gates passed for the stated interacting settings. **No quasiperiodicity-specific causal claim admitted.**

## Executive result

The previous Phase II/III Penrose graph generator used generic pentagrid offsets with a noninteger sum. As established in `Phase_III_Source_Construction_Audit.zip`, this was not a certified Penrose matching-rule construction. This study therefore **does not recycle any earlier Penrose numerical measurements**. Instead, the reference graph is generated from \(\mathbb Z^5\) model-set membership and accepted lattice squares, without invoking the old dual-pentagrid constructor to generate vertices or faces.

On the corrected graph, 16 independent, reproducible Wilson-action trajectories (3,200 retained configurations) were completed and replayed with an accurate dense Hermitian eigensolver. The rank-normalized \(\hat R\), bulk ESS, and tail ESS requirements are met for both the mean plaquette and lowest eigenvalue at both sizes and both couplings. A separate exact \(\beta=0\) independent-Haar experiment sampled five offsets across four sizes (160 configurations).

The geometric-control admission outcome remains negative: **0 of 96** selected comparisons against provisional rational-direction periodic tori passes the frozen rooted-neighborhood/degree/face/boundary thresholds. The new interacting means describe the corrected Penrose finite volumes; they are not evidence that long-range quasiperiodicity causes an advantage.

## A. Construction: direct model-set geometry

Let \(e_j=(\cos(2\pi j/5),\sin(2\pi j/5))\), \(e'_j=(\cos(4\pi j/5),\sin(4\pi j/5))\), and \(k\in\mathbb Z^5\). Physical coordinates are \(r(k)=\sum_j k_je_j\). The five offsets \(\gamma\) are normalized to satisfy \(\sum_j\gamma_j=1\); this is a *new input tiling*, not a transformation of the old numerical output.

For each putative lattice vertex, let \(h=-\sum_j k_j-1\). Only \(h\in\{1,2,3,4\}\) is accepted. The internal coordinate

\[
y(k)=-\sum_j(k_j+\gamma_j)e'_j
\]

must lie inside the convex hull \(W_h\) of all internal vectors \(\sum_{j\in A}e'_j\) with \(|A|=h\), i.e. the corresponding hypersimplex-window slice. The finite graph is explored through \(\pm e_j\) basis steps **in the parent \(\mathbb Z^5\)**; a rhombic face occurs when all four corners \(k,k+\mathbf e_i,k+\mathbf e_i+\mathbf e_j,k+\mathbf e_j\) are accepted and lie in the chosen physical disk. Faces are consistently oriented counterclockwise. In a separate geometric check using Shapely, representative radius-5, radius-8, and radius-10 disks each formed one valid polygonal region with no holes and area-overlap discrepancies below \(10^{-12}\). The symbol \(\mathbf e_i\) here denotes a standard \(\mathbb Z^5\) basis vector, not the 2D projection \(e_i\).

The direct construction has an independent cross-check: for physical cutoff 9.0, the complete face-label sets **exactly match** the audited regular pentagrid implementation using crossing cutoff 7.0 for offsets 0, 1, and 2. Six automated tests now include a multi-offset, multi-size incidence/height check, this independent face-set equality, the exact spectral second-moment identity, gauge covariance, flat-connection zero modes, Haar-link unitarity, and bitwise link/RNG restart reproducibility.

| Physical radius | Vertices (offset 0) | Edges | Rhombi | Euler \(V-E+F\) | Maximum degree | Exact \(\operatorname{Tr}\Delta_U^2/(2V)\) |
|---:|---:|---:|---:|---:|---:|---:|
| 5.0 | 90 | 159 | 70 | 1 | 7 | 17.4000 |
| 6.5 | 148 | 269 | 122 | 1 | 7 | 18.3514 |
| 8.0 | 226 | 421 | 196 | 1 | 7 | 19.1239 |
| 10.0 | 377 | 714 | 338 | 1 | 7 | 19.6393 |

**20 finite graphs** (five offsets at each of four radii) were separately constructed, checked, and hashed in `geometry_manifest.json`. The generator creates **open, finite, 2D rhombic disks**, not a three-dimensional icosahedral tiling.

## B. Exact \(\beta=0\) offset sensitivity

At \(\beta=0\), the Wilson-action Gibbs measure on links is a product of exact normalized Haar measures. Independent normalized-quaternion \(SU(2)\) samples therefore need no Metropolis thermalization. Eight link configurations were sampled for each of five offsets at four physical radii, giving **160 independent link realizations**, nested in 20 finite graph selections. The lowest covariant-Laplacian eigenvalue is computed with a single-eigenvalue sparse Hermitian solve (`eigsh(k=1)`, fixed initial vector); no gap estimates are taken from this calculation.

| Physical radius | Mean lowest eigenvalue (40 configurations) | SD of five offset means | Descriptive SE across five offset means |
|---:|---:|---:|---:|
| 5.0 | 0.382640 | 0.014700 | 0.006574 |
| 6.5 | 0.402247 | 0.011035 | 0.004935 |
| 8.0 | 0.401873 | 0.014322 | 0.006405 |
| 10.0 | 0.406127 | 0.016249 | 0.007267 |

The last column is descriptive, not a population sampling-theory confidence interval: the five offsets are deterministic, relatively few, and not certified independent draws from a tiling hull. The observations demonstrate finite-volume offset sensitivity and do not establish a scaling exponent.

## C. Interacting Wilson-action ensemble, corrected Penrose construction

The action and covariant Laplacian are, respectively,

\[
S_\beta(U)=\beta\sum_{f\in F}\left(1-\tfrac12\operatorname{Re}\operatorname{Tr}W_f\right),\qquad
(\Delta_U\psi)(v)=\sum_{w\sim v}\bigl(\psi(v)-U_{vw}\psi(w)\bigr).
\]

All edges carry independent \(SU(2)\) link variables and are updated by symmetric left-multiplication proposals with single-edge Metropolis acceptance. The **same physics and update code** is retained from the Phase II engine, but the **graphs and all chain states are newly generated**. These ensembles have open finite rhombic faces; links on boundary edges occur in fewer faces, as explicitly encoded in the face-incidence action.

For each of the four settings (physical radius 5.0 or 6.5; \(\beta=1\) or 2), four independent-seed chains were run, each with 100 burn-in sweeps followed by 200 measurements spaced by three sweeps, totaling **16 independent chains and 3,200 retained observations**. Each chain is exactly checkpointed with full links, RNG state, graph SHA-256 fingerprint, and measurement sequence. This is 700 sweeps per chain, **11,200 total sweeps**.

| Radius | \(\beta\) | Vertices | \(\langle P\rangle\) ± MCSE | \(\langle\lambda_0\rangle\) ± MCSE | \(\langle\lambda_2-\lambda_0\rangle\) ± MCSE |
|---:|---:|---:|---:|---:|---:|
| 5.0 | 1 | 90 | 0.240463 ± 0.002218 | 0.306563 ± 0.001079 | 0.041584 ± 0.000906 |
| 5.0 | 2 | 90 | 0.435250 ± 0.002120 | 0.252052 ± 0.001141 | 0.039387 ± 0.000722 |
| 6.5 | 1 | 148 | 0.238050 ± 0.001846 | 0.328176 ± 0.001121 | 0.034834 ± 0.000854 |
| 6.5 | 2 | 148 | 0.432123 ± 0.001543 | 0.266728 ± 0.000900 | 0.031950 ± 0.000690 |

Here \(\lambda_0\) is the smallest eigenvalue and \(\lambda_2\) is the next *distinct* eigenvalue: the \(SU(2)\) spinor spectrum has doublet structure in the verified finite model. The gap results are based on **complete dense Hermitian spectra** at every measured gauge configuration, not the earlier four-vector sparse solve.

### MCMC diagnostics

| Radius | \(\beta\) | Raw draws | Maximum rank \(\hat R\), monitored pair | Minimum bulk/tail ESS, monitored pair | Admission |
|---:|---:|---:|---:|---:|---|
| 5.0 | 1 | 800 | 1.00201 | 583 | Pass |
| 5.0 | 2 | 800 | 1.00562 | 416 | Pass |
| 6.5 | 1 | 800 | 1.00474 | 571 | Pass |
| 6.5 | 2 | 800 | 1.00364 | 508 | Pass |

The monitored pair is the mean plaquette and \(\lambda_0\). The prespecified thresholds are rank-normalized \(\hat R<1.01\), bulk ESS ≥ 400, tail ESS ≥ 400. MCSE of the mean was obtained with ArviZ. These criteria assess the finite-volume MCMC precision and between-chain mixing of the measured observables; they do not prove stationarity or transfer to different offsets and geometries.

As a consistency check *within the same Penrose graph*, changing \(\beta:1\to2\) reduces the mean lowest eigenvalue by \(0.054511\pm0.001571\) at radius 5.0, and \(0.061448\pm0.001438\) at radius 6.5 (Monte Carlo standard error of the independent-ensemble difference). This measures coupling response, **not an advantage relative to periodic tilings**.

### Eigensolver replay audit: an additional correction

Sparse ARPACK runs with `eigsh(k=4)` occasionally omitted one of the twofold eigenvalue partners. Reproducing **all 16 chains** with complete dense Hermitian eigenspectra produced **exactly the same saved RNG states and final gauge-link matrices**, proving that the numerical re-analysis did not change the sampled Markov trajectories. Across 3,200 measured configurations:

- The original lowest eigenvalue \(\lambda_0\) agreed with the dense value in all 3,200 cases to absolute tolerance \(10^{-7}\).
- The original reported third ordered eigenvalue \(\lambda_2\) differed in **389 of 3,200** cases by more than \(10^{-7}\); the largest observed error was about **0.08571**.
- Accordingly, **only the dense-replayed excitation-gap results are admitted**. The sparse-original files are retained solely as auditable provenance in `chains/`, and corrected measurement files are in `chains_dense/`.

A newly provided `checkpoint_wilson.py` uses dense eigenspectra from the outset, verifies both SU(2) doublets at every measurement, and writes into a different `chains_certified/` directory when run through `run_segments.py`.

## D. Repeated geometry-control admission

The **frozen Phase III geometry gate** was rerun on window-first Penrose patches instead of the prior pentagrid-generated patches. The opposing reference remains the provisional rational-direction torus: it is *not* certified as a Penrose substitution approximant. Four Penrose offsets, four periodic scales \(q=6,8,10,13\), two periodic phase offsets, and selected regions of 100, 180, 260 vertices yield **96 selected pairs**.

| Selected size | Pairs | Admitted | Minimum radius-one signature TV | Minimum radius-two signature TV |
|---:|---:|---:|---:|---:|
| 100 | 32 | 0 | 0.3500 | 0.7600 |
| 180 | 32 | 0 | 0.2556 | 0.5556 |
| 260 | 32 | 0 | 0.2192 | 0.4577 |

Admission requires degree TV ≤ 0.05, radius-one signature TV ≤ 0.10, radius-two signature TV ≤ 0.15, face incidence TV ≤ 0.10, boundary-cut relative discrepancy ≤ 0.10, and absolute normalized second-moment discrepancy ≤ 0.20 **simultaneously**. Each displayed minimum is separately minimized and need not correspond to the same pair. The rooted statistics are the project pipeline's deterministic neighbor-degree/WL-style signatures, not complete radius-two graph-isomorphism certificates. **No matched interacting Penrose-minus-periodic contrast is supported.**

## E. What is and is not established

**Established in these finite computations:** independently reconstructed \(\mathbb Z^5\) model-set Penrose disks; exact agreement with an audited dual pentagrid representation over tested windows; valid basis edges and oriented quadrilateral faces; 20 checked graph manifests; an exact \(\beta=0\) Haar baseline; 16 checkpointed Wilson chains with 3,200 dense-certified spectral measurements; measured MCMC precision above the predefined gate for the four settings; and reproducible rejection of all 96 proposed periodic controls.

**Not established:** a comparison satisfying the causal admission gate; robustness of interacting ensembles to Penrose offsets other than zero; asymptotic finite-size exponents from only two interacting sizes; a universal spectral bound or computational improvement due to Fibonacci quasiperiodicity; or the dissertation's independent \(\mathbb Z^6\to\mathbb R^3\) construction. The original dissertation experiments did not provide their own code in the available dissertation archive and therefore are not certified by this follow-on audit.

**Phase III decision:** The Penrose *reference* and corrected interacting finite-volume baseline are now reproducible. The **quasiperiodicity-specific causal claim remains unproven**, and confirmatory Penrose-vs-periodic interacting measurements remain gated until canonical locally convergent periodic substitution approximants pass geometric admission.

## Source/code and reproducibility ledger

The corrected source audit and the dissertation/Paper 2 supplied the canonical \(\mathbb Z^5\) projection/window conventions. This computation itself is recorded in `direct_cut_project.py`, `checkpoint_wilson.py`, `replay_dense.py`, `independent_beta0.py`, `geometry_admission.py`, and their associated JSON files. `README.md` provides execution commands. The source archive's description of 3D \(\mathbb Z^6\) geometry is contextual only; no 3D generator is implemented here.
