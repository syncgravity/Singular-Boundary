# Stage 9 clean restart and Apple M1 optimization

**Environment:** Apple M1 MacBook Pro, 8 GB unified memory, macOS Tahoe 26.4, Python 3.10+.  **Physics:** unchanged Stage 9 SU(2) Wilson Metropolis code; 2D spatial torus extruded to 20 Euclidean time slices; `beta=3.5`, four independent seeds per geometry, 1,000-sweep provisional burn-in, measure every 10 sweeps, planned target 10,000 sweeps per chain. A completed target is not evidence of convergence.

## 0. Put the two new scripts into `ym_stage9/`

Use the existing Stage 9 source directory (where `stage7_checkpointed.py`, `wilson_torus.py`, and `stage9_requirement_audit.py` are already present). Extract the accompanying package there, keeping its two `.py` files in the same folder; you may also copy this guide there.

```bash
cd /Users/sharpe/Projects/Business/QCYangMills/ym_stage9
python3 --version
python3 -c 'import platform,numpy,numba,scipy; print("CPU architecture:",platform.machine(),"numpy:",numpy.__version__,"numba:",numba.__version__)'
pgrep -fl 'stage9_local_batches.py|stage9_m1_manager.py|stage7_checkpointed.py' || true
```

Wait until no old jobs remain; **stop any existing runner before resetting or starting the new one**. Native `arm64` Python is strongly preferred. If the output says `x86_64`, you may be running under Rosetta and losing performance. Confirm your Python/NumPy/Numba installation is Apple Silicon native; do not replace a working environment while a job is running.

## 1. Restart truly fresh (do not restore checkpoints)

A fresh Stage 9 run begins with newly generated, independently seeded Haar SU(2) links. It does **not** reuse the prior warm-up histories or the older Stage 8/9 checkpoints.

**Review the files first:**

```bash
python3 stage9_m1_manager.py reset
```

**Safest option: archive the old checkpoint folder and logs**, keeping them as a recoverable historical snapshot:

```bash
python3 stage9_m1_manager.py reset --mode archive --apply
```

**If you specifically want disk space back and intend to discard these current checkpoint states:**

```bash
python3 stage9_m1_manager.py reset --mode delete --apply \
  --confirm DELETE_OLD_STAGE9_CHECKPOINTS
```

The deletion is deliberately restricted to recognized `square_nt20_seed{101,211,307,419}` / `penrose_nt20_seed{101,211,307,419}` checkpoint files, their progress files, temporary checkpoints, driver lock files, and Stage 9 batch logs. It refuses unexpected filenames; it does **not** touch source code, Stage 9 archives, Stage 5 data, or source reports. Deletion is irreversible unless you have a backup. Do not run reset while any sampler process is active. If you instead archive, the archived files still consume disk space until you delete that archived folder separately.

After reset:

```bash
python3 stage9_m1_manager.py status
# All eight should say "not initialized".
```

The old standalone `stage9_local_batches.py` may remain on disk, but **never run it concurrently** with the new manager; only one orchestration method should own these checkpoints.

## 2. Optional repeat-startup optimization: Numba disk cache

The Stage 9 sampler is already JIT compiled with Numba. Across process restarts, disk caching avoids repeated LLVM compilation of unchanged kernels. The script changes **decorators only** (`@njit` to `@njit(cache=True)`) in exactly two source files, keeping backups for reversal:

```bash
python3 enable_numba_disk_cache.py                # preview
python3 enable_numba_disk_cache.py --apply       # enable, one-time
python3 -m unittest -q \
  test_stage8 test_stage8_observables \
  test_stage9_fit_tools test_stage9_requirement_audit test_stage9_coldinit
```

The same change was checked against the original unpatched sampler: two-sweep gauge links, plaquette caches, and RNG states were exactly equal. The existing 21 regression tests passed. This patch improves *startup overhead*, not the intrinsic Metropolis sweep time. To undo it later, use `python3 enable_numba_disk_cache.py --restore` (only if these files have not been subsequently edited).

**Do not** enable Numba `fastmath`, parallelize updates within one chain, change proposal angles, alter PRNG code, mix incompatible saved states, or switch Wilson couplings for a speed gain: those require a separate mathematical/numerical validation.

## 3. Benchmark the memory-safe parallelism

Start with two chains at once for a bounded **single pass**, and compare with your previous serial baseline of 147–149 s per 100 sweeps. Because only eight GB of unified memory is installed, begin with a small batch size and watch **Activity Monitor → Memory → Memory Pressure / Swap Used**.

```bash
# Two workers, two independent square chains, one short segment each:
python3 stage9_m1_manager.py run \
  --workers 2 --chunk 100 --passes 1 \
  --kinds square --seeds 101 211 --verify-hash
```

This performs actual, saved, independently seeded gauge updates, not a synthetic benchmark. The terminal and `stage9_m1_batch_log.jsonl` record each chain's measured duration. The above test also initializes two chains. If you want a serial comparison on the same machine without redoing those chains, run the remaining two square seeds serially:

```bash
python3 stage9_m1_manager.py run \
  --workers 1 --chunk 100 --passes 1 \
  --kinds square --seeds 307 419 --verify-hash
```

Compare *total wall time per 200 sweeps*, not just the duration of an individual chain. Two-worker concurrency is worthwhile only if throughput improves and Memory Pressure stays green without persistent swap growth. On the M1 8 GB, **do not run 4 or 8 workers**. Two workers is a candidate, not an assumed speedup. Use one worker if two produce yellow/red memory pressure, sustained swapping, thermal throttling, or no throughput improvement. Disable other memory-heavy applications while the run is active.

The driver pins BLAS, OpenMP, Accelerate, and Numba worker thread counts to one *for each child process*, avoiding oversubscription; it never edits the SU(2) transition kernel.

## 4. Overnight or unattended local *process* execution

After the benchmark, select one or two workers and a segment length of 250. If reliable, try 500; this reduces expensive checkpoint/JIT-startup cycles but increases the maximum work lost to a crash. Full gauge state checkpoints are written atomically by the original sampler.

```bash
# Plug in the Mac; run all eight chains and stop between segments
# after approximately six hours of elapsed time.
caffeinate -is python3 stage9_m1_manager.py run \
  --workers 2 --chunk 250 --passes 0 --max-hours 6 --verify-hash
```

Use `--workers 1` if benchmarking recommends serial execution. Keep the laptop adequately cooled and configured not to sleep. `caffeinate -s` prevents system sleep while on AC power; lid-close behavior varies with the actual hardware setup, so don't rely on a closed-lid run without testing it.

When the command returns, resume by executing the **same command again**; completed checkpoints are recognized. To end it cleanly, allow the segment to finish and use the time budget. Pressing Ctrl-C may interrupt an in-progress segment; only the last completed atomic checkpoint is guaranteed to be reusable. No computation continues after the shell process stops.

Periodically check:

```bash
python3 stage9_m1_manager.py status --verify-hash
python3 stage9_requirement_audit.py --root checkpoints --output STAGE_9_ADMISSION.json
```

Run the scientific audit once all eight chains have been initialized. The machine-readable admission outputs must remain **fail-closed** until the physical-measurement criteria are met.

## 5. Resource use, estimates and scientific limits

Each Stage 7 M55 geometry has approximately 1.37 million dynamic gauge links and plaquettes. Your original machine took roughly 1.48 s for a sweep in a serial warm-up run. At that rate, 80,000 combined sweeps take about **33 hours of update work** if executed serially. This estimate excludes checkpoint, geometry construction, JIT compilation, gauge-observable measurement, thermal throttling, and additional continuum ensembles. Under two-worker execution, aggregate throughput *may* improve; do not assume linear scaling. Measurements can slow production markedly beyond the 1,000-sweep burn-in.

At 10,000 sweeps with 1,000 burn-in and thinning by 10, the **nominal maximum** is 900 saved post-burn-in measurements per chain (3,600 per geometry), but this does not imply that they are statistically independent or equilibrated. Actual production acceptance requires hot/cold agreement or another credible equilibration analysis, rank-normalized R-hat < 1.01 and bulk/tail effective sample sizes >= 400 on the observables of interest, stable covariance-weighted multi-time scalar and confinement fits, physical scale/anisotropy matching, finite-volume checks, and a continuum trajectory.

If you see a checksum mismatch after a hard kill, do not delete the checkpoint or overwrite it. It may have a newer atomic `.npz` but stale `_progress.json`; that needs explicit reconciliation using the NPZ's saved sweep count, settings and RNG state before another run. Likewise, if the code reports a missing or unexpected file, stop and inspect rather than renaming files blindly.

## 6. What to send back for our next analysis

Send the text of `stage9_m1_manager.py status --verify-hash`, a few lines of `stage9_m1_batch_log.jsonl` that show actual segment times, the output of `sysctl vm.swapusage`, and `STAGE_9_ADMISSION.json` when you have post-burn-in measurements. Do not send the hundreds of megabytes of full gauge checkpoints unless they are needed for a specific numerical audit.

### Validation of this extension

- 9 targeted launcher and deletion-safety unit tests passed.
- 21 inherited Stage 9 numerical regression tests passed.
- A real single-worker fresh + restarted million-link gauge simulation passed its cache and SHA checks.
- A real two-worker test initialized and checkpointed two independent-seed chains without writing to the same file.
- The JIT-cache-only decorator change yielded exactly the same stored links, plaquette values, RNG state and empty preproduction observable arrays as the unmodified code for the matched two-sweep test.
- None of these engineering tests certifies an equilibrated ensemble or physical Yang–Mills mass or string tension.
