# R3-IR — Differentiated fiber equation and adverse-slope maximum principle

**Date:** 2026-10-31. **Status:** Exact finite-volume implication for the physical SU(2) deleted-face Wilson ground state, **conditional** refinement criterion. No continuum mass gap is proved.

## Setup

Let the finite-volume original-link, Gauss-invariant, target-magnetic-deleted SU(2) Wilson vacuum be strictly positive and smooth. Its exact conditional angular amplitude is Ψ_f(u)>0, u∈[0,π], symmetric Ψ_f(π−u)=Ψ_f(u), and its complete nonadiabatic conditional fiber energy is U_f(cos u), defined in the archived exact fiber factorization. Set c=A_f/4>0, D(u)=U_f(cos u)−E_0, and s(u)=(log Ψ_f(u))'. Smooth group-center regularity gives s(0)=0, center symmetry gives s(π/2)=0. Assume the exact conditional energy has the corresponding C¹ regularity on [0,π/2], as follows for a smooth positive finite-volume state and a smooth compact-fiber disintegration away from singular endpoints (or impose it explicitly if using a weak-fiber formulation).

The archived exact scalar equation is

    −c(Ψ''+2 cot(u) Ψ') + D Ψ=0.

## Theorem FS-1: exact differentiated fiber-score equation

Differentiating the scalar equation and dividing by Ψ gives

    −c [ s'' + (2 cot(u)+2s(u))s' ] + 2c csc²(u) s(u) = −D'(u).       (FS-1)

Equivalently, the derivative y=Ψ' obeys the linear Schrödinger equation

    [−c(∂²+2cot(u)∂)+D(u)+2c csc²(u)] y=−D'(u) Ψ.               (FS-2)

No unknown extensive constant E_0 occurs in the forcing because its angular derivative is zero. The term 2c csc²(u) is *positive* and is a derivative of the SU(2) radial Haar drift.

## Theorem FS-2: adverse-score maximum principle

Let M=max_{u∈[0,π/2]}[s(u)]_+. If M>0, it is attained at an interior u* with s'(u*)=0, s''(u*)≤0. Apply (FS-1):

    (A_f/2) csc²(u*) M ≤ [−D'(u*)]_+.

Thus

    max_{[0,π/2]}[s]_+ ≤ (2/A_f) sup_{0<u<π/2} sin²(u) [−∂_u U_f(cos u)]_+ ,   (FS-3)

and integrating over the half-interval,

    𝔗_f=∫_0^{π/2}[s]_+du ≤ (π/A_f) sup_{0<u<π/2} sin²(u)[−∂_u U_f(cos u)]_+. (FS-4)

The bound is invariant under U_f↦U_f+constant and avoids a direct bound on the absolute extensive conditional fiber energy. It is independent of the previously archived positive-excess Riccati criterion, although neither criterion is presently proved uniform in the Wilson refinement.

## Sharp condition needed for the physical gate

An independently derived Wilson-specific bound

    sup_{f∈D_R} (1/A_{f,h}) sup_{0<u<π/2} sin²(u) [−∂_u U_{f,h}(cos u)]_+ = o(h^(−1/4))

would imply the archived one-sided radial-current gate. **This estimate is NOT established.** In particular differentiating the conditional fiber energy includes derivatives of the normalized conditional state Φ_f, and cannot be replaced by differentiating the retained plaquette potential alone. There is no independent verification here that the angular slope obeys a favorable sign or regulator-uniform bound for actual Penrose cages.

## Diagnostics

`verify.py` tests FS-1, FS-4 for eleven smooth positive center-symmetric class amplitudes Ψ∝exp(k cos2u+b cos4u), with D reconstructed exactly from the radial equation. This includes center-favoring, center-depleting and non-monotonic profiles, **not Wilson interacting vacua**. Numeric residuals and inequalities are recorded in `results.json`. No tests infer a physical spectral gap.