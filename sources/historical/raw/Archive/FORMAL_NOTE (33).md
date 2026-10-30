# Optimized correlated shield repair: exact joint-minimum comparison and remaining obstruction

Date: 2026-10-26. This memorandum does not prove the arbitrary-Penrose-support probability estimate.

## Setup
Finite SU(2) Wilson cell complex, normalized Haar link measure. I interior links (m), H exterior shield links (r), w all remaining exterior links. S_out(h,w) contains undeleted plaquettes, S_I(u,h,w) contains all plaquettes incident on I; no omitted spatial or temporal terms. Assume plaquette lengths and link incidences bounded and 0 <= beta_p <= c_+ lambda, lambda >= 1. The cavity conditional law of h given w has density proportional to exp(-S_out(h,w)). Put
M_out(w)=min_h S_out(h,w), M_joint(w)=min_{u,h}(S_out(h,w)+S_I(u,h,w)), Gamma(w)=M_joint(w)-M_out(w)>=0.
Let E_I(h,w)=min_u S_I(u,h,w).

## Theorem 1 (optimized shield-repair probability)
There exist c,C>0 depending only on degree, face length and c_+ such that for every w
rho_I(E_I(h,w) <= Gamma(w)+Cr | w) >= (c lambda^{-3})^r exp[-Gamma(w)-Cr].

Proof: choose a joint minimizer (u*,h*); then S_out(h*,w)-M_out(w) + S_I(u*,h*,w)=Gamma(w), with both nonnegative. In a product of r SU(2) balls of radius eps/lambda about h*, bounded incidence and the global Lipschitz property of 1-(1/2)Tr W guarantee changes of both S_out and S_I of at most Cr. Therefore E_I(h,w) <= S_I(u*,h*,w)+Cr <= Gamma+Cr in the balls. The normalizing denominator of rho_I(h|w) is <=e^{-M_out(w)}. The numerator density in balls >=exp[-S_out(h*,w)-Cr]. Each ball has normalized Haar mass >= c lambda^-3. Since S_out(h*,w)-M_out(w)<=Gamma, the result follows. The observable event is gauge invariant.

## Theorem 2 (joint minimum gives a conditional partition comparison)
Define the conditional insertion ratio
R(w) = [int dh du exp(-S_out(h,w)-S_I(u,h,w))]/[int dh exp(-S_out(h,w))].
Then
(c lambda^{-3/2})^{m+r} e^{-Gamma(w)-C(m+r)} <= R(w) <= 1.
The lower bound integrates an (m+r)-link product of radius c/sqrt(lambda) around a joint minimizer: at the minimizer the full action has vanishing first derivative in each internal direction, and a uniformly bounded-incidence Hessian <= C lambda gives at most C(m+r) excess action. The numerator >= exp[-M_joint-C(m+r)] (c lambda^-3/2)^{m+r}; denominator <=exp(-M_out). Upper bound S_I>=0.

## Integrated criterion
Let W={w: Gamma(w)<= K m(1+log lambda)} and suppose r<=a m and rho_I^w(W)>=exp[-K' m(1+log lambda)]. Theorem 1 yields
rho_I(E_I<= [K(1+log lambda)+Ca]m) >= exp[-C(K,K',a) m(1+log lambda)].
Theorem 2 also yields the desired insertion free energy bound. These are conditional conclusions, not proofs of W probability.

## Crucial noncircularity audit
Gamma(w) is the minimum added joint action when the deleted plaquettes are reinserted, measured relative to the optimal undeleted action with w frozen. It can be of order lambda already in a fixed-exterior frustrated example. Showing that Gamma is logarithmically small on a polynomial-probability event W is an independent nontrivial dynamical assertion. Since its cavity average controls insertion free energy up to local entropy factors, assuming such a W without proof would be circular.

For an arbitrary interior Penrose thin support, the argument has NOT verified either that an O(m) shield contains an optimizing joint repair (it always optimizes over any preselected H only), or that rho_I^w(Gamma<=Km log lambda) is polynomially large. Thus arbitrary-support logarithmic insertion free energy, large-field contour suppression, residual polymer convergence, and the SU(2) Yang-Mills mass gap remain open.
