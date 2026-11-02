# R3-IR — Residual martingale increments and quadratic response (2026-11-02)

Finite open square SU(2) strip, isolated-plaquette product dressed law nu_N. Write a_i=Re(U_i), r_i=Re(U_i U_{i+1}) in the audited opposite-link orientation, s_g=log psi_g, and w_i=−(1/2)s'_g(a_i)s'_g(a_{i+1})(r_i−a_i a_{i+1}), W_g=sum_i w_i. Independent central dressed face-holonomy variables and conjugation isotropy imply E[w_i|old original links through face i]=0. Therefore w_i belongs to the i-th martingale sector, and all distinct w_i are L²(nu_N)-orthogonal, even adjacent terms.

With M_g=E[s'_g(a)^2(1−a²)], isotropic vector covariance yields ||w_i||²=M_g²/12 and Var(W_g)=(N−1)M_g²/12 exactly. Previous |g|≤0.001 certification s'_g sup≤1/24 gives M_g≤1/576, ||w_i||∞≤1/1152, Var(W_g)≤(N−1)/3981312.

Under the preceding dressed-reference common-filtration inverse decay bound ||Pi_i L_N⁻¹ Pi_j||≤C q^|i−j|, q=13/(72√3)≈0.1042438, C=[(23/144)(1−q)]⁻¹≈6.989479, we obtain
|<w_i,L_N⁻¹ w_j>|≤ C M_g² q^|i−j|/12
and 0≤<W_g,L_N⁻¹ W_g>≤(N−1) C (M_g²/12)(1+q)/(1−q). The certified RHS per bond is ≤2.16419×10⁻⁶. This is *reference quadratic response*, not interacting vacuum connected covariance.

The product ground-state similarity transform yields physical finite-volume operator L_N+W_g+constant. Minmax and ||W_g||∞≤(N−1)/1152 give gap(H_N)≥23/144−(N−1)/576, positive for N≤92 but vacuous for N≥93. A uniform physical gap requires additional convergent reweighting/linked-cluster estimates. The interacting λ=1 and continuum mass gaps remain open.

Full proof, verification script, execution log, SHA256 manifest: Library /The Singular Boundary/Proof Audits.