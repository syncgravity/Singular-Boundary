# R3-IR-526 — Actual M5 root-tree Wilson transport exposure audit (2026-10-30)

Source: archived Approximant(M=5), the actual eleven-face open disk edge IDs stored in global_whitney_11face.npz, inverse of its previously assembled 30x30 Whitney mass matrix. Root tree chosen **deterministically** by BFS from the smallest disk vertex (vertex 0), ascending neighbor order. The disk has 20 vertices and 30 edges, hence 19 rooted tree edges.

With the electric derivative D_j=Ad(V_j(U)) X_j based at the global root, V_j is the product of oriented link variables along the tree path from root to source(j). When a selected link e is a tree edge, dependence of an off-diagonal quadratic coefficient D_i·D_j on U_e can occur when e belongs to exactly one of the two paths. This is a necessary path-exposure mechanism, NOT sufficient to prove (I-P_e)H_E P_e nonzero on a gauge-invariant observable. Nonzero coupling K_ij is necessary for this specific cross term; cancellations between different pairs, derivatives of transport coefficients, and gauge invariance must be checked.

Numerical path exposure for off-diagonal |K_ij|>10^-6, both i,j different from e:
- e=0: tree edge, 125 exposed pairs, example (1,7) K_ij≈1.974868640760386e-6.
- e=1: tree edge, 151 exposed pairs, example (0,4) K_ij≈0.00648855383305473.
- e=4: tree edge, 144 exposed pairs, example (0,16) K_ij≈0.010175038954646769.
- e=13,86,88: non-tree edges, 0 such exposed pairs under THIS tree. They still couple directly via K_ej and may produce nonreducing action by a separate mechanism.
The inverse of the archived matrix has 866 ordered nonzero offdiagonal entries above absolute 1e-9 (threshold-dependent; earlier counts for a different threshold are not interchangeable).

The previously introduced toy three-link Wilson-transport counterexample R3-IR-525 demonstrates that the exposure mechanism can produce a genuine nonzero commutator. This M5 audit DOES NOT yet demonstrate it: the full differential operator must be evaluated on explicit gauge-invariant loop observables, with correct source conventions, derivative-of-transport ordering, and possible cancellations. Also note that the root path is a discretization/gauge choice; a physical conclusion must not rest on a freely chosen rooted tree without establishing the operator's path-choice prescription and covariance.

To proceed: implement an explicit gauge-invariant Wilson-function test on this disk, use automatic/analytic link SU2 differential operators rather than treating coefficients as constant, and check whether the result depends on the selected root tree. No uniform Penrose cap or continuum Yang-Mills mass gap proved.
