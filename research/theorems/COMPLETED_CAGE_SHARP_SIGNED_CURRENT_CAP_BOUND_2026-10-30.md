# Completed-cage cap probability from the actual signed radial score — direct proof test

2026-10-30. A direct quantitative implication of the existing physical Wilson target-score identity; no new hypothetical spatial-mixing mechanism. This theorem is finite-volume and holds for any center-even positive radial target density, including the actual completed Wilson target marginal. It does not establish a uniform current estimate.

Let u in [0,pi] be the target SU(2) conjugacy angle and let its physical marginal have Haar-relative density psi(u)^2, normalized against (2/pi)sin²(u)du. By exact deleted-target center symmetry psi(pi-u)=psi(u). Define
T=int_0^(pi/2) [d/du log psi(u)]_+ du,
the existing one-sided adverse signed-current budget. Let a in (0,pi/2) be an identity-cap angular radius and
m(a)=int_0^a (2/pi)sin²(u)du=(a-sin(a)cos(a))/pi.
The cap and its -I mirror each have Haar mass m, so M=2m is Haar mass on [0,a] conditional on the half-interval [0,pi/2].

For every 0<=u<=a<=v<=pi/2, the definition of T yields
psi(v)/psi(u)<=exp(T).
Let A=int_0^a (2/pi)sin²(u) psi(u)^2 du and B=int_a^(pi/2) (2/pi)sin²(v) psi(v)^2 dv. The center symmetry and normalization imply A+B=1/2. Integrating the pairwise inequality over u,v gives
B*m <= exp(2T) A*(1/2-m).
Thus A/(A+B)>=m/[m+exp(2T)(1/2-m)], i.e.

boxed: P_mu(W_f in B_a(I))>= m(a)/[2m(a)+exp(2T)(1-2m(a))]. (CAP-1)

This is a FULL-COUPLING finite-volume bound for the TRUE physical Wilson target marginal; it does not depend on an assumed Feynman–Kac mixing estimate, an interpolation gap, or the total number of original links. The only unknown is the actually interacting signed score budget T.

Sufficient and quantitatively precise half-Haar gate:
CAP-1 >= m(a)/2 whenever
exp(2T) <= [2-2m(a)]/[1-2m(a)],
or equivalently
boxed: T <= (1/2) log[(2-2m(a))/(1-2m(a))]. (CAP-2)
For a->0 this sufficient threshold tends to (log 2)/2 (~0.346574). This is a SUFFICIENT criterion via this sharp bound, not a necessity for half-Haar survival in any specific Wilson vacuum.

Sharpness within the class of positive smooth center-even radial densities: choose smooth log psi increasing from 0 to T in an arbitrarily thin interval straddling u=a and constant elsewhere on each side in [0,pi/2], reflect about pi/2, and normalize. Then inner/outer density ratio tends to exp(2T), and CAP-1 is approached. Smooth transitions can be chosen away from both group centers and with reflection-compatible flat joins. Therefore CAP-1 cannot be improved using only T, center symmetry, and normalization.

Logical comparison with the canonical radial-current gate: the recorded condition T=o(h^(-1/4)) does NOT, by itself, imply the O(1) threshold CAP-2: for example T(h)=log(1/h) is o(h^(-1/4)) but diverges. Accordingly, if the intended proof needs HALF-HAAR cap survival, that older signed-current scaling criterion requires a separately justified intermediate implication beyond CAP-1. This is a precise logical warning, not a refutation of any stronger theorem that uses additional physical inputs.

Conclusion: a direct completed-cage cap bound is established exactly in terms of the existing signed current; no refinement-uniform bound on T has been proved, and no 3+1D mass gap follows.
