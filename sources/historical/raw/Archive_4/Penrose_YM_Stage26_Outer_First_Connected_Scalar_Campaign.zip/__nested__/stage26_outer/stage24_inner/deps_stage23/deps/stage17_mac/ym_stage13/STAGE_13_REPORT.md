# Stage 13: temporal transporter multilevel validation (exploratory)

## Purpose
Stage 12 reconstructed actual Wilson-path separations on the large M55 rational periodic model-set and equal-area square lattice. Stage 12 did **not** establish a late-time potential plateau or string tension. Stage 13 implements the color-tensor factorization needed for temporal-line variance reduction. This checkpoint is a *software and tiny-lattice feasibility test*, not a production measurement.

## Construction
Represent SU(2) spatial path holonomies at times `0` and `10` by `S0`, `S10`. For source `u` and destination `v`, the temporal Wilson lines across a five-slice slab are `A_s`, `B_s`. The transporter tensor is `P_s = B_s ⊗ conj(A_s)`; multiplication `P_0 @ P_1` retains correct color ordering. Contract with `S0` and `S10` to reproduce `0.5 Re Tr(S0 B0 B1 S10† A1† A0†)` exactly. The slab's fixed spatial boundary links are not changed by the conditional Metropolis updates. Independent conditional slab distributions factorize given the fixed boundary links. Finite inner warmup and sampling can bias practical estimators; a joint inner-chain convergence and outer-sample analysis is necessary.

The validation field uses a 5×5 spatial square torus with `Nt=15`, temporal slab width 5, an ordinary Wilson rectangle of time length 10 (not a time-wrapping Polyakov observable). The implementation is generic in spatial path and two endpoints; a separate **algebra and factorization** test passed on the M5 rational model-set geometry, which is not a geometrically admitted Penrose comparison.

## Test results
Five new tests pass: identity-link Wilson normalization, exact direct/tensor reconstruction on random gauge fields, slab incidence factorization, frozen-boundary/cache integrity after genuine conditional updates, and exact reconstruction plus factorization on the rational model set. Tests do **not** establish equilibrium or continuum-scale matching.

## Pilot observations
The bounded 5×5×15 interacting SU(2) square pilot contains just 16 outer states from **one** Metropolis chain, using 16 inner measurements after 16 conditional warmup sweeps, separated by two inner sweeps. From `PILOT.json`:

- Direct raw Wilson-loop mean 0.00510; conditional tensor-contraction mean -0.00834.
- Direct across-outer standard deviation 0.46162; conditional standard deviation 0.11147; descriptive SD ratio 4.14.
- Paired mean difference is negligible compared to its large uncertainty; **this is not proof of unbiasedness**.
- Frozen-boundary checks pass and maximum plaquette-cache residual is 0.

The SD comparison **does not account for CPU cost, autocorrelation, or independent outer-chain uncertainty**. The direct and conditional measurements have different computational costs and none of these means are precise. It is not appropriate to claim a fourfold *effective* precision improvement.

## Admission gate for larger matched samples
1. Reconstruct the same fixed-r, orientation-class source/destination paths from Stage 12, and verify every spatial edge, physical displacement, winding class, and temporal seam.
2. On the square reference, use at least four independent **stationary** outer chains and test multiple inner depths (e.g. 16, 64, 256) and separate conditional warmups. Compare conditional versus direct results **with paired uncertainty intervals**.
3. Bootstrap outer-chain blocks; never treat nested inner samples as new independent outer configurations. Report variance multiplied by wall-clock cost and chain autocorrelation. Require reproducible cost-adjusted improvements across at least two independent path families and multiple temporal separations.
4. For genuine potential plateaus use `Nt=20` with at least three 5-slice slabs, measuring `T=5,10,15` on consistent source paths (or redesign width for finer time increments). Explicitly separate Wilson rectangles from temporal winding observables.
5. Transfer only after checks to M55 and orientation-matched paths; maintain a geometrical-admission ledger. Equal physical area and tree-level isotropy do not supply nonperturbative anisotropy or renormalized-scale matching.
6. Fit `V(r,T)` against time with correlated uncertainties and test multiple fit windows, then test large-distance slopes and string corrections. Require scale-setting independent of the bare action; repeat at several couplings, physical volumes, and independently vetted approximants before continuum extrapolation.

## Scientifically defensible decision
Only exact transporter algebra and the small conditional-sampling **feasibility** are demonstrated. No square or Penrose physical string tension, scalar mass, mass ratio, physical matching, or continuum difference is admitted. The existing 7,200 Stage 9 observations remain independent *outer-ensemble references*; they have not been replaced or reprocessed as new inner samples.
