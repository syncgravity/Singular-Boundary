# R3-IR-415 — Sharp spin-half compression and asymmetric full Wilson curvature bound

2026-10-30. Proved finite-volume SU(2) Wilson result at zero last-neighbor coupling; favorable full-coupling cap comparison remains OPEN.

Let f be the deleted target face, g its final neighboring face with coupling t=0, x their magnetically private link, and H0=a_e(-Delta_x)+H_y. The normalized positive vacuum Omega=omega(y) is independent of x and Gauss invariant. Let p_g be the fundamental neighboring plaquette, b_g its magnetic coefficient, R=Q(H0-E0)^(-1)Q and c1(t)=<Omega_t,chi_1(W_f)Omega_t>.

The verified two-channel curvature is
c1''(0)=4 b_g² <chi_1(W_f)Omega,R Q p_g R p_g Omega>+2 b_g² <R p_g Omega,chi_1(W_f)R p_g Omega>.
The first term's inner product is at most 1/(3a_e²) in absolute value, by the private-link half-spin and spin-one kinetic gaps, as in R3-IR-414.

NEW LEMMA. On the real spin-half SU(2) link coefficient subspace, identified with linear functions on the quaternion unit 3-sphere S³, the compression of multiplication by chi_1(xL(y)) has eigenvalues 1,-1/3,-1/3,-1/3 for every fixed environment y.

Proof. Write q=(q0,q1,q2,q3) with sum q_mu²=1 and normalized Haar sphere measure. For a rotated unit quaternion axis n determined by L(y), chi_1(xL)=4(n dot q)²-1. For each normalized linear coordinate q_mu, E[q_mu²]=1/4. Haar fourth moments are E[q_mu^4]=1/8 and E[q_mu² q_nu²]=1/24 for mu!=nu. In coordinates where n is axis zero, the compressed matrix is diagonal by parity. Its eigenvalue along n is 4*(1/8)/(1/4)-1=1; its three transverse eigenvalues are 4*(1/24)/(1/4)-1=-1/3. QED.

Since u=R p_g Omega lies in the private-link spin-half subspace, for all environmental states and arbitrarily strong retained Wilson couplings,
-(1/3)||u||² <= <u,chi_1(W_f)u> <= ||u||².
Also ||u||<=2/(3a_e). Inserting this sharp compression bound and the previous absolute first-channel estimate into the exact vacuum curvature gives

boxed: -(44/27)(b_g/a_e)² <= c1''(0) <= (20/9)(b_g/a_e)². (SC-1)

The lower constant is 4/3+8/27=44/27; the upper is 4/3+8/9=20/9. Both improve on the symmetric R3-IR-414 interval [-4,4](b_g/a_e)². For a bounded central cap k with positive spin-one coefficient a1=int k chi_1, the exact filtration gives F_k''(0)=(a1/3)c1''(0); the corresponding asymmetric interval is obtained by multiplying SC-1 by a1/3. If a1<0 the endpoints reverse.

The compressed second-channel bound is optimal for arbitrary spin-half functions at fixed environmental y; simultaneous saturation with the first-channel bound by an actual Wilson vacuum is not claimed. The lower endpoint is still negative and scales like (b_g/a_e)², so it does not prove positive curvature, nonperturbative cap survival or continuum Yang-Mills mass gap. This is a strict sign-sensitive strengthening of the earlier gap-free result, not a solution of the infrared obligation.
