# R3-IR — exact Wilson-word recursion and a nonperturbative strong-field complexity obstruction

**Date:** 2026-10-28. **Classification:** exact finite-volume algebraic and semigroup theorems, a nonperturbative SU(2) one-rhombus theorem, and a bounded-degree combinatorial estimate. **NOT a physical mass-gap result.** No historical Monte Carlo replay or source substitution.

## I. Definitions and source separation

Let `G=(V,E,F)` be a finite connected oriented spatial gauge complex, `H_phys=L²(SU(2)^E)^{SU(2)^V}`, and let `L_e=-Δ_e` with spin-j Casimir `j(j+1)`. Write

`H = H_E + B I - V`, `H_E=Σ_e a_e L_e`, `B=Σ_f b_f`, `V=Σ_f b_f p_f`, `p_f=(1/2)Tr U_f`, `a_e>0`, `b_f≥0`.

All Wilson sources are real normalized fundamental traces `W_γ=(1/2)Tr U_γ` of closed oriented graph words, including words with repetitions, retracings, mixed and winding paths. A based loop holonomy is transported with a connector η when needed. The physical ground state `Ω_H` is NOT the electric vacuum 1 when `b_f>0`. Source-inserted vacuum decay requires `Q_H W_γ Ω_H` and cannot be inferred by evaluating electric-vacuum matrix coefficients alone.

## Theorem W1 — exact elementary Wilson-word Hamiltonian recursion

For any two based closed loops γ and f (transport the face f by a connector η from γ's base), the SU(2) trace identity gives

`p_f W_γ = (1/2)( W_{γ η f η⁻¹} + W_{γ η f⁻¹ η⁻¹} ).`  (W1.1)

Consequently the magnetic multiplication part sends every *single trace* to an explicit sum of at most `2|F|` single traces, with coefficients `b_f/2` (plus the diagonal scalar `B`). **This is an exact finite-graph identity even at strong coupling**; it is not a transfer spectral contraction.

For a closed word γ in which edge e occurs `m_e` times, its electric action obeys the exact differential insertion formula

`L_e W_γ = (3/4)m_e W_γ - 2 Σ_{1≤r<s≤|γ|; e_r=e_s=e} Σ_{a=1}^3 (1/2)Tr(U_γ with T_a inserted at occurrences r and s),` (W1.2)

with `T_a=iσ_a/2` and the signs/placements prescribed by `X_e U_e=T_a U_e` and `X_e U_e⁻¹=-U_e⁻¹ T_a`. Each double insertion is contracted using

`Σ_a T_a M T_a = (1/4)M - (1/2)Tr(M)I`.

The resulting product of trace factors is converted to single traces using (W1.1). Thus `H` maps each finite Wilson trace to a finite linear combination of Wilson traces, with no unproven scalar character closure for repeated edges. In the special case that *no edge of γ is repeated*, the cross-term sum vanishes and

`H_E W_γ=(3/4)(Σ_{e∈γ}a_e)W_γ`.  (W1.3)

**Proof:** differentiate the ordered holonomy product twice using the SU(2) bi-invariant Laplacian, collecting one-occurrence Casimir terms and pairwise product-rule terms. The Pauli Fierz identity and the trace product identity then establish closure. This is an exact algebraic recursion, not a controlled all-scale infrared estimate.

**Connector warning:** For disjoint loops α and f, the two fused traces in (W1.1) can individually depend on a long, arbitrarily chosen connector η, although their sum is connector independent. For `U_α=U_f=iσ_z`, a connector preserving the z axis gives fused trace `−2`, while one conjugating the z axis to x gives `0`; the opposite-orientation trace cancels the change. Therefore separately taking absolute, physical-path-length-weighted values of the two fused terms may destroy exact locality through a representation artifact. A viable source recursion should preserve multi-trace/disconnected structure until a *proved linked cancellation* is performed.

## Theorem W2 — exact finite-volume Dyson/word-insertion expansion and truncation certificate

With all operators restricted to `H_phys`, define `D=H_E≥0`. For each finite `G` and time `t≥0`, the bounded-perturbation Duhamel series converges in operator norm:

`exp(−tH) = exp(−Bt) Σ_{n=0}^∞ ∫_{0<s_1<...<s_n<t} exp[−(t−s_n)D] V exp[−(s_n−s_{n−1})D] ... V exp(−s_1 D) ds`.  (W2.1)

If `S_N(t)` is the partial sum through order N, then

`||exp(−tH)−S_N(t)|| ≤ exp(−Bt) Σ_{n=N+1}^∞ (Bt)^n/n!`. (W2.2)

**Proof:** `||V||≤B`, and all electric heat factors are contractions; the time simplex has volume `t^n/n!`. Multiplication by `exp(−Bt)` yields the stated exact deterministic majorant. Because the source trace algebra is stable under electric heat and the magnetic multiplication W1, each finite-order term gives a finite Wilson-word expansion.

**Scope warning:** `B=Σ_f b_f` is extensive. A bound depending on `Bt` is NOT volume uniform, and on the specified physical refinement path `b_f∼a_sp⁻²` it cannot provide regulator-uniform order-by-order control. W2.2 is a finite-volume reproducibility certificate and a diagnostic of the missing cancellation, not an infrared theorem.

## Theorem W3 — exact positive half-line character paths on a genuine SU(2) rhombus

For the single open spatial rhombus with equal electric coefficient a and magnetic coefficient b, use the physical orthonormal basis `|n>=χ_{n/2}`, n=0,1,2,... . The exact Hamiltonian is

`H_b = D + bI − (b/2)A`, `D|n>=a n(n+2)|n>`, `A|n>=|n−1>+|n+1>` (omit negative index). (W3.1)

Therefore for any m,n≥0,

`<m| exp(−tH_b) |n> = exp(−bt) Σ_{r=0}^∞ (b/2)^r Σ_{nearest-neighbor spin walks n=n_0,...,n_r=m} ∫_{0<s_1<...<s_r<t} exp[−Σ_{i=0}^r a n_i(n_i+2)(s_{i+1}−s_i)] ds` (W3.2),

where `s_0=0, s_{r+1}=t`. Every path weight is nonnegative. The tail over paths with r>N is bounded in `ℓ¹` coefficient norm by the **Poisson upper tail**

`exp(−bt) Σ_{r>N}(bt)^r/r!`.  (W3.3)

**Proof:** character fusion `pχ_{n/2}=(χ_{(n+1)/2}+χ_{(n−1)/2})/2`, bounded nearest-neighbor adjacency, and the positive diagonal electric heat kernels in (W2.1). A given r-step path has coefficient `(b/2)^r`, and at most `2^r` paths emanate from a starting vertex; dropping all electric damping gives (W3.3).

**Interpretation:** This is an **all-positive-b exact source-inserted heat-kernel construction** on a genuine interacting SU(2) Wilson regulator. The fully connected source correlator still involves the unknown *interacting* vacuum and its projector, so positive path coefficients do not imply a common physical decay rate. The Poisson tail bound requires growing retained order as `bt` grows; it is a certified upper bound, not proof that this growth is optimal.

## Theorem W4 — nonperturbative strong-magnetic loss of every fixed-spin ground-state cutoff

Write a conjugacy-class holonomy as `U=cos θ I+i sin θ u·σ`, `θ∈[0,π]`. The class-Haar probability measure is `dμ(θ)=(2/π)sin²θ dθ`. The one-rhombus Hamiltonian `H_b=4a(-Δ)+b(1−cosθ)` is exactly the Sturm–Liouville form

`H_b = −a(∂_θ²+2cotθ ∂_θ)+b(1−cosθ)` (W4.1)

on class functions, with the regular boundary condition. Multiplication by `sinθ` conjugates this to

`−a d²/dθ² − a + b(1−cosθ)` on `L²(0,π)` with Dirichlet endpoints. (W4.2)

Let Ω_b>0 be the normalized unique ground state, and `P_{≤J}` the Haar-orthogonal projection onto characters `{χ_j:0≤j≤J}` (j half-integral). **For any fixed a>0**, as `b/a→∞`,

`E_0(b)≤C_0 sqrt(a b)`, `C_0=8π²+1/2`, when `b≥a`, (W4.3)

`∫_{θ≥δ}|Ω_b|²dμ ≤ C_0 sqrt(a/b)/(1−cosδ)` for every δ∈(0,π), (W4.4)

and, crucially,

`lim_{b/a→∞} ||P_{≤J} Ω_b|| = 0` for every fixed J. (W4.5)

**Proof:** Set `r=(a/b)^(1/4)≤1` and use the Lipschitz form-domain trial `f_r(θ)=(1−θ/r)_+`. The Rayleigh quotient of the kinetic term is at most `8π² a/r²`: `|f_r'|≤1/r`, `f_r≥1/2` on θ≤r/2, `sinθ≤θ`, `sinθ≥2θ/π` on [0,1], and `μ([0,r])/μ([0,r/2])≤2π²`. Since `1−cosθ≤θ²/2≤r²/2` on the support, the potential quotient is at most `b r²/2`. The variational principle yields (W4.3). The potential energy expectation cannot exceed E0 because the electric term is nonnegative, so Markov's inequality gives (W4.4).

Choose `ε=a/b` and `δ=ε^(1/8)≤1`. As `1−cosδ≥δ²/3`, the ground-state probability outside the δ-ball is bounded by `3C_0 ε^(1/4)`, while the Haar volume of the ball is at most `(2/(3π)) ε^(3/8)`. For every normalized character `χ_j`, `||χ_j||∞≤2j+1` and `||χ_j||₂=1`. Splitting its inner product with Ω_b inside/outside the ball and applying Cauchy–Schwarz gives

`|<χ_j,Ω_b>| ≤ (2j+1) sqrt(2/(3π)) ε^(3/16) + sqrt(3C_0) ε^(1/8) →0`. (W4.6)

There are finitely many j≤J, proving (W4.5). The argument uses exact SU(2) Haar measure, a variational upper bound, and positivity—no weak-b perturbation, simulated field data, or continuum assumption.

**Corollary and precise limitation.** On the specified physical Penrose strong-magnetic trajectory, `b/a ∝ a_sp⁻²`, the analogous **one-rhombus reference** leaves every fixed-spin Haar subspace. This rigorously rules out controlling that reference vacuum by a Wilson-character cutoff fixed independently of b/a. It does NOT prove that the Penrose multi-rhombus vacuum does the same, does not prove a physical gap closes, and does not yield a lower bound on the true excitation gap at strong b. The weak-b perturbative formulas from the previous research note and W4 address opposite coupling regimes.

## Theorem W5 — connected spatial support enumeration is volume independent

For any face-adjacency graph of maximum degree Δ≤4 (two quadrilateral faces adjacent when they share an edge), the number N_k of connected sets of k faces containing a prescribed face is at most

`N_k ≤ Δ^{2(k−1)}≤16^{k−1}`. (W5.1)

**Proof:** assign to each connected k-face set a deterministic rooted spanning tree, followed by its deterministic depth-first closed walk. The walk has length `2(k−1)`, stays on the face graph, and determines its visited vertex set; the map is injective. Each step has at most Δ choices. This establishes a volume-independent *combinatorial count*, not an interacting cluster estimate. In particular, its use in a linked expansion still requires a model-derived bound on the weights of connected words, as opposed to applying W2's extensive absolute-norm estimate.

## Critical path and integrity

**Now independently established:** exact finite-graph Wilson-word electric/magnetic closure (W1); convergent finite-volume heat-kernel/Dyson series and Poisson truncation bound (W2); positive half-line SU(2) character paths (W3); nonperturbative one-rhombus high-spin necessity for the ground state (W4); connected-support combinatorics (W5).

**Still open:** a volume- and spatial-refinement-uniform **connected** source-inserted bound for interacting Penrose SU(2), including cancellation of disconnected insertions, large field and generated high-spin words, physical temporal normalization, and all relevant boundary/center sectors. Also open: literal Stage 7/Stage 26 source-to-action equivalence along the declared continuum coefficient trajectory, and R2 quantum spatial reconstruction. None of W1–W5 implies an interacting physical mass gap. No 2+1-dimensional model theorem is represented as proof of 3+1D Yang–Mills.

**Next noncircular lemma to pursue:** construct a linked *source-rooted* Duhamel/character-graph expansion which separates terms supported away from a Wilson source **before** taking absolute norms, and derive a nontrivial bound on its connected remainder with independently established constants. A claim based only on fixed spin cutoff, Poisson tail, or an assumed vacuum mixing/gap must fail this audit. Preserve multi-trace/disconnected representations until connected cancellation is proved.
