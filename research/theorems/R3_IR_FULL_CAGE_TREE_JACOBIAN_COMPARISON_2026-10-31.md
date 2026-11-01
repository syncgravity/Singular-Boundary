# R3-IR — Full original-link Jacobian comparison for two SU(2) tree–cotree transports

**Date: 2026-10-31. Classification: exact finite-cage construction plus numerical Lie-Jacobian diagnostic, not a general tree optimality theorem.**

## Geometric construction

Use a planar 3×3 square-cell disk (16 vertices, 24 oriented original links and 9 bounded faces). Root the full planar dual at the exterior face. Select a breadth-first dual spanning tree or a depth-first dual spanning tree, each with its complementary primal spanning tree. The target is the central completed interior face (1,1). For each dual tree let e(f) denote the unique parent edge of bounded face f.

For a configuration U, form each oriented face Wilson word W_f(U) based at the lower-left vertex. Prescribe W_target^new = g W_target(U) and W_k^new = W_k(U) for all other bounded faces. Process faces in decreasing dual-tree depth, solving its parent-edge SU(2) variable uniquely from the oriented face word A U_e^{±1} B = W_f^new. Parent edges are all distinct; once a descendant face is solved, a subsequent ancestor edge is not on that descendant's boundary except if connected by a dual parent-child edge already assigned, so it cannot spoil the face holonomy. This defines a smooth, invertible map T_g preserving product Haar measure by sequential conditional Haar translations/inversions. It fixes every retained Wilson plaquette holonomy while left-multiplying the target holonomy by g. The explicit map depends on the dual-tree choice.

## Full Jacobian and electric metric

Compute the complete left-trivialized Lie-coordinate Jacobian J of T_g in all 3×24 link directions, including unchanged-link dependencies. Given positive electric coefficients a_e and diagonal A=diag(a_e I_3), define the quadratic-form metric defect M=J A J^T-A and electric-normalized largest positive eigenvalue d=max(0,lambda_max(A^-1/2 M A^-1/2)). Because unchanged tree link variables enter the solved parent-edge words, M can have nonzero rows/columns on unchanged edges.

## Reproducible finite-cage diagnostic

Two fixed seeded noncommuting configurations, randomized positive a_e in [0.7,1.3] and the same noncentral g=exp[(1.1,-0.8,0.5)·i sigma/2] were used for both trees. Finite-difference step 1e-6 in every original-link direction. Results:

| trial | tree | target dual depth | changed links | links in metric support | unchanged links in metric support | d |
|---|---|---:|---:|---:|---:|---:|
| 0 | BFS | 2 | 2 | 3 | 1 | 3.501068 |
| 0 | DFS | 5 | 5 | 9 | 4 | 37.282037 |
| 1 | BFS | 2 | 2 | 3 | 1 | 3.485351 |
| 1 | DFS | 5 | 5 | 9 | 4 | 41.990916 |

All retained holonomy residuals and the prescribed target holonomy residual were <2e-15 in quaternion Euclidean norm. The off-diagonal changed/unchanged metric blocks have nonzero Frobenius norm (1.49–1.74 BFS, 7.30–7.78 DFS). These d values are finite-difference estimates, not rigorous closed-form distortion bounds, and the observed BFS advantage is **sample- and tree-choice-specific**, not universal optimum.

## Consequences and open tasks

The diagnostic establishes concretely that optimizing dual route lengths can strongly reduce full Jacobian distortion on the same completed face, while confirming that full metric support exceeds the visibly modified links. It does not evaluate Q_g=⟨T_gΩ,(H_f^--E0)T_gΩ⟩ in the interacting vacuum, does not bound a general Penrose refinement family and does not imply any control of the signed radial current. A next calculation should test many configurations and alternative shortest-path ties, construct an analytically certified upper bound in terms of the tree structure, and estimate the signed vacuum metric defect. The continuum Yang–Mills mass gap is OPEN.