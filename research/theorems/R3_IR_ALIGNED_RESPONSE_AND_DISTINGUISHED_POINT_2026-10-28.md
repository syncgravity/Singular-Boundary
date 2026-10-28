# R3-IR — Source-aligned nonlinear coupling response and the distinguished-point obstruction
**Date:** 2026-10-28. **Evidence:** new exact finite SU(2) Wilson identities and a sharp abstract positive two-level counterexample. **No physical-point variance collapse, mass gap, or continuum proof is claimed.** No Monte Carlo or historical source modifications.

## Set-up
On a finite planar face-complete SU(2) rhombus complex G_h, every face has four distinct links and every link belongs to at most two faces. Let h>0, F_h=|F(G_h)|, F_h h²≤A₀, a_e∈(0,a_max], and the original positive magnetic coefficients b_f⁰=β_f/h², 0<β_f≤β_max, with face shape factors σ_f∈{σ_-,σ_+}, σ_->0. Let D_h be a specified face subset (possibly an interior physical test region). Consider the actual nonlinear Wilson Hamiltonian on the full link space:
H_h(t)=Σ_e a_e(-Δ_e)+Σ_{f∉D_h}b_f⁰d_f+Σ_{f∈D_h}(β_f+tσ_f)h⁻²d_f,
d_f=1−p_f, p_f=(1/2)ReTr W_f.
The distinguished physical model is t=0. Choose τ=(1/4)min_{f∈D_h}(β_f/σ_f)>0, with a uniform lower bound independent of h if the two Penrose shape coefficients remain fixed. Coefficients are nonnegative on t∈[-2τ,τ]. The full-link ground state Ω_h(t) is positive, simple and gauge invariant. Define K_t=H_h(t)−E_h(t), Q_t=I−|Ω_t><Ω_t|.

The **critical area-smeared field** for the indicator test 1_D is
A_h=h Σ_{f∈D_h} σ_f p_f; its centered version is A_h−〈A_h〉_t.
The key exact alignment is
A_h−〈A_h〉_t = −h³(∂_tH_h−〈∂_tH_h〉_t).

## Theorem AR-1 — Exact source-aligned susceptibility identity
For each finite h and t in the positive coupling interval,
−E_h''(t)=2〈Q_t (∂_tH_h)Ω_t,K_t⁻¹ Q_t(∂_tH_h)Ω_t〉.
Let V_h(t)=Var_t(A_h), M1_h(t)=〈Q_tA_hΩ_t,K_tQ_tA_hΩ_t〉 and χ_h(t)=2〈Q_tA_hΩ_t,K_t⁻¹Q_tA_hΩ_t〉. Then
χ_h(t)=−h⁶E_h''(t),    V_h(t)²≤(M1_h(t)/2)χ_h(t).
Both identities are exact and require neither a uniform spectral gap nor Gaussian or mixing assumptions. K_t⁻¹ is the finite-volume vacuum-orthogonal reduced inverse. The first-moment bound from the Wilson ground-state Dirichlet identity is
M1_h(t)≤4a_max σ_+²F_hh² uniformly in t.

## Theorem AR-2 — One-dimensional coupling integral with explicit h³ rate
The previously proved nonnegative Wilson product-trial estimate bounds E_h(−τ)≤6 F_h sqrt(a_max β_max)/h. The E_h(t) curve is nondecreasing and concave. Hence
∫_{−τ}^{τ} (−E_h''(t))dt=E_h'(−τ)−E_h'(τ)
≤E_h'(−τ)≤[E_h(−τ)−E_h(−2τ)]/τ
≤6F_h sqrt(a_max β_max)/(τ h).
Substitution in AR-1 gives
**∫_{−τ}^{τ}V_h(t)²dt ≤ C_* (F_hh²)²h³ ≤ C_* A₀²h³,**
where one permissible constant is
C_*=12 a_max^(3/2) σ_+² sqrt(β_max)/τ.
This is a **nonperturbative theorem for the actual finite nonlinear SU(2) Wilson Hamiltonian family**, but it is coupling-integrated. It does not claim V_h(0)→0.

Because 0≤C_h(s;t)≤V_h(t) for a centered source, the same L² coupling-integral bound controls all normalized positive-time correlations simultaneously. For any predetermined refinement h_n with Σ_n h_n³<∞, Tonelli gives V_{h_n}(t)→0 for almost every fixed deformation t∈[-τ,τ], uniformly over physical Euclidean time in absolute amplitude. This remains a generic-deformed-coupling statement; t=0 is exceptional until proved otherwise.

## Theorem AR-3 — Sharp distinguished-point response alternative
Write I_h=C_*A₀²h³ and v_h=V_h(0).
If liminf v_h≥v>0, then for all sufficiently fine regulators there exists a deformation t_h, |t_h|≤4I_h/v², with V_h(t_h)≤v/2. In particular, by the mean value theorem somewhere between 0 and t_h,
**|V_h'(t)|≥v³/(8I_h) ≥ [v³/(8C_*A₀²)]h⁻³.**
Thus persistent physical-point variance requires coupling response to grow at least on the scale h⁻³ in this aligned direction. This is a necessary alternative, **not** proof that the physical variance vanishes.

If a uniform-in-volume/regulator modulus |V_h(t)−V_h(s)|≤L_h |t−s| is independently proved, then
v_h ≤ max{(4L_h I_h)^(1/3), (2I_h/τ)^(1/2)}.
Hence **L_h=O(h^(-q)) for any q<3 suffices to prove V_h(0)→0**, with rate O(h^(1−q/3)+h^(3/2)); in particular uniform Lipschitz control implies V_h(0)=O(h). Neither such modulus nor any pointwise nonlinear covariance bound has yet been established. A Hölder response modulus can be treated analogously.

## Theorem AR-4 — Exact positive avoided-crossing obstruction, even with a uniform gap
The averaged-to-pointwise inference is invalid using only the abstract positive-operator, concavity, analytic-ground-state, first-moment and gap information above. Let σ_x,σ_z be Pauli matrices, δ>0 independent of h, K_h=h⁻³, and define
H_h^toy(t)=δ(I−σ_x)+K_h(I−σ_z)+(1+t)K_h(I+σ_z),  |t|≤1/4.
Every summand is nonnegative, the ground state is simple, and the gap satisfies
gap(H_h^toy(t))=2sqrt(δ²+K_h²t²)≥2δ.
The positive coupling derivative is ∂_tH=K_h(I+σ_z). Define the *source-aligned* centered observable A_h^toy=−h³(∂_tH−〈∂_tH〉). Its exact variance and first moment are
V_h^toy(t)=δ²/(δ²+K_h²t²),    M1_h^toy(t)=2δ²/sqrt(δ²+K_h²t²)≤2δ,
while V_h^toy(0)=1 for all h. Nevertheless, for any fixed τ>0,
∫_{−τ}^{τ} (V_h^toy(t))²dt
=(δ/K_h)[arctan(K_hτ/δ)+(K_hτ/δ)/(1+(K_hτ/δ)²)]
~(πδ/2)h³.
Thus even a **uniform positive gap** cannot prevent an h³-wide variance spike when the source-aligned derivative grows with refinement. Its optimal response slope is of order h⁻³. This model is **not** an SU(2) Wilson Hamiltonian and proves no no-go theorem about the Penrose physical point. It proves that the general inference based solely on the current averaged-response hypotheses is invalid and that the h⁻³ threshold is sharp at that abstract level.

## Research ledger, limitations, next theorem
- **Independently proved:** AR-1 exact finite Wilson susceptibility, AR-2 aligned nonlinear coupling integral, AR-3 distinguished-point response alternative, AR-4 abstract exact positive counterexample.
- **Conditionally proved:** physical variance collapse if a coupling-response modulus L_h=o(h⁻³) is independently established (including the stronger O(h⁻q), q<3, case).
- **Open:** any such modulus for the actual interacting Penrose SU(2) Hamiltonian, fixed-point V_h(0), nontrivial interacting continuum fields, volume- and regulator-uniform mass gap.
- **Most productive next theorem:** bound the **aligned third-source inverse-energy response**, equivalently ∂_tV_h(t), near t=0 by o(h⁻³), from actual nonlinear Wilson dynamics without assuming a gap-equivalent mixing estimate. Alternatively derive a direct fixed-coupling variance estimate. The exact toy obstruction requires an argument using SU(2) Wilson locality beyond operator positivity and spectral concavity alone.

Reproducibility: scripts/audit/verify_aligned_response.py, exact symbolic Kato, susceptibility, h-scaling and two-level avoided-crossing checks, no Monte Carlo. Preserves historical binary/source artifacts and earlier claims with explicit corrections.