# R3/R2 — Renormalized Wilson frames: exact operator identities, source-collapse counterexample and transfer reconstruction gates

**Status, 26 October 2026:** This note proves exact Hilbert-space and spectral/transfer identities, together with a counterexample to inferring a uniform gap from equal-time Wilson cumulants. It does **not** establish uniform infrared contraction or the 2+1-dimensional SU(2) Yang–Mills continuum gap.

## I. Scope

For a finite rhombus/square gauge graph, take the physical Hilbert space `\mathcal H_G=L^2(SU(2)^E)^{SU(2)^V}` and positive Hamiltonian `H=\sum_e a_e(-\Delta_e)+\sum_f b_f(1-p_f)`. Let `\Omega` be its unique normalized vacuum, `K=H-E_0\ge0`, `Q=1-|\Omega\rangle\langle\Omega|`, and `P_s=1_{(0,s]}(K)`. All energies below are in Hamiltonian physical-time units.

A finite or countable source family `b_i=Q A_i\Omega` with weights can be expressed as a bounded synthesis operator `B:\ell^2(I)\to Q\mathcal H`, `B c=\sum_i c_i\sqrt{w_i}b_i`, and its frame operator is `S=BB^*`. The Euclidean results of the earlier full-measure note are **spatially averaged equal-time bare-plaquette variance / conditional covariance bounds**, not estimates for `P_s S P_s` nor for `B^*e^{-tK}B`.

## II. Theorem: bare-field variance collapse gives no spectral-gap information

Let `v_h=\|QA_h\Omega_h\|^2` and assume `v_h>0`. Setting `\widehat A_h=(A_h-\langle A_h\rangle)/\sqrt{v_h}` gives `\|\widehat A_h\Omega_h\|=1` and
\[
\|P_s\widehat A_h\Omega_h\|^2=\frac{\|P_s QA_h\Omega_h\|^2}{v_h}.
\]
The bare upper bound `\|P_sQA_h\Omega_h\|^2\le v_h` reduces to `\le1` after renormalization: it supplies no positive power of `s`.

**Exact counterexample.** Take `\mathcal H_h=\mathbb C^2`, `\Omega_h=(1,0)`, `K_h=\operatorname{diag}(0,\epsilon_h)` with `\epsilon_h\downarrow0`, and real bounded multiplier analogue `A_h=\delta_h\sigma_x` with `\delta_h\downarrow0`. Then `\operatorname{Var}_\Omega(A_h)=\delta_h^2\downarrow0` while the renormalized source `\widehat A_h=\sigma_x` has `P_s\widehat A_h\Omega_h=\widehat A_h\Omega_h` whenever `s\ge\epsilon_h`. The normalized source supplies an exact Parseval frame on the excited sector but the gap tends to zero. Thus small equal-time bare variance and excellent normalized observability are compatible with infrared accumulation. This abstract counterexample is not a Yang–Mills example; it demonstrates that the logical implication is invalid without a *dynamical* estimate.

## III. Theorem: exact non-extensive Euclidean-to-Hamiltonian operator inequality

Let `B` be bounded and `S=BB^*`. Define the connected physical-time covariance matrix/operator
\[
C(t)=B^*e^{-tK}B\quad(t\ge0).
\]
It is positive, and `\|C(t)\|=\|e^{-tK/2}Se^{-tK/2}\|` by the `XY`/`YX` nonzero-spectrum equality for `X=e^{-tK/2}B`, or directly by operator norms. For every `s,t>0` one has
\[
\boxed{\|P_sSP_s\|\le e^{st}\|C(t)\|.}\tag{1}
\]
**Proof.** `P_s` commutes with `e^{-tK/2}`, and `\|e^{tK/2}P_s\|\le e^{st/2}`. Thus
`P_sSP_s=(P_s e^{tK/2})(e^{-tK/2}Se^{-tK/2})(e^{tK/2}P_s)` and (1) follows.

If an independently proved, **uniform-in-graph-and-refinement** connected-covariance bound `\|C_h(t)\|\le M(1+t/t_*)^{-p}` holds for all `t\ge0`, then optimizing at `t=p/s` for `s\le p/t_*` gives
\[
\boxed{\|P_sS_hP_s\|\le M e^p(t_*s/p)^p.}\tag{2}
\]
This is precisely the required non-extensive operator-norm infrared contraction. Here `M,p,t_*` must be uniform, `B_h` must have bounded synthesis norm, and Euclidean covariance must be physically reconstructed as `C_h(t)`. This is a **conditional implication**, not a verified Wilson-theory decay theorem.

If also `P_\eta S_hP_\eta\ge c P_\eta` with `c>0` uniform, then (2) implies gap `\ge\min\{\eta, p/t_*, (c p^p/(M e^p t_*^p))^{1/p}\}` (strictly, any lower positive threshold less than these values is excluded). This premise is mass-gap-strength and must be proved independently from Wilson dynamics.

## IV. Theorem: Gram renormalization yields exact finite-subspace Parseval frames, but not uniform locality

Take `n` independent Wilson source vectors `b_i` with synthesis `B:\mathbb C^n\to Q\mathcal H`. Let `G=B^*B`, and define `\widehat B=BG^{-1/2}` on the positive spectral part of `G` (Moore–Penrose inverse on `\ker G^\perp`). Then
\[
\boxed{\widehat B\widehat B^*=P_{\overline{\mathrm{Ran}B}}.}\tag{3}
\]
So Gram whitening gives an exact non-extensive Parseval frame of the *spanned subspace* for any finite interacting Hamiltonian. It preserves the excited spectral subspace's observability if that subspace lies in the source span; otherwise the lower frame bound equals the minimum squared principal-angle cosine, which can vanish. Uniform control of `\|G^{-1/2}\|`, coefficients, loop support, block complexity, and graph/cutoff dependence is **not** implied. Whitening may produce highly nonlocal linear combinations and may require Hamiltonian vacuum correlation data.

## V. The physically correct transfer step and the order-of-limits gate

On any **fixed finite spatial graph**, take spatial plaquette weight `\beta_s(f,a_t)=a_t b_f+o(a_t)` and temporal-link convolution kernel proportional to `e^{\beta_t(e,a_t)p(U)}`, where `\beta_t(e,a_t)\to\infty` and `a_t\beta_t(e,a_t)\to2/a_e`. Character convolution has eigenvalue ratio
\[
\rho_j(\beta)=I_{2j+1}(\beta)/I_1(\beta)=1-2j(j+1)/\beta+O_j(\beta^{-2}).
\]
Consequently, after vacuum scalar normalization, a symmetric transfer product yields a fixed-graph Trotter/Chernoff limit with generator `H=\sum_e a_e(-\Delta_e)+\sum_f b_f(1-p_f)`, subject to the usual gauge projection and boundary choices. This is a *fixed spatial graph* statement; it is not uniform in `h` or the number of links, since the asymptotic error depends on representation and kinetic cutoff. (For general anisotropic geometry choose `a_e=2/(a_t\beta_t(e))` and `b_f=\beta_s(f)/a_t` at leading order.)

The previously studied Euclidean trajectory `a_t=\kappa h`, `\beta\asymp1/(g_3^2h)` takes temporal and spatial spacing to zero together. It does **not** separately establish the fixed-graph limit `a_t/h\to0`, and the finite-time-circle Euclidean measure does not automatically equal the vacuum infinite-time connected covariance. A 2+1D physical reconstruction requires reflection positivity / transfer Hilbert space, `T\to\infty` vacuum extraction, source normalization, and proof that these limits remain controlled with `h\downarrow0` and volume `\uparrow\infty`. None is available from the averaged equal-time cumulant bounds alone.

## VI. Actionable analytic gate: scale-aware renormalized source covariance

The new target can be stated in a form that neither smuggles in a gap nor loses observability by spectral filtering:

(A) Construct `\widehat B_{h,G}` from gauge-invariant graded multilocal Wilson sources using **spatial-only**, physics-defined renormalization, with `\sup_{h,G}\|\widehat B_{h,G}\|<\infty` and uniformly controlled support/complexity per scale (allow disconnected components to detect multiparticle states).

(B) Prove **from the full Euclidean Wilson dynamics**, after temporal reconstruction, the operator estimate `\|\widehat B_{h,G}^*e^{-tK_{h,G}}\widehat B_{h,G}\|\le M(1+t/t_*)^{-p}` uniformly in `h,G,t`. This is not the prior equal-time average bound.

(C) Prove lower observability `P_\eta\widehat B\widehat B^*P_\eta\ge cP_\eta` with `c>0` independent of cutoff/volume, including all center-neutral multilocal sectors in the selected window.

(D) Establish physical continuum reconstruction (vacuum/Schwinger functions, reflection positivity, nontrivial renormalized source limits, time calibration, and non-collapse of the gap in the limiting physical Hilbert space).

**If (A)–(D) were established**, (1)–(2) would prove uniform R3 and support R2. At present (B)–(D) are open. The earlier averaged plaquette-defect result is consistent with both a gapped and a gapless normalization scenario and cannot substitute for (B).
