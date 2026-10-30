# R3 — Exact relative Haar coordinates and local retained-energy reduction
**27 October 2026.** Verified direct-\(\mathbb Z^5\) cut-and-project Penrose rhombus disks × three periodic time steps. This note reports two unconditional theorems and states clearly the missing hypothesis for the requested full insertion theorem.

## Definitions and scope
For normalized Haar links in a finite SU(2) Wilson plaquette complex, put
\[
d(U)=1-\tfrac12\operatorname{Re}\operatorname{Tr}U\in[0,2],\quad
\mu_R(dU)=Z_R^{-1}\exp\{-\lambda\sum_{p\in R}d(W_p)\}\prod_e dU_e.
\]
Here R is the retained set and Q a deleted/inserted set, with equal positive coupling \(\lambda\) unless noted. A geometry-independent constant can depend on the fixed maximum link incidence \(\nu\), not the ambient volume. In the three-step complex, the first Haar-coordinate theorem applies to **any** collection \(Q\) of temporal faces in steps \(t=0,1\), provided step 2 contains no inserted faces; its extension below also covers supports involving all three intervals as long as each spatial edge has at least one retained temporal face.

## Theorem 1 — exact relative product-Haar chart with \(|Q|\) holonomies
For oriented spatial edge \(e=(u,v)\) write its spatial link at time \(t\) as \(U_e(t)\) and vertical links as \(T_u(t),T_v(t)\). The temporal face word is
\[
Y_{t,e}=U_e(t)T_v(t)U_e(t+1)^{-1}T_u(t)^{-1},\qquad t=0,1\pmod 3.
\]
Choose as pivot the spatial link \(U_e(0)\) for every inserted face \((0,e)\), and \(U_e(2)\) for every inserted face \((1,e)\). Distinct inserted faces have distinct pivots, and **none** of the expressions below contains any other selected pivot:
\[
U_e(0)=Y_{0,e}T_u(0)U_e(1)T_v(0)^{-1},\qquad
U_e(2)=T_u(1)^{-1}Y_{1,e}^{-1}U_e(1)T_v(1).
\]
Each replacement is an invertible SU(2) translation/inversion with exactly unit normalized Haar Jacobian. Thus, for every subset of the two temporal intervals,
\[
\prod_{\text{all links}}dU_e=\prod_{q\in Q}dY_q\prod_{z\in\mathrm{other\ links}}dz.
\]
The \(Y_q\)'s are **independent SU(2) Haar variables under the unweighted reference measure**; they are emphatically NOT independent under the retained Wilson Gibbs measure. The number of replacements is exactly \(|Q|\), all inverse pivot formulas above have word length four in the new and unchanged variables. Every retained quadrilateral face has transformed word length at most \(4+3\cdot4=16\), and every pivot changes its own inserted temporal face and at most three retained faces: the temporal face at step 2 and at most two spatial faces at step 0 or 2. Hence the total number of retained faces touching *some pivot* is at most \(3|Q|\). For arbitrary connected spatial Penrose rhombus disks there is no dependence on support diameter or ambient size. This does **not** require Bianchi peeling or a vanishing exterior linearized rank; it also works for supports with new curvature constraints.

A second (simpler) relative chart uses all links \(L(Q)=\bigcup_{q\in Q}\partial q\), with \(|L(Q)|\le4|Q|\) and bounded incidence \(\nu\). Holding every other link fixed, only the retained faces \(A(Q)=\{p\in R:\partial p\cap L(Q)\ne\varnothing\}\) depend on these coordinates. \(|A(Q)|\le\nu|L(Q)|\le4\nu|Q|\), each **original** face word has length four (after substituting the pivots, every retained word has length at most sixteen), and the arbitrary far retained action cancels in the **conditional** ratio. This chart covers arbitrary all-three-step temporal supports, but it does not give independent inserted-holonomy coordinates.

**Exact boundary-marginal formula**: with \(b\) denoting the finite set of exterior links appearing in the affected retained face words,
\[
\frac{Z_{R\cup Q}}{Z_R}=\mathbf E_{\nu_R}\left[\frac{\int\prod_{q\in Q}dY_q\, e^{-S_{\rm near}(Y,b)-\lambda\sum_{q\in Q}d(Y_q)}}{\int\prod_{q\in Q}dY_q\, e^{-S_{\rm near}(Y,b)}}\right].
\]
Only \(\nu_R\), the retained Gibbs marginal on \(b\), remembers the distant ambient volume. There is no artificial Gaussian regularizer and no charges from retained plaquettes disjoint from the pivots.

### Why this does NOT prove R3 pointwise
For one pivot \(Y\), choose a fixed exterior boundary producing exactly one retained plaquette \(-Y\). The conditional retained action is \(\lambda d(-Y)\) and insertion is \(\lambda d(Y)\). As \(d(-Y)+d(Y)=2\),
\[
\frac{\int e^{-\lambda[d(-Y)+d(Y)]}\,dY}{\int e^{-\lambda d(-Y)}dY}
=\frac{e^{-2\lambda}}{q(\lambda)}\asymp\lambda^{3/2}e^{-2\lambda}.
\]
Thus **no volume-uniform polynomial lower bound on the conditional insertion ratio can hold for every fixed exterior configuration** by a bare Haar-coordinate or bounded-degree argument. Exterior Gibbs averaging or an admissible correlated transport is indispensable.

## Extension of Theorem 1 — cycle-breaking supports across **all three** time intervals
The two-interval hypothesis is sufficient but not necessary. For each spatial edge \(e\), let \(T_e\subset\{0,1,2\}\) record the selected temporal intervals. If \(T_e\ne\{0,1,2\}\) for every \(e\), the selected temporal edges form a forest within the three-vertex time-cycle. There is an explicit choice of distinct spatial-link leaf pivots, and no pivot occurs in any other inserted face word. For \(|T_e|=1\) the choices \(t\mapsto\text{pivot time}\) are \(0\mapsto0,1\mapsto2,2\mapsto2\). For the three possible pairs:

| Selected intervals \(T_e\) | Spatial-link pivot for the first face | Pivot for second face |
|:---|:---|:---|
| \(\{0,1\}\) | \((0,e)\mapsto U_e(0)\) | \((1,e)\mapsto U_e(2)\) |
| \(\{0,2\}\) | \((0,e)\mapsto U_e(1)\) | \((2,e)\mapsto U_e(2)\) |
| \(\{1,2\}\) | \((1,e)\mapsto U_e(1)\) | \((2,e)\mapsto U_e(0)\) |

For pivot on the \(U_e(t)\) (positive) side use \(U_e(t)=Y_{t,e}T_u(t)U_e(t+1)T_v(t)^{-1}\); for a pivot on the \(U_e(t+1)^{-1}\) side use \(U_e(t+1)=T_u(t)^{-1}Y_{t,e}^{-1}U_e(t)T_v(t)\). Since the nonpivot spatial links in these formulas are **not** selected pivots for that edge, all replacements commute as a coordinate construction. Exactly \(|Q|\) inserted holonomies become independent coordinates under product Haar, with each changed spatial pivot appearing in at most three retained faces, regardless of support diameter or ambient patch size. This is an **exact nonlinear group-coordinate theorem**, not a nonabelian curvature repair of the retained Gibbs action.

The theorem does not cover any spatial edge with **all three** temporal faces selected; the selected time-cycle has no spatial-link leaf. A different group presentation involving vertical links or correlated transport would be required. `three_interval_forest.py` and `forest_certificate.json` verify fourteen additional genuine Penrose support/volume pairs, with up to 301 inserted temporal faces and all three temporal steps present.

## Theorem 2 — volume-uniform exact single-link heat-bath *excess* energy
Fix a retained link \(e\). Let \(m_e\) denote the number of retained plaquettes incident on it. Conditioning on all other links, each incident term can be written \(d(U_eA_{p,e})\) (use trace invariance to handle inverse link orientations). Regard \(A_{p,e}\in SU(2)\) as a unit quaternion and set
\[
h_e=\sum_{p\in R:p\ni e} A_{p,e}^{\rm quaternion},\quad
H_e=\|h_e\|\le m_e,\quad
F_e=m_e-H_e\ge0.
\]
\(F_e\) is the **conditional minimum of the sum of incident plaquette deficits**, not the minimum of the whole lattice action. If \(r(t)=I_2(t)/I_1(t)\), exact SU(2) Haar integration gives
\[
\mathbf E_{\mu_R}\left[\sum_{p\ni e}d(W_p)\mid U_{\ne e}\right]
=m_e-H_e r(\lambda H_e).
\]
For **every** \(\lambda>0\), every exterior configuration, and every ambient volume,
\[
\boxed{0\le\lambda\mathbf E_{\mu_R}\left[\sum_{p\ni e}d(W_p)-F_e\mid U_{\ne e}\right]\le\tfrac32.}
\]
Proof of numerical-free inequality: \(r'(t)=1-r(t)^2-3r(t)/t\). For \(t>3/2\), comparison with \(b(t)=1-3/(2t)\) gives at every potential contact \(r=b\) the strict derivative inequality \(r'-b'=3/(4t^2)>0\). Since \(r(3/2)>0=b(3/2)\), \(r(t)\ge b(t)\) for all \(t>3/2\); the conclusion is trivial for \(0<t\le3/2\). Hence \(t[1-r(t)]\le3/2\). The case \(H_e=0\) is immediate.

### Corollary — precise reduction of the **local** retained-energy inequality
For **any** prescribed retained face set \(A\subset R\), choose a link cover \(L\) meeting every face of \(A\), e.g. all edges of the faces in \(A\), so \(|L|\le4|A|\). With each plaquette deficit nonnegative,
\[
\boxed{\lambda\sum_{p\in A}\mathbf E_{\mu_R}d(W_p)
\le\frac32|L|+\lambda\sum_{e\in L}\mathbf E_{\mu_R} F_e.}
\]
This is an **unconditional volume-independent local inequality**, but includes the unbounded-as-yet staple-frustration expectation. If \(|A|\le c|Q|\) and
\[
\lambda\sum_{e\in L}\mathbf E_{\mu_R} F_e\le C|Q|(1+\log\lambda),
\]
then the requested local retained-plaquette energy inequality follows with constants independent of ambient volume. Unlike the preceding *spatially averaged* theorem, every term is supported near Q. This identifies exactly where further probabilistic work is needed.

**Unconditional free-link subcase.** If every face \(p\in A\) has at least one link \(e_p\) belonging to no other retained face, then its staple count is \(m_{e_p}=1\), so \(F_{e_p}=0\) identically. The unique-link Haar integral is exactly the one-plaquette factor and
\[
\boxed{\lambda\sum_{p\in A}\mathbf E_{\mu_R}d(W_p)\le\tfrac32|A|.}
\]
This is a genuine ambient-uniform **local raw-energy theorem for the exclusive-link class**, but the interior retained plaquettes in the Penrose three-dimensional prism ensembles generally do not have exclusive links.

One cannot delete \(F_e\): if two incident staples are opposite unit quaternions, \(H_e=0\), \(F_e=2\), and the conditional mean of **each** incident plaquette deficit is 1 for all \(\lambda\). The local excess is zero while the raw energy is \(2\lambda\). This counterexample concerns fixed exterior boundary data; it does not rule out the desired bound **after averaging under the actual full Gibbs marginal**.

For a Bianchi-fillable support with a verified noncommutative curvature comparison \(\sum_{q\in Q}d(W_q)\le K\sum_{p\in A}d(W_p)\), Jensen's inequality yields
\[
\frac{Z_{R\cup Q}}{Z_R}\ge\exp[-K\lambda\sum_{p\in A}\mathbf E_{\mu_R}d(W_p)]
\ge\exp[-K\{\tfrac32|L|+\lambda\sum_{e\in L}\mathbf E F_e\}].
\]
This gives a *conditional theorem for fillable Q* once the local staple-frustration estimate is established. For unfillable Q the independent relative Haar coordinates above are available, but the conditional boundary dependence must still be controlled.

## Genuine Penrose audits: 26 supports
Copied the verified direct-Z5 constructor and three-step face-incidence routines, then tested compact and filament supports on radii 5, 8 and 10; 26 support/volume pairs total. All have exactly \(|Q|\) independent relative Haar pivots. For radius 10 compact supports, the longest transformed retained face word is bounded by **16 factors** (the maximum measured number of substituted pivots in a retained quadrilateral is four):

| Spatial rhombi | Inserted \(|Q|\) | Haar pivots | All insertion links | Retained faces touching pivots | Retained faces touching insertion links |
|--:|--:|--:|--:|--:|--:|
| 1 | 8 | 8 | 20 | 14 | 37 |
| 6 | 27 | 27 | 64 | 41 | 89 |
| 16 | 62 | 62 | 142 | 86 | 164 |
| 40 | 145 | 145 | 327 | 195 | 348 |
| 80 | 279 | 279 | 624 | 360 | 619 |
| 160 | 531 | 531 | 1171 | 656 | 1088 |

Roundtrip and mutation tests on random SU(2) quaternions verified the exact word inversion and that changing one Haar coordinate leaves every far Wilson face unchanged (errors <1e-12). Numerical Bessel scans confirm the sharp excess constant \(3/2\) over the tested range; the theorem's proof is analytic and does not depend on these scans. See `verify.py`, `relative_haar_audit.csv`, and `certificate.json`.

## What remains open
1. **The requested local raw-energy estimate** \(\lambda\sum_{p\in N(Q)\cap R}\mathbf E d(W_p)\le C|Q|(1+\log\lambda)\) under arbitrary Penrose exterior marginals. Our exact inequality reduces it to local staple frustration; it does NOT prove a bound on that frustration.
2. **The full arbitrary-support compact-Haar gluing theorem.** An \(O(|Q|)\) chart exists for all Q trivially using original support links, and an independent inserted-face Haar chart exists for Q in steps 0,1, but these do not supply a uniform lower bound for the conditional Gibbs expectation. Three-step-complete Q with a full three-face temporal cycle on some spatial edge may not admit the same face-wise pivot chart.
3. The general large-\(\lambda\) R3 insertion comparison and continuum mass gap.

### Relevant literature (context only, NOT imported as a Penrose theorem)
O. Borisenko, S. Voloshin and M. Faber, *Field strength formulation, lattice Bianchi identities and perturbation theory for non-Abelian models*, Nucl. Phys. B 816 (2009), 399–426, DOI 10.1016/j.nuclphysb.2009.02.008. This work discusses volume-uniform local plaquette concentration in conventional lattices and cites earlier Mack–Petkova work; extension to nonperiodic Penrose rhombus prisms, the stated boundaries, and deleted-face cavities has not been verified here. The proof in this note is self-contained and does not rely on that external claim.
