# The Singular Boundary: R3 neutral-sector and R2 spatial-continuum proof audit

**Date:** 26 October 2026  
**System:** pure SU(2) gauge theory in **2+1 Euclidean dimensions**; spatial rhombic Penrose gauge complexes, not a proof of four-dimensional Yang–Mills.  
**Method:** exact character/spectral algebra, an explicit counterexample inside the Wilson Hamiltonian class, and deterministic homogenization of the geometric Wilson weights. No new Monte Carlo.

## Executive assessment

* **R3 is not closed.** There is no demonstrated arbitrary-magnetic-coupling, volume- and cutoff-uniform neutral Wilson-loop infrared projection estimate. The exact non-diagonal character insertion means that multiplication of isolated temporal-link Bessel factors is not a valid induction for the physical interacting spectrum. The energy spectrum is *unchanged in physical units* by exact temporal blocking. An exact Wilson-model rescaling counterexample shows that a universal unnormalized spectral-weight bound cannot hold across all positive electric scales.
* **R2 has a new proved geometric portion.** For the weighted geometric action supplied in `penrose_2p1_study.py`, fivefold orbit symmetry forces its **quadratic temporal curvature tensor** to be isotropic, with *exactly the matching spatial coefficient*. Penrose unique ergodicity yields the corresponding macroscopic classical quadratic consistency for van Hove exhaustions with scale-independent geometry. This does **not** imply quantum continuum construction, OS/Wightman reconstruction, or a uniform physical mass gap.
* **R2 has the earlier proved fixed-spatial-complex temporal continuum semigroup limit**, conditional on actual Wilson-factorization. The full simultaneous spatial continuum and boundary-uniform spectral control remain open.

## I. Gauge Hamiltonian and conventions

For a finite oriented spatial gauge complex \(G=(V,E,F)\), set
\[
\mathcal H_G=L^2(SU(2)^E,dU)^{SU(2)^V},\qquad
p_f(U)=\frac12\operatorname{ReTr}(W_f(U)),\quad -1\le p_f\le1.
\]
Normalize the bi-invariant SU(2) Laplacian by \(-\Delta\chi_j=j(j+1)\chi_j\). The physical Hamiltonian is
\[
H_G=\sum_{e\in E}a_e(-\Delta_e)+\sum_{f\in F}b_f(1-p_f),\qquad a_e>0,\ b_f\ge0.
\]
On a compact finite graph this has a simple strictly positive gauge-invariant ground state, with a discrete positive excited spectrum. All claims about infrared uniformity below refer to many graphs, changing coefficients, and/or a spatial continuum scale, not to existence of a positive finite-volume gap.

## II. R3 obstruction 1: exact temporal decimation cannot create a physical gap

**Proposition R3-1 (energy invariance under exact time blocking).** Suppose \(T\) is a strictly positive physical transfer operator with eigenvalues \(\lambda_0>\lambda_1\ge\cdots>0\), and the elementary temporal spacing is \(h\). Let \(T^{(n)}=T^n\), interpreted with spacing \(nh\). Then for every excited eigenvalue
\[
-\frac1{nh}\log\frac{\lambda_k(T^{(n)})}{\lambda_0(T^{(n)})}
=-\frac1h\log\frac{\lambda_k(T)}{\lambda_0(T)}.
\]
**Proof.** Functional calculus gives \(\lambda_k(T^{(n)})=\lambda_k(T)^n\); take logarithms.  \(\square\)

No approximation or gap assumption is used. Decimating an exact transfer step re-expresses, but cannot enlarge, the interacting energy gap. A *nontrivial spatial/field RG* must demonstrate extra estimates on generated interactions and transformed sources; it cannot extract a new physical spectral inequality from the identity \(T^{(n)}=T^n\) alone.

## III. R3 obstruction 2: a uniform all-coupling source bound without an energy scale is false in the literal Wilson class

**Theorem R3-2 (one-rhombus Wilson counterexample to coupling-independent \(s^p\) constants).** On one spatial rhombus with open boundary and equal positive electric weights \(a_e=a\), let \(b=0\), and let \(A=p_f=\chi_{1/2}(W_f)/2\) be the contractible, center-neutral plaquette multiplier. Its vacuum is \(\Omega=1\); its excited source is \(Q A\Omega=A\); and its cumulative excited-state spectral weight is exactly
\[
F_A(s)=\big\|P_{(0,s]}QA\Omega\big\|^2
=\frac14\,\mathbf 1_{\{s\ge3a\}}.
\]
**Proof.** Gauge fixing identifies the physical wavefunctions with conjugation-invariant functions of the loop holonomy \(W_f\). Normalized SU(2) Haar character orthogonality gives \(\langle\chi_{1/2},1\rangle=0\), \(\|\chi_{1/2}\|^2=1\). Thus \(\|A\|_{L^2}^2=1/4\). The gauge-invariant fundamental spin network carries spin \(1/2\) on all four edges, so \(\sum_ea(-\Delta_e)A=4a(3/4)A=3a A\). \(\square\)

For any fixed \(p>0\), a proposed all-coupling bound \(F_A(s)\le Cs^p\) with \(C\) independent of *all* positive electric scales fails: take \(s=3a\), then \(1/4\le C(3a)^p\) is impossible as \(a\downarrow0\).

The same rescaling logic works with a **positive magnetic term**. Fix any \(H_0\) of the form above with \(b>0\). Since the nonconstant Wilson multiplier \(A\) has nonzero overlap with at least one excited eigenfunction of \(H_0\), the family \(H_\epsilon=\epsilon H_0\), \(\epsilon>0\), has identical eigenvectors and spectral weights but excited energies multiplied by \(\epsilon\); again a coupling-independent \(Cs^p\) bound is impossible.

**Scope warning:** this does **not** rule out a theorem with electric coefficients bounded below in **fixed physical units**, nor one restricted to the specific continuum trajectory \(a_e=g_3^2/(2w_e)\). It rules out an unnormalized, arbitrary-coupling claim.

## IV. R3 obstruction 3: first interacting source insertion is off-diagonal

The prior fully checked SU(2) character calculation gives normalized temporal-link convolution coefficients
\[
\rho_j(\beta)=I_{2j+1}(\beta)/I_1(\beta),\quad \rho_0=1.
\]
For a single gauge-invariant rhombus with \(|j\rangle=\chi_j(W)\), let \(C|j\rangle=r_j|j\rangle\), where \(r_j=\prod_{e\in\partial f}\rho_j(\beta_{t,e})\). Multiplication by \(p_f=\chi_{1/2}/2\) obeys the Clebsch–Gordan character identity, so
\[
\langle j'|C M_{p_f}C|j\rangle
=\frac{r_jr_{j'}}2\big(\delta_{j',j+1/2}+\delta_{j',j-1/2}\big).
\]
In particular, \(\langle1/2|C M_{p_f}C|0\rangle=r_{1/2}/2>0\). With \(x=hb\), the actual transfer
\(T=e^{-x(1-p_f)/2}Ce^{-x(1-p_f)/2}\) has
\[
\langle1/2|T|0\rangle=\frac{x}{4}(1+r_{1/2})+O(x^2).
\]
This first-step calculation is exact in its specified isolated subcomplex (expansion error at fixed \(b,h\)); other plaquettes generate further spin-network couplings. Hence an RG map tracking only \(\rho_j\) is not closed for the interacting neutral sector. At \(\beta\to\infty\), \(\rho_{1/2}\to1\); a fixed unrenormalized strict character contraction also fails uniformly over the coupling range.

## V. What a full R3 proof must additionally establish

Fix physical \(g_3^2\), admitted spatial boundaries, and the center-neutral physical sector. Define \(K_{a,L}=H_{a,L}-E_0(a,L)\) on \(\Omega^\perp\). A **source-specific** R3 result would establish (for every admitted, appropriately normalized local observable \(A\))
\[
\|P_{(0,s]}(K_{a,L})QA\Omega_{a,L}\|^2\le C_A s^{1+\alpha},\quad
0<s\le\eta,\ \alpha>0,
\]
with volume-independent constants at fixed cutoff, and separately cross-position bounds for distant observables. Even if this is proved for a class of Wilson loops, it **does not** establish a gap for the whole physical Hilbert space: low-energy states orthogonal to those sources remain possible.

A stronger spectral theorem is \(\inf_{a,L}\operatorname{gap}(H_{a,L})>0\) in fixed physical units, equivalently a uniform vacuum-orthogonal Dirichlet/Poincaré estimate. To derive either theorem by character RG without circularity, the induction must demonstrate:

1. An **exact gauge-preserving field-blocking map** for the chosen Penrose cells and temporal seams, including a source map \(\mathcal O_n\mapsto\mathcal O_{n+1}\).
2. A Banach/polymer norm under which generated multi-loop, higher-spin interactions are summable, with a **derived** contraction estimate in the center-neutral channel, not assumed infrared clustering.
3. A large-field/noncommuting-holonomy bound with constants independent of spatial volume and cutoff, not only a perturbation series near the trivial configuration.
4. Error estimates in physical energy units over arbitrarily many spatial scales, ensuring the observed decay is not merely shrinking overlap of unrenormalized plaquette sources.
5. A completeness/cyclicity argument if source-sector suppression is to imply a full physical spectral gap, and boundary/center-sector control.

No such all-scale RG induction is available from the user-supplied Stage 26 records, dissertation, or first-character-blocking results. R3 remains **open** at arbitrary magnetic coupling and along the continuum trajectory.

## VI. R2 new theorem: exact finite-patch geometric tensor identity

Take a genuine finite rhombus-face collection \(\mathcal F\) in the Euclidean plane. For each face \(f\), let \(A_f>0\) be its area, and let \(u_f,v_f\in\mathbb R^2\) be unit vectors along its two edge directions. Define a *boundary-consistent* edge dual area
\[
D_e=\frac12\sum_{f\in\mathcal F:\,e\subset\partial f} A_f.
\]
For closed quadrangulations every edge has two incident faces, so \(D_e=(A_L+A_R)/2\), exactly the supplied geometric Wilson prescription \(w_e\ell_e^2\). For open patches the one-face rule is a specified boundary extension, not necessarily the unknown Stage 26 action.

Define the symmetric temporal curvature tensor
\[
M_{\mathcal F}=\sum_{e}D_e\,t_et_e^{\mathsf T},
\]
where \(t_e\) is the unit tangent to edge \(e\).

**Theorem R2-G1 (face decomposition and trace).**
\[
\boxed{M_{\mathcal F}=\sum_{f\in\mathcal F}A_f(u_fu_f^{\mathsf T}+v_fv_f^{\mathsf T}),\qquad
\operatorname{tr}M_{\mathcal F}=2\sum_f A_f.}
\]
**Proof.** Interchange the edge and face sums. Each face contributes \(A_f/2\) per incident edge; its four edges comprise two parallel copies of each unit direction, so its contribution is \(A_f(u_fu_f^{\mathsf T}+v_fv_f^{\mathsf T})\). The trace of each rank-one projector is 1. \(\square\)

**Theorem R2-G2 (exact fivefold isotropy).** Suppose the face collection is invariant as an oriented geometric collection under a rotation \(R\) by \(2\pi/5\), including its areas and edge directions. Then
\[
\boxed{M_{\mathcal F}=\Big(\sum_f A_f\Big)I_2.}
\]
**Proof.** The rotation permutes the weighted face collection, so \(RM_{\mathcal F}R^{\mathsf T}=M_{\mathcal F}\). A real symmetric \(2\times2\) matrix commuting with a planar rotation through an angle neither 0 nor \(\pi\) must be a scalar multiple of the identity. Taking traces using R2-G1 identifies that scalar as \(\sum_f A_f\). \(\square\)

A single rhombus is anisotropic: the eigenvalues of \(u_fu_f^{\mathsf T}+v_fv_f^{\mathsf T}\) are \(1\pm|\cos\theta_f|\). For a thin Penrose rhombus at \(36^\circ\), they are approximately 0.190983 and 1.809017; for a fat rhombus at \(72^\circ\), approximately 0.690983 and 1.309017. Fivefold averaging restores identity **exactly**, as verified independently by `check_geometric_tensor.py`.

**Theorem R2-G3 (macroscopic Penrose tensor isotropy).** For the standard rhombic Penrose hull, assume the standard established unique translation-ergodicity with patch frequencies. For van Hove exhaustions \(\mathcal F_R\) of any Penrose tiling, with boundary-to-area ratio tending to 0,
\[
\boxed{\lim_{R\to\infty}\frac{M_{\mathcal F_R}}{\sum_{f\in\mathcal F_R}A_f}=I_2.}
\]
**Proof.** The local additive matrix \(A_f(u_fu_f^T+v_fv_f^T)\) has finitely many prototile-orientation types. Unique patch frequencies give a limiting matrix per area uniformly across van Hove exhaustions. Rotating the tiling by \(R\) sends the hull to itself and conjugates that limiting matrix. The unique translation-invariant probability measure is rotation invariant: \(R_*\mu\) is again translation invariant and uniqueness forces \(R_*\mu=\mu\). Thus the limiting matrix commutes with the nontrivial fivefold rotation and is scalar. R2-G1 fixes its trace to 2 and hence its value to \(I_2\). The boundary error is \(o(\mathrm{area})\). \(\square\)

For bounded Lipschitz physical domains \(D\), scaling the Penrose tiling by \(a\to0\), the same uniform patch-frequency theorem plus mesoscopic partition of unity gives, for a continuous \(F_0:D\to\mathbb R^2\),
\[
\sum_{e\in a\mathcal T\cap D}D_e(a)\,[t_e\cdot F_0(x_e)]^2\ \longrightarrow\ \int_D|F_0(x)|^2\,dx
\]
with the boundary-consistent dual areas, and analogously \(\sum_fA_f(a)h(x_f)\to\int_Dh(x)dx\) for continuous \(h\). This is a **deterministic classical quadratic-form consistency** result for the prescribed geometry, not homogenization of the interacting quantum ground state and not an OS reconstruction.

## VII. R2 classical Yang–Mills quadratic normalization for the supplied geometric action

The directly supplied related-study source in `penrose_yang_mills_2p1_causal_study.zip/penrose_2p1_study.py` implements, for closed quadrangulations,
\[
\beta_{s,f}=\beta_{\rm ref}a_{\rm ref}\frac{h}{A_f},\qquad
\beta_{t,e}=\beta_{\rm ref}a_{\rm ref}\frac{w_e}{h},\quad w_e=D_e/\ell_e^2.
\]
Set \(\beta_{\rm ref}a_{\rm ref}=4/g_3^2\), with SU(2) generators \(\sigma^a/2\). For a fixed smooth continuum connection \(\mathscr A\), the normalized fundamental Wilson deficit around a small loop of area \(\mathcal A\) obeys
\[
1-\tfrac12\operatorname{ReTr}\operatorname{Hol}(\partial S)
=\frac{\mathcal A^2}{8}\sum_a(F^a_{\mu\nu})^2+o(\mathcal A^2)
\]
when the loop shrinks regularly (evaluated at a representative point).

For the temporal ribbon around edge \(e\), \(\mathcal A=h\ell_e\), with tangent \(t_e\), so at leading order
\[
\beta_{t,e}(1-p_{t,e})=\frac{h}{2g_3^2}D_e\sum_a\big(t_e\cdot(F^a_{01},F^a_{02})\big)^2+\text{higher order}.
\]
For a spatial rhombus,
\[
\beta_{s,f}(1-p_{s,f})=\frac{h}{2g_3^2}A_f\sum_a(F^a_{12})^2+\text{higher order}.
\]
Theorem R2-G3 therefore yields the **correct isotropic quadratic continuum action on smooth backgrounds**, for tame simultaneous \(a,h\to0\) and van Hove/macroscopic Penrose sampling:
\[
S_{\rm Wilson}^{(2)}(\mathscr A)\to
\frac{1}{2g_3^2}\int dt\,d^2x\sum_a\big((F^a_{01})^2+(F^a_{02})^2+(F^a_{12})^2\big)
=\frac{1}{4g_3^2}\int d^3x\sum_{a,\mu,\nu}(F^a_{\mu\nu})^2.
\]
The full non-Abelian smooth-field small-loop expansion has controlled vanishing higher-order terms for shape-regular \(a\)-scale rhombi and temporal aspect ratio bounded above/below; the displayed result is a **consistency test on fixed smooth configurations**, not a bound on rough Wilson-distributed gauge fields. It does not prove that the interacting measure concentrates on those smooth fields, establish the renormalized coupling, or control the continuum excitation spectrum.

## VIII. R2 fixed-graph quantum time limit and open spatial continuum

At each **fixed finite spatial graph** with \(a_e,b_f\) fixed, choose temporal Wilson couplings
\[
\beta_{t,e}(h)=2/(a_e h),\qquad \beta_{s,f}(h)=b_fh.
\]
The normalized temporal-link convolution coefficient \(\rho_j\) obeys
\(\rho_j(\beta_{t,e})=1-a_ej(j+1)h+O(h^2)\) for each fixed spin. On the finite Peter–Weyl core, the symmetric transfer product has derivative \(-H_G\), and contraction-semigroup/Chernoff convergence yields
\[
T_h^{\lfloor t/h\rfloor}\psi\ \to\ e^{-tH_G}\psi
\]
strongly, restricted to the physical gauge-invariant space. This is **already proved in the preceding R3/R2 memorandum**. It is not uniform in spatial graph size or in \(a\to0\).

For the geometric prescription and Penrose rhombus area \(A_f(a)=a^2\widehat A_f\), \(w_e\) is dimensionless, giving
\[
a_e(a)=g_3^2/(2w_e)=O(g_3^2),\qquad
b_f(a)=4/(g_3^2A_f(a))=O((g_3^2a^2)^{-1}).
\]
The full magnetic term is **not** relatively small compared with the electric term as \(a\to0\); in fact \(b_f/a_e\asymp(g_3^2a)^{-2}\). With \(h\asymp a\), \(h b_f\asymp1/a\) invalidates a transfer-potential expansion in **operator norm**, even though the classical smooth-field Wilson action is consistent (its Wilson deficits shrink). A highly anisotropic choice \(h=o(a^2)\) restores \(h b_f\to0\) locally but by itself supplies no quantum spatial continuum limit.

To close **quantum R2**, still needed: (i) exact production D1 seam and couplings source audit; (ii) tightness/existence of suitably flowed or smeared gauge-invariant Schwinger functions along genuine Penrose scaling; (iii) OS reconstruction with a common physical metric and a well-defined Hamiltonian; (iv) control of boundaries and of relevant 1-form center/global sectors; and (v) a uniform physical-energy vacuum-orthogonal spectral estimate, derived rather than assumed. Even a successful source-specific R3 bound must be supplemented by a completeness argument to prove (v).

## IX. Known literature and source distinctions

* J. Kogut and L. Susskind, *Hamiltonian formulation of Wilson's lattice gauge theories*, Phys. Rev. D 11, 395 (1975), DOI 10.1103/PhysRevD.11.395.
* M. Creutz, *Gauge fixing, the transfer matrix, and confinement on a lattice*, Phys. Rev. D 15, 1128 (1977), DOI 10.1103/PhysRevD.15.1128.
* J. Mazáč, *Patch frequencies in rhombic Penrose tilings*, Acta Crystallographica A 79, 399–411 (2023), DOI 10.1107/S2053273323004990. Establishes and uses fivefold representation and Penrose patch frequencies/strict ergodicity (with references).
* Source-specific weights and temporal ribbons: user's `penrose_yang_mills_2p1_causal_study.zip/penrose_2p1_study.py`, functions `geometric_weights` and `extrude`, around lines 65–111. This is NOT a source-level certification of the *literal Stage 26* `stage7_checkpointed.setup_geometry` implementation.
* Prior session's `/mnt/data/R3_R2_character_blocking_2026_10_26/FORMAL_CHARACTER_BLOCKING_AND_R2_AUDIT.md` provides the complete first-character-blocking and fixed-spatial temporal semigroup proofs.

## X. Final acceptance table

| Proposition | Disposition |
|---|---|
| Temporal decimation preserves interacting physical excitation energies | **PROVED** |
| A coupling-independent infrared \(Cs^p\) spectral-weight claim without fixing an energy scale | **DISPROVED**, inside the literal one-rhombus Wilson class |
| First center-neutral interacting Wilson insertion off-diagonal | **PROVED** in single rhombus (earlier audit) |
| Arbitrary-coupling, size-uniform neutral-sector source contraction | **NOT PROVED** |
| Full mass-gap coercivity across physical sectors | **NOT PROVED** |
| Exact C5 isotropy of the weighted temporal quadratic tensor | **PROVED** |
| Penrose macroscopic tensor isotropy through unique patch frequencies | **PROVED**, using established strict ergodicity |
| Smooth-field geometric Yang–Mills quadratic normalization | **PROVED as classical consistency**, not as a quantum continuum limit |
| Fixed-spatial-graph continuous-time quantum Hamiltonian limit | **PROVED** in preceding audit |
| Simultaneous quantum spatial continuum, regulator-independent physical gap | **NOT PROVED** |

**Conclusion.** R3 cannot be completed from isolated-character contractions, Ward identities, or geometric C5 alone. R2 has an exact, source-specific *classical* geometric-isotropy normalization and a fixed-graph time-continuum theorem, but lacks quantum spatial-continuum reconstruction and spectral coercivity. These gaps are substantive open problems; they should not be reported as solved.