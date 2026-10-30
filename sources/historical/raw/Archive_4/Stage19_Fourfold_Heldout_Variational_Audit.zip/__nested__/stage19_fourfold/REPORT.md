# Stage 19 four-fold held-out scalar variational audit

## Data and provenance

Eight uploaded complete-auxiliary Stage 19 continuation ZIPs, four seeds 101, 211, 307, 419 per geometry. Each chain contains 490 saved gauge-configuration observations from sweeps 10,110 through 15,000. Every observation is `(20,4)`: unrestricted 3-, 5-, 8-face scalar controls plus the complete-coverage, strict target-matched auxiliary. All eight series passed continuity, shape, finiteness, same-catalogue and full-anchor metadata checks. Previous masked-auxiliary pilot samples were **not** pooled.

## Four-fold protocol

For each geometry and held-out seed, the other three entire chains train a **fixed three-dimensional linear projection** of the four channels. Two projections are compared:

- PCA: top three eigendirections of the training connected zero-lag channel covariance C(0).
- Truncated GEVP: whiten the same top three training C(0) eigendirections and diagonalize the symmetrized training C(1) within that subspace. Eigenvector signs are fixed deterministically.

The held-out chain has no influence on basis construction. Once the basis is frozen, held-out connected correlators use one held-out ensemble-wide vacuum mean and average over all 20 timeslices with periodic shifts. Within each held-out chain, circular moving-block bootstrap with block lengths 10, 20, 40, 80 (320 replicates each) estimates marginal uncertainties. A minimal **screening gate** is three consecutive positive correlators at least 2 SE above zero, starting at t=2,3,or 4. All tests are run on the held-out data without optimizing basis directions there.

## Result

**Zero** screening windows on *any* held-out seed, either geometry, either projection, at *any* tested block length. Therefore no correlated periodic-cosh or scalar-mass fit is admitted.

At block length 40, isolated maximum held-out SNR values among times t=2..6 are:

| Held-out seed | Square PCA | Square GEVP | Penrose PCA | Penrose GEVP |
|---|---:|---:|---:|---:|
| 101 | 2.74 | 1.74 | 1.35 | 1.77 |
| 211 | 2.21 | 1.77 | 0.97 | 1.60 |
| 307 | 1.73 | 2.98 | 1.59 | 1.96 |
| 419 | 1.70 | 1.59 | 0.51 | 0.87 |

Isolated peaks do not form positive multi-time decay signals, and some neighboring values are negative.

## Limitations

1. This is a **held-out positive-signal screen**, not a full constrained variational spectral analysis or a proof that no mass can be extracted by any alternative estimator. No multi-parameter cosh fit was attempted because the preregistered minimal signal gate failed.
2. Four seed chains per geometry provide only four independent Markov trajectories. Folds share training chains and are not independent tests for a combined p-value. Block lengths are sensitivity diagnostics, not an integrated-autocorrelation-time certificate.
3. Circular bootstrap and ensemble-square vacuum subtraction can have finite-sample bias in connected correlators, particularly for weak signals. The result motivates investigating variance of disconnected subtraction and scalar-specific multilevel methods.
4. Periodic Euclidean time is Nt=20; more complete fits need covariance shrinkage, reflection-symmetric correlators, and temporal-plateau/systematics analysis if new operators gain resolution.
5. The square and Penrose channels remain different finite-regulator observables; neither the mass nor renormalized scale, string tension or continuum mass-ratio difference follows from this analysis.

## Recommendation

Do not schedule additional overnight sampling with the identical four-channel estimator solely on this evidence. Next prototype should target scalar-specific variance reduction or independent-vacuum subtraction and test it on a short **held-out** ensemble with explicit effective-sample-size and cost-adjusted variance metrics before deciding on a full run.

## Reproduction

From a directory containing the eight Stage 19 ZIPs at `/mnt/data/{square,penrose}_seed{101,211,307,419}.zip`:

```bash
OPENBLAS_NUM_THREADS=1 python stage19_fourfold/analyze_fourfold.py
```

This regenerates `RESULTS.json` and `SUMMARY.json`. No gauge-field updates are performed.
