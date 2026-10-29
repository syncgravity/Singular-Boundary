# R3-IR — Exact regional vacuum-score and nondegenerate Wilson first-moment theorem

**October 28, 2026.** Mathematical status: exact finite-volume theorem for the *actual ground state* of the declared nonlinear SU(2) Wilson Hamiltonian, conditional on the already audited regional energy and Agmon hypotheses for refinement constants. This is **not** a proof of fixed-support variance collapse, a uniform mass gap, continuum existence, or exact correspondence to the original Stage 7/26 lattice algorithm. There are no Monte Carlo results.

## 1. Hypotheses and provenance

The current audit branch reports checked before derivation are `R3_IR_MODERATE_CURVATURE_EFFECTIVE_DRIFT_2026-10-28.md` (DR-1/DR-4), `R3_IR_REGIONAL_GROUND_STATE_AGMON_2026-10-28.md` (AG-1), `R3_IR_LOCAL_EXCITED_RELATIVE_ENERGY_2026-10-28.md` (ER-1), and `R3_IR_CURVATURE_WEIGHTED_FSUM_2026-10-28.md` (FS-1). The Stage7/Stage26 numerical action has not been equated to these declared coefficients at source level. The canonical Z^5 three-rhombus seed, where checked, is spatial and not temporal Q14.

On a finite face-complete SU(2) rhombus graph, let

\[ H=\sum_e a_e(-\Delta_e)+\sum_f b_f(1-p_f),\quad p_f=\tfrac12\operatorname{ReTr}(W_f),\quad -\Delta\chi_{1/2}=\tfrac34\chi_{1/2}.\]

The finite-volume positive normalized ground state is Ω, E0 its energy and ν=Ω²dHaar. Choose a face region D, its incident edges S and exterior edge-adjacent face collar C(D). Let `H_out` omit S electric and all magnetic terms touching S, `E_out=inf σ(H_out)`, and `Δ_D=E0-E_out`. All these operators and expectations are in the actual finite Hilbert space, including its gauge-invariant reducing subspace. Assume

- `0<a_e≤a_max` on all links, and `b_f≥β_min h^-2` on D.
- for refinement conclusions, `F_D=|D|≤C_F h^-2` and `0≤Δ_D≤C_E h^-3`, with constants independent of h and ambient volume and a full geometric collar;
- real test weights `|q_f|≤q_*` and
  `Y_h=h∑_{f∈D}q_fd_f`, `Z_h=h∑_{f∈D}d_f`, `d_f=1-p_f∈[0,2]`.
- The previous regional Agmon theorem AG-1 is used only for the **uniform higher moments** `sup_h Eν Z_h^r<∞` for each fixed r≥1. This is a derived consequence of the exponential tail at Z>2C_L and bounded Z below it.

Write `Γ(g)=Σ_e a_e|∇_eg|²`. For the finite positive vacuum define the ground-state generator `ℒg=Σ_e a_e[Δ_e g+2∇_e logΩ·∇_eg]`, which is self-adjoint in ν with `Eν ℒg=0`.

## VF-1 — Localized kinetic energy of the exact vacuum score

Define the nonnegative field `T_S(U)=Σ_{e∈S} a_e|∇_e logΩ(U)|²`. Since `H=H_out+Σ_{e∈S}a_e(-Δ_e)+Σ_{g∈D∪C(D)}b_gd_g`, the vacuum eigenvalue identity and nonnegativity yield

\[ \boxed{\ E_\nu T_S\le E_0-E_{\rm out}=\Delta_D\le C_E h^{-3}.\ } \tag{VF-1}\]

This is a **localized score-Fisher bound** of the true nonlinear vacuum, not a global entropy/log-Sobolev estimate. The exact, sharper form `EνT_S+Σ_{D∪C}b_g Eνd_g ≤Δ_D` also holds.

## VF-2 — Exact force decomposition and global L^p control

The exact SU(2) fundamental Casimir gives `Δ_e p_f=−(3/4)p_f` on each boundary link e of f and `|∇_e p_f|²=(1-p_f²)/4≤d_f/2`. Therefore

\[ \boxed{\ \mathcal L Y_h=D_h+F_h,\quad D_h=\frac{3h}{4}\sum_{f∈D}q_f\sum_{e∈∂f}a_ep_f,\quad F_h=+2\sum_{e∈S}a_e\nabla_e\log\Omega\cdot\nabla_eY_h.\ } \tag{VF-2}\]

The geometrical force `||D_h||_∞≤3a_max q_*hF_D`, and the exact local SU(2) f-sum satisfies the pointwise bound

\[\Gamma(Y_h)\le 4a_{\max}q_*^2 h Z_h.\tag{VF-3}\]

Hence `|F_h|²≤4 T_S Γ(Y_h)`. For 1≤p<2 set r=p/(2-p)≥1. Hölder with exponents 2/p and 2/(2−p), then VF-1 and VF-3, yields the **uniform force bound**

\[ \boxed{\ \|h F_h\|_{L^p(\nu)}\le 4q_*\sqrt{a_{\max}h^3\Delta_D}\,\|Z_h\|_{L^r(\nu)}^{1/2}.\ } \tag{VF-4}\]

For fixed physical Penrose support the right-hand side is O(1), because `h³Δ_D≤C_E` and the regional Agmon theorem bounds all fixed Z moments. Also `||hD_h||_∞≤3a_max q_*h²F_D≤3a_max q_* C_F`.

Let `μ_h=(Y_h)_*ν` and let `b_h(y)=Eν[ℒY_h|Y_h=y]`, the exact conditional effective drift from DR-1. Jensen's inequality under conditional expectation gives

\[ \boxed{\ \|h b_h\|_{L^p(\mu_h)}\le 3a_{\max}q_*h^2F_D+4q_*\sqrt{a_{\max}h^3\Delta_D}\,\|Z_h\|_{L^{p/(2-p)}(\nu)}^{1/2}\le C_p,\quad 1\le p<2.\ } \tag{VF-5}\]

This is an **unconditional** estimate of the missing actual vacuum conditional force for signed test sources. It controls magnitude and provides `μ_h(|h b_h|>R)≤C_p^p/R^p`, not the necessary inward restoring slope or derivative. It does **not** prove `Var_ν(Y_h)=o(h)`.

## VF-3 — Moderate-band L² control of the unprojected force

For each fixed T>0, on `{Z_h≤T}`, VF-3 yields `Γ(Y_h)≤4a_max q_*²hT`. Consequently

\[ \boxed{\ E_\nu[|h\mathcal L Y_h|^2\mathbf1_{\{Z_h\le T\}}]\le 2(3a_{\max}q_*h^2F_D)^2+32a_{\max}q_*^2 h^3 T\Delta_D\le C_T.\ } \tag{VF-6}\]

This estimate is again genuine interacting-vacuum information. For signed sources one **cannot** replace `E[ℒY|Y,Z≤T]` by `b_h(Y)` on that event without additional conditional control: conditioning only on Y may mix configurations with large total Z. For nonnegative weights uniformly `q_f≥q_0>0` on all f∈D, `Y_h≥q_0 Z_h`, allowing L² control of b_h(Y) on `[0,T]` from VF-6 with threshold `Z≤T/q_0`. For general signed tests, the L^p estimate VF-5 is the appropriate unconditional marginal statement.

## VF-4 — Matching sharp scales for nonnegative macroscopic sources

Add **new explicit assumptions:** `a_e≥a_min>0` for all edges in S; `q_f≥0`; and `h²Σ_{f∈D}q_f≥q_mass>0` uniformly. These hold for a fixed nonzero nonnegative smooth Penrose test with the declared bounded positive electric coefficients, under a legitimate face-area Riemann sum.

The regional magnetic lower bound and the vacuum energy decomposition give

\[ E_\nu\sum_{f∈D}d_f\le h²\Delta_D/\beta_{\min}\le C_E/(\beta_{\min}h).\]

Since `p_f=1−d_f`, the geometric force expectation satisfies

\[ E_\nu D_h\ge 3h\left(a_{\min}\sum_Dq_f-a_{\max}q_*E_\nu\sum_Dd_f\right)\ge \frac{3a_{\min}q_{\rm mass}}{2h}=:c_D/h\]

for small h. Ground-state stationarity `E_ν ℒY=0` forces `E_νF_h=−E_νD_h`. Therefore the score contribution **cannot be discarded**; indeed `||h F_h||_{L¹(ν)}≥c_D`.

Writing `M1(Y_h)=EνΓ(Y_h)`, Cauchy–Schwarz in VF-2 gives

\[ (E_\nu D_h)^2=(E_\nu F_h)^2\le4(E_\nu T_S)M1(Y_h).\tag{VF-7}\]

The exact bounds `E T_S≤C_E h^-3` and `M1(Y_h)≤C_M h`, with `C_M=4a_max q_*² C_E/β_min`, now imply two-sided, **sharp-order** inequalities:

\[\boxed{\frac{c_D^2}{4C_M}h^{-3}\le E_\nu T_S\le C_Eh^{-3},\qquad \frac{c_D^2}{4C_E}h\le M1(Y_h)\le C_Mh.}\tag{VF-8}\]

Thus `EνT_S=Θ(h^-3)` and `M1(Y_h)=Θ(h)` for the stated macroscopic nonnegative source. For the vacuum-centered normalized field `A_h=(Y_h-EνY_h)/√h`, its **first spectral moment is bounded both above and away from zero:** `M1(A_h)=Θ(1)`. No corresponding variance bound or uniform spectral gap follows. This matches, and upgrades to nondegenerate order, the earlier upper first-moment FS-1.

## Why the target remains open

The desired `Var_ν(Y_h)=o(h)` requires quantitative cancellation in the *conditional force* or connected covariance of the moderate-curvature region. Bounds on `||h b_h||_{L^p}` for p<2 do not control a one-sided slope of `b_h(y)`, its conditional derivative, or a one-dimensional Poincaré constant. Likewise VF-8 proves nontrivial kinetic and first-moment scales but gives no upper bound on the spectral-source variance. There is no logically valid inference from either theorem to a positive mass gap or the R2 quantum continuum.

The next independently necessary theorem would estimate **the derivative of the conditional vacuum score or a coercive conditional covariance of `Y_h` with `b_h(Y_h)`** at the original physical coupling. In terms of the true logarithmic vacuum, the open term is

\[ E_\nu\left[-2\sum_{e∈S}a_e\nabla_e\log\Omega_h\cdot\nabla_eY_h\mid Y_h=y\right].\]

A pointwise or monotone estimate derived from the nonlinear eigenvalue equation, not imported from an assumed gap or Gaussian measure, is still required. The prior Agmon theorem removes far curvature excursions but not the moderate connected covariance. The Stage7/26 action correspondence remains an independent source-provenance gate.

## Reproducibility and integrity

`verify_local_score.py` checks exact SU2 Casimir geometry, Hölder exponents p/(2-p), exact h scalings for VF-5/VF-8, pure-electric one-rhombus drift and the canonical three-face spatial fixture. It verifies algebraic identities, *not* continuum behavior or the original temporal Q14 protocol. No Monte Carlo samples were taken; historical archives are unchanged.

**Algebraic sign erratum (2026-10-28):** The abbreviated vacuum-score force is `F_h=+2Σ_e a_e ∇_e logΩ·∇_eY_h`, equivalently `−2hΣ_f q_fΣ_{e∈∂f}a_e∇_e logΩ·∇_e p_f`. The former minus-sign abbreviation was a transcription error; its absolute-value estimates are unchanged. See the exact joint-force Ward identity in `R3_IR_JOINT_FORCE_COVARIANCE_WARD_2026-10-28.md`.
