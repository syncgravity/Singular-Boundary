# Stage 5 — Longer-time square-reference SU(2) spectroscopy

**Research status (11 October 2026): new interacting gauge ensembles generated and remeasured; no physical glueball mass or string tension admitted.**

## Executive result

This checkpoint executed a new, reproducible, *square-torus reference* in 2+1 Euclidean dimensions, extending the prior eight-slice calculation to **20 time slices**. The SU(2) Wilson-action Monte Carlo delivered **960 stored gauge configurations from four independently seeded chains**, and the updated measurement engine evaluated a nine-operator scalar basis, spatial winding flux in both torus directions, and actual-physical-distance-binned temporal Wilson rectangles through time separation ten.

The 20 new and inherited regression tests passed. All 28 monitored diagnostics meet the stipulated rank-normalized `Rhat < 1.01` target, but **only 10/28 meet the combined effective-sample-size gate**; the minimum monitored bulk ESS is **237.86**, below the required 400. The largest nominal positive scalar `C(t=2)` signal-to-bootstrap-SE ratio is **2.292**; full scalar matrices are not sufficiently positive definite for a generalized-eigenvalue analysis, and winding-flux correlators remain weak. **Neither the mass, nor string tension, nor their ratio can be reliably quoted.**

The square-torus reference is *not* a matched Penrose geometry. The previously studied rational M=5 model-set torus fails the Penrose local-geometry admission test and is not used for physical causal inference in Stage 5.

## 1. Fixed action and new chains

For each oriented spatial or temporal plaquette `p`,

\[
 S[U]=\sum_p\beta_p\left[1-\tfrac12\operatorname{ReTr} U_p\right],\qquad U_e\in SU(2).
\]

The diagonal geometric Hodge candidate adopted from Stage 2 is used, **not** assumed to be a nonperturbatively renormalized or rotationally perfect discretization. For this square control its calculated tree-level directional response eigenvalues are 1 and 1; renormalized physical anisotropy has not been determined.

| Parameter | Stage 5 value |
|---|---:|
| Spatial regulator | square torus, 13 × 14 faces |
| Spatial vertices / links / faces | 182 / 364 / 182 |
| Spatial physical area in construction units | 61.70899448 |
| Spatial period lengths | 7.56975622 and 8.15204516 |
| Euclidean time slices | 20 (previous pilot: 8) |
| Calibrated reference step \(a_t=a_*\) | 0.57292175 (construction units) |
| Bare reference coupling \(\beta_{\rm ref}\) | 3.5 |
| Independent seeds | 101, 211, 307, 419 |
| Initial sweeps per chain | 300 |
| Production sweeps per chain | 1,200 |
| Saving interval | 5 sweeps |
| Configurations retained per chain | 240 |
| Total retained configurations | **960** |
| Total link variables per configuration | 10,920 |

All four chains' gauge links, raw plaquette-action measurements and checksum-audited provenance are saved. Accepted-proposal fractions were approximately 0.503 for every chain; local cached-versus-recalculated plaquettes agreed numerically at their recorded final states. The chains **do not** include a demonstrated multilevel conditional-update algorithm.

## 2. Improved operators and statistical methods

- Spatial APE smearing with SU(2) projection, \(\alpha=0.4\), levels 0, 2, 6, on each saved configuration. Temporal links are unchanged.
- Nine scalar \(0^{++}\)-candidate operators: translation- and quarter-turn-averaged \(1\times1\), \(1\times2\) / \(2\times1\), and \(2\times2\) spatial loops, each at the three smearing levels.
- Spatial winding-flux loops in both torus homology directions, sampled from **24 distinct anchors per direction**, at every smearing level. These are noncontractible gauge-invariant operators, not static point-source rectangles.
- Temporal Wilson rectangles along shortest paths of up to four spatial edges, with actual periodic-geometry displacements, not just link count, retained as physical distances. Time lags \(1,\ldots,10\) measured using the entire periodic time circle.
- Connected covariance estimated using time-translation averages and ensemble VEV subtraction; uncertainty from a **220-replicate, chain-stratified, 10-configuration moving block-resampling implementation** (resampling non-overlapping blocks with replacement; it is *not* an independent per-time-slice bootstrap). Computation caches per-gauge-configuration time-shifted products to avoid repeated evaluation. Asymptotic autocorrelation is separately assessed using bulk/tail ESS and rank R-hat, not assumed to be corrected by smearing.

Because smearing levels share underlying gauge fields, their statistical covariance is preserved. The 20 tests include a direct equivalence check of the accelerated covariance code against the unaccelerated estimator.

## 3. Numerical precision, and why the mass fit is rejected

| Metric | Result |
|---|---:|
| Monitored scalar/action/W/flux statistics | 28 |
| Largest R-hat among those | 1.009729 |
| Minimum bulk ESS | 237.863 |
| Minimum tail ESS | 434.605 |
| Metrics passing R-hat and bulk/tail ESS targets simultaneously | 10/28 |
| Largest positive \(C_{0^{++}}(2)/\operatorname{SE}\) among nine scalar operators | 2.292 |
| Smallest eigenvalue of full scalar \(C(1)\) | \(-6.0654\times10^{-7}\) |
| Smallest eigenvalue of full scalar \(C(2)\) | \(-2.5938\times10^{-6}\) |
| Bootstrap samples with full nine-by-nine \(C(2)\) positive definite | 0/220 |

The largest nominal scalar signal at the second nonzero temporal separation occurs in the two-sweep APE, \(2\times2\) scalar operator. Its response is still below a three-standard-error diagnostic threshold, and the full generalized eigenvalue problem is not stable at \(t_0=1,t=2\). No statistically supported three-or-more-time effective-mass plateau or covariance-controlled multi-state fit has been demonstrated. The sign of a noisy sample correlation-matrix eigenvalue is **not** evidence of a physically negative spectral weight.

**Decision: \(m_{0^{++}}\) not determined.**

## 4. Temporal Wilson loops: resolved short distances, unresolved asymptotic potential

Actual physical-distance bins separate the short-distance evidence from the as-yet unresolved long-distance string tension. The entries are *nominal* blocked-bootstrap signal-to-error ratios for two-sweep APE; comparisons with previous stages have different temporal extents and statistics.

| Physical r bin | Mean r | Paths | W(t=4) S/SE | W(t=6) S/SE | W(t=8) S/SE | W(t=10) S/SE |
|---|---:|---:|---:|---:|---:|---:|
| 0.5–1.0 | 0.663 | 30 | 179.3 | 75.0 | 41.0 | 21.8 |
| 1.0–1.5 | 1.242 | 23 | 53.0 | 14.9 | 4.0 | 0.6 |
| 1.5–2.0 | 1.767 | 22 | 23.5 | 4.2 | 1.2 | -0.8 |
| 2.0–2.5 | 2.329 | 5 | 6.2 | 2.1 | -0.1 | 0.2 |

At the \(1.5\le r<2\) range, two-sweep APE gives a nominal \(t=4\) signal-to-error ratio 23.5 versus 17.4 without smearing, but it is not a demonstrated improvement in \(\sigma\) precision. There is no long-distance, long-time plateau with a demonstrated stable \(V(r)\) slope, and these accessible r values may still contain Coulomb and excited-state contributions. **String tension from a static potential is not determined.**

## 5. Winding flux and scale setting

The physical spatial winding-loop lengths are **7.56976** and **8.15205** construction units. Center-charge behavior and winding topology were validated in Stage 4 and preserved here. The six positive or negative \(t=2\) winding signals across the 3 APE levels × 2 directions have a largest *positive* signal-to-bootstrap-SE ratio only **0.492**. With no stable torelon energy, neither the string tension nor a finite-length effective-string correction can be fitted.

Longer Euclidean extent and time averaging alone did not solve the confining flux signal/noise problem. Multilevel temporal-slab sampling or an independently validated alternative variance-reduction method is the highest priority before enlarging the spatial torus.

## 6. Admission decisions and next experiment

| Research question | Stage 5 decision |
|---|---|
| Executable, reproducible SU(2) square Nt=20 reference | Passed |
| Gauge-covariant smearing and 9-operator measurement | Passed tests and executed |
| Physical-distance-binned Wilson rectangles through t=10 | Executed |
| Multiple winding anchors, two torus directions | Executed |
| R-hat < 1.01 on monitored observables | Passed |
| Bulk/tail ESS ≥400 on *all* monitored observables | **Failed (10/28 fully admitted)** |
| Stable positive variational scalar correlator and mass fit | **Failed** |
| Stable torelon or asymptotic static potential and string tension | **Failed** |
| Nonperturbatively matched anisotropy / scale | **Not performed** |
| Penrose-specific continuum contrast | **Not attempted** |

The next stage should validate temporal-slab multilevel variance reduction on the square torus, target the weak scalar and center-flux channels specifically, extend the checkpointed Monte Carlo chains until the **actual** effective sample sizes and fit windows pass, and obtain \(\sigma\) from a stable long-time, long-distance signal. Only afterward should similarly measured, locally admitted periodic Penrose approximants be brought into a matched physical-scale program with multiple couplings and continuum extrapolations.

The published regular-lattice continuum benchmark for \(m_{0^{++}}/\sqrt{\sigma}\) remains a **literature reference**, not a number derived from this checkpoint.

## 7. Reproducibility and original raw outputs

All source files necessary to repeat the square run and the Stage 4 operators are in the accompanying ZIP along with:

- `configs_seed{101,211,307,419}.npz`: 960 **actual** saved gauge configurations in total, plus action traces.
- `obs_seed*.npz`: each configuration's time-dependent nine scalar operators, six winding signals, and physical-distance Wilson rectangles through t=10.
- `settings.json`, `chain_seed*.json`, `paths.json`, `winding_paths.json`: exact sampler and geometric source definitions and checksums.
- `stage5_correlator_matrices.npz`, `stage5_analysis.json`, `stage5_longtime_wilson_diagnostics.json`: covariance-aware measurements and gate decisions.
- `stage5_generation.log`, `stage5_measurement.log`, `stage5_analysis.log`, test results, and a SHA-256 manifest of ZIP payload entries.

Run instructions are in `README.md`. The raw pilot is intentionally identified as *non-admitted spectroscopy*, not as a completed continuum gap measurement.
