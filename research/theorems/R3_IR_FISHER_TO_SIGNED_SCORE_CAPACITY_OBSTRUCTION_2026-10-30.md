# Sharp obstruction: radial Fisher energy does not bound one-sided center score

**2026-10-30 | Classification:** exact functional-analytic counterexample **in smooth positive SU(2) class amplitudes**, not a Wilson-Hamiltonian ground-state counterexample. This tests whether the previously proved local target Fisher bound (R3-IR-378) can by itself close the signed-current gate.

## Proposition

For every \(\delta>0\) and \(L>0\), there exists a smooth strictly positive class function \(\Omega\) on \(SU(2)\), normalized in Haar \(L^2\), whose marginal score Fisher energy is less than \(\delta\), while its positive one-sided radial current budget on \(0<u<\pi/2\) is at least \(L\). This remains true for a product original-link lattice with \(\Omega\) depending only on the target Wilson class angle and invariant under the full vertex Gauss group.

Consequently **no universal bound** of the form \(\mathfrak T_f\le F(I_f)\), bounded uniformly on Fisher-energy sublevel sets, follows from the Fisher estimate alone; indeed \(\mathfrak T_f\) can be arbitrarily large while \(I_f\) tends to zero.

## Construction and proof

Take a smooth monotone cutoff \(\eta:[0,\infty)\to[0,1]\), \(\eta(s)=0\) for \(s\le1\), \(\eta(s)=1\) for \(s\ge2\), with \(\|\eta'\|_\infty=C\) and derivatives flat at the endpoints. Let \(a>0\) be small, \(2a<\pi/2\), and \(\epsilon=e^{-L}\). Define a positive smooth class amplitude by
\[
\widetilde\psi_{a,\epsilon}(u)=\epsilon+(1-\epsilon)\eta(u/a),
\qquad
\psi_{a,\epsilon}(u)=\frac{\widetilde\psi_{a,\epsilon}(u)}{
\left(\int_0^\pi\widetilde\psi_{a,\epsilon}(u)^2
\frac{2\sin^2u}{\pi}\,du\right)^{1/2}}.
\]
Because it is constant near \(u=0\) and \(u=\pi\), this is a smooth SU(2) class function. Use it as an original-link gauge-invariant amplitude \(\Omega(U)=\psi_{a,\epsilon}(u_f(U))\). Product Haar pushes the target holonomy to Haar exactly, so the radial likelihood-ratio square root is precisely \(\psi_{a,\epsilon}\). The full Gauss group acts on the Wilson holonomy by conjugation, leaving the trace unchanged.

The cutoff derivative is supported in \([a,2a]\), and
\[
\int_0^\pi |\partial_u\psi_{a,\epsilon}|^2
\frac{2\sin^2u}{\pi}\,du
\le
\frac{2 C^2}{\pi a^2 N_{a,\epsilon}^2}
\int_a^{2a}u^2du
\le C_0 a
\]
for a universal \(C_0\), uniformly in \(0<\epsilon<1\), once \(a\) is sufficiently small. Here \(N_{a,\epsilon}\to1\) uniformly as \(a\downarrow0\), since the amplitude differs from one only on a cap of Haar volume \(O(a^3)\).

By the exact score contraction theorem, the marginal Fisher information is
\[
I_f=A_f\int_0^\pi |\partial_u\psi|^2
\frac{2\sin^2u}{\pi}\,du\le A_f C_0a;
\]
choose \(a<\delta/(A_f C_0)\). On the other hand,
\(\partial_u\log\psi\ge0\) for \(u\in[a,2a]\), and by the exact radial score identity \(\mathfrak T_f=\int_0^{\pi/2}[\partial_u\log\psi]_+du\). Therefore
\[
\mathfrak T_f=\log\psi(2a)-\log\psi(a)
=-\log\epsilon=L.
\]
The normalization cancels from the logarithmic difference. This proves the claimed simultaneous arbitrarily small Fisher energy and arbitrarily large one-sided score variation.

## Interpretation

The degeneracy is geometric, not a sign error. A deep but tiny center-cap suppression costs little **Haar-weighted Dirichlet energy** (capacity of shrinking caps in the 3-dimensional SU(2) radial geometry), while the logarithmic depth can be arbitrarily large. Thus even a local score Fisher bound tending to zero cannot establish the center score budget without *an additional anti-depletion principle*.

This is a counterexample to **an inference between functional inequalities**, not a claim that this amplitude minimizes any specified positive Wilson Hamiltonian. The actual physical ground-state eigenvalue equation may exclude these profiles. To close the completed-cage gate one must exploit that equation through a uniform local Harnack / conditional-density estimate, a signed-current differential inequality, or a genuinely new mechanism controlling the cap depth.

## Citation within repository

Relies on \`research/theorems/R3_IR_TARGET_SCORE_FISHER_CONTRACTION_2026-10-30.md\` only for the identification of the radial current with the positive log-amplitude variation. The smooth-class construction and Fisher computation above are independent and require no numerical simulation.
