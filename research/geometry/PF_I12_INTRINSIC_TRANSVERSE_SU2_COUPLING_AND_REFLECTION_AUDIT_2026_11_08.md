# PF-I12 — Intrinsic 2+2 transverse rhombi, nonfactorizing SU(2) couplings, and reflection-positivity tests

**Checkpoint:** November 8, 2026 (America/Denver). **Source inputs:** recovered original unpublished SU(2)/Penrose $\mathbb Z^5$ computational script, exact original selected labels and rhombi from PF-I11, distinct completed-window incident-star controls from PF-I9/PF-I11, and the *unpublished* J-operator draft. **Status:** exact intrinsic four-form; verified eight-size local transverse incidence; exact conditional finite non-Abelian gauge interaction and analytically nonzero connected correlation; an explicit obstruction to one natural reflection kernel; an alternative conditional positive two-face heat-kernel gluing. **Not established:** source-unique coupling magnitude, a physical 4D volume, intrinsic temporal axis, OS/reflection positivity on the whole source complex, nontrivial continuum SU(2) Yang–Mills existence, or a physical continuum mass gap. All physical continuum gates remain **OPEN**.

The dissertation is a **historical, unpublished source**, not binding proof authority. The five integer directions and two nontrivial representation planes are source-defined. In contrast, the proposed cross-plaquette action and its strength are **new, clearly labeled test models**, not recovered postulates of the author. No cubic/triangular physical regulator or chosen 3+1 spacetime is introduced.

## 1. PF-I12.A — exact intrinsic 4-form on the 2+2 representation

Let \(E_\parallel\cong\mathbb R^2\) and \(E_\perp\cong\mathbb R^2\) be the two inequivalent real nontrivial irreducible summands of the \(C_5\) representation on \(\mathbb R^5\), with the trivial height direction removed. Define

\[
 v_j=\Big(\cos\frac{2\pi j}{5},\sin\frac{2\pi j}{5},
 \cos\frac{4\pi j}{5},\sin\frac{4\pi j}{5}\Big)^T,
 \quad j=0,1,2,3,4,
 \qquad A=(v_0\ \cdots\ v_4)\in\mathbb R^{4\times5}.
\]

**Exact theorem.** By fivefold Fourier orthogonality,
\[
 AA^T=\frac52 I_4,\qquad A(1,1,1,1,1)^T=0.
\]
For every four-element family set \(I\subset\{0,1,2,3,4\}\),
\[
\boxed{\left|\det A_I\right|=\frac{(5/2)^2}{\sqrt5}=\frac{5\sqrt5}{4}=2.7950849718747373\ldots .}
\]
**Proof:** The nonzero singular values of \(A\) are all \(\sqrt{5/2}\), and its unit right null vector is \((1,\ldots,1)/\sqrt5\). The cofactor/minor vector therefore has equal magnitude and squared norm \(\det(AA^T)=(5/2)^4\). There are five such minors. Hence each squared minor is \((5/2)^4/5\), yielding the formula. Equivalently the ten \(v_j\wedge v_k\) rhombus bivectors span transverse four-volume whenever the four indices in a pair are distinct. **QED.**

For source rhombi \(f,g\) with family labels \(\{j,k\},\{\ell,m\}\), define the **geometrically selected support**
\[
\mathcal T(K)=\{(f,g,v):f\ne g,\;v\in f\cap g,\;\lvert\{j,k,\ell,m\}\rvert=4\}.
\]
Each such pair has nonzero four-form volume; under the source generic geometry these two faces have only **one** common vertex, so each pair appears once. This selection respects the intrinsic family permutation geometry and uses no arbitrary cut across a cubic mesh. It is also necessary to distinguish what is **not** proved: each actual rhombus projects into **both** irreducible planes. A pair of four distinct family directions is not literally a pair of independent physical/spacetime fields, and \(\lvert\det A_I\rvert\) does **not** by itself supply a physically normalized four-dimensional volume measure. The retained source 2-complex has vertices, edges and genuine rhombi; it has **no attached 3- or 4-cells** in PF-I11. In particular a full four-coordinate \(\mathbb Z^5\) unit cube cannot have all 16 vertices in the height set \(h\in\{1,2,3,4\}\): its height range has width 4. Other higher-dimensional cell/gluing definitions are not ruled out, but they **must be introduced and justified separately**.

### Eight original and eight separately completed finite source populations

Every original row below has independently reproduced exactly the PF-I11 SHA-256 fingerprints for accepted integer vertex labels, rhombi, and \((V,E,F)\), using the original source script hash. Every completed-core row is a **different** population, independently checked against PF-I11's completed-window fingerprint. No original data were silently changed.

| \(N_{grid}\) | Source rhombi \(F\) | Original transverse pairs \(T\) | Completed-core rhombi \(F_c\) | Completed transverse pairs \(T_c\) |
|---:|---:|---:|---:|---:|
| 7 | 1,468 | 3,093 | 1,330 | 2,785 |
| 10 | 2,886 | 6,157 | 2,846 | 6,057 |
| 12 | 4,145 | 8,890 | 4,089 | 8,770 |
| 15 | 6,800 | 14,559 | 6,586 | 14,153 |
| 18 | 9,646 | 20,749 | 9,604 | 20,669 |
| 20 | 11,879 | 25,590 | 11,844 | 25,585 |
| 23 | 16,138 | 34,897 | 15,787 | 34,307 |
| 25 | 18,874 | 40,853 | 18,880 | 40,973 |

The original \(T/F\) is between approximately 2.107 and 2.165, but its finite behavior is **not** a proven infinite-volume density or physical four-volume scaling law. The paired support survives the change of source boundary population and is thus not solely an artifact of the three original finite first-homology sectors. This does **not** prove that any associated gauge dynamics survives the continuum limit.

## 2. PF-I12.B — an exact conditional, gauge-invariant, non-Abelian-sensitive cross-face interaction

PF-I11 proves a finite positive Wilson/Haar measure with one matrix \(U_e\in SU(2)\) per oriented accepted basis edge and a genuine rhombus holonomy \(U_f\). For two transverse rhombi sharing exactly one vertex \(v\), orient/begin both four-edge loops at \(v\) to obtain \(A=U_f^v\), \(B=U_g^v\). Under independent vertex-gauge transformations \(g_x\), **both** transform as \(A\mapsto g_vAg_v^{-1}\), \(B\mapsto g_vBg_v^{-1}\). Therefore
\[
Q(A,B):=1-\tfrac12\operatorname{Tr}[A,B],\qquad [A,B]=ABA^{-1}B^{-1},
\]
is exactly gauge-invariant. It satisfies \(0\le Q\le2\), vanishes for commuting holonomies and is nonzero for generic **noncommuting** SU(2) holonomies.

A minimal conditional candidate, with the four-form magnitude scaled to one because it is identical for every disjoint family quartet, is
\[
\boxed{
 S_{\beta,\lambda}(U)=\beta\sum_{f\in F}(1-\tfrac12\operatorname{Tr}U_f)
 +\lambda\sum_{(f,g,v)\in\mathcal T(K)}Q(U_f^v,U_g^v),\quad\beta,\lambda\ge0.}
\]
This uses only source rhombi and their common vertices. **The term and the parameter \(\lambda\) were chosen here for a falsifiable finite coupling test, not derived as a unique source physical law.** The corresponding product-Haar measure is finite and positive, with
\[
  e^{-2(\beta F+\lambda T)}\le Z_K(\beta,\lambda)\le1,
\]
and gauge invariance follows exactly. Tests on the original 1,550-vertex and 12,207-/19,260-vertex complexes validate based face-holonomy construction and finite positivity; the nontrivial random vertex-gauge transformation check on the 1,550-vertex source graph agrees to floating point precision. No OS physical reflection or kinetic transfer is added.

### Exact PF-I12.C — a nonfactorizing connected covariance

Under the **\(\lambda=0\)** plaquette-only measure, PF-I11's sequential free-face Haar integration makes the entire set of face holonomies independently Haar-distributed after the single-face Wilson weights. For a transverse pair, write \(X=\tfrac12\operatorname{Tr}A=\cos\alpha\), \(Y=\tfrac12\operatorname{Tr}B=\cos\eta\), and let \(c\) be the dot product of the two independent SU(2) quaternion-axis unit vectors. Then \(c\) is uniform in \([-1,1]\), and quaternion multiplication gives the exact identity
\[
\boxed{Q(A,B)=2(1-X^2)(1-Y^2)(1-c^2).}
\]
Since \(\mathbb E_c(1-c^2)=2/3\),
\[
 \mathbb E[Q\mid X,Y]=\frac43(1-X^2)(1-Y^2).
\]
For *any finite* single-face baseline couplings \(\beta_f,\beta_g\), define \(V_\beta=\mathrm{Var}_\beta(X^2)>0\). Differentiating the normalized finite Haar expectation exactly at \(\lambda=0\),
\[
\boxed{\left.\frac{d}{d\lambda}\operatorname{Cov}_\lambda(X_f^2,X_g^2)\right|_{\lambda=0}=-\frac43 V_{\beta_f}V_{\beta_g}<0.}
\]
**Proof:** The first variation of any expectation under \(e^{-\lambda Q}\) is minus its covariance with \(Q\). The derivative of connected covariance is the corresponding third cumulant; using baseline independence and the conditional identity above gives \(-(4/3)\operatorname{Cov}(X^2,1-X^2)\operatorname{Cov}(Y^2,1-Y^2)=-(4/3)V_fV_g\). On the full source 2-complex, contributions from other pair terms cancel in this first derivative for a fixed transverse pair by independence of face-holonomy random variables and uniqueness of that pair. **QED.**

At \(\beta_f=\beta_g=0\), Haar half-trace has density \(\frac2\pi\sqrt{1-x^2}\,dx\), hence \(\mathbb E[X^2]=1/4\), \(\mathbb E[X^4]=1/8\), and \(V_0=1/16\). This yields the **exact coefficient**
\[
\boxed{\left.\partial_\lambda\operatorname{Cov}(X_f^2,X_g^2)\right|_{\beta=\lambda=0}=-\frac1{192}.}
\]
An independent Gauss–Chebyshev/Legendre three-variable Haar integral at \(\lambda=0.4\) gives \(\operatorname{Cov}(X_f^2,X_g^2)=-0.00224688093459\) for \(\beta=0\) and \(-0.00248551394557\) for \(\beta=0.71\). These are **finite mathematical test-model covariances**, not physical Yang–Mills correlators.

Another exact first-order result at \(\beta=0\) is \(\mathbb E_0[Q]=3/4\) per transverse pair, so
\[
\boxed{\left.\frac{\partial}{\partial\lambda}\log Z_K(0,\lambda)\right|_{\lambda=0}=-\frac34\,T(K).}
\]
This is extensive in the counted local support but not a physical four-dimensional thermodynamic free-energy density without an independently defined volume and limiting sequence.

## 3. PF-I12.D — this commutator model fails the simplest exchange-reflection positivity test

A **hypothetical**, not source-proved temporal reflection might exchange two transverse face-holonomy variables. For that two-face exchange test, a reflection-positive gluing would require \(\iint\overline{h(A)}h(B)\,e^{-\lambda Q(A,B)}d\mu_\beta(A)d\mu_\beta(B)\ge0\) for every test function \(h\).

Choose \(h(A)=X(A)^2-\mathbb E_\beta X^2\). At \(\lambda=0\) the quadratic form vanishes, while
\[
\boxed{\left.\frac d{d\lambda}\langle h,\Theta h\rangle_\lambda\right|_{\lambda=0}=-\frac43 V_\beta^2<0.}
\]
Consequently this **particular two-face commutator gluing is NOT reflection positive for sufficiently small positive \(\lambda\)** under that chosen swap. At \(\beta=0\) the derivative is exactly \(-1/192\). Direct Haar integration at \(\lambda=0.4\) yields a negative unnormalized test form \(-0.00126335243\) for \(\beta=0\) and \(-0.00039213705\) for \(\beta=0.71\).

**Scope restriction:** This is an exact no-go for **that exchange-reflection kernel**. It does not establish any physical involution on the complete source cut-and-project complex, and therefore it is not a general impossibility theorem against OS-positive dynamics on the proposed intrinsic geometry. It does rule out promoting the present commutator choice to an OS-positive field theory without further structure.

## 4. PF-I12.E — a conditional positive alternative exists for two-face gluing

For \(t>0\), the standard central SU(2) heat kernel has the Peter–Weyl expansion
\[
\boxed{K_t(AB^{-1})=\sum_{j\in\{0,\frac12,1,\dots\}}(2j+1)e^{-tj(j+1)}\chi_j(AB^{-1}).}
\]
Under simultaneous basepoint-gauge conjugation of \(A,B\), this kernel is gauge-invariant. Its positive Peter–Weyl coefficients make it a **positive-definite pair-exchange kernel**:
\[
\int\!\int \overline{h(A)}\,K_t(AB^{-1})\,h(B)\,dA\,dB\ge0.
\]
This is exact (the convolution operator is \(e^{t\Delta_{SU2}}\)). The positive kernel is normalized under Haar marginals and correlates two face half-traces by
\[
\boxed{\mathbb E_t\left[\tfrac12\operatorname{Tr}A\ \tfrac12\operatorname{Tr}B\right]=\frac14e^{-3t/4}>0.}
\]
At the explicitly **auxiliary** value \(t=0.85\), this equals \(0.1321530760665\); a 16-sample nontrivial SU(2) Gram test has minimum eigenvalue \(0.0816831068>0\), with independently convergent character truncation. This shows **finite nonfactorizing and reflection-positive two-face gluing is mathematically possible**, but **does not** select a physical \(t\), supply the actual reflection of the source tiling, prove global aperiodic OS positivity, or establish a physical mass gap. Pairwise positive kernels do not automatically confer positivity on an arbitrarily glued entire complex.

## 5. PF-I12.F — the source's C5 complex structure does not select a physical time axis

The unpublished revised J-operator manuscript displays \(J=J_\parallel\oplus J_\perp\) and states the complex structure follows uniquely from the \(C_5\) decomposition, then identifies the second sector's imaginary coordinate with \(ict\). The source **does** give a valid constant complex structure and \(C_5\)-equivariant 2+2 splitting. The statement of uniqueness and derivation of physical time require qualification.

**Exact representation lemma:** As real \(C_5\)-modules, the two nontrivial irreps \(E_\parallel\) and \(E_\perp\) are inequivalent. Schur theory gives \(\operatorname{End}_{C_5}(E_\parallel\oplus E_\perp)\cong\mathbb C\oplus\mathbb C\), with no mixed intertwiners. Solving \(J^2=-I\) therefore gives exactly **four** equivariant real complex structures
\[
\boxed{J=(\pm J_\parallel)\oplus(\pm J_\perp).}
\]
Once orientations and the signs in each plane are independently chosen, the source's \(J=(+,+)\) is valid; it is **not** uniquely determined by the bare group decomposition alone. Moreover the \(C_5\) generator acts in \(E_\perp\) as rotation by \(4\pi/5\), with no invariant **real line**. Thus the symmetry representation alone does **not** pick a distinguished real time axis in that plane. A chosen \(u,v\), Wick identification, symmetry-breaking order parameter, dynamical physical clock, or other additional physical principle may yet provide one; none follows simply from \(J^2=-I\) and fivefold symmetry.

This is not an attempt to force conventional \(3+1\) onto the source. It identifies precisely the **additional theorem** necessary to define a physical Hilbert-space evolution from the proposed \(2+2\) source geometry.

## 6. What has been achieved — and what remains open

**Exact FINITE theorems now established:** (i) intrinsic 4-form/minor and a D5/C5-compatible transverse face-pair support, (ii) all eight source and completed-core pair counts anchored by PF-I11 fingerprints, (iii) conditional local SU(2) commutator action is gauge-invariant, positive and nonfactorizing; exact connected-covariance derivative \(-1/192\) at Haar, (iv) its naive two-face exchange reflection fails positivity; (v) a separate conditional SU(2) heat gluing is positive by Peter–Weyl and gives explicit positive connected correlation, (vi) \(C_5\) admits four equivariant \(J\)'s and no distinguished real temporal line inside the internal 2-plane.

**Still OPEN, not stated as proved:** (a) why either interaction coefficient/function follows from the author's unifying field postulates rather than being an arbitrarily selected mathematically allowed action; (b) whether the intrinsic 2+2 construction supplies a physical four-volume and local field algebra or additional 3-/4-cells; (c) a source-justified global reflection/time or alternative constructive Hilbert-space dynamics; (d) finite physical Gauss-law sector, gauge-invariant long-distance correlations, source-phason/boundary-independent exhaustion, scaling/renormalization and a nontrivial interacting 4D Yang–Mills continuum limit; (e) a uniform positive **physical** mass gap. No gravitational UV theorem is inferred.

**Recommended next gate PF-I13:** source-derive or decisively falsify an admissible **global** two-sector gluing/physical time prescription on the intrinsic cut-and-project complex. Prefer a positive representation-theoretic kernel with a truly source-derived reflection/gluing geometry; compare any proposal against the conditional PF-I12 commutator obstruction before asking for a continuum bound. No need to assume cubic spacetime.

## 7. Reproducibility and unpublished-source confidentiality

- `verify_pf_i12_two_sector_coupling.py`: source-hash-verified eight-size \(\mathbb Z^5\) complex, all transverse pair supports and exact C5 four-form; local SU(2) based holonomy and gauge covariance; independent Haar quadrature and pair-exchange positivity counterexample.
- `verify_pf_i12_completed_core.py`: **separate** eight-size corrected window-core pair comparison, checked by PF-I11 SHA-256; does not replace any original source geometry.
- `verify_pf_i12_conditional_heat_gluing.py`: conditional positive two-face heat kernel and fundamental character correlation; no source physical time.
- `test_pf_i12_two_sector_coupling.py`: 26 passing regression tests with 3 original private snapshots; in a public environment without those source snapshots, 19 pass and 7 correctly skip. Exact geometry/representation/conditional gluing tests do not need private source.
- `PF_I12_EIGHT_SIZE_TRANSVERSE_EVIDENCE.json`, `PF_I12_COMPLETED_CORE_CONTROL.json`, `PF_I12_CONDITIONAL_HEAT_KERNEL_CONTROL.json`: deterministic complete finite mathematical evidence; no fake physical four-volume or gap result.
- Original unpublished author script and private PF-I11 graph snapshots remain **in Library**. The repository stores only **derived** proof, reproducible public code, source SHA labels and aggregate numeric results. All source-dependent claims are explicitly labeled.

All proof statuses at and beyond the interacting continuum/mass-gap gate remain **OPEN**.
