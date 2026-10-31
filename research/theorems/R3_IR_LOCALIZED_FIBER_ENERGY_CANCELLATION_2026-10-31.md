# R3-IR — Exact localized fiber-energy cancellation and its limitation

**Date:** 2026-10-31. **Scope:** exact identity for the actual finite deleted-face SU(2) Wilson ground state; separate constructed radial diagnostics are **not** Wilson vacuum measurements. The signed-current gate and continuum mass gap remain open.

## Setup and exact identity

Let `A_f=Σ_(e∈∂f)a_e>0`, `ω(u)=2 sin²(u)/π`, `Ψ(u)=ψ_f(cos u)>0`, `D(u)=U_f(cos u)−E_0`. The actual Wilson fiber factorization yields

`−(A_f/4)(ω Ψ′)′+ω D Ψ=0`.

Multiply by Ψ and integrate on `[0,r]`, where `0<r≤π/2`. Smooth SU(2) center regularity kills the lower boundary term. Integration by parts gives the **exact collar energy balance**

\[
\boxed{\int_0^r\!\omega(u)\Psi(u)^2 D(u)\,du
=\frac{A_f}{4}\omega(r)\Psi(r)\Psi'(r)
-\frac{A_f}{4}\int_0^r\!\omega(u)|\Psi'(u)|^2\,du.}\tag{LE-1}
\]

Center-reflection symmetry entails `Ψ′(π/2)=0`, hence

\[
\boxed{\int_0^{\pi/2}\omega\Psi^2(U_f-E_0)\,du
= -\frac{A_f}{4}\int_0^{\pi/2}\omega|\Psi'|^2\,du\le0.}\tag{LE-2}
\]

This is a cancellation of **the exact complete conditional kinetic and magnetic energy against the true vacuum energy**. It contains all nonadiabatic fiber contributions; no Gaussian or independent-plaquette factorization is used.

For any interval `[r_1,r_2]` replace the boundary term by its difference at the two ends. The conclusion uses no uniform spectral gap.

## Why the sign of the mean cannot bound the positive excess

The Riccati current criterion requires a *different measure* and a positive part:

\[
\mathcal E_f^+ = A_f^{-1}\int_0^{\pi/2}\sin u\cos u\,[D(u)]_+\,du,\qquad \mathfrak T_f\le4\mathcal E_f^+.
\]

Neither LE-1 nor LE-2 bounds `𝔈_f^+`: (i) the integrand in LE-2 is **signed**; (ii) it is weighted by `ωΨ²`, which may be tiny on depleted fibers; and (iii) LE-2 fixes its mean to a *negative kinetic energy*. Replacing the signed mean with its positive part is invalid.

There is an explicit elementary demonstration that even the **magnitude** of the positive excess may be large while the signed cancellation holds. Set `A_f=4` and take any positive center-symmetric smooth radial amplitude `Ψ_k(u)=Z_k^(−1/2) exp(k cos(2u))`, `k>0`, normalized with respect to `ω`. Define the scalar effective excess

\[
D_k(u)=\Psi_k''/\Psi_k+2\cot u\,\Psi_k'/\Psi_k
= -4k\cos(2u)+4k^2\sin^2(2u)-8k\cos^2u.
\]

This smooth even scalar potential obeys the same radial differential equation and LE-2, while `D_k` has large positive lobes and `∫ sin u cos u [D_k]_+` grows with `k`. Importantly `Ψ_k` is *center-favoring*, with `∂_u log Ψ_k=−2k sin(2u)≤0` on `[0,π/2]`, so its adverse current is **exactly zero**. Thus the positive-excess Riccati bound is sufficient but not necessary; it can be extremely loose even for smooth center-favoring solutions.

The `Ψ_k,D_k` family is an **engineered scalar radial model**, not an actual Wilson conditional energy; no Wilson behavior is inferred from it.

## Refinement implication

The original-link local Fisher theorem may bound the *weighted radial kinetic energy*, but LE-2 identifies only the **signed weighted mean** of the fiber excess. It does not turn that bound into a positive unweighted fiber-excess estimate. The missing genuinely Wilson-specific ingredient is a one-sided structure theorem for `D(u)` (e.g. single crossing or a weighted positive-excess estimate), or a collar measure comparison. The finite-volume identity does not establish either condition.

## Reproduction

`verify.py` checks LE-2 for five exactly smooth, Haar-normalized center-symmetric profiles, using analytic expressions for `D_k` and derivatives and deterministic quadrature. Maximum quadrature discrepancy is below `3e−6`. This checks an exact scalar identity, **not** physical interacting-vacuum values.