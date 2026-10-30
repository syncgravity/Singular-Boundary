# Audit: local undeleted curvature and absolute compatible-energy tails

## Setup
Let K be a finite bounded-incidence 3D spacetime cell complex, P0 its undeleted plaquettes, beta_p in [c_- lambda,c_+ lambda], lambda >= 2. Let rho_0(dU)=Z_0^{-1} exp[-S_0(U)]dU, S_0=sum_{p in P0} beta_p d_p(U), d_p=1-(1/2)Tr W_p in [0,2]. Faces have uniformly bounded perimeter and links uniformly bounded incidence. Let N_E be the number of integrated links.

## Theorem 1: Global curvature density, no independence assumptions
There exists C, independent of lambda, volume and plaquette deletions, such that
 E_{rho_0} sum_{p in P0} d_p <= C N_E(1+log lambda)/lambda.
Proof: E S_0 <= -log Z_0 from D_KL(rho_0||Haar)= -E S_0-log Z_0 >=0. A product of SU(2) geodesic balls radius c lambda^-1/2 about identity has volume >=(c' lambda^-3/2)^N_E and all retained plaquette defects <= C/lambda, so Z_0 >= exp[-C N_E](c' lambda^-3/2)^N_E. Finally use beta_p >= c_-lambda.

## Corollary 1: uniform-in-volume sparse density, but not prescribed support
Let H_delta= {p in P0: d_p >= delta}. Then
 E |H_delta| <= C N_E(1+log lambda)/(lambda delta).
For delta=lambda^-1/2, E |H_delta|/N_E <= C (1+log lambda)/sqrt(lambda). This controls the proportion of bad faces but does not control a prescribed thin face set Q.

## Theorem 2: absolute compatible minimum via exterior-curvature filling, conditional on geometry
For a selected interior-link set I with compatible energy E_I(v)=min_u S_I(u,v), assume a deterministic gauge-compatible completion for which
 E_I(v) <= C_fill lambda sum_{q in N(I)} a_q d_q(v), a_q <= M,
where N(I) are undeleted exterior plaquettes and total support A=sum_q a_q. This is a geometric hypothesis (e.g. a bounded filling construction), not a probabilistic claim. Then under rho_0,
 P(E_I > t) <= (C_fill M lambda/t) E sum_{q in N(I)}d_q
 <= C N_E(1+log lambda)/t.
The last inequality is ambient-volume dependent. To deduce a cutoff- and volume-uniform tail centered at |I|log lambda requires an independent localized moment/tail for the specified exterior curvature set. Such a bound does not follow from this theorem.

## Theorem 3: an unconditional absolute tail with a volume penalty
E_I(v) <= S_I(u;v) pointwise for any internal u. For the full Wilson Gibbs law mu on all links, E_I(U_ext) <= S_I(U). Moreover for theta in (0,1),
 mu(E_I >= t) <= exp[-theta t] Z(beta^{theta,I})/Z(beta),
where beta^{theta,I}_p=(1-theta)beta_p for p incident on I and other beta unchanged. Bounding numerator Z(beta^{theta,I})<=1 and denominator Z(beta)>=exp[-C N_E(1+log lambda)] yields
 mu(E_I>=t) <= exp[-theta t+C N_E(1+log lambda)].
This inequality is unconditional but not support-local. It must not be interpreted as proof of the desired O(|I|log lambda) absolute tail.

## Exact insertion-centering theorem
Let rho_cav be the exterior marginal with incident I plaquette terms removed and eta the full exterior marginal; Z_I(v)=integral over u exp[-S_I(u;v)], a=E_{rho_cav}Z_I, F_I=-log a. Since Z_I(v)<=exp[-E_I(v)],
 eta(E_I>= F_I+s) <= exp[-s], s>=0.
There is no independent bound on F_I herein. This centered estimate cannot be promoted to the absolute tail by removing F_I.

## Countercheck on applicability
The global result controls a randomly selected plaquette or the total density. The desired statement controls every adversarial thin support uniformly; the former does not imply the latter. No general SU(2) Wilson Griffiths monotonicity theorem has been invoked. The regular-hypercubic ultraviolet stability theorem of Balaban is distinct from these Penrose arbitrary-support statements.

## Verdict
Under the stated assumptions, the unconditional cutoff-stable global defect density and an ambient-volume-penalized absolute tail are proven. The volume-independent arbitrary thin-support defect estimate and absolute compatible-minimum energy tail remain open. A proof would require a separately established localization or a new constructive gauge-covariant Gibbs comparison.
