# Stage 12 — Reconstructed physical-distance Wilson-loop audit

## Inputs and reproduction

- Eight uploaded Stage 9 final `*_nt20_seed*.npz` files (four seeds 101, 211, 307, 419 in each geometry), each providing an `observables_wilson` array of shape `(900,3,100,10)`. Stage 9 nominal burn cut and statistical diagnostics were reported in the separate admission audit.
- Unmodified Stage 7/9 code `stage7_large_torus.py` and `stage7_measurement.py`. Reconstructed `pair()` and `sparse_paths(sp, n_anchors=80, max_steps=5, per_length=20)` in the original measurement path order. For each geometry, **100 paths, and the exact set of unique physical radii match the archived `*_measurement_plan.json` to seven decimals**. Per-path metadata includes the signed edge-vector displacement, endpoints, and spatial link sequence. This is a deterministic code/summary consistency check, not a separate cryptographic link to the original measurement run.
- Analyzed the 2-sweep APE data, index 1. The rectangles are `W(t)` for temporal t=1..10, in the simulation's temporal lattice units. Quantities `-log(W(t+1)/W(t))` below are in lattice-time units, **not continuum-renormalized physical potentials**.
- For each physical radial interval, averaged the corresponding paths per saved configuration, then averaged independent within-chain blocks of 20 consecutive saved configurations (200 sweeps). Five hundred chain-stratified block bootstrap resamples yielded exploratory standard errors; blocks were resampled separately within each of four chains to preserve local autocorrelations. This neither tests alternative block sizes nor accounts for path-selection, smearing, anisotropy, or matching systematics.

## Selected measurements

| Geometry | Bin r | Number of paths | Mean actual r | W(t=4) SNR | W(t=6) SNR | W(t=8) SNR | Veff(3→4) ± bootstrap SE | Veff(4→5) ± bootstrap SE |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| Square | [0.5,0.9) | 30 | 0.649 | 381.2 | 173.7 | 82.7 | 0.383 ± 0.001 | 0.380 ± 0.002 |
| Penrose M55 | [0.5,0.9) | 23 | 0.647 | 253.9 | 93.8 | 42.0 | 0.469 ± 0.002 | 0.462 ± 0.003 |
| Square | [1.2,1.5) | 13 | 1.275 | 79.6 | 18.3 | 6.2 | 0.723 ± 0.008 | 0.723 ± 0.017 |
| Penrose M55 | [1.2,1.5) | 18 | 1.279 | 43.6 | 6.9 | 1.6 | 0.911 ± 0.018 | 0.938 ± 0.044 |
| Square | [1.5,1.8) | 12 | 1.670 | 44.1 | 7.0 | 1.6 | 0.884 ± 0.017 | 0.853 ± 0.044 |
| Penrose M55 | [1.5,1.8) | 13 | 1.638 | 16.8 | 2.2 | 1.7 | 1.163 ± 0.050 | 1.290 ± 0.175 |
| Square | [1.8,2.1) | 18 | 1.915 | 32.9 | 6.3 | 2.1 | 1.015 ± 0.024 | 1.018 ± 0.072 |
| Penrose M55 | [1.8,2.1) | 13 | 1.942 | 9.4 | 0.5 | ≈0 | 1.216 ± 0.096 | 1.245 ± 0.414 |
| Square | [2.1,2.4) | 13 | 2.324 | 18.7 | 1.6 | 0.1 | 1.047 ± 0.046 | 1.352 ± 0.210 |
| Penrose M55 | [2.1,2.4) | 12 | 2.263 | 3.3 | 0.8 | 0.1 | 1.709 ± 0.327 | 0.413 ± 0.523 |

All reported figures are exploratory Monte Carlo sample estimates; error bars do not include nonperturbative physical matching or full covariance fit-window systematics. Some later effective energy estimators become undefined or misleading because Wilson means approach zero and bootstrap draws change sign.

## Assessment

1. **Path-distance reconstruction succeeded:** archived paths are grouped by actual physical displacement, not spatial link count. The selected physical bins overlap on square and Penrose; e.g. mean 1.275 vs 1.279 in [1.2,1.5).
2. **Short-time Wilson energies have measurable signals** for square and some Penrose bins. However, robust positive long-time plateaus at sufficiently large *physical r* do not survive the signal reduction. At Penrose r≈1.94, W(t=6) is ~0.5 standard errors. Larger radii are worse.
3. **An apparent difference in effective energies is not a Penrose-specific continuum effect.** The geometries differ in orientation and path shape, the nonperturbative renormalized coupling and anisotropy remain unmatched, and we have only one bare beta, one large volume, one model-set phase, and one lattice cutoff.
4. **No admitted string tension.** The radial slopes of short-time Veff are excited-state and path-shape contaminated. They are not sufficient for fitting sigma, and longer-time lattice data have inadequate signal in the large-r bins.
5. **No admitted glueball mass** based on the separate Stage 10–11 scalar analysis. Consequently R and continuum Delta R remain undefined.

## Recommended next computation

Prioritize temporal-slab multilevel Wilson-line transporters at **fixed physical separation** (not merely time-separated smeared spatial loops); calibrate the conditional expectation method on square torus first. For Penrose select distance-and-orientation-matched path sets, increase the number of spatial anchors and path shapes per bin, and estimate full block-bootstrap covariance. Validate adequate time plateaus (at least three consecutive time separations), stability under smearing and path selection, then fit spatial slope with finite-string and volume corrections. Independently establish torelon correlators and nonperturbative anisotropy. Only then quote sigma. The scalar sector requires improved vacuum-subtracted and well-conditioned variational operators, potentially more sophisticated multilevel treatment.

## Data files

- `STAGE12_PHYSICAL_WILSON_AUDIT.json`: all physical bins and bootstrap results.
- `STAGE12_{square,penrose}_paths.npz`: exact reconstructed physical radii/displacements and path order.
- `stage12_analyze.py`: end-to-end measurement and chain-stratified block-bootstrap code, requires original checkpoint NPZ files.
