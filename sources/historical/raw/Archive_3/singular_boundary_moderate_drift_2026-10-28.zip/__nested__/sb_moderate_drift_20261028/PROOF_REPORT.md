# The Singular Boundary — Exact moderate-curvature drift reduction and finite-energy spectral alternative

**Date:** 2026-10-28  
**Research branch:** `audit/2026-10-28-independent-reconstruction`  
**Status:** Exact nonperturbative finite-SU(2) source-marginal identities; exact Agmon-assisted localization of the covariance obligation; **conditional** source-effective-drift criterion; independently proved finite-energy spectral alternative. The *required growing inward drift has NOT been proved* for the nonlinear Penrose Wilson vacuum. Consequently fixed-support covariance collapse, the quartic resolvent, a uniform mass gap, and continuum reconstruction remain OPEN. No Monte Carlo and no changes to historical simulations.

## 1. Prior hypotheses and provenance

This report directly extends the current branch versions of `R3_IR_REGIONAL_GROUND_STATE_AGMON_2026-10-28.md` (AG-1), `R3_IR_MODERATE_CURVATURE_CONCENTRATION_GATE_2026-10-28.md` (MC-1), `R3_IR_MODERATE_PHASE_RELATIVE_ENERGY_NECK_2026-10-28.md` (NE-1), `R3_IR_LOCAL_EXCITED_RELATIVE_ENERGY_2026-10-28.md` (ER-1) and `R3_IR_CURVATURE_WEIGHTED_FSUM_2026-10-28.md` (FS-1). Source-level equivalence to the original Stage7/26 Hamiltonian is still an unresolved *separate* provenance gate.

Let `G_h` be an embedded finite face-complete SU(2) rhombus disk of edge length h, 4 edges per face, at most 2 faces per link. On `L²(SU(2)^E)` and its gauge-invariant reducing subspace take

`H_h = Σ_e a_e(-Δ_e)+Σ_f b_f(1-p_f)`, `p_f=½ ReTr(W_f)`, `a_e∈(0,a_max]` and `b_f≥β_min h^(-2)` on the fixed-physical-support face set D. Let Ω_h be the strictly positive normalized physical vacuum, K_h=H_h−E0, and `ν_h=Ω_h² dHaar`. Fix real test weights `|q_f|≤q_*`, and define

`X_h=Σ_{f∈D}(1-p_f)`, `Z_h=h X_h`, `Y_h=h Σ_{f∈D}q_f(1-p_f)`.

Then |Y_h|≤q_* Z_h, and the original α=3/2 vacuum-centered Wilson test equals `−h^(−1/2)(Y_h−E_ν Y_h)`. The original objective is exactly **Var_ν(Y_h)=o(h)**.

Assume the *previously proved* regional comparison supplies `E0(H_h)−E0(H_out)≤C_D h^(−3)` uniformly in ambient graph size with the selected interior collar, and AG-1 holds with `L_h=C_L/h` for a fixed large enough C_L>0 and `λ_h=c_λ/h`, `c_λ=√(β_min/(32a_max))`. The regional comparison also gives `E_ν Z_h≤C_Z` uniformly in h.

## 2. Theorem DR-1 — Exact one-dimensional effective drift of the actual vacuum

Define the (nonpositive) ground-state generator acting on smooth real multipliers

`𝓛_h f = Ω_h^(-1)(E0−H_h)(Ω_h f) = Σ_e a_e[Δ_e f+2∇_e log Ω_h ·∇_e f]`.

Let μ_h=(Y_h)_*ν_h be the actual one-dimensional vacuum marginal. Define `γ_h(y)=E_ν[Γ(Y_h)|Y_h=y]`, `b_h(y)=E_ν[𝓛_h Y_h|Y_h=y]`, where `Γ(f)=Σ_ea_e|∇_ef|²`. The chain and ground-state identities give for smooth g

`E_ν[Γ(g(Y_h))]=∫ γ_h(y)|g'(y)|² μ_h(dy)`;
`∫[γ_h(y)g''(y)+b_h(y)g'(y)] μ_h(dy)=0`.

Whenever the source marginal has density μ_h(dy)=ρ_h(y)dy, the latter identity is, in distributions on the interior of its support,

**`(ρ_h γ_h)' = ρ_h b_h`.** (DR-1)

These are *exact nonlinear physical-vacuum identities*, not an assumption that the projected stochastic process Y_h(t) is itself Markov. The conditional diffusion is an exact Dirichlet-form compression; it need not be a genuine Markov lumping of the underlying link dynamics.

The local SU(2) Casimir supplies the explicit unprojected force:

**`𝓛_hY_h = h Σ_{f∈D}q_f Σ_{e∈∂f} a_e[(3/4)p_f − 2∇_e logΩ_h ·∇_e p_f]`.** (DR-2)

This isolates the dynamical information missing from the earlier energy comparisons: the conditional alignment of the true ground-state logarithmic derivative with the Wilson-source gradients. The explicit vacuum factor *cannot* be omitted or bounded solely by regional mean flatness.

The exact pointwise Wilson derivative estimate is

**`Γ(Y_h)≤4a_max q_*² h Z_h`.** (DR-3)

Consequently, using `E_νZ_h≤C_Z`, the entire finite-source spectral first moment obeys

**`M1_h(Y_h)=E_νΓ(Y_h)≤C_M h`, `C_M=4a_max q_*² C_Z`.** (DR-4)

## 3. Theorem DR-2 — Agmon reduction to a compact moderate-curvature marginal

Fix `q_*>0`, choose any constant `T_0>2q_*C_L`, and set `c_T=2c_λ(T_0/q_*−2C_L)>0`. The previously proved AG-1 weighted moment implies, uniformly on the declared fixed physical region,

**`ν_h(|Y_h|>T_0) ≤ C_0 h^4 e^(−c_T/h²)`,**
**`E_ν[Y_h² 1_{|Y_h|>T_0}] ≤ C_1 h^4 e^(−c_T/h²)`,**
**`E_ν[Γ(Y_h) 1_{|Y_h|>T_0}] ≤ C_2 h^5 e^(−c_T/h²)`.** (DR-5)

Proof: |Y_h|>T_0 implies `X_h>T_0/(q_*h)`, safely above `2L_h`. Apply the AG-1 weight at this threshold. For the squared moment use the fact that `x exp(−2λ_h(x−2L_h))` decreases above the threshold for small h. DR-3 gives the gradient tail. All three estimates concern the **actual** interacting vacuum.

The distributional identity `(ργ)'=ρb` from DR-1 implies `ργ` has a locally absolutely continuous representative on the interior of the source range. Coarea provides a density ρ almost everywhere, with the usual conventions at source critical values. Integrating its Dirichlet density over `T∈[T_0,T_0+1]` and applying DR-5 permits a choice `T_h∈[T_0,T_0+1]` such that

**`(ργ)(T_h)+(ργ)(−T_h)≤C_2 h^5 e^(−c_T/h²)`.** (DR-6)

Set `I_h=[−T_h,T_h]`, `N_h=μ_h(I_h)`, `m_{I,h}=E[Y_h|Y_h∈I_h]`, and `V_{I,h}=Var(Y_h|Y_h∈I_h)`. For small h, `N_h=1−O(h^4 e^(−c_T/h²))`, and the exact integration-by-parts identity reads

**`∫_{I_h} ρ γ = [ (y−m_{I,h}) ρ γ ]_{−T_h}^{T_h} − N_h Cov_{I_h}(Y_h,b_h(Y_h))`.** (DR-7)

The boundary term has magnitude at most `2(T_0+1) C_2 h^5 e^(−c_T/h²)`. The full variance differs from its conditional moderate-band variance by at most `O(h^4 e^(−c_T/h²))`, using `Var(Y)≤E[(Y−m_I)²]`, `|m_I|≤T_0+1`, and DR-5. Thus the physical covariance obligation has been reduced *rigorously* to the moderate-band conditional covariance; far-curvature tails are negligible to every fixed polynomial order.

## 4. Theorem DR-3 — A noncircular **conditional** effective-drift coercivity criterion

Assume in addition that there exists a sequence `κ_h→+∞` such that, for μ_h-almost every `y,z∈[−T_0−1,T_0+1]`,

**`(y−z)(b_h(y)−b_h(z))≤−κ_h(y−z)²`.** (DR-8, **NOT PROVED**)

This is a **source-specific conditional force-slope hypothesis** on an explicitly defined actual-vacuum marginal, not an assertion of a physical gap or a global Poincaré inequality. It must be independently derived from DR-2 for the original nonlinear Wilson ground state to be used as a theorem about the model.

The covariance identity with two independent draws from the conditional law gives

`Cov_{I_h}(Y_h,b_h(Y_h)) = (1/2)E_{I_h×I_h}[(Y−Y')(b(Y)−b(Y'))] ≤−κ_h V_{I,h}`.

Insert this into DR-7, apply the boundary estimate and DR-4. Then

**`V_{I,h} ≤ [C_Mh+C_bh^5e^(−c_T/h²)]/(κ_hN_h)`**, and hence

**`Var_ν(Y_h) ≤ C_M h/κ_h + O(h^4 e^(−c_T/h²))=o(h)`.** (DR-9)

This would close the fixed-support α=3/2 vacuum variance gate. But **DR-8 is OPEN**, and the current regional Agmon/Dirichlet estimates do not imply it. It is stronger than necessary, and the earlier two-phase and finite-gap witnesses prevent it from being silently assumed. Neither it nor DR-9 constitutes a proof of a positive continuum mass gap.

## 5. Theorem DR-4 — Unconditional finite-energy spectral alternative

Irrespective of DR-8, the verified DR-4 has another exact consequence. Suppose along any regulator subsequence `Var_ν(Y_h)≥v h`, for some fixed `v>0`. Define the normalized-scale physical source `A_h=(Y_h−E_νY_h)/√h`, so

`||A_hΩ_h||²≥v` and `〈A_hΩ_h,K_hA_hΩ_h〉≤C_M`.

For every `Λ>0`, the spectral theorem gives

`||P_{>Λ}(K_h)A_hΩ_h||²≤C_M/Λ`.

Choosing `Λ=2C_M/v` shows

**`||P_{(0,2C_M/v]}(K_h)A_hΩ_h||² ≥v/2`.** (DR-10)

Thus **failure** of physical-point covariance collapse entails a source-accessible physical excitation with finite energy and nonzero source spectral weight. It does not imply an excitation energy tending to zero, and it is **compatible with** a strictly positive physical mass gap. A positive gap does not logically imply collapse of this particular field variance. This corrects any suggestion that the fixed-support covariance gate is equivalent to the Yang–Mills gap itself.

## 6. Exact SU(2) one-rhombus check

For a single open SU(2) rhombus in the purely electric theory, let `p=(1/2)ReTr U`, `H_E=4a(−Δ_class)` with `a>0`. Its genuine vacuum is constant and Haar has density `ρ(p)=2√(1−p²)/π` on p∈[−1,1]. The source-conditioned exact diffusion and drift are

`γ(p)=a(1−p²)`, `b(p)= (ργ)'/ρ =−3ap`.

SU(2) character orthogonality yields `E p=0`, `Var(p)=1/4` and `Eγ(p)=3a/4`, so the drift identity is saturated:

`EΓ(p)=3a Var(p)`.

For `Y=h(1−p)`, the exact drift is `b_Y(y)=3a(h−y)`, with slope `−3a`, *independent of h*, and `Var(Y)=h²/4`. This already satisfies `o(h)` because the true first moment is `O(h²)` in this one-face model. The diverging-drift condition DR-8 is therefore **sufficient but not necessary**, and a one-face electric example does not establish strong-field Penrose conditional drift growth.

The accompanying deterministic verifier checks these exact Haar/character identities, the truncated flux integration-by-parts formula, the AG-1 scaling and the finite-energy spectral witness. It also checks the original three-rhombus Penrose *spatial* incidence (10 edges), not temporal Q14. No stochastic simulations were performed.

## 7. Updated critical path

**Proved on the declared finite SU(2) model:** exact source-marginal Dirichlet generator and conditional drift (DR-1/DR-2); Agmon-to-moderate-band reduction with negligible tails (DR-5–DR-7); unconditional fixed-energy source spectral alternative (DR-10).

**Conditional, not established:** monotone effective drift with κ_h→∞ on the moderate interval (DR-8), which would imply the requested variance collapse (DR-9). A different model-derived proof of improved source-gradient scaling `EΓ(Y)=o(h)` could also close the variance when combined with a separately proved coercivity estimate. No existing input proves either improvement.

**Open independently:** actual moderate-band conditional drift, fixed-support connected variance, three-/four-source inverse-energy response, infinite-volume spectral gap, nontrivial R2 quantum continuum, and original Stage7/26 Hamiltonian correspondence. The next proof task is to estimate the conditional ground-state logarithmic derivative term in DR-2, rather than adding another assumption of mixing or a uniform gap.
