# Stage 19: extended closed-loop scalar operator pilot

**Scope**: deterministic read-only engineering validation on the saved Stage 9 final fields; not a mass measurement.

- Adds spatial connected-face clusters of sizes **3, 5, 8** to the existing single-face/two-face/four-face scalar basis. Samples **96 distinct clusters per size** from each geometry, using seed 19.
- Every cluster is transformed into an explicitly ordered, closed gauge-invariant boundary. Rejects invalid/self-disconnected perimeters.
- Each operator averages `1 - trace(W)` over 96 cluster paths at each of 20 timeslices. These averages are **equal-weight over the selected loops**; they are NOT area-matched or physically renormalized across the two geometries. The supplied `areas` array permits later area-reweighted analyses.
- A random local SU(2) gauge transformation was applied on a full spatial timeslice to test 12+ of the traces, with worst differences `3.61e-16` (square) and `6.66e-16` (Penrose).
- Tested on Stage 9 seed 101 final fields at sweep 10,000, **one configuration per geometry only**; no temporal correlator estimate, signal-to-noise improvement, scalar mass, or string tension is inferred.
- The first priority after this engineering pilot is checking the operators' **geometry/area distribution and low-momentum scalar projection**, then testing statistically whether they add signal beyond APE-6/12. A scalar-specific estimator requires separate conditional-unbiasedness and computational cost tests. Do **not** treat the source-line Wilson multihit as a validated scalar estimator.

## Run

Requires Python with numpy, scipy, and numba. From this directory, with eight Stage 9 checkpoint `.npz` files in `<CHECKPOINT_DIR>`:

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 NUMBA_NUM_THREADS=1 python -m unittest -q test_stage19
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 NUMBA_NUM_THREADS=1 python stage19_pilot.py --kind square --seed 101 --inputs <CHECKPOINT_DIR> --output stage19_results
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 NUMBA_NUM_THREADS=1 python stage19_pilot.py --kind penrose --seed 101 --inputs <CHECKPOINT_DIR> --output stage19_results
```

Outputs for each geometry: `*_stage19_pilot.npz` with `obs` shape (20,3), path lengths, loop areas, and group indices; `*_validation.json` with the geometry hash, counts and gauge-test residual. Inputs are opened read-only, the Stage 17 and Stage 18 continuation data are unaffected.

**Important**: The 96 clusters are sampled spatial locations rather than full-volume sums, so this is a *pilot observable*, not yet a properly constructed full zero-momentum operator. Geometry-aware physical area matching and full spatial integration must be implemented and tested before a production spectroscopy run.
