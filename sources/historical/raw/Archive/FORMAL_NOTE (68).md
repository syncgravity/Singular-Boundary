# Independently normalized serial SU(2) boundary-energy moment and Penrose incidence audit

Date: 2026-10-27. Scope: exact restricted theorem; no arbitrary-support mass-gap claim.

## 1. Definitions and theorem

For SU(2), d(g)=1-(1/2)Tr(g)=1-cos(theta(g)), with theta in [0,pi]. Let q(beta)=int exp(-beta d(g))dg=exp(-beta)2I_1(beta)/beta. Let g_i be independent under pi_{beta_i}(dg)=q(beta_i)^-1 exp(-beta_i d(g))dg, with beta_i>=c_- lambda and lambda>=1. Define H=ordered product g_1...g_n. For any constant C_ext>0 and 0<t<2c_-/(pi^2 C_ext), let alpha=pi^2 C_ext/2. Then

E exp[t C_ext lambda theta(H)^2/n] <= product_i q(beta_i-t alpha lambda)/q(beta_i) <= C_t^n,

with C_t finite uniformly in n, lambda, couplings beta_i>=c_-lambda (even if no upper bound). Hence P[C_ext lambda theta(H)^2/n >= n log(C_t)/t + s] <= exp(-t s).

Proof: theta(H) <= sum theta(g_i), theta(H)^2/n <= sum theta(g_i)^2 <= (pi^2/2)sum d(g_i). Exact independent integration yields the ratio. Uniform ratio follows from q(beta) being comparable to (1+beta)^(-3/2) and beta-t alpha lambda >= (1-t alpha/c_-) beta, so q(beta-t alpha lambda)/q(beta) <= C_t. The moment is independently normalized, not an insertion free energy in disguise.

If an actual prism support can be mapped by Haar-preserving invertible coordinates to a sector of n<=C|Q| such Wilson increments, and the compatible minimum obeys M_K(v)<= A|Q|+C_ext lambda theta(H)^2/n for the same variable H, then conditional thermal-excess concentration and this moment yield an absolute O(|Q| log lambda) tail. These are substantial geometrical hypotheses, unverified in generic 3D Penrose cavities.

## 2. Obstruction to extending the moment directly

If H is Haar rather than Wilson-controlled, then for theta(H)>=delta>0 of constant Haar probability, E exp[t C_ext lambda theta(H)^2/n] >= p_delta exp[t C_ext lambda delta^2/n]. For fixed n this grows exponentially in lambda. Such a marginal can arise from a free holonomy coordinate following deletion of its only controlling interaction. This defeats any uniform C^n bound absent a retained Gibbs mechanism. It does not show that a genuine cavity's chosen exterior holonomy always has this property.

## 3. Data audit

penrose_complete_catalogue.npz has planar cycle arrays idx (22808,22), sign (22808,22), length (22808), etc., cidx (68424,16), csign (68424,16). The stage26 full archive contains sweep observables (e.g. direct_timeslice (20,4), direct_product (9,4,4), conditional (2,9,4,4)) but not a verified signed 3D face-cell incidence matrix. The dissertation archive contains PDF documents; it is not an incidence certificate. Therefore no computational verification of an actual support-local coupled extension with strong extra Wilson interactions or arbitrary 3D prism cavities has been completed.

A conforming rhombus-prism has two rhombic faces and four side faces; its boundary matrix supports the one-missing-face Bianchi fill relation. This local topological fact is insufficient to show that cyclic residual boundary coordinates admit a uniformly bounded holonomy-factorizing pivot system or that strong exterior plaquettes do not add lambda-scale action.

## 4. What remains open

Need certified d_2,d_3 for the actual Penrose prism complex, with d_2 d_3=0 under chosen conventions; for each Q find a support-local nonlinear constrained deformation realizing an energy bound while retaining the actual Gibbs normalization; and prove an absolute exponential moment for its exterior holonomy under the correlated nonlinear cavity measure. The serial theorem does not prove this for arbitrary supports, nor R3 or the continuum mass gap.
