# R3-IR-592 — All three connected M5 spin-1 single-plaquette electric diagonals

Date 2026-10-31. This is a deterministic exact-degree **partial** calculation for the 31-state space in R3-IR-584, not its full 31×31 electric matrix.

Use rooted tree gauge on the M5 candidate 3D prism; select plaquettes A=4, B=29, D=33. Each has exactly two non-tree SU2 chords. Evaluate SU2 Haar using the independent 24-cell design on each chord (24²=576 nodes). Take full K=(M5_mass3d)^-1 with mixed couplings between all four edges in each plaquette, including tree-edge derivatives. Spin-half character χ_{1/2}=2 Re U and spin-1 character χ_1=4(Re U)²−1. Derivatives are computed by quaternion Lie insertion; polynomial degrees <=4 per chord in the quadratic electric integrand, safely inside 24-cell degree-five exactness.

| loop | j=1/2 electric | j=1 electric | cross |
| A (4) | 54.6941315502236 | 145.85101746726295 | 0 |
| B (29) | 75.5290875719122 | 201.41090019176588 | 0 |
| D (33) | 80.04311568867512 | 213.44830850313366 | 0 |

For each 3×3 Haar Gram of [1,χ_{1/2},χ_1], error from identity was zero at floating precision. The ratio E_{j=1}/E_{j=1/2}=8/3 to <5×10^-16 in all three loops, matching the quadratic Casimir ratio 2/(3/4); this exact-form finite Haar phenomenon does not imply multiloop kinetic diagonality or a full-lattice physical mass gap. A/B spin-half entries reproduce R3-IR-567 and D reproduces R3-IR-591.

Careful distinction: in the *31-state basis* the corresponding spin-1 diagonals are a subset of required entries. Cross couplings to other states of the same three-center parity remain unknown. 31-state Ritz eigenvalues and gap **not calculated**.

The independent script `audit_three_connected_spin1_diagonals.py` and machine-readable outputs `m5_three_connected_spin1_electric_2026-10-31.json` are in Library /The Singular Boundary/Source/. Next: systematically contract all center parity blocks (or derive representation-theoretic exact simplifications), verify the 17-state overlap and magnetic matrix, then compute gap. Independently, the cubical full Gauss-invariant strong-coupling gap from R3-IR-589 is not uniform in refinement, and finite transfer positivity R3-IR-590 does not supply continuum existence. No continuum Yang-Mills mass gap proved.
