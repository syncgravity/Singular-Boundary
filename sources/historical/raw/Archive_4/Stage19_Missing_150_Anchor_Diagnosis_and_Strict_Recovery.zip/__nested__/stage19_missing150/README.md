# Stage 19 — Diagnosis of the 150 previously unmatched Penrose anchors

The original strict `all_anchors_strict_min_distance.npz` certificate identifies 150 failures at threshold 1.5 among 22,808 face roots. Their exact indices, original nearest-target distances, local face areas, face-neighbour means, and follow-up results are in `missing_anchor_diagnostics.npz`.

## Recovery without relaxing physical-shape acceptance

Running 8 deterministic growth variants for each face-cluster size 2–19 on the **original 150 failures only** finds at least one strict admissible loop at 149 locations. The last failure, root 10550, was resolved by testing 12 variants over sizes 2–25; its match has descriptor distance 1.2406834641, size 10 and target 4. All 22,808 face anchors now have a strict admissible *existence certificate* (the 22,658 previously accepted plus 150 recovered). This does not imply that one complete consistently weighted path catalogue has been assembled or gauge-invariance tested. Existing full-volume controls are unchanged.

## Local geometry and missingness

The original 150 missing face roots have mean area 0.290118 versus 0.325154 for the previously covered roots; 93/150 are among the three small-area classes (~0.233–0.239). The neighbour-area means differ as well. They consist of 142 connected components in face adjacency, largest 3, and 137 isolated roots. This is patterned local geometry, not 150 deleted lattice sites. Treat p-values in the JSON as **descriptive only**: spatially correlated faces are not independent data.

## Reproduction

Run `analyze.py` from the repository environment with `stage19_target_first` and `stage19_strict_expanded` restored under `/mnt/data`, then `last_anchor.py`. Both require only the previously supplied geometry, SciPy and NumPy, and saved strict-match certificate. They do not alter MCMC files, gauge links, or matching targets.

## Remaining gate

Generate and freeze a full spatial catalogue including each recovered loop, verify closed-loop gauge invariance and reproducible per-anchor weights, audit orientations, and benchmark measurement cost. Zero uncovered anchors eliminates *coverage-missingness*, but does not establish symmetry equivalence, better scalar overlap, or a physical 0++ mass.
