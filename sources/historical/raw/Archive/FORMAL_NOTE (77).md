# R3: Two-port SU(2) Wilson interface on an assembled three-prism strip

October 27, 2026. Scope: a **constructed**, face-sharing, three-quadrilateral prism strip, not a certified patch extracted from the user's Penrose coordinates and not an arbitrary surrounding three-dimensional cavity.

## Exact incidence certificate

Three quadrilaterals have oriented planar vertex cycles (0,1,2,3), (2,1,4,5), (5,4,6,7). Extrude to two time slices, identify common temporal side faces. The accompanying `verify.py` produces integer boundary matrices B1 (16×28), B2 (28×16), B3 (16×3), with B1 B2=0, B2 B3=0; ranks 15, 13, 3; two interior temporal seam faces with cell incidence columns (1,-1,0) and (0,1,-1). Their edge cycles are disjoint. There are 16 vertices, 28 edges, 16 faces, 3 prisms. The prism complex is a three-ball; deleting both internal seam face factors leaves the three individual sphere-minus-boundaries pieces: left disk of five faces, middle annulus of four faces, right disk of five faces.

## Wilson kernel reduction

Use normalized Haar on SU(2), Wilson face weight w_beta(g)=exp[-beta(1-(Tr g)/2)], and q(beta)=∫w_beta dg=e^-beta 2I_1(beta)/beta. The usual gauge-fixed 2D disk/cylinder integration (face-to-edge Haar substitution on a planar ribbon decomposition) integrates each disk into a central convolution f_L(h_1), f_R(h_2), each of five face weights. The four-face annulus integrates to f_M(h_1^-1 h_2), up to simultaneous conjugation and orientation inversions; f_M is a convolution of its four face weights. In particular the two-port *cavity* effective density with respect to dh_1 dh_2 is proportional to

    F(h_1,h_2)=f_L(h_1) f_M(h_1^-1 h_2) f_R(h_2).

This is a 2D surface-integration identity for the isolated complete face collection: it is **not** a general reduction of Wilson theory in an ambient 3D Penrose cavity with further plaquettes attached.

## Matrix-valued Fourier positivity

Every Wilson weight w_beta has nonnegative SU(2) character expansion, w_beta(g)=Σ_j d_j c_j(beta) χ_j(g), c_j(beta)=2e^-beta I_{2j+1}(beta)/beta>0, d_j=2j+1. Central SU(2) convolution preserves the coefficient sign. Thus f_L,f_M,f_R are positive-definite functions on G=SU(2).

On G×G, f_L(h_1) and f_R(h_2) are positive-definite. For a central positive-definite f_M(g)=Σ_j d_j a_j χ_j(g), a_j≥0, the joint function f_M(h_1^-1 h_2) is likewise positive-definite on G×G, since

    χ_j(h_1^-1 h_2) = <Ω_j,[\overline{D_j(h_1)} ⊗ D_j(h_2)] Ω_j>,
    Ω_j=Σ_{a=1}^{d_j} e_a⊗e_a,

and therefore its (contragredient-j, j) Peter–Weyl Fourier coefficient block is d_j a_j |Ω_j><Ω_j|, positive semidefinite, with one eigenvalue d_j² a_j and all remaining eigenvalues zero. (Conventions for normalized Fourier coefficients may rescale these eigenvalues by a positive factor; semidefiniteness is invariant.) Products of continuous positive-definite functions on compact groups are positive-definite, by tensor products of unitary representations. So **F is positive-definite on SU(2)×SU(2)**. This is a matrix-valued statement, not merely nonnegativity of F pointwise.

The script explicitly checks the fundamental j=1/2 block at a_j=1/d_j, yielding M=|Ω><Ω| with spectrum (0,0,0,2).

## Simultaneous two-seam insertion

Let V=gamma_1 d(h_1)+gamma_2 d(h_2). Write w_gamma=q(gamma)+(w_gamma-q(gamma)), where both q(gamma) and w_gamma-q(gamma) are positive-definite functions (the latter has precisely zero trivial-representation coefficient and positive nontrivial coefficients). Since products of positive-definite functions are positive-definite, and the Haar integral of such a function is nonnegative,

    ∫_{G²} F(h_1,h_2) w_gamma1(h_1) w_gamma2(h_2) dh_1 dh_2
    >= q(gamma_1) q(gamma_2) ∫_{G²} F(h_1,h_2) dh_1 dh_2.

Therefore, for this isolated three-prism cavity,

    0 <= F_Q = log(Z_0/Z_1)
       <= -log q(gamma_1)-log q(gamma_2)
       = (3/2) Σ_{i=1}² log(gamma_i) + O(1), gamma_i→∞.

This is an **independently normalized noncircular insertion theorem** for two interacting ports, and the matrix-block positivity correction is zero on this model.

## Crucial limitations

1. The strip is a combinatorially valid rhombus-compatible assembled prism patch, **not** verified as copied from the uploaded Penrose tiles.
2. The factorization uses a planar 2D surface decomposition after integrating all links *not shared with additional external plaquettes*. An arbitrary three-dimensional cavity may attach further faces to the same links, breaking this reduction.
3. A more highly connected prism dual graph with loops, or three or more overlapping ports, can produce general spin-network intertwiners whose Hermitian Fourier blocks are not automatically PSD. This theorem supplies no coupling-independent correction for such kernels.
4. It establishes the combined insertion energy plus relative-entropy bound of the inserted Gibbs law, not individual deterministic local-flow action/Jacobian estimates.
5. Arbitrary Penrose thin-support R3, nonlinear large-field bounds and continuum Yang–Mills mass gap remain unproved.

## Reproduce

Run `python verify.py`. `incidence.npz` and `certificate.json` are created with the exact incidence checks and the fundamental block calculation.
