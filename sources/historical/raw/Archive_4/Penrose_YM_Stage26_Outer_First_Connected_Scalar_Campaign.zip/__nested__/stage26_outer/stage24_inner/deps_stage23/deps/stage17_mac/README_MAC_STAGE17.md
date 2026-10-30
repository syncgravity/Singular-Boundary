# Stage 17 — Corrected SU(2) multihit production measurements on macOS

This is a **new post-10,000-sweep continuation**, not a remeasurement of the 900 historical per-chain snapshots. The Stage 9 `.npz` checkpoints are *read-only*. The Stage 16 corrected quaternion estimator is used for both direct and exact single-source-line multihit Wilson rectangles. No scalar mass, string tension, scale matching, or continuum result is automatically inferred.

## Prerequisites

- Apple Silicon native Python >=3.10, numpy, scipy, numba (the same QC environment used for Stage 9).
- Existing `ym_stage9/checkpoints/` folder containing **all eight** `square_nt20_seed*.npz`, `penrose_nt20_seed*.npz` final checkpoints at sweep 10,000.
- At least ~1–2 GB free disk space for eight new ~75 MB restart states plus observational segments; budget additional space for backups and growth.
- Unzip the `Penrose_YM_Stage17_Mac_Production_Multihit.zip` into `QCYangMills` so the folder `stage17_mac` appears **alongside** `ym_stage9`.

## Safety and scientific scope

* Do not run your old Stage 9 manager at the same time against these checkpoints. This Stage 17 runner never changes Stage 9 input files.
* A separate `stage17_results/GEOMETRY_seedNNN/restart.npz` file holds the evolved gauge state, RNG, cache, and segment-commit hash. Observations are small `observations_START_END.npz` files with `direct`, `multihit`, `measured_sweeps`, `lags`, `r`, `dx`, `path_indices`.
* The Stage 9 RNG **and Metropolis kernel are unchanged**. Their trajectories continue exactly from the 10,000-sweep state. Numba compilation and filesystem I/O can dominate short batches.
* Default interval is every 10 new sweeps, and all nine temporal separations `2 3 4 5 6 7 8 9 10` are measured at time origin 0. Observations within a chain are autocorrelated; the 600 paths are not independent samples. This is a fixed-origin measurement, not an average over all time origins.
* The exact multihit conditional replacement applies to the **source temporal line only**. It is not a full multilevel average and does not alone certify physical potential plateaus.
* The full matched catalogue has <=5% radial and <=25 degree axis discrepancy, not renormalized physical matching.
* No estimator comparison should be interpreted as an unbiased precision gain without blocked cross-chain bootstrap and sufficient time separations.

## Installation and tests

```bash
cd /Users/sharpe/Projects/Business/QCYangMills
unzip ~/Downloads/Penrose_YM_Stage17_Mac_Production_Multihit.zip
cd stage17_mac
python3 -m unittest -q ym_stage16.test_stage16 ym_stage16.test_stage16_matched
```

## One-chain smoke test (writes NEW outputs only)

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 NUMBA_NUM_THREADS=1 \
python3 stage17_measure.py \
  --kind square --seed 101 \
  --inputs ../ym_stage9/checkpoints \
  --output stage17_smoke \
  --chunk 2 --thin 1 --pairs 1 --lags 2
```

Keep the smoke results separate from production; do **not** point a production run at `stage17_smoke` because the configuration (one path/lag, thin=1) is incompatible.

## Initial production test, serial

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 NUMBA_NUM_THREADS=1 \
python3 stage17_manager.py \
  --inputs ../ym_stage9/checkpoints --output stage17_results \
  --workers 1 --chunk 100 --passes 1 \
  --kinds square --seeds 101
```

For each selected chain this advances **100 new sweeps** and records **10 new gauge configurations** at all 600 matched paths and nine temporal lags. The first chunk incurs JIT compilation and first-time geometry construction. Check `stage17_results/square_seed101/latest.json` and the observation file array shapes `(10, 9, 600)`.

## Continue all eight chains with two workers on M1 8 GB (after memory check)

```bash
caffeinate -is python3 stage17_manager.py \
  --inputs ../ym_stage9/checkpoints --output stage17_results \
  --workers 2 --chunk 100 --passes 0 --max-hours 6
```

Do NOT delete Stage 9 checkpoints. The runner uses only two workers on a machine with 8 GB RAM; if Activity Monitor memory pressure is yellow/red, use `--workers 1` instead. Repeating the same command resumes the Stage 17 states rather than copying the original files again.

Each independent chain's results live in a separate folder. Keep `restart.npz`, all `observations_*.npz`, `source_sha256.txt`, and `latest.json` together. Back them up as a group. It is safe to stop between chunks; avoid force-killing during disk writes if possible. The driver refuses inconsistent hashes.

**Manual failure recovery:** if a process is terminated during a chunk, it will restart from the most recent committed `restart.npz`, not midway through the unfinished chunk. It may replace an orphan observation segment with the same exact range; it must not overwrite an already committed segment. Do not manually alter a `.npz` or its source hash.

## Data to upload for analysis

Upload the eight `observations_*.npz` collections in a ZIP, accompanied by eight `latest.json` and `source_sha256.txt` files. Do not upload the large Stage 17 `restart.npz` files unless specifically needed for an audit. Retain all restart files locally for further runs.

This Stage 17 campaign is not yet an admitted physical mass/string-tension calculation. Subsequent analysis must perform chain-block bootstrap, direct-versus-multihit ensemble agreement, fit-window and orientation checks, and nonperturbative scale/anisotropy matching.
