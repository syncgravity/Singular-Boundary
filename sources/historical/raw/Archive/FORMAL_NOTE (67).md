# Local good-field probability and nonlinear SU(2) extension: exact audited estimates
2026-10-27

## Model
Finite oriented 3D cell complex, SU(2) Wilson measure dmu=Z^{-1}exp(-S) product normalized Haar. Each link has <=Delta incident faces, each face boundary length <=L, c_-lambda <= beta_p <= c_+lambda, lambda>=2. Select K of k adjustable links and freeze complementary variables v. Let S_K(u;v) contain all plaquettes touching K, and M_K(v)=min_u S_K(u;v). All terms independent of u cancel in the conditional law.

## Proposition 1: unconditional support-local thermal good event
There is a C depending only on Delta,L,c_+ such that for every s>=0, every v,
 P(S_K-M_K > (3k/2)log(lambda)+Ck+s | v) <= exp(-s).
In particular G_{K,s}={S_K-M_K <= (3k/2)log(lambda)+Ck+s} satisfies mu(G_{K,s}) >= 1-exp(-s), uniformly in volume, cutoff, exterior v and Penrose combinatorics subject to incidence bounds.
Proof: minimizer u_*(v), Hessian of S_K along product geodesics uniformly <= C lambda per coordinate in operator norm after bounded incidence. Gradient at minimizer zero on closed smooth manifold. On product geodesic balls radius c/sqrt(lambda), S_K <= M_K+Ck. Haar ball lower bound (c' lambda^{-3/2})^k. Thus Z_K(v)>=exp[-M_K-Ck](c'lambda^{-3/2})^k. On {S_K-M_K> L+s}, numerator <= exp[-M_K-L-s] since Haar volume <=1. Divide.

## Proposition 2: exact nonlinear SU(2) chain extension
For h in SU(2), theta=arccos(tr(h)/2) in [0,pi], n>=1, define E_n(h)=min_{g_1...g_n=h} sum_{i=1}^n beta_i d(g_i), beta_i in [c_-lambda,c_+lambda]. Then
 (2 c_-lambda/(pi^2 n)) theta^2 <= E_n(h) <= (c_+lambda/(2n)) theta^2.
Proof: triangle inequality theta(h)<=sum theta(g_i), d(g)>=2theta(g)^2/pi^2; upper by geodesic roots g_i=exp((log h)/n), d(g_i)<=theta^2/(2n^2). Cut locus h=-I admits a geodesic logarithm.
This is a serial holonomy-extension theorem, NOT a statement that every Penrose prism buffer can realize such a factorization without crossing-action changes.

## Proposition 3: if independently a geometric extension bound holds, the good-field probability converts to an absolute bound
Assume for every exterior v the selected pivot-block minimum admits M_K(v)<= C_ext lambda theta(H(v))^2/n + A k, where H is a gauge-covariant boundary holonomy and n is a verified effective extension length. Then, for all s>=0,
 mu(S_K > C_ext lambda theta(H)^2/n + Ak + (3k/2)log lambda+Ck+s)<=e^{-s}.
If additionally there is an independently proved boundary-holonomy moment E_mu exp[t C_ext lambda theta(H)^2/n] <= exp(C_H k) at fixed t in (0,1), then by conditional exponential tail and tower property,
 E_mu exp[t S_K] <= exp[t(Ak+L_k)+C_H k]/(1-t), L_k=(3k/2)log lambda+Ck; consequently
 mu(S_K >= Ak+L_k+(C_H/t)k+(1/t)log(1/(1-t))+u) <= exp(-t u).
The boundary-holonomy exponential moment is NOT established for arbitrary Penrose cavities; the geometric extension also is NOT verified for arbitrary supports.

## Proposition 4: noncircular deterministic good/bad decomposition for direct insertion
For V_Q>=0 and an arbitrary good event G with mu(G)>=1-e^{-s}, the insertion free energy F_Q=-log E_mu exp(-V_Q) obeys F_Q <= F_{Q|G}-log(1-e^{-s}). This alone gives no bound on F_{Q|G}; regularity of the undeleted action is insufficient to bound the *inserted* action. In particular a free deleted plaquette may retain Haar holonomy while S_K-M_K=0.

## Warning: a prior pitfall
A true upper-tail estimate for a compatible minimum under the insertion-included marginal must not be automatically attributed to the cavity marginal. The two exterior marginals differ by the insertion's unknown normalization. Any statement that the cavity relative defect is exponentially suppressed solely because the inserted theory penalizes it is circular.

## Status
Established: local conditional thermal excess tail independent of exterior, and exact serial holonomy extension scaling, plus a conditional probabilistic combination.
Unproved: Penrose-uniform effective extension network for arbitrary cavity supports; independent exponential moment for boundary holonomy; absolute support-local curvature tail; arbitrary insertion theorem, RG and mass gap.
