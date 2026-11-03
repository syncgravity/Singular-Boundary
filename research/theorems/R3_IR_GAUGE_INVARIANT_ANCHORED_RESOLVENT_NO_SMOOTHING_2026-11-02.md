# Gauge-invariant anchored polymer resolvent: strict grading and no automatic smoothing (2026-11-02)

**Conditional theorem**, based on the archived original-link SU(2) open-strip face-coordinate model and the earlier fixed-source tame action.

Let X=A^s_(σ,κ,inv) and Y=A^(s+1)_(σ,κ+η,inv), with σ>0, η>0. The suffix inv denotes coefficientwise invariance under simultaneous conjugation of all face holonomies, the residual gauge action in the archived reduction. For χ_n(U)=tr_(n/2)(U), ||χ_n||_Wσ=(n+1)e^(σn). Each χ_n is a Wilson plaquette trace and hence residual-gauge-invariant.

**Explicit strict inclusion:** On I_t=[1,t], set F^(t)_(I_t)=2^(−t)(t+1)^(−s)e^(−κt−σt)∏_(i=1)^t χ_1(U_i), all other polymer components zero. The invariant norms satisfy **||F^(t)||_X=1** but **||F^(t)||_Y=e^(ηt)(t+1)**. An anchored sum over these nested intervals with factors (t+1)^(-2) supplies one explicit F∈X\Y. Spectral-degree strictness holds even on one face: choose F_{ {0} }=e^(−κ)Σ_(n≥1)e^(−σn)(n+1)^(−s−3) χ_n(U_0). Its X norm is Σ(n+1)^−2 finite, but its one-extra-moment norm is Σ(n+1)^−1 infinite.

**Covariance:** In the archived model K_t=4Σ_iL_i−2Σ_iΣ_a R_a^(i)L_a^(i+1); under simultaneous conjugation the three Lie generators at every face rotate by one orthogonal Ad_SU2 matrix, preserving each contracted edge coupling. Thus K,Q,Gamma and the centered inverse preserve the invariant subspace, and so does T_G(F)=K^−1QΓ(F,G) for invariant G. This is a coefficientwise finite-degree invariance statement; no uniformly bounded Haar-conjugation projector in the unrestricted Wigner l1 norm is assumed.

Take fixed nonzero extensive G_{ {j} }=εχ_1(U_j) at every site. It belongs to every finite degree/support graded source class. **Assuming the archived width-graded tame theorem**, T_G is bounded on X and preserves Y. Whenever |λ| ||T_G||_(X→X)<1, its weak-space inverse R_λ=(I−λT_G)^−1 exists. It CANNOT map all X into Y: otherwise (I−λT_G)(R_λ X)⊂Y would force X⊂Y, contradicting the explicit invariant examples. Hence **R_λ(X) ⊄ Y**. This applies separately to extra support-weight and extra spectral-moment requirements.

A strong-space solution is possible only if the data already satisfy the required strong regularity (and the inverse is bounded at that level). This audit does **not** prove direct bilinear unboundedness in the gauge-invariant sector, nor does it validate the archived model's equivalence to the full physical Gauss-law Hilbert space. Nonlinear λ=1 continuation, interacting spectral gap, and continuum Yang–Mills mass gap remain open.

The complete eight-kilobyte proof, exact rational character-norm verifier, passing log, and SHA-256 manifest are preserved in The Singular Boundary / Proof Audits Library.