# Wilson-specific Hessian and connected large-field audit — 26 October 2026

## Setup and normalization
Finite SU(2) 3D Penrose-prism spacetime complex, oriented links `e` and spatial or temporal plaquettes `p`, each of length at most four, bounded link-incidence `D`; full positive Wilson measure `exp[-sum_p beta_p(1-p(W_p))] dU`, `p(W)=Tr(W)/2`. Couplings beta_p=lambda c_p, 0<c_-<=c_p<=c_+. For the physical one-step trajectory a_t=kappa h, lambda=1/(g_3^2 h). Lie generators `X=i x·sigma`, `|X|=|x|`; `1-p(exp X)=|X|^2/2+O(|X|^4)`.

## Exact Wilson second variation for a one-link direction
For W in SU(2), `p(exp(tX)W)=cos(t|X|)p(W)+sin(t|X|) p((X/|X|)W)`. Therefore

`d²/dt² [beta(1-p(exp(tX)W))] at t=0 = beta |X|² p(W)`.

This is exact and shows: at a positive/near-identity plaquette the one-link diagonal curvature is positive, but at W=-I it is negative. It does **not** assert overall gauge-fixed positivity: mixed variations and gauge directions matter.

## Local Wilson Hessian perturbation lemma
Fix a coordinate gauge slice on a block B, identifying independent edge increments `X_e` via `U_e(t)=exp(tX_e)\bar U_e`. Let `H_p(bar U)` denote the second differential of `beta_p(1-p(W_p))`, and `H_p(I)` the flat one with the same coordinate convention. If each oriented background link of p lies at geodesic distance <=eta<eta_0 from I (after a common gauge fixing), smoothness of the degree-4 SU(2) product function on the compact group gives an absolute C, independent of h, beta, volume, such that

`|H_p(bar U)[X,X]-H_p(I)[X,X]| <= C beta_p eta sum_{e in boundary p}|X_e|²`.

The proof is the mean-value theorem for the Hessian of the smooth four-link plaquette map, applied on a fixed small compact chart; derivatives are bounded uniformly because four is fixed. Summing over plaquettes yields

`|H_mag(bar U)[X,X]-H_mag(I)[X,X]| <= C D beta_max eta sum_e |X_e|²`.

Gauge fixing adds the same chosen positive gauge-fixing form to both Hessians; then the difference bound stays unchanged. If the flat gauge-fixed Hessian satisfies `H_0[X,X]>=mu_flat sum_e|X_e|²`, one obtains the *sufficient* relative bound

`|H_bar-H_0|_form <= (C D beta_max eta/mu_flat) H_0`.

Hence `C D beta_max eta < mu_flat` implies coercivity and inverse localization with modified constants. This is an explicit Wilson-specific theorem **conditional on a gauge representative with uniformly small individual link rotations**. It is not implied by plaquette traces alone.

For conventional mass-normalized discrete elliptic forms `mu_flat~L^{-2}`, `beta_max` in the same normalized chart ~h^{-2} after factoring scale, giving the conservative sufficient condition `eta << (h/L)^2`. This condition is not known to hold on blocks of fixed physical L when h→0. One must compare the forms in a single consistently normalized inner product; the beta/mu dimensionless ratio is the invariant test.

## Large-field region bounds and why they are not exponential polymers
Take defect `d_p=1-p(W_p)>=0` and bad indicator `b_p=1{d_p>delta}`. Pointwise `b_p<=d_p/delta`. For any deterministic subset X of plaquettes,

`E[sum_{p in X} b_p] <= (1/delta) sum_{p in X} E[d_p]`.

Further `1{b_p=1 for all p in X} <= (1/(|X|delta)) sum_{p in X}d_p`, so

`P(all p in X bad) <= (1/(|X|delta)) sum_{p in X} E[d_p]`.

This is **linear/first-moment**, not exponential in |X|. From the previous full-measure theorem

`(1/N_P) sum_p E[d_p] <= C(1+log lambda)/lambda`, 

one obtains the spatially averaged bad-site density bound `C(1+log lambda)/(lambda delta)`. For `delta=lambda^{-1/2}` it is `C(1+log lambda)/sqrt(lambda)`. There is no uniform bound on `P(all p in X bad)` for an arbitrary X from the global average alone, and no valid inference of an exponential connected-cluster tail.

A transparent probability counterexample to the missing logical inference is a common Bernoulli variable Z with P(Z=1)=q and b_p=Z for all plaquettes in a connected region. Each marginal bad probability is q, but P(all n bad)=q, not q^n. This does not claim that the Wilson measure realizes that example; it establishes why a one-point estimate cannot prove polymer suppression.

The desired missing estimate is, for connected X and constants c,C independent of h, volume,

`mu_h( all p in X bad ) <= C exp(-c |X| lambda delta)`

or an appropriate contour/activity bound compatible with gauge constraints; this remains **unproved** for the full Wilson measure on Penrose-prism complexes. A proper Balaban large-field argument may use buffered regions, gauge fixing, conditional energy comparisons and partition-function ratios, rather than simple independent-site estimates.

## Correct next steps
1. Specify retained boundary holonomies and a local tree/background gauge. Establish a *curvature-to-link* reconstruction estimate with geometry and holonomy dependence; a long path/area factor may destroy the required smallness.
2. In a unified kinetic-mass norm, estimate the actual Wilson Hessian including curvature commutators and background gauge terms; obtain a relative form estimate only on admitted backgrounds.
3. Prove a contour-specific large-field probability/activity bound by a Wilson partition-function surgery or multiscale conditioning argument; do not promote expected density to exponential tails.
4. Combine a local covariance bound and cluster-activity estimate and check scale-by-scale contraction.

The planar Penrose prototiles ensure local bounded degree and angle regularity, but neither nonabelian gauge reconstruction nor uniform contour activities follow from them. The existing FEEC estimates apply to the stated stable discrete Hodge discretization and still require equivalence to the literal Wilson Hessian. No continuum R3 or R2 mass gap has been proved.

Reference context: Balaban, *Ultraviolet stability of three-dimensional lattice pure gauge field theories* (Commun. Math. Phys. 102 (1985), 255–275); *The variational problem and background fields in renormalization group method for lattice gauge theories* (CMP 102 (1985), 277–309); *Propagators for lattice gauge theories in a background field* (CMP 99 (1985), 389–434). Those are the periodic-lattice/related method, not directly a Penrose theorem.
