# Stage 15 — batched temporal transporter benchmark (exploratory)

## Purpose and decision

Implemented common-inner-trajectory measurements of *three straight spatial Wilson paths* at physical separations 1, 2, and 3 in the 5×5 square reference (Nt=15, beta_ref=3.5). The temporal rectangle spans 10 lattice slices with distinct boundaries. Reuses the same frozen-boundary conditional Monte Carlo trajectory for all three paths, holding the Wilson action and SU(2) Metropolis update unchanged. Tests inner depths 8, 16, 32 as nested prefixes of the same trajectory.

**Decision: no production multilevel speedup certified, and no string tension or mass extracted.** In this screening, the conditional estimator has lower raw across-background SD, but larger `variance × elapsed measurement time` than direct measurement on already generated outer fields. Insufficient outer thermalization, conditional mixing diagnostics, covariance-resolved Wilson signals and fitting controls prevent physical admission.

## Design

- Four independent seeds: 101, 211, 307, 419; six outer gauge fields per seed; burn=200, thin=12. This is a short, noncertified equilibration pilot, **not** the Stage 9 large production ensemble.
- Square Nx=Ny=5, Nt=15, periodic, coupling beta_ref=3.5. Paths are straight oriented x displacement r=1, 2, 3 spatial units (no winding).
- Frozen spatial links at slab boundaries t=0,5,10. Two conditional slabs each contain five temporal links. Inner warm=32 allowed-link sweeps, two allowed-link sweeps between measurements. Frozen links never updated.
- Color-retaining paired SU(2) temporal transporter matrices are averaged in each slab, contracted with frozen spatial endpoint holonomies. Three paths share all gauge update sweeps and the depth 8/16/32 prefix samples.
- Direct estimator is one Wilson rectangle evaluated at the same saved outer gauge configuration. Timings exclude outer ensemble generation and are benchmark-dependent. Since the conditional estimator and direct estimator sample different conditional distributions at finite inner warm and inner depth, mean differences are *not* bias-certified by agreement of naive standard errors.

## Measured screening numbers

Per-path raw SD reduction (direct SD / conditional SD) and cost-normalized variance-time ratio (`Var[conditional]·time_conditional / (Var[direct]·time_direct)`, smaller than one would be better). The conditional measurement time was shared across **all three paths**; it is deliberately charged in full in each individual path's pessimistic standalone efficiency statistic.

| Physical r | Raw SD ratio depth 8 | depth 16 | depth 32 | variance-time ratio depth 32 |
|--:|--:|--:|--:|--:|
| 1 | 2.95 | 6.24 | 13.01 | 1.69 |
| 2 | 2.88 | 4.94 | 8.21 | 4.25 |
| 3 | 4.95 | 6.83 | 10.80 | 2.45 |

Direct means are 0.1126, -0.0834, -0.0453 for r=1,2,3 respectively, while conditional depth-32 means are 0.0114, -0.00119, -0.00635. These mismatches are **not evidence of physical differences**. The raw pilot includes outer backgrounds with no certified equilibrium and a conditional inner chain with no convergence certification. In particular the near-zero conditional means are a warning against assuming raw-SD reduction equals improved estimator quality. No Wilson potential plateau is fitted.

## Validation and limitations

Four Stage 15 tests passed: path contiguity, exact SU(2) identity-field rectangle, frozen-boundary/cache validation, and bitwise-equivalent numerical result to the legacy single-path conditional estimator under identical seed and conditional sweeps. The last check is algebraic/implementation equivalence, not physical correctness of an insufficiently equilibrated estimator.

The benchmark's naive across-background standard deviations ignore any long-tail outer autocorrelations. We did not establish conditional inner mixing, independence or total-cost superiority (including outer gauge update cost). No paired confidence intervals derived from sufficiently independent gauge configurations have been certified. This stage does not remeasure the full 22,808-vertex M55 torus; doing so is not warranted by the present screening. Nonperturbative anisotropy and scale matching, finite-volume corrections and multiple cutoffs remain open.

## Next scientifically productive optimization

Use fixed-boundary two-link or multihit integration and substantially longer conditional mixing diagnostics, with a budget-matched number of independent outer fields. Exploit transporter sharing across *many* matched long-distance paths and temporal extents before returning to M55. Use the previously archived Stage 9 ensemble to independently validate direct signals. Require stationary inner estimates across doubling depths, paired blocked confidence intervals, and improvements in total cost × squared uncertainty for the **same** physically matched target observable. Only then attempt stable positive multi-time potentials and string tension.

## Reproduce

`OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -m unittest -q test_stage15` and `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python stage15_batch.py` from `ym_stage15` after extraction of the companion `ym_stage13` dependencies. Output is `BENCHMARK.json`, including all 24 paired per-background measurements and timings.
