# The Singular Boundary — Bulk-face center-flux deletion Ward theorem and uniform tangent deletion benchmark

**Research date:** 2026-10-28. **Audit branch:** `audit/2026-10-28-independent-reconstruction`.

**Evidence classification:** Theorems CF-1–CF-3 below concern the **actual finite nonlinear Gauss-invariant SU(2) Wilson Hamiltonian**, for *every* face, including bulk faces with no private edge. Theorem CF-4 concerns **only the exact shared-edge quadratic tangent Hamiltonian** for arbitrary growing face counts; it is not an approximation error bound for the nonlinear ground state. The desired physical-point bulk magnetic-deletion increment of order \(O(h^{-1}\operatorname{polylog}(1/h))\), full extreme-defect rarity and mass gap remain **OPEN**.

## 1. Model and prerequisites

Let \(G=(V,E,F)\) be an embedded simply connected face-complete oriented planar rhombus disk, with four links per face and at most two magnetic faces per link. On \(L^2(SU(2)^E,dU)\) (or its Gauss-invariant reducing subspace), define

\[
H=\sum_e a_e(-\Delta_e)+\sum_{g\in F}b_g(1-p_g),\qquad p_g=\frac12\operatorname{ReTr}W_g,\quad a_e,b_g>0.
\]

Use \(-\Delta\chi_{1/2}=3\chi_{1/2}/4\). The full-link ground state is unique and strictly positive, hence Gauss invariant. For a face \(f\) put \(H_f^-=H-b_f(1-p_f)\), \(E^-_f=E_0(H_f^-)\), \(\Omega_f^->0\) its normalized vacuum, \(K_f^-=H_f^--E_f^-\), \(A_f=\sum_{e\in\partial f}a_e\), and \(\Delta_f(b)=E_0(H_f^-+b(1-p_f))-E_f^-\). Here the *other* magnetic couplings stay fixed; the physical coupling is \(b=b_f\).

The previous single-face Laplace theorem gives, with the actual \(\Delta_f(b_f)\), for \(s<\sqrt{8b_f/A_f}\):

\[
\mathbb E_{\Omega}e^{s(1-p_f)}\le\exp\!\left[\frac{\Delta_f}{\sqrt{A_fb_f/8}}\operatorname{artanh}\left(s\sqrt{A_f/(8b_f)}\right)\right].\tag{PE-2}
\]

Thus an independent estimate of \(\Delta_f\), not merely a bound on its first derivative, is required for the extreme-defect tail at an interior face.

## 2. CF-1 — Exact bulk center-flux symmetry of the **deleted** Hamiltonian

Adjoin the exterior face \(\infty\) to the planar dual graph. For any \(f\in F\), choose an arbitrary dual edge-path from \(f\) to \(\infty\). Let \(\mathscr E_f\subset E\) be the primal links crossed by the path. Define the unitary physical multiplication/translation operator

\[
(T_f\Psi)(\{U_e\})=\Psi(\{(-I)^{1_{e\in\mathscr E_f}}U_e\}).
\]

Because \(-I\) is central in SU(2), \(T_f\) preserves Haar measure, commutes with every vertex gauge transformation, and commutes with each link electric Casimir. Each plaquette other than \(f\) is crossed an even number of times; \(f\) is crossed an odd number of times. Consequently

\[
T_fp_fT_f=-p_f,\qquad T_fp_gT_f=p_g\ (g\ne f),\qquad T_fH_f^-T_f=H_f^- .\tag{CF-1}
\]

This holds for *every* interior face, despite all four edges being shared, and even for nonuniform positive electric and magnetic weights. The ground state \(\Omega_f^-\) is positive and unique, so \(T_f\Omega_f^-=\Omega_f^-\). In particular

\[
\boxed{\langle p_f^{2k+1}\rangle_- =0,\quad \langle p_f\,F(p_g:g\ne f)\rangle_-=0,\quad \langle 1-p_f\rangle_-=1.}\tag{CF-2}
\]

The middle identity holds for any bounded Borel function of the *other face traces*. It shows conditional center symmetry, **not** a uniform Haar conditional distribution of the missing-face holonomy.

The minimum number of flipped primal links achieving the parity pattern 'flip only \(f\)' is exactly the dual graph distance from \(f\) to the exterior: a \(\mathbb Z_2\)-valued edge set with dual boundary \(f+\infty\) must contain a path joining those two odd-degree dual vertices, and a shortest path attains it. Therefore, unlike boundary private-edge faces, interior faces generally require a length-growing discrete center-flux string. Its *discrete* symmetry does not furnish the continuous Haar integration used in the previous private-edge variational trial.

## 3. CF-2 — Exact nonnegative face trace and concave coupling response

Set \(\mathcal E_f(t)=E_0(H_f^- - t p_f)\). Unitarly conjugating by \(T_f\) gives \(\mathcal E_f(t)=\mathcal E_f(-t)\). It is concave as the infimum of affine forms, and at fixed finite volume analytic in real \(t\) near zero by simple-ground-state perturbation theory. The Hellmann–Feynman formula and Kato second derivative yield

\[
\mathcal E_f'(t)=-\langle p_f\rangle_t,\qquad
\mathcal E_f''(t)=-2\langle Q_t p_f\Omega_t,(H_f^- -t p_f-\mathcal E_f(t))^{-1}_{Q_t}Q_t p_f\Omega_t\rangle<0.\tag{CF-3}
\]

Strict negativity holds because the ground state is strictly positive on the compact connected link configuration space and \(p_f\) is not an almost-everywhere constant. Since \(\mathcal E_f\) is even and strictly concave,

\[
\boxed{\langle p_f\rangle_{H_f^- -bp_f}>0\quad (b>0),\qquad
\partial_b\langle p_f\rangle_b>0.}\tag{CF-4}
\]

The physical Hamiltonian \(H_f^-+b(1-p_f)\) differs only by the scalar \(b\). Therefore for **every** face, interior or boundary,

\[
\boxed{\Delta_f(b)=\int_0^b(1-\langle p_f\rangle_t)dt,\quad 0<\Delta_f(b)<b\ (b>0).}\tag{CF-5}
\]

This proves positivity of each single-face Wilson trace in the actual nonlinear vacuum at any positive magnetic coupling, with the other face couplings held fixed. This is a one-point sign/screening theorem, **not** the desired \(O(\sqrt{A_fb})\) bound.

At the deleted point, with \(v_f=\langle p_f^2\rangle_-\in(0,1)\) and \(g_f=\langle p_f\Omega_f^-,K_f^-p_f\Omega_f^-\rangle\), the exact group Casimir and ground-state transform give

\[
\boxed{g_f=\frac{A_f}{4}(1-v_f).}\tag{CF-6}
\]

The center-odd spectral susceptibility obeys, by Cauchy–Schwarz,

\[
\boxed{\chi_f=-\mathcal E_f''(0)=2\langle p_f\Omega_f^-,(K_f^-)^{-1}p_f\Omega_f^-\rangle\ge\frac{2v_f^2}{g_f}=\frac{8v_f^2}{A_f(1-v_f)}.}\tag{CF-7}
\]

The expansion \(\Delta_f(b)=b-\chi_f b^2/2+O_f(b^4)\) is valid near \(b=0\) for each *fixed* finite graph, by center parity. The remainder constant need not be uniform in face count.

## 4. CF-3 — Exact two-state physical variational bound for every bulk face

The two gauge-invariant states \(\Omega_f^-\) and \(p_f\Omega_f^-/\sqrt{v_f}\) are orthonormal (opposite center parity). In this trial subspace, \(H_f^-+b(1-p_f)-E_f^-\) has the **exact** Ritz matrix

\[
\begin{pmatrix}b&-b\sqrt{v_f}\\-b\sqrt{v_f}&b+g_f/v_f\end{pmatrix}.
\]

The lower eigenvalue is an upper bound on \(\Delta_f(b)\):

\[
\boxed{\Delta_f(b)\le b+\frac12\left[\frac{g_f}{v_f}-\sqrt{\left(\frac{g_f}{v_f}\right)^2+4b^2v_f}\right]<b.}\tag{CF-8}
\]

Equivalently \(b-\Delta_f(b)\ge\frac12\left[\sqrt{(g_f/v_f)^2+4b^2v_f}-g_f/v_f\right]\). For large \(b\) at fixed \(v_f\), the two-state estimate is generally only \(O(b)\); higher-face-holonomy representations and an independently justified deleted-face marginal estimate would be needed for the desired \(O(\sqrt{A_fb})\). There is no assumption that \(v_f\) stays bounded away from zero uniformly in refinement.

**Exact one-plaquette reference:** with four equal electric coefficients \(a\) and no other magnetic plaquettes, \(\Omega^-\equiv1\), \(v=1/4\), \(g=3a/4\). CF-8 becomes

\[
\Delta_f(b)\le b+\frac12\left[3a-\sqrt{9a^2+b^2}\right].\tag{CF-9}
\]

This is precisely the two-character Ritz bound inside the interacting SU(2) physical character-basis Hamiltonian. It is weaker than the optimized nonlinear private-edge bound at large \(b\), illustrating why center parity alone does not solve the bulk deletion problem.

## 5. CF-4 — Uniform *bulk* deletion increment for the exact shared-edge **Gaussian tangent** Hamiltonian

For any positive definite face-edge kinetic matrix \(M=B\operatorname{diag}(a_e)B^\top\), let

\[
H_G(\boldsymbol b)=-\sum_{fg}M_{fg}\nabla_f\cdot\nabla_g+\frac18\sum_fb_f|y_f|^2
\]

on \(L^2(\mathbb R^{3F})\), restricted if desired to simultaneous rotation-invariants. Write \(V=\operatorname{diag}(b_f)/8\). Its **ground-energy infimum** is

\[
E_G(\boldsymbol b)=3\operatorname{Tr}\sqrt{M^{1/2}VM^{1/2}}.\tag{CF-10}
\]

This continues by continuity when one coefficient is zero; then a free mode means the infimum need not be attained by a normalized vector. Delete \(b_f\) and set \(V^-=V-b_f e_fe_f^\top/8\). Then

\[
X=M^{1/2}V^-M^{1/2}\ge0,\qquad Y=(b_f/8)(M^{1/2}e_f)(M^{1/2}e_f)^\top\ge0,
\]

where \(Y\) is rank one with sole nonzero eigenvalue \((b_f/8)M_{ff}\). The nuclear-norm triangle inequality, using positive square roots (equivalently Rotfel'd's trace concavity inequality), proves \(\operatorname{Tr}\sqrt{X+Y}\le\operatorname{Tr}\sqrt X+\operatorname{Tr}\sqrt Y\). Thus

\[
\boxed{0\le E_G(\boldsymbol b)-E_G(\boldsymbol b-b_fe_f)\le\frac{3}{2\sqrt2}\sqrt{b_fM_{ff}}=\frac{3}{2\sqrt2}\sqrt{b_fA_f}.}\tag{CF-11}
\]

This is a **face-count-independent bulk-face bound**, valid for signed geometric incidence, unequal electric coefficients and arbitrary background magnetic coefficients, *within the exact Gaussian tangent model*. It is precisely the needed scale \(O(h^{-1})\) at \(b_f\asymp h^{-2}\), including faces without private edges. It is **not** known for the genuine nonlinear SU(2) vacuum; its proof relies on the globally quadratic Hamiltonian and hence does not supply a missing nonlinear-vacuum remainder estimate.

## 6. Integrity and next obligation

**Newly proved for the true nonlinear SU(2) system:** arbitrary-bulk-face center-flux parity and conditional symmetry; exact strictly positive one-point Wilson trace and susceptibility identities; an explicit two-state physical deletion-energy inequality. **Newly proved for the exact Gaussian tangent:** a sharp-scale magnetic deletion bound uniformly over growing face count, including deep interior faces.

**Not proved:** transfer CF-11 to the nonlinear vacuum, a uniform lower control of the deleted-face holonomy distribution, the \(\Delta_f=o(h^{-5/4})\) bulk gate, the fixed-support extreme-event bound, nonlinear Gaussian/source comparison, regulator-uniform physical mass gap, quartic resolvent, continuum reconstruction or Stage7/26 source action identity. Discrete center symmetry is not a continuous private-edge Haar-averaging mechanism.

**Suggested next specific theorem:** derive a **nonlinear face-deletion energy bound using a local, gauge-invariant coupling comparison**, possibly via a quantitative comparison of the genuine deleted-face conditional distribution with the exact Gaussian rank-one response. Any approximation must control the simultaneous limit \(F_h\asymp h^{-2}\), \(b_f\asymp h^{-2}\); fixed-F semiclassical convergence is not uniform by itself.

## 7. Reproducibility

The companion deterministic script builds oriented incidence for a three-face Penrose spatial seed and a square grid with a true four-shared-edge interior face, solves the center-twist parity equation over \(\mathbb F_2\), checks minimal dual path length, verifies the exact Ritz and susceptibility coefficients, the Gaussian trace square-root rank-one bound with nonuniform weights, and finite interacting one-face character-basis ground energies. It makes no Monte Carlo calls or historical-data modifications.
