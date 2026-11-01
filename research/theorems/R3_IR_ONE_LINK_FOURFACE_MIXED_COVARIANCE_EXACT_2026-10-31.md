# Exact one-shared-link four-face SU(2) domino covariance coefficient

**2026-10-31.** Four consecutive retained square plaquettes, 13 original SU(2) links, unit electric and magnetic weights, two disjoint domino outer Wilson traces r_AB and r_CD sharing one boundary link. Exact rational result:

**[λ⁴] E_νλ[r_AB r_CD] = 1967237/1843845120.**
**[λ⁴] E_νλ[r_AB]E_νλ[r_CD] = 49/46656 = 1936480/1843845120.**
**[λ⁴] Cov_νλ(r_AB,r_CD) = 30757/1843845120 > 0.**
Thus Cov''''(0)=30757/76826880 and Cov=(30757/1843845120)λ⁴+O(λ⁶); lower and odd orders vanish.

The original-link electric operator in gauge-fixed quaternion face coordinates is K_S=3|S| I+2Σ_(i,i+1∈S)Σ_(a=1)^3 R_a^(i)L_a^(i+1), where R,L are right/left infinitesimal SU(2) quaternion rotations. It reproduces K(p_i p_(i+1))=13p_i p_(i+1)/2−r_(i,i+1)/2. Independent SU(2) face Haar makes quaternion coordinate moments δ_ab/4. Center-parity implies square-free vacuum recursion U_∅=1, U_S=K_S^(-1)Σ_(i∈S)s_i U_(S\{i}). The global-conjugation invariant multilinear tensor sector dimensions for 1–4 faces are 1,2,5,14, yielding **exact rational** linear solves, including all 24 insertion orders. Fourth density coefficient W_4=Σ_(S⊆{A,B,C,D})U_S U_(S^c), with exact tensor Haar contraction against r_AB r_CD.

**Verification:** Delete the central shared-link electric interaction: the same exact solver returns raw coefficient 49/46656 and connected coefficient **0 exactly**. Independent numerical 4^k matrix solver agrees at machine precision. Proof, exact SymPy verifier, separate numerical checker, JSON and SHA256 manifest: Library /The Singular Boundary/Proof Audits/R3_IR_ONE_LINK_FOURFACE_MIXED_COVARIANCE_EXACT_2026-10-31.zip.

Scope: the one-link straight 4×1 geometry only; parallel 2×2 two-shared-link geometry and arbitrary electric/magnetic weights remain unevaluated. No physical-coupling uniform covariance bound, unweighted signed-current estimate, or continuum 3D Yang–Mills mass gap is claimed.