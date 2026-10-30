# Localized Gibbs concentration of compatible staple frustration: exact sensitivity and a noncircular criterion

Date: 2026-10-26. Status: unconditional finite-support sensitivity bound proved; weak-bare-coupling concentration and mean free-energy estimate remain open.

## Setting
Let K be a finite bounded-incidence spatial-temporal cell complex, link variables U_l in SU(2), plaquette defects d_p(U)=1-(1/2)Tr W_p(U), Wilson Gibbs measure proportional to exp(-sum beta_p d_p) product Haar. Assume beta_p <= c_+ lambda. Let J be links such that no plaquette contains two links of J. Let V be the complementary links. For e in J, write incident action S_e(u;V)=B_e-u.q_e(V), B_e=sum_{p contains e} beta_p, kappa_e=|q_e|, F_e(V)=B_e-kappa_e. F_J=sum F_e. The exterior marginal eta_beta(dV) is proportional to exp(-S_out(V)) prod_e exp(-B_e) z(kappa_e(V))dV.

## Theorem 1: localized exterior sensitivity
For exterior configurations V,V' differing only at one link l, and d_SU2(V_l,V'_l)=r <= pi, one has
 |F_J(V)-F_J(V')| <= C_D c_+ lambda r,
where C_D depends only on maximum plaquette incidence D and plaquette length four, not on |J|, ambient volume, or h. More precisely
 |F_J(V)-F_J(V')| <= sum_{e in J} sum_{p containing e,l} beta_p d_SU2(V_l,V'_l),
where d_SU2 is the SU2 round geodesic metric (unit-quaternion S3). Indeed quaternion staple directions are products of links and their inverses, each 1-Lipschitz in a single factor; | |k|-|k'| |<=|k-k'|. Each p containing l can contain at most one selected link. Hence coefficient <= D c_+ lambda. Local Lipschitz sensitivity is O(lambda), not O(log lambda).

For smooth variations of V, the weak gradient exists a.e., and
 sum_{l outside J} |nabla_l F_J|^2 <= C_D (c_+ lambda)^2 |J|.
This uses bounded exterior link incidence per selected link and Cauchy-Schwarz. SU2 geodesic coordinate conventions affect C_D only.

## Theorem 2: conditional Gibbs concentration under a separately established logarithmic Sobolev bound
Suppose the exterior marginal eta_beta satisfies Ent_eta(f^2) <= (2/rho_h) integral |nabla f|^2 d eta, in the product-link geodesic metric (or with correctly defined gauge quotient). Then the Herbst argument and the gradient estimate imply, for all real t,
 log E_eta exp[t(F_J-E_eta F_J)] <= t^2 C_D(c_+ lambda)^2 |J|/(2rho_h).
In particular, eta(F_J-E F_J >= r |J|) <= exp[-rho_h r^2 |J|/(2 C_D c_+^2 lambda^2)]. This is conditional on rho_h and not a mass-gap theorem. On unconstrained gauge-field spaces, unremoved gauge degeneracy does not itself preclude measure LSI on compact product group, but rho_h may degrade with size; no uniform bound is available here.

Even if rho_h~lambda, the t=O(1) moment correction is O(lambda |J|), which fails the desired O(|J|log lambda). Moreover concentration only controls fluctuation around E F_J, not that mean. Thus proving an LSI of natural Gaussian strength alone cannot close the target.

## Theorem 3: exact free-energy criterion (known, included to audit circularity)
For a=1-theta, 0<theta<1, proportional dilution of all p touching J, one has for a cutoff- and volume-independent C_a,
 |log [Z(beta')/Z(beta)] - log E_eta exp(theta F_J)| <= C_a |J|.
Hence a bound log E_eta exp(theta F_J) <= C|J| log lambda is equivalent to the demanded selectively diluted thin-support free-energy bound, up to O(|J|). One cannot assume either to prove the other.

## Corollary: a legitimate sufficient dynamical input
If, independently, E_eta F_J <= M |J|(1+log lambda) and rho_h >= c lambda^2/(1+log lambda), then
 log E_eta exp(theta F_J) <= [theta M+theta^2 C_D c_+^2/(2c)] |J|(1+log lambda),
proving the desired exponential moment. Both premises are open, and the rho_h requirement is far stronger than natural small-field Gaussian scaling. This corollary is NOT a result for Penrose Yang-Mills.

## Physical/logic status
PROVED: exact exterior sensitivity, volume-independent Lipschitz/gradient estimates, conditional Herbst implication, exact equivalence of frustration moment and thin free-energy ratio.
NOT PROVED: Gibbs mean of F_J at O(|J|log lambda); continuum uniform exterior LSI/mixing sufficiently strong; joint bad-staple suppression; connected polymer bound; continuum R3/R2 mass gap.
