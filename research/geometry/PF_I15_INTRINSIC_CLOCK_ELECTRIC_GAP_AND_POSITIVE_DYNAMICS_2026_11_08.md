# PF-I15 — Intrinsic clock selection, source-graph electric Casimir and finite interacting dynamics

**Research checkpoint:** 2026-11-08. **Original sources:** unpublished 2026 dissertation synthesis, `Sharpe_Paper4_J_Operator_Hidden_Domain_Revised.tex` (the J/helix and explicit *Algebraic versus dynamical content* remark), preserved original author cut-and-project source SHA-256 `86ce0bf4e0688899a2f1c9dba980cb6d996c3fef59889807ee8376d6e62369da`, PF-I9 direct accepted-window faces, PF-I11 actual source SU(2) rhombus complexes, and PF-I14 decorated Fibonacci-phason-hull covariance. **The unpublished drafts are references, not certified physical postulates.** Geometry is intrinsically \(\mathbb Z^5\to E_\parallel\oplus E_\perp\oplus\mathbb R\), without a prescribed cubic 3+1 structure.

**Result status:** exact restricted clock nonselection; exact gauge-invariant **pure-electric** spectrum/gap, including a weighted cycle formula; an independently evaluated one-rhombus nonzero Wilson potential; an exact nonunique decorated-phase invariant-measure construction; and a precise nonuniform interacting perturbation obstruction. **No source-derived kinetic energy, physical time, unique invariant physical measure, original-theory global OS reconstruction, interacting thermodynamic/continuum limit, physical Yang–Mills mass gap, or gravitational UV proof.** All physical proof gates remain **OPEN**.

## 1. Source discipline: the proposed J-helical time is kinematic in the draft's own terms

The revised unpublished J paper defines \(z_1=\sum_jm_j\omega^j\), \(z_2=\sum_jm_j\omega^{2j}\), \(\omega=e^{2\pi i/5}\), and \(J|_{E_{\parallel}}\), \(J|_{E_{\perp}}\) as quarter-turn rotations. It *proposes* \(\operatorname{Im}(z_2)=ict\), and traces prescribed helical observer paths \(z_2(\tau)=A e^{2\pi i p\tau}\), with Fibonacci-related pitches. Crucially, its *Algebraic versus dynamical content* remark says that no field equation is invoked and the dynamical question remains open. We preserve the proposal as a source proposal and this caveat as a source admission. PF-I12 also noted that bare \(C_5\)-equivariance does not by itself uniquely fix all complex-structure orientation signs.

### Exact PF-I15.A — no nontrivial invariant *additive* real clock on the height-zero source translations

Let \(\Lambda_0=\{a\in\mathbb Z^5:\sum_{j=0}^4a_j=0\}\), with \(\sigma\) cyclically permuting the five indices. If \(\tau:\Lambda_0\to\mathbb R\) is an additive homomorphism and \(\tau(\sigma a)=\tau(a)\), then for every \(a\in\Lambda_0\),
\[
5\tau(a)=\tau\left(\sum_{r=0}^4\sigma^r a\right)
=\tau\bigl((\sum_ja_j)\mathbf1\bigr)=0.
\]
**Therefore \(\tau=0\).** Equivalently, every \(C_5\)-invariant real linear functional on \(\mathbb R^5\) is \(m\mapsto c\sum_jm_j\); the actual accepted source graph has height \(h=1,2,3,4\), so that functional is **bounded** there. Also \(P_\perp(m+\gamma)\) lies in a bounded acceptance window. In particular, the scalar candidate \(\operatorname{Im}z_2\) is neither invariant under the full cyclic rotation nor an unbounded monotone scalar time coordinate on accepted vertices. A winding-count lift, noninvariant direction choice, hull flow, nonlinear clock, symmetry reduction or physical observer is **not excluded**, but would have to be defined as extra structure.

The elementary quarter-turn \(J^2=-I\) gives a nontrivial rotation \(e^{\theta J}\), which is **orthogonal/unitary**, not a positive self-adjoint heat evolution \(e^{-tH}\) with \(H\ge0\) for generic real \(\theta\). A positive orthogonal operator must equal \(I\). A Euclidean-to-Lorentzian identification can be proposed separately, but neither algebraic rotation nor observer sampling constructs a positive-time field algebra or a Hamiltonian. This is a *restricted logical nonimplication*, not a proof that the user’s proposed physical time cannot emerge.

## 2. Exact PF-I15.B — source gauge-invariant pure-electric spectral gap on any finite accepted graph

On the source's **actual** finite edge graph \(G=(V,E)\), define the gauge-invariant Hilbert space
\[
\mathcal H_G=L^2(SU(2)^E,\otimes_e dU_e)^{SU(2)^V},
\qquad H_{\boldsymbol\varepsilon}=\sum_{e\in E}\varepsilon_e C_e,
\quad \varepsilon_e>0,
\]
where \(C_e=-\Delta_{SU(2),e}\) is the bi-invariant Laplace/Casimir on the link, with \(C_e\chi_{j_e}=j_e(j_e+1)\chi_{j_e}\). This Hamiltonian is an **auxiliary dynamical choice**, not an operator derived from the original scalar spectral zeta or the J geometry.

**Theorem (exact weighted electric gap).** If \(G\) is a finite simple graph with at least one simple cycle, the first positive eigenvalue of \(H_{\boldsymbol\varepsilon}\) restricted to \(\mathcal H_G\) is
\[
\boxed{\Delta_{\rm el}(G,\boldsymbol\varepsilon)
=\frac34\min_{\ell\text{ simple cycle of }G}\sum_{e\in\ell}\varepsilon_e.}
\]
**Proof.** The Peter–Weyl spin-network basis decomposes the gauge-invariant Hilbert space into edge spins \(j_e\in\{0,\frac12,1,\ldots\}\), with invariant intertwiners at vertices. If a support vertex has exactly one occupied \(j_e>0\), no invariant intertwiner exists; every occupied support vertex has degree at least two. A finite nonempty supported subgraph therefore contains a simple cycle. Each occupied edge costs \(\varepsilon_e j_e(j_e+1)\ge(3/4)\varepsilon_e\), so every nonconstant gauge-invariant eigenstate has energy at least the right-hand side. Conversely take the normalized fundamental-character Wilson loop \(\chi_{1/2}(U_\ell)\) on a minimum-weight simple cycle, with all other spins trivial. It is gauge invariant, nonconstant, orthogonal to the constant vacuum and an exact eigenfunction with energy \((3/4)\sum_{e\in\ell}\varepsilon_e\), attaining the bound. **QED.** Disconnected graphs do not alter the argument: tree-only components carry no nonconstant gauge-invariant functions. A forest-only graph has a 1D gauge-invariant Hilbert space and **no nontrivial first excitation**, not a meaningful positive gap.

**Source consequence.** In every source original finite graph, occupied basis edges change \(h=\sum m_j\) by \(\pm1\), so \(G\) is bipartite; there are no triangles or shorter odd cycles. The original PF-I11 genuine rhombi give simple **four-edge cycles** at all eight published sizes. With \(\varepsilon_e=\varepsilon\),
\[
\boxed{\Delta_{\rm el}(G_N,\varepsilon)=3\varepsilon \text{ for all eight source sizes}.}
\]
This is a **genuinely volume-uniform pure-electric reference** when \(\varepsilon\) is independently fixed. It is not a uniform interacting source Yang–Mills gap in physical mass units.

### A second exact source-weighted reference, and its ambiguity

The source Fibonacci **scalar** hopping has two positive values \(w_e\in\{1,\varphi^{-2}\}\). If (an optional choice) one sets electric coefficients \(\varepsilon_e=w_e\), every simple cycle costs at least four weak edges, giving \(\Delta\ge3\varphi^{-2}\). Every one of the eight unchanged source complexes contains accepted genuine four-edge rhombi whose **four** scalar hopping values equal \(\varphi^{-2}\) (full independent source replay below), saturating the bound:
\[
\boxed{\Delta_{\rm el}(G_N,\varepsilon_e=w_e)=3\varphi^{-2}=1.1458980337503155\ldots.}
\]
Likewise \(\varepsilon_e=w_e^{-1}\) gives \(\Delta=3\) because all eight source graphs also contain four-edge all-strong rhombi. All three choices are allowed positive auxiliary electric Hamiltonians on the same intrinsic graph, with **different spectra**. The dissertation's scalar Fibonacci hopping does **not** by itself mandate any of them as the physical gauge-electric coefficient.

### Original-source eight-size certificates

| Source Ngrid | V | E | Accepted rhombus faces | All-weak faces | All-strong faces | Exact uniform electric gap | Exact electric gap if \(\varepsilon_e=w_e\) |
|--:|--:|--:|--:|--:|--:|--:|--:|
| 7 | 1,550 | 3,017 | 1,468 | 223 | 543 | 3 | 1.145898034 |
| 10 | 3,042 | 5,927 | 2,886 | 428 | 1,096 | 3 | 1.145898034 |
| 12 | 4,324 | 8,468 | 4,145 | 581 | 1,626 | 3 | 1.145898034 |
| 15 | 6,980 | 13,779 | 6,800 | 984 | 2,576 | 3 | 1.145898034 |
| 18 | 9,950 | 19,593 | 9,646 | 1,410 | 3,680 | 3 | 1.145898034 |
| 20 | 12,207 | 24,091 | 11,879 | 1,782 | 4,487 | 3 | 1.145898034 |
| 23 | 16,435 | 32,582 | 16,138 | 2,328 | 6,204 | 3 | 1.145898034 |
| 25 | 19,260 | 38,139 | 18,874 | 2,732 | 7,234 | 3 | 1.145898034 |

Original source integer vertex and face SHA-256 fingerprints match the preserved PF-I11 evidence at **all eight** sizes. The proof uses **no periodic/cubic surrogate**, no new 3+1 coordinate system, and no arbitrary face closure. The separate completed-window controls remain separate datasets and are not silently substituted.

## 3. Exact PF-I15.C — a nonzero Wilson potential yields a strictly gapped finite quantum control

For finite accepted \(G\), consider a **specified** auxiliary magnetic/commutator Hamiltonian on the same gauge-invariant Hilbert space:
\[
H_G=\varepsilon\sum_e C_e + \sum_f\kappa_f(1-X_f)
+\sum_{(f,g)\in\mathcal T}\lambda_{fg} Q_{fg},\qquad
X_f=\tfrac12\operatorname{Tr}U_f,\quad Q_{fg}=1-\tfrac12\operatorname{Tr}[U_f^v,U_g^v],
\]
with \(\varepsilon>0\), \(\kappa_f,\lambda_{fg}\ge0\). The terms are gauge invariant and are bounded nonnegative continuous multiplication operators for **finite** complex. The elliptic Laplace operator \(\sum_eC_e\) on compact connected \(SU(2)^E\) has compact resolvent; adding bounded real multiplication preserves this. Its heat semigroup has a strictly positive integral kernel (Brownian motion/Feynman–Kac with bounded potential). The gauge-invariant subspace is preserved and its restricted semigroup is positivity improving. By the compact positivity-improving principal-eigenfunction theorem, \(H_G\) has a **simple ground state** in the gauge-invariant subspace and an **isolated strictly positive finite gap** whenever the source graph has a nonconstant gauge-invariant sector.

**Critical scope:** This constructs positive **auxiliary** quantum dynamics *after* inserting \(\varepsilon\), potential couplings and a semigroup parameter. It is **not** a source-derived physical positive-time field algebra, a four-dimensional continuum limit, or a lower bound on the gap **uniform** as \(G\) and the regulator vary.

### An explicit interacting quantum spectral calculation on one original-source rhombus

Gauge fixing the three tree edges of a genuine four-edge rhombus leaves one conjugacy class of \(SU(2)\). The orthonormal class-character basis \(\chi_j\), \(j=0,\tfrac12,1,\ldots\), diagonalizes the electric operator; the fusion identity \(\chi_{1/2}\chi_j=\chi_{j+1/2}+\chi_{j-1/2}\) (drop negative spins) makes the interacting matrix **exactly tridiagonal**:
\[
\boxed{
\langle\chi_j,H\chi_{j'}\rangle
=[4\varepsilon j(j+1)+\kappa]\delta_{jj'}
-\frac\kappa2\bigl(\delta_{j',j+1/2}+\delta_{j',j-1/2}\bigr).}
\]
With **illustrative** \(\varepsilon=1,\kappa=0.71\), Jacobi truncations at 8,12,20,40 characters yield identical gap to at least nine decimals, \(\Delta=3.0580857125308603\). The independent 600-node class-Haar angular quadrature \((2/\pi)\sin^2\theta\,d\theta\) verifies both the character orthogonality and the magnetic potential matrix to approximately \(2\times10^{-14}\). At \(\kappa=0\), the exact reference spectrum begins \(0,3,8,15,24,\ldots\). This is a fully interacting **finite one-plaquette** model, not a nontrivial 4D multi-plaquette continuum proof.

## 4. PF-I15.D — why a finite gap does not supply the missing physical normalization or interacting uniform bound

### Time-step/energy-scale nonselection

With \(\varepsilon_e=1\), the explicitly added pure-electric transfer \(T_t=e^{-t\sum_e C_e}\) has, on every finite source graph,
\[
\lambda_0=1,\qquad\lambda_1=e^{-3t},\qquad
1-\lambda_1=1-e^{-3t}.
\]
If one chooses \(t_N=1/|V_N|\), a perfectly valid but **external** convention, the dimensionless transfer-step eigenvalue separation tends to zero as \(N\to\infty\), even though the Casimir **energy** gap is 3 when measured in these chosen dimensionless units. Conversely with \(H_{\varepsilon_N}=\varepsilon_N\sum C_e\), the exact energy gap is \(3\varepsilon_N\to0\) if the unconstrained kinetic scale \(\varepsilon_N\to0\). Thus the graph's existence and the PF-I14 positive transfer do **not** select a physical mass or a source-determined volume-uniform energy normalization. This is an ambiguity/under-determination result, **not evidence that a correctly normalized physical continuum theory must be gapless**.

### Why the elementary bounded-potential perturbation bound is nonuniform

For the gauge-invariant finite Wilson Hamiltonian with \(\lambda=0\), uniform \(\varepsilon>0\), nonnegative face couplings \(\kappa_f\), and \(F\) accepted source plaquettes, the min–max principle gives \(E_1(H)\ge3\varepsilon\), since \(V\ge0\). The constant gauge-invariant Haar trial state gives \(E_0(H)\le\sum_f\kappa_f\), because each individual plaquette half-trace has Haar mean zero. Hence
\[
\boxed{\Delta(H)=E_1-E_0\ge 3\varepsilon-\sum_f\kappa_f.}
\]
For uniform fixed \(\kappa>0\), \(\sum_f\kappa_f=\kappa F\) grows with volume. At illustrative \(\varepsilon=1,\kappa=10^{-3}\), this lower bound is **1.532** at source grid7 (1,468 faces), but **−15.874** at source grid25 (18,874 faces), where it is vacuous. This does **not** mean the actual quantum gap is negative or zero: it shows why a naive global operator-norm/supremum perturbation argument cannot close a uniform interacting gap at fixed per-face coupling. A local dressed functional estimate/cluster or other uniform mechanism is required.

## 5. Exact PF-I15.E — auxiliary decorated-hull symmetry does not select a unique invariant phase measure

PF-I14 enlarged the source's **auxiliary mathematical** Fibonacci word backgrounds to five phases \(\rho_j\in\mathbb R/\mathbb Z\). On \(T^5\), zero-height relabeling acts as \(\rho\mapsto\rho-\alpha a\) with \(\sum a_j=0\), while decorated reflection acts as \(\rho\mapsto-\rho-\alpha\mathbf1\), with simultaneous lower/upper flag flip.

The total phase \(s=\sum_j\rho_j\pmod1\) is invariant under every relabeling but transforms under reflection by \(s\mapsto-s-5\alpha\). The irrational translations generated by \(\alpha(e_i-e_4)\) for \(i=0,1,2,3\) are dense in each \(T^4\) fiber of fixed \(s\). Hence any translation-invariant probability on the phase torus is a mixture of conditional Haar measures on these fibers; reflection invariance **only** requires the marginal on \(s\) to be symmetric under the displayed involution (with a corresponding symmetric lower/upper flag distribution).

For example, both the full Haar measure on \(T^5\) and the equal mixture of Haar probabilities on the two distinct fibers \(s=0\) and \(s=-5\alpha\) are invariant under these auxiliary symmetries (take independent fair lower/upper flags). They are **not equal**: the former has Fourier observable \(\mathbb E e^{2\pi is}=0\), while the latter has \(\mathbb E e^{2\pi is}=\frac12(1+e^{-10\pi i\alpha})\), of modulus approximately **0.960144597**.

This is a theorem of the **auxiliary phase fibers**, not a physical invariant measure on the entire geometric/gauge-field hull. It proves that the PF-I14 covariance group by itself does **not** uniquely select a phase distribution or physical vacuum. Additional source dynamics/measure-selection conditions are necessary.

## 6. Completed tests, exact status, and next acceptance gate

The reproducible verifier produces per-size source SHA-checked vertices/edges/faces, source height histograms, the number of all-weak/all-strong actual rhombi, exact electric gaps for three different positive kinetic prescriptions, the illustrative transfer-step scaling and the elementary magnetic bound. The exact one-rhombus Jacobi matrix is checked against independent class-Haar quadrature. The PF-I14 source identity is retained, and source original cropped graphs are **not** replaced by completed-window cores. The full private source replay passes **14 regression tests**; the public source-free suite passes **13** with **one deliberate private-original-script skip**.

**New theorem inventory:** (A) restricted invariant additive-clock no-go and J/heat distinction; (B) exact weighted SU(2) spin-network min-cycle gap with source pure-electric reference \(3\varepsilon\) and optional source-hopping-weighted reference \(3\varphi^{-2}\); (C) existence, uniqueness and strict positive finite gap for any **externally specified** finite SU(2) electric+bounded Wilson/commutator Hamiltonian; (D) exactly soluble one-rhombus interacting Jacobi control; (E) conditional time-scale/volume uniformity under-determination and the extensive-norm perturbation obstruction; (F) nonuniqueness of auxiliary decorated-word invariant phase measures. **None** proves physical continuum Yang–Mills existence or mass gap.

**Next proof objective, PF-I16:** Derive a physically justified time/electric generator and kinetic scale from the original two-sector construction or **falsify** a specific source proposal; choose a source-invariant decorated phason/gauge measure or a justified superselection/hull dynamics; formulate an interacting gauge-invariant infinite-volume limit with compatible reflection/positive-time field algebra or constructive alternative; replace the vacuous \(3\varepsilon-\kappa F\) inequality by an explicitly **local, uniform** connected-observable, functional-inequality or dressed-state gap estimate. No predefined cubic 3+1 background permitted. **All original PF-G0/P0–P5 physical continuum proof gates remain OPEN.**

**Reproducibility:** `verify_pf_i15_intrinsic_time_and_electric_gap.py`, `test_pf_i15_intrinsic_time_and_electric_gap.py`, `PF_I15_SOURCE_EIGHT_SIZE_ELECTRIC_GAP_EVIDENCE.json`, `PF_I15_PUBLIC_TEST_LOG.txt`, `PF_I15_PRIVATE_TEST_LOG.txt`, private original source+PF-I11 reference and pinned `PF_I15_SHA256_MANIFEST_2026_11_08.json` are preserved as a complete Library ZIP. The public repository carries only derived proof, source-independent checker/test and aggregate evidence; original unpublished manuscript/source remains private.
