# R3-IR — Matrix Peter–Weyl projective algebra and edge-local Poisson closure

Date 2026-11-01. Finite original-link SU(2)^E theorem; does not establish all-orders polymer convergence or interacting mass gap.

For each link e, SU(2) irrep V_{n_e} has dimension d_{n_e}=n_e+1 and Casimir λ_{n_e}=n_e(n_e+2)/4. For multi-index n let d_n=∏_e(n_e+1), π_n=⊗_e π_{n_e}, |n|=Σ_e n_e. Write f=Σ_n Tr(A_nπ_n), and set ||f||_{Pρ}=Σ_n d_n exp(ρ|n|)||A_n||_1 (trace/nuclear norm), ρ≥0.

**Algebra:** ||fg||_{Pρ}≤||f||_{Pρ}||g||_{Pρ}. Proof: decompose the product of rank-one coefficient atoms under unitary linkwise Clebsch–Gordan transformations; orthogonal projected vectors satisfy Σ_l||u_l||||v_l||≤||u||||v||. The dimension and exponential output weights are bounded by products of input weights.

Let K=−Σ_e a_eΣ_{k=1}³ X_{e,k}², 0<a₀≤a_e≤a*, P₀=I−Haar, Γ_K=Σ_e a_eΣ_k(X_ef)(X_eg). Then

||K⁻¹P₀Γ_K(f,g)||_{Pρ}≤24(1+a*/a₀)|E(f)∩E(g)| ||f||_{Pρ}||g||_{Pρ}.

Proof: each CG output l on shared link e has exact multiplier (λ_{m_e}+λ_{n_e}−λ_{l_e})/2. Its normalized dimension ratio q=(l+1)/((m+1)(n+1)) satisfies q|λ_m+λ_n−λ_l|/2≤8(λ_l+1) for each CG triple with m,n≥1. If m≥2n, l≥m/2, λ_m+λ_n+λ_l≤9λ_l and q≤1. If n≤m<2n, l<3n, d_md_n≥(n+1)², and the crude bound λ_m+λ_n+λ_l≤12n² yields ≤6(l+1)≤8(λ_l+1), including l=0. If an input link label is zero, Γ_e=0. For any nonconstant multi-link output, denominator Λ_l=Σ_r a_rλ_{l_r} satisfies Λ_l≥a_e λ_{l_e} and Λ_l≥3a₀/4, so a_e(λ_{l_e}+1)/Λ_l≤1+4a_e/(3a₀). The normalized output multiplier is bounded by 8+32a*/(3a₀)≤24(1+a*/a₀). Other links satisfy CG dimension/weight contraction. CG Cauchy inequality takes the maximum multiplier and controls all output blocks. Locality removes edges outside E(f)∩E(g).

The central character norm of the preceding theorem differs: ||χ_n||_{Pρ}=(n+1)²e^{ρn}, not (n+1)e^{ρn}. Consequently boundedness at ρ=0 does not contradict prior character algebra obstruction.

Exact rational verifier checks all admissible triples m≤250 and singlet+spectator examples up to n=1024. Full report, source, execution log and SHA256 manifest in Library /The Singular Boundary/Proof Audits. Remaining: polymer support bookkeeping, repeated leaf insertions, three-face orientation audit, interacting λ=1 gap, and continuum mass gap; all open.