# All-length open-strip Wigner spectrum and overlap-sensitive same-radius Poisson estimate (2026-11-02)

Under the archived original-link orientation, K_t=4Σ_i L_i−2Σ_{i=1}^{t−1}C_(i,i+1), C_(i,i+1)=Σ_a R_a^(i)L_a^(i+1). Each shared-link coupling acts on a different left/right magnetic index from its neighbors, so the couplings commute. For degrees n_i, d_i the degree of face i in the path graph, and admissible coupled spins J_i, the **complete eigenvalue formula** is E=Σ_i(1+d_i/4)n_i(n_i+2)−Σ_i J_i(J_i+1). The centered gap is exactly 3, uniformly in finite interval length.

For nonconstant blocks N=Σ_i n_i, the magnetic coefficient-l1 inverse has the bound
**||K_t(n)^(−1)||_(1→1)≤[ (N+1)/2+6N²/(t(t+1)(t+2)) ]^(−1)**.
Proof uses the exact zero-spin condition C_(i,i+1)=0 if n_i n_(i+1)=0, the Neumann margin M≥Q+(N+1)/2, and the **sharp discrete Dirichlet inequality** Q=Σ n_i²−Σ n_i n_(i+1)≥6N²/[t(t+1)(t+2)], equality for n_i proportional to i(t+1−i). Thus inverse ≤2/(N+1) uniformly in t, or ≤A_t/N² with A_t=t(t+1)(t+2)/6.

For each fixed t and positive analytic radius σ, z=exp(−2σ), the full Wigner coefficient-l1 quadratic Poisson map is bounded at the **same** radius by
**C_(t,σ)=3(3t+1)A_t[1/(2(1−z)^t)+2t z(1+t z)/(1−z)^(t+2)]**.
At t=3 this reproduces the archived coefficient exactly.

**New overlap-sensitive refinement:** If interval inputs overlap in o faces and their union has t faces, all Clebsch–Gordan degree reductions occur only on the o overlapping faces, and at most 3o+1 shared original links contribute. The same bound holds with t replaced by o in the reduction generating factors and derivative-link count, but A_t retained. For disjoint *adjacent* supports (o=0), no degree reduction occurs and the sharper bound is **3A_t/4**, independent of σ. For genuinely separated supports Γ=0. This removes the spurious exponential-in-t estimate for merely touching inputs, but still leaves a polynomial t³ upper bound. No uniform connected-polymer convolution or physical lambda=1 contraction is established, and no interacting or continuum Yang–Mills mass gap is proved. Full mathematical proof, exact rational checker, passing log and SHA256 checksum are in Proof Audits Library.