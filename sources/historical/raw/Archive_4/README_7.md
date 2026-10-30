# Stage 7: large matched torus implementation

This package is **NOT** a completed mass/string-tension calculation. All saved 20-slice gauge fields are **hot-start warm-up states** (4 sweeps), with zero post-burn-in measurements. See `STAGE_7_REPORT.md` for requirements and limitations.

## Reproduction

```bash
python -m pip install numpy scipy numba
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 NUMBA_NUM_THREADS=1
python stage7_large_torus.py            # full M55/square action matrices + audit
python test_stage7.py                   # exact comparison to previous small-volume implementation
python test_stage7_restart.py           # deterministic restart, Haar initialization and SU(2) norms
python test_stage7_measurement.py       # gauge invariance and physical spatial paths
python stage7_measurement.py            # large operator/physical path/winding plans
```

To continue a *single chain* in short, restartable batches, keeping measurements once burn-in is complete:

```bash
python stage7_checkpointed.py --kind penrose --seed 101 --nt 20 --beta 3.5 --burn 1000 --thin 10 --total-sweeps 10000 --max-sweeps-this-run 50 --measure --checkpoint-root checkpoints
python stage7_checkpointed.py --kind square  --seed 101 --nt 20 --beta 3.5 --burn 1000 --thin 10 --total-sweeps 10000 --max-sweeps-this-run 50 --measure --checkpoint-root checkpoints
```

Repeat with independent seeds (e.g., 211, 307, 419) for each geometry. The nominal 10,000-sweep target is only a planning number; successful spectroscopy could require much longer runs. `--measure` is REQUIRED when a segment crosses a post-burn-in thin-sampling sweep; the program refuses to silently discard scheduled production measurements. Measurements are appended to the restorable NPZ, preserving cross-operator and cross-time correlations, while avoiding O(100 GB) storage of all gauge fields. The full gauge configuration, cached plaquettes, PRNG state and all recorded observations are saved atomically on each checkpoint. **Do not use warm-up plaquette values to estimate physical quantities.**

## Source audit and limits

The old non-Haar experimental initialization was identified and superseded before packaging. The current `stage7_checkpointed.py` initializes SU(2) links by normalizing four independent Gaussians, with its distribution checked by `test_stage7_restart.py`.

The 151×151 regular square and 22,808-face rational model-set torus have the same total spatial area and near-equal period lengths but **are not yet nonperturbatively matched**. The rational model-set passes a previous local-motif screening criterion, not the full causal-admission protocol. **No continuum limit or mass gap is established.**
