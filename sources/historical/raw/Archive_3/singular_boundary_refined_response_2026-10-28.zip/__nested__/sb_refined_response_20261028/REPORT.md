# R3-IR — Curvature-weighted source-aligned response at the physical coupling

**Date:** 2026-10-28  
**Evidence status:** new exact finite-volume SU(2) identities and their conditional geometric-refinement corollaries; independent exact two-level obstruction. **The distinguished-point variance, nonlinear continuum field and mass gap remain open.** No Monte Carlo was conducted; no original data were modified.

## Motivation and source provenance

This report independently combines the already committed source-level arguments in:

- `research/theorems/R3_IR_CURVATURE_WEIGHTED_FSUM_2026-10-28.md` (FS-1, FS-2): the pointwise fundamental SU(2) gradient identity and improved interacting energy moment.
- `research/theorems/R3_IR_MESOSCOPIC_INTERIOR_CURVATURE_2026-10-28.md` (MI-1 through MI-3): interior mesoscopic mean curvature, conditional on the *declared* geometric coefficient trajectory.
- `research/theorems/R3_IR_ALIGNED_RESPONSE_AND_DISTINGUISHED_POINT_2026-10-28.md` (AR-1 through AR-5): exact coupling susceptibility and an older, weaker `O(h^3)` averaged bound.

The present result **strengthens, but does not invalidate**, the earlier `O(h^3)` bound at exponent α=1. The older fixed-gap two-level counterexample is not a counterexample satisfying the strengthened `M1=O(h)` hypothesis. We give an adjusted counterexample below.

The physical `Stage 7` / `Stage 26` source-level equality to this declared Hamiltonian is **not independently verified here**. No original numerical source archive has been replaced or rerun.

## Setup and hypotheses

Let `G_h` be a finite face-complete SU(2) Penrose rhombus regulator, each face with four distinct edges, each edge in at most two faces. On the full link Hilbert space use

`H_h(t)= Σ_e a_e (-Δ_e) + Σ_{f∉D_h} b_f^0 d_f + Σ_{f∈D_h} h^(-2)[β_f+t q_f] d_f`,  
`d_f=1−p_f`, `p_f=ReTr(W_f)/2`, `q_f=σ_f φ(x_f)`.

Here `φ` is a fixed **real, bounded, possibly signed** test function with support in a fixed interior physical disk, `A_f=h²σ_f`, and `0<β_min≤β_f≤β_max`, `σ_-≤σ_f≤σ_+`, `0<a_e≤a_max`, all independent of h. The number of faces in the total regulator obeys `F_h h²≤A0` (bounded total physical area). There is an interior collar sufficient for MI-3, uniform for the whole coupling family described next.

Choose fixed `τ>0` so that `|t|≤2τ` implies `β_f+t q_f≥β_min/2>0` for every f in the test region. This is possible since `φ` is fixed and bounded. All background magnetic coefficients are positive and `≤bmax/h²`, and the `t`-deformed family has a common upper bound `β_eff/h²`. The intended physical Hamiltonian is exactly `t=0` under the declared coefficient prescription. All finite H_h(t) have a unique strictly positive, gauge-invariant ground state and compact resolvent.

Let the centered source with an explicit normalization exponent be

`A_{h,α}=h^(2−α) Σ_{f∈D_h} q_f p_f`, `A^c=A−〈A〉`, `V_{h,α}(t)=〈(A^c)^2〉`.

For each `|t|≤τ`, assume the **proved consequence of MI-3** in this uniformly comparable coupling class:

`Σ_{f∈D_h} 〈d_f〉_t ≤ K_R h F_R`, with `F_R h²≤A_R` and constants `K_R,A_R` independent of h and t. This is a consequence of MI-1 and Penrose interior-ball counting, not an independent mixing assumption.

## Theorem RR-1: strengthened interacting first energy moment, uniform in t

For `K_t=H_h(t)−E_h(t)`, let `M_{1,h,α}(t)=〈A^cΩ,K_t A^cΩ〉`. The exact ground-state transform gives

`M1= Σ_e a_e ∫ |Σ_{f∋e} h^(2−α) q_f ∇_e p_f|² dν_t`.

The SU(2) Casimir identity is `|∇_e p_f|²=(1−p_f²)/4≤d_f/2`. Let `D_fg=Σ_e a_e∫∇_e p_f·∇_e p_g dν_t`. Then `D_fg=0` for distinct faces not sharing an edge, `D_ff≤2a_max〈d_f〉`, and the face-overlap degree at most four gives

`wᵀDw ≤5 Σ_f w_f² D_ff`

for every real vector w, without any clustering assumption. Therefore

**`M_{1,h,α}(t) ≤ C_m (F_Rh²) h^(3−2α) ≤ C_m A_R h^(3−2α)`**,  
where `C_m=10 a_max σ_+² ||φ||_∞² K_R`.

For α=1 this is `O(h)` (stronger than the historical `O(1)` bound); for α=3/2 it is `O(1)`. At **t=0**, for α<3/2, the spectral measure `μ_{h,α}` obeys `μ((ε,∞))≤C_m A_R h^(3−2α)/ε` and the exact source correlation obeys `0≤C(0)−C(s)≤s C_m A_R h^(3−2α)` for all physical times s≥0. This imposes no variance assumption and no gap.

## Theorem RR-2: exact aligned susceptibility for signed smooth tests

Because the coupling perturbation is exactly source-aligned,

`∂_t H_h = h^(−2) Σ_{f∈D_h} q_f d_f`,  
`A^c_{h,α}= −h^(4−α)[∂_tH_h−〈∂_tH_h〉]`.

Kato perturbation theory for the finite simple ground state and the exact positive spectral measure give

`−E_h''(t)=2〈Q(∂_tH)Ω,K_t^(-1)Q(∂_tH)Ω〉`,  
`χ_{h,α}(t):=2〈A^cΩ,K_t^(-1)A^cΩ〉=−h^(8−2α) E_h''(t)`,  
`V_{h,α}(t)^2 ≤ (1/2)M_{1,h,α}(t) χ_{h,α}(t)`.

Here `K_t^(-1)` is restricted to the vacuum-orthogonal sector. The response identity is exact for signed φ as long as the deformed Hamiltonian's magnetic coefficients remain nonnegative.

## Theorem RR-3: strengthened coupling-averaged variance — `O(h^(8−4α))`

A positive one-link product trial gives a uniform global ground-energy upper bound for the entire `|t|≤2τ` family:

`0≤E_h(t)≤C_E F_h/h`, with e.g. `C_E=3√(2a_max β_eff)`.

Concavity of E(t) gives

`∫_{−τ}^τ (−E''(t))dt=E'(−τ)−E'(τ)`  
`≤[E(−τ)−E(−2τ)+E(τ)−E(2τ)]/τ`  
`≤[E(−τ)+E(τ)]/τ≤2 C_E F_h/(τ h)`.

**This two-sided bound does not assume `E'(t)≥0`; it remains valid for signed test functions.** Combining it with RR-1 and RR-2 yields

**`∫_{−τ}^τ V_{h,α}(t)^2dt ≤ C (F_R h²)(F_h h²) h^(8−4α) ≤ C A_R A0 h^(8−4α)`**,  
with `C=C_m C_E/τ`.

In particular:

| exponent | improved integrated variance² | distinguished point |
|---|---|---|
| α=1 | `O(h^4)` | **open** |
| α=3/2 | `O(h²)` | **open** |
| 3/2<α<2 | `O(h^(8−4α))` | **open** |
| α≥2 | no decay concluded from this argument | **open** |

For each fixed α<2 and a predetermined dyadic (or otherwise `Σ_n h_n^(8−4α)<∞`) refinement, Tonelli implies `V_{h_n,α}(t)→0` for Lebesgue-almost every **fixed deformed** coupling t in the interval. The physical point t=0 may be an exceptional point. This statement holds for each fixed smooth signed test, not automatically simultaneously for every test in an uncountable family.

## Theorem RR-4: response threshold at the original physical coupling

Put `I_h=C A_R A0 h^p`, `p=8−4α>0`, and `v_h=V_{h,α}(0)`. If `liminf v_h≥v>0`, then some t_h within `4I_h/v²` of zero satisfies `V_{h,α}(t_h)≤v/2`, hence at an intermediate coupling

`|V'_{h,α}(t)|≥v³/(8I_h)=Ω(h^(−p))`.

Conversely, a model-derived Lipschitz bound `sup_{|t|≤τ}|V'_{h,α}(t)|=O(h^(−q))` with q<p suffices to prove `V_{h,α}(0)→0`; the rate is `O(h^((p−q)/3)+h^(p/2))`.

For α=1, a sufficient response estimate is `o(h^(−4))` (not merely the earlier `o(h^(−3))` criterion, which is stronger than necessary). For α=3/2, the threshold is `o(h^(−2))`.

The exact connected **three-source** response is

`h^(4−α) V'_{h,α}(t) = 2 Re〈Q(A^c)^2 Ω,K_t^(-1)Q A^c Ω〉`.

Thus for α=3/2 a sufficient noncircular target is `sup_{|t|≤τ}|〈Q(A^c)^2Ω,K_t^(-1)Q A^cΩ〉|=o(h^(1/2))`. This is **OPEN**, and assuming it would be an assumption about interacting temporal response rather than its proof.

## Theorem RR-5: an exact avoided-crossing obstruction consistent with the improved moment

The earlier abstract two-level witness with fixed δ had first moment `O(1)`, not `O(h)` at α=1. It is therefore **not a counterexample to RR-3's strengthened first-moment hypothesis**. A corrected witness is:

`H_h^toy(t)= δ_h(I−σ_x)+K_h(I−σ_z)+(1+t)K_h(I+σ_z)`,  
`K_h=h^(α−4)`, `δ_h=h^(3−2α)`, for `α∈{1,3/2}`.

All terms are positive semidefinite, the finite ground state is unique, the matrix depends analytically on t, and the gap is `2√(δ_h²+K_h² t²)`. The source `A^toy=−h^(4−α)(∂_tH−〈∂_tH〉)` is just centered `−σ_z`. Its exact variance and first moment are

`V_h^toy(t)=δ_h²/(δ_h²+K_h² t²)`,  
`M1_h^toy(t)=2δ_h²/√(δ_h²+K_h²t²)≤2δ_h=2h^(3−2α)`.

But `V_h^toy(0)=1` for every h. Its integrated squared variance over a fixed symmetric interval satisfies

`∫ V²dt~(π/2)(δ_h/K_h)=(π/2)h^(7−3α)`.

At α=1 the spike is `h^4` wide and *saturates the sharpened averaged rate*, while its physical-point gap closes like `2h`. At α=3/2 the gap is uniformly bounded below by 2, the spike is `h^(5/2)` wide and is consistent with the `O(h²)` averaged theorem, while `V_h(0)=1`. This is an abstract two-level **logical obstruction**, not a Penrose SU(2) Wilson counterexample. It proves that the improved averaged theorem, first-moment estimate, finite-volume analyticity and spectral positivity do not suffice to infer pointwise variance collapse even at α=3/2 and with an abstract uniform gap.

## The remaining actual proof obligation

Prove a **model-specific** distinguished-coupling response estimate for the nonlinear Penrose Wilson ground state, or directly estimate its covariance for an appropriate smooth test field at a chosen α. For α=3/2 the precise sufficient source-aligned bound is `o(h^(−2))` on the variance derivative, equivalently `o(h^(1/2))` on the renormalized integrated three-source response in RR-4. This must follow from actual shared-link SU(2) dynamics, not from an assumed gap or abstract concavity. Alternatively, identify a nontrivial interacting field in a different renormalization class and independently construct its physical time correlations.

**Caution:** All stated constants apply to bounded physical total area and fixed interior regions. They do not establish the infinite-physical-volume limit, Stage26 source identity, or the 2+1D continuum mass gap. They do not address the 3+1D Yang–Mills problem.
