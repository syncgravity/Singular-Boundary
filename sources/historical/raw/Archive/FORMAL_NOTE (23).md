# Nonlinear Gaussian–Wilson comparison: a finite-block theorem and cutoff obstruction

26 October 2026 — The Singular Boundary. Scope: full 2+1-dimensional SU(2) Wilson plaquette action on a finite bounded-incidence Penrose-derived spacetime cell complex. No uniform nonlinear contour theorem or mass gap is claimed.

## Exact normalized comparison lemma

Let Q be an internal link set with m links, all exterior links fixed to v. On a gauge-fixed coordinate chart A in a vector space of real dimension d≤3m, suppose the Wilson conditional measure can be written

  dμ_Q(A | v, chart) = Z_W^{-1} exp[-S_W(A;v)] J(A) dA,

and choose a positive quadratic reference S_2(A;v), with Gaussian law restricted to the same chart

  dγ_Q(A | v, chart) = Z_2^{-1} exp[-S_2(A;v)] dA.

If the function R(A)=S_W(A;v)-S_2(A;v)-log J(A) has oscillation osc_chart R ≤ ω, then exactly

  exp(-ω) ≤ dμ_Q/dγ_Q ≤ exp(ω)

almost everywhere, and for every event E in this chart

  exp(-ω) γ_Q(E) ≤ μ_Q(E) ≤ exp(ω) γ_Q(E).

Proof: dμ/dγ=e^{-R}/E_γ[e^{-R}]; the normalizing expectation lies between exp(-sup R) and exp(-inf R). No total-volume factor occurs. This statement is conditional on *being in the chosen chart*; it does not bound the probability of the complement.

## Wilson-specific Taylor remainder

At a stationary flat background, use local exponential coordinates A_e∈su(2), |A_e|≤η, and fix residual gauge directions. The four-link Wilson plaquette map is analytic on a fixed neighborhood of zero and each link belongs to at most D plaquettes. For bounded c_-λ≤β_p≤c_+λ there is a geometry-independent constant C_D such that

  |S_W(A)-S_W(0)-S_2(A)| ≤ C_D λ m η³.

This is a conservative third-derivative bound; lower-order cancellations on special configurations can improve it, but no uniform quartic remainder is asserted. Haar exponential-coordinate density satisfies |log J(A)-log J(0)|≤C m η² for sufficiently small η, with analogous chart Jacobians after a precisely defined compatible gauge fixing. Hence

  osc R ≤ C_D m(λ η³+η²).

Choosing η=Mλ^{-1/2} (M fixed) gives ω≤C_D m(M³ λ^{-1/2}+M²λ^{-1}). The conditional, chart-restricted Wilson and Gaussian probabilities are therefore within exp[±C_Dm/√λ] for any fixed M and m, with constants independent of *ambient* volume. If m grows with refinement one needs m/√λ bounded (and ultimately small); this elementary estimate is not scale-uniform for macroscopic blocks.

For nonflat backgrounds the expansion must be around an actual stationary constrained background and the quadratic Hessian must be verified positive after gauge fixing. A mere small-plaquette-defect assumption is insufficient. If a linear term is present, one must include it in the Gaussian reference or recenter.

## Why this does not transfer the contour theorem

For SU(2), d_p=1-cos θ_p. The large-field event d_p>δ, δ=λ^{-1/2}, corresponds at small angles to θ_p ≳ const λ^{-1/4}. A chart in which all link amplitudes are O(λ^{-1/2}) has plaquette angle O(λ^{-1/2}) and hence d_p=O(λ^{-1}), so it misses the intended event at large λ. Enlarging the chart to η≈λ^{-1/4}, the conservative bound C_Dλmη³ grows like m λ^{1/4}, and no cutoff-uniform small relative density comparison follows. Nonlinear background readjustment and localized multiscale integration would be needed.

## Nonlinear large-field remainder identity

Let E be an arbitrary plaquette event, G the chosen chart. Decompose exactly:

 μ_W(E) = μ_W(G) μ_W(E | G) + μ_W(E∩G^c)
        ≤ exp(ω) γ(E | G)+ μ_W(G^c).

The second term requires an independent Wilson-measure large-field estimate. This identity is not an all-contour bound unless G and its complement are controlled *jointly and locally*.

## Covariance issue

A positive Gaussian curvature Hessian yields 0≤D(λD*D+G)^{-1}D*≤λ^{-1}I for a positive gauge regulator G. This holds for a flat reference operator and certain admitted backgrounds, not for an arbitrary nonflat Wilson Hessian. The local chart comparison above gives no operator-norm decay for the full interacting covariance.

## Status

Proved: normalized density comparison via oscillation; Wilson-specific local Taylor estimate around a stationary flat background with bounded incidence and fixed gauge chart; explicit scale obstruction at the large-field threshold. Not proved: uniform chart-complement control; background-dependent Hessian positivity throughout the nonlinear measure; gauge-fixing determinant bounds under arbitrary blocks; uniform multiscale polymer activities; R3 or R2 mass gap.

References for *context only*, not imported as theorems on Penrose complexes: T. Balaban, Ultraviolet stability of three-dimensional lattice pure gauge field theories, CMP 102 (1985) 255–275, DOI 10.1007/BF01229380; Propagators for lattice gauge theories in a background field, CMP 99 (1985) 389–434, DOI 10.1007/BF01240355.
