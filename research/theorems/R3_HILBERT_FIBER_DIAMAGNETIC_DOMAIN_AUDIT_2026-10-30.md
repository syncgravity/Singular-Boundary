# R3-IR-530 — Independent domain-and-connection audit of protected non-tree gap (2026-10-30)

**Audit scope:** the concrete rooted-tree *finite regulator* scalar Hilbert-space model of R3-IR-528, NOT the unique canonical Hamiltonian of continuum SU(2) Yang–Mills. No previously reported Penrose floating-point spectrum was re-executed here: its 30-link NPZ is not mounted in the current runtime. R3-IR-528 and R3-IR-529 remain CONDITIONAL on the specified root-tree covariant electric operator, not physically universal.

## Form and frame derivation

Let e be a chord (non-tree edge) and write the link coordinate space as X=SU(2)_e × Y, with normalized Haar. The source generators X_e^a are skew-adjoint in the fiber; every rooted transporter V_j is a smooth function of Y alone. Set D_j^a=Σ_c Ad(V_j)_{ac}X_j^c. On smooth cylindrical functions D_j^a are skew-adjoint (the multipliers do not depend on their own link coordinate for the standard root-to-source path), and the operator is defined through the quadratic form, not by a naive unordered differential product.

Let K=M^-1 be a **fixed real SPD edge matrix**, tensored with the adjoint-component identity. Separate local e components from all other links B, complete the square, and set s_e=K_ee-K_eB K_BB^-1 K_Be=1/M_ee. The background covariant differential array becomes ∇_B=D_B+C D_e, where C=K_BB^-1 K_Be, a real constant matrix (same multiplier for each adjoint component). The cross term C D_e acts on the fiber as a skew-adjoint operator; D_B consists of ordinary skew-adjoint background invariant derivatives rotated by real SO(3) root-frame coefficients. Thus ∇_B is a metric-compatible Hilbert-space connection over Y on the H=L²(SU(2)_e) fiber. It can be curved; curvature/flatness is NOT needed for the Kato inequality.

For r(Y)=||ψ(.,Y)||_H (defined a.e.), in each orthonormal left/right invariant frame, Re<ψ,∇_B ψ>_H = r · (D_B r), since the fiber connection pieces have vanishing real expectation. To handle the SPD *edge-mixed* metric K_BB, apply the Cauchy–Schwarz contraction with K_BB⊗I_3 **after** taking the real fiber contraction. This yields pointwise (D_B r)^* K_BB(D_B r) <= (∇_B ψ)^* K_BB(∇_B ψ) in the quadratic-form sense. The potential V0(Y) is scalar on H. The right-hand background energy is exactly the P_e-sector quadratic form on r(Y), so it is bounded below by E_P ||ψ||², where E_P is its infimum. The local electric remainder gives (g2²/(2M_ee)) Σ_a||X_e^a ψ||². The P_e-sector is reducing (root path contains no U_e), and is included in the full domain. Therefore E0=E_P and

R_e(H0-E0)R_e >= (3g2²/(8M_ee)) R_e

using the fundamental SU(2) Haar Poincare gap 3/4. Note that the earlier proof only stated this contraction in prose; this audit exposes the required positive-tensor and skew-adjoint hypotheses explicitly.

## Domains and limits

Smooth cylindrical functions on the compact finite-dimensional product group are dense in the first-order form domain; K SPD and adjoint rotations orthogonal make the form norm equivalent to the usual H¹ Sobolev norm. The form is closed after H¹ completion, yields a Friedrichs self-adjoint operator, and reduction by bounded Haar projection passes from the smooth core to the form domain. The nonlinear fiber norm r is H¹ by Hilbert-valued Sobolev/Kato contraction, so the lower bound extends by density. Magnetic V0 is bounded multiplication at each finite regulator.

These statements do NOT prove that the chosen root-tree metric is physically equivalent for different transport-tree choices, or that its canonical quantization derives uniquely from lattice gauge action. They do not supply refinement-uniform electric coupling or a center-cap estimate at arbitrary selected b.

## Independent numerical analogue

A separate 5-site background ×4-component fiber graph model uses arbitrary (often large) background scalar potentials, unitary fiber parallel transports that fix the fiber-constant vector, and a positive fiber excitation form. 150 seeded tests verified the background ground-energy comparison and the isolated fiber-sector gap. This is a **finite unitary discrete analogue** testing the abstract inequality structure, not a direct SU(2) Penrose operator simulation or a numerical proof of continuous Kato regularity.

Reproduction: research/scripts/validate_hilbert_fiber_diamagnetic_analogue.py.

**Status:** no counterexample found to the R3-IR-528 inequality under its explicit rooted finite-model assumptions. The implication for R3-IR-529 remains conditional on those assumptions; the refinement-uniform deleted-face cap and continuum Yang–Mills mass gap remain OPEN.
