# PF-I6 — Eight predecessor papers: original script recovery, matched cut-and-project, and finite-crop Laplacian audit

**Date:** November 7, 2026 (America/Denver)  
**Uploaded original:** `Archive(1).zip` · SHA-256 `bdc3792b2f2be40736c20c4574ef72a6f1eded226fe28415a5f1c33392af2f9b` · 5,511,410 compressed bytes · 42 ZIP members (21 substantive; 21 `__MACOSX` metadata).  
**Research status:** authoritative code **for these eight predecessor drafts**, independent finite-source tests. The **merged final dissertation's full numerical source identity, physical 4D dynamics, Yang–Mills continuum gap and gravity UV finiteness remain OPEN**. This report corrects and narrows PF-I2–PF-I5 without erasing them.

## 1. Actual source inventory

Eight draft manuscripts (`paper1.pdf` through `paper8.pdf`), one `paper5_appendix.pdf`, **nine** predecessor Python scripts, two handoff Markdown results summaries and one `paper3_coupled_summary.json` have been verified byte-for-byte in the newly supplied ZIP. The 9 Python programs are syntactically parseable by Python 3. The PDF title pages and extracted paper structure have been inspected. No standalone `paper4_compute.py`, `paper7_compute.py` or `paper8_compute.py` is present; their results partly depend on other scripts, and it would be mistaken to require one-to-one code filenames per paper.

### Complete Python entrypoint map

| `paper1_compute.py` | Fibonacci chain, adjacency-to-Laplacian correction; no P3 graph |
| `paper2_computation.py` | earlier Robinson substitution + Delaunay filtered graph, distinct model |
| `paper2_compute.py` | corrected dual-pentagrid P3 generator, Fibonacci weighted D=sum W; Conway worms |
| `paper3_compute.py` | copies P3 geometry; four-coordinate embedding, zeta, compact 1D proxy |
| `paper3_coupled_compute.py` | same P3 integer labels, adds all accepted ± basis links; reads prior Paper6 result files |
| `paper5_compute.py` | P3 phason/heat kernel/spectrum and position-diagnostic sweep; depends on external P3 eigenvalue data |
| `paper6_convergence_compute.py` | two finite Laplacians, source 35% interior, compact C5/conformal diagnostics |
| `paper6_figures.py` | plots and relative-logdet/graph-gradient revisions; top-level script side effects and missing external data |
| `zeta_prime_validation.py` | zeta-prime corrective audit, rejects earlier invalid direct 5D-R² implementation |

**Python source sizes / function inventory / original SHA prefixes:**

| Script | Lines | Top-level functions | Top-level classes | Original SHA-256 prefix |
|---|---:|---:|---:|---|
| `paper1_compute.py` | 203 | 4 | 0 | `876104b01aa385f6…` |
| `paper2_computation.py` | 633 | 8 | 0 | `7849cc2dcda14393…` |
| `paper2_compute.py` | 700 | 9 | 1 | `a8e73bb783471bed…` |
| `paper3_compute.py` | 915 | 17 | 0 | `f253f4036dfb6a7e…` |
| `paper3_coupled_compute.py` | 516 | 11 | 0 | `ad074fc4fbbbb5dc…` |
| `paper5_compute.py` | 472 | 6 | 0 | `85416b0ec4303207…` |
| `paper6_convergence_compute.py` | 675 | 17 | 0 | `a758befa9bbbe27a…` |
| `paper6_figures.py` | 494 | 11 | 0 | `63315de666d593f9…` |
| `zeta_prime_validation.py` | 590 | 9 | 0 | `fc15434334223368…` |

The PDF manuscripts are the **earlier publication drafts** and are not byte-identical to the later merged `Sharpe_dissertation_v10.7.tar.gz` files. Preserve both versions and avoid back-projecting one manuscript's labels or matrix normalization onto another. SHA-256 of all 21 substantive members is in the companion JSON evidence.

## 2. Geometry by actual implementation, not title

The original code documents an evolution:

1. `paper2_computation.py` generates a Penrose-like graph using Robinson-triangle substitution, **Delaunay triangulation** and a length threshold. It is not a source-authenticated five-integer cut-and-project graph and should not be substituted for corrected versions.
2. `paper2_compute.py`, `paper3_compute.py`, `paper3_coupled_compute.py`, `paper5_compute.py`, `paper6_convergence_compute.py`, `paper6_figures.py`, and `zeta_prime_validation.py` derive P3 multi-index labels from **de Bruijn pentagrid intersections** using generic offsets γ_j = frac(j√2+j²√3) minus their mean (sum zero) and rhombus cells with sum K in {1,2,3,4}. Some scripts then enumerate **all accepted ± original-coordinate nearest neighbours** to form a separately named “coupled Z⁵” Laplacian. These are not independent direct-window origin generators.
3. A distinct **later** `Archive 4.zip` / `Phase_III_Cut_and_Project_Recomputed` `direct_cut_project.py` constructs the 2D accepted graph directly from four perpendicular hypersimplex windows at different gamma conventions; its own matched-pentagrid tests pass, but it is not literally a source file in the newly supplied predecessor ZIP.

### Exact cut/project bridge with the manuscript offsets

The published `paper3`/`paper6` dual-pentagrid multi-index rule can be checked *directly* against its acceptance-window equivalent. Let ω=e^(2πi/5), E_j=(cos(2πj/5),sin(2πj/5)), E'_j=(cos(4πj/5),sin(4πj/5)), and γ the source's sum-zero offsets. For a regular cell, K_j=ceil(r·E_j−γ_j). Define f_j=K_j−r·E_j+γ_j, so 0<f_j<1 and Σ f_j = h = Σ K_j. Since the perpendicular projection annihilates the physical span, y=(K+γ)·E' = f·E'. Thus membership requires **h ∈ {1,2,3,4}** and 

\[
 y\in W_h=\operatorname{conv}\Bigl\{\sum_{j\in A}E'_j: |A|=h\Bigr\}.
\]

This is a **four-slice** acceptance family, not a single arbitrary decagonal disk, and applies to regular offsets (boundary conventions still matter). Using *the exact source gamma* and a new independent integer-basis breadth-first window enumeration—not pentagrid line crossings—the vertices and edges agree exactly with the source program on central physical-radius disks:

| Radius | Vertex count | Edge count | Source versus direct window |
|---|---:|---:|---|
| 3 | 36 | 55 | Exact |
| 5 | 96 | 175 | Exact |
| 7 | 186 | 345 | Exact |
| 9 | 296 | 555 | Exact |

This establishes matched **finite interior** equivalence for those samples. It does not prove numerical equivalence at every grid cutoff or identify the original final merged-dissertation eigenspectra.

## 3. New source-specific spectral operator theorem: crop-induced gap

In the predecessor scripts:

- `build_penrose_laplacian` / `build_2d_penrose_laplacian` take **tile edges emitted by finite grid-pair intersection enumeration**.
- `build_coupled_z5_laplacian` takes **every present original-basis neighbour** among the **same selected integer labels**, with exactly the same Fibonacci level-dependent hopping and **D=diag(sum W)**. The doubled physical coordinates z₁,z₂ are computed for diagnostics; no new independent z₂ edge sector is added to this finite scalar L.
- The 35%-interior rule in the source is **one pass**: identify tiles whose centroids lie within 0.35 times the maximum tile-centroid distance from the mean vertex center; select vertices for which **all incident tiles in the original enumerated patch** are marked interior. This resolves the PF-I4 ambiguity for these drafts.

For each finite source-generated accepted set V, E_tile is a subset of E_basis. Therefore, for positive source hopping w_e,

\[
\boxed{L_{\mathrm{basis}}-L_{\mathrm{tile}}
=\sum_{e\in E_{\mathrm{basis}}\setminus E_{\mathrm{tile}}}
 w_e(\delta_{e^+}-\delta_{e^-})(\delta_{e^+}-\delta_{e^-})^T\succeq0.}
\]

This is an **exact finite graph identity**, not a Yang–Mills gap claim. The independent code proof and real source-code edge enumeration give:

| N_grid | N_int | Tile edges | Basis edges | Extra basis edges | Tile components | Basis components |
|---:|---:|---:|---:|---:|---:|---:|
| 3 | 226 | 405 | 405 | 0 | 1 | 1 |
| 4 | 486 | 915 | 915 | 0 | 1 | 1 |
| 5 | 796 | 1,515 | 1,515 | 0 | 1 | 1 |
| 7 | 1,550 | 3,017 | 3,017 | 0 | 1 | 1 |
| 10 | 3,042 | 5,865 | 5,927 | 62 | 51 | 1 |
| 12 | 4,324 | 8,383 | 8,468 | 85 | 46 | 1 |

For Ng=10, **all 62** additional basis links are emitted as ordinary rhombus edges when the pentagrid intersection enumeration is extended to Ng=12; for Ng=12, **all 85** are emitted by Ng=14. Consequently the observed 0–subpercent discrepancy between the two named scalar Laplacians in the predecessor papers is in these tested patches attributable to a **finite enumeration/cropping defect**, not an independently authenticated new physical interaction.

The reported source component counts also matter. On the **tile-only interior graph**, Ng=10 has 51 components and Ng=12 has 46; adding the missing basis edges makes both connected. This impacts zero-mode filtering and renders source ζ-ratio comparisons especially sensitive to which graph constructor, N denominator, and eigenvalue cutoff were used. An earlier PF-I4 discussion assuming connected tile graphs at all sizes was not supported by these draft scripts.

## 4. Numerical choices now recoverable from real code

- `t_A=1`, `t_B=φ^-2`, hopping chosen by the floor difference `floor((k+1)/φ)−floor(k/φ)`; source weights are attached to the integer **grid family and level**, not to Euclidean bond length.
- **Weighted strength D** = sum of W per vertex. Hence the earlier PF-I2 ambiguity of ordinary degree versus weighted degree is resolved for these predecessor scripts. It is not a proof of the unknown final merged-source code's byte identity.
- Periodic comparator τ uses a **triangular open patch** with `L_side=int(sqrt(N_int))` and `N_per=L_side²`, and averaged bond weight `(1+φ^-2)/2`; it is **not exactly equal N_int**. For Ng7/10/12, source N_per is 1521/3025/4225 versus QC 1550/3042/4324.
- Positive-mode filter in source zeta calculations is `lambda > 1e-10`, typically followed by `np.mean` **over the retained positive modes**. Therefore ζ(0)=1 in those arrays is a normalization identity, not evidence for a nontrivial continuum cosmological counterterm.
- The predecessor summary `paper3_coupled_summary.json` reports eight sizes (1550 through 19260 vertices) and means `R(-1/2)=0.833195` and `R(-1)=0.737092`. Our generator-only source replay independently recovered N_int 1550/3042/4324 at Ng7/10/12; **we have not rerun the large eigenvalue computations**, and the required source `.npy` arrays and `/home/claude` data directories are not included in this ZIP.
- The two Markdown summaries record **substantive corrections**: invalid original adjacency² diffusion (Paper 1), discredited ζprime ratio ≈0.287 (71% effect) from an earlier R²-acceptance approach, corrected small-mass 2D ζprime ratio ≈0.643, and Paper 6 conformal/gradient measures. These are **author-reported predecessor outcomes**, not independently certified physical continuum results.
- `paper6_convergence_compute.py` includes a second definition of `make_gamma_from_perp` that shadows the first. This requires exact-version awareness, though the two displayed formulas are similar.

## 5. Cross-paper status for the proof

| Topic | Source now established | Still required |
|---|---|---|
| Historical draft computational identity | Original nine scripts and eight draft PDFs in authenticated ZIP, hash-pinned | Distinguish later merged-final revisions and any code not in this archive |
| P3 / source accepted geometry | Matched direct cut-project and pentagrid interior patches with source gamma | Formal arbitrary-cut and boundary treatment, phason measure |
| Finite scalar L | Explicit `D=sum W`, t(k), comparator and mode filter; quantified finite-crop defect | Corrected full-scale source matrices and spectral ratios on *one* unambiguously defined operator |
| Coupled two-plane mechanism | z₁ and z₂ retained in integer coordinates and diagnostics | A source-defined **genuinely new** coupling operator whose spectrum depends on both planes beyond the shared accepted P3 graph |
| Gauge / Yang–Mills | No interacting 4D quantum gauge proof in predecessor Python scripts | Source-native SU(2) dynamics, OS reconstruction, gap uniformity |
| Gravitational finiteness | Finite scalar spectral and relative-logdet proxies | Correct gravitational fluctuation operator, continuum limit and renormalization proof |

**Recommended gate transition:** PF-I5 publication-source *unlocated* statement is superseded for the **eight predecessor drafts** (their code is now found), but **merged final operator identity remains OPEN**. PF-G0 remains OPEN until all claimed source final equations/data are consistently reconstructed. Observatory should explicitly track this new source provenance and remove the inference that the 186/616-site matches were purely speculative: source-native cut-project matches hold on the cited central disks, while full finite-grid differences are genuine source-code artefacts.

## 6. Reproduction protocol and scope

The companion side-effect-limited verifier `verify_pf_i6_predecessor_scripts.py` accepts the original `Archive(1).zip` **without running top-level plotting scripts or touching external `/home/claude` paths**. It parses original source function AST nodes, derives the exact source gamma and finite integer labels, enumerates both edge sets, verifies all counts/components and extension-recovery, reconstructs the independent direct acceptance-window disks, and emits `PF_I6_PREDECESSOR_SOURCE_EVIDENCE.json` with SHA-256 for **every substantive archive member**.

The verifier is a finite numerical/integer incidence test; it does not prove the infinite tiling hull, construct 4D physical spacetime, validate all eight published eigenspectra, or solve either target theorem.
