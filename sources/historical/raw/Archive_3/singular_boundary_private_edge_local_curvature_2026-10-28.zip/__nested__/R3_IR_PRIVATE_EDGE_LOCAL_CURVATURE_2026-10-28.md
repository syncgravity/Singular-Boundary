# The Singular Boundary — exact localized SU(2) ground-state curvature bound

**Date:** 2026-10-28  
**Scope:** finite-volume, nonperturbative ground-state estimates for faces with an edge of magnetic incidence one; a neighboring-coupling extension; a rigorously controlled pure-connector torque moment for selected boundary faces.  
**Integrity:** original historical files unchanged, no Monte Carlo, no replacement numerical results. The finite 3-rhombus canonical seed fixture verifies incidence only. Uniform interior curvature, collective physical gap and quantum continuum remain **OPEN**.

## 1. Setup

Let `G=(V,E,F)` be any finite SU(2) Wilson face complex with simple four-link faces and edge-face magnetic incidence at most two. Work first in `L²(SU(2)^E,dU)`; its unique strictly positive ground state is gauge invariant. Normalize `-Δ` so that `(-Δ)p=3p/4` for `p(U)=ReTr(U)/2` and `|∇p|²=(1-p²)/4`.

\[
 H=\sum_{e\in E}a_e(-\Delta_e)+\sum_{f\in F}b_fd_f,
 \qquad d_f=1-p(W_f),\quad a_e>0,\ b_f\ge0.
\]

Write `ν=Ω²dU` for its exact interacting ground-state measure; the statements about invariant observables are statements in the physical gauge sector.

A **private edge** `e0` of face `f` means `e0` occurs in the word of `f` exactly once and belongs to no other magnetic face. An ordinary boundary edge of a face-complete rhombus disk has this property. No large-patch or translation invariance is assumed.

Define `A_f=Σ_{e∈∂f}a_e` (an electric coefficient sum, **not** the physical rhombus area).

## 2. Lemma LC-1 — exact decoupling and normalized conditional trial

For fixed `f` possessing a private edge `e0`, delete its magnetic potential and write `H(0)=H_rest+a_{e0}(-Δ_{e0})`, where `H_rest` is independent of `U_{e0}`. Let `Ω_rest(U_{-e0})` be the unique normalized ground wavefunction of `H_rest`. The full-link ground state of `H(0)` is `Ω_rest⊗1`. Put

\[
 q_\kappa(V)=Z_\kappa^{-1/2}\exp[\kappa p(V)],\quad
 Z_\kappa=\int_{SU(2)}e^{2\kappa p(V)}dV,\qquad \kappa>0,
\]

and define the **gauge-invariant** trial state

\[
 \Psi_\kappa(U)=\Omega_{rest}(U_{-e0})\,q_\kappa(W_f(U)).
\]

For every fixed `U_{-e0}`, the map `U_{e0}→W_f(U)` is a Haar-measure-preserving left/right translation, possibly composed with inversion. Hence

\[
\int dU_{e0}\,q_\kappa(W_f(U))^2=1.
\]

It follows that `Ψκ` is normalized and the expectation of **every term independent of `U_{e0}`** is unchanged, except for electric derivatives acting on the added factor. In particular, for every remaining face `g≠f`, its magnetic expectation equals that in `Ω_rest`.

For an edge `e∈∂f\{e0}`, the derivative of `Ψκ` has a cross term proportional to

\[
 \int dU_{e0}\, q_\kappa(W_f)\nabla_e q_\kappa(W_f)
 =\tfrac12\nabla_e\int dU_{e0}\,q_\kappa(W_f)^2=0.
\]

The metric is bi-invariant, so the squared-gradient contribution of the trial factor is the same `kκ=∫|∇qκ(V)|²dV` on each of the four edges in `∂f`; it vanishes on all other edges. Thus **exactly**

\[
\langle\Psi_\kappa,H(b_f=t)\Psi_\kappa\rangle
 =E_0(0)+ A_f k_\kappa+t(1-r_\kappa),\quad
 r_\kappa=\int p(V)q_\kappa(V)^2dV.
\tag{LC-1}
\]

Because `qκ` is a class function and `Ω_rest` is gauge invariant, this is also an admissible physical-sector trial state.

## 3. Theorem LC-2 — volume-independent local face curvature

For every such private-edge face and `b_f>0`, keeping **all other electric and magnetic coefficients arbitrary**,

\[
\boxed{\quad
 \mathbb E_{\nu_G}d_f\le
 \min\left\{2,\,\frac{3}{2\sqrt2}\sqrt{\frac{A_f}{b_f}}\right\}.\quad}
\tag{LC-2}
\]

**Proof of the one-link estimates.** Under `qκ²dV` the variable `y=1-p(V)∈[0,2]` has density proportional to `y^{1/2}(2-y)^{1/2}e^{-2κy}`. Integrating the derivative of `y^{3/2}(2-y)^{1/2}e^{-2κy}` over `[0,2]` gives

\[
2\kappa\mathbb E y
 =\frac32-\frac12\mathbb E\frac{y}{2-y}
 \le\frac32.
\]

Hence `1-rκ≤3/(4κ)`. Integration by parts with `(-Δ)p=3p/4` gives the **exact** kinetic identity `kκ=3κrκ/8≤3κ/8`. From LC-1 and the Rayleigh principle,

\[
0\le E_0(t)-E_0(0)
 \le \frac{3\kappa}{8}A_f+\frac{3t}{4\kappa}.
\]

Minimizing at `κ=√(2t/A_f)` yields

\[
E_0(t)-E_0(0)\le\frac{3}{2\sqrt2}\sqrt{A_ft}.
\]

As `E_0(t)` is the infimum of affine functions of `t`, it is concave; its simple ground eigenvalue is differentiable at every finite `t>0` by bounded perturbation theory. Therefore Feynman–Hellmann and concavity imply

\[
t\,\mathbb E_{\nu(t)}d_f=t E_0'(t)
 \le E_0(t)-E_0(0)\le\frac{3}{2\sqrt2}\sqrt{A_ft}.
\]

Divide by `t=b_f`. The independent bound `0≤d_f≤2` gives the stated minimum. QED.

This is **an exact local physical-ground-state theorem**. Its constants depend on the four electric edge coefficients of f and b_f, and on nothing else about distant faces, distant coupling strengths, total volume, or boundary shape.

**Uniform-coupling specialization:** if `a_e=a` on all four edges and `b_f=b>0`,

\[
\mathbb E_{\nu}d_f\le\min\{2,\frac3{\sqrt2}\sqrt{a/b}\}.
\]

**Specified geometric Penrose scaling:** with rhombus *physical* area `h² σ_f`, `w_e∈[σ_-/2,σ_+]`, `a_e=g_3²/(2w_e)≤g_3²/σ_-` and `b_f=4/(g_3² h² σ_f)`, one obtains for **every boundary face having a private edge**

\[
\boxed{\mathbb E_{\nu_{h,G}}d_f\le
 \min\left\{2,\frac{3\sqrt\varphi}{2\sqrt2}\,g_3²h\right\},
 \qquad \varphi=\frac{\sigma_+}{\sigma_-}=\frac{1+\sqrt5}{2}.}
\tag{LC-P}
\]

The identity of these declared geometric coefficients with literal Stage 7/26 production source remains a separate historical source audit; no claim is made for unverified alternate actions. This **does not** imply uniform bulk-face curvature or physical spectral decay.

## 4. Theorem LC-3 — general one-edge comparison with an explicit neighbor penalty

For **any** face f and any edge `e0∈∂f` in a complex with incidence ≤2, let `g(e0)` be the other magnetic face incident to that edge, if one exists, and set `b_{g(e0)}=0` if none exists. Then

\[
\boxed{\mathbb E_{\nu_G}d_f\le
\min\left\{2,\,\frac{3}{2\sqrt2}\sqrt{\frac{A_f}{b_f}}
+\frac{2b_{g(e0)}}{b_f}\right\}.}
\tag{LC-3}
\]

**Proof.** Delete both the f and g(e0) magnetic potentials; the chosen edge then decouples exactly. Use the same conditionally normalized trial `Ω_rest qκ(W_f)`; the reintroduced g term has expectation at most `2b_g` since `0≤d_g≤2`. This proves `E_0(b_f,b_g)-E_0(0,0)≤ (3/(2√2))√(A_f b_f)+2b_g`. Since restoring the nonnegative g potential can only increase the ground energy, `E_0(0,b_g)≥E_0(0,0)`. Apply concavity and Feynman–Hellmann in b_f to obtain LC-3. QED.

For interior Penrose faces with `b_g` comparable to `b_f` on **every** edge, the neighbor penalty is order one. The comparison therefore becomes essentially trivial in the strong-magnetic limit. **This is the exact point at which the decoupled-private-edge strategy fails to establish bulk local flatness.** It is not a counterexample to bulk flatness itself.

## 5. Corollary LC-4 — bounded single-connector torque for two boundary sources

For two selected based face holonomies f,g with normalized source weights `v_f²=v_g²=1/2`, assume both possess private magnetic edges. At a **pure** tree connector edge separating the two faces, the exact previous theorem gives

\[
|\nabla_e\mathcal Q_v|²
 =64|v_f\mathbf u_f\times v_g\mathbf u_g|²
 \le64d_fd_g.
\]

Because `0≤d_f,d_g≤2`, `E(d_f d_g)≤2 min(E d_f,E d_g)`. Thus

\[
\boxed{\mathbb E_{\nu_G}|\nabla_e\mathcal Q_v|²
 \le128\min\{\mathbb E d_f,\mathbb E d_g\}
 \le\frac{192}{\sqrt2}\min\left\{\sqrt{\frac{A_f}{b_f}},\sqrt{\frac{A_g}{b_g}}\right\}.}
\tag{LC-4}
\]

This is **one-connector** and **two-boundary-face** control, independent of ambient volume; it does not control a sum over a path of potentially many connector edges. No mixing of d_f and d_g was assumed. In particular, the full source Rayleigh quotient still requires a source variance lower estimate and all connector contributions.

## 6. Authentic finite-source fixture and proof status

Three recovered canonical Q14 seed rhombi have exactly 10 distinct edges, eight incidence-one boundary edges, and respective private-edge counts `(2,3,3)`. These finite counts are independently checked from the stored integer vertex labels, **not** evidence about the entire historical temporal Q14 cavity. The symbolic certificate checks the exact trial optimization, the SU(2) conditional Haar integration-by-parts identity, and the geometric Penrose scaling envelope. No numerical spectral fitting, Monte Carlo or replacement history.

Evidence classification:
- LC-1 conditional normalized private-edge trial: **independently proved**.
- LC-2 local boundary curvature with volume-independent constants: **independently proved**.
- LC-3 one-edge neighbor-penalty comparison: **independently proved**, usually noninformative for interior equal magnetic couplings.
- LC-4 single pure-connector two-boundary source torque: **independently proved**, no full-path/source variance conclusion.
- Uniform bulk-face local curvature, connected long-path torque and regulator-independent interacting gap: **OPEN**.

**Next noncircular dependency:** establish a local comparison for an **interior** face that does not incur an order-one magnetic neighbor penalty, or prove a ground-state weighted joint curvature/path inequality with constants independent of distance and graph size. Possible approaches include a genuinely gauge-covariant local block replacement, a proven local quantum conditional estimate, or a source that avoids long rooted connectors. No such estimate is claimed here.
