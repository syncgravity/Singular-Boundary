# Correlated Wilson fiber transport: exact cancellation, criterion, and Bianchi obstruction
27 October 2026

## Setup and caveat
Let G=SU(2), normalized Haar. d(g)=1-(1/2)Tr(g); q(beta)=int_G exp(-beta d(g))dg=e^{-beta}2 I_1(beta)/beta. Let S0 be a sum of undeleted spatial/temporal Wilson plaquette actions and V_Q=sum_{p in Q} beta_p d(W_p). The object F_Q=-log E_{mu0} exp(-V_Q).

## Theorem 1: correlated two-link fiber transport
Suppose the link variables include u,a,b in G, with fixed other links w, and a Haar-preserving change of variables
  X=u a, Y=u b, z=(b,w),
where the undeleted action is S0(X,z), independent of Y, and the inserted action contains precisely beta d(Y) (other inserted terms, if any, are not included in this statement). This permits arbitrarily strong correlations of X with z under S0, and can model a shared-link undeleted plaquette with an additional exterior link a.

Under the cavity mu0 proportional to exp[-S0(X,z)] dX dY dz, the coordinate Y is independent Haar. Let Phi_beta push Haar to q(beta)^{-1} exp[-beta d(Y)] dY by conjugation-equivariant radial quantile transport. Define X'=X, Y'=Phi_beta(Y), z'=z; equivalently if b is frozen,
  u'=Phi_beta(u b)b^{-1},  a'=(u')^{-1}(u a).
The map is invertible almost everywhere and moves *both* u and a, often by O(1). Nevertheless S0'=S0 pointwise. It acts on actual link variables, so nonabelian Bianchi relations hold automatically. Given fixed b,w, Haar on (u,a) maps to Haar on (X,Y), since transformations use only left/right translations and inversion. Hence the Jacobian cost is exactly
  D_KL(T_*mu0||mu0)= -beta E_{pi_beta} d(Y)-log q(beta),
and the inserted energy is beta E_{pi_beta}d(Y). The sum is -log q(beta)=(3/2)log beta+O(1). The insertion free energy is exactly -log q(beta).

Gauge covariance can be implemented by defining X,Y as based closed holonomies and transporting their conjugacy classes with a common basepoint; the link reconstruction is equivariant under the induced endpoint gauge action (subject to a chosen gauge/frame on the coordinate chart). The result requires the explicit fiber-coordinate hypothesis, not merely that links share a plaquette.

## Theorem 2: general Wilson-invariant Haar-fiber criterion
Suppose a finite link chart has a measure-preserving coordinate decomposition (z,Y_1,...,Y_r) with product Haar on the Y_i, S0=S0(z), and V_Q=sum_{i=1}^r beta_i d(Y_i). Suppose the reconstruction to link variables is invertible almost everywhere and compatible with lattice gauge transformations. Applying independent radial quantile transports Y_i'=Phi_{beta_i}(Y_i) preserves S0 pointwise and gives
  F_Q=-sum_i log q(beta_i)=(3/2)sum_i log beta_i+O(r)
when all beta_i comparable to lambda. The action is exactly unchanged and entropy additive. The criterion is independent of inserted partition functions; all normalizations q(beta_i) are explicit one-face integrals. It allows O(1) link changes.

## Proposition 3: exact Bianchi obstruction to Wilson-invariant fibers
Let a contractible 3-cell have oriented face holonomies W_1,...,W_s with nonabelian Bianchi relation: appropriately conjugated ordered product equals I. If all undeleted s-1 face holonomies are I, the remaining face is also I. Therefore no transformation can preserve the holonomies of those s-1 faces identically and independently vary the final face on that flat locus. In a 3D Penrose prism the same statement holds, provided its cellular Bianchi relation is realized correctly. This does not preclude transports that change undeleted plaquettes at bounded expected cost; it rules out treating an arbitrary interior face as an exactly free S0-invariant Haar fiber.

## Needed bound outside the fiber class
For general T, the exact transport inequality is
  F_Q <= E_mu0[V_Q(TU)+S0(TU)-S0(U)-log J_T(U)].
Theorem 1 establishes the logarithmic bound if a full SU(2) Wilson-invariant coordinate is identified. For arbitrary interior Penrose supports no proof that enough such fibers exist, nor a uniform bound on the leftover correlated crossing-action and Jacobian costs. Therefore arbitrary-support insertion bound, polymer expansion and R2/R3 mass gap remain open.

## Important audit
The two-link example is an *algebraic local Wilson block* that can be embedded only where its incidence factorization holds; it is not a claim that a generic Penrose interior plaquette admits such a coordinate. In particular, S0 must be a function of the fixed product X and other unmodified variables, not separately of u or a. Preserving a single plaquette trace rather than its full holonomy is not enough to conclude a free Haar fiber.
