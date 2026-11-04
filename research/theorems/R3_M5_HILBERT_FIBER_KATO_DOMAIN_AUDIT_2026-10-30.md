# R3-IR-530 — Domain-level audit of rooted non-tree SU(2) diamagnetic comparison

2026-10-30. This note makes explicit the key analytic step of R3-IR-528/529 for a SPECIFIED rooted-tree inverse-Whitney quadratic form, rather than claiming that arbitrary covariant electric discretizations inherit it.

Setting: finite connected graph, E links, product Haar on SU(2)^E; chosen rooted spanning tree T; e outside T. Let D_j^a=Σ_b Ad(V_j(U))_{ab} X_j^b, with X_j^b the source-based invariant link derivatives and V_j the root-to-source tree transporter. Let K=M^-1 be a fixed real SPD E×E matrix, and Q[ψ]=(g²/2)Σ_{i,j,a} K_ij ⟨D_i^a ψ,D_j^a ψ⟩. All V_j depend only on tree links, hence **are independent of U_e**. No condition that a root-to-source path avoids its own link j is needed for the following *pointwise first-order norm* argument.

On the smooth form core partition e,B. Schur completion is an identity:
Q[ψ]=(g²/2){⟨C_B ψ,K_BB C_B ψ⟩ +(1/M_ee) Σ_a||D_e^a ψ||²},
C_j^a=D_j^a+β_j D_e^a, β=K_BB^-1 K_Be.
The adjoint rotations of V_j are real and independent of U_e. Consequently each D_j^a for j≠e is a first-order derivative in the BASE Y variables with coefficients independent of U_e, while each D_e^a is skew-adjoint on the fiber Hilbert space H_f=L²(SU2_e), with an orthogonal matrix coefficient depending only on Y. Thus C_j^a is a base-directional derivative plus a skew-adjoint fiber operator; it defines a metric-compatible first-order connection on the trivial Hilbert bundle Y↦H_f.

For ρ(Y)=||ψ(·,Y)||_{H_f}, the fiber Cauchy-Schwarz/Kato inequality on ρ>0 is
|D_j^a ρ(Y)| = |Re⟨ψ,D_j^a ψ⟩_f|/ρ <= ||C_j^a ψ||_f,
because Re⟨ψ,D_e^a ψ⟩_f=0. For arbitrary real SPD K_BB the needed MATRIX form inequality is also valid: for a positive Cholesky square root L of K_BB, Σ_j L_lj C_j^a is still a base derivative plus skew fiber operator, and the Cauchy-Schwarz argument gives
(∇_B ρ)^T K_BB(∇_B ρ) <= ∫_fiber (C_B ψ)^* K_BB(C_B ψ).
Use regularized ρ_ε=(||ψ||²+ε²)^(1/2) for the zero set, and pass ε→0 in H¹. Multiplication V0(Y) contributes ∫V0ρ². Hence
Q_B,C[ψ]+⟨ψ,V0ψ⟩ >= Q_B[ρ]+⟨ρ,V0ρ⟩ >= E_P||ψ||²,
where E_P is the minimum of H0 restricted to P_e-constant functions. The P sector reduces H0 exactly, so its spectral bottom E_P equals the unrestricted E0. Combine with link Haar Poincaré Σ_a||X_e^a ψ||² >= (3/4)||R_e ψ||² to obtain, on the R_e form domain,
⟨ψ,(H0-E0)ψ⟩ >= 3g²/(8M_ee)||ψ||².
Since e is non-tree, D_e is a pointwise orthogonal rotation of the source invariant derivatives. The restriction to physical gauge-invariant functions preserves the inequality because all forms and P_e are gauge invariant.

Domain qualification: the proof is on the smooth cylinder core and extends by closability of the uniformly elliptic smooth finite-dimensional divergence form and lower semicontinuity. Coefficients are smooth on compact SU2^E. This is a proof for the specified ROOTED model, not a derivation of a unique canonical continuum Yang–Mills kinetic operator. If the transport path for any D_j depends on U_e, or if K is configuration-dependent in a way breaking skew fiber-metric compatibility, the argument does NOT apply without modification. Likewise the local coefficient does not remain useful when selected physical b_e/gamma_e grows under refinement.

This audit upgrades R3-IR-528's indicated diamagnetic step to an explicit matrix-valued Hilbert-fiber proof. It is analytic, not a computer-assisted certification of the full infinite-dimensional spectrum. Numerical tests in research/scripts/validate_m5_fiber_kato_metric.py verify Schur coefficients and finite-dimensional Cauchy-Schwarz analogues, not the operator theorem itself. R3-IR-529 remains a conditional finite-model cap consequence as specified. Continuum and refinement-uniform claims remain OPEN.
