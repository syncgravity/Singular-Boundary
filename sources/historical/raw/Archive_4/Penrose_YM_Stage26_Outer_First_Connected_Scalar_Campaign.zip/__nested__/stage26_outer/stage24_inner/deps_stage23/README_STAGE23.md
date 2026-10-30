# Stage 23 — Full-lattice outer-ensemble scalar conditional benchmark

**Experimental code, not production-approved.** The primary goal is to validate a temporal-slab conditional estimator of scalar two-point products on both ~22,800-anchor geometries, not to extract a mass prematurely.

## Statistically critical distinctions

* Outer updates use the original Stage 9 Monte Carlo kernel and saved `rng` stream; input checkpoints remain **read-only**. Each independently seeded outer chain is an independent *chain*, but nearby outer configurations are autocorrelated. Outer configurations here continue from Stage 9 sweep 10,000, not from Stage 19 sweep 15,000; they are **not independent of other work reusing those Stage 9 states**.
* At each new outer field, four disjoint slab interiors are updated conditioned on frozen spatial boundary links. Separate RNG streams are provided for the slabs. Conditional means within each slab produce their product for operators in different slabs. Their expected product equals the true direct product **only if the outer ensemble and the conditional chains are equilibrated**.
* **Bug fix relative to Stage 22:** for offset 1–4, the correct slab assignment is computed by walking backward to the nearest cyclic boundary; using the smallest numerically sorted boundary was incorrect and can mistakenly admit same-slab pairs.
* Inner conditional chains are not independent outer configurations. Multiple shifted boundary offsets on one outer configuration are also **not independent outer configurations**. Cost efficiency includes inner thermalization and scalar measurement time, and uncertainty must preserve chain and outer-block structure.
* Products are **unsubtracted**: physical connected scalar correlators require a separately estimated vacuum disconnected contribution, preferably a cross-chain estimate with uncertainty propagation. A noisy un-subtracted product does not imply a scalar signal or mass.
* Both original full-volume scalar controls (3,5,8 faces) and the complete strictly matched auxiliary are measured; both geometries use full spatial-anchor coverage. No Penrose anchors are omitted.

## Tests and confirmed full-lattice smoke results

```
cd stage23_outer
python3 -m unittest -q test_stage23
```

Three logic tests pass, including all five shifted offsets. I ran **one actual new outer gauge sweep** from each existing Stage 9 seed-101 full-lattice checkpoint, with one inner sweep at offset 1. Both square and Penrose passed frozen-boundary and plaquette-cache validation. The approx. 10 s per-geometry benchmark includes compilation and setup, and is not representative of your Apple M1 or a thermalized conditional run.

## Run small test on Mac first

From `QCYangMills/stage23_outer`:

```
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 NUMBA_NUM_THREADS=1 \
caffeinate -is python3 stage23_outer_benchmark.py \
  --kind square --seed 101 \
  --checkpoint ../ym_stage9/checkpoints/square_nt20_seed101.npz \
  --output stage23_screen \
  --outer 2 --stride 10 --depths 4 12 --burn 12 --thin 3 --offsets 0
```

Repeat on `penrose` with the corresponding checkpoint. **Do not treat `burn=12` as validated inner equilibration**. Run `--burn 24` or more and vary `--thin` in a distinct benchmark; convergence may need considerably longer. The starting fields are full Stage 9 checkpoints, not Stage 19 later restart states.

To run a more complete, more costly benchmark after the small gate, repeat for all 8 seed/geometry combinations, with `--outer 20 --stride 20 --depths 4 12 32 --burn 32 --thin 4 --offsets 0`. Only scale when you have demonstrated mixing and monitored actual runtime/memory. For reliable variance comparisons, more outer configurations and repeated independent chains will likely be necessary. Increasing `K` alone cannot cure outer-field fluctuations.

Each run writes a compact `.npz` with axes `(outer configurations × offsets, inner depths, temporal lags 2–10, 4 source channels, 4 sink channels)`, one JSON manifest, and no full gauge fields. Runs are deterministic from each unchanged source checkpoint but are not interruption-resumable: treat each invocation as one bounded experiment with distinct output names/paths.

## Exploratory analysis

```
python3 analyze_stage23.py stage23_screen/*_stage23.npz --out STAGE23_SCREEN.json
```

The screen reports the direct-versus-conditional paired difference and naive outer variance for auxiliary at lag 4. Estimates with fewer than 8 outer configurations are not adequate to establish anything; autocorrelation reduces the effective sample count. The screen currently requires **one offset per outer field** for the variance comparison. Use a chain- and outer-clustered bootstrap before doing a real multi-offset test.

## Admission gates before a large campaign

1. Fixed spatial-boundary invariance, exact cache agreement, geometry hashes and matched path catalogues.
2. Inner burn-length, thinning and depth convergence tests, with integrated autocorrelation estimates and independent inner-stream replication where practical.
3. Multiple independent *outer* gauge chains and enough outer observations to assess paired direct-versus-conditional expectation agreement across several lags.
4. Cost-adjusted uncertainty per unit CPU time (including outer sampling, inner thermalization, all offsets) estimated by chain-preserving outer-block bootstrap.
5. Correlated, vacuum-subtracted connected scalar correlators and only then a stable 3+ time point mass plateau. No physical mass values from this package.
