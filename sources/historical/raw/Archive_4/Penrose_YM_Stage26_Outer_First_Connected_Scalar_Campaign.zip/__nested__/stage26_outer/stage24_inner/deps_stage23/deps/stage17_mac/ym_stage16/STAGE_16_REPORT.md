# Stage 16 — SU(2) exact temporal multihit, heatbath control, and large matched-path screening

**Scientific status: METHOD VERIFICATION / EXPLORATORY BENCHMARK ONLY. No accepted glueball mass, string tension, or continuum Penrose–square difference.**

## Executive findings

1. **A critical Stage 13–15 transporter-convention error was identified.** Its `stage13_transport.mat()` is *anti-homomorphic* with respect to the original SU(2) quaternion product `wilson_torus.mul`: `mat(q)@mat(r)=mat(mul(r,q))`. Consequently, the legacy Stage 13–15 matrix-based Wilson rectangles are *not gauge invariant* under the original Wilson-action convention. A stringent test of 128 Wilson rectangles on a locally gauge-transformed flat field gave legacy maximum deviation from the correct value one of **1.9763**. Stage 16 reconstructs standard Wilson rectangles using the original quaternion multiplication; direct and exact multihit values are gauge invariant to within **1.4e-15** and **0.8e-15**, respectively. **Do not use Stage 13–15 raw noise-reduction claims as validated physical Wilson-loop performance.** The Stage 9–12 original Wilson-loop measurements use `corrected_2p1_pilot.rect_path` and are independently consistent with the corrected Stage 16 implementation; this particular defect does not invalidate those measurements.
2. **Exact SU(2) local multihit is implemented**, replacing the selected temporal links by their analytically integrated conditional first moments. The same-link, different-time temporal variables are conditionally independent given other links because no temporal plaquette contains two of them. Thus integration across a *single temporal source line* is exact given all other links. The method needs **zero inner warmup or inner MCMC samples for these integrated links**. A local SU(2) heatbath sampler is also provided as an optional exact conditional Gibbs draw; it does **not** equilibrate the rest of the temporal slab.
3. **13 tests passed**, including local action substitution, Bessel-moment formulas, conditional heatbath distribution, 128 continuous signed spatial paths, independent SU(2) matrix calculation, original Stage 9 quaternion Wilson kernel agreement, full SU(2) gauge invariance, and geometry-only matched path thresholds.
4. **Small interacting benchmark:** 8×8 periodic square torus, Nt=20, beta_ref=3.5, four independent seeds, 8 saved backgrounds per seed (32 total), 300 pilot warmup sweeps and 18 sweeps between saved fields. A real Metropolis action was used; this is **not production-equilibrated**. Three nested path-batch sizes 16, 64, 128; physical separations r=1,2,3,4; temporal lengths 4,10; all paths measured on the same fields for a paired comparison. At batch 128, t=10, raw standard-deviation reductions were **5.18×** for r=1, **3.85×** for r=2, **5.07×** for r=3 and **5.25×** for r=4. Measurement-only variance×time ratios were **0.63**, **1.14**, **0.66**, **0.62**, respectively. They therefore improve measured measurement-only efficiency in three of the four distance groups, not all four. When the cost of generating each outer gauge configuration in this short pilot is included, ratios were approximately **0.038**, **0.068**, **0.039**, **0.037**. These are timing screens, sensitive to workload and how pilot thermalization is amortized, **not certified production cost improvements**. At t=4 the measurement-only ratios are >1 in all distance groups.
5. **No significant paired-estimator disagreement established:** Chain-stratified exploratory bootstrap (2,000 resamples with 4 chains) gives a 95% interval for `multihit-direct` batch mean at t=10,r=1 of approximately **[-0.0714, +0.0205]**, and at r=2 **[-0.0291,+0.0502]**. These include zero; the four short outer chains are too few to certify equality or stationarity. `BOOTSTRAP_SCREEN.json` contains details.
6. **Large geometry-only matched catalog:** Reconstruct 1,000 candidate spatial Wilson paths on each of the validated-size rational M55 torus and equal-area 151×151 square torus (10 graph edges maximum, 180 anchors, up to 100 candidate paths per edge-count). Hungarian assignment of candidate pairs under **≤5% relative physical displacement norm** and **≤25° unsigned orientation-axis discrepancy** yields **600 distinct matched pairs**, with square spatial separations approximately **1.275–5.701**. These criteria do not match detailed bend shape, anisotropy, renormalized coupling, or continuum discretization. The M55 torus remains *not independently certified* as a canonical Penrose inflation approximant; its previous radius-two motif-only test does not confer complete geometric admission.
7. **Genuine million-link smoke measurements:** On one final checkpoint **from each of four independent Stage 9 seeds per geometry** (8 final gauge fields in all), the corrected code measured all 600 matched paths at t=4 and t=8 using both direct and multihit estimators. All outputs were finite; the matching geometry and full Wilson action were used. Four final fields per geometry are **not 3,600 time-series observations**. There is no sensible long-time potential plateau or string tension from this smoke run, and standard deviations across correlated paths are not independent statistical errors. `LARGE_SNAPSHOT_SCREEN.json` records per-seed measurements and runtimes. Historic per-configuration Stage 9 link fields were not archived, so the existing 900×4 Wilson measurement time series cannot simply be recalculated with multihit without new updates.

## Exact SU(2) conditional integration

For a unit quaternion link \(q=(q_0,q_1,q_2,q_3)\in S^3\), the original Wilson action gives, with its other links held fixed,

\[
P(q\mid U_{\setminus e})=\frac{1}{Z(h)}\exp(q\cdot h),\qquad
h_i=\sum_{p\ni e}\beta_p\,\tfrac12\operatorname{ReTr}\big[U_p(q=e_i)\big].
\]

The identity \(\operatorname{ReTr}U_p/2\) is linear in any one link, so evaluating four orthonormal trial quaternions produces the exact local field. The conditional first moment over SU(2) Haar measure is

\[
\mathbb E[q\mid U_{\setminus e}]
=\frac{I_2(\kappa)}{I_1(\kappa)}\frac{h}{\kappa},\qquad\kappa=\Vert h\Vert.
\]

Modified Bessel functions use *exponentially scaled* `scipy.special.ive` for large \(\kappa\). A small-field limit \(\mathbb E[q]\simeq h/4\) removes the removable singularity. A von Mises–Fisher sampler on \(S^3\) provides an independent exact SU(2) heatbath control.

The temporal source links \(U_t(u)\) at a fixed spatial vertex \(u\) and distinct time slices do not appear together in an elementary Wilson plaquette. Their conditional joint law factors when all other links are frozen. Therefore the rectangle's source-line transporter, which is multilinear in these links, is integrated **exactly by replacing each source link with the SU(2) conditional mean**. The spatial endpoint paths and the destination temporal transporter are not integrated, so gauge covariance is maintained and the result is an unbiased Rao–Blackwell estimator for the original Wilson observable under an equilibrium outer ensemble.

**Scope restriction:** Adjacent spatial vertices' temporal links generally share plaquettes and cannot be jointly replaced by products of independently calculated conditional means. `multihit_batched` instead integrates **one source line per observable**, using the same deterministic per-source field across many observables, not asserting an unjustified joint independence for neighboring sources. The exact Gibbs draw on a source line is equilibrated *only conditional on all other links*, not a complete slab update.

## Conditional heatbath mixing control

A fixed-neighborhood one-link test at \(\Vert h\Vert\approx9.881\) with 6,000 trials compared a legacy local Metropolis walk against independent exact heatbath draws. The projection onto the conditional preferred direction had a target mean \(0.85249\): Metropolis empirical mean \(0.85993\) with lag-one autocorrelation \(0.854\) and acceptance 52.4%; exact heatbath mean \(0.85390\) with lag-one autocorrelation \(0.0036\). These are local IID checks, **not evidence of full-slab equilibration or improved production ESS**. The multihit estimator avoids drawing either kind of sample altogether for the integrated source line.

## Cost evaluation and uncertainty restrictions

Measurement elapsed times were recorded after one-time Numba compilation, with each 128-path direct batch costing ~0.1 ms and conditional mean integration costing ~1–2 ms depending on temporal length. Thus a factor-five reduction in across-background standard deviation is not necessarily a factor-25 *measurement-only* efficiency gain. At t=10, r=2, measurement-only cost×variance did **not** improve. Including costs of independent outer gauge-field updates favors analytic integration in this *particular short pilot*, but the pilot's burn-in is amortized over only 8 fields per chain, so these ratios must be remeasured for long equilibrated chains on the actual M55 geometry.

The pilot has just 32 outer backgrounds and deliberately does not satisfy predeclared equilibration / confidence / positivity / three-time plateau gates. Correlations across paths are handled by averaging at the level of each gauge background before calculating variance. The chain-stratified resampling does not certify a physical error interval with only four short chains. Neither nonperturbative anisotropy matching nor finite-volume/alternate-approximant/continuum checks were attempted.

## Numerical admission status

| Requirement | Status |
|---|---|
| Correct Wilson quaternion ordering and gauge invariance | **PASSED** |
| Exact SU(2) local conditional first moment / heatbath tests | **PASSED** |
| Exact conditional integration on one temporal source line | **PASSED** |
| Four-chain exploratory square paired benchmark | **COMPLETED; not production-certified** |
| Large candidate physical-distance-and-axis path matching | **600 matched pairs; geometry-only** |
| Multihit on Stage 9 final M55 and square fields | **8 real-field smoke tests; not an ensemble** |
| Inner-slab convergence for *unintegrated* links | NOT ESTABLISHED |
| Production total-cost variance advantage | NOT ESTABLISHED |
| Positive, plateau-stable multi-time static potentials | NOT ESTABLISHED |
| Nonperturbatively matched \(\sigma\) | NOT ESTABLISHED |
| Independently stable \(m_{0^{++}}\) | NOT ESTABLISHED |
| Continuum \(\Delta R_0\) | NOT ESTABLISHED |

## Recommended Stage 17 production action

Integrate the corrected multihit estimator into a restarted *post-equilibrium Stage 9* measurement driver and measure several independently seeded outer snapshots per geometry, with matched 600-path batches at t=2–10, retaining per-field path indices, physical displacement, winding/orientation, and covariance. Save observables directly, not full million-link fields at every step. Compare raw and multihit **paired** per-outer-field estimates, perform independent-chain block resampling, and use several temporal lengths to check for plateaus; if the 600-path sweep cost is too high on an 8 GB M1, benchmark a stratified ≤100-path subset first without changing the geometry-matching criteria. Use a frozen training chain for path selection and held-out chains for acceptance. Do not infer a string tension from this stage's short-pilot or snapshot results.

## Outputs / reproduction

- `stage16_multihit.py` — analytic SU(2) local moments, exact heatbath, correct quaternion Wilson rectangles, batch geometry and temporal-line integration.
- `stage16_benchmark.py`, `BENCHMARK.json`, `BENCHMARK_SUMMARY.json`, `stage16_screen_ci.py`, `BOOTSTRAP_SCREEN.json` — real interacting square pilot / speed and uncertainty screens.
- `stage16_heatbath_mixing.py`, `HEATBATH_MIXING.json` — local conditional equilibration control.
- `stage16_matched_paths.py`, `MATCHED_PATH_SCREEN.json`, `{square,penrose}_candidate_paths.npz` — 600 matched large-torus path pairs.
- `stage16_large_snapshot.py`, `LARGE_SNAPSHOT_SCREEN.json` — corrected paired measurements on the eight final Stage 9 checkpoints; raw checkpoint files are not redistributed.
- `stage16_convention_audit.py`, `CONVENTION_AUDIT.json` — independent flat-field gauge-covariance test of legacy and corrected Wilson rectangles.
- `test_stage16.py`, `test_stage16_matched.py`, `TESTS.log` — 13 tests passed.

Run all tests from `ym_stage16` with sibling `ym_stage13` dependencies in place:

```
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -m unittest -q test_stage16 test_stage16_matched
```

`Stage16` does not alter historic Stage 9 gauge fields or archived files. This report supersedes Stage 13–15's claim that their particular transporter matrix computations were validated *physical Wilson-loop* estimators, while preserving their historical software and statistical audit trails.
