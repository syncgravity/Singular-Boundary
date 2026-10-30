# Nonstationary SU(2) temporal Wilson comparison: proven extensions and remaining obstruction

Date: 2026-10-27. All transfer operators act on the same finite spatial-link Hilbert space after gauge projection. Let A_t be the completed (possibly time-dependent) positive trace-class temporal transfer operators, B_t the corresponding cavity operators, with A_t >= z_t B_t in Loewner order, where z_t is the product of single-face SU(2) Haar weights over deleted temporal faces in slab t. This requires the *same* spatial potential in the completed and cavity transfer factor in each slab; it may depend on t.

## Theorem 1: Arbitrary nonstationary two-slab reference

For N=2, all spatial and temporal retained masks and nonnegative couplings may depend arbitrarily on time, provided the only changes from completed to cavity are deletions of temporal faces. Then

  Tr(A_0 A_1) >= z_0 z_1 Tr(B_0 B_1).

Proof: write A_0=z_0 B_0+D_0, D_0>=0. Since A_1>=0, Tr(A_0 A_1)>=z_0 Tr(B_0 A_1). Then write A_1=z_1 B_1+D_1 and use Tr(B_0 D_1)>=0. Every trace is well-defined for trace-class positive operators. No commutativity is needed. Hence Z_complete/Z_cavity >= product z(beta_q), independent of volume. This does NOT directly cover the project's N=3 periodic-time Penrose construction.

## Theorem 2: General N, exact nonstationarity-overlap penalty

For arbitrary N and arbitrary time-dependent completed spatial/temporal masks, define

  Omega(A_0,...,A_{N-1}) := [product_t ||A_t||_N] / Tr(A_0 ... A_{N-1}) >=1.

The denominator is strictly positive for the actual Wilson transfer kernels (the physical partition function), even though a product of generic positive matrices need not have positive trace. Then

  Z_complete/Z_cavity >= (product_{q in Q} z(beta_q)) / Omega.

Proof: Schatten-Holder gives Tr(prod B_t) <= product ||B_t||_N. Since 0<=B_t<=z_t^-1 A_t, eigenvalue monotonicity gives ||B_t||_N<=z_t^-1 ||A_t||_N. Divide by Z_complete=Tr(prod A_t). For stationary completed A_t=A, Omega=1, recovering the previous theorem. For N=2, Theorem 1 is strictly stronger because it gives Omega=1 effectively without stationarity.

This is an *exact reduction*, not a solution of the uniform arbitrary-nonstationary problem. Omega can depend on the full ambient system and may grow very rapidly. To obtain the desired q-local bound one would need to prove Omega<=C^q(1+lambda)^{a q} for the relevant completed masks, or replace Omega with a sharper local overlap quantity.

## Theorem 3: Actual exterior barrier, with overlap penalty

Let H be the k insertion links, and assume the same uniform face-incidence Hessian bound nu as in the previous formal note. Let Delta(v) be the difference of the two conditional minima, and nu_0 the *actual* cavity exterior marginal. The exact two-sided conditional Haar-ball comparison gives

  E_{nu_0}[exp(-lambda Delta)] >= b_{k,nu}(lambda) * Z_complete/Z_cavity
  >= b_{k,nu}(lambda) * (product_{q in Q} z(lambda)) / Omega,

with b_{k,nu}(lambda)=exp(-1)(6pi)^(-k)(2nu k)^(-3k/2)(1+lambda)^(-3k/2). Thus

 -log E_{nu_0}[exp(-lambda Delta)] <= (3/2)(k+q)log(1+lambda)+C_{k,nu,q}+log Omega.

For arbitrary nonstationary N=2, Omega is unnecessary, and this is a uniform compact-SU(2) theorem. For arbitrary nonstationary N>=3, the extra log Omega is unproved to be local/volume-uniform.

## The exact obstruction to a naive operator proof for N>=3

Loewner monotonicity of each factor does not imply monotonicity of the trace of a product of >=3 factors. For real unit vectors a=(1,0), b=(1/2,sqrt(3)/2), c=(-1/2,sqrt(3)/2), rank-one positive projections D=aa^T, B=bb^T, C=cc^T satisfy Tr(DBC)=-1/8. Thus increasing a factor by D can decrease the trace product. This example is *not* a Wilson-model counterexample; it only invalidates the attempted abstract operator-order inference. The positive integral kernels of the physical model might supply further structure, but no proof of a q-local overlap estimate for arbitrary completed nonstationary masks is available here.

## Exact uniform fallback without stationarity

Since 0<=d(W_q)<=2, pointwise exp(-lambda S_Q)>=exp(-2lambda q). Therefore for *every* retained background R and insertion Q,

 Z_complete/Z_cavity >= exp(-2lambda q),

and -log E exp(-lambda Delta) <= 2lambda q + (3k/2)log(1+lambda) + C_{k,nu}.

This is volume-uniform but O(lambda q), not the R3 logarithmic target. It is not presented as a solution.

## Research status

The general arbitrary-nonstationary N=3 case remains open. The results above establish an exact theorem for N=2, an exact quantified overlap obstruction for any N, and a rigorous O(lambda q) uniform fallback. None establishes the general N=3 R3 insertion theorem or a continuum mass gap.
