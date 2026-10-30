# Stage 19 — Strict Penrose expanded-size recovery and finite-torus symmetry gate

## Reproducible recovery

The original full-lattice four-variant screen (`stage19_target_diagnostic/variants4_per_anchor.npz`) establishes the strict threshold-1.5 result at every one of 22,808 Penrose anchors for face sizes (3, 5, 8, 10). The enclosed `run_audit.py` regenerates the geometry and scans **all 753 failed roots** over expanded face sizes `(2,3,4,5,6,7,8,9,10,12,15)` and variants 0–3, using the same five targets and the same threshold. Its combined per-anchor minimum is logically identical to a full-volume expanded-size scan for the **binary pass/fail criterion**: on original passing roots the expanded search cannot turn a pass into a failure, and on original failing roots every expanded candidate is checked. The full expanded best-distance distributions at the original passing roots are *not* computed.  No gauge fields or Monte Carlo updates are used.

## Results

* Previous covered: **22,055 / 22,808** (96.70%).
* Newly recovered: **603 / 753** previously missed roots.
* Expanded strict coverage: **22,658 / 22,808 = 99.3423%**.
* Still missing: **150 / 22,808 = 0.6577%**. No imputation.
* Strict matching threshold: **1.5**, unchanged.

`all_anchors_strict_min_distance.npz` stores per-anchor minimum normalized descriptor distance, best size, best target and an uncovered mask. `REPORT.json` includes geom hash and preliminary isometry checks.

## Symmetry audit and limitation

The finite Penrose **periodic rational model-set M55** is not the infinite Penrose tiling. The candidate physical rotations through 72°, 144°, 216°, 288° are **incompatible with the fixed period lattice** (integer-period-coordinate error >=0.309), so treating them as exact global symmetry orbits would be invalid. The identity action was checked explicitly against the spatial vertex-edge graph. The origin-fixed reflection candidate is period-lattice compatible but *not* a vertex-edge automorphism in the checked origin convention. This **does not rule out a reflection with a nonzero spatial translation or a different axis**. Likewise a half-turn and other possible finite torus automorphisms are not exhaustively tested here. Consequently full physical point-group orbit averaging is **not certified**; orientation balance cannot be claimed merely by matching rotation-invariant area/perimeter/compactness descriptors.

The most defensible production protocol remains the **full-anchor scalar control** (the previous 3-,5-,8-face complete rooted catalogue, with equal anchor weighting) plus a **separately labelled target-matched auxiliary channel** with explicit coverage mask, area/perimeter/compactness target and orientation histograms. It would be inappropriate to call the restricted target-matched channel a complete zero-momentum operator when 150 anchors are missing. No scalar glueball mass, continuum limit or confinement-scale claim follows from this geometry-only audit.

## Reproduction

To rerun: place the `stage19_target_first` directory containing `stage19_full.py`, `target_first.py`, `diagnose_missing.py`, `full_anchor_targets.py`, and `vendor/` alongside this folder, and the prior `variants4_per_anchor.npz` in `stage19_target_diagnostic/`, then adjust absolute paths near the start of `run_audit.py` and execute `python run_audit.py`. The saved results and full code are supplied separately for inspection.
