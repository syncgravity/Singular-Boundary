# Common original-link martingale filtration and dressed form-resolvent decay — 2026-11-02

**Theorem conditional on previously certified local SU(2) dressing and spectator-inclusive one-step form bound.** On a finite straight open square strip, let nu_N be the product-of-isolated-plaquette dressed measure and E_j the 3j+1 original links through face j. Fresh-link Haar integration proves marginal consistency nu_N|E_j=nu_j. All P_j=E_nuN[·|E_j] are orthogonal projections in one L2(nu_N); their successive martingale increments H_i form an orthogonal decomposition, with full spectator dependence.

For F in H_i, the original-link generator L_N F depends on links through at most face i+2 because the electric part is link-local and the drift from the next face is the only future term sharing an old link. Therefore the symmetric Dirichlet form has E_N(H_i,H_j)=0 for |i-j|>=2. Adjacent off-diagonal form entries have the earlier certified relative bound eta=13/(144 sqrt(3))≈0.0521218993 for |g|<=0.001. Each diagonal increment has Poincare gap at least kappa_*=23/144 (first block from dressed curvature, later blocks from the conditional fresh-link gap 108/169).

After diagonal-form normalization, the off-diagonal nearest-neighbor form operator T has norm <=2eta=q≈0.1042437986<1. The Neumann form inverse therefore obeys
||Pi_i L_N^{-1} Pi_j||_L2 <= [kappa_*(1-q)]^{-1} q^|i-j|
on the centered dressed reference Hilbert space, uniformly in strip length and representation degree. The prefactor is approximately 6.98948.

**Scope:** This proves inverse decay between common-filtration martingale increments of the dressed reference dynamics. It does **not** prove fixed-support covariance decay of the physical interacting vacuum, residual-potential summability, interacting lambda=1 gap, or continuum Yang-Mills mass gap. Detailed proof and numerical checker are preserved in Library /The Singular Boundary/Proof Audits.