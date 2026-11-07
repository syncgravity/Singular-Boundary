# Yang–Mills proof gate: incidence-weighted SU(2) Wilson locality and exact interacting-vacuum Poincaré criterion

**November 7, 2026. Scope: finite original-link SU(2), mathematically valid on arbitrary finite oriented 2-skeleta under the hypotheses below. No source-authenticated 3D coupled-Z5 geometry, continuum field theory or physical Yang–Mills mass-gap theorem is claimed. P0–P5/T0–T5/PF-G0–G5 remain OPEN.**

## I. The geometric transfer theorem (classical spatial Wilson flow)

Let \(K_h\) be a finite oriented 2-complex with independent SU(2) link variables \(U_e\). Each oriented face boundary is a **simple** loop, using each undirected edge at most once. Let \(\ell_p=1-\tfrac12\operatorname{tr}U_{\partial p}\in[0,2]\) and face coefficients \(a_p>0\). Fix a length scale \(h>0\) and face-center coordinates \(c_p\) in a metric space. Assume:

* each face has at most \(M\) boundary links;
* every two faces incident to a common link have center distance at most \(\kappa h\);
* the local total coefficient \(A_*:=\max_e\sum_{p\ni e}a_p\) is finite and uniformly bounded along any claimed refinement;
* the SU(2) left-invariant metric is normalized by \(T_j=i\sigma_j/2\), so \(\|\nabla_e\ell_p\|^2=\ell_p(2-\ell_p)/4\) for every boundary edge that occurs once.

Set \(S_a=\sum_pa_p\ell_p\). Let \(\dot U_e=-\nabla_e S_a\) be the **classical** negative Wilson-gradient flow in its dimensionless time \(s\). For any real \(L\)-Lipschitz function \(\phi\) on the face-center metric, define \(w_p=e^{2\phi(c_p)}\), \(w_e=\max_{p\ni e}w_p\), \(S_{a,w}=\sum_pa_pw_p\ell_p\), and \(F_e=\nabla_e S_a\). With \(q=1-e^{-2L\kappa h}\),

\[
\boxed{\frac{d}{ds}S_{a,w}+\frac12\sum_e w_e\|F_e\|^2
\le \frac{A_*M}{4}q^2e^{2L\kappa h}S_{a,w}
\le A_*M\kappa^2L^2h^2e^{2L\kappa h}S_{a,w}.}
\]

For **unit plaquette coefficients**, \(A_*\le D\), the maximum number of faces incident to an edge. If physical smoothing time is **defined** as \(\tau=h^2s\), the exponential energy-transfer rate is bounded by \(A_*M\kappa^2L^2e^{2L\kappa h}\) in \(\tau\). For the cubic reference incidence \(D=M=4\), and the conservative cubic adjacent face-center bound \(\kappa=\sqrt2\), the rate becomes \(32 e^{2\sqrt2Lh}L^2\), recovering the prior cubic coefficient. A different electric/geometric preconditioner or face coefficient scaling requires its **own** time/metric normalization; do not silently use \(\tau=h^2s\).

**Proof.** Write \(g_{ep}=\nabla_e\ell_p\) (zero if not incident), \(G_e=\sum_{p\ni e}a_pw_pg_{ep}\) and \(R_e=\sum_{p\ni e}a_p(w_e-w_p)g_{ep}\). Then \(G_e=w_eF_e-R_e\), and the flow gives \(dS_{a,w}/ds=-\sum_e\langle G_e,F_e\rangle\). Young's inequality yields the displayed dissipation term and the error \(\frac12\sum_e\|R_e\|^2/w_e\). If \(p\ni e\), \(0\le w_e-w_p\le qw_e\) and \(w_e\le e^{2L\kappa h}w_p\). Weighted Cauchy–Schwarz gives \(\|R_e\|^2/w_e\le q^2e^{2L\kappa h}A_*\sum_{p\ni e}a_pw_p\|g_{ep}\|^2\). Summing incidences, using the exact SU(2) gradient identity and at most M boundary links per face, yields \((A_*M/4)q^2e^{2L\kappa h}S_{a,w}\). Finally \(q\le2L\kappa h\). QED.

**Limit:** this is a geometric upper bound on **classical spatial Wilson flow**, not positive-time vacuum-moment smoothing, a quantum transfer matrix, a log-Sobolev estimate or a Yang–Mills mass gap. It is largely *incidence universal*: bounded Penrose–Fibonacci incidence alone would not improve the refinement exponent relative to cubic. Any conjectured geometric advantage must enter a sharper gauge-invariant covariance/spectral estimate, a physical renormalization control, or additional structure.

## II. Exact finite interacting-vacuum Poincaré criterion (quantum Hamiltonian)

On the same finite link set, take the **quantum** gauge-invariant original-link Hamiltonian
\[
H=\sum_e\alpha_e(-\Delta_e)+V(U),\quad \alpha_e>0,
\]
where \(V\) is any real bounded gauge-invariant Wilson potential (including \(\sum_p\beta_p\ell_p\)). Let \(\Omega>0\) be its normalized unique real gauge-invariant ground state, \(E_0\) its energy, and \(\nu=\Omega^2\prod_ed\mathrm{Haar}(U_e)\). On the **Gauss-invariant** domain, for any smooth real gauge-invariant test function \(f\),
\[
\boxed{\langle f\Omega,(H-E_0)f\Omega\rangle
=\sum_e\alpha_e\int\|\nabla_e f\|^2\,d\nu.}
\]
The identity is an **exact ground-state transform**: expand the link Laplacian on \(f\Omega\), integrate by parts on compact SU(2) and eliminate potential/cross terms using \(H\Omega=E_0\Omega\). It includes the actual coupled vacuum: \(\Omega\) is not replaced by Haar or an independent-link product.

Define the positive spectral gap above the gauge-invariant ground state by \(m_{h,R}^{\mathrm{phys}}=\inf\operatorname{spec}((H-E_0)|_{\mathrm{Gauss},\Omega^\perp})\). The min-max principle gives the equivalent exact **weighted gauge-Poincaré criterion**:
\[
\boxed{m_{h,R}^{\mathrm{phys}}=
\inf_{\substack{f\text{ gauge-invariant}\\\mathrm{Var}_\nu(f)>0}}
\frac{\sum_e\alpha_e\int\|\nabla_e f\|^2d\nu}{\mathrm{Var}_\nu(f)}.}
\]
Thus a **uniform** physical mass-gap candidate \(m_*>0\) requires proving, in the actual refining interacting theory, for every gauge-invariant \(f\),
\[
\mathrm{Var}_{\nu_{h,R}}(f)\le m_*^{-1}\sum_e\alpha_{e,h,R}\int\|\nabla_e f\|^2d\nu_{h,R},
\]
with constants independent of h and the intended thermodynamic limit, and the correct physical clock and normalization. Such a bound gives finite-regulator Euclidean time covariance decay \(|\langle f\Omega,e^{-t(H-E_0)}g\Omega\rangle|\le e^{-m_*t}\sqrt{\mathrm{Var}_\nu(f)\mathrm{Var}_\nu(g)}\) for centered gauge-invariant f,g. A nontrivial 4D continuum theory and Osterwalder–Schrader/physical reconstruction remain additional open existence gates; finite uniform bounds alone do not establish them.

**Finite positivity is not enough.** Since each SU(2)^E link space is compact and its ground state positive smooth, every fixed finite regulator has some Poincaré constant. Haar product comparison provides the crude lower bound \(m_{h,R}\ge\frac34\alpha_{\min}\,\rho_{\min}/\rho_{\max}\), where \(\rho=\Omega^2\) relative to product Haar and 3/4 is the first SU(2) Casimir eigenvalue in this metric. The density-ratio bound can deteriorate drastically with volume or h and is not a continuum proof. A restricted set of observer Wilson loops cannot substitute for the **all gauge-invariant test functions** inequality.

## III. Proof interface: PF geometry versus cubic control

**Immediately available:** the nonlinear face-incidence lemma above applies conditionally to any finite authenticated PF physical SU(2) cell complex satisfying its hypotheses; the interacting-vacuum Poincaré identity is valid on any finite such gauge complex. No quasicrystallineity is assumed in either identity.

**Still required, in proof order:**

1. **P0/PF-G0:** establish the exact original coupled-Z5 source generator (slice/quotient, acceptance, directed adjacency, 34:55 only if needed as evidence). It is not a certified 3-extended-spatial gauge regulator.
2. **P0/PF-G1:** build a genuinely refining **three-dimensional** physical cell complex with \(\partial^2=0\), shape-regular cell metric and bounded \(M,\kappa,A_*\) after physical normalization. Distinguish the 4-real-dimensional Z5 diagonal quotient and any compact perpendicular coordinate from three extended spatial axes.
3. **P1/PF-G2:** define exact Gauss constraints, positive electric coefficients \(\alpha_e\), Wilson \(V\) with physical geometry weights, and boundary/time renormalization. Check self-adjointness, the physical coupling and positivity of the finite ground state.
4. **P2/PF-G3–G4:** on the **genuine interacting vacuum**, prove a nontrivial \(h,R\)-uniform gauge-invariant Poincaré/covariance inequality; compare against cubic with the same physical observables, clock, support and normalization. The earlier signed current, interacting Fisher, quantum parity and nonlinear spatial-flow bounds are supporting tools, not this inequality.
5. **P3/P4/P5/PF-G5:** control positive-physical-flow-time renormalized field observables, establish a nontrivial 4D continuum OS theory and obtain a strictly positive reconstructed spectral gap; spatial clustering and reflection positivity remain distinct proof obligations.

**Verification:** finite SU(2) noncommuting quaternion holonomies on a tetrahedral face complex and cube boundary: 200 configurations with exact one-link gradients, local M/A/κ and weighted-flow inequalities PASSED. Separately 36 interacting SU(2) class-rotor quantum checks of the exact ground-state Dirichlet form, Poincaré variational inequality and eigenvalue gap PASSED. No authenticated 3D Penrose–Fibonacci coupled vacuum has been numerically computed or assumed.

## IV. New exact C5 representation obstruction and three-dimensional candidate

Let \(C\) cyclically permute the five coordinates of real \(\mathbb R^5\). Under the *real* orthonormal Fourier transform its irreducible decomposition is the trivial 1D representation plus two mutually nonisomorphic real 2D irreducible rotations (angles 2π/5 and 4π/5). Consequently the **diagonal quotient** \(\mathbb R^5/\mathbb R(1,1,1,1,1)\cong E_1^2\oplus E_2^2\) has **no C5-invariant real 3D subspace**, because its invariant real subspaces have dimensions 0,2,4. This is an exact representation-theoretic obstruction to using the diagonal quotient itself as a C5-equivariant three-extended-spatial physical model.

But the **unquotiented** source five-dimensional space has the canonical 3+2 split
\[
E_{\mathrm{phys}}=E_0^1\oplus E_1^2,\qquad E_{\mathrm{internal}}=E_2^2,
\]
where \(E_0\) is the diagonal trivial axis. The explicit physical orthonormal coordinates on \(m\in\mathbb Z^5\) are
\[
y_0=\frac{\sum_jm_j}{\sqrt5},\quad
(y_1,y_2)=\sqrt{\frac25}\sum_jm_j\big(\cos\tfrac{2\pi j}5,\sin\tfrac{2\pi j}5\big),
\]
with internal coordinates \((u_1,u_2)=\sqrt{2/5}\sum_jm_j(\cos(4\pi j/5),\sin(4\pi j/5))\). This is an exact **C5-equivariant physical 3D projection**. Each integer-basis edge has physical length \(\sqrt{3/5}\), the diagonal axial coordinate changes by \(+1/\sqrt5\) along every positive basis edge, and the internal shift has length \(\sqrt{2/5}\). A fixed integer coordinate sum is just a single axial *layer*; it cannot support within-layer one-basis neighbours. Retaining all axial layers makes one-basis neighbour edges possible. This does **not** prove that the original dissertation implemented this 3+2 split or that a C5-equivariant complete 3D mesh is obtained.

### Finite-source-inspired cubical screening

For an **illustrative only**, not source-authenticated, regular-decagon internal acceptance window, and a bounded physical 3D cylinder, a full \(m\in[-4,4]^5\) enumeration gave **903 accepted vertices, 2,620 basis edges, 2,810 complete elementary square faces, and 1,360 complete elementary three-cubes**. All elementary cube boundaries close combinatorially (\(\partial_2\partial_3=0\)); the physical 3D projections of any three *distinct* five basis directions have nonzero determinant (the ten absolute values lie between about 0.235 and 0.380 in orthonormal units). The worst finite face/link incidence is \(D=8\) and \(M=4\). Thus the incidence theorem in Part I gives a **conditional finite 3D projected complex** weighted-flow inequality if the intended physical action uses those faces and the chosen link metric.

**A substantive obstruction appears immediately:** among square faces used by its accepted elementary cubes, **1,700 have more than two incident three-cubes**, up to six. Hence the naive projected full 5D cubical 3-skeleton is **not a three-manifold cell decomposition**; its multiple overlapping 3-cells cannot be silently treated as a legitimate 3D regulator. A direct 3D Delaunay tetrahedralization of these 903 projected vertices has simplex-face incidence at most two, but yields **hundreds of zero-volume/degenerate tetrahedra** for tested Qhull options and no refinement-uniform shape-regularity. This is another geometry failure, not a solved construction.

**Proof implication:** The physically natural 3+2 projection can repair the *rank* obstruction, but a separately specified **non-overlapping, shape-regular, genuinely refining 3D cell-selection/triangulation rule** is still missing. Such a rule must preserve gauge cell incidence, physical normalization, and an adequate degree of fivefold/quasicrystalline structure. The source-authenticated coupled-Z5 construction must be distinguished from this new illustrative regulator candidate. The next proof step is P0/PF-G1 **physical 3D mesh construction**, not further helical observer or parity forensics.

### Verification

The local finite scripts \`verify_z5_3d_gauge_skeleton.py\` and \`verify_z5_delaunay_3d_candidate.py\` examine the 3+2 Fourier projection, C5 invariance, full cubical \(\partial^2=0\), source-illustrative vertex/edge/face/cube counts and 3D nonmanifold incidence; Delaunay tests expose degeneracy. The scripts run entirely on synthetic window parameters, not original dissertation source code. The conditional incidence theorem and quantum Poincaré identity are exactly the currently portable mathematics; the physical shape-regular mesh and genuine interacting PF vacuum remain OPEN.

## V. New arithmetic Delone theorem and an honest 3D Voronoi regulator candidate

The non-manifold projected cubical 3-skeleton in Part IV motivates the **physical Voronoi dual** of the accepted point set instead. This is a NEW mathematics-first regulator proposal, NOT an implementation of the dissertation's original basis-link Wilson Hamiltonian.

Write \(P:\mathbb R^5\to E_{\mathrm{phys}}\cong\mathbb R^3\), \(Q:\mathbb R^5\to E_{\mathrm{internal}}\cong\mathbb R^2\) for the mutually orthogonal real C5 projectors defined in Part IV. Let \(W\subset E_{\mathrm{internal}}\) be a compact C5-invariant window containing a closed disk of radius \(r_{\mathrm{in}}>\sqrt5/2\) about zero and contained in a disk of radius \(R_W\). Define the infinite physical accepted set
\[
X_W=\{P m:m\in\mathbb Z^5,\ Qm\in W\}\subset\mathbb R^3.
\]
The projection P is one-to-one on \(\mathbb Z^5\), and **\(X_W\) is a Delone set with explicit constants**:
\[
\boxed{\|x-y\|\ge \delta_W:=\min\{1/\sqrt5,\,1/(5R_W)\}\quad(x\ne y\in X_W),\qquad
\sup_{z\in\mathbb R^3}\inf_{x\in X_W}\|z-x\|\le R_{\mathrm{cov}}:=\sqrt5/2.}
\]

**Uniform separation proof (cyclotomic norm, an actual Fibonacci/C5 geometric input).** For nonzero integer difference \(k\in\mathbb Z^5\) with \(s=\sum k_j\ne0\), its axial physical coordinate has magnitude \(|s|/\sqrt5\ge1/\sqrt5\). If \(s=0\), the cyclotomic algebraic integer \(z_1(k)=\sum k_j\omega^j\), \(\omega=e^{2\pi i/5}\), is nonzero: the only integer polynomial of degree at most four vanishing at \(\omega\) is an integer multiple of \(1+t+t^2+t^3+t^4\), incompatible with nonzero k and \(s=0\). Its algebraic norm is \(N(z_1)=|z_1|^2|z_2|^2\in\mathbb Z\setminus\{0\}\), so \(|z_1||z_2|\ge1\). Since accepted points have internal difference \(\|Qk\|\le2R_W\), and the orthonormal Fourier coordinates obey \(\|Pk\|\ge\sqrt{2/5}|z_1|\), \(\|Qk\|=\sqrt{2/5}|z_2|\), it follows that \(\|Pk\|\ge1/(5R_W)\). QED.

**Cover proof.** For arbitrary physical \(z\in\mathbb R^3\), lift it to \(Y=P^Tz\in\mathbb R^5\), whose internal coordinates vanish. Coordinatewise round Y to the nearest integer m. Then \(\|m-Y\|\le\sqrt5/2\). In particular \(\|Qm\|\le\sqrt5/2<r_{\mathrm{in}}\), so \(Qm\in W\) and \(Pm\in X_W\), while \(\|Pm-z\|\le\sqrt5/2\). QED.

**Voronoi consequence.** The ordinary Euclidean Voronoi cells \(V_x\) of the Delone set \(X_W\) are a canonical, face-to-face, C5-equivariant (when W is), non-overlapping **three-dimensional convex polyhedral tiling**, and each cell obeys
\[
B(x,\delta_W/2)\subseteq V_x\subseteq B(x,R_{\mathrm{cov}}).
\]
Hence the cells have uniformly bounded *cell inradius/circumradius ratio*, and the number of neighbouring Voronoi cells and the number of polygonal faces/face edges is uniformly bounded by elementary disjoint-ball packing. For scaled \(hX_W\), both in- and out-radii scale as h; it yields a genuinely refining **geometric 3D cellulation** in fixed physical regions. The bounded incidence and adjacency hypotheses in Part I can thus be satisfied with constants independent of h **for the geometric Voronoi model**, provided the face-action weights and chosen metric are also controlled. This is not automatically a full finite-volume quantum gauge-continuum construction: small Voronoi features, weighted Hodge consistency, the physical coupling, and the true interacting-vacuum Poincaré constant remain independent proof obligations.

**Illustrative decagon:** with circumradius \(R_W=1.5\), the regular decagon has inradius \(1.5\cos(\pi/10)\approx1.42658>\sqrt5/2\approx1.11803\). The rigorous separation bound is \(\delta_W\ge2/15\approx0.13333\), and the covering bound is \(R_{\mathrm{cov}}=\sqrt5/2\). The finite accepted 903-site sample has observed minimal physical point separation \(\approx0.45951\); a finite Voronoi calculation identifies 681 cells not touching its truncated convex hull. Random physical targets (10,000) all passed the nearest-integer cover check. These are **sanity checks of the theorem**, not a source-authenticated physical simulation.

**Essential limitation: exact axial periodicity.** The full integer vector \(d=(1,1,1,1,1)\) satisfies \(Qd=0\) and \(Pd=(\sqrt5,0,0)\). Therefore the full infinite model set \(X_W\) is invariant under **the exact physical translation** \(x\mapsto x+(\sqrt5,0,0)\). The C5-equivariant 3+2 construction is not *fully three-dimensionally aperiodic*: its axial direction is periodic, although its five one-basis link directions remain coupled rather than merely a product graph. It must not be asserted equivalent to the intended fully quasicrystalline 3D Penrose–Fibonacci gravitational geometry. Achieving a truly aperiodic 3D physical model may require a larger superspace (for example a separately justified icosahedral construction) or abandoning the exact invariant physical split, both requiring new source/model validation.

**Yang–Mills proof interface, prioritized:** (a) fix the desired geometry class and separate this explicit 3D Voronoi **control/candidate** from the dissertation's actual Z5 source; (b) build original-link or Voronoi-link Gauss-invariant SU2 operators with appropriate metric/electric/plaquette weights and verified Hodge consistency; (c) prove the interacting-vacuum weighted Poincaré inequality uniformly in h and volume on the chosen authentic regulator; (d) independently construct the nontrivial four-dimensional Euclidean/OS continuum theory and physical gap. No gap gate is closed by the Delone/Voronoi result.