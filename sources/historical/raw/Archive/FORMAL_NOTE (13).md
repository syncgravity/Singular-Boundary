# Localized gauge-covariant Wilson variational comparison and frustration moment

26 October 2026. Independent technical result; **does not** prove continuum-uniform frustration moments, large-field contour bounds, polymer convergence, R3, or R2.

## Assumptions
Let Q be a finite set of m integrated SU(2) links, with every Wilson plaquette involving at most four links, each link incident on at most D plaquettes, and couplings 0<=beta_p,beta'_p<=c_+ lambda for lambda>=1. Condition on all exterior links v. Define S_beta(u;v) as the sum of plaquette defects beta_p[1-Tr W_p(u,v)/2] for those plaquettes meeting Q; other terms cancel in conditional ratios. Assume beta'_p<=beta_p for the affected plaquettes. Let E_beta(v)=min_{u in SU(2)^Q} S_beta(u;v), Z_beta(v)=int exp(-S_beta(u;v)) du (normalized product Haar).

## Theorem 1: nonlinear Wilson minimizer comparison
There are constants C,c>0 depending only on c_+, D and SU(2) geometry such that for all lambda>=1, all exterior configurations v and all Q,

 e^{-E_beta(v)}(c lambda^{-3/2})^m exp(-C m) <= Z_beta(v) <= e^{-E_beta(v)}.

Consequently,

 0<= log [Z_beta'(v)/Z_beta(v)] <= E_beta(v)-E_beta'(v) + (3m/2)log lambda+C' m.

Both E's are gauge invariant as functions of the exterior gauge orbit and minimizers transform as sets covariantly (a unique covariant minimizer is not asserted).

*Proof.* Compactness ensures E_beta attained. Equip SU(2)^Q with the product bi-invariant geodesic metric, take a minimizer u*. The first derivative vanishes at u*. Because SU(2) is compact, the group-multiplication trace is smooth, and each link meets at most D four-link plaquettes, the action Hessian along simultaneous geodesics u_e(t)=exp(t X_e)u*_e obeys |d^2 S_beta(u(t);v)/dt^2| <= C lambda sum_e |X_e|^2, with C independent of Q,v,lambda. For |X_e|<=r lambda^{-1/2}, the action increases at most Cm. Haar volume of the corresponding product of balls is >=(c lambda^{-3/2})^m. The upper bound follows from S>=E. For diluted action Z_beta'<=e^{-E_beta'}; take the ratio. Monotonicity beta'<=beta implies Z_beta'>=Z_beta. Gauge transformations preserve the action, Haar measure and the set of minimizers.

## Corollary: full Gibbs comparison
Let Z_full(beta)=int dv e^{-S_out(v)} Z_beta(v), where S_out is unaffected by dilution. Then

 0<= log [Z_full(beta')/Z_full(beta)]
 <= (3m/2)log lambda+C'm + sup_v [E_beta(v)-E_beta'(v)].

A sharper identity is

 Z_full(beta')/Z_full(beta) = E_{eta_beta}[ Z_beta'(v)/Z_beta(v) ],

and the logarithm is bounded by (3m/2)log lambda+C'm plus

 log E_{eta_beta} exp(E_beta-E_beta').

For Q=J a plaquette-separated set of links, E_beta=sum_e F_e, E_beta'=sum_e F'_e. Thus the original frustration-moment comparison is recovered with a genuine gauge-covariant minimization rather than fictitious independent exterior alignment.

## No automatic uniform bound on the compatible minimum-action shift
The variational theorem **does not** bound E_beta-E_beta' by O(m log lambda). It has only the elementary upper bound 2 sum_{p meeting Q}(beta_p-beta_p')=O(lambda m). This order is realized for certain fixed exterior fields. For a shared link with two opposing staple directions of equal weight lambda, E_beta=2lambda; dilute both weights by a factor (1-theta), obtaining E_beta'=2(1-theta)lambda, so E_beta-E_beta'=2theta lambda. The true exterior Gibbs average may suppress these configurations, but no bound on its exponential moment follows from the local minimizer construction.

## Precise additional required statement
A sufficient independent estimate (currently unproved) is

 log E_{eta_beta} exp(E_beta-E_beta') <= C m(1+log lambda),

uniformly for all selected sparse link sets, for the physical anisotropic continuum coupling family. This is a probabilistic statement about jointly compatible exterior backgrounds, not a deterministic consequence of the gauge-covariant minimizer.

## Optional localized good-background theorem
On any measurable exterior sector A satisfying E_beta(v)-E_beta'(v)<=K m(1+log lambda), the *unnormalized* partition-function contribution obeys

 int_A e^{-S_out}Z_beta' <= exp((K+C)m(1+log lambda)) int_A e^{-S_out} Z_beta.

This does not control the complement A^c, nor the full moment without a tail estimate.

## Audit
**Proved:** exact gauge-compatible constrained minimizer; volume-independent local Gaussian neighborhood bound; O(m log lambda) entropy cost; exact reduction to compatible minimum-action shifts; restricted-good-background comparison.
**Open:** exponentially integrable shifts under actual exterior Gibbs measure; uniform sparse bad-staple pattern suppression; convergent Penrose spacetime residual polymers; continuum Hamiltonian mass gap.
