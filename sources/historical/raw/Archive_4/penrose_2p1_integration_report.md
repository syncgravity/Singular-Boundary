# Corrected-geometry 2+1D Yang–Mills integration — executed checkpoint

**11 October 2026**  
**Classification:** Verified software tests; exploratory Monte Carlo pilot; **no continuum Yang–Mills observable extracted**.

## 1. What was integrated

I extracted both user-supplied ZIPs, imported **only** the verified `direct_cut_project.py` generator for Penrose geometry and the previously tested quaternion holonomy mathematics for SU(2). The new `corrected_2p1_pilot.py` builds the entire 3D face/link incidence complex as the product of a verified **open 2D Penrose patch** and a **periodic 8-slice Euclidean time circle**. This avoids pretending that the earlier rational-direction Penrose torus was verified by the corrected construction. No legacy pentagrid geometry is used.

Six new checks were executed successfully: geometry/counts, open-face/time incidence, gauge-invariance of all plaquettes and three scalar operators and multi-edge Wilson rectangles, exact equality of the one-edge temporal rectangle with the temporal plaquette, correct boundary-link local-action differences, and a sampler smoke test. A final cached-vs-recomputed plaquette residual of zero was observed on the saved pilot chains.

## 2. Two new exploratory Monte Carlo pilots

Both use uniform beta=2.0, N_t=8, two independent chains (seeds 101, 211), 24 burn-in sweeps followed by 48 sweep steps thinned by four (24 saved configurations per geometry). **These runs are too short for equilibrium or physical-mass estimates.**

| Quantity | Radius 3.5 | Radius 5.0 |
|---|---:|---:|
| Vertices / edges / rhombi | 50 / 84 / 35 | 90 / 159 / 70 |
| 3D links / 3D plaquettes | 1,072 / 952 | 1,992 / 1,832 |
| Spatial boundary edges | 28 | 38 |
| Scalar basis: thin / thick / adjacent double | 11 / 24 / 56 | 25 / 45 / 121 |
| Mean plaquette, chain 101 | 0.46078 | 0.44977 |
| Mean plaquette, chain 211 | 0.45678 | 0.44904 |
| Maximum cached plaquette mismatch | 0 | 0 |

The following short-time Wilson rectangle averages pool 24 retained configurations and 12 spatial paths per edge-length category. Distances use the physical projected coordinates; temporal lag `t` is in Euclidean **lattice steps**. The bootstrap SE values are exploratory and only reflect the deliberately short sample.

| Radius | Spatial path edges | Mean Euclidean separation | W(t=1) | W(t=2) | W(t=3) |
|---|---:|---:|---:|---:|---:|
| 3.5 | 1 | 1.000 | 0.46414 | 0.20005 | 0.09011 |
| 3.5 | 2 | 1.626 | 0.24365 | 0.06519 | 0.01992 |
| 3.5 | 3 | 2.465 | 0.09918 | 0.02101 | −0.00360 |
| 5.0 | 1 | 1.000 | 0.45487 | 0.19692 | 0.09496 |
| 5.0 | 2 | 1.658 | 0.20460 | 0.06625 | 0.00716 |
| 5.0 | 3 | 2.486 | 0.09672 | 0.00942 | 0.00496 |

The scalar operators are spatial averages of traced rhombic loops (thin/thick) and six-link boundary loops surrounding adjacent face pairs. A full 3×3 connected temporal matrix `C_ij(t)` and its exploratory bootstrap covariance are saved. At time separation t=2, **none of the three diagonal scalar correlators has a signal-to-noise ratio above 3** in either pilot:

- Radius 3.5: −1.21, +1.61, +0.42.
- Radius 5.0: −0.10, +1.00, +1.58.

These are diagnostics of the signed connected correlator, not mass estimates. There is no eligible stable multi-time exponential/cosh plateau. The Wilson loops are at only short spatial distances and short temporal lags, with insufficient long-time plateau information for a string tension. In particular, **a Wilson rectangle decay rate at a single r is a static-source energy, not a glueball mass or a string tension**.

## 3. Why a continuum extrapolation is not yet supported

The two radii change the spatial patch size rather than shrink physical tile spacing at fixed physical volume. This is *not* a cutoff trajectory. The finite open spatial boundary also differs from the toroidal previous comparison, and a uniform Wilson face coupling on a nonorthogonal Penrose mesh is not yet demonstrated to be a suitable isotropic continuum regulator. There is currently no matched regular lattice in the new pilot.

Consequently:

\[
m_{0^{++}}(\beta)\quad \text{undetermined},\qquad
\sigma(\beta)\quad\text{undetermined},\qquad
\Delta\bigl(m_{0^{++}}/\sqrt\sigma\bigr)_{a\to0}\quad\text{undetermined}.
\]

## 4. Next research stages (not executed)

1. Construct **canonical, locally convergent periodic** model-set or inflation/substitution approximants and validate acceptance-window membership, oriented rhombic incidence, physical areas, and boundary identifications independently against the corrected open patches. Include a square reference and geometric-coupling controls.
2. Derive/test an isotropic nonorthogonal discretization (or explicitly compare multiple well-defined prescriptions), calibrate the renormalized anisotropy, and tune the physical scale using the string tension itself. Track actual physical source separation, not merely graph-edge count.
3. Implement true variance-reduced, improved scalar 0++ spectroscopy (spatial smearing/variational generalized eigenvectors, correlated long-time fits) and broad physical-distance static potentials, with full per-configuration histories and autocorrelation-aware resampling. Current pilot supplies the first three-operator basis and multi-distance loop infrastructure, not production spectroscopy.
4. Generate at least four lattice-spacing points at fixed spatial/temporal physical volume, test alternative continuum-fit powers, change the phason offset, and quantify finite-volume and local-coupling-distribution systematics.

**Decision:** The two historical archives were sufficient for this executed integration checkpoint. No additional uploads are required now; new data must be generated by further correctly controlled simulations.
