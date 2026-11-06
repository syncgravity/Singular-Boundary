# R3 / P2–T2 · Full non-Abelian cubic SU(2) plaquette-influence inequality, quantitative locality, and an absolute-value obstruction

**Research date:** 2026-11-06. **Status:** exact finite-volume, classical original-link SU(2) theorem for arbitrary (including noncommuting) configurations, accompanied by independently executed finite-dimensional numerical checks and a reproducible *numerical* local-maximum counterexample. Not a mesh-uniform positive-physical-flow-time nonlinear curvature theorem, true-vacuum probabilistic bound, 4D interacting continuum construction, infrared spectral gap, Penrose transfer, or gravity UV theorem. **All continuum P0–P5 / T0–T5 gates and the separate gravity goal remain OPEN.** Independent mathematical review is required for the proposed proof.

**Depends upon:** The finite original-link 3D cubic Wilson spatial gradient flow (`R3_GAUGE_COVARIANT_SPATIAL_FLOW_AND_FISHER_GAP_OBSTRUCTION_2026-11-06.md`), its exact classical action identity (`R3_NONLINEAR_CUBIC_PHYSICAL_ENERGY_DISSIPATION_2026-11-06.md`), the linearized physical-radius theorem (`R3_FIXED_PHYSICAL_RADIUS_LINEARIZED_CUBIC_FLOW_2026-11-05.md`), and the *Haar-null* exactly invariant Cartan planar nonlinear smoothing theorem (`R3_EMBEDDED_CARTAN_NONLINEAR_POSITIVE_RADIUS_SMOOTHING_2026-11-06.md`). No numerical Stage 26 dataset or independent Penrose claim is used in this argument.

## 1. Original-link geometry and definitions

Let \(\Gamma\) be any finite, open, three-dimensional cubical lattice complex, with oriented links \(E\) and oriented elementary plaquettes \(P\). Every plaquette has exactly four distinct boundary links, and each link is incident to at most four plaquettes. Link variables \(U_e\in SU(2)\) are equipped with the product bi-invariant metric whose orthonormal generators are \(T_j=i\sigma_j/2\). Let \(U_p\) be each oriented plaquette holonomy; set

\[
\ell_p(U)=1-\tfrac12\mathrm{tr}_{\mathbf2}U_p\in[0,2],\qquad a_p(U)=\sqrt{\ell_p(U)},\qquad S(U)=\sum_{p\in P}\ell_p(U).
\tag{1}
\]

The full, unmodified **classical** original-link spatial gradient flow is \(dU_s/ds=-\nabla S(U_s)\), where \(s\) is *lattice spatial flow time*, not physical quantum Hamiltonian time. At physical spatial smoothing radius \(\tau\), write \(s=\tau/h^2\). All observables are gauge invariant and no gauge fixing or common Cartan subgroup is assumed.

Define the symmetric nonnegative incidence matrix and its off-diagonal part:

\[
N_{pq}:=\#(\partial p\cap\partial q),\quad N_{pp}=4,\quad A_{pq}=\begin{cases}\tfrac14N_{pq},&p\ne q,\\0,&p=q.\end{cases}
\tag{2}
\]

Thus \(\|A\|_{\ell^\infty\to\ell^\infty}\le3\); the graph on plaquettes joins two faces exactly when they share an original physical link. We retain the *full* SU(2) noncommutative Wilson action, not independent faces.

## 2. Exact per-plaquette gradient and cross-energy identity

**Lemma 1 (full SU(2) character gradient).** For every incidence \(e\in\partial p\), if \(x_p=\tfrac12\mathrm{tr}_{\mathbf2}(U_p)=1-\ell_p\),

\[
\boxed{\|\nabla_e\ell_p\|^2=\frac{1-x_p^2}{4}=\frac{\ell_p(2-\ell_p)}4\le\frac{\ell_p}2.}
\tag{3}
\]

For any two faces define the original-link carré du champ

\[
\Gamma_{pq}(U)=\sum_{e\in\partial p\cap\partial q}\langle\nabla_e\ell_p,\nabla_e\ell_q\rangle.
\tag{4}
\]

For distinct faces \(p\ne q\), **without any commutativity hypothesis**,

\[
\boxed{|\Gamma_{pq}|\le\frac{N_{pq}}2a_pa_q.}
\tag{5}
\]

**Proof.** Write \(U_p=x_p\mathbf1+\mathbf v_p\cdot i\boldsymbol\sigma\), \(x_p^2+|\mathbf v_p|^2=1\). Differentiating \(1-\mathrm{Re}(U_p)\) on a single link by \(e^{tT_j}\) produces a cyclically permuted product with derivative \(\pm\mathbf v_p/2\); orientation only affects the sign and conjugation, not the norm. This proves (3). Cauchy–Schwarz for each original shared link yields \(|\langle\nabla_e\ell_p,\nabla_e\ell_q\rangle|\le a_pa_q/2\). Summing only over their *actual* shared links proves (5). A product-Haar or continuum assumption is not involved. \(\square\)

**Theorem 2 (exact nonlinear defect balance).** For every finite smooth original-link flow trajectory,

\[
\boxed{\dot\ell_p=-\ell_p(2-\ell_p)-\sum_{q\ne p}\Gamma_{pq}.}
\tag{6}
\]

The global identity is simultaneously \(\dot S=-\sum_e\|\nabla_e S\|^2\le0\). The latter does not imply that individual \(\ell_p\) decrease.

**Proof.** Differentiating \(\ell_p(U_s)\) along \(-\nabla S\) gives \(-\sum_{e\in\partial p}\langle\nabla_e\ell_p,\sum_{q\ni e}\nabla_e\ell_q\rangle\). The \(q=p\) term equals \(-4\cdot\ell_p(2-\ell_p)/4\) by (3). The rest is (4). Summing the action derivative over p gives the negative squared total gradient. \(\square\)

## 3. An all-configuration local influence theorem

**Theorem 3 (non-Abelian plaquette-amplitude comparison).** With \(a_p=\sqrt{\ell_p}\), at every \(s\ge0\), in the upper right Dini-derivative sense at zeros,

\[
\boxed{D_s^+a_p\le-\tfrac12(2-\ell_p)a_p+\sum_{q\ne p}A_{pq}a_q\le(Aa)_p.}
\tag{7}
\]

Therefore the finite nonnegative matrix semigroup gives the pointwise, **all-configurations**, gauge-invariant comparison

\[
\boxed{a(s)\le e^{sA}a(0)\text{ componentwise},\qquad
\|a(s)\|_\infty\le e^{3s}\|a(0)\|_\infty.}
\tag{8}
\]

If the initial defect amplitude is supported at plaquette-graph distance at least \(d\) from a given face p, then, with \(M_0=\|a(0)\|_\infty\),

\[
\boxed{a_p(s)\le M_0\sum_{k=d}^\infty\frac{(3s)^k}{k!}\le M_0e^{3s}\frac{(3s)^d}{d!}.}
\tag{9}
\]

**Proof.** For \(\ell_p>0\), (6) divided by \(2a_p\), with (5), proves the first inequality in (7). At \(\ell_p=0\), the function \(\sqrt{1-\mathrm{Re}U_p}\) is Lipschitz in the finite link variables. Its one-link upper metric slope is at most \(1/(2\sqrt2)\); the self-plaquette Wilson force vanishes at the identity, and the remaining physical forces have norms at most \(\sum_{q\ni e,\,q\ne p}a_q/\sqrt2\). The same upper Dini inequality follows at a zero. The matrix A has nonnegative entries; finite-dimensional comparison with the Metzler field \(Aa\) yields \(a(s)\le e^{sA}a(0)\). The cubic incidence bound gives each row sum \(\sum_{q\ne p}N_{pq}\le4\cdot3=12\), hence \(\|A\|_\infty\le3\). For (9), expand \(e^{sA}\) in nonnegative powers. A length-k adjacency walk cannot connect support to p when \(k<d\), and \(\|A^k\|_\infty\le3^k\); the standard Poisson-tail inequality \(\sum_{k\ge d}x^k/k!\le e^xx^d/d!\) completes the proof. \(\square\)

**What this controls.** The theorem is valid for *all* finite original-link SU(2) fields, including noncommuting link and plaquette holonomies. It gives a finite-regulator locality/influence envelope and the exact nonlinear self-dissipation term. The constants do not depend on n at a fixed **dimensionless** s. **What it does not control:** because \(s=\tau/h^2\), (8) becomes \(e^{3\tau/h^2}\), which diverges as \(h\to0\) at any fixed positive physical flow time. This is a limitation of this positive upper bound; it neither proves singular physical flow nor contradicts possible non-Abelian regularization. The next theorem must exploit *signed covariant cancellations and noncommutative Bianchi/heat structure*, not simply iterate absolute-value influence estimates.

## 4. Countercheck to an unrestricted scalar maximum principle

The same finite SU(2) model admits noncommuting configurations with a **strictly largest** individual plaquette defect \(\ell_{p_*}\) that initially increases under its full nonlinear Wilson gradient flow, while \(S\) decreases. An executable deterministic witness on an open \(n=3\) cube is recorded as full original-link unit quaternions in `docs/evidence/R3_FULL_NONABELIAN_CURVATURE_INFLUENCE_2026-11-06.json`. It is generated with NumPy PCG64 seed `361218`, scale `0.8`, sample `15`, in a fixed ordered loop and verified by evaluating the exact analytic force. The witness has

\[
\ell_{p_*}(0)\simeq1.9147924,\quad\dot\ell_{p_*}(0)\simeq0.0577442>0,
\quad\dot S(0)<0.
\tag{10}
\]

The stored witness has a strict maximum margin over all other plaquettes and noncommuting original links. This is a **finite numerical counterexample** to a blanket all-configurations maximum principle for \(\max_p\ell_p\); it is not an exact symbolic counterexample or proof that a maximum principle fails in every small-plaquette admissible regime. In particular, the maximum is near the large-curvature part of the SU(2) class character. It also does not demonstrate failure of any flow-smoothed gauge-invariant *quantum* observable. Only the precise negative/positive derivatives and strict margin at the displayed numerical witness are asserted.

## 5. Independent reproducibility, classification, and next bridge

`research/scripts/verify_nonabelian_curvature_influence.py` independently constructs every vertex/link/face and its oriented incidence for open 2^3 and 3^3 cubic complexes; represents the SU(2) links as unit quaternions; computes the **analytic left-invariant full non-Abelian Wilson force** and its individual plaquette gradients; and verifies (3), (5), (7), and independent local gauge invariance on 144 noncommuting random configurations at three amplitude scales. It then integrates actual full nonlinear link ODEs at the same positive physical time \(\tau=.02\) on two finite meshes, verifying total action decay, exact SU(2) norms, and distinct local/total energy behavior. The full initial quaternion witness, exact assertion record, and measurement tolerances are preserved in the evidence JSON and reproducible code. Finite tests are *checks of equations*, not an independent all-configurations proof, and no finite quantum Wilson ground state was sampled.

**Indexer requirement.** The authoritative branch theorem registry must enumerate each tracked `research/theorems/*.md` source **exactly once**, bind each record to its Git blob SHA, and reject missing or stale paths when checked out. Historical theorem text is not silently amended; an index entry conveys *discoverability*, not peer review or gate closure. The corresponding graph node for this result must explicitly distinguish `finite` from the **OPEN** full non-Abelian positive-physical-radius curvature estimate.

**Next decisive target (OPEN):** derive a covariant discrete curvature evolution and a sign-sensitive, gauge-invariant physical-time estimate on a class of genuinely noncommuting fields whose probability is controlled under the actual weak-coupling interacting Wilson vacuum. Subsequently prove renormalized nontrivial four-dimensional flowed covariance, complete interacting time-Schur/connected correlations, reflection-positive OS continuum construction, and strictly positive physical spectral separation. Cubic control, Penrose/coupled-\(\mathbb Z^5\) transfer and gravitational quantum UV regularity are distinct obligations. No P0–P5 or T0–T5 gate is closed here.
