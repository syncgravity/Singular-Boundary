# R3-IR-419 — Center-blind spin-one obstruction to identity-cap survival

Date: 2026-10-30. Exact SU(2) harmonic-analysis counterexample for positive smooth central densities. This is NOT a counterexample in the class of physical Wilson vacuum marginals, whose additional constraints remain decisive.

## Proposition

Let B be any central neighborhood of the SU(2) identity I whose closure excludes -I. There are strictly positive smooth normalized central probability densities rho_+ and rho_- with exactly identical integer-spin character moments for every j=0,1,2,..., yet their masses of B can be made arbitrarily close to 1 and 0, respectively.

In particular the spin-one expectation c_1=int chi_1(U)rho(U)dU can be arbitrarily close to its maximum 3 while the identity-centered cap mass is arbitrarily small. Therefore even an exact lower bound c_1>=0, or a stronger lower bound near 3, alone cannot certify identity-centered cap survival.

## Proof

Let K_s(U) be the normalized SU(2) heat kernel at time s>0, for a bi-invariant Laplacian. It is strictly positive, smooth and central, and converges weakly to delta_I as s goes to zero. Define
rho_+(U)=K_s(U), rho_-(U)=K_s(-U).
The second density is the central translate by the nontrivial center element -I and converges weakly to delta_{-I}. Thus int_B rho_+ ->1 and int_B rho_- ->0 for B with appropriate negligible boundary; in particular for standard angular caps with boundary away from both centers.

The spin-j character satisfies chi_j(-U)=(-1)^{2j}chi_j(U). For every INTEGER j the factor is +1. By Haar invariance, int chi_j(U)rho_-(U)dU=int chi_j(U)rho_+(U)dU. This holds for all integer spins, not only j=1. The spin-one moment tends chi_1(I)=chi_1(-I)=3 in both cases.

For any positive bounded cap multiplier k supported near I and vanishing in a neighborhood of -I, the same construction gives int k rho_- ->0 and int k rho_+ ->k(I), provided k is continuous at I. In particular no positive lower bound proportional to the Haar cap mass follows merely from positive c_1 or from any family of integer-spin character moments.

## Consequence for the Wilson proof program

R3-IR-413 through R3-IR-418 identify and reconstruct the spin-one response at low order in the last neighboring coupling. These are correct finite-volume identities in their stated scope but cannot by themselves close the **identity-centered** target-cap comparison. The target cap requires information in half-integer character channels, or an additional proven Wilson-specific theorem controlling the relative weights of center-related cap regions.

The exact R3-IR-418 positive-weight reconstruction ALSO applies directly to F_k(t)-a0 for the actual positive cap k; its eighth mixed derivative is a genuine sufficient target. A sign theorem for D8 c_1 alone would not prove D8 F_k has a favorable sign at full coupling.

This obstruction concerns the information content of observables in the space of smooth strictly positive central SU(2) probability laws. It does not construct an adverse ground-state distribution for the original-link Wilson Hamiltonian, does not disprove any Wilson-specific cap inequality, and has no implication proving or disproving the continuum Yang-Mills mass gap.
