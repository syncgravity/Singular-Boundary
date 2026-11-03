# Gauss-adapted spin-network inverse and finite Temperley–Lieb recoupling audit (2026-11-03)

**Exact, volume-uniform theorem on the corrected physical original-link SU(2) ladder:** Let Ψ_α be an orthonormal original-link Gauss-invariant spin-network basis, with electric energy E_α=Σ_e j_e(j_e+1). Every nonconstant physical spin network contains a cycle of at least four nontrivial spin edges, each contributing at least 3/4, so E_α≥3. A fundamental plaquette Wilson loop saturates 3. Thus in the **original-link spin-network energy eigenbasis**, with ||F||_(SN,1)=Σ_α|F_α|,

**||K_phys^(-1)QF||_(SN,1)≤(1/3)||QF||_(SN,1)**,

and 1/3 is sharp, uniformly in finite strip volume. This is not the coefficient-l1 bound in the previous **uncoupled based-loop Wigner basis**, and it does not imply bounded nonlinear products or original-link connected polymer locality in the spin-network coefficient norm.

**Explicit invariant basis in all-fundamental loop Wigner blocks:** For t face loops of degree one, coefficient space is (V*⊗V)^⊗t, dimension 4^t, with V=C². SU(2) pseudoreality converts each V* to V; the residual Gauss invariant subspace is the spin-zero sector of V^⊗2t. Its dimension is the Catalan number **C_t=binom(2t,t)/(t+1)**. Noncrossing perfect matchings of 2t magnetic slots, each contracted by the antisymmetric SU(2) epsilon tensor, form an explicit Temperley–Lieb Gauss-singlet basis. Applying the inverse pseudoreality map on left magnetic slots gives coefficient vectors in the archived based-loop Wigner convention. Their Gram matrix G=B*B is positive definite; U=B G^(-1/2) is an orthonormal recoupled basis.

**Direct corrected-original-link finite-block verification:** Using all actual top, bottom and vertical original-link derivative fields, and NOT the invalidated nearest-neighbor ansatz, the checker constructs all Gauss singlets and physical restricted electric operators. It verifies the invariant Catalan dimensions and matrix inverse norms:

t | full dim | inv dim | min invariant E | Gram condition | inv-l1 in orthonormal singlets | inv-l1 in raw TL coordinates
1 | 4 | 1 | 3 | 1 | 0.333333333 | 0.333333333
2 | 16 | 2 | 4.5 | 3 | 0.234735911 | 0.222222222
3 | 64 | 5 | 6 | 18.111 | 0.200996415 | 0.166666667
4 | 256 | 14 | 7.5 | 187.48 | 0.191349040 | 0.139958592
5 | 1024 | 42 | 9 | 3008.7 | 0.193356263 | 0.165072011
6 | 4096 | 132 | 10.5 | 69671 | 0.203068362 | 0.171310149

The t=3 restricted physical spectrum is {6,8,8,10,13}, matching the independent ten-link audit. Exact integer Gram ranks/determinants were checked for t≤4; all Gauss residuals vanish to machine precision through t=6. The rapid conditioning deterioration is a feature of the *chosen nonorthogonal matching basis*, not a demonstrated impossibility of a stable orthonormal fusion-tree basis. The inverse-l1 samples do not prove an all-length bound in the recoupled coordinates.

**Remaining mathematical obligation:** Establish uniformly controlled multiplication, carré-du-champ and connected-polymer support structure constants in a chosen physical Gauss-invariant coefficient norm *compatible* with the diagonal or recoupled inverse. Otherwise the abstract diagonal coefficient-l1 bound is insufficient for a nonlinear fixed point. The previously archived non-gauge-invariant Wigner-column growth and nearest-neighbor polymer estimates do not settle this corrected physical question. Neither an interacting lambda=1 gap nor a continuum four-dimensional Yang–Mills mass gap is proved.

Full detailed mathematical report, standalone reproducible Gauss/Temperley–Lieb recoupling verifier, passing execution log and SHA-256 integrity manifest: The Singular Boundary / Proof Audits Library.