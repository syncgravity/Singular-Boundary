# Positive-character interface on two glued rhombus prisms

## Scope
The exact integer incidence model consists of two adjacent quadrilateral prisms with 12 vertices, 20 edges, 11 faces, and 2 cells. It is a realizable local rhombus-compatible combinatorial patch, **not an extraction/certification of an entire Penrose tiling**. All 20 link variables are integrated with product normalized SU(2) Haar, with no frozen outer boundary and no extra Wilson interactions. Wilson plaquette factors are `w_beta(g)=exp[-beta(1-(1/2)Tr(g))]` with beta>0.

## Verified combinatorics
The shared face p=3 has four edges. The five other faces of each cell form a cellular disk; their respective edge sets intersect exactly in the four seam edges. Each disk has Euler characteristic 1, and the boundary operator applied to its five faces is the seam cycle, with opposite signs on the two disks. Matrix identities B1 B2=0, B2 B3=0 hold over integers. See certificate.json and verify.py.

## Two-dimensional disk integration lemma
For any finite cellulated disk with independent edge Haar variables and positive central plaquette weights w_i, the integral of all edges not on its boundary, at fixed oriented boundary holonomy h, is

   f(h)=(w_1*...*w_m)(h) 

(up to orientation reversal h->h^-1). Prove by choosing a spanning tree of the dual graph and sequentially integrating disk face/link variables, or by the standard two-dimensional lattice gauge exact integration. The equality includes normalized Haar conventions. The result is independent of disk cellulation and of the choice of boundary link representatives (by gauge invariance).

For SU(2), expansion w_beta(g)=sum_{j in {0,1/2,...}} d_j c_j(beta) chi_j(g) with d_j=2j+1 and

   c_j(beta) = (1/d_j) integral_SU2 w_beta(g) chi_j(g) dg
             = 2 exp(-beta) I_{2j+1}(beta)/beta > 0.

Thus f(g)=sum_j d_j [product_i c_j(beta_i)] chi_j(g), with every character coefficient nonnegative.

## Two-prism theorem
Let f_L and f_R be the five-face disk factors. Upon integrating all links except the seam, the undeleted partition function is

 Z_0 = integral_SU2 f_L(h) f_R(h^{-1}) dh.

When the common face p is inserted with weight w_gamma(h),

 Z_1 = integral_SU2 w_gamma(h) f_L(h) f_R(h^{-1}) dh.

The product F(h)=f_L(h)f_R(h^{-1}) is central with nonnegative character coefficients: chi_j chi_k=sum_{l=|j-k|}^{j+k} chi_l. Its trivial character coefficient a_0=int F dh is positive. Write w_gamma=q(gamma)+sum_{j>0} a_j chi_j with a_j>=0. By SU2 orthogonality,

 Z_1 = q(gamma) Z_0 + sum_{j>0} a_j * (character coefficient of chi_j in F) >= q(gamma) Z_0.

Hence insertion free energy

 0 <= -log(Z_1/Z_0) <= -log q(gamma) = (3/2) log gamma + O(1), gamma>=1.

Moreover the full inserted joint measure nu has E_nu[V_p]+ KL(nu||mu_0)=-log(Z_1/Z_0), giving a logarithmic aggregate energy--entropy bound. This construction uses no unknown partition-function ratio for the **proof of the estimate**, although defining the exact Gibbs optimal tilt uses normalizing Z_1/Z_0.

## General positive-interface criterion
If integration of everything outside a distinguished interface face produces an SU(2) central effective kernel F(h) whose coefficients in irreducible SU2 characters are nonnegative, then inserting any Wilson face weight w_gamma(h) costs no more than -log q(gamma). This holds even with strong nonlinear correlations in the integrated variables. It requires the entire effective kernel to possess this property. Pointwise positivity F(h)>=0 does NOT suffice.

## Where the extension stops
1. The verified model has no external links held fixed and no additional plaquettes coupling the two five-face disks through their non-seam edges. Actual adjacent prisms in a larger Penrose spacetime patch have further Wilson faces, so the factorization need not hold.
2. At a multi-port interface, the effective boundary kernel is a multivariable SU(2) function with matrix-valued spin-network Fourier sectors. Scalar character positivity cannot be inferred from positivity of each original Wilson weight.
3. A uniform multiplicative correction cannot follow for every fixed exterior: an opposing-staple one-link example gives Z_1/Z_0 ~ exp(-2 lambda)*lambda^(3/2), which violates any `>=exp(-C) q(lambda)` claim. This does not disprove an annealed correction under actual larger-volume Gibbs margins.
4. No arbitrary-support Penrose insertion estimate, nonperiodic stable RG, or continuum mass gap follows.

## Next algebraic verification
For actual multi-cell Penrose incidence, build complete signed face--edge--cell arrays from true rhombus tile geometry; enumerate interface ports, then compute a truncated SU2 representation expansion of the multiport effective kernel, including 6j recoupling signs. A negative eigenvalue in a required positive-definite sector invalidates the positive-kernel induction; an alternative comparison must control its partition effect nonperturbatively.
