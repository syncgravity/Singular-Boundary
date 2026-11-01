# Exact rational shared-face fourth-order SU(2) domino covariance coefficient

2026-10-31. Finite original-link SU(2) square-lattice Wilson Hamiltonian with unit electric link coefficients and independent magnetic couplings t_A,t_B,t_C. For two overlapping domino outer-loop traces r_AB and r_BC sharing face B, with nonshared faces A,C nonadjacent:

**Straight three-face arrangement:**
[t_A t_B² t_C] E_ν[r_AB r_BC] (unnormalized squared-vacuum numerator) = **95056699/100926259200**;
[t_A t_B² t_C] Cov_ν(r_AB,r_BC) = **−30408901/100926259200**.

**Bent three-face arrangement:**
[t_A t_B² t_C] E_ν[r_AB r_BC] (unnormalized squared-vacuum numerator) = **5939647/6307891200**;
[t_A t_B² t_C] Cov_ν(r_AB,r_BC) = **−1901953/6307891200**.

In each case the exact normalization plus connected mean-product subtraction is **29/23328**, from normalization (1/36)(1/144)=1/5184 and product of means (7/216)²=49/46656. Vacuum recursion includes exact e_(2B)=−1/12 and the term −u_AC/12 in the repeated-face fourth-order amplitude. A primal spanning tree with one exterior chord per elementary face is required; arbitrary chord choices can fail to represent the actual plaquette holonomy. The rotationally invariant A B² C symmetric quaternion sector has dimension **8**, reduced from 14 general multilinear invariants. Final Haar integration uses E[B_iB_jB_kB_l]=(δijδkl+δikδjl+δilδjk)/24, not square-free 4-face pairings.

**Independent exact validation:** both geometries yield [t_A t_B]E[r_AB]=7/216 and [t_A t_C]E[r_ABr_BC]=1/144; the attempted preliminary chord reduction that failed the latter check was discarded. Full self-contained exact SymPy solver, original-link generator, verification results, SHA256 manifest, and detailed proof: Library /The Singular Boundary/Proof Audits/R3_IR_OVERLAP_SHARED_FACE_EXACT_RATIONAL_2026-10-31.zip.

**Scope:** these are exact signed coefficients of the repeated-*shared face* monomial only. Additional adjacent spectator face contributions t_A t_C t_X² have not been evaluated, and full uniform-weight fourth-order overlapping covariance remains OPEN. No physical-coupling clustering, signed-current estimate, or 3D Yang–Mills mass-gap result is claimed.