# Dressed short-time L2 Hessian smoothing (2026-11-02)

For the finite original-link SU(2) strip with L_N=-Delta-2 grad S_g dot grad, assume Bakry-Emery curvature and spectral gap kappa=23/144. The exact integrated Bochner inequality gives ||Hess h||_2<=||L_N h||_2. Spectral calculus and ||L_N^(1/2)f||_2=||grad f||_2 yield

**||Hess P_t f||_2 <= (e t)^(-1/2) exp(-kappa t/2) ||grad f||_2**, t>0, uniformly in N.

Proof: sup_(lambda>=kappa) sqrt(lambda) exp(-lambda t) <= exp(-kappa t/2) sup_(lambda>0) sqrt(lambda) exp(-lambda t/2) = (e t)^(-1/2) exp(-kappa t/2).

For undressed SU(2) product one may take kappa=3/4. The SU(2) coordinate harmonic has lambda=3/4, Ric=1/2 and Hess²/gradient²=1/4. This new result is UNWEIGHTED L2 only. It does not prove the missing anisotropic weighted L4 vector-semigroup smoothing, pointwise interacting Hessian, lambda=1 gap, or continuum mass gap. Full report, numerical verifier, passing log and SHA256 are preserved in the Proof Audits Library.