# R3-IR — Weighted L4 calculus and third-order three-distinct-bond closure (2026-11-02)

**Status:** Conditional on previous certified pointwise weighted Bochner curvature κ_alpha≥11/120, uniform dressed spectral gap κ=23/144, and full-future conditional Poincare gap κ. The detailed complete proof is in the corresponding Library audit.

A pointwise Bochner/Kato inequality for weighted gradient magnitude yields ||∇P_t f||_{w,L4}≤e^(−11t/120)||∇f||_{w,L4}, hence ||∇R f||_{w,L4}≤B||∇f||_{w,L4} with B=120/11. Separately P_t Q has L2 norm≤e^(−κt) and L∞ norm≤2, so Riesz–Thorin gives ||P_t Q||_4≤sqrt(2)e^(−κt/2) and ||R f||_4≤2sqrt(2)/κ||f||_4.

For a residual bond |w_i|≤v=1/1152, |∇w_i|≤G=√21·67/13824, set u_i=Rw_i, A=2sqrt(2)v/κ≈0.01537189. Then ||u_i||_4≤A and ||∇u_i||_{S_i,w,L4}≤BG. For two bonds i,j, S=S_i∪S_j, Hölder/Leibniz imply ||∇(u_i u_j)||_{S,w,L2}≤2ABG≈0.007448974.

For third bond k to their right, exact prefix centering P_k w_k=0 and full-future conditional Poincare give
|〈Rw_i,w_k Rw_j〉|=|〈w_k,u_i u_j〉|≤v κ^(−1/2) 2ABG (5/6)^d ≈**1.6179358603e−5 (5/6)^d**, d=distance of future links beyond k to S. This controls both middle-insertion terms. The preceding full-product ordered-chain estimate controls the other four terms with coefficient 7.8436995729e−6 each. Their six-term sum is bounded by 6.37335155e−5(5/6)^d when k is the isolated extremal bond. Reflecting the open straight strip permits the same argument when the *leftmost* bond is isolated. Selecting the larger of the two gaps thus gives conditional diameter decay up to fixed finite link-geometry support offsets for three **distinct** bonds.

**Cautions:** Pointwise weighted Bochner inequality is an analytic input not independently computer verified. Exact geometric conversion of index gap to link-distance should be tracked in applications. Repeated bond labels, all-orders connected expansions, full interacting λ=1 gap, and continuum Yang–Mills mass gap remain open. The arithmetic verifier tests constants only. Complete proof, script, log, hash manifest are archived in Library /The Singular Boundary/Proof Audits.