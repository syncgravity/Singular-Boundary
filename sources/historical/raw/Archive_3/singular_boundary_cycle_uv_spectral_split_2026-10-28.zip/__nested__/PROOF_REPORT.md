# The Singular Boundary — Spectral ultraviolet truncation of nonlinear magnetic cycle-closing susceptibility

**Date:** 2026-10-28. **Branch:** `audit/2026-10-28-independent-reconstruction`. **Evidence classification:** finite true interacting SU(2) Wilson ground-state spectral inequality, with a conditional Penrose-refinement corollary. The theorem does not establish the physical mass gap, the sign of nonlinear mixed magnetic susceptibility, the required low-energy bound, fixed-support covariance, or Stage 7/26 source-level identity. The Gaussian comparison of the previous report is not used. No Monte Carlo.

## 1. Finite physical Hamiltonian and coupling rectangle

Let G be a finite face-complete planar rhombus disk. Each face meets four distinct edges; each edge meets at most two faces. Every vertex gauge transformation is imposed. The finite Wilson Hamiltonian is

\[
 H(u,t)=\sum_e a_e(-\Delta_e)+V_0+t d_f+u W,\quad
 0\le t\le b_f,\quad 0\le u\le1,
\]

where \(a_e>0\), \(d_g=1-\frac12\operatorname{ReTr}W_g\), and \(W=\sum_{g\in\mathcal B} c_g d_g\), \(c_g>0\), contains cycle-closing magnetic interactions. The bridge model corresponds to \(u=0\); full restoration to \(u=1\). All other magnetic terms, included in \(V_0\), remain nonnegative. Let \(\Omega_{u,t}>0\) be its normalized physical ground state, \(E(u,t)\) its ground energy, \(K=H-E\), \(Q=1-|\Omega\rangle\langle\Omega|\), and \(P_{(0,\Lambda]}\), \(P_{(\Lambda,\infty)}\) the **physical-sector** spectral projections of \(K\).

The exact Kato identity is

\[
 E_{ut}=-2\operatorname{Re}\langle Qd_f\Omega,K^{-1}QW\Omega\rangle.
\]

The inverse is restricted to the orthogonal complement of the unique physical ground state, which is finite-dimensional in the spectral sense at every fixed finite graph (compact resolvent); no uniform spectral gap is assumed.

## 2. Theorem US-1 — Local f-sums and a high-energy mixed-resolvent bound

For a real gauge-invariant multiplication source \(A\), the **exact interacting vacuum** ground-state transform gives

\[
 m_1(A)=\langle A\Omega,K A\Omega\rangle
       =\mathbb E_{\Omega^2}\Gamma(A),\qquad
 \Gamma(A)=\sum_e a_e|\nabla_e A|^2.
\]

For the SU(2) fundamental trace, on any incident edge \(|\nabla_e d_g|^2=(1-p_g^2)/4\le1/4\). Hence, writing \(A_g=\sum_{e\in\partial g}a_e\),

\[
 m_1(d_f)\le A_f/4.
\]

At most two selected faces meet each edge. The elementary pointwise \(|x+y|^2\le2(|x|^2+|y|^2)\) therefore gives

\[
 \Gamma(W)\le\tfrac12\sum_{g\in\mathcal B}c_g^2A_g,
 \quad m_1(W)\le\tfrac12\sum_{g\in\mathcal B}c_g^2A_g.
\]

For every \(\Lambda>0\), every \(u,t\), and any two gauge-invariant real multipliers \(A,B\), spectral Cauchy–Schwarz gives

\[
 \begin{split}
 \left|\langle QA\Omega,K^{-1}P_{>\Lambda}QB\Omega\rangle\right|
 &\le \|K^{-1/2}P_{>\Lambda} QA\Omega\|
       \|K^{-1/2}P_{>\Lambda} QB\Omega\|\\
 &\le\Lambda^{-2}\sqrt{m_1(A)m_1(B)}.
 \end{split}
\]

This is sharp for common spectral weight at a single energy just above \(\Lambda\). Therefore **the high-energy part of the mixed response** obeys

\[
 \boxed{\left|E_{ut}^{>\Lambda}\right|
 \le {\sqrt{A_f\sum_{g\in\mathcal B}c_g^2A_g}\over\sqrt2\,\Lambda^2}.}
\tag{US-1}
\]

Crucially, the constants depend only on explicit local electric coefficients, cycle-closing magnetic weights, and the cutoff, **not** on the unknown ground-state score, mixed covariance, physical gap, or full ambient face count except through \(\mathcal B\).

## 3. Theorem US-2 — Exact adverse-sign low-energy decomposition

Let \(\Delta_f(u)=E(u,b_f)-E(u,0)\). Define the *low-energy adverse mixed-response budget*

\[
 \mathcal N_{\le\Lambda}(f)
 =2\int_0^1\!du\int_0^{b_f}\!dt\,
 \big[-\operatorname{Re}\langle Qd_f\Omega,
 K^{-1}P_{(0,\Lambda]}QW\Omega\rangle\big]_+.
\]

Since \(E_{ut}=-2(\chi_{\le\Lambda}+\chi_{>\Lambda})\), and \([-x-y]_+\le[-x]_++|y|\), the exact coupling rectangle and US-1 imply

\[
 \boxed{\Delta_f(1)\le\Delta_f(0)+\mathcal N_{\le\Lambda}(f)
 +{b_f\over\sqrt2\Lambda^2}
    \sqrt{A_f\sum_{g\in\mathcal B}c_g^2 A_g}.}
\tag{US-2}
\]

This holds **at every magnetic coupling** for the true finite nonlinear SU(2) ground state. For a dual-bridge reference, the earlier independent nonlinear variational theorem supplies

\[
 \Delta_f(0)\le {3\over2\sqrt2}\sqrt{A_f b_f}.
\]

There is no assumption that the low-energy integrand is nonnegative or that the physical spectrum has a positive uniform gap.

## 4. Theorem US-3 — Penrose-refinement cutoff chosen to absorb all ultraviolet cycle cost

Assume \(A_g\le4a_*\) and \(0<c_g,b_f\le\beta_+h^{-2}\), with \(m_h=|\mathcal B|\ge1\). Then US-2 becomes

\[
 \Delta_f(1)\le{3\over2\sqrt2}\sqrt{4a_*\beta_+}\,h^{-1}
 +\mathcal N_{\le\Lambda}(f)
 +{2\sqrt2 a_*\beta_+^2\sqrt{m_h}\over h^4\Lambda^2}.
\]

Choose \(\Lambda_h=L h^{-3/2}m_h^{1/4}\), with fixed \(L>0\). Thus **irrespective of the size of the cycle-closing set**,

\[
 \boxed{\Delta_f(1)\le C_Lh^{-1}+\mathcal N_{\le\Lambda_h}(f),}
 \qquad C_L={3\sqrt{2a_*\beta_+}\over2}+{2\sqrt2 a_*\beta_+^2\over L^2}.
\tag{US-3}
\]

For \(m_h=O(1)\), \(\Lambda_h=O(h^{-3/2})\). For an entire fixed-area Penrose patch \(m_h=O(h^{-2})\), \(\Lambda_h=O(h^{-2})\), and the ultraviolet cost **still** has the desired \(O(h^{-1})\) scale. Equivalently, any candidate counterexample with excess deletion energy much larger than \(h^{-1}\) must have an adverse mixed physical response inside this finite energy window. US-3 does not prove that response is small.

If one derives independently \(\mathcal N_{\le\Lambda_h}(f)=O(h^{-1}\operatorname{polylog}(1/h))\), then the nonlinear bulk deletion bound follows, and the previously proved single-face exponential Laplace estimate yields the full-area extreme-defect rarity. This is a **conditional** research target, not a consequence of US-3.

## 5. Theorem US-4 — Exactly vanishing mixed first spectral moment at separated cycle closures

If every face in \(\mathcal B\) is edge-disjoint from \(f\), then \(\nabla_e d_f\) and \(\nabla_e W\) cannot be nonzero on the same edge. Pointwise \(\Gamma(d_f,W)=0\), and the exact nonlinear ground-state Ward identity yields

\[
 \boxed{\langle Qd_f\Omega,KQW\Omega\rangle=0.}
\tag{US-4}
\]

This is **not** a vanishing equal-time covariance or inverse-energy susceptibility. It identifies a particularly useful choice of cycle-breaking magnetic interactions: cutting cycles away from the target face makes the first cross spectral moment exactly zero, so any mixed cycle cost arises from correlated propagation in the full interacting vacuum rather than a direct one-link Dirichlet term. Whether the required geometrical bridge can always be achieved with a remote cut of controlled cardinality is a separate graph problem.

## 6. Deterministic proof checks and scope

The companion Python verifier reconstructs the genuine three-rhombus ten-edge Penrose spatial seed and checks a pair of non-adjacent faces. It exactly verifies the \(1/4,1/2,1/\sqrt2\) SU(2) coefficients, the adaptive-cutoff cancellation, and the sharp spectral Cauchy inequality in a range of finite character-basis, genuinely interacting SU(2) one-face physical Hamiltonians, plus a center-symmetric two-level mixed-coupling fixture. These fixtures validate the algebra and numerical bounds, **not** the unknown low-energy response in a refining Penrose vacuum. No Monte Carlo or historical archive modification.

**Proved:** US-1, US-2, US-3, US-4 at finite interacting SU(2) regulators under stated assumptions. **Open:** uniform bound on \(\mathcal N_{\le\Lambda_h}(f)\) for the cycle-rich Penrose interior; full nonlinear magnetic-deletion bound; fixed-area extreme-defect probability; physically nontrivial continuum source; positive uniform physical mass gap; quartic resolvent; complete continuum construction; Stage7/26 provenance.
