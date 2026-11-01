# Exact two-link original SU(2) domino covariance (2026-10-31)

**Unit electric and magnetic original-link Wilson Hamiltonian, four retained faces arranged as a 2×2 square; two horizontal parallel domino Wilson loops share two original links and no plaquette faces.**

Exact rational fourth coefficients obtained from a correct primal spanning-tree gauge reduction, four-face square-free resolvent recursion, and 14-dimensional invariant quaternion tensor contraction:

**Raw moment:** [λ⁴] E[r_bottom r_top] = 1383961/1261578240.

**Connected subtraction:** [λ⁴] E[r_bottom] E[r_top] = 49/46656.

**Connected covariance:** [λ⁴] Cov(r_bottom,r_top) = **19667/420526080** ≈ 0.000046767610703241044 > 0.

A necessary geometry check shows why naively applying the 4-chain face generator to a cyclic 2×2 adjacency graph is wrong: that operator does not give eigenvalue 6 on the eight-link exterior Wilson loop. The exact 12-original-link kinetic operator is built from the tree of six vertical and two middle-row horizontal edges; four top/bottom horizontal chords carry the independent face holonomies. Each tree edge contributes the quadratic differential generator on **all** chords with endpoints in its descendant vertex subtree, including both-sided conjugation. This exact kinetic operator reproduces both two-face exterior-loop eigenvalues 9/2 and the full eight-link boundary eigenvalue 6 with zero residual.

The square-free four-face vacuum coefficient is computed with exact rational polynomial linear solves in invariant quaternion tensor spaces of dimensions 1,2,5,14 and fully includes 24 insertion orderings plus 2u₁u₃ and u₂². An independent 256-dimensional numerical solve gives 4.676761070324109×10⁻⁵, within floating-point accuracy of the rational result, with max linear-system residual below 2.3×10⁻¹⁶.

With the previous straight-chain one-shared-link coefficient 30757/1843845120, **both geometries of disjoint, original-link-adjacent domino Wilson covariance now have exact positive unit-weight fourth-order coefficients**. No arbitrary-weight sign, physical-coupling convergence, signed current, or continuum Yang–Mills gap is claimed.

Complete proof, exact SymPy and independent numeric verifiers, results, SHA256 manifest: Library /The Singular Boundary/Proof Audits/R3_IR_TWO_LINK_FOURFACE_MIXED_COVARIANCE_EXACT_2026-10-31.zip.