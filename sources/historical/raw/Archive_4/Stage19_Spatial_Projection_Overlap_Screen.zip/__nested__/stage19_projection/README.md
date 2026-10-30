# Stage 19 — pre-production geometry and operator-overlap screen

## Data and scope
Read-only Stage 9 last saved gauge fields at sweep 10,000 for seeds 101, 211, 307, 419 on square151 and rational-model-set Penrose M55; original Stage 9 scalar time-series data from these checkpoints. This is an **engineering screen** and does not constitute new Monte Carlo statistics, an improved scalar correlator, or a mass measurement.

## Spatial projection and geometry audit
The new face-connected Wilson-loop operators have three families of cluster sizes 3, 5, 8. On each geometry an identical deterministic catalogue of 384 spatially sampled closed boundaries per family was applied to four final gauge snapshots. The sample was evaluated using nested initial subsets of 96, 192, and 384 loops per family. Individual loops are exactly gauge invariant from the previous pilot; the operator is a spatial average but **not yet an exact zero-momentum projection over all spatial translations/locations**, because a random cluster-growth process supplies only 384 representatives per family, the Penrose regulator is aperiodic, and subsets may not be representative. An exact or quantitatively controlled site/face-wide spatial projection must precede production.

Penrose loop enclosed-area coefficients of variation (384 loops): 3-face 0.0877, 5-face 0.0609, 8-face 0.0454; corresponding square values are effectively zero by uniform face area. Thus equal face-count families are not exactly equal physical area across geometries. Spatial binning by *measured area* and orientation, not face count alone, must be part of the follow-up geometry-controlled catalogue.

RMS difference between spatial averages with 96 versus 384 selected clusters (averaged over 4 gauge snapshots and 20 timeslices) ranges 0.0378–0.0427 for square, and 0.0407–0.0449 for Penrose. For 192 versus 384, square 0.0219–0.0288, Penrose 0.0224–0.0261. The nested subsets are correlated, so these values are sensitivity metrics, **not Monte Carlo standard errors** or convergence proofs.

## Legacy operator redundancy check
The legacy Stage 9 checkpoint contains the 9 scalar channel timeslice series for the final gauge field at exactly sweep 10,000. The new 384-loop-family averages at the same sweep were centered within each snapshot across 20 timeslices, then compared with each of the 9 legacy channels. Across four snapshots per geometry, maximum absolute correlation of each new family with any legacy channel:

- Square: **0.106, 0.201, 0.127** for 3, 5, 8 faces.
- Penrose: **0.281, 0.211, 0.207**.

These are descriptive same-configuration operator correlations; temporal slices of a field are not independent chain configurations. Low correlations suggest nonduplication of existing local observables but **do not imply larger overlap with the lightest 0++ eigenstate**. That physical question requires correlator matrices formed across many newly measured gauge configurations. In particular, the Stage 18 scalar archives cannot recover measurements of new Stage 19 loops retroactively because they do not contain intermediate gauge-link fields.

## Decision
(1) Geometry-aware construction and spatial sensitivity test: **pilot completed, full-volume zero-momentum and geometry-binned physical-area projection remains required**. (2) Same-field overlap/redundancy with Stage 9 operators: **descriptive pilot completed, actual connected *temporal* operator-overlap test still blocked by missing new-loop time series**. Do not start a new 24-hour Monte Carlo run based on this evidence alone. Next implement a deterministic full-coverage or validated stratified spatial projection, with physical-area/orientation bins and manageable path-count/runtime; then short independent-chain scalar pilot on *new* fields.

## Reproduce
With NumPy/SciPy/Numba and the adjacent Stage 19 pilot vendor code installed in `/mnt/data/stage19_operator_pilot`, run:

```
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 NUMBA_NUM_THREADS=1 python run_projection.py --inputs /mnt/data --seeds 101 211 307 419 --loops 384 --steps 96 192 384
OPENBLAS_NUM_THREADS=1 python overlap.py
```

The results directory contains two compressed `.npz` pilot arrays, two JSON spatial diagnostics and two cross-channel overlap JSONs. File inputs are read-only.
