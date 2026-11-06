# R3 / P2–T2 · Nonlinear fixed-physical-time smoothing in an exactly invariant planar Cartan sector of the cubic SU(2) Wilson flow

**Date:** November 6, 2026. **Research status:** rigorous *conditional classical* spatial-flow theorem for an exactly invariant, commuting SU(2) subgroup embedded in the **original three-dimensional open cubic** model, plus independent numerical verification. It is **not** a theorem for generic noncommuting SU(2) connections, the true interacting Wilson quantum vacuum, a 4D Euclidean quantum field theory, the Yang–Mills mass gap, Penrose transfer, or gravitational ultraviolet finiteness. **All P0–P5 and T0–T5 gates remain OPEN.** Independent mathematical review pending.

**Parent:** draft PR #72, `R3_NONLINEAR_CUBIC_PHYSICAL_ENERGY_DISSIPATION_2026-11-06.md`; earlier PR #71 establishes physical-radius smoothing only for the flat-field linearization. The present result proves **positive-physical-time nonlinear curvature smoothing**, but only on a highly restricted invariant (Abelian/Cartan) subset, with an explicit admissibility condition. Crucially, this subset has **zero product-Haar measure** in the full SU(2) configuration space, hence zero measure under the strictly positive finite interacting Wilson vacuum.

## 1. Full 3D original-link SU(2) construction; exactly invariant subset

Let the physical domain be the open cubical unit box, mesh size \(h=1/n\), with \(n\) spatial cubic cells per side and original-link configuration manifold \(SU(2)^{E_h}\). Retain the previous normalization \(T_a=i\sigma_a/2\), \(S_h(U)=\sum_p[1-\frac12\operatorname{tr}U_p]\), \(\mathscr E_h=8S_h/h\), and full *classical spatial* SU(2) gradient flow \(\frac{d}{ds}U_s=-\nabla S_h(U_s)\), \(\tau=h^2s\). The covariant flow acts on all three spatial link directions and **is not** quantum physical time.

Restrict **initial** configurations as follows: every x/y oriented link is an element \(\exp(\theta_e T_3)\) of the **same fixed Cartan \(U(1)\subset SU(2)\)**; its angle is independent of the z-coordinate; and every z-oriented link is the identity. The xy faces in all \(n+1\) layers carry an identical Abelian flux. Every xz/yz plaquette is exactly the identity.

**Lemma 1 (nonlinear invariance).** This subset is invariant under the **full** finite SU(2) cubic gradient flow. Indeed, all plaquette derivatives in the Cartan configuration lie in the Cartan direction; every vertical face has exactly zero Wilson force at the identity; the x/y forces at corresponding edges in successive z layers are identical. Uniqueness of the finite smooth ODE then preserves all these properties for every finite flow time. This is an *exact embedded nonlinear SU(2) solution class*, not an approximation to noncommuting fields.

Write \(B\) for the oriented open \(n\times n\) **two-dimensional** edge-to-face incidence map on one xy layer. Its plaquette fluxes are \(b=B\theta\), with \(q=b/2\) (a real lift, with no modulo-\(2\pi\) winding ambiguity); put \(L=BB^\top\). Every face has four edges, so on the dual face square grid \(L\) is the nearest-neighbor positive Dirichlet Laplacian: diagonal 4 and off-diagonal \(-1\) for neighboring faces. The exact Wilson flow reduces to

\[
\boxed{\dot\theta=-\tfrac12B^\top\sin q,\qquad
\dot q=-\tfrac14L\sin q.}\tag{1}
\]

The physical (Abelian) plaquette curvature and physical flow time are

\[
F_h=\frac{b}{h^2}=\frac{2q}{h^2},\qquad \tau=h^2s,
\quad\boxed{\partial_\tau F_h=-\frac1{2h^4}L\sin\left(\frac{h^2F_h}{2}\right).}\tag{2}
\]

The full 3D energy of this embedded sector counts the **\(n+1\) identical xy layers**:

\[
\boxed{\mathscr E_h=\frac{8(n+1)}h\sum_{p\in\mathrm{xy\ faces}}(1-\cos q_p).}\tag{3}
\]

No physical curvature field is defined by a naive unwrapped Abelian plaquette angle unless the lift is specified. We impose the **non-winding admissibility condition** \(\delta_0:=\max_p|q_p(0)|<\pi/2\) so \(\sin q\) remains monotone on the whole solution range.

## 2. Exact maximum principle and uniformly elliptic nonlinear conductances

**Theorem 2 (nonlinear maximum principle).** For initial \(|q_p(0)|\le\delta_0<\pi/2\), one has for all \(\tau\ge0\)

\[
\boxed{\max_p|q_p(\tau)|\le\delta_0,\qquad
\|F_h(\tau)\|_\infty\le\|F_h(0)\|_\infty.}\tag{4}
\]

*Proof.* A positive maximum of \(q\) in (1) has a nonpositive derivative because \((L\sin q)_p=4\sin q_p-\sum_{r\sim p}\sin q_r\ge0\), with missing neighbors treated as Dirichlet exterior value 0. The negative minimum has a nonnegative derivative. \(\sin\) is increasing on \([-\delta_0,\delta_0]\). The finite-dimensional comparison principle closes the invariant interval. \(F=2q/h^2\) proves the second claim. \(\square\)

For each dual edge, including edges to the Dirichlet exterior (where \(q_{\rm ext}=0\)), define the divided-difference conductance

\[
c_e(\tau)=\begin{cases}
[\sin q_p-\sin q_r]/(q_p-q_r),&q_p\ne q_r,\\
\cos q_p,&q_p=q_r,
\end{cases}\qquad\boxed{\kappa:=\cos\delta_0\le c_e(\tau)\le1.}\tag{5}
\]

This is **not** a constant-coefficient linearization: the \(c_e\) depend nonlinearly on the full evolving field. Nevertheless, with \(D_c(\tau)=\operatorname{diag}(c_e(\tau))\), the exact nonlinear evolution can be written, along its particular trajectory, as the **time-dependent uniformly elliptic graph heat equation**

\[
\boxed{\partial_\tau F_h=-\frac1{4h^2}B D_c(\tau)B^\top F_h.}\tag{6}
\]

Each instantaneous generator is symmetric, has nonnegative off-diagonal entries in the heat operator and nonpositive row/column sums (Dirichlet killing at the exterior). Its non-autonomous propagator is positive and contractive in the physical \(L^1\) and \(L^\infty\) norms. Its adjoint propagator is associated with the same bounds for time-reversed conductances. No commuting-in-time assumption is made.

## 3. Actual positive-physical-time \(L^2\to L^\infty\) curvature smoothing from bounded 3D initial energy

Define \(\|F\|_{p,h}=(h^2\sum_p|F_p|^p)^{1/p}\), \(\|F\|_{\infty}=\max_p|F_p|\), \(H_h=\|F_h\|_{2,h}^2/2\). A universal dimension-two Dirichlet **discrete Nash constant** \(C_N<\infty\), independent of n, satisfies

\[
\boxed{\|v\|_{2,h}^{4}\le C_N\|v\|_{1,h}^{2}\|B^\top v\|_2^2.}\tag{7}
\]

To see mesh independence, extend a finite face-grid function by zero to \(\mathbb Z^2\) and use the standard \(\mathbb Z^2\) Nash inequality (obtainable by low/high frequency decomposition of the 2D discrete Fourier transform). Scaling both its \(\ell^1\) and \(\ell^2\) norms by the physical cell area \(h^2\) yields exactly (7). The edge energy is the full dual Dirichlet form, including the exterior boundary edges.

**Theorem 3 (positive-flow-time nonlinear smoothing).** Under Lemma 1 and \(\delta_0<\pi/2\), for every \(\tau>0\)

\[
\boxed{\|F_h(\tau)\|_\infty\le
 \sqrt{\frac{2C_N}{\kappa\tau}}\,\|F_h(0)\|_{2,h}.}\tag{8}
\]

*Proof.* Freeze the actual measurable conductance trajectory \(c_e(\tau)\). For its positive evolution operator \(U(t,s)\), the \(L^1\)-contraction and (7) imply, with \(y=\|U(t,s)v\|_{2,h}^2\),

\[
y'(t)=-\frac12\sum_e c_e(t)|B^\top U(t,s)v|_e^2
\le-\frac{\kappa}{2C_N\|v\|_{1,h}^2}y(t)^2.
\]

Hence \(\|U(t,s)\|_{1\to2}\le\sqrt{2C_N/(\kappa(t-s))}\). The time-reversed adjoint equation has symmetric generators with the *same* conductance bounds and \(L^1\)-contractivity, so by duality \(\|U(t,s)\|_{2\to\infty}\le\sqrt{2C_N/(\kappa(t-s))}\). Taking \(s=0\) proves (8). This argument remains valid for **time-dependent nonlinear conductances**; it does not pretend the overall solution map is linear. \(\square\)

Now impose the **separate classical** initial energy bound \(\mathscr E_h(U_h(0))\le M\), with an admissible flux lift. For \(|q|\le\pi/2\), the elementary lower bound \(1-\cos q\ge 2q^2/\pi^2\) and the layer count (3) give

\[
\boxed{\|F_h(0)\|_{2,h}\le\frac\pi2\sqrt M,\qquad
\delta_0\le\frac\pi4\sqrt{\frac{Mh}{n+1}}\le\frac\pi4 h\sqrt M.}\tag{9}
\]

In particular, when \(h\sqrt M\le1\), \(\kappa\ge1/\sqrt2\) and (8) becomes a **mesh-, volume-, and loop-count-independent bound at every fixed positive physical flow time**:

\[
\boxed{\|F_h(\tau)\|_\infty
\le\frac\pi2\sqrt{\frac{2C_N M}{\kappa\tau}}
\le\frac\pi2\sqrt{\frac{2\sqrt2 C_N M}{\tau}}.}\tag{10}
\]

This controls **positive-time curvature amplitude even when initial physical curvature is concentrated and unbounded**. The conclusion is valid only within the invariant planar Cartan lift and does not apply to generic 3D noncommuting SU(2) configurations or to the interacting quantum vacuum.

## 4. Physical gradient dissipation and an all-time O(h²) nonlinear-to-Maxwell comparison

**Theorem 4 (physical gradient integral).** Under the same assumptions,

\[
\boxed{H_h(\tau)+\frac\kappa4\int_0^\tau
 \|B^\top F_h(t)\|_2^2dt\le H_h(0).}\tag{11}
\]

*Proof.* Multiply (6) by \(h^2F\). The exact energy derivative is \(H'_h=-\frac14\langle B^\top F,D_c B^\top F\rangle\le-\frac\kappa4\|B^\top F\|^2\). Integrate. \(\square\)

Let \(F_h^{\rm lin}(\tau)=\exp[-\tau L/(4h^2)]F_h(0)\) solve the exact **flat Abelian** physical curvature heat equation on the *same* finite open grid. Let \(\eta=1-\kappa\). Along the full nonlinear trajectory the coefficient perturbation is \(0\le I-D_c\le\eta I\). A direct difference-energy/Young inequality combined with (11) gives the **all-positive-time**, mesh-independent comparison

\[
\boxed{\|F_h(\tau)-F_h^{\rm lin}(\tau)\|_{2,h}
\le\frac{\eta}{\sqrt{2\kappa}}\|F_h(0)\|_{2,h},\quad \tau\ge0.}\tag{12}
\]

*Proof details.* Set \(w=F_h-F_h^{\rm lin}\). Then
\(\partial_\tau w=-Lw/(4h^2)-B(D_c-I)B^\top F_h/(4h^2)\).
For \(Y=\|w\|_{2,h}^2\), Cauchy–Schwarz/Young gives
\(Y'\le-\frac14\|B^\top w\|^2+\frac{\eta^2}4\|B^\top F_h\|^2\). Since \(Y(0)=0\) and \(\int\|B^\top F_h\|^2\le4H_h(0)/\kappa=2\|F_h(0)\|_{2,h}^2/\kappa\), (12) follows. \(\square\)

With bounded total initial 3D action, (9) implies \(1-\kappa\le\delta_0^2/2=O(Mh^2)\), hence **even for initially concentrated physical curvature** the nonlinear-versus-linear physical \(L^2\) error is \(O(h^2M^{3/2})\), **uniformly for every \(\tau\ge0\)**. This convergence applies to the **embedded Cartan sector**, not to full non-Abelian Yang–Mills.

If one additionally assumes \(\|F_h(0)\|_\infty\le K\) independent of mesh, the elementary Taylor bound \(|\sin z-z|\le |z|^3/6\), \(\|L\|_{\infty\to\infty}\le8\), and the sub-Markov linear semigroup yield the complementary *pointwise* comparison

\[
\boxed{\|F_h(\tau)-F_h^{\rm lin}(\tau)\|_\infty
\le\frac{\tau h^2K^3}{12}.}\tag{13}
\]

The stronger initial \(K\)-bound is **not** assumed in Theorem 3 or the \(L^2\) comparison (12). These formulas show exactly which nonlinear corrections disappear in the smooth Maxwell/Cartan continuum regime.

## 5. Realizable concentrated flux and why it does not solve interacting Yang–Mills

For an open planar grid, \(B\) has full row rank (the disk has no nonzero closed 2-cycles). Thus any prescribed lifted face flux \(b\) is realized by **actual link variables** \(\theta=B^\top (BB^\top)^{-1}b\). Choose a single face \(p_*\) with \(q_{p_*}(0)=h\), all other \(q_p(0)=0\), and repeat the resulting Cartan link configuration across the z layers. Then

\[
\boxed{\mathscr E_h(0)=\frac{8(n+1)}h(1-\cos h)\to4,\quad
\|F_h(0)\|_\infty=\frac2h\to\infty.}\tag{14}
\]

Nevertheless Theorem 3 bounds \(\|F_h(\tau)\|_\infty\le C\sqrt{4/\tau}\) for each fixed \(\tau>0\); the numerical verifier checks physical fixed-time smoothing and the stronger \(L^2\) comparison on this exact realizable concentrated-flux family. This is a **positive-time nonlinear regularization result for a genuinely initial-curvature-concentrated embedded configuration**.

**Absolute scope boundary.** The invariant configurations lie in one fixed maximal torus of SU(2) on the original x/y links and have trivial z links. This has **zero product-Haar measure** in \(SU(2)^{E_h}\), so the smooth strictly positive *actual finite Wilson vacuum* \(\Omega_{h,R}^2d\mu_{\rm Haar}\) also gives it probability zero. Generic SU(2) fields have noncommuting plaquette holonomies and transverse interactions: their full curvature flow is **not** the scalar monotone discrete equation (2). The result therefore proves neither a positive-probability interacting-vacuum regularity estimate, nor a 4D gradient-flow field, nor a nontrivial OS reconstruction, nor a physical spectral gap. The Penrose/coupled-\(\mathbb Z^5\) and quantum-gravity operators remain separate unsolved tasks.

## 6. Independent regression and next requirements

Companion verifier `research/scripts/verify_cartan_physical_flow.py` reconstructs the **actual full cubic SU(2) original-link Wilson force**, independently constructs the 2D oriented incidence, and checks that the 3D gradient and full SU(2) ODE reduce exactly to the Cartan flux evolution on open n=2,3 meshes (maximum observed discrepancy <2e-13). Ten additional open-grid (n=6,10,16,24,32; physical tau=.018,.075) full nonlinear scalar evolutions check the maximum principle, energy-dissipation identity, physical nonlinear-versus-linear error bounds in \(L^\infty\) and \(L^2\), plus the gradient integral. Six more **actual-link-realizable localized flux** checks (n=8,16,32; tau=.02,.05) confirm energy remains O(1), initial curvature amplitude grows like 1/h, and positive-time curvature remains bounded. The verifier does **not** sample or simulate the full interacting quantum vacuum.

The discrete \(\mathbb Z^2\) Nash inequality used here is standard; for a finite domain, extension by zero gives the required Dirichlet inequality. Background examples: Diaconis and Saloff-Coste, *Nash Inequalities for Finite Markov Chains*, Journal of Theoretical Probability 9 (1996); Deuschel, Kumagai and Slowik, *Gradient estimates of the heat kernel for random walks among time-dependent random conductances*, Probability Theory and Related Fields 195 (2026), for broader time-dependent lattice conductance methods. We derive the needed energy, duality, and coefficient-comparison steps above rather than importing their stronger hypotheses or conclusions. Lüscher's Wilson-flow literature provides independent context for gauge-link gradient-flow definitions, not a proof of this invariant-sector theorem.

**OPEN next targets:** (i) quantitative full **noncommutative 3D** curvature regularity stable under true Wilson-vacuum fluctuations; (ii) physically appropriate **four-dimensional** flowed/smeared gauge-invariant field with renormalized nonvanishing covariance; (iii) complete interacting physical-time Schur/connected-correlator estimates through h→0 and increasing spatial volume; (iv) nontrivial 4D Osterwalder–Schrader reconstruction and positive spectral exclusion; (v) source-faithful genuine 3D quasicrystalline regulator and separate gravitational UV fluctuation operator. **No P0–P5 or T0–T5 gate is closed.**
