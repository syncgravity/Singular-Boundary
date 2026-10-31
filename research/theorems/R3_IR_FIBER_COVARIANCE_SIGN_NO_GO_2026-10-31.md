# R3-IR — Conditional Wilson-fiber magnetic covariance has no kinematic sign

Date 2026-10-31. **Two-rotor algebraic counterfamily, not a Wilson ground-state solution.**

Let p=cos u and q=Tr(V)/2 be independent SU(2) class coordinates under Haar measure, so E[q]=0 and E[q²]=1/4. Let the retained magnetic Wilson potential be V_-(q)=b(1-q), b>0. For 0<c<1, n∈N, set α_n(u)=c cos(2nu) and Φ_n(u,q)=sqrt(1+α_n(u)q). This amplitude is smooth, strictly positive, conditionally normalized E_q[Φ_n²|u]=1, and center-even under u↦π−u; cos(2n arccos p) is a polynomial in p. Let Y act as ∂u on class-coordinate observables and h=logΦ.

Exact formulas: E_(ν_u)[Yh]=0, and

2 Cov_(ν_u)(V_-,Yh)=α_n'(u) E_μ[V_-q]=−(b/4)α_n'(u)=(bnc/2)sin(2nu).

The covariance changes sign and has sup norm bnc/2→∞ as n→∞, despite exact positivity, conditional normalization, center symmetry and nonnegative Wilson-form magnetic potential. Therefore no sign or uniform pointwise bound on the *magnetic covariance term alone* follows from these kinematic inputs.

**Limitations:** Φ_n is not the actual ground-state conditional amplitude of the decoupled T+b(1−q) model. The kinetic material term E[Yk] need not vanish and can cancel magnetic covariance. This result does **not** disprove one-sided cancellation in the full physical remainder R=E[Yk]+2Cov(k+V_-,Yh). Any such cancellation must exploit the exact physical eigen-equation and completed-cage structure.

Verification: 282 angle/frequency checks, maximum quadrature discrepancy 7.11e−15 relative to the quadrature moment E[q²]; quadrature moment differs by 6.69e−8 from exact 1/4. Full derivation and runnable verifier are stored in the Library proof archive. Uniform signed current, connected covariance, and continuum mass gap remain OPEN.