# R3-IR — Exact deleted-face U(1) flux-shift symmetry and the nonabelian gate

**Date:** 2026-10-31. **Status:** finite-volume *abelian* Wilson theorem, not an SU(2) deleted-face current estimate or a Yang–Mills gap.

## Setup and theorem
Let G=(V,E,F) be a connected finite cellulation of a topological disk, with freely integrated boundary links and no fixed boundary holonomies. Give each oriented edge an angle θ_e∈R/(2πZ), Haar product measure, and let B∈Z^{F×E} be the oriented face-edge incidence matrix. For a disk, B has full row rank (the cellular boundary ∂_2 is injective, since H_2(disk)=0).

Consider the original-link electric U(1) Hamiltonian

H_f^-=−Σ_e a_e ∂²_{θ_e}+Σ_{g≠f} b_g[1−cos((Bθ)_g)], a_e>0, b_g≥0.

Then the unique normalized strictly positive ground state Ω_f^- has an **exactly uniform deleted-face flux marginal**: the random variable (Bθ)_f mod 2π under Ω²dθ/(2π)^E is uniform. Its density relative to Haar equals 1. In particular its positive logarithmic flux variation is exactly zero for all finite sizes and all coefficients.

## Proof
Because B has full row rank, for each f there exists c∈R^E with Bc=e_f, for instance c=Bᵀ(BBᵀ)^{-1}e_f. For all real t define T_tψ(θ)=ψ(θ+tc). Translation is a unitary Haar isometry and commutes with each constant-coefficient link Laplacian. Moreover, (B(θ+tc))_g=(Bθ)_g+tδ_fg modulo 2π, so every *retained* magnetic term g≠f is fixed. Thus [H_f^-,T_t]=0 for every real t. By positivity improvement on the compact connected link torus, the bottom eigenvalue is simple and Ω>0. Therefore T_tΩ=Ω (rather than a nontrivial phase, since both are normalized strictly positive). Hence Ω²dμ is T_t-invariant, while T_t shifts only the target flux by t. Its flux marginal is translation invariant on U(1), and therefore Haar-uniform.

The statement also holds with other gauge-invariant interactions that are functions solely of retained fluxes, provided the kinetic operator has constant coefficients and preserves the continuous shift symmetry.

## Nonabelian limitation
For SU(2), Haar class-density and the original-link Laplace–Beltrami kinetic operator are not a constant-coefficient abelian flux torus. The vector c implements **additive abelian flux shifts**, not an SU(2) symmetry of the product-link Laplacian that independently translates one face holonomy while leaving all retained Wilson traces fixed. Accordingly the U(1) theorem cannot be imported to SU(2). SU(2) deleted-face center parity is only a discrete constraint and does not imply radial flatness. The missing actual SU(2) Wilson-specific signed prefix-flux estimate remains open.

## Verification
The attached `verify.py` constructs oriented face-edge incidence matrices for rectangular 1×1, 2×2, 3×4 and 7×5 planar disks, checks full row rank and solves Bc=e_f for every face with residual below 1e−12. These finite geometry checks verify the algebraic existence of shifts; the positivity and uniqueness portion is analytic.

**Not proved:** a favorable cumulative reference flux for the actual SU(2) completed Penrose cage; sup_f 𝔗_(f,h)=o(h^(−1/4)); connected covariance or continuum Yang–Mills mass gap.