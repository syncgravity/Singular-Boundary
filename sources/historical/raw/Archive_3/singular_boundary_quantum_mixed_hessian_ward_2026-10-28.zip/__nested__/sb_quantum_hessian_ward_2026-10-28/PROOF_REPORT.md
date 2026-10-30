# R3-IR — Full mixed-link vacuum Hessian Ward identity and Gauss-sector obstruction

**Date:** 2026-10-28. **Branch:** `audit/2026-10-28-independent-reconstruction`.  
**Proved:** exact finite interacting SU(2) Wilson vacuum susceptibility/Hessian identity and its nonphysical Gauss-sector location. **Not proved:** a regulator-uniform lower Hessian eigenvalue, nonlinear vacuum Poincaré inequality, fixed-support connected covariance, quartic resolvent, physical mass gap, or nontrivial continuum. **No simulations.**

## Dependencies and provenance

Live GitHub audit-branch reports inspected: `R3_IR_GAUGE_REDUCED_FLAT_HESSIAN_CHEEGER_2026-10-28.md` (flat classical Hessian theorem); `R3_IR_PROBABILITY_WEIGHTED_MAGNETIC_CONVEX_CORE_2026-10-28.md` (good-face probability and Hessian diagonal blocks); `R3_IR_LOCAL_VACUUM_SCORE_FORCE_2026-10-28.md` (vacuum localized Fisher budget); and the current proof ledger. The original Stage7/26 Monte Carlo action has not been proved to coincide with the separately declared Hamiltonian. The independent spatial fixture remains the three-rhombus, ten-edge Penrose Z5 seed, not temporal Q14.

## Hamiltonian and vector fields

Consider a finite connected rhombus cell complex with four distinct oriented edges per face. The **full kinematical** Hilbert space is `Hkin=L²(SU(2)^E,dHaar)`, with

\[
H=H_E+V,\quad H_E=\sum_e a_e(-\Delta_e),\quad
V=\sum_f b_f[1-\tfrac12\mathrm{ReTr}(W_f)],\quad a_e>0,\ b_f\ge0.
\]

Assume the Laplacian Casimir convention `-Δ_e χ_(1/2)=3χ_(1/2)/4`. The ground state `Ω>0` is unique, smooth, real and invariant under the full local vertex-gauge group. Write `E0=inf σ(H)`, `K=H−E0`, `Q=I−|Ω><Ω|`, `G=Q(K|Ran Q)^(-1)Q` (well-defined at each **fixed finite** lattice, with no regulator-uniform bound). The gauge-invariant physical subspace is the range of the local Gauss projector `P_G`.

For each link e and real Lie-algebra vector `x_e∈su(2)`, define `D_e^{x_e}` as the real left-invariant directional derivative under `U_e→exp(t x_e)U_e`, with all other links fixed. For a fixed link-vector `x=(x_e)` put `D_x=Σ_e D_e^{x_e}`. These derivatives are divergence-free, skew-adjoint on Haar `D_x*=-D_x`, and commute with `H_E`. Their flow is a product of geodesics for the product bi-invariant metric, so `D_x²V=Hess V(x,x)` in left-trivialized constant directions. (The directions need not be gauge-covariant under configuration-dependent gauge transformations.)

## Theorem QH-1 — Exact positive full mixed magnetic Hessian *in the interacting vacuum*

For every fixed real link-vector x,

\[
\boxed{\ E_\nu[D_x^2V]
=2\langle D_x\Omega,K D_x\Omega\rangle
=2\langle (D_xV)\Omega,G(D_xV)\Omega\rangle\ge0.\ }
\tag{QH-1}
\]

Here `ν=Ω²dHaar`. The same statement holds for any finite positive magnetic couplings and any graph; no good-core, flatness, gap, or continuum limit is assumed.

**Proof:** `[H_E,D_x]=0` and `[V,D_x]=−(D_xV)` give the exact differentiated eigenfunction equation
`K(D_xΩ)=−(D_xV)Ω`. The anti-self-adjoint vector field satisfies `〈Ω,D_xΩ〉=0`, and the right side is likewise orthogonal to Ω (`Eν[D_xV]=0` by the expectation of `[H,D_x]`). Thus `D_xΩ=−G[(D_xV)Ω]`. Consequently
`〈D_xΩ,KD_xΩ〉=−∫(D_xΩ)(D_xV)ΩdHaar=(1/2)∫Ω² D_x²V dHaar`, by integration by parts of `D_x(Ω²)`. This proves all equalities. Since K≥0, the average full Hessian is positive semidefinite. QED.

Polarization gives a **matrix-valued mixed-link identity**

\[
\boxed{\ E_\nu[\mathrm{Hess}V(x,y)]
=2\mathrm{Re}\langle D_x\Omega,KD_y\Omega\rangle.\ }
\tag{QH-2}
\]

This does not follow from positive diagonal blocks alone: it is a ground-state Ward identity involving *every mixed link direction*. It is also the exact cancellation of the second derivative of the ground energy under the unitary link translation `H(t)=exp(−tD_x)Hexp(tD_x)`, whose spectrum is constant. The positivity is an **integrated statement**, not pointwise convexity of V or of `−logΩ`.

The kernel is exactly

\[
\boxed{\ \ker E_\nu[\mathrm{Hess}V]
=\{x:D_xV\equiv0\}=\{x:D_x\Omega\equiv0\}.\ }
\tag{QH-3}
\]

Indeed a vanishing quadratic form in QH-1 gives `D_xΩ=0` (uniqueness of vacuum and orthogonality); the differentiated eigenfunction equation implies `D_xV=0` pointwise because Ω>0. The converse follows by the same equation. This is an *algebraic symmetry kernel*, not necessarily the fixed-flat connection's infinitesimal gauge kernel.

## Theorem QH-2 — Exactly averaged logarithmic-vacuum Hessian

For every fixed left-invariant link direction x,

\[
\boxed{\ -E_\nu[D_x^2\log\Omega]
=2E_\nu[(D_x\log\Omega)^2]\ge0.\ }
\tag{QH-4}
\]

This is an exact Fisher-information integration-by-parts identity: apply Haar divergence-freeness to `D_x(Ω² D_x logΩ)`. Polarization gives the full mixed-link tensor. It holds for *every* smooth positive density, whether or not Ω solves the Hamiltonian eigenvalue equation; consequently positive **integrated** score Hessian is not a Bakry–Émery lower bound, not a connected covariance theorem and not a quantitative source Poincaré inequality. With the prior regional bound `Eν Σ_{e∈S}a_e|∇_e logΩ|²≤Δ_D`, it yields for x supported in S

\[
\boxed{\ E_\nu[(D_x\log\Omega)^2]
\le \big(\sum_{e\in S}|x_e|^2/a_e\big)\Delta_D.\ }
\tag{QH-5}
\]

In the declared fixed-area Penrose geometry the right side is O(h^(-3)) for a uniformly normalized x with electric coefficients bounded below. No *lower* Fisher eigenvalue follows.

## Theorem QH-3 — Exact physical Gauss-sector obstruction

**Assume full Gauss invariance at every vertex**, including boundary vertices (other boundary conditions must be treated separately). For any edge e with tail vertex v, the local gauge action sends a constant left-invariant generator `D_e^x` to `D_e^(Ad_g x)` when g acts at v. Since Ω is gauge invariant, averaging over Haar SU(2) at v kills the adjoint vector: `∫_SU2 Ad_g x dg=0`. Therefore

\[
\boxed{\ P_G D_e^x\Omega=0,\quad P_G D_x\Omega=0.\ }
\tag{QH-6}
\]

As K and P_G commute, `P_G(D_xV)Ω=−P_GK D_xΩ=0`. In particular the resolvent susceptibility and every nonzero excitation in QH-1 occur entirely in the **orthogonal complement of the physical Gauss-invariant Hilbert space**. This is a decisive limitation: a positive full-link averaged Hessian from QH-1 **cannot be promoted to a bound on the physical mass gap**. It is *not* the physical gauge-reduced Hessian of a gauge-invariant source, and it does not control `Var_Ω(Y_h)` for a macroscopic Wilson curvature observable.

## Exact SU(2) one-plaquette weak-field consistency check

For one open SU(2) plaquette with four identical electric coefficients a and magnetic coefficient b, the gauge-invariant character basis `χ_n` obeys `H_E χ_n=a n(n+2)χ_n` for n=0,1,..., and `pχ_n=(χ_(n−1)+χ_(n+1))/2`. For small b/a, the normalized vacuum is
`Ω=χ_0+(b/(6a))χ_1+O(b²)` and `Eν p=b/(6a)+O(b²)`.
For a unit left-invariant direction on one link,
`D_x²[b(1−p)]=(b/4)p`, so
`Eν D_x²V=b²/(24a)+O(b³)`.
On the other side, `||D_x χ_1||²=1/4` by the SU(2) Casimir/rotational identity and `K(D_x χ_1)=3a D_xχ_1` at b=0. Thus
`2〈D_xΩ,KD_xΩ〉=2(b/(6a))²(3a)(1/4)+O(b³)=b²/(24a)+O(b³)`.
The deterministic verifier checks this coefficient exactly. This is an analytic consistency check, **not** a numerical interacting Penrose-vacuum computation or proof of the general theorem (which is the operator argument above).

## Proof status and next noncircular gate

**Proved:** exact QH-1/QH-2 mixed-link magnetic vacuum Hessian–force susceptibility Ward identity and kernel; QH-4 Fisher-Hessian identity; QH-6 Gauss-sector exclusion under full vertex Gauss conditions. Source coefficients and boundary assumptions explicitly stated. Original three-face Z5 geometry used only as an incidence fixture.

**Open:** direct *physical gauge-invariant source* covariance bound with fixed physical support; a model-specific Gauss-reduced vacuum Hessian/conditional variance estimate on the good core, including exceptional plaquettes; interacting quartic resolvent; uniform physical spectral gap; nontrivial continuum reconstruction; original Stage7/26 action identity. The prior classical flat Hessian and current averaged Hessian are neither sufficient nor appropriate replacements for this missing quantum input.

**Recommended next approach:** use gauge-invariant Wilson-source perturbations and the exact physical Dirichlet form of `Y_h` instead of constant-link derivative susceptibilities. Test a **regional conditional-energy penalty for fixed-source fluctuations**, including the actual Gauss projection, or directly construct an observable-specific local spectral comparison. No physical gap is to be assumed, and the desired variance rate must not be taken as an input.

**Integrity:** deterministic algebraic verifier `verify_quantum_hessian_ward.py`; no Monte Carlo; original Stage7/26 archives untouched.
