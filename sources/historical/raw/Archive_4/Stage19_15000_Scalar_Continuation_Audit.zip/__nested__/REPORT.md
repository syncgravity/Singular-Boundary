# Stage 19 complete-auxiliary scalar audit through sweep 15,000

## Provenance and integrity
Eight uploaded ZIP files (`square_seed{101,211,307,419}.zip`, `penrose_seed{101,211,307,419}.zip`) were independently opened. Each contains 245 contiguous 20-sweep observation files spanning 10,100–15,000, with two observations per segment (sweeps 10,110–15,000), totaling 490 scalar samples per chain and 3,920 overall. All arrays are finite with shape `(2,20,4)`. Array metadata, sweep indices, same-catalogue checks and `latest.json` endpoints agree. ZIP CRC checks pass. Penrose accepted/all anchor counts are 22,808/22,808; square 22,801/22,801. The original masked auxiliary was **not** combined with the new complete-coverage auxiliary.

## Analysis definition
We estimate the connected circular timeslice correlator C(t) = <O(τ) O(τ+t)> - <O>², pooled over configurations, all 20 timeslices and four chains within each geometry. This estimator uses a single ensemble vacuum subtraction and periodic temporal shifts. Standard errors use 500 circular moving-block resamples **within each chain**, separately for block lengths 10, 20, 40 and 80 saved configurations. This captures some serial dependence but is not an autocorrelation-convergence certificate or an optimized unbiased finite-sample estimator. We do not fit a mass unless positive later-time data persist over at least three consecutive times.

## Key observation
For 40-observation blocks, connected correlator SNR at t=2,3:

| Geometry | Operator | t=2 | t=3 |
|---|---|---:|---:|
| Square | 3-face control | 1.52 | -1.04 |
| Square | 5-face control | 1.20 | 0.98 |
| Square | 8-face control | 2.71 | 0.22 |
| Square | Complete auxiliary | 0.89 | 0.71 |
| Penrose | 3-face control | -0.37 | 0.33 |
| Penrose | 5-face control | -1.28 | 0.22 |
| Penrose | 8-face control | 0.12 | 0.10 |
| Penrose | Complete auxiliary | 0.34 | 0.71 |

No individual channel in either geometry has a three-consecutive-point positive 2σ window in t=2..6 for any block length examined. Square eight-face at t=2 is the only individual above 2σ in these times across block lengths. The auxiliary-timeslice correlation with the 3-,5-,8-face controls is [0.454,0.517,0.479] on square and [0.330,0.439,0.296] on Penrose; these are **not** ground-state overlaps.

## Interpretation / recommended next step
The complete-coverage auxiliary passes the sampled observation data integrity and is not near-identical to the three controls, but does not supply demonstrable late-time scalar resolution. No physical 0++ mass can be quoted. Repeating another long MCMC campaign with identical four channels is not justified yet. Next test four-chain held-out low-rank or generalized-eigenvalue combinations, with training-only operator selection, and audit disconnected vacuum-subtraction variance and independent block-length convergence. If that also fails, change the measurement strategy (scalar multilevel estimator, better vacuum noise control, physically larger/smeared loops) and pilot before more production sweeps.

## Limitations
- The primary checks are file CRC and metadata plus mathematical consistency of segment data; there is no external independent gauge-field replay.
- Four independent seed sequences descend from Stage 9; Stage 17/18 continuations are *not additional independent gauge chains*.
- This is not a finite-volume, renormalized scale, or continuum-limit analysis.
- Across-geometry numerical scalar-operator mean differences are **not** mass differences.
