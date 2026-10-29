# R3-IR — Exponentially weighted regional vacuum score and physical Wilson-source second spectral moment

**Date:** October 28, 2026.  **Branch:** `audit/2026-10-28-independent-reconstruction`.

**Status:** New finite-regulator, genuine interacting SU(2) ground-state theorems WS-1 through WS-5. In the stated fixed-physical-support Penrose geometry the constants are uniform over the regulator and ambient graph (provided the full interior collar and magnetic lower bound are preserved). These results improve the prior local-force `L^p, p<2` estimate to the endpoint **`L^2`**, give a uniform weighted vacuum-score energy bound, and quantitatively constrain the second physical excitation-energy moment. They do **not** prove bounded/nonzero continuum Wilson variance, a uniform physical gap, the quartic resolvent, the full Euclidean quantum field or source-level equality with the Stage7/Stage26 historical numerical action. No Monte Carlo.

## 1. Dependency audit and model

The exact current GitHub branch documents consulted before derivation are:

- `R3_IR_LOCAL_EXCITED_RELATIVE_ENERGY_2026-10-28.md` (ER-1) for the regional cut-Hamiltonian comparison;
- `R3_IR_REGIONAL_GROUND_STATE_AGMON_2026-10-28.md` (AG-1/AG-2) and `R3_IR_PROBABILITY_WEIGHTED_MAGNETIC_CONVEX_CORE_2026-10-28.md` (PC-1) for actual-vacuum exponential moments of rescaled total curvature;
- `R3_IR_LOCAL_VACUUM_SCORE_FORCE_2026-10-28.md` (VF-1–VF-8) for the source-force decomposition and nondegenerate first spectral moment;
- `R3_IR_PHYSICAL_SOURCE_RESPONSE_SPECTRAL_TRICHOTOMY_2026-10-28.md` (PS-1–PS-3) for the **physical Gauss-invariant** spectral measure;
- `R3_IR_QUARTIC_SPECTRAL_WARD_AUDIT_2026-10-28.md` (QR-1–QR-3), whose inverse-energy quartic challenge remains independent.

Work in the actual finite compact link-space `L²(SU(2)^E,dU)` of a face-complete rhombus disk, and in its vertex-Gauss invariant reducing subspace. Let

`H_h = sum_e a_e(-Delta_e) + sum_f b_f d_f`, `d_f=1-p_f`, `p_f=(1/2)ReTr W_f`.

Assume every face has four links, every link belongs to at most two faces, `0<a_e<=a_*`, and selected region `D` has `b_f>=beta_* h^-2`. Its incident link set is `S` and exterior magnetic collar is `C(D)`. Let `H_out` omit the electric terms on S and all magnetic terms on D union C(D), with `Delta_D=E0(H)-E0(H_out)>=0`.

Let `Omega_h` be the unique, strictly positive, normalized interacting ground state, `nu_h=Omega_h²dU`, `Gamma(f)=sum_e a_e |grad_e f|²`, and define

`X_h=sum_{f in D} d_f`, `Z_h=h X_h`, `T_S=sum_{e in S}a_e|grad_e log Omega_h|²`.

For fixed-physical-support Penrose refinement, assume (as independently established in ER-1 with its specific geometric assumptions)

`|D| <= C_F h^-2`, `Delta_D <= C_E h^-3`, and for each fixed t>0, `E_nu exp(t Z_h) <= M_t`, with `M_t` independent of h and ambient graph volume. The latter is supplied by AG-1/PC-1. All identities below are **finite-h exact**, with asymptotic estimates requiring precisely these listed inputs.

## WS-1. Exponentially weighted *interacting vacuum* local Fisher energy

**Theorem.** For every fixed t>=0,

**`E_nu[e^{t Z_h} T_S] <= 2 Delta_D E_nu[e^{t Z_h}] + 4a_* t² h E_nu[Z_h e^{t Z_h}]`.**  (WS-1)

For fixed Penrose support, in particular,

**`E_nu[e^{t Z_h} T_S] = O_t(h^-3)`** for every fixed t>0. (WS-2)

Consequently `E_nu[T_S Z_h^r]=O_r(h^-3)` for every fixed real r>=0, including r=1. This supplies the **weighted** kinetic information unavailable in VF-1 (which only bounded `E_nu T_S`).

**Proof (with explicit regional form decomposition).** The cut Hamiltonian is nonnegative above its vacuum: `H_out-E_out >= 0`. The exact decomposition

`H_h-E_out=(H_out-E_out)+sum_{e in S}a_e(-Delta_e)+sum_{g in D union C(D)}b_g d_g`

has nonnegative last two terms. For a real, smooth, gauge-invariant multiplier f of the S-link variables, the positive-form comparison gives

`sum_{e in S} a_e ||grad_e(f Omega_h)||² <= <f Omega_h,(H_h-E_out)f Omega_h>`.

The exact interacting ground-state transform ` <fOmega,(H-E0)fOmega>=E_nu Gamma(f)` turns the right hand side into

`Delta_D E_nu[f²] + E_nu[Gamma(f)]`.

The elementary *vector-valued* inequality `|f grad Omega|² <= 2|grad(f Omega)|²+2Omega²|grad f|²` then yields

**`E_nu[f² T_S] <= 2Delta_D E_nu[f²] + 4 E_nu[Gamma(f)]`.** (WS-3)

Put `f=exp(t Z_h/2)`. The SU(2) character identity `|grad_e p_f|²=(1-p_f²)/4<=d_f/2`, face degree 4 and edge incidence at most 2 give the exact pointwise bound

`Gamma(X_h)<=4a_* X_h`; hence `Gamma(Z_h)=h² Gamma(X_h) <=4a_* h Z_h`.

By the chain rule,

`Gamma(exp(t Z_h/2)) = (t²/4) exp(t Z_h)Gamma(Z_h) <= a_* t² h Z_h exp(t Z_h)`.

Inserting this into WS-3 proves WS-1. Since the local energy increment is bounded by `C_E h^-3`, and the AG-1 exponential moments bound `E[e^{t Z}]` and `E[Z e^{t Z}] <= E[e^{(t+1)Z}]`, WS-2 follows. For r>=0, the elementary inequality `z^r<=C_{r,t}e^{t z}` for z>=0 completes the weighted-polynomial corollary. The multiplier is bounded on every finite graph; no interchange of infinite-dimensional limits or unstated spectral gap occurs. QED.

## WS-2. Exact endpoint `L²` source-force control for signed tests

Let real `|q_f|<=q_*` and write

`Y_h=h sum_{f in D}q_f d_f`.

Define the true ground-state generator and its exact force decomposition (VF-2):

`L_h Y_h=D_h+F_h`,

`D_h=(3h/4) sum_f q_f sum_{e in boundary(f)} a_e p_f`,

`F_h=+2sum_{e in S}a_e grad_e(logOmega_h).grad_e Y_h`.

Then

`|hD_h|<=3a_*q_*h²|D|<=3a_*q_* C_F`,

`|hF_h|²<=4h² T_S Gamma(Y_h) <=16a_*q_*² h³ T_S Z_h`.

Setting t=1 in WS-1 and using `z<=e^z` yields

`h³ E[T_S Z_h] <= 2C_E M_1 +4a_*h⁴M_2`,

where `M_1` and `M_2` are the actual-vacuum exponential-moment constants for `exp(Z_h)` and `exp(2Z_h)`, respectively. Therefore

**`||h L_h Y_h||_{L²(nu_h)} <= 3a_*q_*C_F+4q_*sqrt[a_*(2C_E M_1+4a_*M_2)] =: C_force`**, (WS-4)

for h<=1 after fixing the physical units. This is valid for **arbitrary bounded signed q**, no positivity restriction.

Let `mu_h=(Y_h)_*nu_h` and `b_h(y)=E_nu[L_h Y_h | Y_h=y]`. The conditional-expectation contraction gives

**`||h b_h||_{L²(mu_h)} <= C_force`.** (WS-5)

This closes the endpoint missing from prior VF-5 (`1<=p<2`). It does **not** bound the derivative of b_h, its inward slope, or a Poincare constant. Nothing here implies `Var(Y_h)=o(h)` or a gap.

## WS-3. Second physical spectral moment and source variance lower envelope

Define the vacuum-centered *physical* Wilson source

`A_h=(Y_h-E_nuY_h)/sqrt(h)`.

It preserves Gauss invariance because each plaquette trace does. Its positive physical excitation spectral measure `mu_h^sp` is the projection measure of `A_h Omega_h` under `K_h=H_h-E0`. At each finite graph, `K_h(A_h Omega_h)=-(L_hY_h)Omega_h/sqrt(h)`. Thus the *exact* second spectral moment is

`m_{2,h}:=int_0^infty E² mu_h^sp(dE)=||K_h A_h Omega_h||²=(1/h)E_nu[(L_hY_h)²]`.

The global force endpoint yields

**`m_{2,h} <= C_force² h^-3`.** (WS-6)

For every energy cutoff Λ>0,

**`mu_h^sp((Λ,infty))<=min{m_{1,h}/Λ, C_force²/(h³Λ²)}`** and

**`int_(Λ,infty) E mu_h^sp(dE)<= C_force²/(h³ Λ)`.** (WS-7)

These are genuine physical Gauss-invariant spectral bounds. They do not claim the inverse-energy susceptibility is uniformly finite.

For the *additional* nonnegative, macroscopic test hypotheses of VF-8, `a_e>=a_min>0` on S and `q_f>=0`, with `h²sum q_f>=q_mass>0`, prior independently proved stationarity gives `m_{1,h}:=int E mu_h^sp(dE)>=m_*>0`. Cauchy-Schwarz in the positive spectral measure gives `m_{1,h}² <= v_h m_{2,h}`, where `v_h=Var_nu(Y_h)/h`. Consequently

**`v_h >= (m_*²/C_force²)h³`**, i.e.

**`Var_nu(Y_h) >= (m_*²/C_force²)h⁴`.** (WS-8)

This is a **nonzero finite-regulator lower envelope** for the exact interacting vacuum, not a nonzero continuum limiting variance. It is far weaker than `liminf v_h>0`, which remains OPEN.

Moreover, taking `Λ_h=(2C_force²/m_*)h^-3`, the second energy-moment tail gives

**`int_(0,Λ_h] E mu_h^sp(dE) >= m_*/2`, and `mu_h^sp((0,Λ_h]) >= m_*² h³/(4C_force²)`.** (WS-9)

Hence an order-one first energy moment cannot escape entirely above energies growing faster than h^-3. This does **not** constrain that spectral weight to any fixed physical energy scale, and it does not establish a uniform gap.

## WS-4. Exact one-plaquette physical consistency check

On one open rhombus with four equal electric coefficients a, zero magnetic coupling and gauge-invariant Haar vacuum Ω=1, the physical class function p=(1/2)Tr W has mean 0 and variance 1/4. For q=1, `Y=h(1-p)` and `A=−sqrt(h) p`. The first nonzero physical energy is 3a, so

`v_A=h/4`, `m_1=3ah/4`, `m_2=9a²h/4`, and `m_1²=v_A m_2`.

This exactly checks the relationships between source normalization, the second spectral moment, first spectral moment and variance. It is **not** a fixed-physical-area Penrose refinement and does not satisfy the macroscopic nonzero-first-moment assumption `m_*>0`. The purpose is to rule out missing h factors, not to simulate an interacting vacuum.

## Crucial interpretation and next obligation

The earlier proof program at times treated `Var(Y_h)=o(h)` as a mandatory mass-gap step. PS-1–PS-3 already corrected that: an interacting *gapped* theory may have a nonzero finite variance for its selected gauge-invariant field. The new WS-8 lower envelope does not resolve the variance trichotomy, and WS-6 cannot prevent spectral mass from moving to energies of order h^-3.

The natural next route is a **stronger source-specific dynamical cancellation** of the *actual* geometric force D_h with the score force F_h at the level of the `L²` norm, not merely their means. If one could independently prove the uniform endpoint `||L_hY_h||²=O(h)` (equivalently `m_{2,h}=O(1)`), then the pre-existing `m_{1,h}>=m_*>0` would establish a **nonvanishing source variance** `v_h>=m_*²/O(1)`. Neither WS-4 nor the existing Agmon, curvature, or energy estimates prove this cancellation. Conversely, a nontrivial Euclidean field also requires an *upper* variance bound, and an independent uniform physical gap remains a separate global spectral problem.

Source identity with the historic Stage7/Stage26 numerical action, physical quartic resolvent, operator distribution tightness, and continuum reconstruction all remain OPEN. No original data, historical simulation archives, or geometry were modified.

## Verification notes

`verify_weighted_score_second_moment.py` uses exact SymPy identities to check the fundamental SU(2) Casimir relation, exponential multiplier chain rule, weighted-kinetic IMS inequality, scaling of the second spectral moment and spectral Chebyshev bound, and the canonical three-face, ten-edge **spatial** Penrose seed. It does **not** prove the infinite sequence from finite numerical tests or certify the original temporal Q14. Exact theorems rest on the mathematical form comparison and ground-state calculus above. No Monte Carlo.

**Algebraic sign erratum (2026-10-28):** The abbreviated vacuum-score force is `F_h=+2Σ_e a_e ∇_e logΩ·∇_eY_h`, equivalently `−2hΣ_f q_fΣ_{e∈∂f}a_e∇_e logΩ·∇_e p_f`. The former minus-sign abbreviation was a transcription error; its absolute-value estimates are unchanged. See the exact joint-force Ward identity in `R3_IR_JOINT_FORCE_COVARIANCE_WARD_2026-10-28.md`.
