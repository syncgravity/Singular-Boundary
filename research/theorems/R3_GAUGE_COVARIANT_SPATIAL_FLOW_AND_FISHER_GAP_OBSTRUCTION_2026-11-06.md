# P2 / T2 · Gauge-covariant spatial Wilson-flow observables, a local Dirichlet test, and an exact Fisher–gap obstruction

**Dated:** November 6, 2026 (UTC)  
**Scope:** finite cubic SU(2) original-link models, exact Lie-group heat flow identities, and an independent compact SU(2) class-rotor counterexample.  
**Status:** proposed finite-model lemmas and an explicit *obstruction to an inference*. No 4D Yang–Mills continuum existence, positive mass gap, weak-bare-coupling uniformity, Penrose equivalence or physical quantum-gravity claim. Independent referee review pending.

## 1. Question, source fidelity and why this step matters

The immediately preceding finite cubic audit, `R3_LOCAL_INTERACTING_SU2_FISHER_AND_THERMODYNAMIC_SUBSEQUENCE_2026-11-06.md` (draft PR #69), establishes for the genuine interacting vacuum of a finite 3D open cubic SU(2) Wilson Hamiltonian that a simple physical-loop holonomy marginal obeys

\[
\int_{SU(2)}|\nabla\sqrt{\rho_{h,R}}|^2\,dU\le16/g_0(h)^4,
\]

independently of the number of edges around the loop and of the containing spatial box. The estimate supports fixed-\(h,g_0\) thermodynamic subsequences, but worsens as \(g_0(h)\to0\). The next desired theorem concerns renormalized/smeared, gauge-invariant observables at **fixed physical support**, a nontrivial physical-time limit, and complete interacting Schur forms.

The present work performs **three independent checks**:

1. It proves that even *uniformly bounded* Fisher information and strictly nonzero Wilson-trace variance do **not** imply a positive weighted SU(2) spectral gap. This shows exactly what cannot be inferred from the prior local estimate alone.
2. It rules out **single-holonomy group heat-convolution** as a substantive renormalization of a centered, variance-normalized fundamental Wilson trace: the observable is unchanged after normalization.
3. It constructs a genuine, finite, **gauge-equivariant spatial Wilson-action gradient flow** on a full 3D cubic link configuration, proves uniform-in-volume finite-flow-time stability and factorial quasi-locality, and supplies a model-specific covariance/Dirichlet matrix test that an interacting, renormalized observable must satisfy to obtain ultraviolet first-moment tightness. This is *not* the complete four-dimensional Wilson flow or a proof of the test at physical flow radius.

These checks distinguish **observation noise**, **finite gauge-field flow**, and **physical Euclidean-time quantum evolution**—three different mathematical operations.

## 2. Same original-link cubic source model

Let \(\Gamma_{h,R}=(V,E,F)\) be a finite oriented **open** 3D cubical complex, with every plaquette having four distinct links and every link belonging to at most four plaquettes. Choose the bi-invariant SU(2) metric normalized by

\[
C=-\Delta,\qquad C\chi_n=\frac{n(n+2)}4\chi_n,\qquad \chi_1(U)=\mathrm{tr}_{\mathbf2}U.
\]

The quantum Hamiltonian on the gauge-invariant sector of \(L^2(SU(2)^E,d\mu)\) is

\[
H_{h,R}=\alpha_h\sum_e C_e+\beta_h\sum_p\left(1-\frac12\chi_1(U_p)\right),
\quad \alpha_h=\frac{g_0(h)^2}{2h},\quad\beta_h=\frac2{g_0(h)^2 h}.
\]

At each **finite** regulator the unique strictly positive gauge-invariant ground state \(\Omega_{h,R}\) defines \(d\nu_{h,R}=\Omega_{h,R}^2d\mu\). Its ground-state transformed, nonnegative generator \(L=\Omega^{-1}(H-E_0)\Omega\) has the closed Dirichlet form

\[
\mathcal E_{h,R}(f,g)=\alpha_h\sum_{e\in E}
\int\langle\nabla_e f,\nabla_e g\rangle\,d\nu_{h,R}.
\]

No uniform spectral gap for this generator is assumed. In particular, the finite positive vacuum is an input established in PR #67, not the desired continuum vacuum.

## 3. A compact SU(2) counterexample: bounded Fisher and nonzero variance but an arbitrarily small gap

**Proposition A (exact gauge-invariant class rotor counterexample).** Put \(x(U)=\chi_1(U)/2\in[-1,1]\). With normalized Haar measure \(dU\), \(\int x^2dU=1/4\), \(\int x^4dU=1/8\), and \(|\nabla x|^2=(1-x^2)/4\). For \(\varepsilon>0\), set

\[
Z_\varepsilon=\tfrac14+\varepsilon^2,\qquad
\rho_\varepsilon(U)=\frac{x(U)^2+\varepsilon^2}{Z_\varepsilon},\qquad
\Omega_\varepsilon=\sqrt{\rho_\varepsilon}.
\]

Each \(\rho_\varepsilon\) is smooth, everywhere positive, conjugation-invariant and normalized. Its square-root Fisher energy and Wilson-trace variance satisfy

\[
\boxed{\int|\nabla\sqrt{\rho_\varepsilon}|^2dU\le\frac34,\qquad
 \operatorname{Var}_{\rho_\varepsilon}(\chi_1)
 =\frac{\tfrac12+\varepsilon^2}{\tfrac14+\varepsilon^2}\ge1.}
\tag{A1}
\]

Nevertheless the self-adjoint, nonnegative class-rotor generator

\[
L_\varepsilon=-\rho_\varepsilon^{-1}\operatorname{div}(\rho_\varepsilon\nabla)
\]

on \(L^2(SU(2),\rho_\varepsilon dU)\) has a strictly positive but nonuniform first nonzero **class-sector** eigenvalue with

\[
\boxed{0<\lambda^{\mathrm{class}}_1(L_\varepsilon)\le\varepsilon.}\tag{A2}
\]

For each \(\varepsilon>0\), this is the ground-state transform of a *genuine finite smooth SU(2) class-rotor Hamiltonian*

\[
H_\varepsilon=-\Delta+V_\varepsilon,\qquad
V_\varepsilon(x)=\frac{\varepsilon^2(1-x^2)}{4(x^2+\varepsilon^2)^2}
 -\frac{3x^2}{4(x^2+\varepsilon^2)},\quad H_\varepsilon\Omega_\varepsilon=0.
\]

Its potential is bounded and smooth for every fixed \(\varepsilon\), but the potential barrier at the SU(2) equator \(x=0\) grows like \(1/(4\varepsilon^2)\). **This potential is not the cubic Wilson magnetic potential.** Consequently this is a counterexample to an *invalid inference from static bounds*, not a counterexample to the Yang–Mills mass-gap conjecture.

**Proof.** As \(|\nabla x|^2=(1-x^2)/4\),

\[
\int|\nabla\sqrt{\rho_\varepsilon}|^2 dU
=\frac1{4Z_\varepsilon}\int
\frac{x^2(1-x^2)}{x^2+\varepsilon^2}dU
\le\frac{3/16}{Z_\varepsilon}\le\frac34.
\]

The trace mean vanishes by \(x\mapsto-x\) parity, and \(\int x^4dU=1/8\) gives the stated variance. For the smooth odd class test function

\[
f_\varepsilon(U)=\frac{x(U)}{\sqrt{x(U)^2+\varepsilon^2}},
\]

\(\int f_\varepsilon\rho_\varepsilon dU=0\) and \(\operatorname{Var}_{\rho_\varepsilon}(f_\varepsilon)=1/(4Z_\varepsilon)\). Haar's one-dimensional trace density is \(p_0(x)=2\sqrt{1-x^2}/\pi\le2/\pi\). Therefore

\[
\begin{split}
\mathcal E_\varepsilon(f_\varepsilon)
 &=\frac{\varepsilon^4}{4Z_\varepsilon}\int_{-1}^1
 \frac{1-x^2}{(x^2+\varepsilon^2)^2}p_0(x)dx\\
 &\le\frac{\varepsilon^4}{4Z_\varepsilon}\frac2\pi
 \int_{\mathbb R}\frac{dx}{(x^2+\varepsilon^2)^2}
 =\frac{\varepsilon}{4Z_\varepsilon}.
\end{split}
\]

The Rayleigh quotient is thus at most \(\varepsilon\). Strict positivity of \(\lambda_1\) at each fixed \(\varepsilon\) follows from uniform ellipticity/compactness and strictly positive smooth density. The class radial Laplace–Beltrami formula \(\Delta f(x)=[(1-x^2)f''(x)-3xf'(x)]/4\) gives \(V_\varepsilon=\Delta\Omega_\varepsilon/\Omega_\varepsilon\), so \(H_\varepsilon\) is nonnegative with unique positive vacuum by its ground-state quadratic-form identity. QED.

**Necessary lesson.** A coupling-uniform version of the previous cubic Fisher estimate, **even if supplemented by positive Wilson variance**, would not by itself deliver infrared spectral exclusion. The actual cubic Wilson dynamics, their interacting effective Schur forms, and physical-time estimates remain mathematically necessary.

## 4. A heat-smearing no-go for the fundamental loop

Let \(P_s^{\mathrm{grp}}=e^{s\Delta_{SU(2)}}\), acting by SU(2) heat convolution on functions **of a single loop holonomy**. The fundamental character is a Laplace eigenfunction:

\[
\boxed{P_s^{\mathrm{grp}}\chi_1=e^{-3s/4}\chi_1.}\tag{H1}
\]

For *any* true interacting marginal \(\rho_{h,R}\), any \(s<\infty\), and any nonzero variance, the normalized, centered deterministic observable obeys **exactly**

\[
\boxed{\frac{P_s^{\mathrm{grp}}\chi_1-\mathbb E_\rho(P_s^{\mathrm{grp}}\chi_1)}{
\sqrt{\operatorname{Var}_\rho(P_s^{\mathrm{grp}}\chi_1)}}=
\frac{\chi_1-\mathbb E_\rho\chi_1}{\sqrt{\operatorname{Var}_\rho\chi_1}}.}\tag{H2}
\]

Therefore group heat smoothing of **this one character** is merely a nonzero scalar multiplication and cannot alter its normalized physical-time correlations or the prior raw first-moment mismatch. This is exact; no statistical calculation is required.

Smoothing the **distribution** is different: if an independent SU(2) heat variable is added to the holonomy readout, the observed density is \(P_s^{\mathrm{grp}}\rho\). In the countermodel of Proposition A,

\[
\rho_\varepsilon=1+\frac1{1+4\varepsilon^2}\chi_2,
\quad P_s^{\mathrm{grp}}\rho_\varepsilon
=1+\frac{e^{-2s}}{1+4\varepsilon^2}\chi_2
\ge1-e^{-2s}>0.\tag{H3}
\]

It is a uniformly smooth positive **noisy marginal**, but its smoothing comes from an auxiliary measurement channel, not from the original quantum Hamiltonian or a renormalized gauge field. It cannot certify a Yang–Mills continuum vacuum, even when it produces perfectly controlled static density bounds.

## 5. An actual gauge-equivariant spatial Wilson-action flow

Define the spatial Wilson functional on the full finite link configuration manifold \(\mathcal M=SU(2)^E\):

\[
S_W(U)=\sum_{p\in F}\left(1-\tfrac12\chi_1(U_p)\right).
\]

For dimensionless *spatial* flow time \(s\ge0\), solve the smooth finite-dimensional ODE

\[
\boxed{\frac{d}{ds}\Phi_s(U)=-\nabla S_W(\Phi_s(U)),\qquad\Phi_0(U)=U.}\tag{W1}
\]

This is a deterministic flow **of gauge fields, not heat noise on an observed loop**, and not the Euclidean-time quantum semigroup \(e^{-t(H-E_0)}\). The standard Wilson/gradient-flow program motivates flow-time observables [Lüscher 2010, JHEP 08 (2010) 071, DOI 10.1007/JHEP08(2010)071], but this *spatial* 3D finite construction must not be identified with the complete 4D gradient-flow continuum theory.

**Proposition B (finite gauge flow, stability and quasilocality).** On every finite open cubic complex as above:

1. \(\Phi_s\) exists uniquely and smoothly for all finite \(s\in\mathbb R\), and is a diffeomorphism of \(\mathcal M\). The spatial Wilson action decreases: \(dS_W(\Phi_sU)/ds=-\|\nabla S_W\|^2\le0\). The flow commutes with every local SU(2) gauge transformation, so \(W_{C,s}(U):=\chi_1(U_C(\Phi_sU))\) is gauge invariant for every closed loop \(C\).
2. Its Hessian has a **volume-independent operator norm bound**

   \[
   \boxed{\|\operatorname{Hess}S_W(U)\|_{\mathrm{op}}\le4,\qquad
   \|D\Phi_s(U)\|_{\mathrm{op}}\le e^{4|s|}.}\tag{W2}
   \]

3. Let two configurations agree on every link whose plaquette-adjacency distance from the links of \(C\) is strictly less than \(r\). Then, writing \(L_C\) for the number of original links in \(C\),

   \[
   \boxed{|W_{C,s}(U)-W_{C,s}(V)|
   \le2\pi L_C\,\sum_{k\ge r}\frac{(4s)^k}{k!},\qquad s\ge0.}\tag{W3}
   \]

   This bound is **independent of the total box volume**, at fixed lattice flow time \(s\); it decays factorially in the lattice distance \(r\). The coefficient \(2\pi\) is an upper bound on the geodesic diameter of SU(2) with the stated Casimir normalization.
4. For the *actual* interacting Wilson vacuum at this regulator, its raw Dirichlet energy satisfies

   \[
   \boxed{\mathcal E_{h,R}(W_{C,s},W_{C,s})
     \le \alpha_h L_C e^{8s}.}\tag{W4}
   \]

**Proof.** Smoothness/compactness give global finite-time flow. Gauge transformations act isometrically on \(SU(2)^E\), preserve \(S_W\), and hence commute with its gradient flow by uniqueness. For the Hessian, use orthonormal Lie algebra generators \(T_a=i\sigma_a/2\), whose operator norm is \(1/2\). On a face with distinct links, the second derivative of \(-\frac12\mathrm{tr}\) in arbitrary link directions \((v_e)_{e\in\partial p}\) has absolute value at most

\[
\frac14\left(\sum_{e\in\partial p}\|v_e\|\right)^2
\le\sum_{e\in\partial p}\|v_e\|^2.
\]

Summing over plaquettes and using \(d(e)\le4\) yields \(|\operatorname{Hess}S_W(v,v)|\le4\|v\|^2\). Parallel-transported derivatives of the flow obey the variational equation \(J'=-HJ\), proving (W2) by Grönwall. Moreover, each Hessian block for two links of the same plaquette has norm at most \(1/4\); hence the matrix of blockwise norms has row sums at most four and vanishes between links not sharing a plaquette. Expanding the time-ordered variational equation, any path from a contour edge to an edge at graph distance at least \(r\) contains at least \(r\) Hessian factors; the *total row mass* of such paths is bounded by \(\sum_{k\ge r}(4s)^k/k!\). Integrate this derivative estimate along a product geodesic interpolating the two configurations, moving each exterior SU(2) link by at most \(2\pi\). The loop trace gradient on each of its original links has norm at most one, giving (W3). Finally \(\sum_{e}|\nabla_e W_C|^2=L_C(1-W_C^2/4)\le L_C\) for a simple loop, and the flow Jacobian bound gives \(\sum_e|\nabla_e W_{C,s}|^2\le e^{8s}L_C\). Integrate against *any* normalized probability, in particular the interacting vacuum, to obtain (W4). QED.

**Boundary of this result.** A fixed physical smoothing radius would conventionally require dimensionless flow time growing like \(s=t_{\mathrm{phys}}/h^2\); the crude derivative bound then becomes \(\alpha_h L_C\exp(8t_{\mathrm{phys}}/h^2)\), and the factorial locality bound is not uniform for a fixed physical neighborhood. **This is a failure of these sufficient worst-case estimates, not evidence that the actual flowed observables diverge.** Better diffusive/off-diagonal bounds and true-vacuum renormalization are required. Our spatial flow does not include temporal plaquettes; 4D gradient-flow equivalence is a distinct open problem.

### Exact isolated-plaquette gauge-field flow (nontrivial test)

On a single isolated square with four distinct original links, put \(x=\frac12\mathrm{tr}U_p\). For the flow (W1), the exact loop evolution is

\[
\boxed{\dot x=1-x^2,\qquad
x(s)=\frac{x(0)+\tanh s}{1+x(0)\tanh s}.}\tag{W5}
\]

Unlike group heat convolution, this gauge-field flow is a **nonlinear transformation** of the Wilson loop. At a free Haar reference state, the normalized physical-time first Dirichlet moment of the four-link flowed trace (in units \(\alpha_h=1\)) starts at 3, then has values approximately 3.114 at \(s=0.3\) and 3.901 at \(s=0.8\). This finite control demonstrates that flowing the gauge field need not automatically lower the normalized short-time spectral moment. It does *not* model an interacting 3D Wilson vacuum.

## 6. The actual observable-level P2/T2 test: covariance versus Dirichlet form

Let \(\Phi_{1,h},\ldots,\Phi_{m,h}\) be any *real*, smooth, gauge-invariant, finite-regulator observables with physical supports and normalization conventions specified—e.g. a finite family of flowed Wilson loops at a common **physical** flow radius. They may depend on the entire link configuration through a gauge-field flow. Under the actual interacting vacuum \(\nu_{h,R}\), define symmetric positive semidefinite matrices

\[
S_{ij}^{(h,R)}=\operatorname{Cov}_{\nu_{h,R}}(\Phi_i,\Phi_j),\qquad
G_{ij}^{(h,R)}=\sum_e\int\langle\nabla_e\Phi_i,\nabla_e\Phi_j\rangle\,d\nu_{h,R}.
\]

For any weights \(a\) with \(a^\top Sa>0\), the centered variance-normalized state \(f_a=a\cdot(\Phi-\mathbb E\Phi)/\sqrt{a^\top Sa}\) obeys the **exact** first physical-time moment identity

\[
\boxed{-\frac{d}{dt}\langle f_a,e^{-tL}f_a\rangle\big|_{t=0}
=\alpha_h\frac{a^\top Ga}{a^\top Sa}.}\tag{D1}
\]

The best initial-time *UV moment* in the chosen finite observable span is therefore the smallest generalized eigenvalue of the positive form pair \((\alpha_h G,S)\), restricting to \(a^\top Sa>0\). At fixed \(h,R\), no unknown nonperturbative dynamics is hidden in the identity; the difficult part is bounding \(S,G\) for the **true** interacting \(\nu_{h,R}\) uniformly along the weak-bare-coupling trajectory.

**Conditional UV compactness criterion (not an IR gap criterion).** If a sequence of such normalized observables admits a scale-independent bound \(\alpha_h(a_h^\top G_h a_h)/(a_h^\top S_h a_h)\le M\), then their normalized positive spectral measures have first moments at most \(M\), hence \(\sigma_h([E,\infty))\le M/E\); subsequences converge weakly and their positive-time correlations are equicontinuous at zero. This does **not** prove the spectral measures exclude \((0,M_0)\) for any \(M_0>0\), nor does it produce an OS 4D physical Hilbert space or nontrivial interacting continuum field.

**Haar baseline/no-go for one-holonomy observables.** If the reference state is *exactly product Haar* (the free electric limit), then every centered nonconstant function of one simple \(L_C\)-link holonomy satisfies the SU(2) Poincaré inequality

\[
\boxed{\frac{-C_f'(0)}{\alpha_h}
 =L_C\frac{\int|\nabla f|^2dU}{\operatorname{Var}_{\mathrm{Haar}}f}
\ge\frac34 L_C.}\tag{D2}
\]

For \(f=\chi_1\), equality holds, and the four-link Haar matrices for \(\chi_1,\chi_2\) are \(S=I_2\), \(G=\mathrm{diag}(3,8)\), confirming the generalized-eigenvalue test. Likewise, an average of pairwise edge-disjoint independent Haar loops cannot improve the minimum \(\frac34\alpha_h L_{\min}\) by scalar weights alone. This is **conditional on the Haar reference state**; it is not a theorem on the true weak-bare-coupling Wilson vacuum.

## 7. Executable independent checks

The companion program `research/scripts/verify_spatial_wilson_flow_2026_11_06.py` performs:

- independent SU(2) Weyl/quadrature normalization and exact class-rotor \(H_\varepsilon\Omega=0\) checks; adaptive integration of Fisher, trace variance, and Rayleigh quotients down to \(\varepsilon=0.002\), retaining the analytic \(\lambda_1\le\varepsilon\) bound;
- a 58-character Peter–Weyl heat-kernel convolution test at three positive times, showing both the fundamental multiplier and the adjoint-density multiplier;
- exact SU(2) character covariance and Dirichlet matrices \(S=I_2\), \(G_{4\mathrm{link}}=\mathrm{diag}(3,8)\) under Haar;
- an independently constructed open \(2\times2\times1\) cubic spatial geometry with 18 vertices, 33 original links, 20 faces, maximum link incidence four; randomized Hessian directional checks against the proven volume-independent constant four;
- quaternion SU(2) checks of exact gauge covariance of the spatial force and numeric integration of the isolated plaquette flow versus (W5);
- independent SU(2) Haar quadrature of the normalized first-moment ratio of flowed isolated plaquette Wilson traces, and the factorial sensitivity-bound values.

All executable tests serve as consistency checks. The exact statements are established by the variational, Lie-group, flow-Jacobian and harmonic-analysis arguments—not by finite sampling.

## 8. Refined open proof obligation (next mathematical target)

This checkpoint does **not** eliminate \(g_0(h)^{-4}\) in the *actual interacting cubic Wilson vacuum*, does not prove the flowed observable has nonzero uniformly controlled variance, and does not control its full physical-time Schur/influence kernel.

A viable next P2/T2/T3 subtheorem must state explicitly:

1. A gauge-equivariant, spatially localized **four-dimensional physically normalized** flowed/smeared Wilson observable \(\Phi_{h,R,t_{\mathrm{phys}}}\), with physical support and a common comparison dictionary for adjacent cubic meshes; the three-dimensional spatial flow above is a finite **candidate/control**, not the finished 4D field.
2. A *noncircular* estimate on the true Wilson-vacuum covariance \(S_{h,R}\), Dirichlet form \(G_{h,R}\), and the complete energy-dependent shorted/Schur form, uniform for \(h\to0\), increasing \(R\), and the correct running bare coupling.
3. Long physical-time positive spectral exclusion for a dense family of gauge-invariant probes, not just finite first-moment tightness; nontrivial OS reconstruction; then an independently justified transfer from cubic to source-certified 3D quasicrystalline geometry.

**Every P0–P5 continuum Yang–Mills gate, the T0–T5 Penrose transfer, and the distinct gravitational ultraviolet physical-operator problem remain OPEN.** No main-branch scientific gate is promoted by this finite checkpoint.

### Source/provenance

- Original local finite Wilson Fisher theorem, `research/theorems/R3_LOCAL_INTERACTING_SU2_FISHER_AND_THERMODYNAMIC_SUBSEQUENCE_2026-11-06.md` (stacked PR #69).
- True finite interacting vacuum and Schur-form program, `research/theorems/R3_VACUUM_WEIGHTED_OBSERVABLE_MAP_AND_SCHUR_FORM_2026-11-06.md` (draft PR #67).
- Exact Wilson first-moment formula, `research/theorems/R3_FINITE_WILSON_MARGINAL_HARNACK_AND_TWO_SCALE_SUM_RULE_2026-11-06.md` (draft PR #68).
- Martin Lüscher, *Properties and uses of the Wilson flow in lattice QCD*, JHEP 08 (2010) 071, DOI [10.1007/JHEP08(2010)071](https://doi.org/10.1007/JHEP08(2010)071), for the **established research motivation** for gauge-field flow, not for the new finite estimates or SU(2) class counterexample.
