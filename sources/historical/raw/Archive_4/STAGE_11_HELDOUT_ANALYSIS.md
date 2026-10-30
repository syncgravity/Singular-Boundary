# Stage 11: Held-out scalar-basis validation and Wilson time-signal audit

## Inputs and controls

All eight user-uploaded final Stage 9 checkpoints, 4 seeds/geometry, 900 stored measurement draws/seed, 20 Euclidean time slices. No new Monte Carlo sweeps. Stage 10 audit and unchanged Stage 9 estimator definitions. Analysis source: `stage11_analyze.py`; machine-readable numbers: `STAGE_11_DIAGNOSTICS.json`.

Three chains (seeds 101, 211, 307) are **training only** for selecting the scalar channel with the highest positive ratio of diagonal connected `C(1)/C(0)`; seed 419 is held out. A second training-only channel uses the leading `C(0)` eigenvector. Means are removed at ensemble level, never per configuration. Results use a descriptive standard error across non-overlapping blocks of 20 saved configurations. This is **not** a proof of equilibrium, a bootstrap-stable fit or full cross-validated spectroscopy. Temporal times t=1..5 are reported in lattice time-slice units, not physical mass units.

## Scalar signal, held-out seed 419

| Geometry | Train-selected scalar channel | Held-out t=1 SNR | t=2 SNR | t=3 SNR | t=4 SNR | t=5 SNR |
|---|---:|---:|---:|---:|---:|---:|
| Square | operator 5 | 13.27 | 1.61 | 0.64 | 0.50 | 1.12 |
| Penrose M55 | operator 5 | 5.47 | -1.01 | 1.98 | 0.67 | -0.93 |

The leading C(0) eigenvector of each geometry, also trained only on three chains, fares no better: held-out t=2..5 SNR are square 2.30, 0.27, 0.58, 0.91 and Penrose -0.59, -0.80, 1.18, 1.01. The top-three C(0) directions were additionally screened for held-out C(1) definiteness; see machine-readable JSON. The full nine-operator GEVP reference remains inadmissible, and neither reduced channel has the three or more resolved later times needed for a scalar mass.

## Wilson-loop signal

Existing checkpoint `observables_wilson` has shape (900 configurations, 3 APE levels, 100 paths, 10 time separations). The original Stage 7 `sparse_paths` implementation enumerates 20 paths at each edge count from 1 to 5. This checkpoint analysis averages the 20 paths within each path-*length* group at APE level 2. Those path groups **are not physical-distance bins** and cannot be used for a static-potential slope or a geometry comparison until the exact physical path metadata are joined and matching by distance/orientation/path shape is done. Block-20 standard error, 180 blocks per geometry; no autocorrelation-length sensitivity study.

| Geometry | Spatial edges | t=4 SNR | t=8 SNR |
|---|---:|---:|---:|
| Square | 1 | 397.1 | 81.7 |
| Square | 2 | 159.9 | 18.2 |
| Square | 3 | 82.3 | 6.2 |
| Square | 4 | 41.5 | 2.0 |
| Square | 5 | 16.3 | 0.7 |
| Penrose M55 | 1 | 238.9 | 43.0 |
| Penrose M55 | 2 | 70.8 | 4.0 |
| Penrose M55 | 3 | 24.4 | 0.4 |
| Penrose M55 | 4 | 8.9 | 1.5 |
| Penrose M55 | 5 | 1.7 | -0.5 |

Even where Wilson loops are individually detected, this does not demonstrate a time-independent static potential or string tension. The long-range Penrose signal is especially weak; a valid fitting analysis needs true distances, within-group variability, orientational control, joint block-bootstrap covariance, t_min/t_max variation, and nonperturbative physical matching. Avoid averaging significantly different paths before constructing a potential.

## Decisions

- Independent train/hold-out scalar reduction tested: **no admitted scalar mass**.
- Wilson correlator precision screened across spatial path lengths and time: **positive short-time signals, no admitted potential or string tension**.
- Flux correlators in JSON: no admitted three-time torelon plateau.
- Overall `m_0pp`, `sigma`, `m_0pp/sqrt(sigma)`, and continuum effect: **null**.

Next: reconstruct or upload exact per-path geometry metadata; calculate individual-path and physical-distance/orientation-resolved Wilson correlators with blocked cross-time covariance; validate plateau and r-dependence on held-out seeds. If those fail, allocate computational effort to temporal-slab multilevel estimators or better operators, not undirected extra sweeps.
