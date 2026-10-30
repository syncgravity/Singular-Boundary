# R3 — Ward identities, energy sum rules, and the infrared obstruction

October 26, 2026 · The Singular Boundary

## Setting
Let G be finite, with spatial links E and gauge group SU(2). On \(L^2(SU(2)^E)\), \(H=\sum_e a_e(-\Delta_e)+B(U)\), where \(a_e>0\), \(B\) is real, bounded, gauge invariant, and is a multiplication operator (weighted spatial Wilson action). With local gauge group \(\mathcal G=SU(2)^V\), the physical Hilbert space is the invariant subspace. Let \(\Omega>0\) be the normalized physical ground state, \(K=(H-E_0)|_{\Omega^\perp}\). The following are exact finite-volume identities, not continuum estimates.

## Theorem W1 (Gauss-law Ward identity)
Let \(G_v^a\) denote infinitesimal generators of the vertex gauge action. The Hamiltonian commutes with vertex gauge transformations. Physical vectors obey \(G_v^a\psi=0\), and gauge-invariant bounded observables commute with them. Consequently \(\langle\Omega,[G_v^a,O]\Omega\rangle=0\). This eliminates gauge-charged amplitudes, but yields no lower bound for energy eigenvalues in the gauge-singlet sector. Domains for unbounded generators are handled on smooth cylindrical functions followed by closure.

## Theorem F1 (local oscillator-strength / double-commutator sum rule)
Let A be a real bounded smooth gauge-invariant function of finitely many links, acting by multiplication. Set u=(A-\langle A\rangle)\Omega and its spectral measure \(d\mu_A(s)=\langle u,dP_K(s)u\rangle\) supported on s>0. Then
\[
\int_0^\infty s\,d\mu_A(s)=\langle A\Omega,(H-E_0)A\Omega\rangle=\sum_e a_e\int|\nabla_e A|^2|\Omega|^2\,dU=\frac12\langle\Omega,[A,[H,A]]\Omega\rangle.
\]
The Wilson magnetic potential B commutes with A, hence drops out of the double commutator. In particular the right-hand side is at most \(\sum_{e\in\mathrm{supp} A} a_e\|\nabla_e A\|_\infty^2\), independently of spatial volume for fixed support and coefficients. This is a positive-energy-weighted **upper** moment, not the inverse-energy-weighted R3 susceptibility.

For separated real multiplication observables A_X,V_Y, one likewise has \(\langle\Omega,[A_X,[H,V_Y]]\Omega\rangle=2\sum_e a_e\int \nabla_e A_X\cdot\nabla_e V_Y|\Omega|^2\,dU\), which vanishes for disjoint edge supports. This yields the cross-spectral first-moment cancellation \(\int s\,d\mu_{AV}(s)=0\) when supports are disjoint (with the appropriate symmetric real part). It does not force \(\int s^{-1}\,d\mu_{AV}(s)=0\).

## Proposition F2 (exact infrared representation)
For u=Q A\Omega and v=Q V\Omega, \(\chi^{<\eta}_{AV}=-2\mathrm{Re}\langle u,K^{-1}P_{(0,\eta]}v\rangle\). With positive spectral measure \(\mu_A\), the diagonal susceptibility is \(\chi_{AA}^{<\eta}=-2\int_{(0,\eta]}s^{-1}\,d\mu_A(s)\). The positive first moment F1 and the total mass \(\mu_A((0,\infty))\le\|A\|^2\) do not bound the negative first moment uniformly as the low spectrum approaches zero.

## Counterexample C1 (Ward identity and sum rule do not imply infrared bound)
On a two-dimensional Hilbert space define \(H_\epsilon=\mathrm{diag}(0,\epsilon)\), \(\Omega=(1,0)\), and \(A=\sigma_x\). Let every gauge transformation act trivially, so both vectors are gauge singlets and every Ward identity holds. Then the spectral weight of u=A\Omega equals one at \(\epsilon\); the oscillator-strength moment is \(\epsilon\to0\), while the static susceptibility magnitude is \(2/\epsilon\to\infty\). This is a logical counterexample to an inference from Ward identities and positive sum rules alone, **not** a counterexample to the particular Yang–Mills Hamiltonian.

For spatially separated operators on general local systems, vanishing cross first moment still permits nonzero cross inverse moment: choose two excited energies s1,s2 and signed cross masses c1,c2 with s1 c1+s2 c2=0 but c1/s1+c2/s2\ne0. Such signed cross measures are permitted because cross measures need not be positive.

## Multiscale test M1
For dyadic bands I_n=(2^{-n-1}\eta,2^{-n}\eta], one has exactly
\[
|\chi^{<\eta}_{AV}|\le 2\sum_{n\ge0}\frac{2^{n+1}}\eta\|P_{I_n}u\|\,\|P_{I_n}v\|.
\]
A genuine proof requires a **new** infrared bound such as \(\|P_{(0,s]}u\|^2\le C_A s^{1+\alpha}\) and a distance-sensitive cross measure estimate. W1 and F1 do not supply either: they constrain positive moments, not negative moments. Splitting into scales alone does not change this.

## R2 (separate continuum obligation)
To use any R3 estimate along a->0, normalize energy thresholds and observables in physical units, control a-dependent electric coefficients and the renormalization of local Wilson operators, and establish constants independent of cutoff and physical volume. The finite-cutoff statements above do not prove R2.

## Conclusion
Independently proved: exact Gauss-law Ward identities; a local oscillator-strength (f-sum) identity; a cross-first-moment cancellation for disjoint multiplication observables; the dyadic susceptibility inequality. Not proved: a low-energy suppression estimate or distance decay for the inverse-energy-weighted spectral measure. No continuum mass-gap conclusion follows. This rules out a common, circular route: replacing the infrared resolvent by a positive first-moment commutator estimate.

## References
Hastings and Koma, *Spectral Gap and Exponential Decay of Correlations*, Communications in Mathematical Physics 265 (2006), 781–804, doi:10.1007/s00220-006-0030-4. Bravyi, Hastings and Verstraete, *Lieb-Robinson Bounds and the Generation of Correlations and Topological Quantum Order*, Physical Review Letters 97 (2006), 050401. These results establish important locality implications under their respective hypotheses, but neither proves the missing Wilson-model R3 infrared estimate.
