# Stage 24: conditional inner convergence and connected-estimator diagnostic

## Goal and scientific status

This is a **full-size** SU(2) scalar multilevel diagnostic, not a physical glueball mass extractor. It measures full-volume 3-, 5- and 8-face controls and the completed strict auxiliary on both square (22,801 spatial anchors) and periodic Penrose M55 (22,808 spatial anchors). Original Stage 9 checkpoints are read-only. Stage 23's cross-slab selector fix is retained.

Independent **inner replicas** are started from the same outer gauge field, but use independent streams and are NOT independent outer configurations. Each burn-in length receives a fresh replica; it is not a nested prefix of the previous burn. Within each replica, the reported sample-depth means are nested prefixes. This is a convergence diagnostic, not a proof of thermal equilibration.

Raw data contain conditional one-point means (`onepoint`, shape `[outer,offset,burn,replicate,depth,20,4]`), lagged cross-slab products (`conditional`, shape `[outer,offset,burn,replicate,depth,9,4,4]`), direct timeslice observables (`direct_timeslice`, shape `[outer,20,4]`), direct cross-slab products (`direct_product`, shape `[outer,offset,9,4,4]`), per-lag pair counts, inner wall-clock times, cache errors, source/catalogue SHA-256, and source sweeps. Time lags are 2 through 10.

**Important distinction:** The one-point means and products can fluctuate considerably at finite burn/depth. Correlation functions are obtained only after an outer-ensemble expectation and a *separately estimated* vacuum-product subtraction. Subtracting inner means on a single conditioned gauge configuration is NOT the connected mass correlator. The analysis script refuses disconnected subtraction with fewer than two distinct chain seeds; its multi-seed point estimate is still exploratory, without autocorrelation confidence bounds.

## Install and tests

Unzip `Penrose_YM_Stage24_Inner_Connected_Diagnostics.zip` in your existing `QCYangMills/` folder. Enter `stage24_inner` and run

```bash
python3 -m unittest -q test_stage24
```

## First Mac benchmark — one outer field, two burn lengths and two depth limits

From `stage24_inner`:

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 NUMBA_NUM_THREADS=1 \
caffeinate -is python3 stage24_inner_diagnostics.py \
  --kind square --seed 101 \
  --checkpoint ../ym_stage9/checkpoints/square_nt20_seed101.npz \
  --cache deps_stage23/deps/stage19_complete \
  --output stage24_results --outer 1 --stride 10 \
  --burns 12 48 --depths 4 12 --reps 2 --thin 3 --offsets 0
```

Run the corresponding Penrose test:

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 NUMBA_NUM_THREADS=1 \
caffeinate -is python3 stage24_inner_diagnostics.py \
  --kind penrose --seed 101 \
  --checkpoint ../ym_stage9/checkpoints/penrose_nt20_seed101.npz \
  --cache deps_stage23/deps/stage19_complete \
  --output stage24_results --outer 1 --stride 10 \
  --burns 12 48 --depths 4 12 --reps 2 --thin 3 --offsets 0
```

Expect **four conditional replicas per outer field per offset** (two burn lengths x two independent replicas), each reaching the largest K. This may take several minutes per geometry on an M1. For a first brief integrity screen use `--burns 0 --depths 1 --reps 2 --stride 1`, but never infer inner equilibration from that screen. `--offsets 0 1 2 3 4` is more comprehensive and approximately five times the inner cost.

## Analyze and upload

```bash
python3 analyze_stage24.py stage24_results/*stage24*.npz --out STAGE24_DIAGNOSTICS.json
```

Upload the compact `.npz` and `.json` outputs. The intermediate Stage 23 arrays cannot substitute for this experiment because they do not retain independent replica and one-point data. Do **not** delete source gauge checkpoints.

## Admission criteria before expanding

1. Replicate means approach stable values with increasing burn-in and inner depth, with uncertainty assessed at fixed outer states.
2. Direct versus conditional products agree **after** combining enough independently equilibrated outer fields and preserving chain/outer identity; not necessarily on an individual outer state.
3. Compare CPU time and error bars at the **outer-chain level**, with inner sampling noise included. Inner replicas cannot multiply the outer sample size.
4. Construct connected correlators with vacuum subtraction from independent *outer chains*, test stationary and autocorrelation assumptions, and require at least three adjacent positive and reproducible time separations before a mass fit.
5. The full catalogue and primary unrestricted control channels are retained; no spatial anchor dropped in the full strict auxiliary.

### Current status

Three small code tests passed. One real full-size **square** seed-101 smoke test (one outer sweep, two inner replicas, one sample each, zero burn) passed, including a zero plaquette-cache discrepancy. Penrose full-size Stage 23 smoke tests passed previously, but **this new Stage 24 replica driver has not yet been run on Penrose** here. No ensemble convergence or variance improvement is claimed.
