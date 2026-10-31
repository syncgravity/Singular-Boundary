# Exact Wilson neighboring-force Fierz identity and center vanishing

**Date:** 2026-10-31. **Status:** rigorous original-link finite SU(2) identity and a uniform *geometric* conditional bound. It does **not** establish the signed-current bound or a uniform bound on the remaining second-derivative score response.

For SU(2) generators X_a=iσ_a/2, let p(M)=Tr(M)/2. For any C,D∈SU(2), the fundamental trace/Fierz identity gives

Σ_a [Tr(X_a C)/2][Tr(X_a D)/2] = [p(C D^{-1})-p(C)p(D)]/4.

Fix one edge variable U and the other links. Cyclically start both oriented face words at the common edge. If the two plaquettes traverse the edge in the **same** direction, write p_f=p(UA) and p_g=p(UB). Then

Σ_a (X_a p_f)(X_a p_g) = [p((UA)(UB)^{-1})-p_f p_g]/4.

If they traverse it in **opposite** directions, write p_f=p(UA), p_g=p(U^{-1}B). Since X_a p_g=−Tr(X_a B U^{-1})/2, the correct orientation formula is

Σ_a (X_a p_f)(X_a p_g) = −[p((UA)(BU^{-1})^{-1})−p_f p_g]/4.

The right-hand products are **based, transported** loop words, not simply Tr(W_f W_g)/2 without compatible basepoints and edge orientations. The expressions are gauge invariant as a whole. Rotating/reversing cyclic words yields the other presentations.

By Cauchy–Schwarz and the SU(2) norm identity Σ_a (X_a p_h)^2=(1−p_h²)/4,

|Σ_a (X_a p_f)(X_a p_g)|≤¼√(1−p_f²)√(1−p_g²).

Consequently, for the already-defined deleted-Wilson force correlation B_e(p)=−Σ_{g≠f:e∈∂g} b_g E[∇_e p_f·∇_e p_g | p_f=p],

**|B_e(p)|≤¼√(1−p²) Σ_{g≠f:e∈∂g} b_g E[√(1−p_g²)|p_f=p]≤¼√(1−p²) Σ b_g.**

In the center angle p=cos u, the last bound is (sin u/4)Σ b_g on 0≤u≤π/2. This vanishing factor holds for *any* ground-state measure (indeed any conditional measure) and is independent of total face count when bounded edge incidence is assumed. The b_g coefficients may nevertheless diverge as h^{-2}. The force correlation has **no universal sign**, even at fixed p_f and p_g; this is certified by explicit noncommuting SU(2) examples and follows algebraically because the relative vector axes can be aligned or anti-aligned.

**Crucial limitation:** This controls B_e, *not* K_e, L_e, or C_f in the earlier exact distributional balance (ρK_e)'=ρ(B_e+L_e). No bound on L_e or a legitimate inversion of the weighted derivative is obtained. In particular, a center-vanishing local forcing term does not supply an anti-depletion estimate, and the proof obligation sup_f 𝔗_{f,h}=o(h^{-1/4}) remains OPEN. The bound is a geometric restriction, not a physical mass-gap assertion.

**Verification:** 4,000 independent SU(2) noncommuting configurations, both shared-edge orientations. Maximum Fierz residual 5.56×10^-17; Cauchy–Schwarz bound never violated. Both signs appear for each orientation. Program and JSON in the corresponding Library bundle.