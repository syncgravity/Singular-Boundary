# Proof dependencies and noncircular checkpoints

## P0-H · Perpendicular quotient density obstruction (2026-11-11)

Paper 2's identification \(\mathbb R^2_\perp/\pi_\perp(\mathbb Z^5)\cong\mathbb T^2\) is false as written. Four explicit sum-zero lattice vectors show that the perpendicular image contains dense subgroups on both real and imaginary axes, using irrational generator ratios \(\varphi^{-1}\) and \(\varphi\). Thus \(\pi_\perp(\mathbb Z^5)\) is dense, not a period lattice; the quotient is non-Hausdorff and cannot be the claimed flat torus. This blocks the stated compactification / KK inference, not the real \(C_5\) decomposition or the 2D Penrose model set.

A distinct 3D cut-and-project candidate is specified by \(E_{\rm phys}=V_{72^\circ}\oplus\mathbb R e_u\) and \(E_{\rm int}=\mathbb R e_v\), but it changes the acceptance rule, breaks \(C_5\), and supplies no SU(2) dynamics. It is not the original Penrose set and is not yet the canonical regulator. **P0-H remains OPEN.** See the [full exact audit](../../research/audits/P0_COUPLED_Z5_INTERNAL_QUOTIENT_DENSITY_AUDIT_2026-11-11.md) and [standard-library verifier](../../research/verification/verify_p0_coupled_z5_internal_quotient.py). The alternative 3D point-set candidate has a finite buffered Voronoi diagnostic: 7,383 core cells, 8/12/14 faces, measured maximum aspect ratio 3.4858; see the [cellulation report](../../research/audits/P0_H3D_VORONOI_CELLULATION_DIAGNOSTIC_2026-11-11.md) and [SciPy verifier](../../research/verification/verify_p0_h3d_voronoi_sample.py). This remains a changed model and not a canonical regulator.

---

## PF-I16 · 2026-11-11 derivative-input correction

The four-factor SU(2) group-product mixed covariant derivative has passed an independent quaternion audit over all 16 orientation words and 3,840 ordered-pair cases; see [the sign/trivialization audit](../../research/audits/PF_I16_FOUR_FACTOR_MIXED_COVARIANT_DERIVATIVE_AUDIT_2026_11_11.md) and [its verifier](../../research/verification/verify_pf_i16_four_factor_mixed_derivative.py).

A more consequential correction blocks the current refined-rotor ladder: the inherited first-derivative estimate \(\|s_\beta'\|_\infty\le\beta\) is incompatible with the radial equation recorded in the refined-rotor theorem. Analytic perturbation at zero coupling gives \(q_\beta=s_\beta'=-\frac43\beta\sin\theta+o(\beta)\) uniformly, hence \(\|s_\beta'\|_\infty/\beta\to4/3\). See [the perturbative obstruction audit](../../research/audits/PF_I16_ISOLATED_ROTOR_FIRST_DERIVATIVE_OBSTRUCTION_2026_11_11.md). Consequently the inherited Hessian blocks, derivative-flow rate, \(1/40000\) threshold, residual derivative constants, and third-order numerical prefactor are not currently certified and must be rederived. The exact dressing identity, incidence count \(784^{k-1}\), and exact centered third-order recursion remain distinct valid finite identities. No canonical proof gate is closed.

---


## R3_IR · Conditional weighted trace–gradient block on the finite open SU(2) strip (2026-11-10)

This is a separate R3_IR strip calculation, not part of PF-I16. The conditional one-link Poincaré estimate gives \(c_{\rm tr}=\frac34e^{-49\pi/144}\approx0.2575101\) and leakage \(\ell\approx0.00248474\), including the nonzero conditional-mean correction. The exact trace commutator for \(L=\Delta+2\nabla S_g\cdot\nabla\) is

\[
C_e=4\sum_d H^S_{ed}:H_{ed}+2\sum_d\langle\nabla_d\Delta_eS_g,\nabla_df\rangle+4\operatorname{Ric}_e(\nabla_eS_g,\nabla_ef),
\]

so on radius-two SU(2) its Ricci term is \(+2\langle\nabla_eS_g,\nabla_ef\rangle\). The weighted trace equation contains the unevaluated \(A_2\), \(A_{3,w}\), and \(T_wK_w\) terms. The two-variable coercive skeleton rate \(c-\ell\approx0.0891819\) is not a full semigroup contraction.

The next required work is local plaquette evaluation of \(A_2\), an ordered covariant operator bound for \(A_{3,w}\), and a trace-free/mixed Hessian estimate for \(K_w\), followed by a full \(3\times3\) positivity check. No interacting \(\lambda=1\) gap or 3D/continuum transfer is claimed. See [the conditional theorem record](../../research/theorems/R3_IR_CONDITIONAL_WEIGHTED_TRACE_GRADIENT_BOCHNER_BLOCK_2026-11-10.md).

---

## PF-I16 · Auxiliary dressed-locality ladder (2026-11-10; no canonical gate closure)

The Penrose–Fibonacci groundwork now supports a more detailed **sub-proof route** inside the existing P0–P5 / PF-G0–G5 architecture. It does not replace those gates and does not close any of them.

1. **Finite source interaction data — established at fixed scope.** PF-I16's exact seven-class \(C_{2,2,2,2}\) result remains the fully four-face-connected eighth-order contribution only; it is not the complete eighth-order energy.
2. **Universal incidence and support counting — established combinatorially.** The safe source-uniform inventory is \(d_e\le8\), giving face-overlap degree \(D\le28\) and rooted connected support count \(784^{k-1}\). The sharper \(D\le4\) is observed on eight finite crops only.
3. **Single-face dressing — exact finite-graph identity.** The ground-state conjugation leaves a residual supported only at shared links (at most 25 links per residual term under \(d_e\le8\)). Uniform derivative/Hessian and Poincaré estimates are separate analytic obligations.
4. **Third-order mixed coefficient — exact algebra, conditional norm bound.** The centered reduced-resolvent coefficient has a six-permutation formula. The exact identity is established algebraically, but the previously stated numerical prefactor and old curvature/derivative thresholds have not been rederived after the refined rotor/residual estimates; treat them as historical working calculations, not current consequences. At this checkpoint no spatial spanning-tree decay had yet been proved; this statement is superseded by the 2026-11-13 conditional Dobrushin tree estimate below.
5. **Refined isolated-rotor Hessian and residual derivatives — conditional working estimate.** The exact weighted-mean identity gives \(\|\nabla^2s_f\|_{\rm op}\le\frac43\beta_f+\frac{20}{3}\beta_f^2\), assuming the inherited \(\|s_f'\|_\infty\le\beta_f\). Under the stated product-holonomy mixed-Hessian estimate, the working face blocks are \(H_{ee}^{(f)}\le\frac{32}{3}b_0+\frac{320}{3}b_0^2/a_0\) and \(H_{eg}^{(f)}\le\frac{44}{3}b_0+\frac{320}{3}b_0^2/a_0\). For \(b_0/a_0\le1/40000\), the residual bounds are \(\|R_e\|_\infty\le1040b_0^2/a_0\), component derivative \(\le8450b_0^2/\sqrt{a_0}\), support \(\ell^2\) derivative \(\le42250b_0^2/\sqrt{a_0}\), and support \(\ell^1\) derivative \(\le211250b_0^2/\sqrt{a_0}\). The product-holonomy mixed covariant derivative/orientation calculation has now passed an independent finite-difference audit over all 16 orientation words and 3,840 ordered-pair cases; see [the audit report](../../research/audits/PF_I16_FOUR_FACTOR_MIXED_COVARIANT_DERIVATIVE_AUDIT_2026_11_11.md) and [verifier](../../research/verification/verify_pf_i16_four_factor_mixed_derivative.py). This closes only the algebraic sign/trivialization check. The isolated-rotor derivative hypothesis and downstream analytic estimates remain conditional. The earlier third-order numerical bound and its old curvature/decay thresholds have not been rederived with these constants.

5. **Fourth-order spatial tree — conditional fixed-order estimate now recorded.** The cut-interpolation theorem retains the full four-source coefficient and avoids termwise loss of pair-partition cancellations; its derivative-flow and face-pullback inputs remain conditional.
6. **All-orders connected activity — open.** Need cancellation-preserving joint space/time majorants with controlled K_8^k growth, uniform higher-order cut-response constants, and an actual quantum KP application. The absolute Leonov–Shiryaev majorant is superfactorial and cannot serve as the convergence proof.
7. **Physical transfer and continuum — still open.** Source-derived kinetic/time normalization, physical gauge/hull measure, genuine refining 3D regulator, interacting continuum reconstruction and a strictly positive physical mass gap remain unproved.

### Effect on the canonical gates

- **P0 / PF-G0–G1:** source/operator identity and a physically valid, genuinely refining three-dimensional regulator remain open. The accepted-rhombus incidence result is useful geometry, not a completed 3D cellulation certificate.
- **P1 / PF-G2:** the auxiliary SU(2) finite-graph identities do not supply source-derived physical kinetic coefficients, time, or the complete physical Gauss-sector Hamiltonian.
- **P2 / PF-G3–G4:** PF-I16 now has conditional finite-volume spatial tree bounds through third and fourth order; all-orders summability and refinement-uniform physical estimates remain open.
- **P3–P5 / PF-G5:** physical vacuum/current, reconstructed infrared spectrum, nontrivial four-dimensional continuum theory and positive physical mass gap remain open.

The PF-I16 refined-rotor record is [here](../../research/theorems/PF_I16_REFINED_ROTOR_HESSIAN_RESIDUAL_DERIVATIVES_2026_11_10.md). The PF-I16 ladder is therefore an internal refinement of the research plan, not a relaxation or renaming of the acceptance criteria. See the [PF-I16 theorem records](../../research/theorems/PF_I16_CONNECTED_SUPPORT_INCIDENCE_CORRECTION_2026_11_10.md), [dressing identity](../../research/theorems/PF_I16_LOCAL_DRESSING_SHARED_LINK_RESIDUAL_2026_11_10.md), and [third-order coefficient note](../../research/theorems/PF_I16_DRESSED_THIRD_ORDER_COEFFICIENT_2026_11_10.md).

---


## P2 / T2 · Original-link full non-Abelian plaquette-influence theorem (2026-11-06; finite classical)

[Full proof and numerical scope](../../research/theorems/R3_FULL_NONABELIAN_CUBIC_PLAQUETTE_INFLUENCE_AND_MAXIMUM_OBSTRUCTION_2026-11-06.md). Unlike the positive-physical-time **Cartan-planar** nonlinear theorem, this result applies to **all finite 3D cubic original-link SU(2) configurations, including noncommuting fields**. With `ell_p=1-Re U_p`, `a_p=sqrt(ell_p)`, and `N_pq=# shared original links`, the exact one-link derivative `||grad_e ell_p||²=ell_p(2-ell_p)/4` gives `D_s^+ a_p <= -(2-ell_p)a_p/2 + Σ_(q ne p)N_pq a_q/4`. Original-link incidence implies `A=N_off/4` has row norm ≤3, so the **finite nonlinear** comparison is `a(s)<=exp(sA)a(0)` and `||a(s)||infinity<=exp(3s)||a0||infinity`, with explicit factorial graph-distance influence tails. A reproducible finite SU(2) quaternion example also has an **increasing strict largest local plaquette defect** while total action decays. This refutes an unconditional *plaquette maximum principle* but not a near-flat or physical-time covariant smoothing theorem.

At fixed physical flow time **s=tau/h²**, the positive absolute-value bound becomes `exp(3tau/h²)`, which is **not uniform** as h→0. The decisive **OPEN** interface is a signed covariant SU(2) curvature evolution exploiting Bianchi and commutator cancellations under source-supported assumptions for the **actual weak-coupling quantum Wilson vacuum**, then nonvanishing renormalized covariance, complete interacting physical-time Schur/long-time correlations, nontrivial OS continuum and positive spectral exclusion. Penrose original 3D regulator and gravity UV objectives remain separate OPEN gates.

**Theorem navigator audit:** historical 740 links preserved; 13 post-historical theorem source files plus this new theorem bring the proposed branch to **754 exactly indexed records**. [Full source navigator](THEOREM_INDEX.md) · [Git-hash source registry](THEOREM_INDEX_LIVE.json) · [index completeness verifier](../../research/scripts/verify_theorem_index.py). Source indexing does NOT certify a proof or close a gate.

## P2/T2 · Exact invariant Cartan-planar nonlinear physical-time smoothing (2026-11-06; conditional classical subsystem)

[Full mathematical report](../../research/theorems/R3_EMBEDDED_CARTAN_NONLINEAR_POSITIVE_RADIUS_SMOOTHING_2026-11-06.md) proves a **true nonlinear positive-time curvature estimate**, not merely a flat-field linearization: the full 3D cubic original-link SU(2) Wilson spatial flow exactly preserves z-independent xy links in one **fixed Cartan U(1)** and identity z links. On each open xy plane, with lifted q=(Bθ)/2 and h=1/n, the curvature F=2q/h² obeys **∂τ F=−(2h⁴)^−1 BBᵀ sin(h²F/2)**. With an explicit no-winding |q(0)|<π/2 condition, the associated **time-dependent scalar conductances** c_e lie in [κ,1], κ=cos||q(0)||∞>0. The exact discrete maximum principle and 2D Dirichlet Nash inequality give **||F(τ)||∞≤sqrt(2 C_N/(κτ))||F(0)||_(2,h)** for τ>0.

The **actual three-dimensional classical initial-action bound** E_h(0)≤M, counting all n+1 identical xy layers, implies **||F(0)||_(2,h)≤π√M/2** and ||q(0)||∞≤(π/4)h√M, so κ≥1/√2 on sufficiently fine meshes. Hence positive-physical-flow-time curvature is uniformly bounded even for realizable initially concentrated curvature F(0)~2/h with E_h(0)→4. A separate exact physical nonlinear-to-linear Dirichlet comparison gives **||F_nl(τ)−F_lin(τ)||_(2,h)≤(1−κ)/sqrt(2κ)||F(0)||_(2,h)=O(h²M^(3/2))**, uniformly for all τ≥0. Under an **additional** sup-bounded initial F, the L∞ error is at most **τh²||F(0)||∞³/12**. The underlying 3D SU2 link-force invariance and exact face equation have independent quaternion tests.

**Most important limitation:** the **fixed commuting Cartan planar subset has zero product-Haar measure**, and therefore zero probability under the strictly positive true *finite* interacting Wilson vacuum. It does **not** furnish a generic noncommuting 3D curvature bound or a quantum expectation/Schur estimate. Next **OPEN** step: prove a commutator-stable full non-Abelian physical-radius curvature estimate under hypotheses *justified for the true weak-coupling vacuum*, and then renormalized nontrivial covariance plus complete h,R-uniform physical-time Schur/OS/infrared exclusion. All P0–P5, 3D quasicrystal transfer, and independent gravity UV objectives remain OPEN.

## P2/T2 · Full nonlinear classical cubic physical-energy identity, concentration warning and finite vacuum variance (2026-11-06)

[Exact finite source and full numerical consistency checks](../../research/theorems/R3_NONLINEAR_CUBIC_PHYSICAL_ENERGY_DISSIPATION_2026-11-06.md). On a finite **three-spatial-dimensional** original-link cubic SU(2) Wilson complex, the classical gauge-field flow `dU/ds=-grad S_h` obeys **E_h(tau)+8 integral_0^tau h^-3 ||grad S_h||²dt=E_h(0)** for `tau=h²s`, `E_h=8S_h/h`, without linearizing. For any family with **uniformly bounded classical initial E_h**, evolving action and integrated physical force are uniform in h; all plaquette angles are at most `(pi/2)sqrt(h E_initial)`. Positive curvature-energy measures on a fixed physical domain have weak subsequences. However a genuine original-link configuration with one link `exp(sqrt h T3)` has **E_h→4**, **plaquette angle/h²=h^-3/2**, and initial curvature-energy measures tending to an atom. Thus the theorem controls **energy and integrated force**, not pointwise nonlinear positive-radius smoothing or a unique continuum curvature density.

At every **finite** full interacting cubic SU(2) Wilson regulator, `Omega_h² dHaar` has full support, and finite-time spatial flow is a gauge-equivariant diffeomorphism; flowed nonconstant Wilson loops therefore retain **strictly positive finite covariance**. This is not a uniform h,R lower bound. The exact classical dissipation identity may be averaged against this true finite vacuum, but an **initial unrenormalized physical curvature-energy expectation uniformly bounded in h** has not been shown. The quantum vacuum's physical time, energy-dependent Schur form, renormalized flowed covariance, nontrivial 4D OS limit and infrared spectral exclusion remain distinct **OPEN** tasks. Penrose/coupled-Z5 and quantum-gravity ultraviolet objectives are independent.

## P2/T2 · Fixed physical-radius curvature smoothing in the flat cubic sector (2026-11-05; not an interacting 4D theorem)

[Exact finite/linearized source and independent nonlinear control](../../research/theorems/R3_FIXED_PHYSICAL_RADIUS_LINEARIZED_CUBIC_FLOW_2026-11-05.md). On the **open cubic original-link SU(2) flat-field linearization**, (S_W=(1/8)||d_1a||²+O(a³)), (partial_sa=-(1/4)d_1^*d_1 a), and (d_1d_0=0). With (	au=h²s) and (F_h=d_1 a/h²), (F_h(	au)=exp[-	au d_1d_1^*/(4h²)]F_h(0)). The spectral theorem gives **(|L_h^{k/2}F_h(	au)|≤(2k/e	au)^{k/2}|F_h(0)|)** with (L_h=d_1d_1^*/h²), independent of mesh/box. A **separate periodic cubic Fourier control** gives a sharp per-fixed-mode (O(h²)) physical-flow multiplier comparison. These are **positive linearized reference results**, not statements on the genuine interacting vacuum, nonlinear curvature or four-dimensional OS theory.

In a distinct **nonlinear four-link plaquette under Haar/free-electric reference**, as (arepsilon=1-	anh sdownarrow0), the normalized flowed Wilson variance scales as (4sqrt2arepsilon^{3/2}), while the initial electric moment grows as (alpha/(4arepsilon)). The unit-variance normalized observable converges weakly to zero, and its fixed-positive-quantum-time free-electric correlations vanish. This exact warning is **not** a counterexample to 4D SU(2) Yang–Mills or a test of the same fixed-physical-size contour under (h	o0). **OPEN next theorem:** nonlinear gauge-covariant fixed-physical-radius flow, a nontrivial true-interacting-vacuum covariance/renormalized Wilson field, complete physical-time Schur/connected-correlation control, nontrivial 4D OS construction and independent Penrose/gravity interfaces.

## P2/T2 · Finite spatial Wilson-flow candidate and Fisher-to-gap obstruction (2026-11-06; no continuum closure)

[Mathematical source and complete checks](../../research/theorems/R3_GAUGE_COVARIANT_SPATIAL_FLOW_AND_FISHER_GAP_OBSTRUCTION_2026-11-06.md). The previous cubic Wilson local interacting vacuum estimate is **not** an infrared estimate. A smooth positive gauge-invariant SU(2) **class rotor** (not the cubic Wilson action) has densities ρ_ε=(x²+ε²)/(1/4+ε²), x=tr(U)/2, with **∫|∇√ρ_ε|²≤3/4**, **Var_ρ(trU)≥1**, but class-sector spectral gap **≤ε→0**. Thus even a uniform Fisher/variance bound would not by itself prove the YM gap.

**Single-holonomy group heat smoothing does not renormalize the centered fundamental Wilson observable:** e^{sΔ}χ₁=e^{−3s/4}χ₁, so the normalized observable and its physical-time correlations are unchanged. A genuinely gauge-equivariant *spatial Wilson-action flow* Φ_s of **all original cubic links** is defined on the finite SU(2)^E configuration, with exact finite **||Hess S_W||≤4**, **||DΦ_s||≤e^{4s}**, and factorial distant-link sensitivity ≤2π L_CΣ_{k≥r}(4s)^k/k!. This is volume-independent for fixed lattice flow time, but **not uniform at fixed physical flow radius** s=t_phys/h²; it is not the full 4D Wilson-flow theory.

For any finite true interacting Wilson-vacuum observable family, the exact initial physical-time moment is **−C′_a(0)=α_h(aᵀG_h a)/(aᵀS_h a)** with S the genuine interacting covariance and G the original-link electric Dirichlet matrix. An h-uniform quotient bound would imply **ultraviolet spectral first-moment tightness**, not low-energy spectral exclusion. **OPEN P2/T2/T3 target:** a 4D physically normalized flowed/smeared gauge-invariant observable dictionary, uniform true-vacuum covariance and full shorted/Schur estimates, and long physical-time correlation bounds along weak-bare-coupling h→0 and R→∞. All continuum mass-gap, Penrose transfer, and independent gravitational UV objectives remain OPEN.

## P2 · Gap-free local SU(2) interacting Wilson Fisher estimate (2026-11-06; fixed coupling / thermodynamic subsequence)

[Source-qualified finite and infinite-box subsequence theorem](../../research/theorems/R3_LOCAL_INTERACTING_SU2_FISHER_AND_THERMODYNAMIC_SUBSEQUENCE_2026-11-06.md). On the actual finite original-link cubic SU(2) Wilson vacuum Ω, remove any selected set S of links and all incident magnetic plaquettes. Variational comparison with a Haar-constant state on S yields **αΣ_{e∈S}⟨Cₑ⟩+Σ_{p touching S}⟨Vₚ⟩≤β·#{plaquettes touching S}**, without assuming the interacting gap or using source-response differentiation. A single interior link has ≤4 incident plaquettes. Haar disintegration of a *simple ordered physical-loop holonomy* through one of its elementary edges then implies **∫_{SU2}|∇√ρ_C|²≤16/g₀⁴** and Fisher(ρ_C)≤64/g₀⁴, **independent of the surrounding box size and the number of elementary contour links**. A fixed SU2 Sobolev constant C_S yields **Var_ρ(tr U_C)≥π²/[64 C_S³(1+16/g₀⁴)³]**. At each fixed h,g₀ this certifies nontrivial local thermodynamic subsequences and normalized Wilson spectral-measure tightness from an R-independent *first* moment bound.

**Strict limitation:** no bound here is uniform as g₀(h)→0; H¹ does not imply a pointwise L∞ Harnack on SU2, and fixed-h first-moment tightness does not exclude soft positive-energy support. The **OPEN** P2/T2/T3 target remains a scale-uniform renormalized/smeared gauge-invariant Wilson field and complete long-physical-time Schur/connected-correlation comparison, plus nontrivial P5 reconstruction. No Yang–Mills continuum gate is closed and the Penrose/quantum-gravity questions remain separate.

## P2 exact finite interacting marginal and fixed-loop UV moment (2026-11-06; no continuum closure)

[Finite Wilson marginal and two-scale sum-rule audit](../../research/theorems/R3_FINITE_WILSON_MARGINAL_HARNACK_AND_TWO_SCALE_SUM_RULE_2026-11-06.md): the exact finite cubic Wilson ground state Ω is positive, and a global Feynman–Kac heat-kernel argument certifies **e^(−2Λ)≤ρ_X≤e^(2Λ)** with Λ=64F/g₀⁴+E log(101/99). This is a genuine interacting-vacuum result with explicitly **nonuniform** constants, not a uniform weak-coupling bound. The centered normalized Wilson trace on a fixed physical loop has the exact first moment **−C′(0)=α L Eρ(1−W²/4)/Varρ(W)**, where the number L of elementary links doubles across dyadic refinement. The conditional two-scale inequality for |log(ρf/ρc)|≤δ is **k e^(−2δ)≤[−C′_f(0)]/[−C′_c(0)]≤k e^(2δ)** with k=4[g₀(h/2)²/g₀(h)²]; the true interscale δ estimate is still **OPEN**. Static marginal closeness alone therefore cannot establish unchanged short-time physics for the unrenormalized thin Wilson loop. A divergent ultraviolet first spectral moment does not imply a vanishing infrared gap. Source-response Hellinger estimates contain the inverse finite spectral gap Δ and cannot be used circularly to prove a uniform lower bound on that same gap. **Next**: noncircular boundary-local estimates, physically renormalized/smeared gauge-invariant observables, and full energy-dependent interacting Schur-form comparisons uniform in h,R.

## P0–P2 interacting-vacuum local Wilson map and effective shorted form (2026-11-06; finite only)

[Exact conditional-vacuum theorem](../../research/theorems/R3_VACUUM_WEIGHTED_OBSERVABLE_MAP_AND_SCHUR_FORM_2026-11-06.md): each **finite** cubic Wilson SU(2) Hamiltonian has a smooth strictly positive gauge-invariant ground state Ω. Relative to Ω² dHaar, the same eight physical boundary holonomies define a finite **vacuum-preserving** conditional expectation and normalized centered Wilson observable. Its coarse electric form is exactly a positive weighted diffusion with coefficient `a=α_h` on the original coarse links or `a=2α_(h/2)` on their two-link products, and smooth induced potential `v=a (Δ sqrt(ρ))/sqrt(ρ)`. The eliminated-sector influence is an explicit conditional variance of the vacuum logarithmic-score drift. Since its offdiagonal term can be **unbounded**, the mathematically correct full Schur object is the variational shorted form `inf_(q in Q) [E(f+q)+z||f+q||²]` at `z>0`. A source-independent finite SU2 gauge-graph counterexample shows that identical static coarse laws and first-time generators can still have **strictly different all-positive-time correlations**. This is a finite local observable **candidate**, **not** a uniform renormalization theorem, 4D mass gap, 3D Penrose action, or gravitational UV theorem. **OPEN requirement:** control the actual interacting marginals, induced potentials, conditional-score variance and complete energy-dependent shorted forms across h→h/2 and spatial volume with a common physical time scale.
## P0–P2 full Wilson exponential plus temporal blocking memory (2026-11-06; finite review)
## Exact P/Q influence across genuine cubic dyadic refinement (2026-11-06; finite only)

[Finite cubic two-time influence and dyadic scaling theorem](../../research/theorems/R3_EXACT_TWO_TIME_INFLUENCE_AND_DYADIC_SCALING_2026-11-06.md): on a genuine original-link SU(2) `2×2×1` slab and its same-physical-region `4×4×2` refinement, retain the same eight original coarse boundary holonomy products by normalized Haar conditional expectation. Every distinct pair of elementary plaquettes has a unique unretained edge and SU(2) Schur orthogonality gives **the sharp all-coarse-state** `B*B=(beta_h² F_h/4)P`, with `B=QHP=QVP`. The exact continuous-time projected dynamics are non-Markovian with memory `M_h(t)=B*exp(-tD)B`, `D=QHQ`, and the energy-dependent Feshbach self-energy `Σ_h(z)=B*(D+z)^(-1)B`. The positive symmetric heat-kernel transfer has an exact discrete Volterra recurrence with memory bounded in operator norm by `epsilon² beta_h² F_h/4`, at fixed h. On the same physical boundary variables the bare memory strength changes by the **exact ratio** `(128/5)[g0(h)/g0(h/2)]⁴`. Explicit positive finite interacting resolvent bounds exist, but the two-scale difference is **not summably small** along the required weak-bare-coupling trajectory. This does not constitute a continuum mass gap, a 3D Penrose regulator or a gravitational ultraviolet theorem. The decisive missing step is a renormalized connected physical-time/Schur-complement comparison with uniform h/volume control.


[Full 3D Wilson shell/time-memory proof](../../research/theorems/R3_FULL_WILSON_3D_SHELL_AND_TEMPORAL_MEMORY_2026-11-06.md) upgrades the prior truncated plaquette weight to **the complete Wilson exponential** on a 2×2×1 spatial cubical slab. Exactly four complementary five-face caps survive at the first transverse support; their SU(2) all-spin character kernel is explicit, with a uniform remainder bound for supports of eight or more. At arbitrary fixed bottom coupling the fifth shell Taylor coefficient is `(∂_b+4a₀'/a₀)Z_planar/16`, and the *same cap* has a seventh-order correction. The finite physical-time Kogut–Susskind heat-kernel transfer is positive, but its Haar-compressed two-step memory satisfies `PT²P−(PTP)²=PT(I−P)TP≥0`; on the 20-face test slab its vacuum leading coefficient is `ε²×5β_h²`. Thus no purely static/Markovian Haar-compressed spatial potential is an exact physical-time blocking rule. This **does not** prove a continuum divergence or positive mass gap; multiscale influence-kernel control and nontrivial 4D OS reconstruction remain OPEN. Source-independent checks are in [the executable verifier](../../research/scripts/verify_wilson_shell_time_2026_11_06.py). The source carries the exact model/coupling domains.



## Finite three-dimensional transverse-shell result · scope-limited (2026-11-06)

The first full `2×2×1` cubic spatial slab about a four-face block has 20 plaquettes, including 12 transverse xz/yz faces. For the **positive truncated** SU(2) magnetic weight `1+λ tr U_p` (not the Wilson exponential or time-transfer action), exact Haar integration of 25 interior links gives `Z(U;λ)=P0(λ)+P1(λ)χ1(U)+E12`, with `P0=1+λ⁶/4+λ¹⁰/64`, `P1=λ⁴/8+λ⁸/32+λ¹⁰/128`, and an explicit finite sup-norm bound on `E12`. A single transverse cubical bulge supplies `λ⁸χ1/32`, the first shell correction; the full 16-face outer sphere supplies the **exact adjoint character coefficient** `λ¹⁶/16384`. This calculation checks actual **3D spatial** magnetic coupling, but is **not** a physical-time interacting correlation estimate, a 3D Wilson-exponential RG theorem, a refinement-uniform estimate, or a Penrose equivalence. It **closes no P0–P5 or T0–T5 gate**.

See [exact 3D transverse-shell report](../../research/theorems/R3_CUBIC_FIRST_TRANSVERSE_SHELL_CHARACTER_BLOCK_2026-11-06.md) and its [reproducible verifier](../../research/scripts/verify_cubic_transverse_shell_2026_11_06.py). The 2²⁰ squarefree face configurations were enumerated independently; only 32 pass the Haar center-parity test, while all higher-order non-manifold channels were bounded without unjustified factorization. The next step is **the full Wilson exponential plus temporal heat-kernel transfer, with the nonabelian recoupling channels included**, not a claim of a continuum gap.

The numbering **P0–P5** follows the dated [publication audit](../../research/audits/SINGULAR_BOUNDARY_PUBLICATION_PROOF_MAP_2026-11-01.md), with later records retained as additional evidence rather than erasing that audit.

## 2026-11-05 source-faithful model hierarchy (draft correction)

The **original dissertation goal** is a Penrose/Fibonacci/coupled-ℤ⁵ spectral quantum-gravity hypothesis, not merely an SU(2) mass-gap proof. Its original periodic comparison is the **square 2D spatial control**. Stage 7/26 experiments use area-matched Penrose/square **2+1D SU(2)** ensembles; cubic 3D is a later independent control, not an equivalent Penrose regulator.

P0 requires separate model-indexed subcertificates: **P0-H** for historical Penrose/coupled-ℤ⁵ geometry and spectral operator, **P0-C** for square and cubic controls, and **P0-X** for the correctly normalized same-observable comparison. The P0–P5 diagram below applies **only to the separate Yang–Mills theorem objective**. Paper 2's reported spectral-zeta difference is not a result of Stage26 scalar Monte Carlo; neither is a gravitational finiteness theorem. P3 is Penrose-route-specific, while Git LFS is reproducibility infrastructure and not a mathematical prerequisite.

[Read the detailed P0 hierarchy and evidence audit](P0_MODEL_HIERARCHY_PENROSE_CONTROL_AUDIT_2026-11-05.md).

## P0/T2 exact two-scale SU(2) blocking results (2026-11-05; review draft)

Three model-scoped original-link cubical calculations are now available: (1) the gauge-compatible holonomy-product cylinder injection has **scalar fine magnetic Hamiltonian compression** under product-Haar conditional expectation, and a nonzero bare operator leakage; (2) the **four** fundamental characters of one dyadically subdivided coarse face have joint conditional expectation equal to **one-eighth of the coarse fundamental Wilson character**, while every nonempty proper squarefree subset vanishes; (3) an **isolated planar SU(2) central-weight block** has the exact character expansion `Z_B(U)=Σ_n a_n(t)^F/(n+1)^(F−1) χ_n(U)`, with leading 2×2 fundamental coefficient `t^4/8` and independently generated higher representations.

These are exact **kinematic / isolated planar** identities, NOT an interacting full-three-dimensional effective action or a physical-time correlation inequality. Transverse cubical plaquettes prevent the planar integral from factoring in the complete 3D model. Neither the P0 physical regulator-universality condition nor the P2 interacting, h- and R-uniform renormalization estimate is closed. The next test must include at least the first transverse plaquette shell and a physical-time transfer observable; quasicrystalline T0–T5 and the separate quantum-gravity operator remain OPEN.

[Haar magnetic-loss theorem](../../research/theorems/R3_CUBIC_HAAR_BLOCK_MAGNETIC_LEAKAGE_2026-11-05.md) · [four-plaquette recovery](../../research/theorems/R3_CUBIC_FACE_BLOCK_HAAR_RECOVERY_2026-11-05.md) · [exact isolated planar character blocking](../../research/theorems/R3_SU2_PLANAR_BLOCK_CHARACTER_TRANSFER_2026-11-05.md).

## 2026-11-05 ultraviolet and quasicrystal transfer contract (draft)

**A finite cubic 3D SU(2) gap is not the 4D continuum mass gap.** R3-IR-589's full finite-Gauss-space sufficient estimate is Δ_h≥[3g₀²/2−2F/g₀²]/h with F=3n²(n+1), h=1/n. Its positive lower-bound criterion g₀⁴>4F/3 forces *large* bare coupling under refinement, whereas asymptotic freedom requires g₀(h)→0. The separate periodic weak-perturbation Yarotsky application applies for small z=4/g₀⁴, also outside the ultraviolet z→∞ trajectory. These are limitations of particular proof certificates—not counterexamples to the physical mass gap.

**Model-transfer interfaces (all OPEN or conditional):** T0 genuine 3D quasicrystal refinement; T1 same-action Gauss-invariant original-link quantum dynamics; T2 renormalized physical observable map; T3 interacting, all-large-physical-time exponentially weighted correlation comparison uniform in h and spatial volume; T4 nontrivial 4D OS reconstruction; T5 spectral support transfer on a dense physical observable set. Small finite-time or unweighted correlation differences do not preserve spectral exclusion. The source operator relevant to a proposed gravitational ultraviolet mechanism is an **additional independent interface**. [Read the quantified audit and counterexample](YM_CUBIC_PENROSE_TRANSFER_AND_INFRARED_GATES_2026-11-05.md).

The following historic P0–P5 diagram is specifically a **Yang–Mills theorem dependency map**. P3 is a route-specific quasicrystalline mechanism, not a universal axiom. The 2+1D Penrose/square comparison is not itself a 3D continuum regulator.

```text
P0 source, model, topology, Gauss sector, and normalization
  |--> P1 original-link operator/orientation and exact score identity
  |       '--> P2 intrinsic PW inverse + connected recurrence + radius control
  |                      '--> λ=1 interacting chain theorem [OPEN]
  |--> P3 deleted-face Wilson current and completed-cage anti-depletion [OPEN]
  |--> P4 physical source-visible spectrum and infrared estimates [OPEN]
  '--> P5 continuum/OS reconstruction + physical positive gap [OPEN]
            (requires its own stated noncircular inputs)
```

## P1 correction chain (read both, do not choose by filename date)

- [Three-face earlier discrepancy](../../research/theorems/R3_IR_THREE_FACE_QUADRATIC_QUARTIC_COUPLING_2026-11-01.md)
- [Shared-edge convention reconciliation](../../research/theorems/R3_IR_SHARED_EDGE_SIGN_RECONCILIATION_2026-11-01.md)
- [Canonical shared-link orientation](../../research/theorems/R3_IR_CANONICAL_SHARED_LINK_RECONCILIATION_2026-11-01.md)
- [Physical operator re-audit](../../research/theorems/R3_IR_PHYSICAL_OPERATOR_REAUDIT_2026-11-01.md)
- [Lower-order three-face re-audit](../../research/theorems/R3_IR_THREEFACE_LOWER_ORDER_REAUDIT_2026-11-01.md)
- [Cross-operator consistency](../../research/theorems/R3_IR_CROSS_OPERATOR_CONSISTENCY_2026-11-01.md)

This *documents* a local reconciliation; it does not mean every score recurrence from older archives has been independently reverified. The previous publication map's unresolved P1 warning remains a historical snapshot to be reread in light of the correction chain.

## P2 exact finite calculations and analytic effort

- [Three-face full fourth-order Poisson solution](../../research/theorems/R3_IR_THREEFACE_FULL_FOURTH_ORDER_POISSON_2026-11-01.md)
- [Four-face exact connected S4](../../research/theorems/R3_IR_FOURFACE_CONNECTED_S4_EXACT_2026-11-01.md)
- [All-length free PW spectrum](../../research/theorems/R3_IR_EXACT_ALL_LENGTH_PETER_WEYL_SPECTRUM_2026-11-01.md)
- [Intrinsic PW analytic inverse](../../research/theorems/R3_IR_INTRINSIC_PW_ANALYTIC_INVERSE_2026-11-01.md)
- [Compatible PW analytic bilinear](../../research/theorems/R3_IR_PW_ANALYTIC_BILINEAR_2026-11-01.md)
- [Formal connected Gevrey-8](../../research/theorems/R3_IR_FORMAL_CONNECTED_GEVREY8_2026-11-01.md)
- [Later Gevrey-2 scalar/connected records](../../research/theorems/R3_IR_CONNECTED_GEVREY2_OPTIMAL_SCALAR_2026-11-01.md)
- [Radius-loss obstruction](../../research/theorems/R3_IR_PW_RADIUS_MAJORANT_OBSTRUCTION_2026-11-01.md)

An attempted majorant must state the support/interval constant, derivative losses, (sigma-sigma') budget, recursion convention, and whether it proves merely formal coefficient growth or genuine convergence.

## P3–P5 remain logically separate

[Penrose signed current](../../research/problems/R3-IR.md), [physical-time and infrared obligations](../../research/problems/R3-IR.md), [continuum R2](../../research/problems/R2.md), and [separate historical prism geometry](../../research/problems/R3-PRISM.md). Explicit source-to-Hamiltonian equivalence is a P0 prerequisite, not an inference from numerical agreement.


## PF-I16 pointwise Kato–Bochner and derivative-flow checkpoint (2026-11-10)

The finite-product vector Bochner equation for
\[
\mathscr G=\Delta_{\widetilde g}-2\nabla_{\nabla\Phi},
\qquad
\widetilde g=\bigoplus_e a_e^{-1}g_e
\]
has Bakry–Émery endomorphism \(\operatorname{Ric}^{\sharp}+2(\nabla^2\Phi)^\sharp\). Since the product connection preserves link tangent blocks and \(\operatorname{Ric}^{\sharp}|_{T_e}=(a_e/2)I\), Kato's inequality followed by the finite-product scalar maximum principle gives a componentwise cooperative upper-Dini inequality. The refined face blocks yield the weighted comparison matrix and the conditional derivative-flow estimate with kernel prefactor one:
\[
\|D_eP_tf\|_\infty\le e^{-\lambda t}
\sum_g25^{-d(e,g)}\|D_gf\|_\infty,\quad
\lambda=\frac{a_0}{2}-\frac{53312}{3}b_0
-\frac{389120}{3}\frac{b_0^2}{a_0}.
\]
At \(b_0/a_0\le1/40000\), \(\lambda\ge26087a_0/468750>0.0556522a_0\). The kernel has row and column sums at most 13, while convolution requires spatial-exponent loss. For a finite-link-supported observable, the resulting oscillation bound is \(26\pi e^{-\lambda t}\sum_{g\in S}\|D_gf\|_\infty\).

See [the pointwise Kato–Bochner theorem record](../../research/theorems/PF_I16_POINTWISE_KATO_BOCHNER_DERIVATIVE_FLOW_2026_11_10.md). This closes the componentwise Kato/Duhamel bridge **conditional on** the refined face-Hessian blocks, which in turn retain the isolated-rotor gradient and four-factor group-product hypotheses. The standalone sign/trivialization/regularization audit remains next. All P0–P5 and PF-G0–G5 gates remain OPEN; no physical-time normalization, continuum reconstruction, all-orders summability or Yang–Mills mass gap is claimed.

### Corrected rotor estimates after the linear-response obstruction

The radial ODE itself yields the replacement bound \(-2\beta\le s_\beta'\le0\), hence \(\|s_\beta'\|_\infty\le2\beta\), and the weighted-mean identity then yields \(\|\nabla^2s_\beta\|_{\rm op}\le\frac43\beta+\frac{80}{3}\beta^2\). The corrected provisional face blocks are \(h_d\le\frac{32}{3}b_0+\frac{1280}{3}b_0^2/a_0\) and \(h_o\le\frac{56}{3}b_0+\frac{1280}{3}b_0^2/a_0\). At \(b_0/a_0\le1/50000\), the corresponding unweighted curvature and \(\log25\)-weighted derivative-flow margins are respectively \(>0.4786a_0\) and \(>0.0483a_0\), conditional on the remaining Bochner and product-Hessian estimates. The shared-link residual magnitude becomes \(4160b_0^2/a_0\); corrected derivative ceilings and derivations are in the obstruction/repair audit. The previous blocks, residual constants, \(1/40000\) threshold and third-order prefactor are superseded. The exact-rational arithmetic regression is [here](../../research/verification/verify_pf_i16_corrected_rotor_constants.py). This repair does not establish all-orders summability or close a canonical gate.



## PF-I16 · 2026-11-13 finite-order spatial-tree update

This later checkpoint supersedes the earlier statements above that no third-order spatial tree had been proved and that fourth-order partition cancellation was still the next unclosed fixed-order task. It does **not** close a canonical P0–P5 or PF-G gate.

1. **Corrected isolated rotor.** From the radial ODE and regular endpoint conditions, the maximum principle gives $-2\beta\le s_\beta'\le0$. The weighted-mean identity then gives the corrected Hessian bound $\|\nabla^2s_\beta\|_{\rm op}\le\frac43\beta+\frac{80}{3}\beta^2$. The corrected face-block, curvature, derivative-flow and residual constants are recorded in the [rotor repair audit](../../research/audits/PF_I16_ISOLATED_ROTOR_FIRST_DERIVATIVE_OBSTRUCTION_2026_11_11.md) and checked arithmetically by [the rational verifier](../../research/verification/verify_pf_i16_corrected_rotor_constants.py). These analytic transfer estimates remain conditional on the face-map metric/pullback and finite-product Kato–Bochner comparisons.

2. **Third-order spatial tree.** The [Dobrushin third-order record](../../research/theorems/PF_I16_DOBRUSHIN_THIRD_ORDER_TREE_BOUND_2026_11_13.md) derives a weighted influence norm $\|C\|_{\log25}\le12\pi/125<264/875<1$ for the finite-volume dressed reference measure. With the Föllmer covariance inequality and corrected derivative-flow input, it proves a volume-independent support-MST tree bound for each ordered third-order term and hence the complete six-permutation coefficient. Its exponent is $\eta=\frac18\log(25/23)>0$. This is conditional and concerns $d\nu_\Phi$, not the actual interacting Wilson-vacuum measure.

3. **Fourth-order spatial tree.** The [cut-interpolation record](../../research/theorems/PF_I16_FOURTH_ORDER_CUT_INTERPOLATION_TREE_BOUND_2026_11_13.md) retains the full four-source coefficient under a separating cut and derives a finite volume-independent prefactor $\mathcal C_{1234}$ with exponent $\eta_4=\frac1{24}\log(25/23)>0$. This is a conditional fixed-order result, uniform along the interpolation only if the corrected derivative-flow and face-map metric/pullback inputs hold.

4. **Separate reference-path cumulant route.** The [joint space-time cluster record](../../research/theorems/PF_I16_JOINT_SPACETIME_CLUSTER_TREE_OPEN_GATE_2026_11_13.md) also proves an order-four support-sensitive maximum-tree inequality for four elementary-tensor insertions. Its crude constant is finite but enormous, and the actual PF-I16 insertion projective norms are not controlled sufficiently to use it as an activity bound. The absolute all-orders Leonov–Shiryaev envelope is superfactorial. The exact link-factorization identity for Boolean quasi-factorization variables is established, but the analytic one-link majorant and connected-subset resummation with $K_8^k$ growth remain open.

5. **Still open.** A uniform bound on the cut-response prefactors $\mathcal C_n$, the all-orders cancellation-preserving joint space/time tree theorem, actual quantum connected-resolvent/KP convergence at the intended coupling, stability in the physical interacting vacuum, source-derived physical kinetic/time normalization, a genuine refining physical 3D regulator, continuum reconstruction and a positive physical mass gap.

No result above imports R3-IR constants or establishes a theorem for the physical continuum Yang–Mills theory.


## PF-I16 finite-product face-pullback and Kato–Bochner closure (2026-11-13)

The companion [face-pullback/Kato–Bochner closure audit](../audits/PF_I16_FACE_PULLBACK_KATO_BOCHNER_CLOSURE_2026_11_13.md) discharges the finite-model metric-pullback and pointwise Kato comparison under the universal incidence (d_e\le8), allocation bounds (A_f\ge a_0/2), (a_e\le8A_f), and weak-coupling condition (b_0/a_0\le1/50000). Thus the corrected derivative-flow estimate is a finite-accepted-graph theorem, uniform in graph volume, with (kappa\ge0.478655744a_0) and (lambda_{\log25}\ge0.048379136a_0). It does not supply physical-time normalization or the interacting-vacuum/continuum gap.

The conditional Dobrushin third-order support-tree result and fourth-order cut-interpolation support-tree result therefore have proved finite dressed-reference inputs under the same source-incidence and weak-coupling hypotheses. The actual quantum connected-resolvent/KP theorem, all-orders activity convergence, interacting Wilson-vacuum stability, source-derived physical time, refining physical 3D regulator, continuum reconstruction and physical mass gap remain OPEN.
