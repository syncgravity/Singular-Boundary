# PF-I16 — D4 noniterability on the authenticated three-face source graph

**2026-11-09. Exact finite-graph functional-analytic obstruction, NOT a mass-gap counterexample.** Complete proof, numerical radial check, log and manifest: Library \`/The Singular Boundary/Proof Audits/PF_I16_D4_CRITICALITY_2026_11_09.zip\`. Uses the authenticated genuine three-rhombus source motif, not the disallowed opposite-face coordinate cube and not a cubic spatial surrogate.

## Geometry and operator

The source motif has 8 vertices, 10 original links and cycle rank r=10−8+1=3. Spanning-tree gauge fixing gives the gauge-invariant orbit space SU(2)^3/Ad(SU(2)), whose regular irreducible-triple stratum is a smooth dimension-6 manifold. The positive original-link electric Casimir \(K=\sum_ea_e C_e\), \(a_e>0\), induces a uniformly elliptic operator in any sufficiently small regular quotient chart, with positive smooth Haar-pushforward density.

Let \(\Gamma_K(F,G)=\sum_ea_e\langle\nabla_eF,\nabla_eG\rangle\), \(P_0\) the Haar-mean-zero projection, and
\[
D_p(F)^2=\sum_ea_e\|\nabla_eF\|_{L^p(\mu)}^2.
\]
The preceding PF-I16 theorem established \(\|K^{-1}P_0\Gamma_K(F,G)\|_2\le D_4(F)D_4(G)/(3a_0)\), but did **not** control \(D_4\) of the output.

## Exact no-go theorem

\[
\boxed{\text{No finite }C\text{ satisfies }D_4(K^{-1}P_0\Gamma_K(F,G))\le C D_4(F)D_4(G)\text{ for all smooth gauge-invariant }F,G.}
\]

Proof: In a regular gauge quotient chart of dimension \(d=6\), choose \(f\in C_c^\infty(B_1)\), \(f\ge0\) nonconstant, and define \(F_\varepsilon(x)=\varepsilon^{1-d/4}f((x-x_0)/\varepsilon)\). Uniform local ellipticity and smooth measure give \(D_4(F_\varepsilon)\asymp1\) and \(D_{4/3}(F_\varepsilon)=O(\varepsilon^{d/2})=O(\varepsilon^3)\). Set \(h_\varepsilon=\Gamma_K(F_\varepsilon,F_\varepsilon)\) and \(u_\varepsilon=K^{-1}P_0h_\varepsilon\). The exact weak identity
\[
\mathcal E_K(u_\varepsilon,F_\varepsilon)
=\int F_\varepsilon h_\varepsilon\,d\mu
-\Bigl(\int F_\varepsilon d\mu\Bigr)\Bigl(\int h_\varepsilon d\mu\Bigr)
\]
has a strictly positive leading contribution \(c_1\varepsilon^{1+d/4}=c_1\varepsilon^{5/2}\) and a negligible mean correction \(O(\varepsilon^{1+5d/4})=O(\varepsilon^{17/2})\). Edgewise Hölder and weighted Cauchy-Schwarz imply \(|\mathcal E_K(u_\varepsilon,F_\varepsilon)|\le D_4(u_\varepsilon)D_{4/3}(F_\varepsilon)\). Hence
\[
\boxed{D_4(K^{-1}P_0\Gamma_K(F_\varepsilon,F_\varepsilon))\ge c_2\varepsilon^{-1/2}\to\infty,}
\]
while the input \(D_4\) norms stay uniformly bounded. This disproves \(D_4\)-bilinear iteration **on one fixed original source graph**. Smooth compact bumps are available, and all arguments are on the regular gauge-invariant quotient.

The scaling generalizes: on a regular orbit quotient of dimension \(d>4\), the obstruction exponent is \(1-d/4<0\). The \`d\` here is **configuration space**, not physical spacetime.

## Independent radial consistency check

For a flat 6-dimensional chart choose \(f(r)=(1-r^2)^4_+\), a \(C^3\) illustrative profile approximable by smooth bumps. Exact beta-function integrals and independent SciPy radial quadrature give
\[
J_4=\int|\nabla f|^4dx=2.052387027836264,\quad
J_{4/3}=\int|\nabla f|^{4/3}dx=1.2012396160328742,\quad
J_c=\int f|\nabla f|^2dx=0.24780241103136716.
\]
After \(D_4\)-normalization, the flat-model weak-duality lower-bound coefficient is \(J_c/(J_4^{1/2}J_{4/3}^{3/4})=0.1507487300533894\), multiplying \(\varepsilon^{-1/2}\). Six epsilon cases reproduce this scaling exactly within quadrature accuracy. **This numerical coefficient is NOT asserted as the constant for the curved source-gauge quotient**, whose local metric differs.

## Status and next gate

This result rules out only the unqualified \(D_4\times D_4\to D_4\) estimate. It does not show that the actual score perturbation series diverges or that the interacting Hamiltonian is gapless; it does not rule out stronger analytic/Gevrey, spin-network weighted, or source-local polymer norms that preserve extra derivative control. The next objective is to formulate and prove such an iterable volume-uniform norm estimate, or a different interacting-Poincaré mechanism. Source-selected physical energy/time, continuum reconstruction and 4D Yang–Mills mass gap remain OPEN. Canonical main, historical source bytes and Observatory certification are unchanged.