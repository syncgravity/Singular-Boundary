# The Singular Boundary — Deleted-vacuum flat-holonomy small-ball criterion

**Date:** 2026-10-29. **R3-IR audit classification:** an exact finite, genuinely nonlinear SU(2) Hamiltonian variational theorem; a conditional uniform Penrose refinement and sparse-defect exclusion theorem; and a necessary stretched-exponential *deleted-vacuum* flat-ball obstruction if the *full* vacuum has persistent extreme defects. **Not established:** any uniform polynomial lower bound for the deleted-vacuum flat-holonomy probability in a cycle-rich Penrose interior, the nonlinear bulk deletion bound without that hypothesis, the physical continuum gap, the quartic resolvent, or Stage7/26 source-level identity.

## Model and notation

Let \(G=(V,E,F)\) be a finite simply connected, face-complete planar rhombus cellulation, with four edges per face and no edge incident on more than two faces. Work in the physical all-vertex Gauss-invariant SU(2) link Hilbert space, for
\[
H=\sum_e a_e(-\Delta_e)+\sum_f b_f d_f,\quad d_f=1-\tfrac12\operatorname{ReTr}W_f,\quad a_e>0,\ b_f>0.
\]
The electric normalization is \(-\Delta\chi_j=j(j+1)\chi_j\). Its positive normalized vacuum \(\Omega\) is unique. For a specified face \(f\), set \(H_f^-=H-b_fd_f\), \(E_f^-=E_0(H_f^-)\), \(\Omega_f^-\) its positive normalized physical ground state, \(\nu_f^-=(\Omega_f^-)^2\,d\mathrm{Haar}\), and \(\Delta_f=E_0(H)-E_f^-\in[0,2b_f]\). Let \(A_f=\sum_{e\in\partial f}a_e\). No private-edge, dual-bridge, Gaussian comparison, clustering, or uniform excitation gap is assumed.

## Theorem FB-1 — exact all-bulk deletion trial inequality

For every \(\kappa>0\), write \(L_f(\kappa)=\mathbb E_{\nu_f^-}e^{-2\kappa d_f}\), \(\bar d_{f,\kappa}=\mathbb E[d_fe^{-2\kappa d_f}]/L_f(\kappa)\). Then
\[
\boxed{\Delta_f\le (b_f+\tfrac12A_f\kappa^2)\bar d_{f,\kappa}.}\tag{FB-1}
\]
**Proof:** the normalized gauge-invariant trial state is proportional to \(e^{-\kappa d_f}\Omega_f^-\). The exact (nonlinear) ground-state transform gives
\[
\langle e^{-\kappa d_f}\Omega_f^-,(H_f^--E_f^-)e^{-\kappa d_f}\Omega_f^-\rangle
=\kappa^2\mathbb E_{\nu_f^-}[e^{-2\kappa d_f}\Gamma(d_f)].
\]
The SU(2) Casimir identity is \(\Gamma(d_f)=\tfrac14A_f(1-p_f^2)=\tfrac14A_f(2d_f-d_f^2)\le\tfrac12 A_fd_f\). Add the \(b_fd_f\) energy, divide by the positive norm \(L_f(\kappa)\), and apply Rayleigh–Ritz. This is a trial about the **true deleted interacting vacuum**, rather than an independent-plaquette or Gaussian measure. QED.

## Theorem FB-2 — quantitative flat-holonomy small-ball criterion

Fix \(\kappa\ge1\), and denote
\[
m_f(\kappa)=\nu_f^-(d_f\le\kappa^{-1})>0.
\]
The positivity follows from the smooth strictly positive ground state on the compact SU(2) configuration manifold at every fixed regulator. On that event, \(e^{-2\kappa d_f}\ge e^{-2}\), so \(L_f(\kappa)\ge e^{-2}m_f(\kappa)\). For any \(\delta\ge0\), split the numerator of \(\bar d\):
\[
\mathbb E[d_fe^{-2\kappa d_f}]\le \delta L_f(\kappa)+2e^{-2\kappa\delta};\quad
\bar d_{f,\kappa}\le\delta+\frac{2e^2}{m_f(\kappa)}e^{-2\kappa\delta}.
\]
Choose \(\delta=(2\kappa)^{-1}\log(2e^2\kappa/m_f)\ge0\). Then
\[
\boxed{\bar d_{f,\kappa}\le\frac1\kappa\left[1+\tfrac12\log\frac{2e^2\kappa}{m_f(\kappa)}\right].}\tag{FB-2}
\]
At the balanced trial \(\kappa_f=\sqrt{2b_f/A_f}\ge1\), equations FB-1–2 yield
\[
\boxed{\Delta_f\le\frac{b_f}{\kappa_f}\left[2+\log\frac{2e^2\kappa_f}{m_f(\kappa_f)}\right].}\tag{FB-3}
\]
Equivalently, rearranging the *same unconditional finite-volume inequality*,
\[
\boxed{m_f(\kappa_f)\le 2e^4\kappa_f\exp(-\kappa_f\Delta_f/b_f).}\tag{FB-4}
\]
FB-4 is informative when the deletion cost is anomalously large; it is not a lower bound on \(m_f\). The bound applies even if f has four shared edges and the deleted Hamiltonian contains all neighboring magnetic interactions.

## Theorem FB-3 — conditional Penrose interior extreme-defect exclusion

Assume declared geometric coefficients on the fixed-area interior region D satisfy
\(0<A_-\le A_f\le A_+\), \(\beta_-h^{-2}\le b_f\le\beta_+h^{-2}\), and \(|D|\le C_Fh^{-2}\). If, in addition, the **actual magnetic-deleted vacuum** has a uniform polynomial flat-ball mass
\[
\inf_{f\in D}\nu_{f,h}^-(d_f\le\sqrt{A_f/(2b_f)})\ge c h^s
\]
with constants \(c,s>0\) independent of h, then FB-3 yields
\[
\boxed{\max_{f\in D}\Delta_f\le C_{c,s}h^{-1}[1+\log(1/h)].}\tag{FB-5}
\]
The earlier all-face exact single-plaquette exponential deletion-tail theorem, applied with a *common* allowed tilt \(s_h=c_0h^{-1}\), establishes
\[
\nu_h(d_f\ge h^{3/4})\le\exp(C_1h\Delta_f-c_1h^{-1/4}).
\]
Thus union over \(O(h^{-2})\) faces shows, for any fixed \(N>0\),
\[
\boxed{\nu_h(\max_{f\in D}d_f\ge h^{3/4})=O_N(h^N),}\tag{FB-6}
\]
and indeed \(\le\exp(-c'h^{-1/4})\) for small h, after readjusting c'. No face independence is used. By the already proved sparse-defect rare-event and good-cutoff theorems, the critically normalized fixed-area source difference \(R_h=\sqrt h\sum_{f\in D}q_f[(\arccos p_f)^2/2-d_f]\) satisfies \(\operatorname{Var}_{\Omega_h}(R_h)\to0\) for bounded q. **This is conditional on the new deleted-vacuum polynomial small-ball hypothesis, which remains OPEN for cycle-rich interiors.**

## Theorem FB-4 — persistent defects imply a stronger deleted-vacuum obstruction

Conversely, assume the same coefficient and region bounds but *not* the polynomial small-ball hypothesis. If along a refinement sequence
\[
\nu_h(\max_{f\in D}d_f\ge h^{3/4})\ge\varepsilon>0,
\]
then the earlier single-face Laplace inequality and pigeonhole principle yield at least one interior face \(f_h\) with
\[
\Delta_{f_h}\ge c_2h^{-5/4}-C_2h^{-1}\log(1/h).
\]
Boundary/private-edge faces already have \(\Delta_f=O(h^{-1})\), so an anomalous face must lie in the cycle-rich remainder. For small h, \(\Delta_{f_h}\ge(c_2/2)h^{-5/4}\). Since \(\kappa_{f_h}=\Theta(h^{-1})\) uniformly, FB-4 implies
\[
\boxed{\nu_{f_h,h}^-(d_{f_h}\le\sqrt{A_{f_h}/(2b_{f_h})})\le C h^{-1}\exp(-c_3h^{-1/4}).}\tag{FB-7}
\]
This is a necessary, *quantitatively anomalous depletion of nearly flat face holonomies in the **deleted** interacting ground state*. It is **not** an assertion that the event persists or that this depletion occurs. Because the deleted Hamiltonian has center-flux parity, it gives equal probability to \(p_f\) near +1 and near −1; under the conditional persistent-defect alternative, **both** center neighborhoods must be depleted. Parity alone gives no polynomial lower bound.

## Exact Haar and interacting SU(2) verification

For a single plaquette (or a dual-bridge/private-edge deleted face), the deleted-holonomy marginal is Haar. Its class-deficit density is \(\rho(d)=(2/\pi)\sqrt{d(2-d)}\) on \([0,2]\), hence for \(0<r\le1\),
\[
\frac{4}{3\pi}r^{3/2}\le\nu_{\rm Haar}(d\le r)\le\frac{4\sqrt2}{3\pi}r^{3/2}.
\]
This verifies the polynomial criterion with exponent s=3/2 for already-solved private-edge and dual-bridge faces, without extending it to cycle-rich bulk faces. `verify_deleted_flat_ball.py` computes these exact Haar probabilities, the tilted energy Rayleigh quotient, and independent interacting one-plaquette ground energies by SU(2) character-basis diagonalization for h=0.2,0.1,0.05,0.025, magnetic coupling b=4/h² and equal electric link coefficient a=1. It also reconstructs the original three-face, ten-edge Penrose spatial fixture. All checks pass; no Monte Carlo, no Stage7/26 or Q14 modification.

## Proof classification and next gate

**Independently proved at finite nonlinear SU(2):** FB-1–2, the all-bulk trial and quantitative flat-ball/converse bounds. **Proved conditional on declared Penrose scaling *and an unproved deleted-vacuum polynomial flat-ball lower bound*:** FB-3, full extreme-defect exclusion and fixed-support Wilson–angle equivalence. **Proved conditional on an unproved persistent full-vacuum extreme-event probability:** FB-4, a necessary stretched-exponentially depleted center-holonomy distribution in at least one deleted bulk vacuum. **Open:** proving the polynomial deleted-vacuum flat-ball bound on cycle-rich connected Penrose patches, or independently bounding the adverse low-energy mixed susceptibility. The full all-physical-sector mass gap, quartic resolvent, source nontriviality, continuum reconstruction and Stage7/26 action provenance remain open.