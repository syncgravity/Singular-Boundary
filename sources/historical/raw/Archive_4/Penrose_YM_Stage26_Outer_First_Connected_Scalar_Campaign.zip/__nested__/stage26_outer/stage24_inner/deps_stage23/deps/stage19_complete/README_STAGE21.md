# Stage 21: full-lattice conditional scalar-slab engineering prototype

The experiment operates on the complete square (22,801 face anchors) or periodic Penrose M55 (22,808 anchors) lattice, `Nt=20`, and uses the full Stage 19 strict matched auxiliary plus the three unrestricted full-volume rooted controls. This is *not* a small-lattice surrogate. It is a one-outer-field engineering prototype, NOT an accepted multilevel efficacy test or a production mass determination.

## Conditional identity and construction

Freeze **all spatial links** at times 0,5,10,15. This partitions the periodic 20-timeslice gauge field into four distinct temporal slabs with boundaries on those slices. Each updated temporal link belongs to only one slab; all interior spatial links are updated. The Wilson action factorizes into slab terms conditioned on the frozen spatial-link boundaries, so the interiors of different slabs have a product conditional law. At the representative interior times 2,7,12,17, the exact identity is

`E[O(t) O(s) | frozen spatial boundaries] = E[O(t)|B] E[O(s)|B]` for times in *different* slabs.

Each restricted local Metropolis sweep retains Stage 9's exact local action difference and acceptance rule; it simply skips frozen spatial links. The inner Markov chain is started from an existing (nominally equilibrated) Stage 9 outer configuration, so the conditional stationarity argument is exact **only if that outer field is a stationary sample**. No independent thermalization of inner chains is assumed for the identity: if the starting outer field is exactly sampled from the conditional law, invariant restricted sweeps retain its law. For practical variance and mixing diagnostics, vary inner sweeps and number of independent outer draws.

At each outer configuration, compare a single direct `O(t)O(s)` product against the product of inner estimates from different slabs, retaining outer configuration as the bootstrap unit. Subtract `E[O]^2` by *cross-chain* vacuum-product estimates during ensemble analysis; do NOT square a noisy conditional mean for the disconnected contribution. Inner updates are NOT independent outer fields. Avoid the same-slab product-of-means shortcut, which would generally be biased. Six cross-slab pairs and 16 channel pairs are saved.

The package checks frozen-link bitwise invariance, initial/final recomputed plaquette caches, catalogue hashes, coverage, and source linkage. Original checkpoints are read-only. It uses four physical scalar channels from the complete Stage 19 catalogue and does not change the gauge updater.

## Local execution

Extract `Penrose_YM_Stage21_Full_Lattice_Scalar_Slab_Prototype.zip` into your QCYangMills folder (archive root `stage21_full_lattice/`). From `stage21_full_lattice/deps/stage19_complete`:

```
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 NUMBA_NUM_THREADS=1 python3 -m unittest -q test_stage21
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 NUMBA_NUM_THREADS=1 \
 python3 stage21_scalar_multilevel.py --kind square --seed 101 \
 --checkpoint ../../../ym_stage9/checkpoints/square_nt20_seed101.npz \
 --cache stage19_complete_catalogues --output stage21_smoke --inner 4 --inner-sweeps 1
```

**Path correction:** The above relative checkpoint path depends on where you extract the archive. Check with `ls` before running; preferably use an absolute `--checkpoint /Users/.../QCYangMills/ym_stage9/checkpoints/square_nt20_seed101.npz` path. Penrose uses `--kind penrose` and `penrose_nt20_seed101.npz`. Do not run against `restart.npz` unless it contains the required field and plaquette arrays and its state is appropriately tagged. The package does not run new outer sweeps or automatically launch an overnight simulation.

## Measured engineering checks (this environment, not Apple M1)

* Square seed 101, one restricted full sweep and K=1: 1,185,652 active links, 0 cache discrepancy, 13.5 s including geometry and JIT overhead.
* Penrose seed 101, one full restricted sweep and K=1: 1,186,016 active links, 0 cache discrepancy, 13.8 s including geometry and JIT overhead.
* Square seed 101, K=4, one sweep between measurements: zero cache discrepancy, 22.0 s including startup.
* The attempted sequential K=4 Penrose call was not completed/confirmed before the tool time limit. No claim about its runtime.

## Admission gates before physics

1. Independently check scalar loop gauge invariance and full catalogue source hashes on both geometries (prior Stage 19 measurement checks are available but do not independently certify this new full conditional process).
2. Multiple *independent outer gauge fields per chain* and a stationary-ensemble validation of direct/conditional agreement at all cross-slab pairs.
3. Inner mixing and autocorrelation vs inner sweep count; multiple independently seeded conditional trajectories; cost-adjusted variance per effective outer configuration.
4. Cross-chain vacuum subtraction; chain/block-aware covariance of connected channel-correlator matrix; held-out basis selection.
5. Rotate the slab boundaries/time-origin to gain more t values and control finite Nt effects; four slabs of width five do not suffice to fit a scalar mass.

### Physical limitations

The fixed 4x5 slab arrangement provides cross-slab time separations 5,10,15, not a three-point effective-mass sequence at t=2..6. This is a **conditioning and cost engineering benchmark only**. The Stage 19 operator construction still lacks an exact 5-fold symmetry projection on the finite Penrose periodic approximant. This package does not establish a glueball mass, string tension, or continuum difference.
