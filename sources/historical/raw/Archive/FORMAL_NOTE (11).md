# R3: Exact bad-staple frustration cost and the unresolved joint partition comparison
26 October 2026

## Setup
On a finite SU(2) Wilson spacetime complex of bounded link incidence D, write each plaquette defect as d_p=1-p(W_p), p(W)=Tr(W)/2. Assume beta_p in [c_- lambda,c_+ lambda], lambda >=1. Pick a link e, condition on all other links, and use quaternion representation u,q_i in S^3 for all incident plaquettes. The contribution of these plaquettes is S_e(u)=sum_i beta_i(1-u dot q_i)=B-u dot k, B=sum_i beta_i, k=sum_i beta_i q_i, kappa=|k|. The conditional distribution is e^{k dot u}/z(kappa) Haar, z(t)=2I_1(t)/t.

## Theorem 1: exact local frustration identity
F_e:=min_u S_e(u)=B-kappa >=0. In fact
B^2-kappa^2 = sum_{i<j} beta_i beta_j |q_i-q_j|^2,
so (for B+kappa>0)
F_e= [sum_{i<j} beta_i beta_j |q_i-q_j|^2]/(B+kappa).
This is exact and gauge invariant as a function of the exterior links, because it is the minimized local Wilson action.

Fix target i=0 and set r_delta=arccos(1-delta), delta in (0,1]. Let G_e be the event kappa >= c_0 lambda AND angle(n,q_0) <= r_delta/2, with n=k/kappa, where 0<c_0<c_-. Then
G_e^c implies F_e >= min{(c_- - c_0)lambda, c_- lambda [1-cos(r_delta/2)]}.
Since 1-cos(r_delta/2) = 1-sqrt(1-delta/2) >= delta/4,
F_e >= min{(c_- - c_0)lambda, (c_-/4)lambda delta}.
For delta=lambda^{-1/2}, lambda>=1, F_e >= c_* sqrt(lambda) with c_*=min(c_- - c_0,c_-/4).
Proof: if kappa<c_0 lambda, B>=beta_0>=c_-lambda. Otherwise F_e=sum_i beta_i(1-n dot q_i)>=beta_0(1-n dot q_0).

## Theorem 2: exact cavity partition cost
The one-link conditional *unnormalized* partition function, with the defect action convention, is
Z_e(ext)=int exp[-S_e(u)]du=e^{-B}z(kappa).
Compare with the fictitious fully aligned set of staples, Z_e^al=e^{-B}z(B). For B>=1,
Z_e/Z_e^al <= C(1+B)^{3/2} exp[-F_e].
Indeed z(kappa)<=e^{kappa}, whereas z(B)>=c e^B/(1+B)^{3/2}.
On G_e^c, Z_e/Z_e^al<=C(1+D c_+lambda)^{3/2} exp[-c_*sqrt(lambda)].
The denominator is an aligned-staple reference at *the same exterior link configuration*, generally not the conditional partition of any globally compatible Wilson field.

## Theorem 3: multiple nonconflicting core links
For core links e in E_0 such that no plaquette contains two such links, condition on all exterior links. Then Z_{E_0}(ext)=prod_e Z_e(ext). Consequently the ratio to the product of fictitious individually aligned cavity functions obeys
Z_{E_0}(ext)/prod_e Z_e^al(ext) <= [C(1+D c_+lambda)^{3/2} e^{-c_*sqrt(lambda)}]^{|J|}
whenever J subset E_0 are bad-staple links (G_e^c). This is a real simultaneous energy/partition penalty, but **does not yield** an unconditional Gibbs probability bound without a bound on the ratio of the globally integrated aligned reference to the true partition function (or an explicit measure-preserving exterior repair map with bounded Jacobian and energy cost). It also does not imply a bound on the event 'at least one bad staple' exponential in |E_0|; that event is a union and may contain configurations with only one bad staple.

## Logical obstruction and correction to previous requested target
The earlier decomposition P(L_X)<=P(L_X intersect all good)+P(L_X intersect at least one bad) cannot give an exp(-a|X|) bound merely by showing that a *cluster of all bad* links is rare. A single bad link can occur while all other core links are good. A correct contour proof needs a sum over patterns J of bad links, with joint probabilities or repair costs proportional to |J|, and simultaneous good-core failure probabilities proportional to |E_0\J|. If a uniform conditional pattern comparison P(L_good on E_0\J AND G_good AND G_bad(J)) <= q^{|E_0\J|} r^{|J|} were established, summing patterns would yield (q+r)^{|E_0|}; no such estimate is established here.

## Remaining core problem
Establish a gauge-covariant exterior repair/partition comparison with cost at most exp(C |J| log lambda) and benefit exp(-c sqrt(lambda)|J|), simultaneously for any separated collection J and uniformly in the Penrose cutoff/volume, or derive an alternative joint contour bound via localized background-field conditional integration. Verify that the repaired boundary configurations respect plaquette Bianchi constraints, temporal links, and noncommutative holonomies. This is not a consequence of local cavity identities.

No unconditional all-contour suppression, residual polymer activity convergence, R3 or R2 mass gap is established.
