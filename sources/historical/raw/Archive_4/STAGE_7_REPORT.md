# Stage 7 — Large-scale Penrose/regular SU(2) Wilson gauge study: geometry, code, and admission audit

**Date:** 2026-10-11. **Status:** Large geometry and interacting algorithm verified, non-equilibrium warm-up checkpoints saved, physical spectroscopy **not admitted**. A reliable glueball mass or string tension **has not** been extracted.

## Question and strict answer

Can the verified rational cut-and-project Penrose torus be compared with a geometry- and area-matched square torus in full 2+1D interacting SU(2) gauge theory, and does that comparison produce reliable physical mass or string tension estimates?

The **large-lattice implementation and matched tree-level geometry are feasible**. It does **not** follow that the spectral quantities have been determined. The Stage 5 square reference did not pass its full effective-sample-size and spectroscopy gates, and Stage 6 multilevel outer/inner statistics remained uncertified. The new M=55 ensembles have **zero production observations**, so neither the Penrose nor a matched square mass or string tension is currently estimable. No continuation to a Penrose continuum difference is justified.

## Reconstructed large periodic geometry

| Quantity | Rational cut-and-project model-set M=55 | Regular square control |
|--|--:|--:|
| Vertices | 22,808 | 22,801 (151 × 151) |
| Spatial edges | 45,616 | 45,602 |
| Spatial faces | 22,808 | 22,801 |
| Physical area | 7,410.863377501975 | 7,410.863377501975 |
| Spatial periods | 85.8254, 86.3481 | 86.0864, 86.0864 |
| Spatial gauge links for 20 time slices | 912,320 | 912,040 |
| Total 2+1D links | 1,368,480 | 1,368,060 |
| Total oriented 2+1D plaquettes | 1,368,480 | 1,368,060 |
| Mean-area reference length | 0.57002093 | same reference convention |
| Tree-level normalized quadratic response eigenvalues | (1, 1) to numerical precision | (1, 1) to numerical precision |

The M=55 rational periodic approximant was inherited from the *corrected* window-first model-set research. Its radius-two rooted-motif TV distance 0.0821 passed the earlier local-motif **screen** of 0.15. That does not by itself certify all geometric causal controls, different phason offsets, long-range order, or continuum equivalence. The periodic model-set candidate is not claimed to be an independently certified canonical inflation supertile.

The positive gauge couplings use the earlier specified Hodge-like diagonal face- and edge-area prescription. For M=55 the spatial plaquette couplings span 2.97595–4.87725 and temporal plaquette couplings span 2.04883–3.34997 at beta_ref=3.5. The square reference has spatial coupling approximately 3.49893 and temporal coupling 3.5 under the shared area normalization. **Weak-field quadratic isotropy is not nonperturbative coupling or anisotropy matching.**

## Numerical verification performed now

1. Independently assembled full-volume, oriented 20-slice space-time plaquettes on both geometries. Spatial incidence count is exactly two faces per edge and four 3D plaquettes per spatial link. Temporal-link incidence equals the spatial vertex degree. Face closure is exact, including periodic seams.
2. Validated the fast vectorized 3D action against the original Stage 3 Python assembler *element by element* on M=5 and 13×14 square tori: identical plaquette indices, orientations, local-action adjacency, coupling arrays, and link degrees.
3. Evaluated millions of SU(2) Metropolis proposals on the large tori. Full-sweep timing is approximately 1.5 seconds per lattice per sweep in the benchmark environment. Independent full plaquette recomputation agrees with the cached action to numerical precision.
4. Implemented an on-disk, parameter-locked restart with persistent two-word PRNG state, every-link SU(2) quaternion state and cached plaquettes. Tests show bitwise-identical continuation on smaller periodic tori and exact SU(2) norm preservation. Four *corrected Haar-start* warm-up sweeps per geometry are saved in restartable checkpoints. The intermediate experimental generator that did not create Haar-distributed starting links was rejected and excluded from the package.
5. Verified independent Haar quaternion generation by normalized four-Gaussian initialization; sample coordinate-square means are near 1/4 and coordinate means near zero.
6. Built bounded-source physical Wilson paths to avoid an O(V²) all-vertices path precomputation; 100 paths per geometry span 1–5 spatial edges, with unwrapped physical displacement tracked across toroidal seams.
7. Built and executed the enlarged scalar and flux measurement pipeline on one deliberately **unequilibrated** 20-slice gauge field per geometry. Each measurement contains scalar time series `(20, 9)`, two-direction flux `(20, 6)`, and physical Wilson rectangles `(3, 100, 10)` for three smearing levels. Small-volume tests confirm gauge invariance (maximum numerical deviation below 1e-15). These are **software smoke tests only**, not physics samples.
8. Constructed genuine torus winding paths with 168 and 176 edges in the Penrose period directions; the reference square windings are 151 edges in both directions. The long winding length at fixed beta makes torelon signal extraction especially demanding.

## Quantitative readiness and computational cost

Current production checkpoints cover **four hot-start warm-up sweeps per geometry from one chain each, and zero post-burn-in saved configurations**. No mass, flux-tube energy, asymptotic potential, string tension, continuum ratio, uncertainty interval, or physically calibrated coupling difference can be estimated. These checkpoints are intentionally labeled *burn_in* to prevent scientific misuse.

The included campaign setting targets 1,000 warm-up sweeps and 10,000 total sweeps per independent chain, measuring every tenth production sweep (900 candidate configurations per chain), but this is a **run plan**, not an executed outcome or a guarantee of ESS or plateau precision. Four seeds for each of two geometries would entail ~80,000 lattice sweeps, about **33 hours of gauge updates** at the observed 1.5 sec/sweep, before measurements and convergence-driven extensions. On the pilot configurations, measuring all three APE levels, the scalar basis, winding paths and Wilson loops took ~8–13 sec per configuration. Serial measurement costs are therefore potentially comparable to update costs; scale up may demand HPC resources, variance reduction and more efficient sampling.

M=55's fundamental physical periods are around 86 in the current coordinate units, versus ~7–8 in Stage 5. Increasing M at fixed local tile spacing and bare beta chiefly increases volume; it is **not** a continuum extrapolation. For a finite-size/continuum matched study, coupling, time extent, spatial scale and physical volume require independent nonperturbative tuning. A huge winding torelon at this fixed bare coupling is not a shortcut to reliable string tension.

## Strict admission rule for future measurements

- At least four independent, equilibrated chains per geometry with acceptable rank-normalized R-hat (<1.01), bulk/tail ESS >=400 for *the specific fitted channels*, and autocorrelation-aware covariance/bootstrap samples.
- Gauge-invariant scalar 0++ correlator basis (APE 0/2/6, three loop groups) with positive/stable projected covariance, a verified three-or-more-separation plateau/fit, stability under fit-window changes, and finite-time-cosh treatment.
- String tension from several physically calibrated source separations and long-time Wilson-loop plateaus, or torelon energies from independently converged, center-charged winding correlators, with finite-length string corrections; check orientation and finite-volume effects.
- Pair-wise matched renormalized reference scale, anisotropy and physical extent. Multiple couplings/lattice spacings for continuum extrapolation, and more than one approximant/phason offset with independent geometry admission.
- The scalar mass and sigma must be extracted from the same statistically accepted gauge ensembles to obtain correctly correlated bootstrap estimates of m/sqrt(sigma). **If either fit fails, do not report the ratio or a geometry-dependent mass shift.**

## Provenance

Sources are Stage 2's corrected rational model-set torus, Hodge-like calibration, Stage 3 torus actions, Stage 4 APE and winding operators, Stage 5 square correlator pipeline and Stage 6 conditional sampling. The code and numerical matrices are not presented as independently validated results about physical spacetime. The historic flawed de Bruijn Penrose construction is not used in this stage.

The Stage 7 package includes both exact restart checkpoints, source code, test scripts, measurement plans, action audits, one-field smoke-test arrays and a reproducibility guide. The checkpoint fields have no production measurements and cannot support physical inference.
