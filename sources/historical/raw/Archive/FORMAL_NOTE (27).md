# Gauge-invariant coarse curvature: Hodge separation and a nonlinear conditional large-field estimate

Date: 2026-10-26

## Scope
Finite oriented 3-dimensional cell complex with SU(2) Wilson action S(U)=sum_p beta_p d(W_p), d(W)=1-(1/2)Tr W. Assumed bounded incidence and beta in [c_-lambda,c_+lambda]. All assertions below are finite-volume. Results explicitly conditional on a compatible low-action boundary must not be promoted to arbitrary exterior backgrounds.

## Theorem 1: linearized gauge/curvature separation and spectral covariance
Let C^0,C^1,C^2 be finite-dimensional real cellular cochains with Hilbert structures, d_1 d_0=0. On each su(2) color coordinate, Hodge decomposition C^1=im d_0 direct_sum im d_1^* direct_sum (ker d_1 cap ker d_0^*) holds. The quadratic flat-background gauge action on coexact C^1 is (lambda/2)||DA||^2, D=W^{1/2}d_1, with strictly positive singular values. (For weighted adjoints use D and d_0 as defined and coexact im D^*.) Let D=U Sigma V^* be a singular-value decomposition on coexact coordinates. In the centered Gaussian law exp(-lambda||DA||^2/2), each physical singular coordinate a_r has variance 1/(lambda sigma_r^2), and the curvature coordinate f_r=sigma_r a_r has variance exactly 1/lambda. Hence Cov(F)=lambda^{-1} P_im(D), and for any partition of singular indices into low and high, F=F_<+F_> independent, Cov(F_<)=lambda^{-1}P_< and Cov(F_>)=lambda^{-1}P_>, each <=lambda^{-1}I. All statements hold in the three color copies. This controls fluctuation magnitude uniformly but does not establish decay of the spatial kernel of the projectors P_<,P_>.

## Theorem 2: exact gauge-invariant coarse holonomy energy inequality
Let D be a shellable, simply-connected oriented plaquette disk of N faces, with boundary Wilson holonomy W_boundary (based at a marked boundary vertex). A suitable cellular shelling expresses this holonomy as an ordered product of N transported face holonomies (possible signs absorbed by inversion). With SU(2) bi-invariant geodesic angle theta in [0,pi], theta(W_boundary)<=sum_p theta(W_p) <=sqrt(N sum_p theta(W_p)^2). Since 1-cos theta>=2 theta^2/pi^2, sum_p beta_p d(W_p)>= (2 beta_min/(pi^2 N))theta(W_boundary)^2. Boundary conjugation does not affect theta. No stochastic mixing is presumed.

## Theorem 3: nonlinear conditional Wilson large-field bound on flat-extendible exteriors
Fix a set I of m interior links; freeze all other links as v. Let P(I) be all plaquettes touching I and S_I(u;v)=sum_{p in P(I)}beta_p d(W_p(u,v)), with beta_min>=c_-lambda and beta_max<=c_+lambda. Assume there exists u_0 such that W_p(u_0,v)=I for every p in P(I). Then for any X subset P(I) and delta>0,
  nu_I( d_p>delta for all p in X | v ) <= exp[-c_- lambda delta |X| +(3m/2)log lambda + C m]
for lambda>=1 and C depending only on incidence and upper coupling coefficient. Proof: numerator <= exp(-c_-lambda delta |X|) by normalized product Haar <=1. Denominator: integrate each u_e in geodesic ball of radius a/sqrt(lambda) about u_{0,e}; face holonomy changes by at most (#boundary edges)*a/sqrt(lambda), so 1-cos theta <=C a^2/lambda, and S_I<=Cm. Product normalized Haar ball volume >= (c lambda^{-3/2})^m. Result. No linearization of the action, no independence or Gaussian comparison. Gauge covariance: flat-extension condition, events and resulting inequality are gauge invariant.
If m<=K|X|, then for delta=lambda^{-1/2} and sufficiently large lambda, the RHS <= exp(-c sqrt(lambda)|X|). This result is conditional on strong compatibility of ALL boundary plaquettes touching the interior; arbitrary retained guard fields do not satisfy this assumption.

## Variant: compatible low-energy exterior
If E_I(v)=min_u S_I(u;v) and no flat extension is assumed, same proof with balls about a minimizer gives
  nu_I(all X bad|v) <= exp[-c_-lambda delta |X|+E_I(v)+(3m/2)log lambda+Cm].
This bound is useful only where E_I(v) is controlled. Controlling the Gibbs probability of incompatible guard fields without assuming the desired thin-support free energy is open.

## Why this does not prove R3
(1) Curvature projections have no established uniform spatial decay; the low sector remains dynamical. (2) The nonlinear large-field theorem requires an exactly compatible (or suitably low-energy) exterior; general correlated guard fields may be frustrated at order lambda. (3) The entropy term m log lambda is harmless for bounded m/|X|, but not for mesoscopic collars with m growing much faster than |X|. (4) Gaussian linearized curvature is gauge covariant infinitesimally; finite nonabelian coarse loops are conjugation-invariant, not additive. (5) Neither transfer to the full exterior marginal nor strict renormalized influence contraction nor continuum mass gap follows.
