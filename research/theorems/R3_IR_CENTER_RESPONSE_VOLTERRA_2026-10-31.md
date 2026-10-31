# R3-IR — Exact center-response Volterra identity and quantitative source separation

**2026-10-31.** Status: exact finite-volume corollary of the conditional Wilson force-projection theorem and the fixed-volume quadratic center-force theorem. It **does not prove any regulator-uniform endpoint score estimate**.

## Assumptions and notation

For an original-link deleted-target Wilson ground state on a finite SU(2) complex, accept the previously certified conditional identity `(ρK)' = ρ(B+L)` for one boundary link. Here `ρ(p)=(2/π) sqrt(1-p²) ψ(p)²`, smooth positive `ψ` on `[-1,1]`, `K(1)=0`, and `|B(p)|≤C_B(1-p²)` (finite C_B, no mesh uniformity). Set `z=1-p`, `S=B+L`, and `ρ(1-z)=sqrt(z) r(z)` with positive smooth `r(z)` on `[0,z0]`.

## V-1 Exact Volterra identity

For `0<z≤z0`, integrating the conditional equation to the endpoint yields

`K(1-z)=-[1/(sqrt(z)r(z))] ∫_0^z sqrt(v) r(v) [B(1-v)+L(1-v)] dv`.

The endpoint boundary term is zero because K is smooth and K(1)=0. No center-cap probabilities are divided out; the ratio is well defined for every finite volume.

## V-2 Quantitative source separation on a collar

Assume `|∂_z log r(z)|≤M` and `|L(1-z)|≤Λ` for `0≤z≤z0`. Then

`|K(1-z)| ≤ exp(Mz) [(2/3)Λ z+(4/5)C_B z²]`.

Proof: `r(v)/r(z)≤exp(Mz)`, `|B(1-v)|≤C_B(2v-v²)≤2 C_B v`; integrate `sqrt(v)` and `v^(3/2)` exactly. Therefore the explicitly Wilson-local source is second order and the nonadiabatic score response first order. Note M itself depends on the unknown endpoint log-amplitude derivative: `r(z)=(2√(2-z)/π)ψ(1-z)²`. This is a **conditional estimate**, not closure; imposing mesh-uniform M or Λ without proof would be circular.

## V-3 Exact second endpoint coefficient

Let `k1,k2` be coefficients in `K(1-z)=k1 z+k2 z²+O(z³)`, and let `r1=(∂_z log r)(0)=-1/4-2 (∂_p log ψ)(1)`. Write `S(1-z)=S0+S1 z+O(z²)`; here `S0=L(1)`, `S1=-B'(1)-L'(1)`. Then

`k1=-(2/3)S0`, `k2=-(2/5)(S1+r1 k1)`.

This refines the prior `L(1)=-(3/2)k1` endpoint compatibility. The new second coefficient shows explicitly how `B'(1)`, `L'(1)` and the radial density jet enter together; neither sign nor uniform control follows.

## Independent diagnostic

`verify.py` uses mpmath to form 12 smooth central densities `ρ(p)=sqrt(1-p²)exp(2cp+dp²)`, sources `S(p)=p-Eρp` (satisfying the necessary whole-interval zero-mean constraint), `B(p)=b(1-p²)` and `L=S-B`. Direct high-precision Volterra quadrature agrees with both endpoint coefficients to maximum absolute residual 2.16e-13 at z=1e-4. These are synthetic conditional model profiles, **not solutions to the true Wilson ground-state equation**.

## Status and next gate

A regulator-uniform estimate on `L(1)` and its collar supremum cannot be extracted from `B=O(1-p²)` or from the signed balance alone. The density-ratio derivative M also requires independent control. To prove `sup_f 𝔗_(f,h)=o(h^-1/4)`, one needs a noncircular Wilson-specific coercive estimate for the score response or direct one-sided radial score, and a center anti-depletion estimate. The Stage26 M55 reconstruction is a periodic 2+1D Euclidean incidence, not established to be the Hamiltonian regulator of the continuum problem. No covariance or continuum mass-gap theorem follows.