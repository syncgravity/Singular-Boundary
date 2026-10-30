# Stage 19 — deterministic full-anchor scalar projection and engineering benchmark

This package is **read-only** and requires the existing final Stage 9 checkpoints. It introduces **one rooted face-connected loop shape per face anchor per family**, with families of 3, 5 and 8 faces. Each face anchor is represented once in each family; **it does not integrate over every shape, rotation, or geometrical orbit at that anchor**. Accordingly it is a full *face-anchor* average of a particular deterministic operator design, not a mathematically complete shape-average, and not automatically the same physics on two regulators. This is important in the M55 rational-model-set Penrose regulator.

## Reproduce

From this directory in an environment with numpy, scipy, numba:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 NUMBA_NUM_THREADS=1 python3 -m unittest -q test_stage19_full
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 NUMBA_NUM_THREADS=1 python3 stage19_full.py --kind square --inputs ../ym_stage9/checkpoints --output results
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 NUMBA_NUM_THREADS=1 python3 stage19_full.py --kind penrose --inputs ../ym_stage9/checkpoints --output results
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 NUMBA_NUM_THREADS=1 python3 area_orientation.py --kind square --inputs ../ym_stage9/checkpoints --output results
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 NUMBA_NUM_THREADS=1 python3 area_orientation.py --kind penrose --inputs ../ym_stage9/checkpoints --output results
```

The source checkpoint files are not changed; all outputs go to `results`.

## Empirical results on the supplied seed-101 checkpoints

| Metric | Square | Penrose M55 |
|--|--:|--:|
| Spatial face anchors, per family | 22,801 | 22,808 |
| Total three-family loop evaluations per time slice | 68,403 | 68,424 |
| Rejected face anchors | 0 | 0 |
| Maximum tested gauge-transformation trace discrepancy | 9.99e-16 | 5.55e-16 |
| Compile-warm full measurement, 20 timeslices | 1.033 s | 0.863 s |
| Geometry setup | 4.83 s | 4.51 s |
| Catalogue construction | 3.29 s | 3.01 s |
| Common area × 4-fold orientation occupied bins | 6 | 20 |
| Bin evaluation including first-time JIT compilation and normalization rechecks | 4.86 s | 4.84 s |

The 128-path timing of ~3 seconds includes JIT compilation and is **not** a cost of each small batch. Timings refer to this container, not Apple M1. Peak process memory was not measured. The binning was checked by recomputing the direct full-family average from count-weighted bin means to tolerance 2e-12. Deterministic catalogue and all-anchor coverage tests passed (4 tests).

## What the test validates

- All spatial **face roots** represented in 3, 5, 8-face families, with simple closed boundaries and deterministic generation.
- Spatially averaged gauge-invariant traces on all 20 timeslices.
- Common physical-area boundaries `[0,1.0,1.4,1.8,2.2,2.6,3.0,∞)` and an illustrative fourfold orientation label on `[0,π/2)`.
- Face-root normalization; stratified bins exactly recombine into the overall projection.
- Feasible evaluation cost on a saved 1.37-million-link gauge field once compiled.

## Outstanding gates before a 24-hour production run

1. **Orientation convention and loop-shape bias:** the reported boundary-edge fourfold angular moment is an engineering descriptor, **not a demonstrated matched representation of square and Penrose rotations**. Some symmetric shapes have ill-conditioned orientation. Root-based deterministic BFS favors vertex/edge indices, potentially biasing the shape. A physically matched, symmetry-averaged operator definition should precede admissions claims.
2. **Physical matching:** common numerical area bins are not proof of operator or renormalized-scale equality across geometries. Occupied bins differ: square 6 and Penrose 20.
3. **True operator overlap:** no new Monte Carlo configurations were generated, so no connected temporal cross-correlators or glueball mass fits can be inferred.
4. **Mac resource check:** use a single-chain smoke test to measure Apple M1 peak RSS, compilation, actual post-JIT time, and restart correctness. A short additional-configuration test across independent chains should validate signal behavior before a 24-hour run.

The design is intentionally **fail-closed**: it does not claim a scalar mass, gap improvement, or physical string tension.
