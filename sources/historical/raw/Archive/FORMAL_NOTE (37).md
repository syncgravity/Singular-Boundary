# Relative crossing-face energy in a finite SU(2) Wilson cavity

27 October 2026. Rigorous comparison; unrestricted thin-face logarithmic bound remains open.

## Setting
Finite oriented gauge complex, normalized product Haar measure on SU(2) links, face length bounded by L, incidence bounded by D. Couplings 0<=beta_p<=c_+ lambda, lambda>=2. Q is a set of undeleted plaquettes; K is its link support of k links. Y consists of other undeleted plaquettes touching K. Exterior links v fixed. S_Q and S_Y nonnegative. S_K=S_Q+S_Y and conditional law nu_v=Z_K(v)^-1 exp(-S_K)du. For selected Q faces beta_p>=c_- lambda.

Define M_Y(v)=min_u S_Y(u;v), M_K(v)=min_u(S_Q(u)+S_Y(u;v)), Gamma_Q=M_K-M_Y>=0. Both minima gauge invariant with induced transformations of exterior and interior.

## Theorem 1: relative thermal equipartition, with cutoff logarithm
For every v,
  0<=E_nu_v[S_K-M_K] <= (3/2)k log(lambda)+Ck,
  E_nu_v S_Q <= Gamma_Q(v)+(3/2)k log(lambda)+Ck.
Consequently under the actual cavity Gibbs measure rho,
  E_rho sum_{p in Q} d_p <= (E_rho Gamma_Q+(3/2)k log lambda+Ck)/(c_- lambda).
For nonnegative integer multiplicities a_p<=M, E sum a_p d_p <= M times this.

Proof: compactness gives a minimizer u_*. Wilson action gradients vanish at the unconstrained minimum on SU(2)^k. Along exponential coordinates u_e=u_{*,e}exp(X_e), the absolute second derivative is <= C lambda sum_e |X_e|^2 by bounded incidence, uniformly in v; the gradient of full action vanishes. On product balls |X_e|<=eps/sqrt(lambda), S_K(u)<=M_K+Ck. The normalized Haar measure of each SU(2) ball is >=c lambda^-3/2. Therefore Z_K(v)>=exp(-M_K-Ck)(c lambda^-3/2)^k. KL(nu_v||Haar)=-E S_K-log Z_K>=0 hence E S_K <=-log Z_K <=M_K+(3/2)k log lambda+Ck. Because S_Y>=M_Y, S_Q<=S_K-M_Y; take expectation. The average over v is exact.

## Theorem 2: joint lower-tail consequence, with explicit compatibility gap
If q=|Q| and multiplicities a_p<=M,
 rho_I[sum_{p in Q} a_p d_p <= (2M/(c_- lambda))(E_rho Gamma_Q+(3/2)k log lambda+Ck)] >=1/2
by Markov. If E_rho Gamma_Q<=C k(1+log lambda), obtains cutoff-sharp lower tail for arbitrary Q, including thin, but that hypothesis is presently unproved.

## Proposition: conditional sharp obstruction
A one-link local configuration with two positive Wilson plaquette terms can have S_Q(u)=lambda(1-u dot n) and S_Y(u)=lambda(1+u dot n), from opposite fixed staples. Then M_Y=0, M_K=2lambda, Gamma_Q=2lambda. The joint conditional law is Haar; E S_Q=lambda. Thus no bound Gamma_Q<=C k log lambda can hold uniformly over all frozen exteriors, even at k=1 and bounded incidence. A genuinely probabilistic estimate under the exterior cavity marginal is essential.

## A sharper entropy lemma
The logarithmic entropy loss above can also be expressed exactly as E(S_K-M_K)<=-log[exp(M_K)Z_K], not necessarily small O(k). No general O(k) bound follows from bounded incidence alone; degenerate constrained directions and frustration can affect local phase volume. A lower bound Gamma_Q>=0 and upper bound Gamma_Q<=2 sum_{p in Q}beta_p remain valid, but the latter is O(lambda q).

## Scope and proof status
This is a cutoff-uniform relative *thermal excess* estimate, not an unconditional cutoff-sharp estimate of the absolute Q energy. The missing ingredient is E_rho Gamma_Q<=C k(1+log lambda). Earlier conditional Gibbs concentration about an insertion free-energy or a repair-cost optimization does not independently supply this estimate. No continuum polymer, R3 or R2 mass-gap conclusion is established.
