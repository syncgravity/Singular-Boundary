# M5 seven-face: exact all-pairs second-order resolvent regression
Date: 2026-10-30. Status: 21 exact pair cases independently tested in Python against supplied penrose_study.zip; seventh-order amplitude UNEVALUATED.

S={1,2,3,4,7,8,10}, all a_e=1, physical SU(2) Casimir j(j+1). For g,k disjoint, T(p_gp_k)=6p_gp_k, and the squarefree subset coefficient F_{g,k}=p_gp_k/9. For adjacent g,k share a single edge with opposite oriented signs, set G=p_gp_k, U=p_(g union k); T G=(13/2)G-(1/2)U and T U=(9/2)U, whence F_{g,k}=(4/39)G+(4/351)U. Exact inversion verifies T F_{g,k}=(2/3)G in each case.

The reconstructed periodic M5 seven-face graph contains exactly 6 adjacent unordered pairs: (1,3) edge3; (1,8) edge14; (2,3) edge2; (2,4) edge5; (7,8) edge8; (7,10) edge12. The remaining 15 of 21 pairs are edge-disjoint. All orientations and exact rational identities passed in the executable validator. This extends the previous one-pair check across every two-face subset, providing a test fixture for the full 127-subset spin-network solver.

The verification is a second-order analytic regression, NOT a seventh-order coefficient evaluation, not evidence of nonzero Q_f response, and not a continuum mass gap proof.
