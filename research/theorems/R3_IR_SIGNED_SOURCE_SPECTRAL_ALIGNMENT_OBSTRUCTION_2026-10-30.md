# Signed-resolvent order obstruction and a precise Wilson-specific spectral alignment certificate

**Date 2026-10-30. Status:** exact finite-volume identities and an explicit positive reversible two-state countermodel. This does NOT establish a negative sign for an actual SU(2) Wilson neighbor response and does NOT close cap survival or the mass gap.

## Physical formula and sign certificate

For the genuine Gauss-invariant four-neighbor Wilson Hamiltonian H(t) in R3_IR_CAP_TRANSPORT_SIGNED_PHYSICAL_RESOLVENT_2026-10-30.md, take the normalized positive vacuum Ω, O=k_a(W_f)>=0, p_i=(1/2)Tr W_{g_i}, F=<Ω,OΩ>>0, and the positive reduced resolvent R=(H-E_0)^{-1} on Ω-perp.

The exact established identity is
\[
\partial_{t_i}\log F=\frac{2b_i}{F}\langle QO\Omega,R Qp_i\Omega\rangle.
\]
Define the **source-alignment measure**, for Borel B subsets of (0,infinity),
\[
\sigma_{O,i}(B)=\langle QO\Omega,\mathbf1_B(H-E_0)Qp_i\Omega\rangle.
\]
This is a finite **signed** measure, not a positive spectral measure. At fixed finite volume,
\[
\boxed{\quad \partial_{t_i}\log F=\frac{2b_i}{F}\int_{(0,\infty)}E^{-1}d\sigma_{O,i}(E).\quad}\tag{SA-1}
\]
Therefore a sufficient *Wilson-specific* hypothesis for nondecreasing cap response in a given coupling is the spectral alignment inequality
\[
\int E^{-1}d\sigma_{O,i}(E)\ge0.
\]
A weaker integrated diagonal completion suffices for the Haar-order cap survival:
\[
\int_0^1\sum_i\frac{2b_i}{F(\lambda\mathbf1)}
\int E^{-1}d\sigma_{O,i,\lambda}(E)\,d\lambda\ge-\log2.
\tag{SA-2}
\]
**Neither has been proved.** These are exact sign targets, not assumed consequences of spectral positivity.

The signed measure admits total-variation control from two *positive* source measures via the spectral Cauchy--Schwarz inequality, but that erases its sign and reintroduces the low-energy obstruction.

## An exact two-state reversible countermodel to automatic sign

Consider the connected two-state reversible Markov generator with stationary weights (1/2,1/2):
\[
L=\begin{pmatrix}-1&1\\1&-1\end{pmatrix},\qquad K=-L.
\]
On the real L² stationary space, the constant is the simple positive ground vector, and the orthogonal mode \(v=(1,-1)\) has energy 2, hence \(R v=v/2\).

Choose strictly positive bounded observables \(O=(2,1)\) and \(P=(1,2)\). Their centered vectors are
\[
QO=\tfrac12v,\quad QP=-\tfrac12v.
\]
Therefore
\[
\boxed{\langle QO,R QP\rangle=-\tfrac14<0.}\tag{SA-3}
\]
If instead \(P=(2,1)\), the overlap is \(+1/4\). In both examples the reversible semigroup is positivity preserving and its ground state is strictly positive, and both observables are positive. Thus **semigroup positivity, positive R, and positive O cannot determine the cross-source resolvent sign**.

This is not an original-link SU(2) Wilson counterexample: the two-state dynamics lack Wilson plaquette geometry, Gauss constraints, and four-neighbor selection. It excludes only an unjustified universal positivity argument.

## Implication for this project

The mathematical path from the exact transport identity to a nonnegative signed response must exploit genuinely Wilson-specific **joint** information, e.g. a correlation inequality or a proved alignment property for cap and neighbor plaquette sources in the physical interacting vacuum. The archived spin-selection identities constrain vanishing orders near coordinate hyperplanes, but do not prove SA-1's sign at full coupling. Absolute gap-dependent bounds already fail at strong-field scaling.

To establish the desired cap survival, prove SA-2 (or another scale-uniform negative-transport lower bound) with original-link Wilson geometry, explicitly without assuming a uniform physical gap or clustering. This claim is OPEN.
