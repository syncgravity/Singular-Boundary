# P2/T2 — Exact transported quantum-vacuum entropy and time-averaged force
**2026-11-06; finite original-link cubic SU(2) research audit. Independent mathematical review pending. All P0–P5/T0–T5 gates remain OPEN.**

## Model
Let \(\mathcal U=SU(2)^E\) be the compact original-link configuration space for a finite open 3D cubical regulator with four distinct links per face, product normalized Haar measure \(\mu\), product bi-invariant metric with generators \(T_j=i\sigma_j/2\). Let \(x_p=\tfrac12\mathrm{tr}_2U_p\), \(S=\sum_{p\in P}(1-x_p)\), \(G=\|\nabla S\|^2\), and the full classical **spatial** Wilson gradient flow \(\dot U_s=-\nabla S(U_s)\) with map \(\Phi_s\). The quantum Hamiltonian is **separate**: \(H=\alpha\sum_e(-\Delta_e)+\beta S\), with \(\alpha=g_0(h)^2/(2h)\), \(\beta=2/[g_0(h)^2h]\). Its unique positive interacting ground state \(\Omega\) defines \(\nu_0=\Omega^2\mu\); write \(\nu_s=(\Phi_s)_\#\nu_0\). The prior cubic variational theorem (draft PR #82) supplies \(\mathbb E_{\nu_0}S/|P|\le b_{h,R}:=(3g_0(h)^2/2)\sqrt{|E|/|P|}\). The earlier full nonlinear classical flow theorem gives \(S(\Phi_sU)+\int_0^sG(\Phi_rU)dr=S(U)\).

## Theorem A — exact finite-regulator probability transport
In the stated metric,
\[
\Delta_{\mathcal U}S=3\sum_p x_p=3(|P|-S).
\]
Indeed, each original link Laplacian gives \(\Delta_ex_p=-3x_p/4\) for the four distinct links in face p, and zero otherwise. Since the flow vector field is \(-\nabla S\), Liouville's formula yields the Riemannian Haar Jacobian
\[
J_s(U)=\exp[-3\int_0^s(|P|-S(\Phi_rU))dr].
\]
Writing \(d\nu_s=\rho_s d\mu\), change of variables gives
\[
\rho_s(\Phi_sU)=\rho_0(U)\exp[3\int_0^s(|P|-S(\Phi_rU))dr].
\]
Consequently the *Haar-relative entropy* satisfies, exactly,
\[
D(\nu_s\|\mu)-D(\nu_0\|\mu)=3\int_0^s\{ |P|-\mathbb E_{\nu_0}S(\Phi_rU)\}\,dr,
\]
and the existing monotonicity/variational bounds imply
\[
3|P|s(1-b_{h,R})\le D(\nu_s\|\mu)-D(\nu_0\|\mu)\le3|P|s.
\]
In particular at physical reference spatial flow time \(s=\tau/h^2\), the lower bound per face is \(3\tau(1-b_{h,R})/h^2\), which grows when \(b_{h,R}\to0\). This concentration of flowed probability relative to Haar is **not** a statement about divergent physical curvature or the existence or absence of a mass gap.

## Theorem B — physical-time averaged, volume-uniform lattice-force bound
For any \(0\le\tau_0<\tau_1\), letting \(Q(\tau,U)=G(\Phi_{\tau/h^2}U)/|P|\),
\[
\frac1{\tau_1-\tau_0}\int_{\tau_0}^{\tau_1}\mathbb E_{\nu_0}Q(\tau,U)d\tau\le\frac{h^2b_{h,R}}{\tau_1-\tau_0}.
\]
Proof: substitute \(\tau=h^2s\) in the exact pathwise action-dissipation identity, then use \(\mathbb E_{\nu_0}S/|P|\le b_{h,R}\). For an independent uniform \(\Theta\in[\tau_0,\tau_1]\), Markov and union bounds give
\[
\mathbb P\left\{ S(\Phi_{\Theta/h^2}U)/|P|>\delta\ \mathrm{or}\ Q(\Theta,U)>\epsilon\right\}
\le\min\left(1,\frac{b_{h,R}}\delta+\frac{h^2b_{h,R}}{(\tau_1-\tau_0)\epsilon}\right).
\]
These are **unrenormalized lattice-unit** expectations at a randomly sampled physical time, not pointwise regularity for each deterministic time, physical curvature tightness or spectral decay. Center saddles have zero force despite positive action.

## Exact one-face instability calibration
For an isolated four-original-link plaquette \(S=1-x\), \(\|\nabla x\|^2=1-x^2\). Hence \(\dot x=1-x^2\) and \(x_s=(x_0+\tanh s)/(1+x_0\tanh s)\). The preimage of \(x_s\le-1+\delta\) obeys
\[
1+x_0\le \frac{(1-\tanh s)\delta}{1+\tanh s(1-\delta)}
\sim \frac{\delta}{1-\delta/2}e^{-2s}.
\]
The Haar cap near -I is \(O((1+x)^{3/2})\), so for any initial one-face smooth density bounded by \(M_0\), the probability of remaining within a fixed cap of -I is at most \(C_\delta M_0e^{-3s}\) for \(s\ge1\). This is **not transferred to the coupled cube**: cross-plaquette gradients destroy the scalar ODE. The one-face exact Jacobian \((\cosh s+x_0\sinh s)^{-3}\) provides an independent entropy calibration.

## Verifier, provenance, next gate
A deterministic checker passed **142** assertions including one-face flow/Jacobian identities, center-cap inversion, nine independent entropy double-quadrature comparisons and cubic incidence ratios. It is not a coupled-vacuum simulation. Complete mathematical report, Python verifier, log, SHA-256 manifest and CRC-checked ZIP are in Library: `/The Singular Boundary/Proof Audits/R3_COUPLED_VACUUM_FLOW_ENTROPY_2026_11_06.zip`.

**Next open gate:** establish a truly coupled, vacuum-weighted signed-covariant estimate for a renormalized fixed-physical-support observable at positive spatial flow radius, with a quantified persistence bound for unstable near-center regions and uniformity in both h and volume. Do not promote this entropy/time-average theorem to physical curvature regularity, continuum OS existence or an interacting mass gap.
