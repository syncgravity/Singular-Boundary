# P0–P2: interacting-vacuum conditional SU(2) blocking, local observables, and the exact effective Schur form

**November 6, 2026 (UTC) · Independent finite-regulator theorem candidate · NOT a continuum mass-gap proof.**

This result continues `R3_EXACT_TWO_TIME_INFLUENCE_AND_DYADIC_SCALING_2026-11-06.md` (draft PR #66). The earlier result establishes the exact *bare Haar* P/Q influence and its 20-to-128-face growth, but it does not define a vacuum-adapted physical renormalization prescription. Here the **true finite interacting ground state** supplies a canonical positive conditional measure, an exact local gauge-invariant normalized Wilson observable, and an energy-dependent effective form. It is rigorous at each fixed finite regulator; no estimates uniform in refinement or spatial volume follow automatically.

## 1. The actual finite SU(2) lattice and its vacuum

Let \(K_{h,R}\) be a finite connected three-dimensional oriented cubical cell complex (including the previously checked 2×2×1 and 4×4×2 slabs), with original-link configuration space \(G^{E_{h,R}}\), \(G=SU(2)\), normalized product Haar probability \(dm\), and the gauge-invariant physical subspace \(\mathcal H^{\mathrm{phys}}=L^2(G^E,dm)^{G^V}\). Use the full bounded spatial Wilson potential, not a polynomial truncation:

\[
H=K+V,\quad K=\alpha\sum_{e\in E}(-\Delta_e),\quad
V=\beta\sum_{p\in F}\left(1-\tfrac12\chi_1(U_p)\right),
\qquad\alpha=\frac{g_0(h)^2}{2h},\quad \beta=\frac{2}{g_0(h)^2h}.
\]

Here \(\Delta_e\) is the negative-semidefinite bi-invariant Laplace–Beltrami operator with fundamental Casimir \(3/4\). The finite product-group elliptic heat kernel is strictly positive; Feynman–Kac with the bounded real potential preserves strict positivity. Compact resolvent and positivity improvement yield a unique normalized smooth, strictly positive ground state \(\Omega\), with energy \(E_0\), on the full finite link space. Since gauge transformations commute with \(H\), simplicity implies gauge invariance of \(\Omega\). This conclusion holds only at **finite E**. In particular \(\Omega\) depends on every link and on \(h,R,g_0\) and is **not** computed for the 3D slabs in this audit.

Define the true interacting vacuum measure and ground-state transform

\[
 d\nu=\Omega^2dm,\qquad
L=\Omega^{-1}(H-E_0)\Omega,
\]

unitarily acting in \(L^2(G^E,\nu)\), with \(L\ge0\), \(L1=0\), and the exact Dirichlet form

\[
\mathcal E(f,g)=\alpha\sum_{e\in E}\int\langle\nabla_e f,\nabla_e g\rangle\,d\nu.
\tag{1}
\]

On smooth functions, the whole Wilson potential cancels into the vacuum logarithmic drift:

\[
Lf=-\alpha\sum_e\left(\Delta_e f+2\nabla_e\log\Omega\cdot\nabla_e f\right).
\tag{2}
\]

This does **not** make the interacting dynamics free: the unknown \(\nabla\log\Omega\) contains the full interacting information.

## 2. Exact vacuum-preserving, gauge-invariant fixed-support coarse map

Choose a physical closed boundary loop composed of **eight coarse link holonomies** (the bottom boundary of the 2×2 plaquette block). Let \(X=(X_1,\ldots,X_8)\in G^8\) be these ordered holonomies. On the coarse lattice, each \(X_i\) is one original link; on the dyadic fine lattice each \(X_i\) is the ordered product of **two** fine links. All other link variables are integrated. The product-Haar pushforward of either link family to \(X\) is normalized Haar \(dm_8\). The **interacting** pushforward of \(\nu\) is instead

\[
 d\nu_X(X)=\rho(X)\,dm_8(X),\qquad
 \rho(X)=\mathbb E_m[\Omega^2\mid X]>0,\quad \int\rho\,dm_8=1.
\tag{3}
\]

The smooth strictly positive \(\rho\) is gauge invariant under coarse-vertex transformations. The map

\[
J^{\Omega}:L^2(G^8,\rho\,dm_8)\longrightarrow L^2(G^E,\nu),\quad (J^{\Omega}f)(U)=f(X(U))
\]

is an **isometry**; its adjoint is interacting conditional expectation \(\mathsf P^\Omega f=\mathbb E_\nu[f\mid X]\), not free Haar expectation. It restricts to gauge-invariant observables. In the original physical Hilbert space, the corresponding isometry is \(f\mapsto\Omega\,f(X)\). It retains the physical vacuum because \(J^\Omega1=1\); hence

\[
Q^\Omega L\mathsf P^\Omega1=0.
\tag{4}
\]

**Critical correction to a tempting inference.** Bare Haar blocking gave \(B^*B=(\beta^2F/4)P\) and substantial bare vacuum mixing. Equation (4) says the **true-vacuum** projection has *zero* off-diagonal mixing on the vacuum. The two projections are different. It is logically invalid to promote the bare coefficient into an invariant lower bound for the physical renormalized influence. Conversely, (4) says **nothing** about the coupling of excited coarse observables.

## 3. Exact coarse generator, weighted kinetic form and its potential

Let \(m\) be the number of fine links in each original retained link product (\(m=1\) coarse, \(m=2\) fine), and put \(a=m\alpha\). Bi-invariance of the SU(2) metric gives \(|\nabla_{e_k}f(X)|^2=|\nabla_{X_i}f(X)|^2\) for each constituent link of a coarse product, with no extra shape factor. Integrating the untouched links yields, **exactly** for all smooth physical coarse functions,

\[
\mathcal E(J^\Omega f,J^\Omega g)
=a\sum_{i=1}^8\int_{G^8}
\langle\nabla_{X_i}f,\nabla_{X_i}g\rangle\,\rho\,dm_8.
\tag{5}
\]

The positive self-adjoint coarse form generator is therefore

\[
\boxed{A^\Omega=-a\sum_{i=1}^8\rho^{-1}\operatorname{div}_{X_i}(\rho\nabla_{X_i}),\qquad
 a_c=\alpha_h,\quad a_f=2\alpha_{h/2}.}
\tag{6}
\]

For a common reference Hilbert space \(L^2(G^8,dm_8)\), the unitary map \(f\mapsto\sqrt\rho\,f\) conjugates (6) into the exact Schrödinger-form operator

\[
\boxed{\widehat A^\Omega=a(-\Delta_X)+v_\rho(X),\qquad
 v_\rho=a\frac{\Delta_X\sqrt\rho}{\sqrt\rho},\qquad \Delta_X=\sum_{i=1}^8\Delta_{X_i}.}
\tag{7}
\]

The vacuum of this coarse operator is \(\sqrt\rho\), with zero energy. Thus even if the kinematic holonomy labels match, the physically relevant **coarse marginal density** and **induced potential** must be controlled across refinements.

With \(a_c=\tfrac{g_c^2}{2h}\) and \(a_f=2\tfrac{g_f^2}{2(h/2)}\), their exact diffusion ratio is

\[
\boxed{a_f/a_c=4(g_f/g_c)^2,\quad g_c=g_0(h),\quad g_f=g_0(h/2).}
\tag{8}
\]

A slowly running ultraviolet coupling may make \(g_f/g_c\) close to one, leaving a factor of approximately four **in this bare fixed-physical-time compression**. This is a diagnostic of missing physical rescaling/counterterms—not a no-go theorem for continuum Yang–Mills.

### Exact fixed-physical-support Wilson observable

For the same physical bottom loop \(C\) on both meshes let \(W(X)=\chi_1(X_1\cdots X_8)\). Set

\[
 m=\int W\rho\,dm_8,\quad \sigma^2=\int(W-m)^2\rho\,dm_8>0,\quad f=(W-m)/\sigma.
\]

This is an **explicitly specified** local gauge-invariant observable map on each finite interacting vacuum, with \(\|f\|_\rho=1\) and \(\langle1,f\rangle_\rho=0\). Its normalization depends on the unknown \(\rho\); no uniform nonzero variance has been proved. SU(2) character identities \(-\Delta\chi_1=\tfrac34\chi_1\) and \(|\nabla\chi_1|^2=1-\chi_1^2/4\) give the exact finite physical first spectral moment

\[
\boxed{-C_f'(0)=\mathcal E(f,f)=\frac{8a}{\sigma^2}\int_{G^8}
\left(1-\frac{W^2}{4}\right)\rho\,dm_8,
\qquad C_f(t)=\langle f,e^{-tL}f\rangle_\nu.}
\tag{9}
\]

This yields an **upper variational bound**, not a positive lower bound, on the physical excitation gap. No gap is inferred from the first moment alone.

## 4. The eliminated-sector influence is a conditional vacuum-score fluctuation

The coarse product electric Laplacian maps smooth \(f(X)\) to functions of \(X\). Consequently the \(Q^\Omega\)-component of (2) comes entirely from the interacting drift. Define

\[
S_f=\alpha\sum_{e\text{ in retained paths}}
\nabla_e\log\Omega\cdot\nabla_e f(X).
\]

For every smooth retained physical observable,

\[
\boxed{B^\Omega f\equiv Q^\Omega Lf=-2\big(S_f-\mathbb E_\nu[S_f\mid X]\big),\qquad
\|B^\Omega f\|^2=4\int \operatorname{Var}_\nu(S_f\mid X)\,d\nu_X.}
\tag{10}
\]

The conditional variance is a **precise observable-specific renormalization target**, unlike the bare global coefficient \(\beta^2F/4\). For \(f=1\) it vanishes exactly. For nonconstant Wilson observables it is generally nonzero. At fixed finite regulator it is finite because \(\Omega\) is positive smooth; no upper bound uniform in \(h,R\) is supplied.

For normalized \(f\), the exact initial curvature of its *actual interacting positive-time* spectral correlation obeys

\[
\boxed{C_f''(0)=\|A^\Omega f\|^2+\|B^\Omega f\|^2.}
\tag{11}
\]

Equation (11) exposes a second-time-moment contribution that the vacuum-matched Markovian compressed generator alone omits. It cannot be replaced with a gap conclusion.

## 5. A genuine full Schur complement, with correct unbounded-domain treatment

The vacuum-weighted P/Q split does **not** generally reduce the kinetic Laplacian; \(B^\Omega\) is a first-order differential operator and need not extend to a bounded operator on the entire coarse \(L^2\) space. Therefore the bounded-B block resolvent formula from the bare Haar decomposition **cannot simply be reused** without a domain proof.

A correct all-sector, all-energy finite-regulator replacement uses the closed Dirichlet form. For each \(z>0\) and smooth coarse function \(f\), define the **effective Schur form**

\[
\boxed{\mathfrak S_z(f)=\inf_{q\in Q^\Omega\cap H^1(G^E,\nu)}
\left\{\mathcal E(J^\Omega f+q,J^\Omega f+q)
+z\|J^\Omega f+q\|_\nu^2\right\}.}
\tag{12}
\]

This is the shorted form of \(L+z\) and identifies the *complete* compressed interacting resolvent, in the quadratic-form sense:

\[
\boxed{[\mathsf P^\Omega(L+z)^{-1}\mathsf P^\Omega]^{-1}=\mathfrak S_z}
\]

with the right side interpreted as the operator associated with the form (12) on the retained Hilbert space. Form domains are handled through completion and minimization; the infimum is attained at \(z>0\). Because \(q\perp J^\Omega f\) and \(\mathcal E\ge0\),

\[
 z\|f\|_\rho^2\le \mathfrak S_z(f)
 \le \mathcal E(J^\Omega f,J^\Omega f)+z\|f\|_\rho^2,
\qquad \mathfrak S_z(1)=z.
\tag{13}
\]

These finite exact bounds **do not exclude low physical excitation energies**. The next proof must estimate the difference of the entire shorted forms (or renormalized positive-time correlations) along \(h\to h/2\), uniformly in spatial volume, after a physically justified identification of their local observables.

### Explicit conditional two-scale resolvent comparison

Let \(\widehat A_i=a_iK_X+v_i\) be the two *compressed Markovian* coarse operators in the common Haar space from (7), with \(K_X=-\Delta_X\), smooth bounded real potentials \(v_i=a_i(\Delta_X\sqrt{\rho_i})/\sqrt{\rho_i}\), \(i=c,f\). For every fixed \(z>0\), the second resolvent identity and \(\widehat A_i\ge0\) give

\[
\boxed{
\| (\widehat A_f+z)^{-1}-(\widehat A_c+z)^{-1}\|
\le \frac{|a_f-a_c|}{z a_c}
\left(1+\frac{\|v_c\|_\infty}{z}\right)
+\frac{\|v_f-v_c\|_\infty}{z^2}.}
\tag{14}
\]

This is a **sufficient conditional stability inequality**, not a small-error finding: neither \(\|v_f-v_c\|\), a scale-matched kinetic coefficient nor the full Schur-form difference is controlled by existing cubic results. The true memory contribution (12) is an *additional* missing estimate.

## 6. Exact SU(2) finite gauge-graph counterexample: static and one-step agreement does not determine time correlations

This example is **not the cubic Wilson action**. It is an exact finite SU(2) **one-vertex/two-loop graph**, with independent loop holonomies \(A,B\in SU(2)\), local gauge transformations given by simultaneous conjugation, and the gauge-invariant retained character \(W=\chi_1(AB)\). Let

\[
\Omega_\kappa(A,B)=\frac{e^{\kappa\chi_1(A)/2}}{\sqrt{a_0(\kappa)}},\quad
 a_0(\kappa)=I_0(2\kappa)-I_2(2\kappa),
\]

and choose the **bounded gauge-invariant potential**

\[
V_\kappa(A)=\alpha\frac{\Delta_A\Omega_\kappa}{\Omega_\kappa}
=\alpha\left[-\frac{3\kappa}{8}\chi_1(A)
+\frac{\kappa^2}{4}\left(1-\frac{\chi_1(A)^2}{4}\right)\right].
\tag{15}
\]

The Hamiltonian \(H_\kappa=\alpha(-\Delta_A-\Delta_B)+V_\kappa(A)\) has ground state \(\Omega_\kappa\), ground energy zero, and is nonnegative by its ground-state transform. Add a scalar to (15) if a pointwise nonnegative potential convention is desired; the ground-subtracted dynamics are unchanged. Because \(B\) is independent Haar, \(X=AB\) has **exact Haar law for every \(\kappa\)**. The compressed generator on the \(X\) character algebra is exactly \(-2\alpha\Delta_X\), regardless of \(\kappa\).

The eliminated-sector influence on the gauge-invariant normalized \(W=\chi_1(X)\) nevertheless has the **strict positive** value

\[
\boxed{
\|B^\Omega W\|^2=
\frac{\alpha^2\kappa^2}{4}\,G(\kappa),\quad
G(\kappa)=\frac{3I_0(2\kappa)-4I_2(2\kappa)+I_4(2\kappa)}
{4[I_0(2\kappa)-I_2(2\kappa)]}>0.}
\tag{16}
\]

Indeed \(\mathbb E_\nu[\nabla\chi_1(A)\mid X]=0\) by conjugation symmetry, while \(\mathbb E_{X\sim\mathrm{Haar}}[\nabla_i\chi_1(X)\nabla_j\chi_1(X)]=\delta_{ij}/4\). Equation (16) follows from exact SU(2) character and Haar identities.

Now compare to the **one-link** free SU(2) coarse rotor with kinetic coefficient \(\alpha_c=2\alpha\). Both have identical \(\chi_1(X)\) distribution, normalized vacuum state, compressed generator, and initial correlation slope \(3\alpha/2\). Nevertheless, for every \(\kappa\ne0\) and every \(t>0\), strict scalar spectral Jensen implies

\[
\boxed{C_{\kappa}(t)>e^{-3\alpha t/2}=C_{\mathrm{free}}(t),
\qquad C_{\kappa}(t)-C_{\mathrm{free}}(t)=
\frac{\alpha^2\kappa^2G(\kappa)}8t^2+O(t^3).}
\tag{17}
\]

The strict inequality uses the positive nonzero variance of the full spectral measure: the coarse \(W\) is not an eigenvector of the interacting \(H_\kappa\). **Thus matching the complete static coarse probability law and the projected Markovian generator does not imply matching two-time correlators.** The time-memory term must be controlled independently. This theorem is about a specified finite SU(2) gauge graph, not an inferred continuum or quantum-gravity phenomenon.

The companion deterministic verifier checks (15)–(17), independent class-angle SU(2) Haar quadratures, irreducible Casimir/gradient identities by quaternion finite differences and the dyadic coefficient (8). In the illustrative choice \(\alpha=0.5,\kappa=1\), it finds \(G\approx0.6496911401\) and \(\|B^\Omega W\|^2\approx0.0406056963\) (independent integration error below \(10^{-14}\)).

## 7. What this closes and what it does not

**Finite theorem checkpoint obtained:** a true-vacuum-preserving gauge-invariant coarse observable representation on any finite SU(2) cubical regulator, the exact state-dependent Dirichlet generator and physical Wilson first moment, an exact conditional-score formula for eliminated-sector influence, a legitimate full energy-dependent **form** Schur complement, and a fully explicit SU(2) gauge-graph counterexample to discarding time memory merely because static coarse laws agree.

**Still OPEN:** computing or controlling \(\rho_{h,R}\), \(v_{h,R}\), the conditional score variance, the entire effective Schur form and long-physical-time connected correlations uniformly along \(g_0(h)\to0\), \(h\to0\), and spatial size \(R\to\infty\). No nontrivial 4D Osterwalder–Schrader limit, positive physical mass gap, genuine 3D Penrose-compatible operator or gravitational ultraviolet finiteness follows. Importantly, even after the finite vacuum-centering issue is resolved, a uniform **lower** spectral gap requires estimates far stronger than the first-moment and fixed-z resolvent comparisons above.

### Next falsifiable theorem target

For the same eight-holonomy physical loop on adjacent cubic refinements, establish physically normalized uniform estimates (in true interacting vacua) for the marginal densities \(\rho_{h,R}\) and their logarithmic derivatives, plus the **full** energy-dependent form \(\mathfrak S_{h,R,z}\), or else a common exponential physical-time bound for the normalized Wilson-centered correlations. In particular, a proposed scale estimate must account for both the induced coarse potential (7) and the eliminated-sector drift-variance/memory (10)–(12); static measure convergence or a first-time derivative match alone is mathematically insufficient.

### Prior source records (original scope preserved)

- `research/theorems/R3_FIXED_DOMAIN_CUBICAL_CHAIN_REFINEMENT_2026-10-31.md` (R3-IR-586), 3D geometric refinement;
- `research/theorems/R3_CUBICAL_SU2_GAUSS_HAMILTONIAN_REFERENCE_2026-10-31.md` (R3-IR-587), finite original-link Gauss Hamiltonian;
- `research/theorems/R3_CUBICAL_SU2_FINITE_TRANSFER_POSITIVITY_2026-10-31.md` (R3-IR-590), finite time transfer;
- `research/theorems/R3_FULL_WILSON_3D_SHELL_AND_TEMPORAL_MEMORY_2026-11-06.md` (draft PR #65), full spatial Wilson and temporal memory;
- `research/theorems/R3_EXACT_TWO_TIME_INFLUENCE_AND_DYADIC_SCALING_2026-11-06.md` (draft PR #66), bare P/Q influence and true 3D dyadic comparison.

**Review protocol:** mathematically separate the exact finite theorem from the demonstrative SU(2) two-loop counterexample and the unproved uniform physical continuum hypotheses. Archive numerical check files in Library; commit report, executable verification, JSON manifest, and source-qualified Observatory nodes in a private stacked draft PR. No public Pages or Git LFS changes.
