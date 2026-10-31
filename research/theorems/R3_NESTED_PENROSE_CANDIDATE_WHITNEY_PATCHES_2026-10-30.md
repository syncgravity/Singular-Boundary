# R3-IR-557 — Nested Penrose disk construction: six actual candidate Whitney assemblies

Date: 2026-10-30. **Completed geometry-and-matrix construction, NOT an h→0 physical refinement sequence.**

## Provenance and algorithm

Recovered archived geometry from ChatGPT Library `/The Singular Boundary/Source/Archive 4.zip` via `penrose_causal_study.Approximant(M=5)` and `wilson_torus.penrose_faces`. Start at actual deleted face 0, and build concentric nested patches by expanding each face's edge-sharing adjacency neighborhood to radii 1 through 6. Compute all active edge and vertex sets. Form the quadratic bilinear Whitney/Nédélec *candidate* mass matrix on each four-sided face by mapping the canonical oriented unit-square edge basis `[(1−v,0), (0,u), (−v,0), (0,−(1−u))]` with affine Jacobian `Qpar[:,[axis_a,axis_b]]`, signed global edge incidence, and tensor Gauss-Legendre quadrature (3×3). The quadrature is exact for these polynomial integrands. Verify each assembled matrix symmetric positive definite. Build a tree with face-0 edges other than edge 13 inserted first, then other edges except edge 13 by Kruskal, so that face 0 has one chord.

## Computed rows

| Face radius | Faces | Edges | Vertices | lambda_min | lambda_max | condition | M_13,13 | rho, g2²=1 and b=3/32000 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 5 | 15 | 11 | 0.165375053 | 1.965260223 | 11.883656 | 0.694741427 | 0.0001736854 |
| 2 | 14 | 37 | 24 | 0.173685357 | 2.281306457 | 13.134708 | 0.694741427 | 0.0001736854 |
| 3 | 28 | 67 | 40 | 0.173685357 | 2.399516424 | 13.815306 | 0.694741427 | 0.0001736854 |
| 4 | 46 | 106 | 61 | 0.192943964 | 2.434333014 | 12.616788 | 0.694741427 | 0.0001736854 |
| 5 | 70 | 158 | 89 | 0.173685357 | 2.434626283 | 14.017453 | 0.694741427 | 0.0001736854 |
| 6 | 96 | 213 | 118 | 0.165375053 | 2.434673750 | 14.722134 | 0.694741427 | 0.0001736854 |

In every row edge 13 has exactly two incident patch faces (deleted f0 and retained f10), is non-tree by construction, and face 0 contains exactly one chord. The mass diagonal M_13,13 remains fixed because precisely the same two incident cells contribute to it at every radius; **this does not imply physical refinement stability**. At radius 1 and larger the selected magnetic model has only f10 depending on chord edge 13, as in earlier finite proof assumptions. The root tree differs from the historical rooted BFS tree but obeys the protected-chord criterion.

## Authentic historical matrix discrepancy

The real archived original `global_whitney_11face.npz` (SHA-256 d7bd716dcfa5ef640aabb824099ad614b4d64bfb781a3cbf4cc484bb8e902fbf) was defined on another selected eleven-face disk, with edge 13 diagonal **0.777859028095** and spectrum approximately [0.14317415, 1.10465934]. This candidate assembly gives **0.694741426782** on this edge and does not reproduce the original prescription. Do not mix the original M5 matrix with these candidate matrices or claim historical-model validation. In particular the generated patch sequence is not a sequence of lattice-spacing values h→0; it is a sequence of nested face sets at a single `Approximant(M=5)` geometry and a single physical scale.

The example `rho=8|b|M_ee/(3g2²)` is computed only under **arbitrarily fixed illustrative values** g2²=1 and b=3/32000; it does not test physical Yang–Mills coupling renormalization. It is *not* a proof of a uniform continuum relative cap, thermodynamic limit, or mass gap.

## Provenance and recovery

The executable full construction script is persisted in ChatGPT Library `/The Singular Boundary/Source/build_penrose_nested_patches.py`. Results are `penrose_nested_patch_candidate_results_2026-10-30.json` and `penrose_nested_patch_candidate_data_2026-10-30.npz` in that same Library folder. Neither data NPZ nor other binary payloads are committed to Git. This note and the claims ledger are text-only Git checkpoints.

## Next physical construction obligation

Construct independent approximants M=5,7,9,... or a geometrically calibrated inflation/refinement hierarchy with explicit cell lengths h_M; fix the historical Whitney integration normalization (or approve the alternative as a *different* model); map the same physical/local face across levels, construct reproducible rooted trees, and supply **physical** g2²(h), b(h). Check mass-spectrum conditioning and face-adjacent local mass scaling across those genuine levels. The absence of that calibration must not be hidden by the fixed-volume patch experiment.
