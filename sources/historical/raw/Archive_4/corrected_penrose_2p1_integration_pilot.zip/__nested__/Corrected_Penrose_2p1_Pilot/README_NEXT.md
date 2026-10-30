# Corrected cut-and-project Penrose × interacting SU(2) 2+1D: integration pilot

**Status:** Executed software/observable-validation pilot, **not** a physical continuum-gap measurement.

## Contents

- `corrected_2p1_pilot.py` — newly written, standalone corrected-geometry open-patch 2+1D SU(2) Wilson sampler and gauge-invariant observable measurements. It **never calls** the superseded Phase II Penrose graph generator. It imports the quaternion arithmetic and plaquette holonomy calculation from the older engine, but **not** its periodic Penrose geometry.
- `direct_cut_project.py` — unmodified verified window-first model-set generator from the supplied `Phase_III_Cut_and_Project_Recomputed.zip`.
- `wilson_torus.py`, `penrose_causal_study.py` — unmodified source modules from the supplied `penrose_yang_mills_2p1_causal_study.zip`, imported for SU(2) quaternion multiplication and Wilson-loop holonomy only. Their older periodic approximant generator is **not called** in this study.
- `test_corrected_2p1_pilot.py` — six independent validation tests (gauge invariance, geometry and plaquette closure, 1-edge loop=temporal plaquette, locally computed Metropolis action change including open boundaries, identity links, and sampler smoke test).
- `outputs/` — radius-3.5 pilot: 50 vertices, 84 edges, 35 rhombi.
- `outputs_R5/` — radius-5 pilot: 90 vertices, 159 edges, 70 rhombi (matching one radius of the validated Phase III geometry).
- `INTEGRATION_REPORT.md` — actual results, interpretation, and next experimental requirements.
- `SOURCE_SHA256.json` — SHA-256 manifest for archived source copies.

## Requirements

Python >= 3.10, `numpy`, `scipy`, and `numba` (NumPy 2.x was used for the included runs). No GPU or external service. Run with a single BLAS thread if desired.

## Commands

```bash
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1
python -m unittest -v test_corrected_2p1_pilot
python corrected_2p1_pilot.py --pilot --radius 3.5 --nt 8 --beta 2 --outdir outputs_reproduced
python corrected_2p1_pilot.py --pilot --radius 5.0 --nt 8 --beta 2 --outdir outputs_R5_reproduced
```

These commands regenerate the small pilot datasets from the recorded seeds. The scripts are intentionally limited to pilot-length chains unless parameters are supplied explicitly. Use `--offset` to select a separate validated phason offset.

## Wilson action and boundary conditions

The spatial complex is the actual open finite cut-and-project rhombic patch, with **periodic time** only. All links are dynamical SU(2) quaternions; the action is

\[
S=\beta\sum_{p\in\text{spatial and temporal plaquettes}}\left[1-\tfrac12\operatorname{ReTr} U_p\right].
\]

Uniform plaquette `beta` is adopted solely as a gauge-invariant computational baseline. It is **not** a validated discrete Hodge operator for nonorthogonal rhombi and is **not** guaranteed to approach the correct isotropic continuum Yang–Mills action. Spatial boundary links participate in three plaquettes (one spatial face and two time plaquettes); interior spatial links participate in four. The previous toroidal engine's requirement of exactly four cannot be used for the open patch.

## Observables and statistical limitations

A time-slice scalar-basis array comprises (1) means over thin-rhombus traces, (2) means over thick-rhombus traces and (3) means over the boundary traces of neighboring two-rhombus clusters. Their connected matrix is computed after ensemble averaging by the proper vacuum-subtraction formula. A nonoverlapping, exploratory block bootstrap gives errors and a **flattened covariance matrix**, not a production covariance estimate.

Spatial Wilson paths are shortest paths restricted to interior edges, grouped by their number of edges (one, two, or three); every path records the **actual Euclidean end-to-end separation**. Temporal Wilson rectangles are measured at lags 1, 2, and 3 and averaged over time. `pilot_configs.npz` contains all saved full 3D SU(2) gauge-link arrays, so alternative operators can be measured without rerunning the short chains.

Each pilot has only **two chains**, 24 burn-in sweeps and 48 measurement sweeps at thinning 4, resulting in 12 saved configurations per chain (24 total). Neither stationary mixing nor the physical finite-volume/continuum limits are established. The bootstrap assumes a short block length only for software diagnostics. No glueball mass, string tension, or continuum ratio is fitted.

## Critical research separation

The earlier geometric-weight 2+1D periodic Penrose results remain valuable finite-regulator evidence for a coupling-distribution confound, but their specific geometry and boundary conditions are **not** silently substituted for the corrected model-set reference. The next physically decisive step requires a fully verified **periodic cut-and-project/inflation approximant**, an appropriate area/anisotropy gauge action, matched renormalized scales, much higher-signal 0++ correlators, multi-distance large-time potentials, and at least four continuum lattice spacings at controlled volumes. The new pilot is only a validated staging point for those tasks.
