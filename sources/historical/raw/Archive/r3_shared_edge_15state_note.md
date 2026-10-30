# R3: shared-edge two-loop recoupling, exact 15-state block
Date: 2026-10-27

**Scope.** Four spatial squares in a 2×2 disk, 12 spatial links, SU(2) Wilson weight. This is a constructed combinatorial proxy, not certified Penrose spatial geometry. This note extends `r3_two_loop_7state.py`. The full untruncated mixed trace is **not** determined.

## Two shared-edge channels
Let `a,b` be adjacent oriented plaquettes with one common spatial link, and let `x_a=chi_{1/2}(W_a)`, `x_b=chi_{1/2}(W_b)`. Choose gauge-tree transports so the outer boundary loop is `o_ab=chi_{1/2}(W_a W_b)` (relative orientation of the adjacent plaquette words fixed to cancel the common edge). SU(2) Schur orthogonality on the common edge gives conditional projector `P_{j=0}(x_a x_b)=o_ab/2`. From independent Haar plaquette coordinates:

  ||x_a x_b||²=||o_ab||²=1,   <x_a x_b,o_ab>=1/2.

The *normalized orthogonal* link-spin eigenstates are

  psi_ab^(0)=o_ab,
  psi_ab^(1)=(2/sqrt(3)) (x_a x_b-o_ab/2).

They are eigenstates of the temporal one-link convolution on the common edge with j=0,1 respectively; the six nonshared perimeter edges each carry j=1/2. In temporal step r,

  k_ab^(0)(r)=prod_{six perimeter e} k_1/2(t_{r,e}),
  k_ab^(1)(r)=k_1(t_{r,shared}) prod_{six perimeter e} k_1/2(t_{r,e}),
  k_j(t)=I_{2j+1}(t)/I_1(t) (t>0), and k_j(0)=delta_{j0}.

**Note**: orthogonality to other included loops uses the full product Haar spatial measure and their distinct edge-spin labels. The two channels above are an orthonormal basis in the adjacent fundamental-pair subspace; no claim is made that the 15 states exhaust the Hilbert space.

## Exact Wilson matrix elements
For independent Haar plaquette holonomies `h_a=x0_a I+i vec_a sigma`, let `x_a=2x0_a`. Then

  o_ab = x_a x_b/2 - 2 vec_a . vec_b.

For spatial factor f=prod_{c=0}^3 w_kappa(h_c), set unnormalized moments `m_n=int_SU2 w_kappa(g) chi_{1/2}(g)^n dg`. They are calculated exactly by the SU(2) character recursion `chi_{1/2} chi_j=chi_{j+1/2}+chi_{j-1/2}` and the Wilson character coefficients `a_j=2(2j+1)e^{-kappa}I_{2j+1}(kappa)/kappa`.

Each of the 15 states has a scalar polynomial component `P_alpha(x_0,...,x_3)` and, for an adjacent pair, possibly a vector dot component `c_alpha vec_a.vec_b`. The exact matrix `F_alpha,beta=int f psi_alpha psi_beta` equals the product of scalar moments plus, **only if the two vector-dot pairs coincide**, the contraction

  c_alpha c_beta/3 * (m_0-m_2/4)^2 * m_0^2.

Cross terms with one dot vanish by odd-vector symmetry, and dot terms for distinct adjacent pairs vanish because some vector appears only once. This computes the *full* principal 15x15 Wilson multiplication block, including all 7-to-8 cross terms and two-loop shared-edge intertwiners. The `j=0` and `j=1` states are kept separately and are not spuriously treated as independent product-loop eigenfunctions.

## Quantitative two-step defects in a three-step periodic system
Use spatial kappa=2, baseline all temporal faces absent and the third transfer a vacuum projection. The previously used diagonal pattern activates only the seven original states and does not test shared-edge spin recoupling. Therefore also use truly adjacent overlapping supports:

* Temporal step 1: union of perimeter-link sets of faces {0,1}, each t_e=3.
* Temporal step 2: union of perimeter-link sets of faces {0,2}, each t_e=5.

These have an overlapping face 0 and activate `j=0,j=1` adjacent channels in each interval.

The exact 15-state mixed sum gives **9.076315414884484e-10**, compared with **7.560595306497718e-10** from its embedded seven-state part. Its additional recoupling contribution is **+1.5157201083867655e-10**, consisting of one-loop/adjacent cross **+1.448773519064467e-10** and adjacent/adjacent **+6.694658932229848e-12**. In this convention the entire 15×15 spatial matrix is entrywise nonnegative at kappa=2; signs are not invariant under arbitrary sign changes of basis vectors, and this does not imply a globally entrywise nonnegative spin-network basis.

## Scalar comparison and remaining bound gap
Define `T=Tr(F K1 F K2 F P0)` and baseline `T0=Tr(F P0 F P0 F P0)=F_00^3`. The true mixed coefficient `M` sums over **all** gauge-invariant spin networks, not just these 15. A negative contribution from excluded states can outweigh a selected positive principal contribution. Thus neither `T>=T0` nor the target `Z_insert/Z_cavity>=prod q(t_e)` follows from this finite block.

A scalar fallback always exists on this **fixed** 3-step 12-prism complex: after 26 vertex gauge fixes, 63-26=37 free SU(2) links. With all present couplings bounded by `c lambda`, Haar balls of radius `O(lambda^-1/2)` around a simultaneous flat connection give `Z_full>= c' lambda^(-111/2)`, while `Z_cavity<=1`. Hence `F_Q<=55.5 log lambda+C` for lambda>=1. This cost is volume-dependent and is **not** the ambient-uniform C|Q| log lambda theorem. Any claim of a support-local large-coupling bound requires an additional localized scalar comparison or a uniform relative control of the omitted intertwiner tail. A fixed representation truncation is not uniform as lambda→infinity.

To reproduce: `python /mnt/data/r3_shared_edge_recoupling.py`; see `r3_shared_edge_15state_matrices.npz` and `r3_shared_edge_15state_certificate.json`.
