# PF-I14 — Exact Fibonacci-decorated phason-hull covariance and a conditional gauge-projected link transfer

**Research date:** November 8, 2026. **Primary inputs:** original unpublished source construction authenticated in PF-I9; PF-I10 actual Fibonacci weighted graph and triangular negative control; PF-I11 actual accepted SU(2) rhombus Wilson complexes; PF-I12 transverse four-family commutator support; PF-I13 phason-pairing involution, fixed-word reflection mismatch and matched-versus-swapped heat seams. The dissertation is an **unpublished historical reference**, not a completed field-theory proof. The original source script and raw finite graphs remain privately preserved in Library.

**PF-I14 result:** An exact, explicitly described **extended/decorated phason hull** removes the PF-I13 *fixed Fibonacci scalar word* mismatch by transporting the mechanical-word phase **and its lower/upper boundary convention**. The extension has a height-preserving integer reindexing group and an involutive complement satisfying a semidirect-product relation. On **all eight original finite source complexes**, original and reflected full-window source rhombi, weighted Laplacians, local SU(2) gauge action and the *conditional* PF-I12 non-Abelian transverse action intertwine; two separate completed-window controls agree. An auxiliary **gauge-projected positive SU(2) link transfer** can be defined on the actual source edges after matching phason fibers, rather than independent fictitious faces. **No physical source time, source-derived kinetic scale, global original-theory OS reflection, 4D interacting continuum, uniform mass gap, or gravitational UV finiteness is proved.**

## 1. Exact PF-I14.A — reversibility of the Fibonacci hopping word, including the singular source boundary

Let \(\alpha=\varphi^{-1}=(\sqrt5-1)/2\). The author's actual PF-I10 hopping is the **lower** mechanical word at phase \(\rho=0\):

\[
 s^\downarrow_\rho(k)
 =\lfloor(k+1)\alpha+\rho\rfloor-\lfloor k\alpha+\rho\rfloor\in\{0,1\},\qquad
 t^\downarrow_\rho(k)=
 \begin{cases}1&s^\downarrow_\rho(k)=1,\\\varphi^{-2}&s^\downarrow_\rho(k)=0.\end{cases}
\]

The **upper** word is defined using ceilings instead of floors. Set \(\rho'=-\rho-\alpha\) modulo integers. For *every* integer \(k\), **including discontinuity indices**, one has the exact identity

\[
 \boxed{s^\downarrow_\rho(k)=s^\uparrow_{-\rho-\alpha}(-k),\qquad
        s^\uparrow_\rho(k)=s^\downarrow_{-\rho-\alpha}(-k).}
\]

**Proof:** The first right-hand side is
\[
 \lceil-k\alpha-\rho\rceil-
 \lceil-(k+1)\alpha-\rho\rceil
 =-\lfloor k\alpha+\rho\rfloor+\lfloor(k+1)\alpha+\rho\rfloor.
\]
The second follows by replacing ceilings/floors symmetrically. **QED.** This is an identity of Sturmian mechanical words, not an unverified asymptotic claim.

The image of the author's default \((\rho=0,\text{lower})\) is **\((\rho'=-\alpha,\text{upper})\)**. If one reflects the phase but mistakenly retains the *lower* convention at \(-\alpha\), the infinite word differs at **exactly** source indices \(k=-1,0\). This two-index defect occurs because the source's \(\rho=0\) is singular for the lower/upper coding. Keeping the *untransformed* original word at both phasons causes much more widespread mismatches. The checker uses **exact integer square roots in \(\mathbb Q(\sqrt5)\)** (arbitrary-precision integers and rational intercepts) to avoid rounding at the discontinuity; \(200{,}010\) indexed reflection checks and a Decimal independent check pass.

**Scope:** Introducing a reflected *Sturmian boundary convention* is a mathematically necessary and sufficient way to construct an exact reflection-covariant **scalar hopping family**. The actual source has only its lower word at zero phase; this extension **does not claim** the author introduced five physical mechanical-word phases, that a phason is physical time, or that the scalar hopping is an SU(2) gauge coupling.

## 2. Exact PF-I14.B — a height-preserving decorated hull and its semidirect reflection

Let the original accepted source integer labels be \(m\in\mathbb Z^5\) at height \(h=\sum m_j\in\{1,2,3,4\}\), with perpendicular-window membership \(P_\perp(m+\gamma)\in\operatorname{int}W_h\), \(\sum\gamma_j=0\). Define **five** mechanical-word phases \(\boldsymbol\rho=(\rho_0,\ldots,\rho_4)\in(\mathbb R/\mathbb Z)^5\) and five lower/upper boundary decisions \(\boldsymbol\eta\). The source point is \(\rho_j=0\), all lower. This is an **auxiliary mathematical enlargement** of the source parameter space.

For any height-preserving integer relabeling \(a\in\Lambda_0=\{a\in\mathbb Z^5:\sum a_j=0\}\), set
\[
 T_a:(m,\gamma,\rho_j,\eta_j)\mapsto
 (m+a,\gamma-a,\rho_j-a_j\alpha,\eta_j).
\]
All accepted windows and genuine face triangles are unchanged because \((m+a)+(\gamma-a)=m+\gamma\); source height is unchanged. Source edge lower level becomes \(k+a_j\), and the transformation of \(\rho_j\) guarantees
\[s_{\rho_j-a_j\alpha}^{\eta_j}(k+a_j)=s_{\rho_j}^{\eta_j}(k).\]
The physical projection is shifted by \(P_\parallel a\); a **finite crop must be translated with it**. This is covariance among labeled/cropped hull members, **not** an assertion that the author's original fixed-center finite source selection is invariant.

Extend PF-I13's exact window complement by reflecting the decoration:
\[
 R:(m,\gamma,\rho_j,\eta_j)\mapsto
 (\mathbf1-m,-\gamma,-\rho_j-\alpha,\overline{\eta_j}),
\]
where upper/lower decisions are exchanged. The exact word identity and four hypersimplex/face-triangle identities imply that the **weighted accepted 2-complex** maps bijectively to its reflected counterpart, with the source basis edge \((m,m+e_j)\) mapping to the reversed positive edge \((\mathbf1-m-e_j,\mathbf1-m)\). Direct substitution yields
\[
 \boxed{R^2=1,\qquad T_aT_b=T_{a+b},\qquad R T_a R=T_{-a}.}
\]
Therefore a *mathematical* \(\Lambda_0\rtimes\mathbb Z_2\) action exists on this decorated family. The five separate phases are needed for closure under all such relabelings via the natural phase-transport rule: a shared \(\rho\) would require \((a_i-a_j)\alpha\in\mathbb Z\) for every \(i,j\), forcing all \(a_j\) equal; with \(\sum a_j=0\), only \(a=0\) remains because \(\alpha\) is irrational. The source's equal-phase slice is **not itself closed** under the full \(\Lambda_0\) action.

**Caution:** This is a group action on **source-labeled, independently decorated hull data**, not a claim that \(\Lambda_0\) is physical spacetime translation, that the finite cutoff is equivariant without transport, or that its \(\mathbb Z_2\) generator defines Euclidean time reflection. PF-I13 already established that the induced nontrivial physical/perpendicular linear map is \(-I_4\), **not** a single-real-axis hyperplane time reflection.

## 3. Exact PF-I14.C — finite scalar and SU(2) gauge covariance across paired phasons

Let \(C_\gamma=(V,E,F)\) be any finite selected source subcomplex whose faces are verified by the actual two-fixed-coordinate window triangles; let \(RC_\gamma=C_{-\gamma}\) denote its **specifically reflected finite image**, **not** a separately re-selected source crop. The map \(v\mapsto\mathbf1-v\) is a vertex bijection; \((v,v+e_j)\mapsto(\mathbf1-v-e_j,\mathbf1-v)\) is the corresponding oriented-positive edge reversal; source face orientation is preserved after cyclic rebasing. The completed and original retained populations are treated separately throughout.

On edge \(e=(v,v+e_j)\), let \(w_e=t_{\rho_j}^{\eta_j}(v_j)\). Under the decorated reflection, every target edge has **exactly the same weight**, so with the vertex permutation \(P_R\),
\[
 \boxed{L_{RC,R\rho,R\eta}=P_R L_{C,\rho,\eta}P_R^{-1}.}
\]
This identity is **exact for the covariantly extended scalar weighted-strength Laplacian**, hence every finite spectral functional is the same on each properly paired reflected fiber. It does not assert invariance when one holds the original fixed hopping word unchanged at both phasons; PF-I13's mismatch remains valid for that different comparison.

For source positive-basis oriented SU(2) links, define \((RU)_{(\mathbf1-v-e_j,\mathbf1-v)}=U_{(v,v+e_j)}^{-1}\), with \((Rg)_{\mathbf1-v}=g_v\). The transformed links obey the exact gauge-group intertwining identity \(R(g\cdot U)=(Rg)\cdot(RU)\). Each face holonomy is conjugate to its reflected face's holonomy at the relocated basepoint, hence individual half-traces agree. Distinct transverse pairs of four-family rhombi and their common vertex are carried bijectively by \(R\); their commutator half-traces agree too.

Consequently **any finite Wilson/commutator action with explicitly transported couplings** (including the illustrative positive nonconstant face coupling \(\kappa_f=\beta[1+0.17w_jw_k]\) and the PF-I12 pair penalty with test coefficient \(\lambda\)) is related by an SU(2) Haar-measure-preserving link bijection:
\[
 \boxed{S_{RC}(RU;R\kappa,R\lambda)=S_C(U;\kappa,\lambda),\qquad
 Z_{RC}(R\kappa,R\lambda)=Z_C(\kappa,\lambda).}
\]
The link map includes orientation inversion, and Haar measure is inversion-invariant. This equality is a **fiber-to-fiber isomorphism**; it does not supply a physical time ordering, positive-time subalgebra, reflection-positive kernel, or a nontrivial continuum measure. The use of PF-I10 scalar weights to define an optional face coupling is **a covariance stress test**, not a source-approved SU(2) action.

### Independently checked eight original source systems

| Source `Ngrid` | Original vertices | Original basis edges | Source faces | Fixed-word edge-type mismatches under geometric inversion | Remaining if one changes phase but retains lower convention | Correct decorated reflection mismatches |
|---:|---:|---:|---:|---:|---:|---:|
| 7 | 1,550 | 3,017 | 1,468 | 1,864 | 488 | **0** |
| 10 | 3,042 | 5,927 | 2,886 | 3,872 | 690 | **0** |
| 12 | 4,324 | 8,468 | 4,145 | 5,507 | 830 | **0** |
| 15 | 6,980 | 13,779 | 6,800 | 9,562 | 1,030 | **0** |
| 18 | 9,950 | 19,593 | 9,646 | 13,780 | 1,240 | **0** |
| 20 | 12,207 | 24,091 | 11,879 | 17,194 | 1,391 | **0** |
| 23 | 16,435 | 32,582 | 16,138 | 23,185 | 1,600 | **0** |
| 25 | 19,260 | 38,139 | 18,874 | 27,350 | 1,714 | **0** |

For **all eight** original source systems, the reflected finite labels, basis edges and actual rhombi form an identical incidence complex by permutation, the source edge weights and illustrative nonconstant face weights transport with **zero** type mismatches, link gauge transformations intertwine, Wilson action matches numerically to floating precision, and the non-Abelian PF-I12 transverse pair penalty matches **pair by pair** (max discrepancy about \(4.44\times10^{-16}\)). The complete eight-size numerical record retains the PF-I11 source SHA-256 fingerprints; no original source vertex selection was overwritten. Exact \(\Lambda_0\) source relabeling was additionally tested at `Ngrid=7` and `25` using \(a=(2,-1,0,-1,0)\).

Two separately reconstructed full-window incident-star **completed** core controls (`Ngrid=7`, `25`) also satisfy exact decorated reflection; their sizes are 1,432/2,761/1,330 and 19,256/38,135/18,880 (vertices/edges/faces) respectively, and they match PF-I11's **different** completed-core reference hashes. Their fixed-word mismatch counts (1,666/27,372) differ from the original source counts: this is an expected boundary-selection distinction, not a source replacement.

## 4. PF-I14.D — positive **gauge-projected** finite link gluing on the actual source graph, conditionally

PF-I13 established an auxiliary matched positive heat seam for *abstract independent face variables*. PF-I14 moves the constructive comparison to **actual SU(2) oriented links on the accepted source complex**, including their local vertex gauge symmetry. This is still an **externally supplied kinetic/doubled construction**, not physical evolution derived from the source.

For a finite actual source graph \(C\), put \(G=SU(2)\), \(\mathcal H_C=L^2(G^E,dU)\), and let \(\mathcal G_C=G^V\) act on links by \((g\cdot U)_{vw}=g_vU_{vw}g_w^{-1}\). Let
\[
 P_C=\int_{\mathcal G_C}\Gamma(g)\,dg
\]
be its **orthogonal Haar gauge projector**. For arbitrarily chosen positive edge parameters \(t_e>0\), define the heat operator
\[
 H_{\boldsymbol t}=\bigotimes_{e\in E}\exp(-t_eC_e),
\]
where \(C_e\) is the bi-invariant SU(2) Casimir on the actual source link. Every \(\exp(-t_eC_e)\) is self-adjoint, compact/trace-class, **positive as an operator**, and has a strictly positive smooth SU(2) heat kernel. The product commutes with all local vertex gauge transformations. For any finite **gauge-invariant** Wilson/transverse within-side action \(S_+(U)\), let \(w(U)=e^{-S_+(U)}>0\) and \(M_w\) denote multiplication. Then
\[
 \boxed{T_C=P_CM_w H_{\boldsymbol t}M_wP_C\succeq0.}
\]
**Proof:** \(P_C\) is self-adjoint idempotent and \(H_{\boldsymbol t}\succeq0\); for any \(F\),
\[
 \langle F,T_CF\rangle
 =\langle M_wP_CF,H_{\boldsymbol t}M_wP_CF\rangle\ge0.
\]
Since all \(t_e>0\), the finite product heat kernel is strictly positive and smooth; gauge averaging preserves strict pointwise positivity. On the **gauge-invariant** subspace, this compact positivity-improving operator has a simple isolated largest eigenvalue (standard compact positive-kernel theorem), hence a finite **auxiliary** top-eigenvalue isolation. No estimate is uniform as source graph size grows or as the unknown physical scale varies. **QED.**

After the exact PF-I14.C decorated \(\Theta\) identifies the source phason \((\gamma,\rho,\eta)\) graph and its reflected \((-\gamma,-\rho-\alpha,\bar\eta)\) graph, \(T_C\) defines a **conditional matched two-hull-fiber positive gluing** on the actual source link Hilbert space. The corresponding kernel on *one identified fiber* can be written
\[
 K_C^{\mathrm{GI}}(U,V)=w(U)w(V)\int_{G^V}\prod_{e=(a,b)}
 K_{t_e}\!\left(U_e\left(g_aV_eg_b^{-1}\right)^{-1}\right)\,dg,
\]
with the target fiber first pulled back through the reflected edge orientation. Gauge averaging makes it invariant under independent gauge-frame changes in its two link arguments; the original, **unprojected** heat seam is only invariant under *matched* vertex frames. Thus the projection resolves a mathematical gauge-frame matching issue of PF-I13's auxiliary construction, **not** the missing physical time or kinetic normalization.

A deterministic local test uses **two genuine transverse rhombi from the original `Ngrid=7` source**, spanning **7 accepted vertices and 8 actual links**, with genuine non-Abelian commutator coupling \(\lambda=0.4\), Wilson \(\beta=0.3\), and optional heat parameter \(t=0.85\). Both the unprojected link-kernel Gram and a finite two-sided *gauge-averaged* Gram are nonnegative; a mismatched independent-half gauge transformation changes the unprojected seam, confirming the need for gauge projection or matching. The **global positivity theorem is analytic**; a finite Monte Carlo gauge average is only a diagnostic, not the proof.

**Crucial physical boundary:** A positive compact transfer on each artificially doubled finite graph does not select a physical temporal half, a source-defined \(t_e\), a renormalization group law, a nontrivial continuum Hilbert-space limit, or a positive continuum mass gap. Nor does source-hull covariance alone imply Osterwalder–Schrader reflection positivity of any original undoubled gauge path measure.

## 5. What PF-I14 does and does not resolve

| Obligation | PF-I14 status |
|---|---|
| Exact reversal of original source Fibonacci hopping with singular boundary convention | **PROVED, all integer indices** |
| Height-preserving decorated-hull relabeling and \(\Lambda_0\rtimes\mathbb Z_2\) action | **PROVED, exact source-independent identity** |
| Finite weighted graph, SU(2) gauge, Wilson and commutator covariance across paired phasons | **PROVED, checked on all eight original source complexes** |
| Separately selected complete-window core controls | **CHECKED at `Ngrid=7,25`** |
| Global gauge-projected positive heat gluing on actual finite source link space | **PROVED conditionally, auxiliary \(t_e>0\) and doubled matched phason fibers** |
| Finite auxiliary transfer isolation of leading eigenvalue | **PROVED conditionally, no uniform estimate** |
| A source-approved physical meaning for extra \(\rho_j\)/upper-lower decorations | **OPEN** |
| A source-derived physical time/reflection, positive-time observable algebra and physical kinetic coupling | **OPEN** |
| Uniform nontrivial interacting Yang–Mills continuum existence and positive physical mass gap | **OPEN** |
| Gravitational ultraviolet finiteness | **OPEN** |

## 6. Next proof contract: PF-I15

**PF-I15-SOURCE-INTRINSIC-POSITIVE-TIME-AND-UNIFORM-DYNAMICS.** We now possess a precise *decorated hull* allowing full source hopping/gauge covariance and a gauge-projected auxiliary positive link transfer on genuine rhombi. The next decisive obligation is to establish whether the mathematical hull parameters are physically justified, to define an intrinsic positive-time algebra/reflection or defensible constructive alternative, to derive physical kinetic scales (instead of selecting \(t_e\) arbitrarily), and to control genuine gauge-invariant Wilson/commutator correlations and a nontrivial continuum/gap **uniformly over a source-justified finite-volume/phason exhaustion**. Do not impose cubic physical spacetime, equate scalar spectral-zeta with quantum gauge spectra, or promote a finite auxiliary transfer isolation to the Yang–Mills mass gap.

## 7. Source, tests and evidence provenance

The original unpublished source script remains sha256 `86ce0bf4e0688899a2f1c9dba980cb6d996c3fef59889807ee8376d6e62369da` and is **not** committed to GitHub. The original source geometry and three original finite graph snapshots are held privately in Library, with the full all-eight source reconstruction reproducible from the exact script. The derived verifier `verify_pf_i14_decorated_hull.py` is independent of de Bruijn construction, using actual source accepted labels and window face tests. `verify_pf_i14_gauge_projected_gluing.py` supplies the optional actual-link gauge projector and source-local SU(2) heat Gram test. `verify_pf_i14_completed_core.py` rebuilds **two separate** completed-window controls and verifies their PF-I11 SHA fingerprints. Exact irrational arithmetic is performed in \(\mathbb Q(\sqrt5)\) with integer square roots. All large source link/face calculations use the original private snapshots or authenticated unpublished script; the public tests skip source-dependent cases when original bytes are absent. The archive manifest pins every file and raw input; detailed original source snapshots/manuscripts are **Library only**, and derived aggregate evidence and mathematical report can be published to the research repository.
