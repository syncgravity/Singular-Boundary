# Full two-face Wigner matrix-coefficient module and same-radius Poisson estimate

**The Singular Boundary, 2026-11-02.** On adjacent SU(2) faces A,B, the correctly oriented original-link electric operator is K=4L_A+4L_B-2C, with C=sum_i R_i^A L_i^B. Its full (j,k) Wigner degree block couples one right magnetic index of A and one left magnetic index of B. The shared coupling is unitarily represented by -sum_i J_i^(j) tensor (J_i^(k))^T. Standard SU(2) spin addition gives exact eigenvalues

**E(j,k;J)=5/4[j(j+2)+k(k+2)]-J(J+1)**, J from |j-k|/2 to (j+k)/2 in unit steps, each with multiplicity (j+1)(k+1)(2J+1). The centered spectrum starts at 3. The fundamental (1,1) block reproduces 11/2 and 15/2. The original-link quadratic identities Gamma(a,b)=(ab-r)/4, K(ab)=11ab/2+r/2 and K(r)=15r/2, r=Re(AB), follow directly.

For the **unnormalized Wigner coefficient** norm ||f||_Wσ=sum e^(σ(j+k)) |f^(j,k)_(mn;pq)|, σ>0, magnetic-spin column sums give ||K_(j,k)^(-1)||_(1→1) ≤ 4/[1+(j+k)^2] on nonconstant blocks. This is degree preserving and uniform.

**Full two-face bilinear theorem:** For all coefficient arrays in Wσ and z=e^(−2σ), the centered quadratic Poisson map obeys
||K^(-1)Q Gamma_K(f,g)||_Wσ ≤ [24/(1−z)^2 +192z(1+2z)/(1−z)^4] ||f||_Wσ ||g||_Wσ.

Proof: each original-link generator has Wigner coefficient-l1 norm at most its PW degree; the two-face Gamma formula costs at most 12N_fN_g per input pair. Wigner Clebsch–Gordan multiplication yields at most one coefficient per output bi-degree (j_f+j_g−2r_A,k_f+k_g−2r_B), each CG product modulus at most one. At total output degree N=N_f+N_g−2r, the inverse contributes 4/(1+N²), and 48N_fN_g/(1+N²) ≤24+96r². Summing over r_A,r_B≥0 with weight z^(r_A+r_B) gives the stated explicit constant. The constant-output block is removed by Q.

This is a theorem for the complete **fixed two-face** Wigner matrix-coefficient Banach algebra, not for growing connected polymers. It does not prove λ=1 contraction, a uniform interacting spectral gap, or a continuum Yang–Mills mass gap. Full mathematical proof, independent full-block verifier and SHA-256 manifest are preserved under The Singular Boundary / Proof Audits.