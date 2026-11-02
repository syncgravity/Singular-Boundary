# R3-IR — Ordered third-chain weighted product bound (2026-11-02)

Under the previously audited dressed SU(2) weighted Bochner, full-future conditional Poincaré and prefix-gradient commutator bounds, for residual bonds i<j<k, R=L_N^{-1}Q and P_j old-prefix conditioning, the **specific ordered chain**
[
langle w_k,RQ(w_jP_jRw_i)angle
]
has a physical-distance bound. Define S=S_i∪S_j, let d be distance from S to the future-link region at bond k, and use ρ=6/5, v=1/1152, κ=23/144. The first projected response satisfies
[
|
abla P_j Rw_i|_{S_i,logρ}le C_v|
abla w_i|_2,quad
C_v=120/11+ρ(sqrt3/24)[1440/(11sqrt{23})]approx13.2730313.
]
The product-gradient Leibniz estimate with conservative sup gradient bound G=√21·67/13824≈0.0222101 gives
[
|
abla(w_jP_jRw_i)|_{S,logρ}le vC_vG+Gv/κapprox 0.000376606.
]
Finally exact conditional centering P_k w_k=0 and weighted-gradient/Poincaré transfer imply
[
|langle w_k,RQ(w_jP_jRw_i)angle|
 le [v,1440/(11sqrt{23})],[vC_vG+Gv/κ],(5/6)^d
 le 8.924	imes10^{-6}(5/6)^d.
]

**Scope:** This handles one centered ordered third-order chain with its last bond to the right; it does not bound the other pieces or permutations, and it does not establish connected third-order diameter decay, nonlinear convergence, the interacting λ=1 gap or continuum Yang–Mills mass gap. Numerical checker validates only constants, with analytic input taken from previously archived SU(2) geometric estimates. Full report, verifier, log, and SHA256 manifest in Library /The Singular Boundary/Proof Audits.