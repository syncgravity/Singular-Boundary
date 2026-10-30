# The Singular Boundary — Wilson cap response and sharp SU(2) representation resolution

**Research date:** 2026-10-29. **Program:** R3 independent reconstruction, finite 2+1D SU(2) Hamiltonian regulators. **Status:** exact nonlinear physical-sector interpolation and spectral-cutoff theorem; exact separate SU(2) heat-kernel obstruction to insufficient spin resolution. The needed actual-vacuum low-energy mixed response remains **OPEN**. No physical continuum mass gap is claimed.

## A. Setup and prior group-harmonic certificate

Let the finite spatial regulator be a simply connected face-complete planar rhombus disk with four edges per face, at most two faces per edge, and all-vertex Gauss invariance. Let

\[ H=\sum_e a_e(-\Delta_e)+\sum_g b_gd_g,\quad d_g=1-\tfrac12\operatorname{ReTr}W_g,\quad a_-\le a_e\le a_+,\quad \beta_-h^{-2}\le b_g\le\beta_+h^{-2}.\]

Fix any interior target face \(f\), and choose **one** edge-sharing neighbor \(g\). Throughout, the target magnetic term has been **deleted**, and we interpolate the neighboring magnetic term:

\[ H(u)=\sum_e a_e(-\Delta_e)+\sum_{k\ne f,g}b_kd_k+u b_gd_g,\qquad 0\le u\le1.\]

Write \(\Omega_u>0\) for its unique normalized, physical Gauss-invariant ground state, \(K_u=H(u)-E_0(u)\), \(Q_u=I-|\Omega_u\rangle\langle\Omega_u|\), \(G_u=Q_uK_u^{-1}Q_u\). Each finite-volume positive excitation energy is strictly positive; **no uniform gap** is assumed. At \(u=0\), the shared edge between \(f\) and \(g\) is private (belongs to no remaining magnetic face), so the ground state is independent of that link, and \(W_f\) is Haar under \(|\Omega_0|^2\). This exact one-neighbor bridge is valid for any interior face, including cycle-rich faces.

For a small geodesic angular radius \(a\), choose a fixed radial bump \(\phi\in C_c^\infty(SU(2))\), real, central, \(0\le\phi\le1\), supported on \(B_{a/2}\), and identically 1 on \(B_{a/4}\). More explicitly, scale a fixed smooth profile \(\phi_a(U)=\varphi(u(U)/a)\). Define

\[ \alpha_a=\int\phi_a\,dU,\quad \nu_a=\int\phi_a^2\,dU,\quad k_a=\phi_a*\phi_a^{\vee},\quad \phi_a^\vee(U)=\phi_a(U^{-1}).\]

The exact positive-convolution properties are

\[ k_a\ge0,\quad \operatorname{supp}k_a\subset B_a,\quad \|k_a\|_\infty\le\nu_a,\quad \int k_a=\alpha_a^2,\quad c_1a^3\le\alpha_a,\nu_a\le c_2a^3.\]

All constants depend on the fixed bump but **not** on the number of plaquettes. The observable \(k_a(W_f)\) is gauge invariant and positive. By the exact bridge Haar marginal, \(\langle k_a(W_f)\rangle_{u=0}=\alpha_a^2\).

## B. CR-1. Exact nonlinear one-neighbor cap-response Ward identity

The finite-volume analytic ground-state perturbation identity gives, for every bounded gauge-invariant multiplier \(O\),

\[ \frac{d}{du}\langle O\rangle_u=-2\operatorname{Re}\langle Q_uO\Omega_u,G_uQ_uW\Omega_u\rangle,\qquad W=b_gd_g.\]

For \(O=k_a(W_f)\), integrating from the *exact* Haar bridge reference yields

\[ \boxed{\langle k_a(W_f)\rangle_1=\alpha_a^2-2\int_0^1\operatorname{Re}\langle Q_uk_a\Omega_u,G_uQ_uW\Omega_u\rangle\,du.}\tag{CR1}\]

This identity includes every nonlinear magnetic interaction outside the one removed neighbor and operates on the true physical Hilbert space. It makes no sign assumption on the mixed response.

## C. CR-2. Uniform high-energy cutoff at physical energy \(Lh^{-2}\)

For any \(\Lambda>0\), let \(P_{u,>\Lambda}\) and \(P_{u,\le\Lambda}\) denote spectral projections of \(K_u\) onto the positive excitation spectrum. Its two reduced-response pieces commute with \(G_u\). Spectral Cauchy–Schwarz implies

\[ 2|\langle Q_uO\Omega_u,G_uP_{u,>\Lambda}Q_uW\Omega_u\rangle|\le\frac{2}{\Lambda^2}\sqrt{m_{1,u}(O)m_{1,u}(W)},\]

where \(m_{1,u}(O)=\langle O\Omega_u,K_uO\Omega_u\rangle=\mathbb E_{\Omega_u^2}\Gamma(O)\).

The SU(2) class-function gradients and bounded incidence give \(m_{1,u}(W)\le b_g^2 A_g/4\), \(A_g=\sum_{e\in\partial g}a_e\). The convolution derivative obeys

\[ \|\nabla k_a\|_\infty\le\|\nabla\phi_a\|_{L^1}\|\phi_a\|_\infty\le C_\phi a^2,\]

so \(m_{1,u}(k_a(W_f))\le C_\phi^2A_fa^4\), \(A_f=\sum_{e\in\partial f}a_e\). Consequently the **integrated high-energy contribution** obeys the exact finite-volume inequality

\[\boxed{\mathcal V_{a,>\Lambda}\le\frac{C_\phi a^2b_g\sqrt{A_fA_g}}{\Lambda^2}.}\tag{CR2}\]

Set \(a=a_h=\arccos(1-h)\asymp\sqrt h\), \(b_g\le\beta_+h^{-2}\), and \(\Lambda_h=Lh^{-2}\). Then

\[ \mathcal V_{a_h,>\Lambda_h}\le \frac{C}{L^2}h^3,\qquad \alpha_{a_h}^2\ge c h^3.\]

Choose a **fixed** numerical \(L\) large enough in terms of the declared electric, magnetic and smooth-bump constants that \(\mathcal V_{a_h,>\Lambda_h}\le \alpha_{a_h}^2/4\) for sufficiently small \(h\). No additional power of \(h\) in the cutoff is required.

## D. CR-3. Exact physical low-energy alternative for polynomial flat-ball mass

Define the **adverse low-energy mixed-response budget**

\[\mathcal S_{a,\le\Lambda}=2\int_0^1\Big[\operatorname{Re}\langle Q_uk_a\Omega_u,G_uP_{u,\le\Lambda}Q_uW\Omega_u\rangle\Big]_+\,du.\]

By (CR1), (CR2), and positivity of \(k_a\),

\[\boxed{\mathbb P_{\Omega_{f,h}^-}(B_a)\ge\frac{[\alpha_a^2-\mathcal S_{a,\le\Lambda}-\mathcal V_{a,>\Lambda}]_+}{\nu_a}.}\tag{CR3}\]

In particular, choose \(\Lambda_h=Lh^{-2}\) as above. Either

1. \(\mathcal S_{a_h,\le\Lambda_h}\le\alpha_{a_h}^2/4\). Then \(\mathbb P(B_{a_h})\ge \alpha_{a_h}^2/(2\nu_{a_h})\ge c h^{3/2}\), the required polynomial near-flat mass, giving the previously proved \(O(h^{-1}\log(1/h))\) deletion bound and extreme-defect reduction; or
2. \(\mathcal S_{a_h,\le\Lambda_h}>\alpha_{a_h}^2/4\gtrsim h^3\). The actual neighboring-plaquette interpolation has an **adverse gauge-invariant mixed resolvent response**, of the indicated scale, inside physical excitation energies \(E\le Lh^{-2}\).

This is an **unconditional dichotomy** at every sufficiently fine *finite* regulator. It is not evidence that case (1) actually occurs. The new independent nonlinear proof gate is the \(O(h^3)\) **low-energy cap-response** bound, which is a one-neighbor physical object. The result is independent of any Gaussian tangent comparison.

## E. CR-4. Necessity of near-angular spin resolution for character-sign tests

The preceding character-convolution certificate controlled integer-spin expectations \(c_j\) through \(J(h)=O(h^{-1/2-\varepsilon})\). We now show the near \(h^{-1/2}\) resolution is **not an artifact of that proof**.

For a positive integer \(J\), let \(t=J^{-2}\). Define the smooth normalized strictly positive **center-even SU(2) heat-kernel density**

\[F_t(U)=\tfrac12(K_t(U)+K_t(-U))=\sum_{j=0}^\infty (2j+1)e^{-j(j+1)t}\chi_j(U),\]

where only integer spins appear. Its exact nontrivial integer-spin coefficients are

\[c_j(F_t)=(2j+1)e^{-j(j+1)/J^2}\ge e^{-2}(2j+1),\quad 1\le j\le J.\]

Let \(0<a<c_*/J\), and choose a smooth **center-even** cutoff \(\eta_a(U)\in[0,1]\) that is zero on the two SU(2) center caps \(B_a(I)\cup B_a(-I)\) and 1 outside the corresponding doubled caps. Let \(\delta=\int F_t(1-\eta_a)\,dU\). The standard three-dimensional SU(2) heat kernel estimate \(\|F_t\|_\infty\le C t^{-3/2}\) gives \(\delta\le C(Ja)^3\). Pick \(c_*\) small enough that \(\delta<e^{-2}/2\).

For \(\widetilde F=F_t\eta_a/(1-\delta)\), all integer spins through \(J\) remain strictly positive:

\[c_j(\widetilde F)\ge\frac{(2j+1)(e^{-2}-\delta)}{1-\delta}>0,\quad 1\le j\le J,\]

but \(\Pr_{\widetilde F}(B_a(I))=0\). Replacing \(\eta_a\) by \(\eta_{a,\epsilon}=\epsilon+(1-\epsilon)\eta_a\) gives a **strictly positive smooth** center-even density with the same character signs while allowing arbitrarily small cap mass. Taking \(\epsilon=e^{-J^2}\) produces stretched-exponential cap depletion along \(a\asymp J^{-1}\).

Such a density is the square of the unique strictly positive ground state of a suitable smooth center-symmetric SU(2) *rotor* Hamiltonian \(-\Delta+V\), by choosing \(V=(\Delta\sqrt F)/\sqrt F\) plus an additive constant. **This is a separate quantum-rotor comparator, not the actual deleted Penrose Wilson vacuum.**

Thus checking sign positivity only through \(J(h)=o(h^{-1/2})\) cannot, even with smooth strict positivity and center symmetry, guarantee Haar-order mass of a cap at angular scale \(a_h\asymp\sqrt h\). The scale \(J\gtrsim h^{-1/2}\) in the earlier finite-spin certificate is structurally necessary in the class of general center-even positive SU(2) marginals. The full special Wilson Hamiltonian may impose additional constraints, which remain to be proved.

## F. Verification and research status

`verify_character_cap_response.py` independently checks the SU(2) character integrals, the smooth center-even heat-kernel cap-excision construction at \(J=4,8,12,24\), strictly positive low-spin characters, and exact \(h\)-powers in the ultraviolet spectral inequality. The rigorous bounds use the standard compact SU(2) heat kernel supremum estimate and elementary group convolution; the numerical checks are finite benchmark calculations only. No Monte Carlo. No historical Penrose Stage26 or Q14 archives altered.

**PROVED:** CR-1 exact one-neighbor nonlinear Wilson cap-response identity, CR-2 all-volume high-energy cutoff of order \(h^{-2}\) for this cap observable, CR-3 physical cap-vs-low-energy adverse-response dichotomy, and CR-4 sharp low-spin positivity counterexample at \(Ja\ll1\).

**OPEN:** control \(\mathcal S_{a_h,\le Lh^{-2}}\le \alpha_{a_h}^2/4\) for the *actual* cycle-rich deleted SU(2) Penrose vacuum; equivalent Wilson-specific character positivity/negative-budget control; all-bulk magnetic deletion, fixed-support source covariance, regulator-uniform physical mass gap and continuum reconstruction.
