# Scale-sharp Penrose-block discrete Hodge–Poincaré and gauge-covariance theorem

## Scope and model

This note proves a scale-sharp result for **Whitney/FEEC discretization of the trivial-background quadratic SU(2) Wilson gauge action** on a specified geometrically regular family of Penrose spacetime blocks. It is NOT a theorem for arbitrary clipped Penrose patches, arbitrary choices of discrete Hodge stars, or all nonflat Wilson backgrounds. It is not a mass gap.

Take a fixed bounded contractible reference Lipschitz 3D domain Omega (topological ball), and domains B_L with uniformly controlled bi-Lipschitz charts after scaling by L. Use blocks assembled from whole Penrose rhombi, whose rhombus angles are 36/144 and 72/108 degrees, times time slabs a_t=kappa h, 0<kappa_-<=kappa<=kappa_+. Triangulate rhombi using a diagonal and prisms by a fixed compatible tetrahedral template. ASSUME boundary fitting, mesh conformity and uniform shape regularity, and uniform bi-Lipschitz geometry of the block family; Penrose's two prototiles guarantee interior cell shape regularity, but **do not alone guarantee these boundary/block conditions**. For the planar rhombus split along the short diagonal, the smallest triangle angle is >=18 degrees.

Use Whitney one-form spaces V_h^1 (lowest order FEEC) with relative/tangential Dirichlet boundary condition. They form a subcomplex; rely on established bounded commuting cochain projections for uniformly shape-regular Lipschitz meshes, with uniform bound C_pi. Equip them with L2 Whitney mass matrices, and use the FEEC discrete adjoint d_{0,h}^*. On color components su(2) the flat-background operator is

  A_h = d_{1,h}^* B_{2,h} d_{1,h} + xi d_{0,h} d_{0,h}^*

in the L2 inner product (with properly chosen gauge-fixing coefficient and possibly weighted 0-form inner products); B_2 uniformly elliptic 0<b_-<=B_2<=b_+. For statements of sparse-local covariance use instead a spectrally equivalent **local diagonal mass-lumped inner product** (or a proved local Riesz basis), with matrix H_h in the corresponding diagonal-normalized link basis. Mere use of exact non-diagonal Whitney mass matrices does not make M^{-1/2} sparse; locality is an additional assumption in the matrix estimate.

## Theorem 1 (FEEC Poincare; scale sharp)

For such uniformly regular block family with trivial degree-one relative cohomology and suitable degree-zero boundary conditions, there exists C independent of h and numbers of cells with

  ||u_h||_{L2(B_L)} <= C L ( ||d_1 u_h||_{L2} + ||d_{0,h}^*u_h||_{L2})

for all Whitney one-forms satisfying the relative boundary condition. Equivalently

  <u_h,A_h u_h> >= c L^{-2} ||u_h||^2,

where c depends on b_-, xi, C_pi and uniform block geometry, not on h. This is obtained from the two FEEC discrete Poincare inequalities for the orthogonal exact/coexact Hodge decomposition, with the absence of discrete harmonic one-forms guaranteed by topology and commuting projections; continuous Poincare constants scale linearly with L. It is not enough merely to have d_1d_0=0 or a topologically contractible incidence graph: stable mass matrices and projections are necessary. A mass-lumped variant inherits the estimate if its forms are uniformly spectrally equivalent.

For the corresponding normalized local matrix H_h, assume the standard FEEC inverse inequality and uniform row/column norm estimates: lambda_max(H_h)<=C h^{-2}. Together

  spec(H_h) subset [mu,Lambda], mu=c/L^2, Lambda=C/h^2.

The exponent is **physically scale-sharp**: massless curvature fluctuations have block-scale 1/L spectral frequencies; no volume-independent mass is introduced.

## Theorem 2 (scale-sharp inverse matrix localization)

Assume H_h is SPD and nearest-neighbor finite-range on an adjacency graph of basis degrees of freedom with each hop changing physical location by at most R_0 h. Set kappa=Lambda/mu and

  q=(sqrt(kappa)-1)/(sqrt(kappa)+1) in [0,1).

For nodes e,g with graph distance n=d_graph(e,g)>=1,

  ||(H_h^{-1})_{eg}|| <= (2/mu) q^{n}

(up to harmless adjustment of n due to block-support radius). Proof: choose a degree n-1 Chebyshev polynomial p_{n-1} approximating 1/x on [mu,Lambda] with uniform error <=(2/mu)q^n. Graph finite range makes p_{n-1}(H)_{eg}=0. Consequently

  ||(H_h^{-1})_{eg}|| <= C L^2 exp[-c dist_phys(e,g)/L],

where c,C depend on uniform mesh geometry and ellipticity, not h or number of cells within B_L. This resolves the h^2/L^2 artificial exponent of an elementary Combes–Thomas estimate, though it is not a pointwise continuum Green function 1/r estimate. At a fixed physical block L, this exponential localization occurs only on the block scale and is insufficient by itself for an inter-block polymer norm with arbitrarily large scales.

For general finite-range radius R lattice hops, replace n by floor(d_graph/R) and adjust constants.

## Theorem 3 (conditional stability of the nonflat background)

Let H_h(bar U) be the true **gauge-fixed quadratic Hessian** around an admitted background and H_h(1) the flat Hessian in the same retained-variable gauge slice. If its quadratic-form difference obeys

  |<u,[H_h(bar U)-H_h(1)]u>| <= eps <u,H_h(1)u>

for all u, with eps<1 independent of h,L, then

  (1-eps)H_h(1) <= H_h(bar U) <= (1+eps)H_h(1).

Hence its eigenvalues lie in [(1-eps)c/L^2, (1+eps)C/h^2] and the same Chebyshev local inverse estimate applies **provided the background Hessian remains finite-range in the chosen local basis**. The simple relative-form condition is explicit and sufficient, but has NOT been established from plaquette defect <= lambda^{-1/2} on general nonabelian Penrose backgrounds. Individual small plaquette traces do not control global holonomy or gauge-fixed link variables; background-dependent Wilson Hessians can have stationary-point/negative-curvature and gauge-zero-mode subtleties. One must derive relative-form estimates using localized axial/background gauge, Wilson expansion and curvature/homotopy control, plus correct boundary holonomy constraints. Coefficients of the nonflat Wilson Hessian also need an honest curvature-based estimate; do not conflate it with the flat FEEC Laplacian.

## Limitations to Wilson Hamiltonian RG

* Exact Whitney/FEEC weighted Hodge stiffness need not coincide with the quadratic Hessian of the specified literal Wilson action and dual-area/electric weight recipe; uniform spectral equivalence must be proved from those weights. In particular, anisotropic factors and boundary terms matter.
* Boundary blocks cut arbitrarily near a vertex can have sliver cells and destroy regularity unless blocks are unions of entire rhombi or are remeshed with uniform regularity.
* Periodic or nontrivial-topology blocks may carry harmonic one-forms, so project them out or retain the corresponding boundary/topological variables rather than claiming positivity.
* The elliptic constant depends on physical block scale L, so this does **not** produce a mass independent of large L and cannot prove R3 or R2.
* To run Balaban-type RG, still need gauge choice with background-form smallness, scale-dependent covariance localization and connected large-field polymer suppression, plus quantum transfer reconstruction.

## References

- Arnold, Falk & Winther, *Finite element exterior calculus: from Hodge theory to numerical stability*, arXiv:0906.4325. Bounded commuting projections and discrete Poincare/Hodge stability.
- Christiansen & Winther, *Smoothed projections in finite element exterior calculus*, Math. Comp. 77 (2008), 813–829. Essential boundary conditions and non-quasiuniform meshes.
- Licht, *Smoothed projections over weakly Lipschitz domains*, Math. Comp. 88 (2019), 179–210. Uniform projection bounds for shape regular finite elements.
- Demko, Moss & Smith, *Decay rates for inverses of band matrices*, Math. Comp. 43 (1984), 491–499. Sparse inverse polynomial approximation.
