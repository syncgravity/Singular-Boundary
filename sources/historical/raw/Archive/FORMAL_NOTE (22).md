# Gauge-fixed Gaussian curvature covariance and joint contour bound

26 October 2026 — conditional reference-theory theorem, not a nonlinear SU(2) Wilson mass-gap proof.

## Definitions
Let a finite bounded-degree Penrose-derived spacetime cell complex have real Lie-algebra-valued one-cochains A in a gauge-fixed finite-dimensional coordinate space, and linear curvature D A with D=W^{1/2}d_1, where W has positive plaquette weights. Let G>=0 be a gauge-fixing/regulator quadratic form and suppose H= lambda D*D+G is strictly positive. The Gaussian reference measure is N(0,H^{-1}). All norms are Euclidean in the coordinates stated; uniformity for physically weighted FEEC norms requires a uniformly stable discretization.

## Exact curvature covariance
C= D H^{-1}D* <= lambda^{-1}I. Proof: lambda D*D<=H, hence ||D H^{-1/2}||^2<=1/lambda, and C=(D H^{-1/2})(D H^{-1/2})*. No eigenvalue lower bound on H independent of volume is used. Under a shell decomposition using mutually orthogonal projections in H-whitened coordinates, each Gaussian shell covariance is also bounded by lambda^{-1}I, provided shell is defined via an orthogonal projection of the whitened Gaussian.

## Arbitrary thin contour Gaussian estimate
Select ANY set X of n plaquettes (connected or disconnected). Assume su(2) has three real components per plaquette. Let F_X be the restriction of F to X. Its covariance has operator norm <=lambda^{-1}. For every delta>0,
P(||F_p||²>2delta for every p in X)
 <=P(||F_X||²>2delta n)
 <=exp(-lambda delta n/2) E exp[(lambda/4)||F_X||²]
 <=2^{3n/2} exp(-lambda delta n/2).
Indeed the Gaussian quadratic moment is det(I-(lambda/2)C_X)^(-1/2)<=2^{3n/2} since C_X<=I/lambda.
With delta=lambda^{-1/2}, this is exp[-(sqrt(lambda)/2 - (3/2)log2)n]. For the unweighted linearized curvature d_1 A, replace lambda by lambda w_min if W>= w_min I, and account for appropriate norm-conversion factors.
The bound is uniform in total volume and n (beyond the displayed dependence), and **does not require plaquette independence or bounded incidence**. It is not automatically a statement about nonlinear Wilson plaquette defects 1-p(W_p) or nonflat background Hessians.

## Independent nonlinear transfer gate
Let A be a Gaussian-coordinate domain on which the exact blocked Wilson density relative to gamma is proportional to exp[-R(A)] times a Jacobian J(A). A sufficient contour transfer theorem requires estimates on both the numerator restricted to the large-curvature event and the full denominator. For instance, if pointwise on the entire coordinate domain one has 0<j_-<=J<=j_+, |R|<=r, then P_W(E)<= (j_+/j_-)e^{2r}P_gamma(E). But r may be extensive, so this is not a continuum-uniform theorem. A localized, conditional ratio with factor exp(c|X|) would suffice: P_W(E_X) <=e^{c|X|}P_gamma(E_X). Derivation of this localized ratio is open.

## Scale-shell caution
H= lambda D*D+G is invertible for a fixed regulator; curvature bound is regulator-independent even when H^-1 is not. If H is split into shells by orthogonal projections in whitened coordinates, curvature covariance of each shell is bounded by the full covariance in Loewner order, but determinant/Jacobian/nonlinear polymer controls are not proved by this observation. For a nonflat background the Wilson Hessian has curvature-dependent indefinite terms and may not dominate lambda D*D: background stability is an independent requirement.

## Status
PROVED: Gaussian curvature operator bound, arbitrary multi-plaquette Gaussian large-field suppression, covariance control for orthogonal Gaussian shells. OPEN: transfer to nonlinear SU(2) Wilson measure, simultaneous background-gauge control, large-field polymer activity estimates, finite-volume-to-continuum quantum Hamiltonian reconstruction, R3/R2.
