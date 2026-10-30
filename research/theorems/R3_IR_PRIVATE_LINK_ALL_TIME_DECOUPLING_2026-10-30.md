# Private-link Euclidean decoupling Ward identity in the physical Wilson vacuum

2026-10-30 — R3-IR-394. **Status:** proved exact fixed-finite-volume Wilson statement on a *coordinate hyperplane* of the neighbor-coupling cube, not a bulk full-coupling sign theorem.

## Setup

Take a finite original-link SU(2) rhombus disk, with the target magnetic face \(f\) deleted, and one neighboring face \(g_i\) coupled with parameter \(t_i=0\). Let \(e_i\) be their shared edge. Assume this edge belongs to no other retained magnetic face (edge-to-edge disk). Write \(x=U_{e_i}\), \(y\) for the remaining links. The *unrestricted original-link* elliptic Hamiltonian (before taking the invariant subspace) splits exactly
\[
H_0=a_e(-\Delta_x)\otimes 1+1\otimes H_y,
\]
because no retained Wilson magnetic term involves \(x\). The unique normalized strictly positive full-space ground state is \(1_x\otimes\omega(y)\), independent of \(x\); it is Gauss invariant and hence is also the physical vacuum. Denote it \(\Omega\). Its ground-state Doob semigroup has stationary probability \(\Omega^2\,d\mu_xd\mu_y\) and splits into independent stationary \(x\)-Brownian and \(y\)-interacting processes. Gauge-invariant insertions may be computed in the unrestricted ground-state representation because the full Hamiltonian commutes with the Gauss projector and the vacuum is physical.

Let \(O=k_a(W_f(x,y))\) be any bounded class observable of the target holonomy. Haar integration in \(x\) at fixed \(y\) gives a constant
\[
\overline O:=\int_{SU(2)}O(x,y)\,d\mu_x=\int_{SU(2)}k_a(W)\,d\mu(W)=\alpha_a^2.
\]

## Theorem: all-time environment decoupling

For any bounded functional \(G\) of the entire *stationary Euclidean path* \(y(\tau)\), over any finite collection of times or a finite time window, with no dependence on \(x(\tau)\),
\[
\boxed{\quad
\mathbb E_{\Omega}^{\mathrm{stat}}[O(W_f(x(0),y(0)))G(y(\cdot))]
=\alpha_a^2\mathbb E_{\Omega}^{\mathrm{stat}}G(y(\cdot)).
\quad}\tag{PL-1}
\]
Proof: the \(x\)-path and \(y\)-path are independent under the ground-state transform. Conditional on the entire \(y\)-path, \(x(0)\) is Haar distributed. The fixed-\(y(0)\) Haar average of the holonomy class observable is \(\alpha_a^2\). QED.

Consequently, every mixed **joint cumulant** of \(O(W_f(0))\) and any positive number of random variables depending *solely* on the \(y\)-path is zero. In particular, for \(j\neq i\), the neighboring plaquette \(p_{g_j}\) does not use \(e_i\) in a regular disk, and all cross Euclidean correlations between \(O(W_f(0))\) and arbitrary products of the integrated \(p_{g_j}\) vanish on \(t_i=0\), so long as every inserted plaquette avoids \(e_i\).

## Physical reduced resolvent consequence

At \(t_i=0\), for any bounded, gauge-invariant multiplier \(B(y)\) independent of \(x\), let \(Q=1-|\Omega\rangle\langle\Omega|\) and \(R=(H_0-E_0)^{-1}\) on its physical orthogonal complement. Then
\[
\boxed{\quad
\langle QO\Omega,R QB\Omega\rangle=0.
\quad}\tag{PL-2}
\]
Indeed \(QB\Omega\) lies in the \(x\)-constant invariant sector of the kinetic factorization; this sector is preserved by the full reduced resolvent. But \(QO\Omega\) has zero projection onto the \(x\)-constant sector, because its \(x\)-average is \(\alpha_a^2\Omega\). Their inner product vanishes. The same statement holds if one first restricts to the physical gauge-invariant sector, since the full-space resolvent preserves gauge invariance and agrees on physical inputs.

PL-1 and PL-2 are exact for *arbitrary couplings on the other retained faces*, requiring no uniform spectral gap and no perturbation series.

## What does not follow

The neighbor observable \(p_{g_i}\) **does** use the private link \(e_i\) even when its coefficient is switched off. Thus PL-1 does not directly imply the sign or vanishing of \(\langle QO\Omega,R Qp_{g_i}\Omega\rangle\). Vanishing of the *own-coordinate* first response at \(t_i=0\) is a different archived center-flux/evenness selection statement (FN-2), not a consequence of PL-1.

At full coupling \(t_i=1\), the private link is no longer magnetically private, so the exact factorization breaks. In particular, PL-1 does **not** prove that the integrated off-diagonal signed source alignment is favorable, does not bound the eighth-order mixed response, and does not close the Penrose cap or mass gap.

## New targeted obligation

Quantify the loss of all-time private-link decorrelation as \(t_i\) increases from 0 to 1 with the genuine Wilson fundamental-affine perturbation \(-t_i b_i p_{g_i}\). Any resulting signed bound must retain the correlation between target cap and the *same* neighbor source \(p_{g_i}\), not confuse it with independent-of-edge environment observables. It must be nonperturbative at \(b_i\asymp h^{-2}\); the previously recorded finite-gap power-series bound cannot reach physical full coupling.

Dependencies: archived FN-1/2 (private link and symmetry), R3-IR-392/393 (signed physical source response). This is an exact new all-time decoupling extension and not a Yang-Mills mass gap theorem.
