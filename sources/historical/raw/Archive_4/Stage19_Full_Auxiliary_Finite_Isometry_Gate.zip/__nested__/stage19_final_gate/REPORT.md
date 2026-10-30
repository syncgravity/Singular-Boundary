# Stage 19 — Full strict auxiliary and finite-isometry gate

Square: 22801/22801 roots; Penrose: 22658/22808 roots. Threshold **1.5** unchanged, and Penrose unmatched mask matches the previous independently certified 150 exactly.

All 20 timeslices on the saved seed-101 gauge field were measured for the matched auxiliary and each of the 3 complete full-volume rooted controls. The auxiliary treats uncovered anchors explicitly: `aux_unconditional` uses 1/F weights and includes zero contributions for missing roots; `aux_conditional` is normalized by accepted count. Neither should silently be substituted for a complete zero-momentum scalar.

## Single-field means

| Geometry | auxiliary (conditional) | controls (3,5,8 faces) |
|---|---:|---|
| square | 0.87437282 | 0.66222635, 0.82900537, 0.93098576 |
| penrose | 0.92203917 | 0.69063645, 0.85033006, 0.95143921 |

## Finite periodic symmetry classification

The Penrose torus periods imply absolute entrywise bounds on every integer period-coordinate Euclidean orthogonal action: [[1.0, 0.993946], [1.006091, 1.0]]. Therefore every such action has integer coefficients in [-2,2], a subset of the enumerated [-3,3] GL(2,Z) candidates. Only four orthogonal linear actions survive: identity, half turn and two reflections.

For each linear action we enumerated all 832 possible images of a rare-degree reference vertex and tested vertex uniqueness and edges for each surviving candidate. Only the identity at zero translation survived. This exhausts **Euclidean affine graph isometries** of the stored Penrose periodic geometry, not every abstract graph automorphism.

## Admission decision

**Not yet admitted as a full scalar production measurement**: 150 unmatched Penrose roots remain, orientation distributions are imbalanced, and the present one-loop-per-root target rule is not an exact symmetry orbit average. Full-volume controls must remain the spectroscopy reference; auxiliary should be carried as an explicitly masked diagnostic. No 0++ mass is extracted.

## Reproducibility

`run_full_gate.py` (square) and `run_penrose.py` (Penrose), `symmetry_gate_fast.py`, `make_report.py`, and arrays document the numerical screen. Dependencies remain in the prior `stage19_target_first` and `stage19_full_projection` packages; scripts reference `/mnt/data` source paths. The final output is a reproducible measurement record, not a standalone installable Mac runner.
