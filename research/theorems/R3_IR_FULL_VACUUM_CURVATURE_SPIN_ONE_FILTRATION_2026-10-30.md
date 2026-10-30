# R3-IR-413 — Exact spin-one filtration of full physical vacuum cap curvature

2026-10-30. PROVED at finite original-link SU(2) Wilson volume, with the target face deleted and the selected neighboring magnetic coupling t=0. This reduces the complete two-resolvent-channel vacuum curvature, but supplies no favorable sign.

Let x be their shared magnetically private link and y all other links. In the unrestricted original-link Hilbert space H0=a_e(-Delta_x)+H_y. Its unique positive normalized vacuum Omega=omega(y), independent of x, is physical. The perturbation is -t b p_g(x,y), with p_g fundamental in x. For a bounded central target observable k(W_f), W_f=xL(y), write a0=int_SU2 k(W)dW and a1=int_SU2 k(W) chi_1(W)dW.

Analytic perturbation of the nondegenerate normalized positive ground state yields Omega_t=Omega+t u+(t²/2)v+O(t³) in L². The first correction u=b R p_g Omega lies exclusively in the x-spin-1/2 Peter-Weyl sector. The second correction v=2 b² R Q p_g R p_g Omega - b²||R p_g Omega||² Omega lies only in x-spin 0 and spin 1, because the fundamental tensor square decomposes as 0 plus 1. Multiplication by H_y, R and Q preserves each x-isotypic sector, since H0 splits.

Thus the second derivative of rho_t(x,y)=Omega_t(x,y)² is
rho''_0=2u²+2Omega v.
It belongs to the sum of x-spin 0 and 1 sectors. For every fixed y its Haar integral need not vanish, but integration over y is zero because total normalization holds. Since k(xL) is central in its argument, the spin-one Fourier projection of k is (a1/3) chi_1(xL), while its spin-zero projection is a0.

THEOREM (SF-1). Let F_k(t)=<Omega_t,k(W_f)Omega_t> and c_1(t)=<Omega_t,chi_1(W_f)Omega_t>. Then the exact second derivative is
F_k''(0)=(a1/3)c_1''(0). (SF-1)

Proof: pair rho'' with k(xL). At fixed y, the spin-zero component of k is a0, and that contribution integrates to a0 int rho''_0 dxdy =0 by normalization. All x-spins above 1 are orthogonal to rho''_0. The spin-one projection of the central function k(xL) is (a1/3)chi_1(xL), from Peter-Weyl character orthogonality. The remaining pairing gives SF-1. The argument is compatible with Gauss projection because the full-space vacuum and its analytic real continuation are unique, strictly positive and gauge invariant.

For an identity-centered cap with a1>0, the sign of its full, correctly normalized physical vacuum curvature is therefore EXACTLY the sign of c_1''(0). The two-channel resolvent terms of R3-IR-412 both contribute to this single spin-one coefficient and cannot be separately discarded.

No inference for full coupling t=1 follows: higher-order perturbation terms can populate every integer x-spin, and the response can change sign away from zero. This is not a Penrose-uniform signed bound or a continuum mass gap.
