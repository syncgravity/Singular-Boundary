# R3 · Exact nonlinear SU(2) cubic physical-energy dissipation, local plaquette admissibility, and an energy-concentration obstruction

**Audit date:** November 6, 2026. **Parent:** draft PR #71, `R3_FIXED_PHYSICAL_RADIUS_LINEARIZED_CUBIC_FLOW_2026-11-05.md`; underlying finite spatial flow from draft PR #70, `R3_GAUGE_COVARIANT_SPATIAL_FLOW_AND_FISHER_GAP_OBSTRUCTION_2026-11-06.md`.  
**Scientific status:** finite **nonlinear classical spatial** gauge-flow theorem; fixed-regulator interacting-vacuum positivity lemma; classical concentration counterexample. It does **not** prove a nonlinear positive-time *smoothing derivative* bound, a scale-uniform interacting quantum covariance/Schur form, 4D OS existence, a Yang–Mills mass gap, a Penrose regulator comparison, or quantum-gravity UV finiteness. All P0–P5 and T0–T5 gates remain **OPEN**.

## 1. Scope and source conventions

Let \(\Gamma_h\) be a finite **open** oriented 3D cubic complex with lattice spacing \(h=1/n\), fixed physical unit-cube domain, vertex/edge/face sets \(V_h,E_h,F_h\), distinct links on each four-link plaquette, and link–face incidence degree \(d_e\le4\). The original-link configuration manifold is \(\mathcal U_h=SU(2)^{E_h}\), with product bi-invariant Riemannian metric normalized by \(T_j=i\sigma_j/2\), Casimir \(C\chi_n=n(n+2)\chi_n/4\). A gauge transformation \(g:V\to SU(2)\) acts on an oriented link by \(U_{xy}\mapsto g_xU_{xy}g_y^{-1}\).

Define the **spatial** Wilson functional and associated *classical* deterministic flow

\[
S_h(U)=\sum_{p\in F_h}\ell(U_p),\quad
\ell(U)=1-\tfrac12\operatorname{tr}_{\mathbf2}U\in[0,2],\quad
\frac{dU_s}{ds}=-\nabla S_h(U_s),\quad U_s=\Phi_s(U_0).
\tag{1}
\]

Here \(s\) is dimensionless **spatial gauge-field flow time**, NOT the physical Euclidean-time parameter of the quantum Hamiltonian. A standard physical-radius scaling is \(\tau=h^2s\). In this same metric the flat-field quadratic term is \(S_h=(1/8)\|d_1 a\|^2+O(a^3)\), so the **physically normalized spatial curvature-energy functional** is

\[
\boxed{\mathscr E_h(U)=\frac8h S_h(U).}\tag{2}
\]

For smooth continuum connections sampled by exact link parallel transport, this normalization approaches \(\int_{[0,1]^3}\sum_{i<j}\|F_{ij}(x)\|^2\,d^3x\). The definitions refer to **three spatial dimensions**, and \(\mathscr E_h\) is neither a quantum renormalized energy nor the four-dimensional Yang–Mills action.

The quantum original-link Wilson Hamiltonian of the previous audits is distinct:
\(H_{h,R}=\alpha_h\sum_e C_e+\beta_h S_h\), \(\alpha_h=g_0(h)^2/(2h)\), \(\beta_h=2/[g_0(h)^2h]\). It has its own strictly positive finite ground state \(\Omega_{h,R}\), whose probability law is \(d\nu_{h,R}=\Omega_{h,R}^2d\mu_{\rm Haar}\). This paper never replaces that law by product Haar in its claims about the actual interacting vacuum.

## 2. Main theorem: exact nonlinear physical-time energy identity

**Theorem 1 (gauge-equivariant global flow and mesh-independent energy–dissipation law).** For every fixed finite cubic \(\Gamma_h\), \(\Phi_s\) is a smooth global diffeomorphism of the compact configuration manifold for every finite \(s\in\mathbb R\), and it commutes with all local gauge transformations. For every initial configuration \(U\) and every physical flow time \(\tau\ge0\),

\[
\boxed{\mathscr E_h(\Phi_{\tau/h^2}U)
+8\int_0^\tau h^{-3}\sum_{e\in E_h}
\|\nabla_e S_h(\Phi_{t/h^2}U)\|^2\,dt
=\mathscr E_h(U).}\tag{3}
\]

Therefore \(\mathscr E_h(\tau)\) is nonincreasing; under the **additional explicit hypothesis** \(\sup_h\mathscr E_h(U_h(0))\le M<\infty\),

\[
\sup_{h,\tau\ge0}\mathscr E_h(U_h(\tau))\le M,
\qquad
\sup_h\int_0^\infty h^{-3}\sum_e\|\nabla_e S_h(U_h(t))\|^2dt\le M/8.
\tag{4}
\]

Neither conclusion asserts any all-time **pointwise** bound on \(h^{-3/2}\|\nabla S_h\|\) or on physical derivatives of curvature; the force is controlled **in the time-integrated norm only**. The hypothesis concerns bounded total classical initial curvature energy, not the unrenormalized quantum Wilson vacuum.

*Proof.* The product-group gradient field is smooth on a compact manifold, hence complete and globally invertible for every finite signed flow time. Local gauge transformations act as isometries, preserve every plaquette character and thus commute with the gradient field and its flow. The chain rule gives exactly \(dS_h(U_s)/ds=-\|\nabla S_h(U_s)\|^2\). Substitute \(\mathscr E_h=8S_h/h\) and \(ds/d\tau=h^{-2}\), then integrate on \([0,\tau]\) to obtain (3). Positivity of the integrand and \(S_h\ge0\) yields (4). No spectral gap, weak-field expansion or semiclassical approximation is used. \(\square\)

**Local force-energy inequality.** In the conventions above a plaquette contribution \(\ell_p\) obeys \(\|\nabla_e\ell_p\|^2=(1-x_p^2)/4\le(1-x_p)/2=\ell_p/2\) for every incident link \(e\), where \(x_p=\tfrac12\mathrm{tr}U_p\). Cauchy–Schwarz, \(d_e\le4\), and four links per face yield

\[
\boxed{\|\nabla S_h\|^2
\le\frac12\sum_e d_e\sum_{p\ni e}\ell_p
\le 8 S_h.}\tag{5}
\]

This is an **upper** bound on force given energy; it is not a coercive lower spectral-gap or curvature-parabolic regularity inequality. It implies \(d\mathscr E_h/d\tau\ge -8\mathscr E_h/h^2\), another nonuniform sufficient estimate, not a physical positive-time smoothing bound.

## 3. Exact nonlinear plaquette admissibility and energy-measure compactness

**Corollary 2 (small plaquette holonomies under uniformly bounded total energy).** For every face \(p\) and every \(\tau\ge0\),

\[
0\le\ell(U_p(\tau))\le\frac h8\mathscr E_h(U_h(0)).\tag{6}
\]

Writing \(U_p=\exp(\theta_p\, \hat n\cdot T)\) with principal \(\theta_p\in[0,2\pi]\), the elementary inequality \(1-\cos(\theta/2)\ge\theta^2/(2\pi^2)\) gives

\[
\boxed{\max_p\theta_p(\tau)\le\frac\pi2\sqrt{h\,\mathscr E_h(U_h(0))}.}\tag{7}
\]

So **uniformly bounded total energy implies uniform small plaquette holonomy** as \(h\to0\), at *every positive and zero physical flow time*. It does **not** imply bounded physical curvature \(\theta_p/h^2\): the best bound from (7) allows growth like \(h^{-3/2}\).

**Corollary 3 (only measure-level compactness).** On a fixed compact physical domain define the gauge-invariant positive face-curvature energy measure at any fixed \(\tau\), using face centers \(x_p\),

\[
\mu_{h,\tau}=\frac8h\sum_{p\in F_h}\ell(U_p(\tau))\,\delta_{x_p}.
\tag{8}
\]

If \(\sup_h\mathscr E_h(U_h(0))\le M\), then \(\mu_{h,\tau}\) has total mass at most \(M\), so subsequences converge weakly to finite positive Radon measures for each fixed \(\tau\). This does **not** identify the limit as the density \(\|F\|^2dx\), guarantee uniqueness, establish gauge-field convergence, or provide a finite positive physical-time quantum correlation.

## 4. Sharp countercheck: bounded energy permits atomic concentration

**Proposition 4 (one-link SU(2) curvature concentration).** On each open \(n^3\) complex with \(n\ge3\), set all links to identity except one interior link \(e_h\) close to the physical center, assigning \(U_{e_h}=\exp(\sqrt h\,T_3)\). There are exactly four incident plaquettes; all four have \(x_p=\cos(\sqrt h/2)\), and every other face has \(x_p=1\). Thus

\[
\boxed{\mathscr E_h(U_h(0))
=\frac{32}{h}\left(1-\cos\frac{\sqrt h}{2}\right)\longrightarrow4.}\tag{9}
\]

Yet on each of those four faces the principal plaquette angle is \(\sqrt h\), and its curvature-angle scale is

\[
\boxed{\theta_p/h^2=h^{-3/2}\longrightarrow\infty.}\tag{10}
\]

The four face centers tend to the same spatial point \(x_*=(1/2,1/2,1/2)\), and each has energy-measure weight tending to one. Hence

\[
\boxed{\mu_{h,0}\ \rightharpoonup\ 4\delta_{x_*}.}\tag{11}
\]

This configuration obeys **all SU(2) cubical Bianchi/incidence requirements**, because it is a genuine assignment of original-link holonomies. It proves that even the **full nonlinear, uniformly bounded physical action plus uniformly small plaquette holonomies** do not force diffuse physical-curvature energy or a pointwise bound on \(\theta_p/h^2\). The example is at **initial flow time**; no assertion of concentration after a fixed strictly positive flow time is inferred. It is a counterexample to an overly strong classical compactness inference, **not** to Yang–Mills existence or a quantum mass gap.

*Proof.* Each face containing \(e_h\) has the holonomy \(U_{e_h}^{\pm1}\) and character \(2\cos(\sqrt h/2)\). The Taylor expansion \(1-\cos(\sqrt h/2)=h/8+O(h^2)\) gives (9). All other assertions follow from the link-to-face incidence count and shrinking face centers. \(\square\)

## 5. Smooth nonabelian initial data and finite quantum vacuum statement

**Proposition 5 (continuum-sized action for smooth sampled fields).** Let \(A\) be a sufficiently smooth \(\mathfrak{su}(2)\)-valued continuum connection on a fixed bounded physical cubic domain, and let each link variable be the exact path-ordered parallel transport of \(A\) along that link. Uniformly in plaquettes,

\[
\ell(U_p)=\tfrac18 h^4\|F_{ij}(x_p)\|^2+O_A(h^5),
\qquad
\mathscr E_h(U_h)=\int\sum_{i<j}\|F_{ij}(x)\|^2d^3x+O_A(h).
\tag{12}
\]

Hence smooth *classical* initial connections satisfy the hypothesis of Theorem 1, and their deterministic nonlinear flows have the exact uniform action/dissipation bounds for arbitrary fixed physical flow times. This is an energy bound, **not a proof of convergence to continuum Yang–Mills heat flow** or any nonlinear higher-derivative heat estimate. It does not apply automatically to configurations sampled from the fluctuating quantum vacuum.

**Proposition 6 (strictly finite interacting-vacuum variance).** For any fixed finite cubic regulator, the original-link Wilson Hamiltonian has a smooth, strictly positive gauge-invariant ground state \(\Omega_h\) (as certified in PR #67). For every nontrivial simple closed loop \(C\) and every finite \(\tau\), the flowed trace \(W_{C,h,\tau}(U)=\chi_1(U_C(\Phi_{\tau/h^2}U))\) is a continuous nonconstant gauge-invariant function. Since the finite-time flow is a diffeomorphism and \(\nu_h=\Omega_h^2d\mu_{\rm Haar}\) has full support,

\[
\boxed{\mathrm{Var}_{\nu_h}(W_{C,h,\tau})>0}\tag{13}
\]

at each finite \(h,R,\tau\). **No lower bound uniform in \(h\) or \(R\)** follows: the nonlinear isolated-plaquette reference in PR #71 shows why variance can shrink strongly under long dimensionless flow. Formula (13) licenses a *finite-regulator normalized observable*, not a continuum nontriviality certificate.

**Conditional true-vacuum energy identity.** Integrating (3) against \(\nu_{h,R}\) gives the exact equality

\[
\mathbb E_{\nu_h}\mathscr E_h(\tau)
+8\int_0^\tau h^{-3}\mathbb E_{\nu_h}\|\nabla S_h(\Phi_{t/h^2}U)\|^2dt
=\mathbb E_{\nu_h}\mathscr E_h(0).\tag{14}
\]

This is valid for the true **finite** interacting vacuum; that vacuum is **not** invariant under deterministic spatial flow. To obtain bounds uniform along \(h\to0\) from (14), a state-dependent *unrenormalized* bound \(\sup_h\mathbb E_{\nu_h}\mathscr E_h(0)<\infty\) would have to be proved or replaced by a suitable renormalized and local analysis. **No such bound is proved here.** The previous finite vacuum link-excision estimate only implies a very weak \(\mathbb E_{\nu_h}\mathscr E_h\le8F_h/h\), divergent on refinement. Physical quantum fields typically require ultraviolet renormalization before an unsmeared energy density can have a finite limit. The deterministic spatial energy law alone cannot close this gap.

## 6. Executable independent tests and explicit open requirements

The accompanying independent verifier `research/scripts/verify_nonlinear_energy_flow.py` uses SU(2) unit quaternions, oriented full open cubic incidence and an **analytic left-invariant gradient**, cross-checked by central finite differences and by arbitrary vertex gauge transformations. The nonlinear flow is integrated with an adaptive high-order ODE solver; the energy balance is checked independently from its integrated squared force. It includes:

- A 2×2×2 cube gradient/gauge covariance test and the exact force-energy inequality (5).
- Smooth, noncommuting continuum-motivated SU(2) link-angle data sampled on 7 open cubic meshes \(n=2,3,4,5,6,8,10\); physically normalized initial energy remains bounded while the number of plaquettes grows from 36 to 3300.
- Actual full **nonlinear** 3D Wilson flow on open meshes \(n=2,3,4\) at a common strictly positive physical flow time \(\tau=.015\), with energy-dissipation defects at numerical precision.
- Five genuine open cubic concentration configurations \(n=3,4,6,8,12\), confirming \(\mathscr E_h\to4\) and exact curvature-angle growth \(h^{-3/2}\).

These computations are **regression checks**, not the proofs of all configurations; Theorem 1 is the gradient-flow chain rule, and Propositions 4–6 are exact analytic arguments. The nonlinear flow code does **not** simulate the true interacting quantum vacuum; the latter enters only through the already-established finite strictly positive \(\Omega_h\) and conditional identity (14).

### Work remaining (all OPEN)

1. Prove nonlinear, gauge-covariant, **positive-physical-radius curvature derivative bounds** or appropriate renormalized spatial observables under assumptions justified for the **true** weak-coupling interacting SU(2) vacuum. The present bound controls total classical energy, its time-integrated force and measure-level subsequences only; concentrated initial curvature provides a sharp failure mode for stronger inference.
2. Prove a physically meaningful renormalized covariance lower bound or nontrivial limit for flowed gauge-invariant Wilson fields and the **complete** energy-dependent variational Schur form/long physical-time connected correlations, uniform in mesh and spatial volume. Fixed-regulator variance positivity is insufficient.
3. Construct the nontrivial 4D reflection-positive interacting continuum, positive spectral exclusion, and the independent physical Penrose/coupled-\(\mathbb Z^5\) 3D regulator transfer. Quantum-gravity ultraviolet finiteness remains a separate operator and dynamics problem.

**Claim classification:** Theorem 1, Corollaries 2–3 and Propositions 4–6 are finite classical/model-scoped statements (Corollaries 2–3 require the stated bounded-initial-energy hypothesis for scale-uniform conclusions). No continuum P0–P5 gate is marked solved. Neither a fluctuation bound over the interacting quantum vacuum nor an interacting four-dimensional Yang–Mills gap has been proved.
