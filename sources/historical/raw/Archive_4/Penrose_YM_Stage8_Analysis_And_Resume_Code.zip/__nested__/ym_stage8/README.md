# Stage 8 — checkpointed independent-chain continuation (2+1D SU(2))

This is an **incomplete production campaign**, not a result for a glueball mass, string tension, or continuum ratio. The large M=55 rational model-set / 151x151 square geometries and Wilson dynamics are inherited unchanged from Stage 7. The old de Bruijn graph generator is not used.

## Confirmed environment

Python >=3.10 with `numpy`, `numba`, `scipy`, and `arviz` for future post-burn statistical diagnostics. Use single-threaded BLAS: `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 NUMBA_NUM_THREADS=1`.

## Source and saved checkpoints

`checkpoints/<geometry>_nt20_seed<seed>.npz` includes the entire last SU(2) configuration, plaquette cache, RNG state, lockfile parameters, sweep count, all individual measurement time series if/when any exist, and the complete warm-up plaquette history. `*_progress.json` is written alongside each NPZ and hashes the latter. Four distinct hashed PRNG seeds (101, 211, 307, 419) are used for each geometry. **These are not four equilibrium chains yet.**

`stage8_campaign.py` iterates over the eight independent checkpoints and runs one bounded segment per chain (default 20 more sweeps). `stage8_admission.py` verifies saved files, SHA-256, burn-in tags, geometry-lock consistency and observable dimensions; **it refuses to fabricate mass/string-tension values**. `stage8_physical_matching.py` checks planned physical Wilson source distances only, not renormalized scale matching. `stage8_extended_paths.py` creates separately versioned 1–12-edge plans (288 paths per model, reaching 6.57 and 6.84 physical units); these new paths are **not** yet sampled by the legacy 100-path checkpoint estimator.

## Continue a short chunk on a local machine

```bash
cd ym_stage8
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 NUMBA_NUM_THREADS=1
python stage8_campaign.py --checkpoint-root checkpoints --seeds 101 211 307 419 --increment 20 --target 10000 --burn 1000 --thin 10
python stage8_admission.py --root checkpoints --output stage8_admission.json
```

`--burn 1000` is a provisional warmup threshold, **not a proof of equilibrium**. Check independent hot/cold-start agreement, parameter sensitivity and chain mixing before treating any saved post-burn records as equilibrated.

## Slurm production job array

The `stage8_slurm_array.sh` example is prepared for a computing cluster: `sbatch stage8_slurm_array.sh`. It assigns each of eight jobs to a different geometry/seed checkpoint, run in increments of 100 sweeps. Site-specific environment, queue limits, storage and CPU requirements should be verified first. Run **only one process per checkpoint**. The planned 10,000 sweeps per chain are neither completed nor guaranteed sufficient for precision. The current two-geometry workload was previously estimated at ~33 hours of gauge updates, plus comparable spectroscopy overhead if measuring all three smearing levels on every tenth sweep.

## Required science gates before a physical fit

1. Four **equilibrated** chains per geometry; rank-normalized Rhat below 1.01 and bulk/tail ESS of at least 400 **for the fitted correlator channels**, checked for several possible warm-up cuts, with chain-block/joint-bootstrap uncertainty.
2. For the **scalar 0++ mass**, stable, positive 3+ nonzero-time fit windows under time-cosh and variational analysis, APE levels 0,2,6, multi-operator covariance regularity and systematic stability.
3. For **sigma**, time-plateaued static potentials from several actual physical separations (with orientation checks), **or** independent converged center-charged winding-flux energies corrected for finite-string length.
4. Tune nonperturbative scale and temporal/spatial anisotropy and control physical volume before Penrose/square comparisons. A mean bare beta or isotropic *quadratic* action does not certify these.
5. Additional tile scales, approximant phases and couplings are needed for finite-volume, geometry-admission and continuum extrapolations. M=55 passes one local rooted-motif screen, **not the full causal-admission or continuum-equivalence criteria**.
6. Obtain scalar mass and string tension from the *same accepted ensembles*, then run joint bootstrap ratio fits. If any one gate fails, output `null` and explain why. No extrapolation should be run on incomplete or mixed observations.

## Regression tests

```bash
python -m unittest -v test_stage8 test_stage8_observables
python test_stage7.py
python test_stage7_restart.py
python test_stage7_measurement.py
python stage8_physical_matching.py
```

The source can be resumed independently without needing any prior conversation links. Do not use results from the superseded de Bruijn Penrose graph generator.

## Restore the split checkpoint archives

The approximately 400 MiB of saved gauge fields are distributed separately from the compact code ZIP. Unzip the compact `Penrose_YM_Stage8_Analysis_And_Resume_Code.zip` and then all four checkpoint archives into **the same directory** (each archive already contains the `ym_stage8/` prefix):

- `Penrose_YM_Stage8_Checkpoints_Square_101_211.zip`
- `Penrose_YM_Stage8_Checkpoints_Square_307_419.zip`
- `Penrose_YM_Stage8_Checkpoints_Penrose_101_211.zip`
- `Penrose_YM_Stage8_Checkpoints_Penrose_307_419.zip`

Run `python stage8_admission.py --root checkpoints` after `cd ym_stage8`; the SHA-256 manifest in the compact ZIP covers the full source and checkpoint set. No part of the saved configurations is omitted from these four checkpoint archives.
