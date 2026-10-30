# R3: localized conditional Haar-ball inequality and rank audit
2026-10-27. This is a **conditional theorem with an explicit unresolved frustration defect**, not the arbitrary-support R3 result.

## Exact setup
Let Q be a collection of inserted SU(2) Wilson plaquettes in a finite lattice. Choose a set L of m link variables containing *all edges of Q*, and let ξ denote the fixed complementary exterior links. Under the cavity law, the conditional measure on u∈SU(2)^m has density proportional to exp(-S0(u;ξ)). Define V_Q(u;ξ)=Σ_{q∈Q}γ_q d(W_q(u;ξ)), d(W)=1-ReTr(W)/2 ∈[0,2]. Define

 E0(ξ)=min_u S0(u;ξ), E1(ξ)=min_u [S0(u;ξ)+V_Q(u;ξ)], Δ(ξ)=E1(ξ)-E0(ξ)≥0.

Assume all couplings on faces touching L are ≤b λ, λ≥1; each face length≤ℓ and each link incidence ≤D, uniformly. Any other retained faces depending only on ξ cancel. The conditional ratio is

 R(ξ)= (∫exp[-S0(u;ξ)-V_Q(u;ξ)]du)/(∫exp[-S0(u;ξ)]du).

## Rigorous localized Haar-ball lemma
There are constants c,C>0 depending only on b,D,ℓ and SU(2), independent of ambient lattice size and ξ, such that

 R(ξ) ≥ c^m λ^(-3m/2) exp[-Δ(ξ)].

Proof: a global minimizer u* of S1=S0+V exists on compact SU(2)^m. At u*, all first derivatives vanish. Along product Lie exponential geodesics, second derivative of S1 is bounded in absolute value by C λ times sum of squared coordinate displacements because of bounded face length and incidence. On the product of m balls of radius a/√λ around u*, S1≤E1+C a²m. Its normalized Haar measure ≥(c a³ λ^-3/2)^m. Thus numerator ≥ e^-E1 (c λ^-3/2)^m, after absorbing e^-C a²m; denominator ≤e^-E0. This uses no Fourier-matrix positivity and requires no uniform Hessian nondegeneracy.

After averaging over the *cavity exterior marginal* ρ0(dξ),

 Z1/Z0 = E_{ρ0}R(ξ) ≥ c^m λ^(-3m/2) E_{ρ0} exp[-Δ(ξ)].

In particular, for any good event G with Δ(ξ)≤D0|Q| on G and ρ0(G)≥exp[-D1|Q|], we obtain

 F_Q≤ (3m/2) log λ + m log(1/c) + (D0+D1)|Q|.

If m≤C0|Q| (e.g. m≤ℓ|Q| for L=union of insertion face boundaries), this is the sought O(|Q|(1+logλ)) **provided the good-event frustration hypothesis holds**. It is important that ρ0(G) is the cavity exterior marginal, not independent Haar. The hypothesis is not proven here.

## Explicit test geometry and linearized rank
The independent incidence checker `verify.py` constructs a 2×2 four-quadrilateral spatial disk times a 3-edge temporal circle with (27,63,48) vertices/edges/faces and rank(∂2)=36. At t=0, Q0 contains the seven temporal faces on the union of boundaries of spatial faces 0 and 1. At t=1, Q1 contains the seven faces on the union of boundaries of spatial faces 0 and 2. Thus |Q|=14, the supports overlap spatially but differ, and their union touches m=36 link variables. The retained 34 plaquettes have rank(∂2_ret)=30; inserting Q adds linearized rank 6, while 8 added face constraints are redundant in the linearized cellular image. This rank is NOT a nonlinear partition-function asymptotic and does not control Δ(ξ) or its cavity probability.

The lemma gives in this fixed assembly

 F_Q≤54 log λ +36 log(1/c) - log E_{ρ0}exp[-Δ(ξ)].

This is a localized-variable cost (m=36 instead of all 63 link variables), but a genuine support-local theorem awaits control of the last term. The coefficient 54 is intentionally not reduced by merely counting linearized independent constraints (six); that reduction requires substantial additional analysis of nonlinear critical sets and zero modes.

## Obstacles and next test
Find a *uniform cavity-probability estimate* ρ0{Δ≤C|Q|}≥exp(-C'|Q|) or directly E_{ρ0}exp(-Δ)≥exp(-C|Q|). Conditional worst-case exterior fields can have Δ=Θ(λ), so such a bound cannot be asserted pointwise without added geometry or a correlated exterior rearrangement. A practical next numerical diagnostic samples ξ under the retained cavity law and minimizes S0 and S1 over L to measure the distribution of Δ/λ at large λ. A proof should replace sampling by a support-local comparison/transport controlling exterior interface holonomies. The verified 15-state spin-network computation remains a separate positive benchmark, not a proof of this missing good-event probability.
