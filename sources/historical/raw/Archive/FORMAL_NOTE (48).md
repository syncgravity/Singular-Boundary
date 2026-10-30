# Constrained curvature fibers and an explicit Gaussian residual transport
27 October 2026

## Scope
This result is for a **finite, positive gauge-fixed quadratic reference measure** at a flat SU(2) Wilson background. It is NOT a theorem for the nonlinear compact SU(2) Wilson Gibbs measure, nor a uniform statement without an infrared/spectral lower bound.

Let H0 be a real symmetric n-by-n positive-definite precision matrix, D an m-by-n matrix of weighted selected-face linearized curvatures, and lambda>=1. The reference law mu0=N(0,H0^{-1}). Insert V(x)=(lambda/2)||Dx||^2, giving H1=H0+lambda D^T D and mu1=N(0,H1^{-1}). In SU2, m<=3|Q|.

## Theorem 1: Exact constrained-fiber rank reduction
Set z=H0^{1/2}x and B=sqrt(lambda) D H0^{-1/2}. Under mu0, z is standard Gaussian and the insertion is ||Bz||^2/2. Orthogonally decompose R^n=ker B direct_sum ran B^T. Insertion depends only on the r=rank B <=m<=3|Q| second-sector coordinates. This is true even when D has constraints/linearly dependent rows. It is a statement about linearized curvature, not global group-valued face coordinates.

## Theorem 2: Explicit correlated transport with nonpositive expected retained action change
Let M=I+B^T B and T(x)=H0^{-1/2} M^{-1/2} H0^{1/2}x. Then T pushes mu0 to mu1, is invertible, and equals the identity on ker B in whitened coordinates. Its rank deformation rank(T-I)<=r. The normalized Jacobian is det M^{-1/2}. Under this transport,
 E_mu0[S0(Tx)-S0(x)]=(1/2)tr(M^{-1}-I)<=0.
 The transported insertion energy is E_mu0[V(Tx)]=(1/2)tr(B M^{-1}B^T) <= r/2.
 The relative entropy is KL(mu1||mu0)=(1/2)[tr(M^{-1}-I)+log det M], nonnegative.
 Summing insertion energy and KL gives the exact free-energy formula:
 F_Q=-log E_mu0 exp(-V)=(1/2) log det M = (1/2) log det(I_m+lambda D H0^{-1} D^T).
 Therefore F_Q <= (r/2) log(1+lambda ||D H0^{-1/2}||^2).
 If H0>=mu I and ||D||<=C_D, then F_Q <= (3|Q|/2) log(1+lambda C_D^2/mu). For mu>= c lambda^{-a} with fixed a, this is O(|Q|(1+log lambda)). The coefficient of logarithm depends on a. The norm bound on D is valid on bounded-incidence fixed-length-cell complexes with appropriately normalized local inner products; not asserted for unspecified FEEC mass-matrix norms.

Proof: z standard Gaussian, T_z=M^{-1/2}z; covariance M^{-1}. Formula for Gaussian KL, energy, and determinant follow by diagonalizing B^TB. E S0(T)-S0=(1/2)tr(M^{-1}-I)<=0. The rank restriction follows by factorization of M. Gauge compatibility is only infinitesimal and depends on selected gauge-fixed coordinates; no global SU2 nonlinear equivariance is asserted.

## Why this is not the full Penrose transport theorem
1. T is generally spatially nonlocal: H0^{-1/2} and M^{-1/2} need not be local even though D is local. Finite-rank deformation is not finite spatial support.
2. When the infrared regulator mu vanishes, the norm ||D H0^{-1/2}|| can grow with volume or refinement; a uniform determinant estimate needs an independent weighted trace/log spectral inequality, not just rank.
3. At nonflat backgrounds the true Wilson Hessian may be indefinite; positivity is not automatic.
4. At nonlinear SU(2) link level neither global Gaussian coordinates nor the linear Jacobian formula are exact. Large-field and topology sectors need independent controls.
5. The transport decreases *total expected* S0^(2); this does not mean each crossing plaquette individually decreases, nor does it imply decay of connected Wilson cumulants.

## Required nonlinear upgrade
An independently normalized, gauge-compatible transport or trial measure must control E[V_Q]+KL(nu||mu0) with constants O(|Q| log lambda), without invoking the missing insertion free energy, and must have a cutoff-uniform localization/large-field decomposition. The present finite-dimensional Gaussian construction proves this in the strictly quadratic, regulated sector only.
