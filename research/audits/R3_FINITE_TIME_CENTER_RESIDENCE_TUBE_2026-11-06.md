# R3 / P2–T2: Finite-time unstable-center residence tube
**Research audit 2026-11-06. Finite 3D original-link cubic SU(2) regulator only; independent mathematical review pending. All P0–P5/T0–T5 and continuum mass-gap gates remain OPEN.**

Previous PR #85, the center-saddle cap and null-basin audit, was merged into main as commit `1d6ba8a865f5bac9d09e5950c9f38c40d75d3eb8` after its archived checker independently reproduced 30,448 deterministic assertions.

## Nonlinear finite-time residence theorem

Let S(U)=Σ_p(1−½tr₂ U_p) on SU(2)^E and Φ_s be its original-link negative gradient flow. Fix a center-valued critical configuration U* with an unstable unit eigenvector v of L=−Hess S(U*) and eigenvalue λ>0. In product exponential coordinates a about U*, the exact vector field is ȧ=La+N(a); smoothness gives finite regulator-dependent C_(h,R), r₀>0 such that ||N(a)||≤C_(h,R)||a||² when ||a||≤r₀. For a trajectory remaining within the global product metric ball of radius r≤r₀ throughout [0,s], projecting on v and using backward variation of constants proves

|⟨v,a(0)⟩| ≤ r exp(−λs) + [C_(h,R)/λ]r²(1−exp(−λs)).

For one interior negative center link (others positive), exact face-edge incidence gives Hess S=(1/4)Bᵀ diag(z_p)B, with Rayleigh quotient −1 on that link, hence an eigenvalue λ≥1 of L. The result retains the **quadratic nonlinear floor** and does not assert a global contraction or continuum-uniform escape bound.

## Interacting-vacuum residence probability

The actual finite-regulator Gauss-invariant ground state Ω>0 of H=αΣ_e(−Δ_e)+βS, α=g₀(h)²/(2h), β=2/[g₀(h)²h], defines ν=Ω² Haar. Under the established previous link kinetic bound ∫|∇_eΩ|²≤32/g₀(h)^4, a localized one-dimensional H¹ slab estimate in the unstable direction, combined with product exponential-chart Haar Jacobian comparability, yields universal constants C,r*>0 such that for r≤min(r₀,r*):

ν({||a(Φ_t U)||≤r for all 0≤t≤s}) ≤ min{1, C[exp(−λs)+(C_(h,R)/λ)r][1+32|E|r²/g₀(h)^4]}.

Derivation: use an exponential-coordinate cutoff supported in the radius-2r ball, integrate one-dimensional Sobolev over the line a=xv+y, and control its directional derivative by Σ_e∫|∇_eΩ|². The product Haar Jacobian differs by only exp(O(||a||²)) from its value at the origin. This is a genuinely coupled-vacuum, finite-regulator residence **probability** estimate, not a full-orbit estimate.

At s=τ/h² the exponential term is exp(−λτ/h²), but the nonlinear remainder C_(h,R)r and |E|/g₀⁴ factor persist. C_(h,R) has not been shown uniform in refinement; the tube is a ball in all link coordinates around a specified center configuration, rather than a gauge-orbit or fixed-physical-support set. Neither fixed physical radius renormalized curvature nor any continuum spectral mass gap follows.

## Verification and files

The independent local deterministic verifier passed **631** assertions across cubic n=2…6 and scalar Riccati residence envelopes. The scalar model is only a calibration of the variation-of-constants formula; it is not a coupled non-Abelian simulation. Full mathematical derivation, executable script, test log, SHA-256 manifest, and CRC-verified ZIP were uploaded to Library /The Singular Boundary/Proof Audits/, filenames `R3_FINITE_TIME_CENTER_RESIDENCE_TUBE_2026-11-06.md` and `R3_FINITE_TIME_CENTER_RESIDENCE_TUBE_2026-11-06.zip`. The ZIP SHA-256 is `01730be18da934b9d1afb6706f027a78d8bee84de8d834b5b6839f5d13d3f439`. Do not promote canonical claims or Observatory gates.

**Next open obligation:** gauge-orbit and fixed-physical-support finite-time residence estimates, uniform constants in h and volume, and a renormalized positive-flow-time curvature measure bound under the actual interacting quantum vacuum.
