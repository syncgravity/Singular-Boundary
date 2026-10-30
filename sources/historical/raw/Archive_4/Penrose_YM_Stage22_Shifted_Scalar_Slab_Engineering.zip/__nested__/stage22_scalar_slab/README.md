# Stage 22 — Full-size shifted-slab scalar engineering benchmark

**Status:** full-lattice smoke verification on one saved square and one saved Penrose seed-101 gauge field. The implementation is an engineering prototype, **not yet a validated scalar variance-reduction method**. No glueball mass or string tension is inferred.

## Requirements

- Python 3, numpy, scipy, numba
- Four-channel Stage 19 complete catalogues are bundled under `deps/stage19_complete/stage19_complete_catalogues/`.
- Stage 9 final saved gauge checkpoint fields, e.g. `square_nt20_seed101.npz`, are **read-only**.

`stage22_shifted.py` depends on `deps/stage19_complete/stage21_scalar_multilevel.py` and its bundled Stage 19/Stage 7 code. Start from the directory `stage22_scalar_slab`.

## Tests and pilot

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 NUMBA_NUM_THREADS=1 python3 -m unittest -q test_stage22
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 NUMBA_NUM_THREADS=1 python3 stage22_shifted.py \
  --kind square --seed 101 --checkpoint /path/to/square_nt20_seed101.npz \
  --inner 2 --burn 1 --thin 1 --offsets 0 --output smoke
```

For Penrose replace `--kind` and `--checkpoint`. For all shifted boundaries use `--offsets 0 1 2 3 4` with `--inner 8 --burn 8 --thin 4` as a **mixing diagnostic**, not final production acceptance. Runtime scales roughly with inner updates and offsets; on an 8GB Mac use a single process.

## Method

At offset o, spatial links on four boundary slices o,o+5,o+10,o+15 modulo 20 are held fixed. The temporal and internal spatial links form four disjoint active masks. Each slab is updated with a *separate deterministic RNG stream*, using the same SU(2) local Metropolis kernel as the original chain. The complete spatial scalar controls (3-, 5-, 8-face) and strict full-anchor auxiliary are measured on each conditioned field. Only pairs strictly inside distinct slabs are used. Shifted offsets provide separation coverage t=2..10, but are **correlated measurements of the same outer configuration**, not five independent outer observations.

The direct value is O(t)O(s) from the original outer gauge field. The conditional-product is the product of within-slab sample means for O(t), O(s). Correctness of conditional-product inference depends on the outer state having the intended stationary distribution, exact slab factorization given the boundaries, and valid conditional updates. Finite K introduces Markov-chain estimation noise; stationarity and mixing must be checked on multiple independent outer fields. No comparison of sample variances from a single outer field is meaningful.

Each produced NPZ stores offset, lag, source and sink time indices, full 4x4 direct and conditional-product matrices, source input SHA256 and catalogue SHA256. Original checkpoint untouched. Each record includes one outer configuration only; chain and sweep must be tracked when merging future outputs.

## Statistical gates still pending

1. Multiple truly distinct outer states from both geometries, preserving independent chain/sweep identifiers. The eight **Stage 9 final snapshots** yield at most four outer observations per geometry, insufficient for precise variance or bias conclusions. Stage 19 continuation NPZ contains scalar observations, **not full gauge fields**, so it cannot be used to recalculate conditional slabs.
2. Check inner effective sample sizes by varying K, burn, skip, and independent RNG seeds; outer ensemble direct versus conditional agreement with paired bootstrap, not inner-as-outer pseudo-replication.
3. Compare variance **per end-to-end unit time**, including inner simulation and loop measurement, across both geometries and 20-time periodic windows. Scalar connected correlators require a separately estimated disconnected term with independent-chain safeguards.
4. Periodic-cosh or other physical mass inference is prohibited until strong, covariance-conditioned long-time data and excitation/finite-volume checks pass.

**Important:** the provided Stage 22 code is an engineering benchmark, not an overnight Monte Carlo continuation runner. It works on checkpointed full gauge fields. Do not treat the Stage 19 observation-only archives as outer gauge snapshots.
