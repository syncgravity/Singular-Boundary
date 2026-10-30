# The Singular Boundary — Improved nonlinear vacuum mesoscopic angle comparison and sparse-defect fixed-support obstruction

**Date:** 2026-10-28. **Audit branch:** `audit/2026-10-28-independent-reconstruction`. **Scope:** exact consequences of the actual finite interacting SU(2) ground-state equation, plus an exact positive gauge-invariant *trial-state* counterexample to inferring fixed-support nonlinear Wilson-versus-angle remainder concentration from a priori moment/energy budgets. **Not proved:** fixed-support comparison in the actual vacuum, source covariance limit, continuum Hamiltonian, physical mass gap, nonlinear quartic resolvent, and Stage 7/26 source equivalence. No Monte Carlo or historical archive modifications.

## 1. Model and precise hypotheses

Let G_h be a finite simply connected edge-to-edge rhombus disk, with fundamental SU(2) Wilson Hamiltonian H=Σ_e a_e(-Δ_e)+Σ_f b_f d_f on full link L² and its vertex-gauge-invariant reducing subspace. Put p_f=½ReTr W_f, d_f=1−p_f∈[0,2]. Each face has four links and each link meets at most two faces. Let Ω_h be the strictly positive, normalized physical ground state, ν_h=Ω_h²dHaar. For a selected interior face region D_R, S=∪_{f∈D_R}∂f, C(D_R) its exterior crossing collar, H_out the cut Hamiltonian, E_out its ground energy and Δ_D=E0(H)−E_out. Assume a_e≤a_* on S and b_f≥b_*:=β h⁻² on D_R. Under the previously stated fixed-physical-support Penrose geometry, the regional comparison gives Δ_D≤C_E(R²+R)h⁻³ for h≪R≤R0 with a complete interior collar. Source weights may be any bounded real |q_f|≤q_*; no positivity or smoothness is needed for the norm estimates.

Define X_h=Σ_{f∈D_R}d_f, Z_h=hX_h, and principal class-angle θ_f=2 arccos p_f∈[0,2π]. Let Q_f=θ_f²/8=(arccos p_f)²/2 and r_f=Q_f−d_f. The exact global SU(2) inequalities (proved in the prior comparison report) are

0≤r_f≤c_angle d_f,  c_angle=π²/4−1, and r_f≤(π⁴/96)d_f².

The Q_f multiplier is bounded and continuous, but **not globally smooth at W_f=−I** (the SU(2) cut locus). Only bounded multiplication and norm estimates are used; no unqualified commutator differentiation of Q_f is asserted.

## 2. Theorem MA-1 — Sharp regional exponential-barrier tail for the actual interacting vacuum

The cut-Hamiltonian form inequality is H−E0≥b_*X_h−Δ_D. For nonnegative real s<√(b_*/a_*), set f=e^{sX_h/2}. The exact ground-state transform gives 〈fΩ,(H−E0)fΩ〉=Eν Γ(f). The SU(2) Casimir and local incidence give Γ(X_h)≤4a_*X_h pointwise. Therefore, writing M(s)=Eν e^{sX_h},

(b_*−a_*s²)M'(s)≤Δ_D M(s).

Integrating M(0)=1 proves

log M(s)≤[Δ_D/√(a_*b_*)] artanh(s√(a_*/b_*)).

Fix 0<ζ<1, choose s=ζ√(b_*/a_*), k_h=s/h=ζ√(β/a_*)h⁻², and set

u0_h=h(Δ_D/b_*)[artanh(ζ)/ζ].

Markov's inequality yields the **true-vacuum** tail

Pν(Z_h>u0_h+t)≤exp(−k_h t), t≥0.                    (MA-1)

For W=(Z_h−u0_h)_+, integration of the tail gives E W≤1/k_h, E W²≤2/k_h². Since Z_h≤u0_h+W,

Eν Z_h²≤u0_h²+2u0_h/k_h+2/k_h².                  (MA-2)

This is an exact finite-volume moment consequence of the ground-state equation, not a Gaussian comparison. Under the regional Penrose increment assumption, u0_h≤C(R²+R), 1/k_h=C'h²; so

Eν Z_h²≤C[(R²+R)²+h⁴].                           (MA-3)

For fixed R, (MA-1) suppresses excursions beyond a conservative regional energy-budget wall with width O(h²), **not** fluctuations below that wall. It does not imply Varν(Z_h)=o(h), a physical gap, or a fixed-time source correlator.

## 3. Theorem MA-2 — Improved **vacuum-only** mesoscopic Wilson/angle equivalence

For any bounded signed q on D_R, set B_h^W=−√h Σ_{D_R}q_fd_f, B_h^θ=−√h Σ_{D_R}q_fQ_f and R_h=B_h^θ−B_h^W=−√hΣq_fr_f. Pointwise |R_h|≤c_angle q_* Z_h/√h. It follows from MA-3 that

||R_h Ω_h||²≤C q_*²[(R²+R)²/h+h³].                (MA-4)

The same estimate holds for ||B_h^WΩ_h||² and ||B_h^θΩ_h||², with different constants, using Q_f≤(π²/4)d_f. If R=h^γ (in fixed physical units), 1/2<γ<1, all three vector norms are O(h^{γ−1/2}+h^{3/2})→0. This **strictly improves** the earlier γ>2/3 sufficient condition for comparing these sources on the **vacuum**. It does **not** improve the old theorem's uniform operator norm on an entire low-energy spectral band; arbitrary superpositions in that band are not eigenstates and MA-1 was proved for Ω_h.

For centered physical vectors v_h=(B_h^W−EνB_h^W)Ω and w_h=(B_h^θ−EνB_h^θ)Ω, the same bounds imply ||v_h||+||w_h||=O(h^{γ−1/2}+h^{3/2}) and ||v_h−w_h|| of the same order. Let μ_v,μ_w be their positive spectral measures for K_h=H_h−E0. By polarization and the spectral theorem,

||μ_v−μ_w||_TV≤(||v_h||+||w_h||)||v_h−w_h||=O(h^{2γ−1}+h³).   (MA-5)

Uniformly for every Euclidean time t≥0, |〈v,e^{−tK}v〉−〈w,e^{−tK}w〉| obeys the same bound. This is **unconditional for the actual interacting vacuum** under declared hypotheses, but both source vectors tend to zero; it does not construct a nontrivial continuum field.

## 4. Theorem SD-1 — Positive gauge-invariant sparse-defect trial-state obstruction at fixed support

**Not a statement about Ω_h.** Consider any simply connected rhombus disk with F_h∼A h⁻² faces, nonnegative magnetic couplings b_f≤β_max h⁻², and electric a_e≤a_max. Select a nonempty fixed positive-area face region and M_h=⌊h⁻¹/²⌋ faces inside it, each with q_f=1 (or q_f uniformly bounded below by a positive constant). The face holonomies g_f are independent Haar variables under maximal-tree gauge fixing, although the kinetic energy in those coordinates couples faces. With κ=1/h and Zκ=I₁(2κ)/κ, define sign patterns s^+_f=+1 on all faces and s^-_f=−1 on M_h selected faces and +1 elsewhere, and define

Ψ_{±,h}(U)=Zκ^(−F_h/2) exp[κΣ_f s_f^± p_f(U)].

These are strictly positive, normalized and gauge invariant. For s_f=+1 the one-face law is proportional to exp(2κp) times SU(2) Haar; for s_f=−1 it is the reflected law. Each one-face deficit d has mean O(h) for the plus law and 2−O(h) for the minus law. The one-face radial moment estimates give E_plus r=O(h²), Var_plus r=O(h⁴), E_minus r→r_*:=π²/2−2>0, Var_minus r=O(h), with r(p)=½(arccos p)²−(1−p). (The minus variance arises from the cut-locus square-root cusp; it is O(h), not O(h²).)

The overlap is exactly s_h=〈Ψ_+,Ψ_-〉=Zκ^(−M_h)=exp[−Ω(h⁻³/²)], because the two signs cancel on the M_h differing face variables and the full Haar product is normalized. Put Φ_h=(Ψ_+ +Ψ_-)/√[2(1+s_h)]. This is a **positive normalized gauge-invariant trial wavefunction**.

All of the following budgets hold uniformly as h→0:

- 〈Φ_h,H_hΦ_h〉=O(h⁻³). Indeed magnetic energy of the plus branch is O(h⁻³), and the M_h fully curved faces contribute only O(M_h h⁻²)=O(h⁻⁵/²); electric kinetic energy is O(κ F_h)=O(h⁻³) from the local SU(2) identity E_κ|∇p|²=O(κ⁻¹) and incidence ≤2. The nonnegative H quadratic form and Cauchy–Schwarz control the positive superposition.
- (1/F_h)Σ_f E_{Φ_h}d_f=O(h), since M_h/F_h=O(h^{3/2}).
- For every fixed real t≥0, sup_h E_{Φ_h} exp(t hΣ_f d_f)<∞: plus faces contribute O(F_h h²) to the logarithm of the product MGF, minus faces contribute O(h M_h), and |Φ_h|²≤Ψ_+²+Ψ_-².
- For every 0<γ<1, the expected physical area of faces with d_f≥h^γ tends to zero, by the preceding mean bound and Markov (indeed the M_h intentionally defected faces occupy area O(h^{3/2})).
- The Wilson-source Dirichlet expectation E_{Φ_h}Γ(√hΣ_f q_fd_f)=O(1) by Γ≤4a_max q_*²hΣ_fd_f and the previous mean bound. **This is not a physical first spectral moment for Φ_h**, since Φ_h is not an eigenstate.

Nevertheless, for the fixed-support remainder R_h=√hΣ_f q_fr_f with q_f=1 on the selected region and 0 outside, product-Haar independence within each branch gives Var_{Ψ_+}(R_h)→0 and Var_{Ψ_-}(R_h)→0. Their means differ by

E_{Ψ_-}R_h−E_{Ψ_+}R_h=√h M_h(E_minus r−E_plus r)→r_*.

The interference corrections to moments of R_h are bounded by a polynomial in h⁻¹ times s_h and vanish superexponentially. Thus

**lim_{h→0} Var_{Φ_h}(R_h) = r_*²/4 = (π²/2−2)²/4 ≈2.153266.**   (SD-1)

This **does not disprove** fixed-support Wilson/angle equivalence for the *true ground state*; it proves that the previously established mean-curvature, sparse-bad-area, fixed-order exponential-moment, regional-size energy, and basic Dirichlet budgets do not imply that equivalence in arbitrary gauge-invariant positive wavefunctions. The actual vacuum eigenstate equation or an independent local-defect suppression/connected-cumulant theorem is indispensable.

## 5. Exact fixed-support covariance gate, without importing a Gaussian vacuum

For the actual interacting vacuum, define the bounded pointwise remainder R_h=√hΣ_{f∈D_R} q_fr_f and its centered counterpart Ȓ_h=R_h−EνR_h. Its exact variance is

**Varν(R_h)=hΣ_{f,g∈D_R}q_fq_g Covν(r_f,r_g).**    (CG-1)

Consequently a sufficient, source-specific and **independently required** estimate for fixed-support centered Wilson/angle source-vector equivalence is

Σ_{f,g}q_fq_g Covν(r_f,r_g)=o(h⁻¹).

For convergence of the associated full positive spectral measures in total variation it additionally suffices that ||(B_h^W−EνB_h^W)Ω_h|| remain bounded (or, more generally, that the product of its norm with ||Ȓ_hΩ_h|| tend to zero). These are **conditional criteria**, not results deduced from the current Hamiltonian budgets. A stronger but not necessary absolute connected-kernel summability may be used. The two source multipliers live in the *same nonlinear vacuum*: CG-1 compares no Gaussian measures.

The sparse-defect witness shows precisely why a mere bound on the physical area fraction of bad faces cannot supply CG-1: O(h⁻¹/²) defects have vanishing physical area O(h^{3/2}), yet their coherent two-branch occupation creates O(1) fluctuations of the critical remainder. One needs a true-vacuum statement bounding the number/connected fluctuations of localized defects, rather than only their average area.

## 6. Verifier and evidence limitations

The deterministic Python script `verify.py` checks the exact global SU(2) Wilson-angle inequalities, radial Haar integrals with Bessel normalizers and reflected minus branch, sparse-defect overlap, two-branch source means and variances at refinements h=n⁻² for n=12,20,32,48,64, and all optimized Laplace exponents/threshold algebra. The two-branch moment calculation is **analytical product-measure quadrature**, not Monte Carlo. The test evaluates up to F=16,777,216 nominal faces through exact factorization, without creating a lattice of that many edges; these are normalized gauge-invariant face-holonomy states on any simply connected disk with that face count, not a claimed realization of the original Stage 26 geometry.

**Status:** MA-1/MA-2 proved for the stated true interacting vacuum and regional hypotheses. SD-1 proved only for positive physical trial wavefunctions with energy O(h⁻³). CG-1 exact but its required o(h⁻¹) connected-kernel estimate remains OPEN. Physical continuum gap, stage-source reconstruction and quartic resolvents remain OPEN. Original historical data unchanged.
