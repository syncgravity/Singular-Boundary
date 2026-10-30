# Stage 16 corrected multihit on macOS Apple Silicon

This is a **read-only measurement runner**. It takes the final SU(2) gauge field from each Stage 9 checkpoint and measures corrected quaternion-based direct and exact single-link conditional-mean ('multihit') Wilson rectangles for identical physical-distance/orientation-matched path pairs. It leaves your 10,000-sweep checkpoints intact. It **cannot recover the 900 historical gauge configurations per chain** from the saved scalar/Wilson observations. Accordingly, its outputs are a *four-snapshot-per-geometry software/performance study*, not a reliable potential, string tension, or bootstrap ensemble.

## Install

1. Download/extract `Penrose_YM_Stage16_Mac_Multihit_Runner.zip` in `/Users/sharpe/Projects/Business/QCYangMills/` (the ZIP contains `stage16_mac/`).
2. Activate your existing `(QC)` environment. Verify that `numpy`, `scipy`, and `numba` are installed (prefer native arm64 Python).
3. Put the eight `*nt20_seed*.npz` files under `stage16_mac/checkpoints/` **or** pass your existing `ym_stage9/checkpoints` using `--checkpoints`.
4. No need to replace your Stage 9 code. This ZIP bundles the audited Stage 16 dependencies under `ym_stage13/` and `ym_stage16/`.

```bash
cd /Users/sharpe/Projects/Business/QCYangMills/stage16_mac
(cd ym_stage16 && python3 -m unittest -q test_stage16 test_stage16_matched)
python3 run_corrected_multihit.py --checkpoints ../ym_stage9/checkpoints \
  --output results_smoke --kinds square --seeds 101 --pairs 1 --lags 4
```

Then run the complete **snapshot** screen:

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 NUMBA_NUM_THREADS=1 \
python3 run_corrected_multihit.py \
  --checkpoints ../ym_stage9/checkpoints \
  --output results_600 \
  --pairs 600 --lags 4 6 8 10 \
  --kinds square penrose --seeds 101 211 307 419
```

An individual lag can take substantial time on the million-link system. For your 8GB M1, **run one process at a time initially** to avoid additional copies of 1.37M-link fields and geometry in RAM. The script prints the elapsed seconds for every checkpoint's lag array. Output `.npz` files are written atomically and the input checkpoints are never modified. On restart, existing results may be remeasured/overwritten; no physics results are merged automatically.

To view the data, `np.load('results_600/square_seed101_sweep10000_multihit.npz')` has arrays `direct` and `multihit` with shape `(n_lags,600)` and `r`,`dx`, source/target vertices, and matched indices. All paths in one snapshot are correlated. **Do not treat 600 paths as 600 independent Monte Carlo samples**. The manifest explicitly declines physical fits.

### Next requirement for valid physical extraction

To obtain production statistics with the new operator, we need to **continue independent Stage 9 gauge chains beyond 10,000 sweeps** and measure exact multihit on each newly saved, thinned configuration (or modify the existing Stage 9 production sampler to perform multihit *at measurement time*). The historical 7,200 configurations cannot be reconstructed from the 8 final link states. A statistically powered extension should retain per-chain/per-sweep/per-path measurements, perform blocked bootstrap and direct-vs-multihit consistency tests, then require stable long-time plateaus and nonperturbative anisotropy matching. This package does not automatically continue the Markov chains.

Note: Stages 13–15 had a quaternion/matrix convention mismatch. This runner uses the corrected Stage 16 quaternion algebra and must not be mixed with the earlier uncorrected transporter output.
