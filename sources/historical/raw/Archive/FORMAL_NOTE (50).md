# R3: covariance, nonflat Hessian and chart complement — rigorous audit
Date: 2026-10-27

## Setup
Finite gauge-fixed real link-coordinate space V, Euclidean inner products, undeleted linearized curvature D0: V -> F0, inserted curvature DQ: V -> FQ. Regulator mu>0. H0=lambda D0*D0+mu I. C_Q=DQ H0^{-1} DQ*. No claim that Euclidean normalization corresponds to the properly FEEC-mass-scaled Penrose Wilson Hessian without verification.

## Proposition 1: algebraic dichotomy
Let N=ker D0 and P_N its orthogonal projector. Let sigma>0 be the smallest nonzero singular value of D0 on N^perp. For every lambda,mu>0,
 C_Q=(1/mu) DQ P_N DQ* + DQ P_{N^perp} (lambda D0*D0+mu I)^{-1}P_{N^perp} DQ*,
and
 0 <= C_Q <= (1/mu) DQ P_N DQ* + (1/(lambda sigma^2)) DQ P_{N^perp} DQ*.
If DQ P_N=0, then DQ=A D0 where A=DQ D0^+ and 
 C_Q <= (1/lambda) A A*;
therefore rank(DQ)<=3|Q| and
 F_Q^(2)=(1/2)log det(I+lambda C_Q) <= (3|Q|/2)log(1+||A||^2).
This is uniform in lambda,mu if ||A|| uniform. Conversely if DQ P_N !=0 and mu fixed while lambda->infty, at least one eigenvalue of lambda C_Q diverges linearly as lambda/mu. This is a failure of the strengthened uniform O(1/lambda) inserted-curvature covariance; it does NOT rule out the weaker O(|Q| log lambda) determinant estimate at fixed mu. If mu->0 quickly, determinant constants worsen by log(mu^{-1}).
Proof: spectral decomposition of D0*D0; factorization via pseudoinverse; use H0 >= lambda D0*D0 on N^perp and operator monotonicity for inverse, or SVD contraction D0H0^-1D0*<=I/lambda. For converse, nonzero DQ P_N DQ* positive in some direction.

## Proposition 2: nonflat Hessian condition
If on a gauge-fixed regular background the actual Hessian Hbar satisfies the relative quadratic-form bound |<x,(Hbar-Hflat)x>|<=epsilon<x,Hflat x> for all physical x and some epsilon<1, then Hbar>0 and DQ Hbar^-1 DQ* <= (1-epsilon)^-1 DQ Hflat^-1 DQ*. Proof: Loewner inversion. This is NOT established from a bound only on individual plaquette defects for arbitrarily large Penrose blocks. Also a Hessian at a nonstationary background cannot directly justify centered Gaussian Laplace approximation without linear-source control.

## Proposition 3: product chart lower bound cannot be generic
Take one Haar-free cavity link e and a coordinate ball d_SU2(Ue,I)<=M/sqrt(lambda), lambda large. Haar probability equals (theta - (1/2)sin 2theta)/pi with theta=M/sqrt(lambda), asymptotic 2 M^3/(3pi lambda^(3/2)). Thus -log probability=(3/2)log lambda+O_M(1). With m independently Haar-free links, -log probability=(3m/2)log lambda+O_M(m). For chart based on ALL active links, m may be volume, not O(|Q|). Consequently cannot claim a uniformly bounded chart complement or -log mu0(G)<= C |Q|log lambda on the basis of locality/positive Wilson couplings alone.

## Relationship to exact Wilson insertion
For any measurable chart G of positive cavity mass, F_Q=-log E_mu0 e^-V <= F_Q^G-log mu0(G). A bound on F_Q^G alone does not prove global F_Q without an independently estimated mass mu0(G). Conversely gamma1(G)>=gamma0(G) for centered Gaussian measures with covariance ordering and symmetric convex G cancels only the ratio of restricted Gaussian normalizations, not the full Wilson G probability.

## Boundaries of proof
Propositions 1-3 are established finite-dimensional results. Need a uniform local filling operator A with ||A|| controlled, a nonflat relative Hessian estimate in the physical gauge-invariant sector, and a multiscale large-field collar bound using the actual Wilson measure. None follows from bounded incidence alone, and no arbitrary thin-support Penrose insertion estimate, R3 polymer convergence or R2 mass gap is proved.
