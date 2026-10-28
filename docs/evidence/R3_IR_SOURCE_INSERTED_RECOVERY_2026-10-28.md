# The Singular Boundary — R3-IR source-inserted transfer and connected-correlator recovery

**Date:** 2026-10-28. **Scope:** exact original October 26 R3-IR notes; Stage 11–20 mathematical source and saved summary records; archived R3 contraction note. **No new research conjecture, Monte Carlo chain replay, mass fit, continuum extrapolation or new simulation.**

## Conclusion and status definitions

**No recovered source proves a volume- and regulator-uniform positive physical-energy exponential connected *vacuum* Wilson-source decay for the interacting Penrose SU(2) trajectory, or an equivalent Hamiltonian R3-IR spectral gap.** We recovered exact finite-volume *source-insertion identities*, exact *local conditional measurement* methods, restricted low-energy estimates, and *numerical* connected scalar estimates. These are different assertions, and must not be promoted to a common mass-gap theorem.

Classification: **E** exact algebra/formal theorem under stated finite-model hypotheses (independent verification limited to core identities or archived proofs); **M** exact unbiased measurement construction conditional on correct outer equilibrium; **N** finite-sample evidence only; **C** sufficient but unproved R3-IR hypothesis; **O** open.

## 1. Source-to-status ledger

| Archived primary record | Existing result | Class | R3-IR limitation |
|---|---|---|---|
| `FORMAL_CHARACTER_BLOCKING_AND_R2_AUDIT.md`, 2026-10-26 | Exact SU(2) one-link Bessel-character coefficient; exact two-face fused-loop source derivative; first interacting center-neutral off-diagonal insertion `⟨j'|C M_p C|j⟩` | E | Does not bound connected sources after arbitrary spatial/time blocking; full interacting transfer is not diagonal in free-character labels |
| `R3_THEOREM_OBSTRUCTION_AND_MULTISCALE_GATE.md`, 2026-10-26 | Exact `||P_s i[H,B]Ω||²≤s²||QBΩ||²` for commutator sources; disjoint-support *full* static current response cancels; center 1-form selection rules | E | Derivative sources suppress their own low-energy overlap but do not uniformly observe arbitrary low-energy glueball modes; contact cancellation need not hold band-by-band |
| `FORMAL_THEOREMS.md`, `SCALAR_WILSON_IR_AND_COMPLETENESS.md` | K1/K2, Wilson-area f-sum, high-spin (`j(h)≫1/h`) restricted low-energy suppression, Wilson-algebra density | E | Positive first moments are **not** IR upper bounds; high-spin sources lack continuum normalization/observability; qualitative density not uniform frame |
| `FORMAL_FRAME_AUDIT.md`, `FORMAL_NOTE.md` | Electric-limit exact Wilson/spin-network frames; multi-component locality no-go; operator-frame + infrared inequality implies a gap | E/C | No simultaneously interacting, continuum-uniform observability and independent collective operator-norm IR estimate |
| `R3_SU2_transfer_barrier_2026_10_27_bundle.zip` | Stationary *uninserted* temporal-face partition ratio `Z_full/Z_deleted≥∏ z(beta)` | E | A free-energy comparison, **not** source-inserted time-decay. The single-face Wilson countertest already demonstrates no automatic spectral gap |
| `R3_Penrose_contraction_next_bundle(1).zip` | Conditional 54-fill nonnegative B-matrix Ward criterion; naive-star self-feedback obstruction | E/C | It is a local Gibbs *energy* recursion, not a Hamiltonian source-transfer estimate; archive is byte-identical to earlier copy |
| `STAGE_11_Heldout_Spectroscopy_Analysis.zip` | Held-out scalar connected estimates on seed 419; Wilson temporal rectangular signals | N | No accepted late-time scalar fit, no gauge-invariant continuum excitation estimate |
| `STAGE_12_Physical_Wilson_Audit.zip` | Actual physical-distance Wilson-loop paths reconstructed; short-time potential screens | N | No accepted long-time static potential or string tension; Wilson rectangles probe static-source-sector dynamics, not directly neutral vacuum 0++ decay |
| Stage 13–15 temporal-transporter ZIPs | Fixed-boundary conditional transporter *proposal* and tiny exploratory benchmarks | **invalidated for legacy matrix Wilson observable** | Stage 16 proves `stage13_transport.mat` is anti-homomorphic relative to original quaternion action; **do not use Stage 13–15 raw precision gains as gauge-theory evidence** |
| `Penrose_YM_Stage16_Exact_Multihit_Matched_Paths.zip` | Correct quaternion Wilson rectangles, gauge-covariance tests; exact SU(2) one-temporal-line conditional mean `E[q|rest]=(I2(k)/I1(k))h/k` and source-line conditional factorization | M | Rao–Blackwell variance reduction for Wilson **rectangle** under stationary outer gauge law; **not** connected scalar vacuum source transfer, not exact integration of entire slab |
| `Penrose_YM_Stage17_Mac_Production_Multihit.zip` | Restart/continuation runner using corrected Stage 16 estimator, retained paths and nine temporal lags | M (pipeline) | Runner **is not itself** proof of completed production equilibration, fitted potential, source-inserted gap bound or independently sourced new chains |
| `Penrose_YM_Stage18_Scalar_Continuation.zip` and `Stage18_Scalar_12000_Initial_Audit.zip` | Spatial scalar measurement at 4 APE levels × 3 operators, connected timeslice analysis on 8 continuing chains | N | No positive >2σ at any of t=2..6 across the 12 channels in reported block-20 screen. No accepted 0++ mass |
| `Stage19_15000_Scalar_Continuation_Audit(1).zip` | 8-chain, 3,920-sample ensemble-connected timeslice scalar curves through sweep 15,000 | N | **No** channel has three consecutive positive 2σ later-time points across block widths 10/20/40/80 |
| `Stage20_Scalar_Vacuum_Estimator_Benchmark.zip` | Cross-chain unbiased disconnected-mean-subtraction *under independence/stationarity assumptions* and block-bootstrap benchmark | N + elementary estimator identity | Corrects minor plug-in bias, not the connected-correlator variance bottleneck; **no** three consecutive positive 2σ points at t=2..6 |

## 2. Scope of the exact source-inserted results

The *single-rhombus* fundamental source transfer is an actual vacuum-centered correlator in that simplified model:

`C_A(n)=⟨Q A Ω,(T/λ0)^n Q A Ω⟩= (1/4)[I2(beta)/I1(beta)]^(4n)` for `A=χ_(1/2)(W)/2` and vanishing spatial magnetic potential. It proves exponential decay **at fixed beta** and identifies its exact physical rate, but it has no uniform positive rate over all coefficient scales. It is not the actual interacting Penrose continuum gauge system.

The October 26 full Wilson character insertion and midpoint potential insertion explicitly mix representations. These formulas preserve the source exactly at the first blocking step; they do not establish contraction under repeated interacting blocking. Similarly, Ward identities and the f-sum bound control positive spectral moments, not the inverse-energy resolvent needed for long-time neutral response.

The Stage 16 one-line multihit identity is an **estimator**: conditional expectation reduces measurement variance without changing the equilibrium expectation. The line's conditional decoupling works because no temporal plaquette contains two different time-slice source links on the same vertex. It does not integrate an adjacent destination line (its links can share plaquettes), nor two separated scalar time-slice spatial plaquette fields. The Stage 13–15 legacy matrix anti-homomorphism must not be inherited by a new source estimator.

## 3. Saved-data checks, no source simulation

- `Stage19_15000_Scalar_Continuation_Audit(1).zip` is byte-identical to the previously uploaded unsuffixed Stage 19 audit; `R3_Penrose_contraction_next_bundle(1).zip` is likewise an exact byte duplicate. Neither counts as independent corroboration.
- Stage 19 archived `RESULTS.json` has eight chain metadata entries, four channels per geometry, and **zero** saved three-consecutive two-standard-error positive windows at all four block widths on square and Penrose. Square eight-face at lag 2 is individually positive but does not propagate to three lags.
- Stage 20 archived `RESULTS.json` has the per-channel `cross_chain − plugin` shift **exactly constant in temporal lag** (verified from saved decimal arrays); no three-lag acceptance window under either estimator across the four bootstrap widths. The maximum absolute shift across each geometry is ≈`8.26e-10` square and `1.059e-9` Penrose in scalar correlator units.
- **Minor original report discrepancy:** The report states the estimator correction is at most `0.015` cross-chain bootstrap SE over lags 2–6. Evaluating **all four block widths** gives a maximum `0.0171031` SE (Penrose, block 80, channel 3-face, lag 6); square maximum is `0.0137648`. This does not alter the result, but the source-data value is authoritative.
- Stage 20 reuses Stage 19's saved samples, and Stage 18 extends the original Stage 9 chains. They are **not independent replicated physics campaigns**. The Stage 16 pilot had 32 outer backgrounds on a small square torus, not production Penrose spectral precision. Stage 17 package is a measurement continuation runner, not a new proof.
- The deterministic source summary audit is in `audit_saved_summaries.py`, with exact checks and archive checksums in `SUMMARY_CERTIFICATE.json`, and per-ZIP source/member indexing in `SOURCE_INDEX.csv`. No old experiments were rerun.

## 4. What is still missing for R3-IR

The classical-field or uninserted-partition ratio does not produce a *vacuum-connected* estimate of

`C_A(n) = ⟨Q AΩ,(T/λ0)^n Q AΩ⟩`

with `C_A(n) ≤ M_A exp(-m_phys n a_t)` and **common** `m_phys>0` independent of physical regulator, volume and admitted boundaries, plus an appropriately observing family of gauge-invariant sources in all relevant physical (including winding/center) sectors. A source-family frame alternative is uniform interacting observability `P_η S P_η ≥ c P_η` plus independent `||P_s S P_s||op ≤ C s^p`, or an independently derived complete source-inserted polymer-crossing bound.

**Neither a verified source-inserted exponential estimate nor a cutoff-uniform interacting frame is present in the examined historical records.** Positivity, source transfer identities, conditional estimator correctness, good short-time Monte Carlo signals, and finite-link Cauchy–Schwarz bounds are not substitutes.

## 5. Precise source to retrieve next, if it exists

If historical papers or archives outside the above source set contain a *proof*, prioritize the **source-inserted multiscale/transfer kernel or connected Euclidean crossing estimate**, with explicit Wilson insertion words, physical time normalization, all-scale constant bounds and nontrivial low-spin observability (or the associated spectral projector/frame estimates). Do **not** request duplicate Stage 19/20 ZIPs or repeat Stage 7–26 measurements. If no such document exists, the absence is a genuine mathematical R3-IR gate rather than an archival or data-processing omission.

## Files

Original archive SHA-256, ZIP member hashes and the computed saved-summary checks are in the accompanying audit bundle. Source originals are not modified and large binary data are not added to normal Git.