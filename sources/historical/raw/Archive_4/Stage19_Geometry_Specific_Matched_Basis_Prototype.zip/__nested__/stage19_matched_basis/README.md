# Stage 19 — Geometry-specific common-support scalar basis

This engineering prototype uses the exact root-balanced two-variant connected-face catalogues from Stage 19 and constructs *two different geometry-specific coefficient vectors* whose probability distributions on predefined bins of **(family, absolute area, compactness, absolute perimeter)** are identical. The coefficients depend only on the geometry, not on gauge fields, measured Wilson values, or observed correlators. It does NOT claim equivalence of C4 square and Penrose rotational representations or physical scalar-state overlaps.

## Empirical result (seed-independent geometry, M55 vs 151x151)

- Five joint descriptor bins in common.
- Coupled probability mass: **0.35591973445** (sum of minimum original bin probabilities); only that fraction of the original complete descriptor distribution can be coupled without extra assumptions.
- Square original root-balanced probability retained on the supported bins: **0.666667**; Penrose: **0.503157**. These are *different* from coupled probability mass because one geometry can put more weight than the other into the same bin.
- After coupling and rescaling, square and Penrose joint-bin probabilities match to floating-point precision.
- Effective path counts after weighting: square ~74,724; Penrose ~41,185 (1/sum(weights^2)).
- Spatial-anchor coverage of retained paths: square 100%, Penrose 94.19%, but spatial weights are no longer uniform: matching changes the spatial projection.
- **3-face operator family entirely absent in common bins.** Family conditional weights after rescaling: 3 faces 0, 5 faces ~0.46993, 8 faces ~0.53007 for both geometries.

This is a **restricted matched-support operator**, NOT a complete, unbiased zero-momentum volume projector. The lost family and 64.4% coupled-mass deficit cause the *full scalar spectroscopy admission gate to FAIL*. Increased bin granularity including |cos(2 theta)|-style anisotropy harmonics will typically further reduce overlap; `--anisotropy-bins` is an available diagnostic, not an authorized physical match. The common bins do not prove same shape distributions inside each bin, nor equivalent gauge-field renormalizations, and no continuum matching has been performed. **Do not launch a new full Monte Carlo production run based on this screen alone.**

## Files

- `matched_basis.py`: builds both catalogues, computes anisotropy descriptors, constructs predeclared joint descriptor-bin coupling and weight vectors, and optionally evaluates weight-normalized per-family operators from a Stage 9 final field.
- `results/geometry_only.json`: actual matched-geometry output from the two real lattices (no gauge field needed).
- `test_matched_basis.py`: small synthetic tests of exact bin coupling and zero-support failure.
- `stage19_symmetry.py`, `stage19_full.py`, `stage19_pilot.py`, `vendor/`: frozen earlier code dependencies.

## Reproduce the geometry-only check

```bash
cd stage19_matched_basis
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 NUMBA_NUM_THREADS=1 python3 -m unittest -q test_matched_basis
```

The complete geometry check takes tens of seconds and is reproduced by the `construct(...)` call in `matched_basis.py`. For an optional checkpoint observation run:

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 NUMBA_NUM_THREADS=1 \
python3 matched_basis.py --inputs ../ym_stage9/checkpoints --output results --seed 101
```

**Runtime caveat:** This final full checkpoint-observation command has **not** completed in the current execution environment; an attempt exceeded the available execution window before saving data. The geometry-only calculation and its outputs have been executed, and the lightweight coupling tests passed. The gauge-field measurement function is supplied for subsequent benchmarking and needs an independent full-run validation before use for physics.

## Recommended next design gate

Instead of forcing a joint-binned match on the original unmatched catalogues, create **paired target loop-shape distributions in physical units from the outset** (area, length, curvature/aspect ratio, intrinsic orientation response), allowing each geometry to choose different face counts, and average full geometry-appropriate symmetry orbits. Report retained support, matching bias, spatial weighting and computational cost, and verify the resulting gauge-dependent operators on independent snapshots. Only then gather temporal correlators across configurations.
