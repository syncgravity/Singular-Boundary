# Stage 18 scalar continuation: first 12,000-sweep audit

## Inputs and integrity
Eight archives `square_scalar_seed{101,211,307,419}.zip` and `penrose_scalar_seed{101,211,307,419}.zip`. Each archive has 20 contiguous 100-sweep segments, from 10,000 to 12,000, each with 10 measurements at 10-sweep intervals. Each chain contributes 200 configurations at sweeps 10,010 through 12,000. Total 1,600 configurations (800 per geometry). Each timeslice-resolved scalar observation has shape `(20,12)` and APE levels `(0,2,6,12)`. All latest-record final segment SHA-256s match and reported plaquette cache discrepancies are zero. Source geometries and seeds verified from stored arrays.

## Method
For each geometry and operator O, compute ensemble/timeslice centered `O - mean(O)` and periodic connected correlator `C(t)=mean_{configuration,time} [(O(time)-mean(O))(O(time+t)-mean(O))]`. Use chain-preserving, equal-sized nonoverlapping blocks of 5,10,20,40 configurations, bootstrap 400 resamples per block size, drawing within each of the four chains independently; compute the full-sample mean again per bootstrap replicate. Interpret SNR at block 20 as exploratory. The 12 channels correspond to three spatial operator types at each APE-smearing level, in input order.

## Results
At block length 20, none of the 12 individual channels on either geometry has a positive connected correlator exceeding twice its bootstrap standard error at any of t=2,3,4,5,6. Therefore no individual operator exhibits three consecutive resolved positive time points; no 0++ mass is admitted. Maximum across individual channels of C(t)/SE for t=2..6:

| t | Square | Penrose |
|---|---:|---:|
| 2 | 0.92 | 1.72 |
| 3 | 1.93 | 0.82 |
| 4 | 0.21 | 0.86 |
| 5 | -1.05 | 0.34 |
| 6 | -0.38 | 0.77 |

The APE level-12 channels have substantial timeslice-value correlation with level-6 channels; largest absolute Pearson correlation with any of the three level-6 channels is approximately 0.888–0.905 (square) and 0.879–0.894 (Penrose). Thus smearing to level 12 has not yet supplied clearly distinct measured directions; these correlations alone do not rule out improved optimal linear combinations.

These 200 measurements per chain are not statistically independent. Existing Stage 9 chains contain 900 saved scalar configurations per chain, albeit without the added 12-level channels; Stage 18 resumes the same original states/RNG streams and is not an independent physical ensemble of Stage 17. The sample ratio 800 new per geometry versus 3,600 original per geometry should be considered before interpreting any apparent gain or loss of signal. The preliminary individual-channel criterion is not a full cross-validated variational analysis. A negative or weak connected estimate is not proof of a zero physical mass gap.

## Next decisions
Do **not** admit a glueball mass from these outputs. Perform held-out training/validation of a low-rank 12-channel scalar combination, using the full covariance including cross-channel components and chain-preserving block uncertainty, with diagnostics of nonstationarity. If no positive multiple-time signal remains, consider higher-overlap scalar operators and a scalar-specific multilevel or noise-reduction measurement strategy; merely increasing smearing is not demonstrated to solve this problem. Do not conflate this with the Wilson-loop static-potential results or a continuum mass comparison.

## Reproduction
Run `python analyze.py` in a folder containing the eight ZIP files at `/mnt/data` (or adjust those paths), with NumPy. `RESULTS.json` includes per-chain continuity, central values, bootstrap uncertainties and leave-one-chain-out connected correlators. `compare.py` provides an optional comparison with full Stage 9 checkpoint scalar observations.
