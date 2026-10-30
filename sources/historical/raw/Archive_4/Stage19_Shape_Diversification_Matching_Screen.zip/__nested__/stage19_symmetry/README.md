# Stage 19 — Root-balanced shape diversification and geometry-matching screen

This read-only engineering pilot uses **two candidate shapes per face root** in each of the 3-, 5- and 8-face scalar-loop families. Multiple deterministic growth priorities reduce reliance on the previous single adjacency-order breadth-first shape. A boundary-valid BFS fallback guarantees every root is represented. Identical clusters are deduplicated **only within a root**, then weighted so each root contributes exactly 1/F per family. This is **not** an unbiased sample of all connected lattice animals or a complete rotation-orbit average.

`stage19_symmetry.py` checks shape area and dimensionless isoperimetric compactness, `4π area / perimeter²`, with bins defined in the same numerical units for both geometries. Those are invariant under planar reflection and rotation but **do not establish symmetry equivalence** of the actual spatial path operators. This screen does not equate C4 and fivefold Penrose orientational symmetry; that requires a further regulator-aware operator study. No physical scale conversion is performed.

## Reproduce

```sh
cd stage19_symmetry
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 NUMBA_NUM_THREADS=1 python3 -m unittest -q test_stage19_symmetry
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 NUMBA_NUM_THREADS=1 python3 stage19_symmetry.py --inputs ../ym_stage9/checkpoints --output results --variants 2
```

Add `--measure` to compute per-family unweighted spatial averages on each supplied final field. They are **not** already root-weighted or matched-stratum measurements; root weights and geometry fields are included with the output for developing that observable. The script never modifies input checkpoints. An earlier four-variant trial was too expensive for quick iterative tests; two variants are the validated screening setting.

## Empirical screen on seed 101

- Square: 113,801 rooted loops; 3 family root-weight sums all 1.0; 15.3 s catalogue build.
- Penrose M55: 113,509 rooted loops; 3 family root-weight sums all 1.0; 13.7 s catalogue build.
- Six populated common `(family, area bin, compactness bin)` strata. Fraction of total family-normalized root weight covered: square 100%, Penrose 53.6%.
- Substantial unmatched Penrose weight means this design **fails as a fully matched physical basis**. A root-normalized, within-common-support projection can be defined later, but must be labeled a restricted operator and cannot be treated as a complete Penrose scalar projection.
- The `invalid` counter reports rejected candidate-growth attempts (some rescued by fallback); it is *not* an anchor-rejection count.

## Decision and next gate

The shape-diversification and root-normalization engineering is verified; the common-support geometry-matching **gate fails**. Before a new 24-hour run, improve cross-geometry overlap in the **joint area, perimeter, compactness and orientation distributions**, specify and test a regulator-specific symmetry average, and validate gauge invariance and computational cost of **weighted per-stratum timeslice observables**. No scalar mass or improved physical overlap is claimed.
