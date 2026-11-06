# P2 finite SU(2) Wilson vacuum: quantitative marginal bounds, physical-loop spectral sum rule, and a two-scale normalization constraint

**November 6, 2026 (UTC) · Source-qualified finite-regulator theorem candidate · No uniform 4D mass-gap claim.**

## Executive proof result

The previous finite interacting-vacuum construction (`R3_VACUUM_WEIGHTED_OBSERVABLE_MAP_AND_SCHUR_FORM_2026-11-06.md`, draft PR #67) supplies a strictly positive ground state Ω, conditional coarse-loop law ρ, induced generator and exact shorted Schur form. It does **not** yet estimate ρ along refinement. This checkpoint establishes three mathematical statements:

1. A **completely explicit, all-coupling finite-model pointwise bound** for the *actual* Wilson vacuum marginal ρ and the variance of every fundamental Wilson loop. The bound is rigorous but has exponential dependence on the entire lattice's numbers of faces and links; it **cannot** close a volume-/spacing-uniform gate.
2. An **exact arbitrary-path-length first spectral moment** for the normalized, interacting-vacuum Wilson loop and a **conditional dyadic comparison theorem**. If the true interacting marginals become close on the same physical loop, the unrenormalized first moment generally retains the factor `4 g₀(h/2)²/g₀(h)²`. Bare thin Wilson loops are therefore not automatically time-normalized by static vacuum matching.
3. A **bounded-source marginal-response inequality** whose constant depends explicitly on the *finite* interacting gap. Using this particular route to prove a uniform gap would be **circular**. It is a response diagnostic, not a source-independent ultraviolet estimate.

An independent positive spectral-measure example demonstrates that a divergent first moment **can coexist with a fixed positive infrared gap**. None of the results says the physical Yang–Mills gap is zero or nonzero.

## 1. Model, normalization and finite vacuum

Consider any finite, connected, oriented three-dimensional open cubical complex, with E original SU(2) link variables, F oriented plaquettes, normalized product Haar measure μ, and finite full-link Hamiltonian

\[
H_{h,R}=\alpha_h\sum_{e=1}^E(-\Delta_e)
+\beta_h\sum_{p=1}^F\bigl(1-\tfrac12\chi_1(U_p)\bigr),
\qquad \alpha_h=\frac{g_0(h)^2}{2h},\quad
\beta_h=\frac{2}{g_0(h)^2h}.
\tag{1}
\]

Here \(\chi_1(U)=\mathrm{tr}_{\mathbf2}U\) and \(-\Delta\chi_n=n(n+2)\chi_n/4\). Every plaquette potential lies in [0,2β_h]. The strictly positivity-improving compact heat semigroup gives a unique smooth, strictly positive, gauge-invariant ground state Ω, normalized by \(\int\Omega^2d\mu=1\), for each **finite** E and F. Define the actual interacting vacuum \(d\nu=\Omega^2d\mu\), not an arbitrary exponential of a guessed effective action.

For a selected non-self-intersecting closed contour C made of L **distinct original lattice edges**, let \(X\) be its ordered edge holonomies (or their grouped coarse-link products). The free-Haar pushforward to X is normalized Haar. The interacting marginal is

\[
\rho_X(X)=\mathbb E_\mu[\Omega^2\mid X],\qquad
 d\nu_X=\rho_X\,d\mu_X,\qquad
\rho_X>0,\quad\int\rho_Xd\mu_X=1.
\tag{2}
\]

The contour is fixed in **physical** space when comparing successive meshes, so L doubles under a dyadic refinement. The historical eight-holonomy loop is the unit square at grid n=2 in the fixed \([0,1]^3\) box; it contains 8 elementary edges at h=1/2 and 16 at h=1/4.

## 2. Explicit nonperturbative finite-volume marginal bound

Let \(P_t=e^{t\alpha\sum_e\Delta_e}\) be the free electric heat semigroup on \(SU(2)^E\). Its normalized single-link kernel has the absolutely convergent Peter–Weyl expansion

\[
 k_s(U)=\sum_{n=0}^\infty (n+1)e^{-s n(n+2)/4}\chi_n(U),\qquad s=\alpha t>0.
\tag{3}
\]

For \(s=8\), using \(|\chi_n|\le n+1\),

\[
|k_8(U)-1|\le\delta_8:=\sum_{n\ge1}(n+1)^2e^{-2n(n+2)}
\le 4e^{-6}+\left[\frac{1+e^{-8}}{(1-e^{-8})^3}-1-4e^{-8}\right]
<\frac1{100}.
\tag{4}
\]

The bracket bounds the n≥2 tail because n(n+2)/4≥n for n≥2. Hence \(99/100\le k_8\le101/100\), and the E-link product heat kernel has a maximum-to-minimum ratio ≤\((101/99)^E\).

**Proposition A (finite interacting marginal Harnack bound).** Define

\[
\boxed{\Lambda_{h,R}=\frac{64F}{g_0(h)^4}
+E\log\frac{101}{99}.}
\tag{5}
\]

Then the **true** normalized finite Wilson ground state and **every** Haar-projected physical coarse marginal (2) obey

\[
\frac{\sup\Omega}{\inf\Omega}\le e^{\Lambda_{h,R}},\qquad
\boxed{e^{-2\Lambda_{h,R}}\le\rho_X(X)\le e^{2\Lambda_{h,R}}\quad\text{for all }X.}
\tag{6}
\]

**Proof.** The normalized Wilson potential satisfies \(0\le V\le2\beta F\). For any nonnegative test f, Feynman–Kac gives the positive-semigroup order

\[
e^{-2t\beta F}P_tf\le e^{-tH}f\le P_tf.
\]

The ground-state equation \(e^{-tH}\Omega=e^{-tE_0}\Omega\), combined with the strictly positive E-fold free heat kernel, yields

\[
\frac{\max\Omega}{\min\Omega}
\le e^{2t\beta F}\left(\frac{\sup k_{\alpha t}}{\inf k_{\alpha t}}\right)^E.
\]

Taking \(t=8/\alpha\), noting \(\beta/\alpha=4/g_0^4\), gives (5). Since \(\int\Omega^2d\mu=1\), the ratio bound implies \(e^{-\Lambda}\le\Omega\le e^\Lambda\); squaring and conditional expectation yields (6). QED.

This statement is **uniform in X at each fixed finite lattice**, not uniform in E,F,h,R. The exponents grow at least as the coarse global cell count, even if the *actual local marginal* remains benign. For the open n³ cubical grid, \(E=3n(n+1)^2\), \(F=3n^2(n+1)\). Thus this direct global Harnack route yields \(\Lambda\sim 192 n^3/g_0^4\), not a usable infinite-volume/ultraviolet marginal estimate. Its weakness is a property of this **bound**, not a theorem about divergence of the true marginal.

## 3. Exact fixed-physical-loop Wilson spectral moment

Write \(W_C=\chi_1(U_C)\in[-2,2]\), with \(\mu_C=\mathbb E_\nu W_C\), \(\sigma_C^2=\mathrm{Var}_\nu(W_C)\), and \(f_C=(W_C-\mu_C)/\sigma_C\). The Haar pushforward of U_C is Haar SU(2), so

\[
\int W_C\,d\mu=0,\quad\int W_C^2d\mu=1,\quad
\int(1-W_C^2/4)d\mu=3/4.
\]

From (6) and the variational formula for variance,

\[
 e^{-2\Lambda}\le\sigma_C^2\le e^{2\Lambda},\qquad
\tfrac34 e^{-2\Lambda}\le\mathbb E_\nu(1-W_C^2/4)\le\tfrac34 e^{2\Lambda}.
\tag{7}
\]

These provide an **explicit nonzero finite variance certificate** in the actual interacting vacuum, not a numerical approximation to Ω.

**Proposition B (exact normalized first spectral moment).** Let \(L_C\) be the number of distinct elementary links traversed once by C. In the ground-state transform \(L=\Omega^{-1}(H-E_0)\Omega\),

\[
\boxed{-C_{f_C}'(0)=\mathcal E(f_C,f_C)
=\alpha L_C\frac{\mathbb E_\nu[1-W_C^2/4]}{\sigma_C^2}.}
\tag{8}
\]

In particular,

\[
\tfrac34\alpha L_C e^{-4\Lambda}\le -C_{f_C}'(0)
\le \tfrac34\alpha L_C e^{4\Lambda}.
\tag{9}
\]

**Proof.** For fundamental SU(2), \(-\Delta\chi_1=3\chi_1/4\) and the pointwise Casimir identity is \(|\nabla\chi_1|^2=1-\chi_1^2/4\). Every distinct elementary edge in the ordered loop contributes exactly one such positive derivative square; links outside the loop contribute zero. Integrating under Ω² Haar and dividing by \(\sigma_C^2\) gives (8). Equation (7) gives (9). QED.

For a loop of **fixed physical perimeter** ℓ whose elementary lattice edges have physical length h, \(L_C=\ell/h\), so (8) becomes

\[
\boxed{-C_{f_C}'(0)=\frac{g_0(h)^2\ell}{2h^2}\,q_{h,R}(C),\quad
 q_{h,R}(C):=\frac{\mathbb E_\nu(1-W_C^2/4)}{\mathrm{Var}_\nu(W_C)}.}
\tag{10}
\]

This fixes the otherwise ambiguous issue of whether an eight-link loop retains eight **elementary** links during refinement. It does not: the same physical contour has eight coarse links and sixteen fine elementary links after the first refinement.

## 4. Conditional two-scale theorem: marginal matching does not automatically match physical time

On the **same physical contour** let \(\rho_c\) and \(\rho_f\) be the true interacting single-loop (or eight-coarse-holonomy) marginals, both expressed against the common SU(2) Haar reference on the physical contour. The coarse holonomies on the refined lattice must be ordered products of fine links, not different geometric loops. Assume a concrete yet **unproved** density-comparison hypothesis,

\[
\boxed{\|\log(\rho_f/\rho_c)\|_{L^\infty}\le\delta.}
\tag{11}
\]

Because (11) implies \(e^{-\delta}\rho_c\le\rho_f\le e^\delta\rho_c\), both \(G_i=\mathbb E_i(1-W^2/4)\) and \(V_i=\mathrm{Var}_i(W)=\inf_a\mathbb E_i(W-a)^2\) satisfy the same multiplicative bounds. Thus

\[
 e^{-2\delta}\le \frac{G_f/V_f}{G_c/V_c}\le e^{2\delta}.
\]

The factor-of-two refinement \(h_f=h_c/2\) doubles the number of elementary links on C and doubles the kinetic coefficient up to the running bare-coupling ratio. Consequently:

**Proposition C (conditional unrenormalized two-scale first-moment comparison).** Define \(k=4g_0(h/2)^2/g_0(h)^2\). Under (11),

\[
\boxed{k e^{-2\delta}\le
\frac{-C'_{f_f}(0)}{-C'_{f_c}(0)}\le k e^{2\delta}.}
\tag{12}
\]

If one additionally demands that the *unrenormalized* initial slopes agree within logarithmic tolerance \(|\log[(-C'_{f_f}(0))/(-C'_{f_c}(0))]|\le\epsilon\), the static density mismatch must satisfy the **necessary condition**

\[
\boxed{\delta\ge\frac12\bigl(|\log k|-\epsilon\bigr)_+.}
\tag{13}
\]

For slowly running bare coupling, \(k\approx4\). Thus static convergence \(\delta\to0\) makes the raw initial-slope ratio approach four, not one. This is a rigorous **conditional kinematic mismatch of the unsmeared normalized Wilson observable**, not a no-go for a renormalized/smeared operator, a physically adjusted time convention, or a mass gap. Indeed, continuum Wilson loops can require their own ultraviolet renormalization and need not possess a uniformly finite derivative at t=0.

**Proof.** Apply the multiplicative order implied by (11) to the positive function \(1-W^2/4\) and to the variational formula \(\inf_a\int(W-a)^2\rho\,d\mu\), then divide and combine with (8). Taking logarithms yields (13). QED.

## 5. Distinguish ultraviolet moment divergence from an infrared gap

Let h decrease to zero and consider the positive normalized spectral measures

\[
 d\mu_h=(1-h)\delta_M+h\delta_{h^{-3}},\qquad 0<h<\min(1/2,M^{-1/3}),\quad M>0.
\]

They all have the **same** positive spectral gap M, with correlations

\[
C_h(t)=(1-h)e^{-Mt}+h e^{-h^{-3}t},\qquad
-C_h'(0)=(1-h)M+h^{-2}\to\infty.
\tag{14}
\]

For every fixed t>0, \(C_h(t)\to e^{-Mt}\). Thus an unbounded first moment is consistent with a stable infrared gap, because it can reflect arbitrarily high energies with vanishing weight. The finite Wilson first-moment formula is an **ultraviolet normalization diagnostic** and cannot alone prove or disprove the Yang–Mills mass gap. This toy measure is not a solved SU(2) lattice spectrum.

## 6. The coupling-source response bound exposes a circular proof route

At **fixed finite lattice and fixed electric coefficient α**, introduce an auxiliary bounded gauge-invariant source θ by \(H_\theta=H_0+\theta F_0\), \(F_0=\sum_p(1-\chi_1(U_p)/2)\). This is **not** differentiation along the physical running coupling \(g_0(h)\): on that path the electric coefficient also varies and its derivative is unbounded.

Let Ωθ be the normalized unique positive ground state, Δθ>0 its finite spectral gap and \(\rho_\theta\) the marginal on a fixed physical loop or retained holonomies. Kato differentiation of the isolated ground eigenvalue gives

\[
\partial_\theta\Omega_\theta
=-(H_\theta-E_0)_{\Omega_\theta^\perp}^{-1}
(F_0-\langle F_0\rangle_\theta)\Omega_\theta,
\qquad
\|\partial_\theta\Omega_\theta\|_2\le
\frac{\sqrt{\mathrm{Var}_\theta(F_0)}}{\Delta_\theta}.
\]

Marginalizing is a Hellinger-speed contraction by conditional Cauchy–Schwarz:

\[
\boxed{\|\partial_\theta\sqrt{\rho_\theta}\|_{L^2(\mu_X)}
\le\frac{\sqrt{\mathrm{Var}_\theta(F_0)}}{\Delta_\theta}
\le\frac{F}{\Delta_\theta}.}
\tag{15}
\]

The last bound uses \(0\le F_0\le2F\), hence \(\mathrm{Var}(F_0)\le F^2\). This is an **exact finite spectral susceptibility bound**. It is *not* a noncircular proof of uniform control: its denominator contains the full interacting finite gap Δθ, precisely the quantity that still needs a physical continuum lower bound. A proof of uniform marginal regularity cannot legitimately infer that gap by assuming (15) is uniform unless an independent, noncircular lower bound is supplied.

## 7. Reproducibility and status of the next gate

`research/scripts/verify_marginal_harnack_2026_11_06.py` independently verifies:

- the SU(2) heat-kernel Peter–Weyl upper tail bound \(\delta_8<0.01\), and exact Wilson/Haar Casimir normalization;
- exact oriented open n³ cubical cell counts for n=1,2,4,8,16 and the fixed-physical-square loop length \(L_C=4n\), with first free-vacuum moments `1.5, 6, 24, 96, 384` for fixed \(g_0^2=1\); **these are free-vacuum diagnostics, not interacting three-dimensional spectral computations**;
- 140,000 random SU(2) Haar quaternions at each of five distinct loop lengths, checking moment identities only;
- five *admissible illustrative* positive SU(2) class marginals \(e^{\kappa W}/a_0(\kappa)\) against the exact two-scale ratio bounds; these densities are **not asserted to equal the 3D Wilson interacting marginals**;
- the finite response contraction using a four-state strictly positive matrix model (a **numerical regression for the universal spectral inequality**, **not SU(2)**); and
- the positive-spectral-measure UV/IR counterexample (14).

**Finite theorem checkpoint obtained:** real interacting-vacuum marginal pointwise/variance bounds with explicit all-model constants, an exact fixed-physical Wilson spectral moment, a sharp conditional two-scale normalization inequality, and an exactly quantified warning against gap-dependent source-response shortcuts.

**OPEN:** a volume-independent *local* marginal/score estimate replacing the global Harnack factor \(e^{64F/g_0^4}\); an actual physically renormalized, gauge-invariant observable with useful time normalization; and an energy-dependent full Schur-form comparison with summable errors in the interacting weak-bare-coupling/continuum/large-volume regime. These are not inferred by this note. The Penrose 3D regulator, nontrivial 4D OS reconstruction, Yang–Mills mass gap and gravitational ultraviolet problem remain separately OPEN.

### Model and source references

- `research/theorems/R3_CUBICAL_SU2_GAUSS_HAMILTONIAN_REFERENCE_2026-10-31.md` (finite original-link SU(2) model and Casimir convention).
- `research/theorems/R3_CUBICAL_SU2_FINITE_TRANSFER_POSITIVITY_2026-10-31.md` (finite positive transfer).
- `research/theorems/R3_EXACT_TWO_TIME_INFLUENCE_AND_DYADIC_SCALING_2026-11-06.md` (bare P/Q memory and true 3D two-scale geometry; draft PR #66).
- `research/theorems/R3_VACUUM_WEIGHTED_OBSERVABLE_MAP_AND_SCHUR_FORM_2026-11-06.md` (finite true-vacuum map and full Schur form; draft PR #67).
- `docs/research/YM_CUBIC_PENROSE_TRANSFER_AND_INFRARED_GATES_2026-11-05.md` (distinct YM and gravity obligations).

**No P0–P5 or T0–T5 gate is closed by this analysis.**
