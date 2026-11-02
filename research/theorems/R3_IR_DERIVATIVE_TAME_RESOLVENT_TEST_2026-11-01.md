# R3-IR — Derivative-tame electric resolvent tests (2026-11-01)

**Status:** exact Casimir commutator, uniform Hilbert-space gradient resolvent estimate, and symbolic polynomial checks. **Not** a holomorphic nonlinear convergence theorem.

Let K=−Σ_e a_e Σ_{k=1}³ X_{e,k}² on the finite product SU(2)^E, with a_e≥a₀>0; X_{e,k} are skew-adjoint right-invariant generators normalized by quaternion imaginary units/2. Let P denote independent-link Haar projection, P₀=I−P.

**Exact commutator:** [K,X_{e,k}]=0 on the polynomial core, since each link Casimir is central and operators on different links commute; hence X_{e,k}K⁻¹P₀=K⁻¹P₀X_{e,k} on the common domain.

**Dimension-independent gradient bound:** Since the nonconstant spectrum has lower edge λ_gap=3a₀/4 and u=K⁻¹P₀f,
Σ_e a_e Σ_k ||X_{e,k}u||²₂ = ⟨u,Ku⟩ = ⟨K⁻¹P₀f,P₀f⟩ ≤ (4/(3a₀))||P₀f||²₂.
Therefore
(Σ_e a_e Σ_k ||X_{e,k}K⁻¹P₀f||²₂)^{1/2} ≤ 2/√(3a₀) ||P₀f||₂.
The constant is uniform in the number of links and polynomial degree. This L² result does not imply a holomorphic sup-norm product estimate.

**Exact SU(2) character check:** On one link, a=Re(U), χ_n(U)=U_n(a), Kχ_n=(n(n+2)/4)χ_n. Thus K⁻¹χ_n=(4/[n(n+2)])χ_n. The local SymPy checker verifies n=1,...,12 and [K,X_k]=0 for six coordinate polynomials.

**Important limitation:** The formula X K⁻¹P₀ f=∫₀∞ X e^{−tK}P₀f dt suggests heat-gradient smoothing, but no fully uniform H∞(Q_R^E) estimate for K⁻¹Γ has been proved. All-orders connected score convergence, the interacting λ=1 gap and the continuum mass gap remain open.

**Next objective:** derive a derivative-tame Banach-scale estimate that is an algebra for connected products; control all spatial embeddings and reconcile the three-face sign conventions. Companion local report, Python checker, execution log and SHA-256 manifest are held in Library Proof Audits.
