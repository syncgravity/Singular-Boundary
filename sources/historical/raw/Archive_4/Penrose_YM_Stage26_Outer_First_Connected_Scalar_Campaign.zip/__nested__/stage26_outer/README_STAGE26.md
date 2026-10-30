# Stage 26: independent-outer-field scalar multilevel campaign

This run is designed to **measure connected scalar correlators across independent outer gauge chains**, not to count replicas as outer configurations. It uses the full 22,801-anchor square and 22,808-anchor Penrose geometries, 20 temporal slices, and the three unrestricted controls plus the full strict matched auxiliary.

## Critical limitations

- No finite Monte Carlo sample guarantees a mass plateau or continuum conclusion. Burn 96, depth 32 and two independent inner replicas are provisional settings based on *one* saved outer field per geometry. Monitor drift and covariance before mass fitting.
- Four distinct chains per geometry are required for the cross-chain vacuum estimate. Inner replicas and the five shifted offsets do not increase independent outer sample count.
- The saved direct products and conditional products refer to **the same cross-slab time pairs**, which differ with offset. Each offset independently covers lags 2..10; offsets rotate over consecutive outer samples to reduce measurement cost. This preserves temporal span, but potentially incurs offset-specific variance and bias: analyze by offset and chain.
- Do not treat these Stage 9-resumed chains as independent of Stage 17/18/19 runs using the same initial state and RNG. The eight seeds are separate chains; historical stage runs are not additional independent samples.
- Direct and conditional one- and two-point estimators are stored. The provided audit makes **only exploratory point estimates** and does not admit scalar masses. Rigorous autocorrelation-aware block bootstrap, covariance-aware fit windows, inner equilibration, direct/conditional agreement and ensemble effective sizes must still be assessed after sufficient data.
- Estimated run duration is potentially **multiple days** for eight chains. Each outer field requires ~2 inner trajectories. Always ensure free disk space; source checkpoints remain read-only.

## Installation and tests

Extract this ZIP into the `QCYangMills` working directory so it creates `stage26_outer/`. From that directory:

```bash
python3 -m unittest -q test_stage26
(cd stage24_inner && python3 -m unittest -q test_stage24)
```

## Mandatory one-field end-to-end check

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 NUMBA_NUM_THREADS=1 \
python3 stage26_outer.py --kind square --seed 101 \
  --checkpoint ../ym_stage9/checkpoints/square_nt20_seed101.npz \
  --output smoke_only --target-sweeps 10001 --stride 1 \
  --burn 0 --depth 1 --thin 1 --reps 1 --max-outer 1
```

The smoke data use NONPRODUCTION inner parameters and must not be merged into the real campaign.

## One single restartable full campaign

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 NUMBA_NUM_THREADS=1 \
caffeinate -is python3 stage26_manager.py \
  --inputs ../ym_stage9/checkpoints \
  --output stage26_results \
  --cache stage24_inner/deps_stage23/deps/stage19_complete \
  --target-sweeps 12000 --stride 20 --burn 96 --depth 32 --thin 3 --reps 2
```

This schedules **100 new outer fields per chain** after sweep 10000, 800 outer fields total, across four independent seeds per geometry. Set `--target-sweeps` higher (e.g. 14000) only after reviewing expected cost. Target is a *hard upper sweep bound*; a rerun with unchanged parameters resumes from `stage26_results/<kind>_seed<seed>/restart.npz`. The manager processes chains sequentially to minimize memory pressure on an 8 GB M1. A worker can be stopped between completed outer records; only the currently running record may be lost. Stored checkpoint updates occur after writing the observation, so a crash between the two triggers deterministic replay and replacement. Do not edit or remove the `restart.npz` or the source Stage 9 files.

## Records and basic audit

`stage26_results/<kind>_seed<seed>/outer_00010020.npz` records per outer sweep: `direct_timeslice [20,4]`, `direct_product [9,4,4]`, `conditional [reps,9,4,4]`, `conditional_onepoint [reps,20,4]`, `offset`, `pair_counts`, inner timings, and catalogue hashes. `latest.json` and `restart.npz` are stored separately. Do not count two replicas as two outer configurations.

```bash
python3 analyze_stage26.py --results stage26_results --out STAGE26_AUDIT.json
```

Upload the compact `outer_*.npz` records plus `latest.json`, optionally grouped by chain in ZIP archives. **Keep the very large `restart.npz` files locally.**
