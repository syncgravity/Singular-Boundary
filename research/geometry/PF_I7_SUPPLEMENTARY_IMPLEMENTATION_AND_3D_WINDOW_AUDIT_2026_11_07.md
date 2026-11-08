# PF-I7 — Supplementary source implementations, original graph replay and 3D acceptance-window audit

**Research date:** November 7, 2026, America/Denver. **Source policy:** Draft filenames and paper numbers are only filesystem locators; mathematical claims must be matched to **source functions, exact parameters, saved numerical data, and plotted observables**. Uploaded source code was neither edited nor silently replaced. This is a **supplementary audit** to the existing PF-I6 content-title-first source registry: that registry already inventories **nine predecessor Python programs and eight manuscript texts** in the earlier `Archive(1).zip`. This audit adds the five recently uploaded Python files, extended manuscripts and figures. One of these five programs (the zeta-prime validator, SHA-256 `fc154343...`) is **byte-identical** to a predecessor program already in PF-I6; the other four have distinct SHA-256 digests. Distinct hashes do not, by themselves, establish chronology or source lineage. **No Yang–Mills continuum theorem or gravitational ultraviolet-finiteness theorem is established by this audit.**

## 1. The newly accessible sources, classified by executable content

Five **additional uploads** of executable Python source are now available (one duplicate of an already indexed predecessor among the earlier **nine** programs); their original file hashes are pinned in the supplementary `PF_I7_SOURCE_SHA256_MANIFEST.json`. The nine predecessor scripts are separately indexed by content-defined behavior in the Observatory PF-I6 crosswalk. They serve five computational roles, regardless of draft names:

1. **P3 tile and spectral/compact extension.** Defines `make_generic_gamma`, `build_penrose_tiling`, `build_penrose_laplacian`, `build_regular_laplacian`, `extract_z5_coordinates`, `analyze_compact_direction`, `verify_4d_isotropy`, `compute_oneloop_ratio`; extends `N_grid` to 20, 23, 25. It literally constructs rhombi by **de Bruijn pentagrid line crossings** and then crops the resulting tiles.
2. **Fibonacci hopping/Lapidus decomposition.** Independently repeats a pentagrid tiling and builds three finite operators on one source graph: Fibonacci-modulated hopping, a **same-topology uniform-hopping control**, and a triangular periodic control. It computes the auxiliary Fibonacci 1D chains and Lapidus-residue expressions. Its fixed `gamma` offsets agree in formula with the other 2D code; these are **not** the direct-window offsets from the later PhaseIII archive.
3. **Coupled Z5 basis-neighbor operator.** Starts from pentagrid-generated integer-labeled vertices and retains vertices incident only to tiles in a 35% tile-center-radius interior. It then connects **every accepted ±e_j integer-basis pair** and assigns Fibonacci weights. This is **not the same adjacency rule as requiring that pair to be an edge of a retained rhombus**. This source function generates published 1,550, 3,042 and 4,324 interior sizes exactly; see §2.
4. **Mass-dependent spectral-zeta and determinant validation.** Implements weighted graph Laplacians and `ζ'(0)=-mean log(λ+m²)` on positive modes; its accompanying supplied results document correct **2D** ζ-prime ratios around 0.643 and `ζ(-1/2)` around 0.833, and explicitly reject a prior 71%-suppression claim. The script **also contains a separate direct-Z5 radial-disk R² acceptance experiment**; the supplied `zeta_prime_validation_results.md` itself labels that part **CORRUPT / unreliable** and says it must not be used for coupled-Z5 certification. Do not silently reuse those figures.
5. **3D Z6 icosahedral finite-spectrum/negative-control experiment.** Enumerates Z6 points, projects onto physical/perpendicular three-spaces, filters by six perpendicular-space slabs, keeps an interior physical-radius fraction, builds ±e_j Fibonacci hopping, and compares against an **ordinary periodic cubic negative control**. The cubic reference is not imposed as the desired quasicrystalline geometry. The source's *name* for its window is inaccurate; see §4.

The uploaded LaTeX drafts separately discuss 1D spectral/holomorphic structure, 2D Penrose spectral dimension, the coupled-Z5/hidden-domain geometry, and a J-operator/helical-observer proposal. Their filenames and serial numbers do not establish a canonical publication sequence. Four uploaded figures correspond to these **content-defined themes**, but **none of the five supplied Python scripts contains the plotting source or saved figure-generation notebook for all four graphics**. A plotted illustration or predicted helical frequency is not yet authenticated as an independently computed dynamical measurement.

The supplied 412-line conversation is a **historical interpretation source**, not executable numerical evidence. Its statements about singular-continuous spectral measures, Lapidus complex dimensions, and gravitational finiteness must remain distinguished from what the presently available finite scripts actually establish.

## 2. Exact source-code reproduction of the first three 2D published interior counts

The uploaded P3 tiler uses the generic phase vector

\[
\gamma_j=\operatorname{frac}(j\sqrt{2}+j^2\sqrt{3})-\overline{\operatorname{frac}(k\sqrt{2}+k^2\sqrt{3})},\quad\sum_{j=0}^4\gamma_j=0.
\]

`build_penrose_tiling` creates the five-family pentagrid rhombi with integer labels `K`; the 35% interior procedure **first compares the distances of tile centers from the mean vertex center**, then retains a vertex if **all incident tile indices** were selected. Thus PF-I4's conjectured iterative **vertex-neighbor closure** was **not the procedure used in these author-supplied scripts**. It is a one-pass *incident-tile erosion*, and is entirely coherent on a finite graph.

The two independently defined finite operators were built from the **same** selected vertex labels at each size (executed, not inferred from plots):

| `N_grid` | Generated tiling vertices | Retained source vertices | Periodic control vertices | P3 tile edges | Coupled ±basis edges | Coupled-only edges |
|---:|---:|---:|---:|---:|---:|---:|
| 7 | 3,962 | **1,550** | 1,521 | 3,017 | 3,017 | **0** |
| 10 | 7,839 | **3,042** | 3,025 | 5,865 | 5,927 | **62** |
| 12 | 11,018 | **4,324** | 4,225 | 8,383 | 8,468 | **85** |

The retained vertex counts reproduce all three corresponding published size entries **exactly**. The 2D and coupled-Z5 Laplacians agree entry-by-entry at grid 7. At grids 10 and 12, the coupled source has, respectively, 62 and 85 additional *genuine unit-length projected ±e_j basis edges*; every P3 tile edge is present in the coupled operator; weights on shared edges agree exactly. This is a direct, model-internal proof that the source programs can construct **different operators on the same vertex labels**, despite a previously claimed same-basis-edge equivalence. The PF-I2 conditional “all such steps are already tile edges” assertion **does not apply** to these author-provided finite graph outputs at 10 and 12; numerical source identity had been overstated.

The published regular controls are **not strictly equal-N** in these scripts: `int(sqrt(N_QC))**2` is used for the finite 2D triangular and square references. An equal-N periodic control is a **separate experiment**, not a reproduction of the source comparator. Later PF-I3 control calibration must therefore be regarded as a sensitivity study, **not** as validation or contradiction of these source results.

## 3. Cut-and-project versus de Bruijn: what can and cannot be asserted

The uploaded 2D functions **explicitly implement de Bruijn's grid-line dual**. Their 5D integer labels and projections are relevant to cut-and-project geometry, and the two methods may be mathematically equivalent under matched phases/windows/boundaries. But **this has not been certified for the source's exact finite operator**. The earlier PhaseIII archive's direct 5D cut-and-project test passed at matched phases and its own window; it cannot be substituted as the present 2D numerical source without matching the integer labels, strip/window membership, one-pass incident-tile criterion and hopping.

In contrast, the uploaded 3D Z6 program genuinely **enumerates integer lattice points and tests perpendicular-coordinate membership**. It is a different dimension and symmetry family; its cubic control must remain **a negative comparator only**, never a requirement that the intended regulator be cubic. No assumption about the emergence of physical time or a predetermined 3+1 spacetime geometry is made by these finite checks.

## 4. Exact 3D geometry certificate: the coded acceptance window has 12, not 30, facets

The script's `triacontahedron_test` evaluates

\[
W_{\rm code}=\{r\in\mathbb R^3: |r\cdot e_j^\perp|<R_W\quad (j=0,\ldots,5)\}.
\]

This is the intersection of six slabs, hence **at most 12 supporting faces**. Evaluating the actual six normalized Galois-conjugate basis directions with `scipy.spatial.HalfspaceIntersection` yields **20 vertices, 12 pentagonal faces, five vertices per face**: a dodecahedral window, **not** the stated **30-rhombus rhombic triacontahedron**. This is a structural discrepancy in the *implemented acceptance window*, not in the 3D cubic negative control. It is a pure finite-dimensional halfspace result and does **not** establish what the correct dissertation/physical geometry must be. Correcting the icosahedral acceptance domain requires source-author confirmation and independent eigenvalue regeneration.

The script also uses an empirically multiplied `R_W = sqrt(2/(φ+2))*1.15`, which is a **chosen density calibration** and not demonstrated to be the precise canonical Z6 window scale in the supplied code.

## 5. Original 3D data: finite-size evidence versus incompatible spectral subsets

The uploaded `paper67_data.tar.gz` contains archived positive-mode eigenvalues, per-size JSONs, a summary and a recorded finiteness verdict. I independently loaded the `.npy` arrays and recalculated the stored `ζ_QC(-1/2)/ζ_per(-1/2)` ratios to machine accuracy. The verdict uses **`N_range=8,9,10,11,12,13` only** and states

\[
\Delta\gamma(-\tfrac12)=+0.0009256399609,\qquad \text{script-estimated uncertainty }0.00651629,
\]

with its own **`finiteness=false`** outcome. This is a finite-size regression under a particular scalar window model, not a proof about any thermodynamic or gravitational UV limit.

The archive also contains `N_range=14,15`, but the source eigensolver **switches at matrix size 15,000** from a complete dense spectrum to `eigsh(k=3000, which='SM')`, storing only the **2,999 positive smallest eigenvalues**. These two archived arrays **cannot be combined with the full spectra of sizes 8–13 for complete spectral moment, heat-kernel, or scaling comparisons**. In particular, their largest retained QC eigenvalues are only about **1.099** and **0.866**, whereas the full earlier spectra reach about **7.693**. Their reported ratios near 0.525 and 0.503 are not full-spectrum source ratios.

### Exact finite heat-kernel correction for the connected periodic reference

`compute_eigenvalues` removes all `λ≤10^{-10}` before the 3D `spectral_analysis` applies `P(σ)=mean exp(-σλ)`. But a finite connected Laplacian has one exact zero mode and its normalized heat trace is

\[
P(\sigma)=\frac{1+\sum_{\lambda_k>0}e^{-\sigma\lambda_k}}{N},
\]

not the mean over positive eigenvalues alone. The omission artificially removes the late-time plateau and can cause inflated spectral-dimension peaks. For archived size 8, the source's periodic `peak d_s=9.329743` becomes approximately **3.195159** when the periodic control's one zero eigenvalue is reinstated and the same finite-difference rule is used. The 3D quasicrystal code removes only isolated degree-zero vertices and **does not verify connectedness**, so its correct number of zero modes must be checked separately; do not automatically add exactly one QC zero mode.

These calculations are deterministic checks on the original archived positive spectra, not independent regeneration of all Z6 graphs. Source-window correction must precede any claim of 3D icosahedral finiteness.

## 6. Interpretation of the four supplied figures

- **The 2D seven-panel argument:** exhibits reported spectra, IDS, Weyl-like counting, heat kernel and spectral dimension on 19,260 vertices. Its plotted “gravitational integral” includes a `Pen/Tri = 0.9941` annotation, which should **not** be conflated with `ζ(-1/2)≈0.833` or a determinant `ζ'(0)` ratio. The plot is not a proof of an ultraviolet limit.
- **Holomorphic resolvent image:** depicts Fibonacci vs regular finite resolvent contrast and a phase map, but the actual plotted complex-grid samples, resolvent matrix/eigenvalues and figure-generation code are not among the five Python scripts. Treat analytic interpretations separately from source-verifiable claims.
- **J-operator/helix and curvature image:** displays theoretical hidden-coordinate constructs and reported finite size trends; the figure-generation code and raw helical/curvature observation table were not supplied in these five scripts.
- **J-operator temporal oscillation image:** labels its curves as a **sampled** field vs the **predicted** `f=10p` frequencies and the ratios 3:5:8. No independent measured temporal dynamics or continuum temporal-evolution theorem follows from the image alone. Source plotting/trajectory routines still need authentication.

The five `.tex` documents link graphics by their roles; different draft numbering is not evidence of changed physics or source identity.

## 7. Status, nine-script predecessor registry, and correction protocol

**Supported now:** exact reproduction of the first three published P3 interior sizes; explicit source identification of the one-pass tile-interior selection; actual finite coupled-operator edge excess; exact identification of the wrong 3D facet count; independent recalculation of 3D archived moment ratios; correct scoping of truncated eigenspectra; and an independent heat-kernel zero-mode check on the periodic negative control.

**Not established:** complete end-to-end execution and mathematical certification of all **nine already recovered predecessor scripts plus four additional distinct script variants**; precise 2D source-equivalent acceptance-window implementation; original high-N `N_grid=25` graph and full spectrum replay; 3D correct rhombic-triacontahedral window numerical regeneration; canonical spacetime temporal dynamics; physical gauge-field fluctuation operator; four-dimensional continuum Yang–Mills existence or positive mass gap; gravitational ultraviolet finiteness.

**Required next obligation:** authenticate any missing **final-merged-source** plotting, full `N_grid` acceptance-window and numerics scripts by their *functions and checksums*, not filenames. Generate a source-controlled direct-window graph for the **same** `N_grid`, `γ`, integer labels, tile selection and weights as the original P3 source, compare accepted vertices/edges/matrices byte-for-byte, and only then rerun source-matched spectra. Independently correct the Z6 acceptance polytope and spectral zero-mode handling, keeping the cubic model as negative control. **All physical proof gates remain OPEN.**

## 8. Relationship to existing PF-I6 Observatory records

The earlier PF-I6 proof atlas already recorded nine predecessors by **content title, function behavior and SHA**, as well as a source-gamma direct-cut/project finite-disk proof and finite-crop coupled versus tile-edge differences. This supplementary report **independently reruns** the 1,550/3,042/4,324 vertex/source edge comparisons and **does not claim** those findings are new theorem discoveries. Its material new source-specific diagnostics concern: (i) the exact **12-faced** acceptance polytope in the additional Z6 implementation despite the 30-faced name; (ii) the archived Z6 eigenvalue/truncation provenance; (iii) incorrect exclusion of zero modes from finite heat-trace spectral-dimension estimates; and (iv) context-scoped provenance for the helical/resolvent figures, whose plotting code has not yet been identified among the source files examined here. All requirements remain contingent on identifying which computation is carried into the merged-final dissertation model.
