# R3: Independent localized-curvature audit and annealed thin-support theorem

## Scope
Finite bounded-incidence SU(2) spacetime complex, cavity Wilson law rho_0 with retained plaquettes P_0, N=|P_0|, L links, beta_p in [c_-lambda,c_+lambda], lambda>=2. d_p=1-Tr W_p/2. Assume N >= c_* L (to express average per face; without that use L/N explicitly). No translation symmetry or independence presumed.

## Theorem 1 (global bound revisited)
Relative entropy with respect to normalized Haar product gives E_rho S_0 <= -log Z_0. Integrating balls of radius lambda^-1/2 around flat identity gives -log Z_0 <= C L(1+log lambda). Thus sum_{p in P_0} E d_p <= C L(1+log lambda)/lambda.

## Theorem 2 (annealed thin-support, exact)
Take any distribution nu over subsets Q of P_0, independent of the gauge field, satisfying inclusion probabilities pi_p=P_nu(p in Q) <= A q/N for every p, where every sampled Q has |Q|=q. Then
E_{Q~nu} E_{rho_0} sum_{p in Q} d_p = sum_p pi_p E d_p <= CA(q L/N)(1+log lambda)/lambda.
If N >= c_* L, this is <= C'(A/c_*)q(1+log lambda)/lambda. Joint Markov over Q and U gives
 (nu x rho_0){sum_{p in Q} d_p <= 2 C' (A/c_*) q(1+log lambda)/lambda} >= 1/2.
For any eta in (0,1), at least fraction 1-eta of sampled Q satisfy rho_0{sum_Q d_p <= [2 C' A/(c_* eta)] q(1+log lambda)/lambda} >= 1/2. Proof: define b(Q)=E_rho sum_Q d_p, Markov over Q shows at least 1-eta have b(Q)<=C' A q(1+log lambda)/(c_*eta lambda); Markov under rho shows probability <=2b(Q) at least 1/2. This is a genuine joint lower-tail bound for typical prescribed supports, but NOT for every prescribed support; sampling distribution must have bounded inclusion density. For repeated filling faces a_p<=M multiply threshold by M. No nonlinear independence is assumed.

## A caution on pointwise local bounds
The bound for a fixed Q cannot be inferred from the global estimate: finite positive numbers {a_p} with sum <= CN log lambda/lambda may be concentrated on one chosen p. Uniformly bounded geometric incidence does not add symmetry of the Gibbs law, nor does it imply the target local free-energy deletion bound.

## Exact source/ratio gate
For fixed Q,
F_Q=-log E_{rho_0} exp(-sum_{p in Q} beta_p d_p).
A fixed-support bound F_Q<=Cq log lambda is equivalent to a polynomial lower bound on the insertion Laplace transform; a bound on the first moment under rho_0 would be a sufficient strictly stronger input by Jensen. The prior local conditional relative-entropy bound includes an unresolved crossing-face compatibility gap. An annealed estimate is not a pointwise substitute.

## Status
Proved: global bound, annealed typical-support joint lower tail, all finite-volume and correlation-preserving. Unproved: pointwise prescribed arbitrary Penrose thin-support curvature estimate; absolute compatible-minimum tail; arbitrary-support logarithmic insertion bound; continuum RG/mass gap. Hypercubic multireflection source results require additional regular-grid structure and do not directly establish Penrose cavity result.
