# The Singular Boundary — Quartic parity-resolvent audit and SU(2) spectral-window Ward identity

**Research branch:** `audit/2026-10-28-independent-reconstruction`  
**Date:** 2026-10-28  
**Methods:** exact finite-volume operator proof; exact SU(2) differential identities; symbolic/rational checks. No Monte Carlo and no alteration of original historical artifacts.

## Executive finding and corrected proof priority

The previously derived parity-resolved second response (SR-1) is correct under its finite-volume assumptions. Its three terms have *different spectral information requirements*. Unlike the three-source response, a quartic expression cannot in general be truncated to low energies by bounding the first energy moment of the **original** Wilson source: the operator inserted between resolvents can transfer a low-energy excitation into a high-energy parity sector without a resolvent penalty. We give (i) an exact two-sector truncation inequality, (ii) a model-specific SU(2) commutator/Ward identity that controls matrix elements across separated energy windows, and (iii) an exact counterexample to using the known variance and first moment alone. These are constructive mathematical constraints, **not** a gap theorem or a nonlinear Penrose inverse-energy bound.

## Primary dependencies and provenance

Directly inspected: `R3_IR_PARITY_RESOLVED_SECOND_RESPONSE_2026-10-28.md`, the local historical `sb_second_response_20261028/REPORT.md` and its executable verifier (rerun successfully), `R3_IR_THREE_SOURCE_ENERGY_WINDOW_2026-10-28.md`, `R3_IR_CURVATURE_WEIGHTED_FSUM_2026-10-28.md`, and `R3_IR_REFINED_CURVATURE_WEIGHTED_ALIGNED_RESPONSE_2026-10-28.md`. Exact three-rhombus spatial seed: 3 faces, 10 distinct edges, canonical Z^5 coordinate involution swaps outer faces. This is NOT the full temporal Q14 cavity. The Stage7/Stage26 coefficient identity to the declared spatial Hamiltonian is not authenticated here.

## Setup

Let `G` be a finite, face-complete rhombus complex, all spatial links SU(2), with positive Wilson Hamiltonian on full `L²(SU(2)^E)`

`H=Σ_e a_e (-Δ_e) + Σ_f b_f[1−p_f(U)]`, `a_e>0, b_f>=0`, where `p_f=(1/2)ReTr(W_f)`. The standard bi-invariant SU(2) metric has `-Δ χ_j=j(j+1)χ_j`. The gauge-invariant subspace is reducing, and the full strictly positive unique vacuum Ω is physical. All resolvent statements are at a **fixed finite graph**, with `K=H−E0`, `Q=I−|Ω><Ω|`, and `G=QK^{-1}Q` (bounded at fixed regulator, with no uniform bound asserted). Suppose an exact unitary involution `R` commutes with H, Ω is even, and A is a bounded, real, reflection-odd, gauge-invariant multiplication observable, so `RAR=-A`. For source aligned coupling `H(t)=H−tcA`, center is zero at t=0. Put

`X=AΩ` (odd), `S=QA²Ω` (even), `v=||X||²`, `Y=GX` (odd), `m=⟨X,KX⟩`, `U=||A||∞`, `χ=⟨X,GX⟩>=0`.

The exact finite Kato identity from SR-1 is

`V''(0)/c² = 4 Re⟨S,G A G X⟩ + 2⟨GX,(A²−v)GX⟩ −8χ²`.   (QR-1)

All resolvents preserve reflection parity; the first term has an even resolvent acting on an odd-to-even transition.

## Theorem QR-1: rigorous two-sector ultraviolet decomposition

Let `P_< = 1_(0,Λ](K)` and `P_> = 1_(Λ,∞)(K)`, with Λ>0; vacuum projection is excluded. Write `G_< =GP_<`, `G_> =GP_>`, `Y_< =G_<X`, `Y_> =G_>X`, `S_< =G_<S`, and `S_> =G_>S`. Define the **fully low-resolvent approximation**

`B_<(Λ)=4 Re⟨S_<, A Y_<⟩ +2⟨Y_<,(A²−v)Y_<⟩ −8⟨X,Y_<⟩²`.

Write `B=V''(0)/c²`, `r=√m Λ^(−3/2)` and `u=m/Λ²`. Then the following finite-model bound is exact:

```
|B−B_<(Λ)| ≤
  4U r [2U||Y|| + ||G S||]
  + 2(U²+v)[2||Y|| r+r²]
  + 16 χ u+8u².                                         (QR-2)
```

**Proof.** For any finite-first-moment vacuum-orthogonal vector `z`, spectral calculus gives

`||GP_> z||² = ∫_(Λ,∞) E^(−2) dμ_z(E) ≤ Λ^(−3) ⟨z,Kz⟩`,  
`0≤⟨z,GP_>z⟩≤Λ^(−2)⟨z,Kz⟩`.

The ground-state form is `M1(F)=Σ_e a_e ∫|∇_e F|² Ω²dU`, and `∇(A²)=2A∇A`, hence `M1(S)≤4U²m`. Thus `||Y_>||≤r`, `||S_>||≤2Ur`, and `0≤χ_>=⟨X,Y_>⟩≤u`. Expand each term of (QR-1) into low/high pieces. Bound the even-high and odd-high terms of the first expression by Cauchy–Schwarz, the second by the operator norm of `A²−v`, and the last by `|χ²−χ_<²|=2χ_<χ_>+χ_>²`. This gives QR-2.

**What QR-2 does NOT do:** the right-hand side still contains `||GX||`, `||GS||`, and `χ`. First energy moments alone do not control these inverse-energy quantities as Λ increases. In particular, unlike the earlier 3-source ultraviolet theorem, one cannot declare all quartic ultraviolet terms negligible without further spectral input. The *inserted* operator `A` can create high-energy excitations inside the `A²` factor without a corresponding inverse-energy denominator.

## Theorem QR-2: exact nonlinear SU(2) spectral-window commutator (Ward identity)

For any smooth gauge-invariant multiplication A, on the common smooth core,

`[H,A]u = - Σ_e a_e [ (Δ_e A)u +2 ∇_e A ·∇_e u ]`.  (QR-3)

**Proof.** The Wilson magnetic potential is also a multiplication operator and commutes with A. Use `Δ_e(Au)=(Δ_e A)u+2∇_e A·∇_e u+A Δ_eu`. The result is exact and does not depend on the size of magnetic couplings.

For any 0≤η<Λ with spectral projections of K,

`|| P_>Λ A P_≤η || ≤ || P_>Λ [H,A] P_≤η ||/(Λ−η)`.  (QR-4)

**Proof.** On the high-to-low block let `K_>=P_>Λ K`, `K_<=P_≤η K`, and `X=P_>Λ A P_≤η`. The Sylvester identity gives `K_>X−XK_<=P_>[K,A]P_≤`. Its unique bounded solution is `X=∫₀^∞ e^(−sK_>) P_>[K,A]P_≤ e^(sK_<)ds`, whence the norm bound because `||e^(−sK_>)||≤e^(−Λs)` and `||e^(sK_<)||≤e^(ηs)`. Finite-volume smoothness makes the restricted commutator well-defined.

**Explicit model-specific coefficient control.** Suppose every edge meets at most two magnetic faces, `a_e≤a_max`, the test source is `A=h^(2−α)Σ_{f∈D}q_fp_f` with `|q_f|≤q_max` and `|D|h²≤A_R`, and set `D_A=−Σ_e a_eΔ_eA`. The SU(2) fundamental Casimir yields

`||D_A||∞≤3 a_max q_max A_R h^(−α)`,

`Σ_e a_e ||∇_e A||∞²≤2 a_max q_max² A_R h^(2−2α)`.

For `v∈Ran P_≤η` of unit norm, nonnegative V and the electric-form inequality `H_E≤H` imply `Σ_ea_e||∇_ev||₂²≤E0+η`. Accordingly,

```
||P_>Λ A P_≤η|| ≤ [ 3a_max q_max A_R h^(−α)
   + 2√(2a_max) q_max √A_R h^(1−α) √(E0+η) ]/(Λ−η).   (QR-5)
```

This is a **noncircular, explicitly SU(2)-based** low/high spectral transition estimate valid at all magnetic couplings. The global product trial gives `E0=O(h^(−3))` for fixed bounded *total* physical area under the declared geometric coefficient bounds. At α=3/2 and η at most `O(h^(−1))`, the resulting numerator is only `O(h^(−2))`. Therefore QR-5 does **not** suppress transitions across the previously selected cutoff `Λ=h^(−1−δ)` when `0<δ<1`; it becomes effective only for substantially higher energy separation, e.g. `Λ≫h^(−2)`. This identifies a genuinely missing **local excited-state kinetic-energy** or commutator cancellation estimate; it is not a no-go theorem for more sophisticated bounds.

## Theorem QR-3: exact counterexample to a naive quartic first-moment cutoff

On `C³` let `K_N=diag(0,1/N,N)`, parity `R=diag(1,−1,1)`, and the real odd self-adjoint multiplier analogue

```
A_N = [[0,1/N,0],
       [1/N,0,1],
       [0,1,0]],       N≥3.
```

The unique vacuum is e₀, the odd first excitation has energy 1/N, and the even high excitation has energy N. The operator norms satisfy `||A_N||≤√2`. Exact rational calculation gives

`v_N=||A_NΩ||²=N^(−2)`, `m_N=⟨A_NΩ,K_N A_NΩ⟩=N^(−3)`,

`4⟨S,GAGX⟩=4/N²`,  
`2⟨GX,(A_N²−v_N)GX⟩=2`,  
`−8⟨X,GX⟩²=−8/N²`.

Thus `V_N''(0)/c²=2−4/N²→2`, **despite** vanishing source variance and first moment, while `A_N` is uniformly bounded. The unsuppressed term contains the high even state through `A_N|odd>`, with no high-energy inverse resolvent. This is a precise abstract matrix witness, **not** an SU(2) Wilson, positive-kernel, reflection-symmetric Penrose continuum counterexample. Its odd-sector gap closes, so it does not refute results requiring a proved uniform odd-sector gap. It proves the **logical insufficiency** of variance/first moment and high source-energy-tail bounds for quartic response.

## What remains and the honest next theorem

The earlier low/intermediate three-source bound remains **OPEN** for generic physical Penrose Wilson sources; on reflection-odd symmetric seed it vanishes at exactly the symmetric point, but this does not control a coupling neighborhood. QR-2 and QR-5 establish that a quartic response proof must independently control at least the odd-sector low resolvent vector `G_oX`, the even-sector `G_eS`, and/or the commutator transitions `P_> [H,A] P_<`. Neither sector mixing nor the requisite local excited-state energy bound follows from vacuum curvature or exact geometry alone.

**Best next mathematical obligation:** prove a source-specific, localized excited-state kinetic or resolvent bound for the true nonlinear SU(2) Hamiltonian at the declared strong-magnetic coefficients, uniformly on finite physical regions and, ultimately, all required boundary conditions. This is stricter and less circular than assuming a Poincaré or transfer contraction equivalent to the full mass gap. Even that local bound would not by itself prove the gap or the R2 quantum continuum.

**Evidence classifications:** QR-1, QR-2 and QR-3 independently proved at finite volume; QR-5 is a model-specific deterministic bound conditional only on displayed coefficients and bounded total physical area for its asymptotic interpretation. Regulator-uniform quartic resolvent, physical-point variance and continuum mass gap: **open**. Previous historical claim R3-IR-119 remains open and is sharpened, not closed.