# The Singular Boundary × Yang–Mills — Stage 3
## Calibrated toroidal pilot, autocorrelation gate, and physical-distance scale-setting audit

**Executed:** 11 October 2026. **Scope:** exploratory 2+1-dimensional interacting SU(2) Wilson calculation. **Decision:** software and geometric boundary-condition checkpoint passed; physical spectroscopy and string-tension gates failed. No continuum or quasiperiodicity-specific mass-gap conclusion is drawn.

## Executive decision

The preceding Stage 2 ran the corrected direct-cut-and-project **open** Penrose patch against an **open** square control. Here we add an actual spatial torus comparison to remove the open-versus-periodic boundary mismatch from the *pilot*. A rational model-set **M=5** torus (188 vertices, 376 edges, 188 rhombi) is paired with a **13×14** periodic square torus (182 vertices, 364 edges, 182 faces). Both have total spatial area **61.7089944822**, with nearly matched global aspect ratios and an exactly common Euclidean time spacing **a_t = sqrt(61.7089944822/188) ≈ 0.57292175**. All spatial links and time links participate in the 2+1D Wilson action; this is not a set of decoupled 2D models. The M=5 model is a **rational periodic model-set candidate**, not a certified canonical Penrose inflation supertile or a locally admitted Penrose control. Its previously recorded radius-two motif TV distance is 0.9043, exceeding the pre-registered 0.15 motif-only threshold. Stage 2's M=55 motif-screen success is **not** transferred to these M=5 ensembles.

We generated **four seeded chains per geometry** (`101,211,307,419`), each with **64 burn-in and 200 retained-measurement sweeps**, thinning by 4, yielding **50 saved snapshots per chain** and **200 fully saved 2+1D gauge configurations for each torus** (400 total), at **beta_ref=3.5** and **N_t=8**. Calibrated face and edge couplings follow the weak-field Stage 2 positive formula, without a renormalized anisotropy or string-tension match. All 29 unit/integration tests passed (20 inherited and nine new), including physical path displacement across torus seams, plaquette closure, action gauge invariance, and multiedge Wilson rectangles.

## 1. Wilson action and physical geometry

For a spatial face with area \(A_f\), spatial edge \(e\) of physical length \(\ell_e\), dual-edge area \(A_e^*=\tfrac12\sum_{f\ni e} A_f\), and reference step \(a_*\), the action uses

\[
S=\sum_{t,f}\beta_s(f)\left(1-\tfrac12\operatorname{ReTr}U_{t,f}\right)+\sum_{t,e}\beta_t(e)\left(1-\tfrac12\operatorname{ReTr}U_{t,e}\right),
\]
\[
\beta_s(f)=\beta_{\rm ref}\frac{a_*a_t}{A_f},\qquad
\beta_t(e)=\beta_{\rm ref}\frac{a_*}{a_t}\frac{A_e^*}{\ell_e^2}.
\]

The **same** \(a_*=a_t\) is applied to both tori. The true edge displacement is computed from the parent Z5 projected basis for the rational model set and by wrapped unit directions for the square. Subtracting canonical vertex representatives across a torus seam would yield a false long edge and invalid source distance. The spatial-torus plaquette incidence is twice per spatial edge; the three-dimensional action has **4,512 links** on the rational model-set torus and **4,368** on the square torus for \(N_t=8\).

Global weak-field spatial-vs-temporal tensor eigenvalues are 1, 1 within numerical precision on both tori, as checked computationally. This is **not** a nonperturbative determination of anisotropy or proof of local geometric continuum consistency.

## 2. Fresh gauge-invariant Wilson-loop data

The multi-edge Wilson rectangle \(W(r,t)\) is measured on each saved gauge configuration for spatial path lengths 1, 2 and 3. The true physical source separation \(r\), angle and path structure are retained per path. The following are **ensemble means over path groups**, whose spread in \(r\) is nontrivial; statistical errors and per-configuration arrays are saved in the archive.

| Geometry | Paths in group | Mean physical r | W(t=1) | W(t=2) | W(t=3) |
|---|---:|---:|---:|---:|---:|
| Rational M5 | 1 edge | 0.635 | 0.62503 | 0.39921 | 0.25737 |
| Rational M5 | 2 edges | 1.066 | 0.39997 | 0.17118 | 0.07624 |
| Rational M5 | 3 edges | 1.507 | 0.27388 | 0.08643 | 0.02794 |
| Square 13×14 | 1 edge | 0.582 | 0.68354 | 0.48078 | 0.34026 |
| Square 13×14 | 2 edges | 0.994 | 0.49921 | 0.27905 | 0.15821 |
| Square 13×14 | 3 edges | 1.450 | 0.35585 | 0.15281 | 0.06786 |

The block bootstrap preserves chain membership, temporal Wilson-loop covariance and neighboring time-lag covariance, using five saved configurations per block (40 resampled chain-stratified blocks in total). For one-edge paths, **short-time** effective energies from \(-\log[W(t+1)/W(t)]/a_t\) are:

- Rational M5: \(V_{\rm eff}(2/1)\approx0.782\) (bootstrap 95% interval 0.758–0.809) and \(V_{\rm eff}(3/2)\approx0.766\) (0.727–0.803).
- Square: \(V_{\rm eff}(2/1)\approx0.614\) (0.595–0.634) and \(V_{\rm eff}(3/2)\approx0.603\) (0.575–0.631).

These are **neither matched-r static potentials nor string tensions**. The first comparison probes different physical separations, may have excited-state contamination, and has not been renormalized to a common physical coupling.

### Actual physical-distance bins (not link-count bins)

We additionally reran the analysis with the *same* radial bins for both geometries. Of the common populated bins, two have mean physical separations agreeing within 5%:

| Physical r bin | Mean r, M5 | Mean r, square | Relative mismatch | W(t=2), M5 | W(t=2), square |
|---|---:|---:|---:|---:|---:|
| [1.05,1.35) | 1.1974 | 1.2431 | 3.74% | 0.15662 | 0.19701 |
| [1.65,1.95) | 1.7375 | 1.7469 | 0.54% | 0.07688 | 0.14770 |

For the second bin, short-time \(V_{\rm eff}(2/1)\) is 2.185 [1.959,2.420] vs 1.509 [1.366,1.658] (nominal 95% chain-block intervals). The **difference cannot be attributed to Penrose physics**: M5 fails local admission; path shapes/orientations, higher cutoff effects, renormalized couplings and anisotropy are unmatched; two or three temporal separations are inadequate for an asymptotic plateau. The physical-distance binning infrastructure is now in place, but **\(\sigma\) is not fitted**.

## 3. Scalar spectroscopy and autocorrelation gate

The saved configurations also contain the full three-operator time series of connected scalar Wilson-loop observables (Penrose: thin/thick rhombi and adjacent double-rhombus loops; square: two checkerboard-labelled plaquette groups and adjacent two-plaquette loops). Chain-stratified bootstrap calculations are performed on the connected \(3\times3\) correlator matrix, subtracting the ensemble vacuum expectation correctly on every bootstrap replicate.

At Euclidean lag t=2, **diagonal scalar C(t=2) signal/noise** is:

- Rational M5: **−2.51, +0.03, −0.72** for the three basis operators.
- Square: **+0.63, −0.51, +0.01**.

The symmetrized C(2) matrix has negative eigenvalues in both point estimates. In 500 chain-block bootstrap replicates it is positive-definite in **0%** (rational M5) and **1%** (square). These outcomes rule out trusting a three-channel generalized-eigenvalue mass plateau at the current precision. A noisy negative estimator does not imply a physical negative spectral weight.

Rank-normalized multichain diagnostics were separately computed from per-configuration scalar averages and short Wilson loops. They **do not pass** the originally specified \(\hat R<1.01\), bulk/tail ESS ≥ 400 gate:

| Diagnostic | Rational M5 | Square |
|---|---:|---:|
| Largest monitored R-hat | 1.0213 | 1.0915 |
| Smallest monitored bulk ESS | 98.4 | 35.8 |
| Number of snapshots | 200 | 200 |

The pilot burn-in and number of configurations cannot certify thermal equilibrium, and convergence thresholds are not silently relaxed. There are still only two to three nonzero temporal lags with even moderately resolved Wilson-loop data, no scalar plateau, and only one coupling/spacing in the torus study.

**Decision:** Reject \(m_{0^{++}}\), \(\sigma\), \(m_{0^{++}}/\sqrt\sigma\), and any continuum-extrapolated geometry shift. The physical difference is not measured.

## 4. Next physical-production checkpoint

1. **Admit geometry at matched physical size:** extend the model-set torus and regular reference to a common physical aspect and volume; compare locally matching regions and multiple offsets; identify long-range-order contrasts independently. M55 passes motif-only screening but is not admitted as a fully matched finite-volume causal control.
2. **Determine a physical scale:** use a dense family of physically binned and angle-binned long-time Wilson loops, or gauge-invariant winding-flux (torelon) correlators on the spatial tori. Extract \(V(r)\) only after an excited-state plateau; then fit its long-distance slope with finite-volume and string-correction checks. Tune physical anisotropy and \(\sqrt\sigma\) separately, not just bare beta.
3. **Improve scalar spectroscopy:** introduce gauge-covariant link smearing and a larger variational basis, and variance-reduction/longer temporal extent. Require a positive, statistically stable covariance/GEVP fit over at least three usable time points, plus operator/fit-window cross-checks.
4. **Certification and continuum:** use longer checkpointed independent chains until the actual joint observables satisfy convergence/ESS requirements; vary beta and lattice spacing at fixed physical volume/temporal extent with at least four cutoff scales and more than one tiling offset; fit correlated ratios using multiple correction ansätze.

## 5. Reproduction

`stage3_periodic_pilot.py` constructs the rational model-set torus using Stage 2 `build_torus(5)` and a new square torus with fully explicit oriented face-edge incidence, computes physical signed edge vectors across seams and performs Metropolis sampling with calibrated weights. The four seeded chains save **all gauge links**, operator time series, physical-path metadata and Wilson rectangles. `stage3_statistical_gate.py` computes scalar correlators, diagnostics and covariance-aware bootstrap effective energies. `stage3_physical_bins.py` bins observations by actual physical distance. `test_stage3.py` and `test_stage3_stats.py` add nine tests to the inherited suite (29 passing total). Dependencies: NumPy, SciPy, Numba and ArviZ; single-threaded BLAS recommended.

From the package root:

```bash
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1
python -m unittest -q test_corrected_2p1_pilot test_stage2_ym_calibration test_stage2_rational_torus test_stage3 test_stage3_stats
python stage3_periodic_pilot.py --out outputs --four-chains --burn 64 --steps 200 --nt 8 --beta 3.5
python stage3_statistical_gate.py
python stage3_physical_bins.py
```

All numerical arrays, including the 400 saved 2+1D gauge configurations, are included in the new Stage 3 archive; no raw data needs to be retrieved from earlier chats. The earlier Stage 2 archive remains separate provenance.
