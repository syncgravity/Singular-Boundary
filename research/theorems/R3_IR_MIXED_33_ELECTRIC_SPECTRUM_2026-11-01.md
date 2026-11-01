# The Singular Boundary — Exact (3,3) Peter–Weyl electric block

**2026-11-01.** Two adjacent faces in the finite open straight original-link SU(2) chain; generator convention `K = l(l+2) + k(k+2) + 2 Σ_a R_l^a ⊗ L_k^a` on the degree-(l,k) harmonic block, where `R_l,L_k` are anti-Hermitian SU(2) vector fields normalized by imaginary quaternion basis /2. With this convention, the shared-link term has eigenvalues `J(J+1)-s(s+1)-t(t+1)` where `s=l/2`, `t=k/2` and `J=|s-t|,...,s+t`.

## Exact general two-face formula

The degree-l SU(2) harmonic/Peter–Weyl matrix-coefficient space has dimension `(l+1)^2`; under SU(2)_L × SU(2)_R it is the representation `(s,s)` with `s=l/2`. The right action on face 1 and left action on face 2 couple spins `s` and `t`. Each spin-J component has dimension `2J+1`, and unused spectator factors contribute `(l+1)(k+1)`. Thus for nonnegative integers l,k,

`κ_(l,k;J) = l(l+2)+k(k+2)+J(J+1)−[l(l+2)+k(k+2)]/4`,

or equivalently `κ_(l,k;J) = (3/4)[l(l+2)+k(k+2)]+J(J+1)`, with multiplicity `(l+1)(k+1)(2J+1)`.

The formula reproduces the previously audited (2,1) eigenvalues 9 (mult 12), 12 (mult 24), and (2,2) values 12 (mult 9), 14 (mult 27), 18 (mult 45). The (3,3) spectrum is **45/2 (mult 16), 49/2 (mult 48), 57/2 (mult 80), 69/2 (mult 112)**. Its exact Haar-L² inverse norm is **2/45**. The dimension check is 16+48+80+112=256.

The minimum eigenvalue for fixed (l,k) is `(3/4)[l(l+2)+k(k+2)]+|l-k|(|l-k|+2)/4`. This gives a spectral positivity estimate across *all two-face irreducible sectors* and therefore the unrestricted mean-zero two-face free-electric inverse bound `||K_2^{-1}||_(L²_0→L²_0)=1/3` (achieved in the (1,0) or (0,1) sector).

## Precise limits

This calculation is an analytic Clebsch–Gordan spectral reduction validated by exact arithmetic. It is **not** an explicit rational inverse of the 256×256 matrix in the previous monomial harmonic basis. The induced coefficient-ℓ¹ norm, which depends on basis normalization, was **not calculated**. No extension to the multi-face noncommuting nearest-neighbor spin-chain spectrum, an intrinsic analytic Fourier norm, or a length-uniform analytic inverse bound is proven here. No interacting λ=1 or continuum mass-gap claim follows.

Run `python verify.py`. It checks exact eigenvalue and multiplicity arithmetic for the prior blocks and (3,3), and verifies representation-dimension sums for all 0≤l,k<16. The arbitrary-l,k formula follows from SU(2) representation coupling, not finite enumeration.