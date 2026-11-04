# The Singular Boundary — All-width radius-loss fusion estimate
Research audit, 2026-11-03. **Conditional finite-strip estimate; NOT fixed-radius nonlinear closure, an interacting gap, or a continuum proof.** The complete expanded report and verifier are archived in the conversation.

## Assumptions
Let E be the original links of a finite, open, simply connected straight square strip and work with Gauss-invariant functions on SU(2)^E. Define

\[
K=-\sum_{e\in E}a_e\sum_{j=1}^3 X_{ej}^2,\qquad 0<a_0\le a_e\le a_*,
\qquad \Gamma_K(f,g)=\sum_{e,j}a_e(X_{ej}f)(X_{ej}g).
\]

Normalize generators so the irreducible label n has Casimir n(n+2)/4 and \(\|d\pi_n(X_{ej})\|_{\mathrm{op}}\le n/2\). Assume the physical Gauss-invariant free-electric gap \(\ge3a_0\), valid on these original-link open square strips; do not import this assumption to arbitrary geometries/boundaries. Q deletes constants and \(\mathcal B=K^{-1}Q\Gamma_K\).

For the original-link Peter–Weyl expansion \(f=\sum_{\mathbf n}\operatorname{Tr}(A_{\mathbf n}\pi_{\mathbf n})\), define \(d_{\mathbf n}=\prod_e(n_e+1)\), \(|\mathbf n|=\sum_e n_e\), and

\[
\|f\|_{P_\sigma}=\sum_{\mathbf n}d_{\mathbf n}e^{\sigma|\mathbf n|}\|A_{\mathbf n}\|_{S_1}.
\]

For history-labelled polynomials \(F=\sum_I[I]\otimes f_I\), where I is a connected face interval and \(f_I\) uses only links incident on I, let

\[
\|F\|_{\kappa,\sigma}=\sum_Ie^{\kappa|I|}\|f_I\|_{P_\sigma}.
\]

Define \(\mathcal B_{\mathrm{hist}}\) by applying \(\mathcal B\) to each pair of coefficient functions with shared original links and labelling the output by the connected union of their histories, without removing any physical output channel.

## Proposition: uniform in strip length, support width and spin, WITH radius loss
For \(\kappa>0,\sigma>\sigma'\ge0,\delta=\sigma-\sigma'>0\),

\[
\boxed{
\|\mathcal B_{\mathrm{hist}}(F,G)\|_{\kappa,\sigma'}
\le
\frac{a_*}{4a_0e^2\delta^2}
\left(1+\frac{3}{e\kappa}\right)
\|F\|_{\kappa,\sigma}\|G\|_{\kappa,\sigma}.
}
\]

### Argument
1. SU(2) Clebsch–Gordan outputs satisfy \(l\le n+m\) and \(d_l\le d_nd_m\). Tensor-product decomposition followed by trace-class pinching gives a coefficient \(\ell^1\) nuclear estimate, so \(\|\cdot\|_{P_\tau}\) is submultiplicative for every \(\tau\ge0\), uniformly over finite original-link products.
2. On each input representation, \(\|d\pi_{n_e}(X_{ej})\|\le n_e/2\), and \(n_e e^{-\delta|\mathbf n|}\le1/(e\delta)\). Consequently
\[
\|\Gamma_K(f,g)\|_{P_{\sigma'}}
\le \frac{3a_*}{4e^2\delta^2}|E(f)\cap E(g)|
\|f\|_{P_\sigma}\|g\|_{P_\sigma}.
\]
3. Original-link K is diagonal in the spin labels, with nonzero gauge-invariant eigenvalues at least \(3a_0\). Thus \(\|K^{-1}Qh\|_{P_{\sigma'}}\le(3a_0)^{-1}\|h\|_{P_{\sigma'}}\).
4. If I,J are connected face intervals whose link sets meet, let \(t=|I\cap J|\) and \(T=I\cup J\). Then \(|E(I)\cap E(J)|\le3t+1\) (touching intervals allow t=0), and
\[
\frac{e^{\kappa|T|}}{e^{\kappa|I|}e^{\kappa|J|}}=e^{-\kappa t},
\qquad (3t+1)e^{-\kappa t}\le1+\frac{3}{e\kappa}.
\]
Sum over all labelled history pairs. The bound follows.

## Scope and limitations
The estimate maps a **stronger spin-analytic radius** to a weaker one. It does not establish same-radius boundedness as \(\delta\to0\). Repeated radius loss at every nonlinear tree vertex can exhaust a finite analyticity budget, so this result by itself proves neither all-orders convergence of the physical vacuum score nor an interacting Hamiltonian spectral gap.

It also does not prove a 3D bulk infinite-volume gap, the Penrose interacting signed-current bound, a physical continuum mass gap, or nontrivial axiomatic quantum Yang–Mills theory on R^4. The Clay problem requires both existence and mass gap (and calls for any compact simple gauge group). The OpenAI October 2026 announcement concerned a claimed existence result, not a mass-gap result.

## Next obligation
Prove a fixed-radius tame or renormalized convergent history-aware connected-score theorem (while retaining all fusion channels). Then transfer it to a uniform interacting gap, extend beyond the straight strip to 3D spatial lattices, and track the physical gap through infinite-volume and continuum limits.

Exact finite verification in the separately archived executable checks face-link overlap identities, SU(2) representation dimension inequalities and the scalar support-weight bound. Such checks do not replace the mathematical proof.