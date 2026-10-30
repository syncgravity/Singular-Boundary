# Stage 18: independent scalar spectroscopy continuation

This package extends the **original Stage 9** gauge fields with per-timeslice spatial APE scalar measurements at levels 0, 2, 6, 12. Square and Penrose use the original verified plaquette/cluster operator families, three scalar groups per level (12 scalar channels in total, shape `(measurements,20,12)`). The lattice geometry, Metropolis update kernel, coupling, Nt, RNG state and plaquette cache follow Stage 17/Stage 9. Stage 18 is **not a mass determination**; later chain-blocked, vacuum-subtracted, cross-validated connected correlators are necessary.

## Critical isolation

**Do not run this in your active Stage 17 `stage17_results` output tree.** It is a separate continuation from original Stage 9 sweep 10,000, saving under `stage18_scalar_results`. It does not read or change Stage 17 live restarts. If the same original field, seed and RNG state are used with the same gauge updater as Stage 17, the trajectories are **not independent** of Stage 17. Count them once for gauge-statistics purposes; Stage 18 adds scalar channels to that trajectory, not another independent Monte Carlo chain.

This is a future Mac activity: **do not launch Stage 18 while Stage 17 is running on the 8GB M1 unless you explicitly decide to share computational resources**. The files here merely prepare a reliable self-contained runner.

## Extract, test, smoke

```bash
cd /Users/sharpe/Projects/Business/QCYangMills
unzip ~/Downloads/Penrose_YM_Stage18_Scalar_Continuation.zip
cd stage18_continuation
python3 -m unittest -q test_stage18
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 NUMBA_NUM_THREADS=1 \
python3 stage18_scalar_run.py --kind square --seed 101 \
  --inputs ../ym_stage9/checkpoints --output stage18_smoke \
  --chunk 1 --thin 1 --target-sweeps 10001
```

**Note:** the smoke command requires `stage18_smoke/square_seed101/` to be absent or compatible. It creates an independent one-sweep result.

## Production after Stage 17 completes

Start with 100 new sweeps on a single seed to estimate throughput:

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 NUMBA_NUM_THREADS=1 \
caffeinate -is python3 stage18_scalar_run.py \
  --kind square --seed 101 --inputs ../ym_stage9/checkpoints \
  --output stage18_scalar_results --chunk 100 --thin 10 --target-sweeps 12000
```

When comfortable, run all 8 chains serially to a **fixed per-chain target** (unlike Stage 17's time-based cap):

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 NUMBA_NUM_THREADS=1 \
caffeinate -is python3 stage18_manager.py \
  --inputs ../ym_stage9/checkpoints \
  --output stage18_scalar_results --target-sweeps 12000 \
  --chunk 100 --thin 10
```

This runs up to **sweep 12,000 for each chain**, resumes each from `restart.npz`, and stops on a count. Change `--target-sweeps` to extend later. Each 100-sweep segment contains 10 configurations with `observables_scalar` shape `(10,20,12)`, timeslice-by-operator samples, provenance hashes, and sweep indices. Keep `restart.npz` locally; upload only `observations_*.npz` and `latest.json` for the later analysis. All source checkpoints are read-only. No Stage 17 files are needed.

## Checks and limitations

- Real-field smoke tests on square and Penrose seed 101 at sweep 10001: **max plaquette cache error 0.0**, output shape `(1,20,12)` for each.
- Target cutoff re-invocation checked: reports `target_reached` without additional updates.
- Two unit tests pass.
- Stage 18 extension levels 0/2/6/12 and underlying original kernels have been regression-tested in the preceding Stage 18 snapshot pilot.
- No positive-definite variational spectrum, mass gap, or physical Penrose difference is claimed. Extraction requires vacuum subtraction, autocorrelation blocking, held-out subspace choice, and >3 stable temporal points. A single lattice spacing cannot establish a continuum result.
