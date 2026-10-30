# The Singular Boundary — Penrose-family C5 covariance and physical Hamiltonian coercivity

26 October 2026. Mathematical investigation; distinction between source statements, established general theory, deductions, and unproved obligations.

## Source and physical scope
Paper 3 of dissertation v10.7 defines the representation `sigma(z1,z2)=(omega z1,omega^2 z2)` and `J(z1,z2)=(i z1,i z2)`. Its helical observer uses pitches 3/13,5/13,8/13. This does **not** identify sigma with exp(2pi J/5), and observer winding is not energy evolution. Stage 26 is a finite (2+1)D weighted SU(2) Wilson simulation, with its `stage26_outer.py` calling `stage22_shifted.setup_geometry` and `stage7_checkpointed` internals; the full production plaquette/coupling builder is not yet certified in this audit. The results below are finite-cutoff conditional theorems, not a claimed four-dimensional continuum Yang–Mills solution.

## Definition 1 — Canonical C5 family map, not fixed M55 symmetry
Let T be a Penrose rhombus tiling from a regular pentagonal cut-and-project window with physical embedding pi_parallel of Z5 and perpendicular embedding pi_perp. Write an element n in Z5, and let S be cyclic permutation of the five integer coordinates. The two physical and perpendicular representations obey pi_parallel(Sn)=R_{2pi/5}pi_parallel(n) and pi_perp(Sn)=R_{4pi/5}pi_perp(n), with convention-dependent orientation signs. The window W must be carried to S_perp W (or, for C5-symmetric W, fixed), and offset/phason xi must be carried to S_perp xi, with boundary-hit conventions preserved. This constructs a map of tilings T_xi -> T_{S_perp xi}, possibly returning the same hull member only for special offsets. It maps vertices, rhombus edges, faces, and oriented boundary cycles. If patches are chosen as r-invariant domains (e.g. disk centered at rotation center) or transported as patches G -> rG, induced boundary complexes are isomorphic. **A fixed arbitrary patch or the periodic rational M55 quotient need not be invariant.**

### Proof of graph map
The integer permutation S is bijective; if n is accepted, pi_perp(n)-xi ∈ W, then pi_perp(Sn)-S_perp xi belongs to S_perp W. Differences in the Z5 unit basis are permuted; rhombus incidences thus map to rhombus incidences. Physical distances and areas are unchanged under R. Oriented face loops are carried to oriented loops, possibly with orientation reversal if a reflection is used instead. Conditions on singular window boundary points must be fixed so no vertex is gained or lost spuriously. This construction works equally on finite transported patches and on the hull, with measurability issues for family Hilbert spaces addressed separately.

## Definition 2 — Coupling-preserving map
Define beta_s(f)=B_s(I_s(f)), beta_t(e)=B_t(I_t(e)) where I_s and I_t are geometric invariants preserved by the rotation, such as face area, edge length, or assigned edge/face type transported with geometry. Require all local coefficients real, beta_t(e)>0, and constant in Euclidean time. Then beta_s'(r f)=beta_s(f), beta_t'(r e)=beta_t(e). A coupling prescription that depends on an absolute laboratory orientation, a non-transported phason, a non-covariant anchor label or a non-transported boundary potential can break this property. Gauge invariance alone is insufficient for C5 covariance.

## Theorem 1 — Exact Wilson action and transfer covariance
For two finite spatial weighted gauge complexes G,G' related by a bijection phi of vertices, edges and faces preserving their incidences, orientations up to inversion, both spatial beta_s and temporal beta_t, temporal ribbons, and time boundary conditions, let X_G=SU(2)^E and H_G=L²(X_G,Haar)^{SU(2)^V}. The pullback U_phi maps gauge-invariant functions between H_G and H_G' unitarily (Haar invariance and preservation of Gauss transformations). With the standard one-step gauge-projected Wilson transfer T_G and T_G', one has T_G' U_phi = U_phi T_G. When transfer operators are positive with maximal eigenvalue lambda_0, the normalized generators H_G=-(1/a_t)log(T_G/lambda_0) satisfy H_G' U_phi=U_phi H_G. Hence eigenvalue sets and gaps coincide **within each corresponding fibre**.

Proof: phi permutes spatial Haar link variables, with inversion where needed (Haar invariant). Spatial Wilson traces map termwise with preserved coefficients. In temporal gauge the cross-slice ribbons map to the same edge factors; hence the integral kernels transform by change of variables. Gauge projections intertwine under phi, proving T covariance. Functional calculus proves H covariance. This result follows from standard gauge transfer constructions; no originality is claimed for the general covariance lemma.

## Corollary 1 — Explicit family lift
Let O={G,rG,...,r⁴G} with fibre Hilbert spaces H_k and unitary maps U_k:H_k -> H_{k+1} satisfying 5-fold cocycle consistency. Then the direct sum K=⊕_{k=0}⁴ H_k supports a unitary family shift R with R⁵=I. Define T_family=⊕ T_k. Then [R,T_family]=0 and K decomposes into five C5 character sectors, with projections P_l=(1/5)Σ_{j=0}⁴ exp(-2pi i lj/5)R^j. Crucially, the fibre vacuum appears five times and gives five degenerate family ground states: **a direct-sum gap defined above a unique global vacuum is ill-posed**. One should either restrict to a fibre or remove the full family vacuum subspace, or define a covariant bundle rather than regard its sum as one ergodic quantum gauge theory. Equal-energy copies are not a nontrivial excitation gap.

## Proposition 2 — Source of genuine spectral selection rules
If a single fixed spatial gauge complex has an exact weighted graph C5 automorphism r, then R commutes with T on that fibre. If the normalized ground state is unique and C5 invariant, and O_l transforms under C5 character l, matrix elements <n,k|O_l|Omega> vanish unless the excited state lies in the sector k=l (with dual convention for complex conjugation). At finite M55 the existence of such an automorphism is **not** established (prior finite Euclidean isometry search found only identity), so do not claim these selection rules for Stage 26. A Penrose-family covariance is *not* automatically fixed-fibre symmetry.

## Obstruction 1 — C5 covariance cannot force a mass gap
Choose an arbitrary positive transfer operator T_epsilon with normalized eigenvalues (1,exp(-epsilon)), and take five identical C5-related fibres. All covariance statements hold exactly, for arbitrary epsilon>0, including epsilon->0 as volume grows. Therefore there is no implication [C5 covariance] => [uniform gap]. Similarly J²=-I and [J,sigma]=0 do not produce coercivity. Any mass-gap result needs dynamics-sensitive inequalities. This is a theorem of logical insufficiency, not a no-go theorem against all possible J-dependent interaction mechanisms.

## Proposition 3 — A *physical* Hamiltonian coercivity bound at zero magnetic coupling
On a finite connected spatial graph let H_E=Σ_e a_e (-Δ_{SU(2),e}) acting on the gauge-invariant L²(SU(2)^E) space, with a_e>=a_*>0. SU(2) Peter–Weyl decomposition gives eigenvalues j(j+1), j=0,1/2,... for each -Δ_e. The constant function is the unique zero-energy state on the full tensor product, hence also on its gauge-invariant subspace. Any normalized orthogonal vector has expectation >=(3/4)a_* (the actual physical gap may be higher because Gauss constraints restrict excitations). Thus H_E >= (3/4)a_* (I-|Omega_E><Omega_E|) as a quadratic form on the physical space, independent of the number of edges. This is a genuine volume-uniform finite-scale **strong-electric/electric-only** result; not a J-derived bound. If the a_e depend on a, the physical gap estimate scales with a_*(a) and does not by itself survive the continuum limit.

Proof: Peter–Weyl diagonalizes each edge Laplacian, with smallest nonzero eigenvalue 3/4, and tensor-product eigenfunctions span the full Hilbert space. Gauge projection commutes with H_E. Since a nonconstant tensor-product component has at least one excited edge, its eigenvalue is >=3a_*/4. Restricting to gauge invariant states cannot lower this bound.

## Proposition 4 — Explicit but volume-deteriorating magnetic perturbation bound
Let H=H_E+B, with B=Σ_f b_f(1-(1/2)ReTr W_f), b_f>=0. Each SU(2) plaquette term is a bounded nonnegative multiplication operator between 0 and 2, so ||B||<=2 Σ_f b_f. For the two lowest eigenvalues ordered with multiplicity, min-max/Weyl eigenvalue shift gives

  gap(H)=E_1(H)-E_0(H) >= (3/4)a_* - 2||B|| >= (3/4)a_* - 4Σ_f b_f.

Here the first inequality follows because the electric-only E_1>=3a_*/4 and E_0=0, and each eigenvalue shifts by at most ||B||. In fact since B>=0 and E_0(H)>=0 while E_1(H)>=E_1(H_E), the same conservative estimate holds; no claim of sharpness. Because Σ_f b_f grows proportionally to the number of faces at fixed couplings, the bound becomes vacuous as volume grows. **A local gap-stability theorem or independent clustering/Dirichlet-form argument is required to improve the estimate.** The finite-degree/finite-local-complexity Penrose structure might help establish the required uniform local constants, but C5 covariance alone does not.

## Candidate 5 — Local perturbative stability, not proved here
At strong electric coupling, study H/H_unit = H_E/H_unit + Σ_f v_f with small local interaction norms, uniformly bounded face degree, face length and overlap. One may attempt a locally uniform gap stability theorem for a product-ground-state unperturbed Hamiltonian (on the unconstrained tensor-product edge space, before restricting to Gauss states), then restrict the result to gauge invariants. Verify precise hypotheses for unbounded electric Laplacians, graph-dependent non-translation-invariant interactions, operator domains, and any finite-volume boundary. No theorem from regular translational lattices can be imported automatically to a Penrose tiling; prove all required constants independent of tiling patch size. Success would establish a gap only in a specified **strong-coupling regime at fixed scale**, not weak-coupling continuum Yang–Mills.

## Candidate 6 — Direct transfer contraction criterion
For each finite patch and physical lattice parameters, normalize T so its leading eigenvalue is 1. A uniform gauge-invariant gap would follow from ||T|_{Omega^perp}|| <= exp(-a_t m_*) for one positive m_* independent of spatial patch and regulator, provided the positive transfer and unique vacuum are certified. Equivalently H-E0 >= m_*(I-P_Omega). Neither C5 covariance nor the fundamental-representation background connection Laplacian gives this estimate. To connect Level I graph coercivity to this physical statement requires an explicit operator-form comparison on the SAME physical Hilbert space; no such comparison is currently known in this program.

## Scaling and 2+1D vs 3+1D
Stage 26 explores (2+1)D SU(2) at one beta_ref, finite Nt and one graph size. Even a proven uniform gap there would not solve the 3+1D continuum constructive Yang–Mills problem. A continuum ratio m_0++/sqrt(sigma) requires separately admitted m_0++, sigma, nonperturbative anisotropy/scale matching, multiple regulator scales and infinite-volume control. The dissertation's one-loop suppression depends on graph definition; no numerical factor or 3:5:8 kinematic pitch can substitute for a physical gap proof.

## What exactly preserves Wilson couplings?
1. Exact parent Z5 coordinate cycle S, with phason/window carried covariantly, yields correspondence among Penrose hull tilings.
2. All rhombus geometric face areas, edge lengths, incidence, face-type labels transported by S preserve distance/area-based couplings.
3. Graph cochains and oriented plaquette traces preserve SU(2) Wilson action, modulo conjugation/inversion of loop holonomy.
4. Fixed periodic M55 quotient, fixed chart, absolute-angle-sensitive or otherwise label-sensitive couplings, and arbitrary cropped boundaries do NOT automatically preserve C5; they require independent proof.
5. The full Stage 26 production builder (`stage7_checkpointed.setup_geometry`) has not been independently checked for timelike positive factors and seam in these files; the class theorem is **not yet a source-certified statement about Stage 26**.

## Evidence and prior work
- Paper 3 of Sharpe dissertation v10.7: effective C5 representation, J structure, helical observer. The parent-space rotations and their interpretation are source-derived; the transfer covariance, electric gap and obstruction are mathematical deductions developed in this memorandum.
- K. Osterwalder and E. Seiler, “Gauge field theories on a lattice,” Ann. Phys. 110 (1978), 440–471, https://doi.org/10.1016/0003-4916(78)90039-8: lattice-gauge reflection positivity and strong-coupling infinite-volume program.
- P. Menotti and A. Pelissetto, “General proof of Osterwalder–Schrader positivity for the Wilson action,” Commun. Math. Phys. 113 (1987), 369–373, https://doi.org/10.1007/BF01221251.
- The bounded-perturbation/min-max estimate above is elementary; strong-coupling volume-uniform stability on nonperiodic complexes is a separate unproved proof obligation here.

## Acceptance gates
A. Specify one canonical nonsingular Penrose hull and finite transported patch family, with C5-compatible window/phasons/boundaries.
B. Supply weight functions and verify exact equality beta_s'(rf)=beta_s(f), beta_t'(re)=beta_t(e); identify positive temporal couplings from original production source.
C. Establish T-family covariance and gauge invariance by the change-of-variables proof; do not confuse orbit covariance with a fixed-fibre representation.
D. Prove an interacting gap (at least fixed-scale strong coupling) with a volume-independent local stability argument, or find an explicit counterexample to proposed hypothesis.
E. Study physical scaling separately; demand uniform-in-volume bounds first and regulator scaling second. No additional Monte Carlo campaign is required for A–D.
