# Exact weighted SU(2) domino-loop mean and fourth connected subtraction

For finite original-link planar SU(2), K=−Σ_e a_e Δ_e and V=Σ_(k≠f)b_k(1−p_k). Two adjacent retained elementary faces A,B sharing original link e have electric eigenvalues ε_A=(3/4)Σ_{u∈∂A}a_u, ε_B similarly; c_X=b_X/ε_X; γ_AB=ε_A+ε_B−3a_e/2. Then the **exact second-order leading mean coefficient** for the two-face exterior Wilson trace r_AB is

[λ²] E_νλ[r_AB] = c_A c_B(1/4 + 3a_e/(16γ_AB)).

The proof combines the mixed second log-vacuum term Q_AB=c_Ac_B a_e[(3/(4γ_AB)+1/(4β_AB))r_AB−p_Ap_B/β_AB], β_AB=ε_A+ε_B+a_e/2, with density coefficient Q+2F² and exact product Haar identities E(r_AB²)=1/4, E(r_AB p_Ap_B)=1/16. The β terms **cancel algebraically**, a nontrivial simplification. Odd powers vanish by global SU2 central parity; remainder is fixed-volume, not uniform.

For face-disjoint dominoes AB and CD, the exact [λ⁴] subtraction E[r_AB]E[r_CD] equals the product of the respective local λ² coefficients. For uniform a=b=1, ε=3, γ=9/2, the single mean coefficient is 7/216 and fourth-order subtraction is 49/46656, matching an independently solved original-link two-face recursion.

**Open:** The raw [λ⁴] E[r_AB r_CD] for two face-disjoint but original-link-adjacent dominoes remains unknown. No fourth mixed coefficient, physical-coupling covariance, signed-current estimate or 3D Yang–Mills mass gap is claimed.

Full proof and exact SymPy verifier: Library /The Singular Boundary/Proof Audits/R3_IR_WEIGHTED_DOMINO_MEAN_SUBTRACTION_2026-10-31.zip.