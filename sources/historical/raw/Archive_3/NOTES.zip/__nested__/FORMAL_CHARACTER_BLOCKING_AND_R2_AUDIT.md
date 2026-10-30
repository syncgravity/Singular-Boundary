# The Singular Boundary: exact first Wilson-character blocking, neutral source, and R2 normalization

**Date:** 26 October 2026. **Result:** exact one-link/one-face character blocking and first neutral Wilson source insertion **proved**; fixed-spatial-complex continuous-time Hamiltonian limit **proved**; all-scale neutral-sector infrared suppression and spatial continuum coercivity **not proved**. No Monte Carlo calculation is used.

## 0. Scope, provenance, and what the previous program does not establish

The finite graph is an oriented cell complex \(G=(V,E,F)\), with SU(2) on its spatial links. The physical space is \(\mathcal H_{\rm phys}=L^2(SU(2)^E)^{SU(2)^V}\), product normalized Haar measure, and \(p_f(U)=\frac12\chi_{1/2}(W_f(U))\in[-1,1]\). The temporal Wilson weight on one link is \(k_\beta(U)=\exp(\beta p(U))\). Couplings may vary among links and faces but are positive.

The directly provided `penrose_2p1_study.py` in `penrose_yang_mills_2p1_causal_study.zip` has the explicit geometrical rule `bs=beta_ref*a_ref*dt/farea`, `bt=beta_ref*a_ref/dt*wt`, `wt=(area_left+area_right)/(2*edge_length**2)`; its extrusion uses 4-link temporal ribbons at each spatial edge, including a periodic Euclidean time seam. This is evidence for that **related specified action class**, not certification of the 2026 Stage 26 production couplings: Stage 26 imports `stage7_checkpointed.setup_geometry`, and that defining file was not recovered among the accessible sources. At fixed beta_ref=3.5, Nt=20, the Stage 26 campaign is **not a spatial continuum trajectory**.

We distinguish exact **representation/character blocking**, which is integration over links or time slices, from **infrared spectral blocking**, which estimates the excited-state projector of the *interacting* Hamiltonian. The former does not imply the latter.

## 1. Exact SU(2) character transfer coefficients (Theorem C1)

Normalize Haar measure to mass 1. For spin \(j\in\{0,1/2,1,\dots\}\), write \(d_j=2j+1\), \(\chi_j\) for its character, and \(I_n\) for the modified Bessel function. The Weyl integration formula and \(\sin^2\theta\,\chi_j(\theta)=\sin\theta\sin(d_j\theta)\) yield
\[
 a_j(\beta)=\int_{SU(2)}k_\beta(g)\chi_j(g)\,dg
 =I_{2j}(\beta)-I_{2j+2}(\beta)
 =\frac{2d_j}{\beta}I_{2j+1}(\beta).
\]
For \(\beta>0\), \(a_j>0\); \(a_0=2I_1(\beta)/\beta\). The normalized central probability density
\[
 K_\beta(g)=k_\beta(g)/a_0(\beta)
 =\sum_j d_j\rho_j(\beta)\chi_j(g),\qquad
 \rho_j(\beta)=\frac{I_{2j+1}(\beta)}{I_1(\beta)},\quad \rho_0=1
\]
has link-convolution eigenvalue \(\rho_j\) on every matrix element of spin \(j\) (Schur orthogonality). In particular \(0<\rho_{1/2}(\beta)<1\), \(\rho_{1/2}(\beta)=I_2(\beta)/I_1(\beta)\). The large-\(\beta\) expansion for fixed \(j\) is
\[
 \rho_j(\beta)=1-\frac{2j(j+1)}{\beta}+O(\beta^{-2});\qquad
 \rho_{1/2}=1-\frac{3}{2\beta}+O(\beta^{-2}).
\]
The character expansion is absolutely convergent at finite beta by smoothness of the compact-group density.

## 2. Exact first *spatial* link decimation and source insertion (Theorem C2)

For a pair of adjacent oriented rhombus plaquettes sharing an edge, write their holonomies as \(AU\) and \(U^{-1}B\), with all other edge variables fixed. Then Schur orthogonality gives
\[
 \int dU\,\chi_j(AU)\chi_k(U^{-1}B)
   =\frac{\delta_{jk}}{d_j}\chi_j(AB).
\]
Thus integrating out the common link exactly produces the fused-loop weight
\[
 \boxed{\int dU\,K_{\beta_1}(AU)K_{\beta_2}(U^{-1}B)
  =\sum_jd_j\rho_j(\beta_1)\rho_j(\beta_2)\chi_j(AB).}
\]
The fundamental character eigen-ratio after this one idealized fusion is \(\rho_{1/2}(\beta_1)\rho_{1/2}(\beta_2)\). This **is** a contraction at each fixed positive beta, but no strictly subunit constant is uniform as both couplings approach infinity, because \(\rho_{1/2}(\beta)\to1\). Moreover the full Penrose lattice has other incident plaquettes and shared links: this two-face formula is an exact local building block, not an exact full-lattice RG transformation.

A normalized centered Wilson source at the first face is obtained by differentiation. Set \(m_0(\beta)=d\log a_0(\beta)/d\beta\). Then
\[
 (p(AU)-m_0(\beta_1))K_{\beta_1}(AU)=\partial_{\beta_1}K_{\beta_1}(AU).
\]
Accordingly,
\[
 \boxed{\int dU\,(p(AU)-m_0(\beta_1))K_{\beta_1}(AU)K_{\beta_2}(U^{-1}B)
 =\sum_{j>0}d_j\rho_j'(\beta_1)\rho_j(\beta_2)\chi_j(AB).}
\]
This is a **nonzero, gauge-invariant, center-neutral source insertion** on the fused loop. The derivative subtraction centers the source relative to the *isolated one-plaquette weight*; it does **not** center it relative to the full interacting many-face ground state. The presence of all \(j\) precludes deducing a norm or interacting infrared contraction from the \(j=1/2\) factor alone.

## 3. Exact first *temporal* blocking with a neutral Wilson source (Theorem C3)

Let the normalized free temporal operator be \(C_{\Delta t}=\bigotimes_{e\in E}C_{\beta_{t,e}}\), restricted to the gauge-invariant Hilbert space. Let
\[
 B=\sum_fb_f(1-p_f),\quad b_f\ge0,\qquad
 T_{\Delta t}=P e^{-\Delta t B/2}C_{\Delta t}e^{-\Delta t B/2}P.
\]
Since \(P\) commutes with all factors on the full space, the **exact** doubled temporal transfer operator is
\[
 \boxed{T_{\Delta t}^{2}
 =P e^{-\Delta t B/2}C_{\Delta t}e^{-\Delta t B}C_{\Delta t}e^{-\Delta t B/2}P.}
\]
The middle slice includes the full interacting source factor \(e^{-\Delta t B}\). For one plaquette with \(B=b(1-p)\), its middle insertion is
\[
 C_{\Delta t}e^{-\Delta t b(1-p)}C_{\Delta t}
 = e^{-\Delta t b}\big[C_{\Delta t}^{2}
 +\Delta t b\, C_{\Delta t}M_pC_{\Delta t}
 +O((\Delta t b)^2)\big]
\]
in bounded-operator norm at fixed \(\Delta t b\to0\), where \(M_p\) multiplies by \(p\) and \(\|M_p\|\le1\). A uniform local error estimate for this single insertion is \(\|e^{xM_p}-I-xM_p\|\le(x^2/2)e^{|x|}\), \(x=\Delta t b\). It is **not** a bound for the sum of all plaquettes at arbitrary spatial volume.

For a single open rhombus gauge complex, gauge invariants are class functions of the loop holonomy \(W\). The characters \(|j\rangle=\chi_j(W)\) are orthonormal, with
\[
 C_{\Delta t}|j\rangle=r_j|j\rangle,
 \quad r_j=\prod_{e\in\partial f}\rho_j(\beta_{t,e}).
\]
The exact SU(2) tensor-product identity gives \(\chi_{1/2}\chi_j=\chi_{j+1/2}+\chi_{j-1/2}\) (omit the negative label), and therefore
\[
 \boxed{\langle j'|C_{\Delta t}M_pC_{\Delta t}|j\rangle
 =\frac12r_jr_{j'}\,[\mathbf 1_{j'=j+1/2}+\mathbf 1_{j'=j-1/2}].}
\]
In particular \(\langle\tfrac12|C_{\Delta t}M_pC_{\Delta t}|0\rangle=r_{1/2}/2\ne0\), whereas \(\langle\tfrac12|C_{\Delta t}^2|0\rangle=0\). This **proves** that even the first neutral Wilson source creates representation mixing not captured by squaring isolated-link eigenvalues. The insertion is gauge invariant and 1-form-center neutral (its loop is contractible).

The **complete** one-step interacting transfer operator on this single-rhombus space already has a nonvanishing vacuum-to-loop entry. Expanding both half-potential factors for \(x=\Delta t b\to0\), with \(r=r_{1/2}\), gives
\[
 \boxed{\langle\tfrac12|T_{\Delta t}|0\rangle=\frac{x}{4}(1+r)+O(x^2),\qquad
 \langle\tfrac12|T_{\Delta t}^{2}|0\rangle=\frac{x}{4}(1+r)^2+O(x^2).}
\]
The first formula follows from \(T=C-\tfrac{x}{2}[(I-M_p)C+C(I-M_p)]+O(x^2)\), together with \(\langle\tfrac12|M_p|0\rangle=1/2\). The second is the product of the first-order one-step matrix elements with the diagonal free \(C\); it equivalently includes both endpoint and midpoint source insertions. The error constants here are for this **single bounded plaquette term** and are not asserted uniform in the number of faces.


On a larger Penrose patch, \(M_{p_f}\) couples spin networks according to Clebsch-Gordan intertwiners, so the one-loop Jacobi rule is a demonstrative *subcomplex* computation, not a general closed form for the many-plaquette kernel.

## 4. What iteration would have to prove, and why it does not follow (Obstruction C4)

(i) The free link block satisfies exact \(C_{\Delta t}^2\) eigenvalues \(\rho_j(\beta_t)^2\). (ii) Once \(B\ne0\), time blocking instead inserts \(e^{-\Delta t B}\) between convolutions. The explicit nonzero off-diagonal matrix element above shows that the blocked operator **does not remain diagonal** in the free character basis. (iii) At fixed \(a_s\), \(\Delta t b_f\to0\) permits a controlled infinitesimal source expansion, yielding the interacting Hamiltonian. (iv) On a spatial refinement with \(a_s\sim\Delta t\to0\), the geometric Wilson prescription gives \(\Delta t b_f\asymp \Delta t/a_s^2\asymp1/a_s\), which diverges; there is no uniform first-order-in-plaquette-source bound. (v) Neither \(\rho_j^2\) nor the one-face mixing calculation bounds the low-energy projector \(P_{(0,s]}(H-E_0)\) in the many-face **center-neutral** sector.

For an actual R3 closure, one must derive and prove a blocked **interacting** map \((S_n,\mathcal O_n)\mapsto(S_{n+1},\mathcal O_{n+1})\) on gauge-invariant effective actions *and source insertions*, with all newly generated higher-representation and multi-loop interactions controlled by a weighted local/polymer norm; a patch-independent estimate on its connected source transfer; a genuine neutral-sector low-energy decay estimate such as \(F_A(s)\le C s^p\) with \(p>1\), or stronger \(F_A(s)=0\) for \(s<m\); and control of all scale errors. A decay estimate only for special commutator sources or only in center-charged forbidden sectors cannot close this gate.

The failure of this **particular** microscopic contraction/first-order expansion does not prove the Wilson theory is gapless, and it does not rule out a different nonperturbative multiscale mechanism.

## 5. R2a is closed: continuous-time normalization at any **fixed** finite spatial graph (Theorem T1)

Choose an anisotropic temporal continuum family with electric coefficients \(a_e>0\) and magnetic coefficients \(b_f\ge0\) **fixed in physical Hamiltonian units** as \(\Delta t\to0\):
\[
 \beta_{t,e}(\Delta t)=\frac{2}{a_e\Delta t},\qquad
 \beta_{s,f}(\Delta t)=b_f\Delta t.
\]
The normalized temporal Wilson convolution has \(\rho_j(\beta_{t,e})=1-a_e j(j+1)\Delta t+O(\Delta t^2)\) for each fixed spin \(j\). Thus on the dense finite Peter-Weyl span,
\[
 \lim_{\Delta t\downarrow0}\frac{C_{\Delta t}-I}{\Delta t}\psi=-\sum_ea_e(-\Delta_e)\psi.
\]
Multiplication by the bounded \(e^{-\Delta t B/2}\) then gives the derivative \(-H\psi\), \(H=\sum_e a_e(-\Delta_e)+B\), on this core. All \(T_{\Delta t}\) are self-adjoint positive contractions (\(B\ge0\)) and preserve the physical subspace. The product/Chernoff semigroup theorem therefore yields, for fixed \(t\ge0\),
\[
 \boxed{\lim_{\Delta t\downarrow0} (T_{\Delta t}|_{\rm phys})^{\lfloor t/\Delta t\rfloor}\psi
 =e^{-tH_{\rm phys}}\psi\quad\text{strongly}.}
\]
The statement uses \(T_{\Delta t}\) normalized by the *trivial convolution coefficient* \(\prod_ea_0(\beta_{t,e})\), not by the unknown interacting top eigenvalue. The ground-energy subtraction \(E_0\) can be performed **after** the fixed-graph Hamiltonian is defined. The infinite-dimensional on-link spaces cause no problem for this fixed finite-graph core argument.

**Specialization to the provided geometrical rule.** The related study code sets
\[
 \beta_{s,f}=\beta_{\rm ref}\frac{a_{\rm ref}\Delta t}{A_f},\qquad
 \beta_{t,e}=\beta_{\rm ref}\frac{a_{\rm ref}}{\Delta t}w_e,
 \quad w_e=\frac{A_{f_L}+A_{f_R}}{2\ell_e^2}.
\]
For standard SU(2) Wilson normalization \(\beta_{\rm ref}a_{\rm ref}=4/g_3^2\), this gives
\[
 \boxed{a_e=\frac{g_3^2}{2w_e},\qquad b_f=\frac{4}{g_3^2 A_f}.}
\]
Thus the anisotropic Wilson transfer construction tends to the specified **inhomogeneous Kogut-Susskind Hamiltonian** at fixed spatial geometry, rather than to a fictitious heat-kernel model. If a different beta convention or independently mean-rescaled coupling set is used, its physical \(a_e,b_f\) must be calculated from its own limits; the same formula cannot be transferred silently.

## 6. R2b is NOT closed: the simultaneous Penrose spatial continuum trajectory

Scale a fixed-shape rhombus prototype geometry as \(A_f(a)=a^2\widehat A_f\), \(\ell_e(a)=a\widehat\ell_e\), so \(w_e\) is scale independent and uniformly bounded above/below on appropriate face-complete interior patches. At fixed physical \(g_3^2\),
\[
 a_e(a)=g_3^2/(2w_e)=O(1),\quad b_f(a)=4/(g_3^2a^2\widehat A_f)=O(a^{-2}),\quad b_f(a)/a_e(a)=O(a^{-2}).
\]
Consequently the \(\Delta t b_f\) source expansion is controlled only when \(\Delta t=o(a^2)\) as a *local* sufficient condition; setting \(\Delta t\asymp a\) gives an uncontrolled small-source expansion. Choosing an extreme anisotropy does **not** establish the spatial continuum mass gap, because it still leaves the whole interacting spatial Hamiltonian as \(a\to0\).

The exact physical-energy gap and transfer eigenvalue criterion is
\[
 m_{a,L}=\frac{1}{\Delta t(a)}\log\frac{\lambda_0(T_{a,L})}{\lambda_1(T_{a,L})},\quad
 \inf_{a\ll1,L\in\mathcal L(a)}m_{a,L}>0
 \ \Longleftrightarrow\ \ 
 \frac{\lambda_1}{\lambda_0}\le e^{-m_*\Delta t(a)}.
\]
The eigenvalue ordering is within the **physical gauge-invariant** Hilbert space, and \(\lambda_0\) is its unique top eigenvalue. Importantly, a finite physical gap is compatible with \(\lambda_1/\lambda_0\to1\) when \(\Delta t\to0\); requiring a *fixed* per-step contraction \(<1\) is the **wrong continuum criterion**. The isolated-link ratio \(\rho_{1/2}(\beta_t)=1-O(\Delta t)\) is therefore a correct time discretization, not evidence of gap closing. What is not known is the analogous bound in the full neutral physical interacting spectrum with constants uniform as \(a\to0\), spatial volume varies, and boundaries are changed.

A true R2 closure additionally needs a rigorous gauge-invariant continuum Hilbert-space reconstruction; a common physical \(g_3^2\), matched anisotropy/metric normalization on the Penrose approximants; uniformly controlled source renormalization/smearing; uniform positivity and neutral spectral estimates; and boundary/thermodynamic-limit control. The Stage 26 fixed \(\beta_{\rm ref}=3.5\), \(N_t=20\) ensemble and its finite-sampling correlators do not provide these.

## 7. Research acceptance criteria and status

| Statement | Proof status |
|---|---|
| Exact SU(2) Wilson character coefficients and convolution | PROVED |
| Exact two-rhombus shared-link decimation | PROVED (isolated local subcomplex) |
| Exact normalized first-face Wilson source insertion | PROVED (isolated local subcomplex) |
| First interacting midpoint temporal source creates gauge-singlet representation mixing | PROVED (single rhombus), not an all-scale contraction |
| Uniform strict contraction from \(\rho_{1/2}^2\) along \(\beta\to\infty\) | FALSE as stated: \(\rho_{1/2}^2\to1\) |
| Full Penrose neutral-sector source RG iteration | NOT PROVED |
| R3 center-neutral low-energy spectral-weight suppression for all physical local observables | NOT PROVED |
| R2 fixed-spatial-graph continuous-time Wilson-to-KS semigroup normalization | PROVED |
| R2 spatial continuum reconstruction, uniform physical gap and boundary control | NOT PROVED |
| 4D continuum Yang-Mills mass gap | NOT PROVED; the above is 2+1D Hamiltonian gauge theory |

## 8. References

* J. Kogut and L. Susskind, *Hamiltonian formulation of Wilson's lattice gauge theories*, Phys. Rev. D **11**, 395 (1975), DOI 10.1103/PhysRevD.11.395.
* M. Creutz, *Gauge fixing, the transfer matrix, and confinement on a lattice*, Phys. Rev. D **15**, 1128 (1977), DOI 10.1103/PhysRevD.15.1128 (Wilson-to-Hamiltonian temporal limiting context).
* K. Osterwalder and E. Seiler, *Gauge field theories on a lattice*, Ann. Phys. **110**, 440–471 (1978), DOI 10.1016/0003-4916(78)90039-8 (reflection positivity and strong-coupling limits).
* Source-specific formulae from the user-provided `penrose_yang_mills_2p1_causal_study.zip/penrose_2p1_study.py` lines 65–79 and 98–111, plus `YM_2P1_CAUSAL_NOTE.md` lines 15–35.
* Deterministic checks are in `check_character_factors.py` and `character_factors_output.txt`, accompanying this note. Checks demonstrate arithmetic, not a proof of the multiscale spectral gap.

**Bottom line:** The requested first neutral Wilson-character blocking and insertion are explicitly calculated, and the fixed-spatial-graph time normalization is established rigorously. The source induces nonzero physical representation mixing. No model-derived, all-scale contraction or volume-/cutoff-uniform neutral physical infrared bound follows, so claiming a full R3 plus continuum R2 proof would be mathematically unsupported.
