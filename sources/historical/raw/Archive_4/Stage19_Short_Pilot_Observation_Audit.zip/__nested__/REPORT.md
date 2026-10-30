# Stage 19 short scalar Monte Carlo pilot — observation audit

## Input and integrity

Source: `stage19_pilot_results.zip`, all eight `square/penrose × seed 101, 211, 307, 419` chains. Five contiguous 20-sweep segments per chain, 2 measurements per segment at sweeps 10010, 10020, ..., 10100. Total **80 gauge configurations** across eight chains (40 per geometry), with 20 timeslices and four scalar channels per observation. Latest-segment SHA256 verified against latest.json; geometry/catalogue/source hashes cross-checked within segments and metadata. All arrays finite. The independent control channels are unrestricted rooted 3/5/8-face averages; auxiliary is strictly shape-matched and normalized over accepted anchors. Square accepted 22801/22801; Penrose 22658/22808.

## Descriptive findings

Across the 40 configurations per geometry, the channel means (3-, 5-, 8-face control, auxiliary) are:

* Square: `[0.66129, 0.82678, 0.93164, 0.87346]`.
* Penrose: `[0.68937, 0.84905, 0.95034, 0.91375]`.

The timeslice-level correlations of auxiliary with the three controls are:

* Square: `[0.396, 0.499, 0.466]`.
* Penrose: `[0.364, 0.456, 0.310]`.

These correlations are not operator-state overlaps; they are same-ensemble, timeslice-value correlations and cannot establish superior glueball spectroscopy.

For exploratory connected correlators, subtract the mean over all configurations/timeslices in each geometry, and average products separated by periodic temporal shift. For exploratory SEs, bootstrap 2-configuration blocks within each chain (five blocks per chain, 1800 resamples), preserving the four original chains. This dataset supports **only a pilot noise screen**; five blocks per chain is insufficient for credible autocorrelation or long-block studies.

No channel achieves a positive signal-to-noise ratio greater than 2 at any of three consecutive separations in t=2..6. Across individual channels, t=2..6 SNR:

| Geometry | t | 3-face | 5-face | 8-face | Strict auxiliary |
|---|---:|---:|---:|---:|---:|
| Square | 2 | 0.36 | -0.98 | -0.18 | -0.03 |
| Square | 3 | 0.61 | 1.92 | 1.26 | 0.39 |
| Square | 4 | -0.59 | 0.97 | -1.35 | -0.78 |
| Square | 5 | 1.64 | 0.40 | -0.19 | -1.08 |
| Square | 6 | -2.13 | 0.26 | 0.33 | 1.87 |
| Penrose | 2 | 1.09 | 0.58 | 1.96 | 1.72 |
| Penrose | 3 | 1.82 | 0.25 | -1.53 | -1.17 |
| Penrose | 4 | -0.82 | -0.61 | -0.07 | 0.31 |
| Penrose | 5 | -1.84 | -1.08 | -1.32 | 0.59 |
| Penrose | 6 | -0.05 | -0.35 | 0.68 | 0.13 |

## Limitations and scientific gate

- This is 10 configurations per chain; temporal SNR estimates are noise-dominated and sensitive to unmeasured longer-range autocorrelation. Its statistical width does not support operator optimization, a positive state mass, plateau claim, or go/no-go extrapolation to a much longer pilot.
- These Stage 19 continuations may share the *same underlying Markov configurations* as Stage 17 and Stage 18 because all restarted from Stage 9 snapshots and RNG states. Do not naively combine these ensembles as independent.
- The matched auxiliary excludes 150 Penrose anchor locations and does not have exact Penrose fivefold symmetry. Keep masked and unrestricted channels separate; comparisons of their absolute means across geometries are not matched renormalized physics.
- The pilot contains no simultaneous original 9-/12-channel scalar measurements, so no direct covariance comparison against Stage 18 on identical configurations is possible from the uploaded files.
- No admissible m_0++, sigma, mass-to-tension ratio, or continuum physical effect follows from this pilot.

## Recommendation

No further extended run is justified *solely* by these 80 observations. Before a costly continuation, test a short multi-chain extension (e.g. 500 more sweeps per chain) if computational cost is modest and checkpoint integrity intact; then re-evaluate signal versus operator construction, autocorrelation and chain-to-chain stability. Alternatively prioritize physically optimized scalar-specific variance reduction. Retain Stage 19 checkpoints for a seamless continuation if selected.

## Reproducibility

`audit.py` reproduces `RESULTS.json` from the original uploaded `stage19_pilot_results.zip` at `/mnt/data/`; no simulation code or checkpoint state is modified.
