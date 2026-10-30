# R3 — Relative curvature repair, rank obstruction, and a bounded-local-filling theorem

Date: 2026-10-27. Status: exact linear algebra and cellular identities; the final nonlinear Yang–Mills R3 inequality remains **open**. The worked examples are a constructed 2×2 quadrilateral disk × three periodic time steps, **not a verified Penrose tile extraction**. The abstract sufficient conditions apply to any genuine rhombus-prism complex satisfying them.

## 1. Exact conditional least-squares identities

Let D be the oriented edge–face boundary matrix, let Q be a set of inserted faces, R its complementary retained faces, L all links incident to Q, and E the exterior links. For S=R or S=R∪Q, write A_S=D[L,S]^T and B_S=D[E,S]^T. The exterior Gaussian effective form after optimizing local variables is

 C_S=B_S^T Π_S B_S,    Π_S=I−A_S A_S^+.

It is positive semidefinite. The relative exterior rank is exactly

 rank(C_S)=rank(D[:,S])−rank(D[L,S]),

which can be established using integer/modular arithmetic. Also C1≥C0.

Define u0(ξ)=−A_R^+ B_R ξ, residual r0=(I−A_RA_R^+)B_R ξ, and the inserted mismatch t=(B_Q−A_Q A_R^+ B_R) ξ = T ξ. Then

 ξ^T(C1−C0)ξ=min_v (||A_R v||²+||A_Q v+T ξ||²).

Let J=A_R^T A_R+A_Q^T A_Q and G=I−A_Q J^+ A_Q^T (a positive semidefinite q×q matrix, 0≤G≤I). Therefore the exact factorization is

 C1−C0=T^T G T≥0,   rank(C1−C0)≤|Q|.

Let Rmap=(I−A_RA_R^+)B_R, so C0=Rmap^T Rmap. Uniform domination C1≤M C0 is equivalent to the relative-repair inequality

 ||G^(1/2) T ξ|| ≤ sqrt(M−1) ||Rmap ξ||  for every ξ.

For one finite system it holds for finite M iff ker(C0)=ker(C1), and its optimal factor is

 M_min=1+||G^(1/2) T Rmap^+||².

This algebraically optimal map need not be spatially local! For a genuinely local repair theorem, one needs a bounded-range factorization through nearby retained residuals, uniformly over all support shapes and ambient volumes. Bounded Penrose face degrees or finite local complexity alone do not supply it.

## 2. Good and rank-obstructed supports on the SAME complex

`verify.py` uses the exact three-step incidence from the previous R3 calculation and modular Gaussian elimination over p=1,000,003, cross-checking the effective real symmetric matrices.

Good support (14 temporal faces): Q=[12,13,14,15,16,17,18,24,25,26,27,31,32,33]. Local links 36, exterior links 27, exterior ranks C0/C1=5/5, generalized eigenvalues [1,1.0028617068,1.0041769540,1.3036544364,1.4327744517]. M_min=1.43277445. Perturbation rank 4. The earlier Gaussian exterior frustration determinant is 0.9477150612.

Rank-changing support (8 temporal faces): Q=[13,18,22,25,26,29,32,37]. Local links 26, exterior links 37, exterior ranks C0/C1=10/11. There is an explicitly saved unit exterior witness ξ with ξ^T C0 ξ=0 (roundoff <1e−14), while ξ^T C1 ξ≈2.3007160417. Thus **no finite M exists** for that support's unregularized quadratic forms. This invalidates any universal claim that bounded-valence prisms automatically preserve exterior rank for arbitrary selected faces. It is a counterexample in the constructed quadrilateral model, not a proven counterexample on a specified true Penrose patch.

## 3. An explicit uniform local filling criterion from the prism Bianchi identity

Assume the rhombus-prism complex has quadrilateral prism cells (each with six faces), every face belongs to at most two prism cells, and the inserted Q satisfies:

 For each q∈Q, one can choose a prism c(q) containing q, with all five other faces retained; no selected prism is used for more than one q.

The exact cellular equation ∂2∂3=0 constructs a **strictly local**, integer-valued map H from inserted to retained face chains,

 D_Q=D_R H.

Every column of H has ≤5 entries of absolute value 1, and every row ≤2. Thus ||H||²≤||H||_1||H||_∞≤10, **uniformly in the ambient number of cells**. For any L/E link split, the face curvature constraints obey r_Q=H^T r_R for every linearized link configuration, and

 C1≤(1+||H||²) C0≤11 C0.

This establishes rank preservation and spectral domination for the geometrically isolated-face class on any complex satisfying the stated cell adjacency conditions. Note that H is a **face-filling/constraint repair map**, not a construction of an actual SU2 link-coordinate transport or a right inverse to the local link Jacobian.

In `bianchi_repair.py`, Q=[12,16,19,24,28] consists of five separated temporal faces on the three-step constructed complex. The integer array H (43 retained faces ×5 inserted faces) satisfies D_Q=D_RH exactly, with max column sum 5, max row sum 2, ||H||²=7.1357792051. The actual exterior generalized maximum is 1.3953488372. `bianchi_certificate.json` records the five explicit neighboring prisms.

### Nonlinear counterpart, already exact at the level of plaquette holonomies

The nonabelian lattice Bianchi relation expresses each inserted prism-face holonomy, after parallel transport, as a product of five retained face holonomies or inverses. For SU2 Wilson deficit d(U)=1−Tr U/2, chordal triangle inequality yields d(∏_{i=1}^k U_i)≤k∑_i d(U_i), and d(V U V^{-1})=d(U). Hence for the above isolated-face class

 d(W_q)≤5∑_{p∈∂c(q)\{q}} d(W_p).

For comparable Wilson face couplings this is an *ambient-independent pointwise bound on local curvature*. It does **not** automatically prove a partition-function ratio. A sufficient additional condition is a uniform retained-face energy estimate sup_p β_p E_{μ0} d(W_p)≤K. Jensen then yields −log E_{μ0}exp(−V_Q)≤25(γ_max/β_min)K|Q|, given the five-face filling and β_min>0. That additional uniform energy estimate is NOT proved here.

## 4. Rank-changing supports still give logarithmic cost in a REGULARIZED Gaussian proxy

For η>0 independent of λ, add an isotropic quadratic exterior reference η||ξ||²/2 and define formal exterior Gaussian partition functions with Hessians ηI+λ C_i. For three Lie-algebra color directions, the regularized frustration free energy is

 H_η(λ)=(3/2) log det(ηI+λ C1)/det(ηI+λ C0).

Let ν=max number of faces incident to an edge, p=max number of edges in one face, and assume each face's quadratic weight is at most λ (or multiply pν by the uniform weight bound). Since the exterior matrix B1 is a submatrix of D^T,

 0≤C1≤B1^T B1≤||D||² I≤pν I.

Combined with rank(C1−C0)≤|Q|, the determinant lemma gives the **uniform regularized Gaussian theorem**:

 0≤H_η(λ)≤(3/2)|Q|log(1+λ pν/η).

This holds for arbitrary Q, including rank-increasing supports, on any finite bounded-degree cell complex; the constant is ambient-volume independent. It requires no spectral domination C1≤M C0. At fixed finite volume, if r=rank(C1)−rank(C0), then H_η(λ)=(3/2)r log λ+O(1) as λ→∞.

The current 3-step complex has p=4, ν=4, and ||D||²=9. The 8-face example has r=1 and slope 3/2, confirmed at λ up to 100,000 by `verify.py`; `uniform_gaussian.py` tested the dimension-independent determinant inequality on 38 distinct support sets.

**Physical limitation:** ηI is an additional *exterior quadratic regularization* of the linearized Gaussian model, NOT a consequence of normalized SU2 Haar measure or a gauge-invariant mass term. The physical unregularized Gaussian has flat directions and its normalizing integral is undefined without quotienting or compactifying them. Compact SU2 has different flat-connection sectors and Jacobians. Therefore this Gaussian result cannot be cited as an established Wilson R3 insertion theorem.

## 5. Implication for arbitrary Penrose prism supports and the nonlinear remainder

The original proposed 'rank preservation plus uniform spectral domination for all arbitrary Q' cannot be automatic: even among combinatorially simple prism cavities there exist rank-changing supports. For a *particular* Penrose support there are two paths:

 **A. Local filling:** identify a bounded-radius face-chain map H with D_Q=D_RH and bounded operator norm, verified at every support component with uniformly bounded overlap. This gives exact linearized uniform domination and a nonlinear local Bianchi curvature bound. Finite local complexity can reduce checks to a finite set of bounded-radius patch types **once the radius and compatible supports have been fixed**, but it does not establish the existence of bounded fillings for arbitrary large connected Q.

 **B. Allow new exterior modes:** accept rank(C1)>rank(C0), control their number by |Q| using the exact low-rank update, and seek a *physical* compact-Haar analogue of the regularized Gaussian determinant bound. This must handle nonlinear SU2 holonomy, gauge quotient, near-flat moduli, and possible boundary frustration without introducing an unjustified ηI reference.

An ambient-uniform nonlinear comparison should only be pursued with an explicit local gluing map or local density-lower-bound certificate, including a uniform bound on its Jacobian and retained-action cost. The finite Gaussian determinant estimate is encouraging but does not establish these nonlinear hypotheses. A full Yang–Mills continuum mass gap remains open.

## Reproduction

Run `python verify.py`, `python bianchi_repair.py`, and `python uniform_gaussian.py`. Outputs: `certificate.json`, `effective_forms.npz`, `bianchi_certificate.json`, `bianchi_operator.npz`, `uniform_gaussian_certificate.json`. No Monte Carlo is needed.

### Exact-rational rank confirmation

`python exact_rank.py` independently recomputes all relevant matrix ranks over the exact field QQ using SymPy DomainMatrix. They confirm (rank D_R, rank A_R; rank D_all, rank A_all): good14 (30,25;36,31), rank-changing8 (35,25;36,25), isolated-Bianchi5 (36,16;36,16). These are **exact rational ranks**, not just numerical SVD inferences. The witness nonzero quadratic energy and generalized-eigenvalue magnitudes remain floating-point calculations.
