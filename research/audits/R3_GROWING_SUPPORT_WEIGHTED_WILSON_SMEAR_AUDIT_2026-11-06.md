# P2/T2: Growing-support Wilson-defect smears and the physical-curvature scaling gap

**November 6, 2026 · finite original-link SU(2) cubic research audit, pending independent mathematical review. All P0–P5/T0–T5 continuum and mass-gap gates OPEN.**

Previous PR #89 (fixed-k private-pivot joint holonomy marginal) was merged into main at `dc5b143538fae30cb4fe9db457d08759c02bce8d` before this investigation.

Consider the finite open n³ cubic mesh of the **fixed unit physical cube**, h=1/n, E=3n(n+1)² links, P=3n²(n+1) plaquettes, Wilson defect ℓ_p=1−½tr₂U_p∈[0,2], S=Σ_p ℓ_p. The genuine coupled Gauss-invariant ground-state measure ν=Ω² Haar is that of H=αΣ_e(−Δ_e)+β S, α=g₀(h)²/(2h), β=2/(g₀(h)²h). The previously derived variational bound is E_ν[S]/P≤b_h:=(3g₀(h)²/2)√(E/P)≤3g₀(h)²/√2. The **classical spatial** full non-Abelian negative-gradient Wilson flow Φ_s satisfies S(Φ_sU)≤S(U) pathwise.

## Theorem A (growing number of faces, fixed spatial volume)

Let f be any bounded nonnegative profile 0≤f≤L on the unit physical cube and f_p=f(x_p). Its support may contain k(h)=Θ(h⁻³) distinct faces. Define the gauge-invariant **box-normalized lattice-unit** smear F_h(f,s)=P⁻¹ Σ_p f_p ℓ_p(Φ_sU). Then for every s≥0, including s=τ/h²,

- E_ν F_h(f,s) ≤ L b_h;
- E_ν F_h(f,s)² ≤ 2L² b_h;
- ν(F_h(f,s)>ε) ≤min(1,L b_h/ε).

Proof: 0≤F≤LS(Φ_s)/P≤LS(U)/P, and F≤2L; combine the true-vacuum mean bound, F²≤2LF and Markov. No factorization of ν, independent-plaquette hypothesis or private pivot is used. Along g₀(h)²→0 this gives lattice-unit L² and probability flattening, **not physical curvature**.

## Theorem B (sharp/simple non-Abelian gradient control for bare smears)

For any real weights w_p, let F_w(U)=Σ_p w_pℓ_p(U), **without flow**. The exact character-gradient identity on each incident link is ||∇_eℓ_p||²=ℓ_p(2−ℓ_p)/4≤1/4. Since each link meets ≤4 plaquettes and each plaquette has exactly four distinct edges, Cauchy–Schwarz implies the **pointwise** inequality

||∇F_w(U)||² ≤ 4 Σ_p w_p².

Thus with w_p=f_p/P,
||∇F_h(f,0)||²≤4L²/P,
and the *quantum ground-state-transformed* Dirichlet form satisfies
𝓔_ν(F_h(f,0),F_h(f,0))≤4αL²/P=2g₀(h)²L²/(hP)=O(g₀²h²).

This bound holds for the full non-Abelian interacting setting, but **cannot be transferred to derivatives of F_h(f,τ/h²)** without bounds on DΦ_s, which can expand near center saddles. More importantly, a small quantum Dirichlet form does **not** imply small vacuum variance or quantum correlation decay without a uniform Poincaré/spectral-gap theorem.

## Exact obstruction in physical-curvature normalization

The prior classical physical-energy functional is 𝓔_h(U)=(8/h)S(U). On the unit cube, 𝓔_h(Φ_sU)=(8P/h)F_h(1,s), with P/h~3h⁻⁴. Consequently the present estimate gives only
E_ν 𝓔_h(Φ_sU)≤(8P/h)b_h=O(g₀²h⁻⁴).
To get a finite expected physical energy from the normalized defect smear would require **O(h⁴) mean defects**, not merely O(g₀²). This is an **insufficient upper bound**, not a proof that actual curvature diverges. At zero flow time a physical-weight smear (8/h)Σ f_pℓ_p has quantum Dirichlet bound O(g₀²h⁻⁶), which is equally insufficient.

For a fixed physical support in a **growing** spatial box, local normalization by k(h) introduces the factor P/k(h) and the global mean S/P alone does not give a uniform thermodynamic local estimate.

## Verification and next gate

An executable deterministic verifier checked 2,954 cubic-incidence and normalization assertions, including direct finite-difference SU(2) Lie derivatives of randomly drawn noncommuting original-link configurations. This is a calibration, not a simulated coupled quantum vacuum or continuum proof. The complete detailed mathematical note, verifier, execution log and SHA-256 manifest are in the user's Library under `/The Singular Boundary/Proof Audits/R3_GROWING_SUPPORT_WEIGHTED_WILSON_SMEAR_2026-11-06.zip`, ZIP SHA-256 `fd67ddbb7b864b1c3026e52856a29956f7546228ee8b0023fe00245924cd14af`.

**Next P2/T2 task:** derive *locally normalized* fixed-physical-support estimates uniformly in h and growing volume for renormalized curvature after positive-physical-time non-Abelian spatial flow, with signed-covariant derivative control, and separately prove interacting infrared covariance/spectral exclusion. No Observatory canonical theorem counts or proof gates are changed; Penrose and gravity remain separate open work.
