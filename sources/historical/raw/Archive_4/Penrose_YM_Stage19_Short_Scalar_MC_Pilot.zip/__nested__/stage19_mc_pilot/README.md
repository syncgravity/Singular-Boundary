# Stage 19 — Capped scalar Monte Carlo pilot (not mass spectroscopy)

Four time-slice channels on newly updated gauge fields: **full-volume 3-face, 5-face and 8-face controls**, plus the **strict 1.5-threshold auxiliary**, normalized over accepted spatial anchors. A fifth array stores the auxiliary with the *full-root denominator*. Square 22,801/22,801 and Penrose 22,658/22,808 anchors, independently enforced against the Stage 19 coverage certificate. No Penrose fivefold orbit average is claimed; this is a masked diagnostic, NOT a full zero-momentum operator.

The runner reads the original **Stage 9 final 10,000-sweep NPZ files** and resumes the original Markov states (links/cache/RNG). It does not modify them, Stage 17, or Stage 18 outputs. Since this starts from the same Stage 9 chains, **these are not statistically independent copies of any other continuation with the same RNG trajectory**.

## Installation and validation

Unzip into `/Users/sharpe/Projects/Business/QCYangMills/` so that `stage19_mc_pilot/` is next to `ym_stage9/`. With your `(QC)` Python venv active:

```bash
cd /Users/sharpe/Projects/Business/QCYangMills/stage19_mc_pilot
python3 -m unittest -q test_stage19_mc
```

Requires NumPy, Numba and SciPy as in Stage 18. A **first-time Numba compilation may take several minutes**. The geometry catalogues are expensive to build but are cached and SHA256-bound to all restart states. The cache is constructed once per geometry and reused across seeds.

## 1: Small smoke test

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 NUMBA_NUM_THREADS=1 \
python3 stage19_mc.py --kind square --seed 101 \
  --inputs ../ym_stage9/checkpoints --output stage19_smoke \
  --cache stage19_catalogues --target-sweeps 10001 --chunk 1 --thin 1
```

The smoke directory is separate from the proper pilot. **Do not restart production from the smoke directory**, because its `thin` and configuration differ.

## 2: Capped 100-sweep, eight-chain pilot

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 NUMBA_NUM_THREADS=1 \
caffeinate -is python3 stage19_manager.py \
  --inputs ../ym_stage9/checkpoints --output stage19_pilot_results \
  --cache stage19_catalogues --target-sweeps 10100 \
  --chunk 20 --thin 10
```

This runs serially (one process at a time), safely under an 8 GB M1, and stops at **10,100 sweeps per chain**. It produces 10 new observations per chain, 80 total across 8 chains. This is an **engineering / early-variance pilot, not enough to admit a physical glueball mass**. Each chain has distinct restart state and observation segments. To stop between chunks, use Ctrl+C after a `SAVED` line; rerun the identical command to resume. Do not force-quit while saving. The target is absolute—not 10,100 *additional* sweeps.

Expect each measurement to cost several seconds per saved gauge field in this execution environment, in addition to MCMC sweeps. Real Mac runtime may be different. All 8 chains might take significant time; inspect the first two chains before running all eight if resources are limited.

## Outputs

```
stage19_pilot_results/square_seed101/
  source_sha256.txt
  observations_00010000_00010020.npz
  restart.npz
  latest.json
```

`scalar` is `(n_measurements, 20, 4)` in channel order: 3-face, 5-face, 8-face, strict auxiliary conditional. `aux_full_denominator` has `(n_measurements, 20)`. The explicitly missing Penrose sites are **not** replaced by artificial loops. In the full-denominator channel missing roots contribute zero; this is a deliberately masked diagnostic, not an unbiased full-volume projection. Never treat it as a complete scalar operator. All input and segment SHA256 are recorded; restarting checks the last committed segment.

## Acceptance

The two geometries' physical operators are not equivalent simply because their shape descriptors meet the threshold. The first statistical audit should check connected correlators, chain/bootstrap dependence, and paired comparisons against unrestricted controls. The 100-sweep pilot cannot establish a physical 0++ mass, continuum scaling, or a Penrose–square effect.

**Upload compact `observations_*.npz`, `latest.json`, and optionally `stage19_catalogues/*_strict_catalogue.npz` for audit; keep `restart.npz` locally.**
