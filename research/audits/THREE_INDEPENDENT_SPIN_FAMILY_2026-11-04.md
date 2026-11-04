# Three independently variable SU(2) spins: exact nested original-link Wilson-family bound

**Date:** 2026-11-04. **Scope:** finite open three-face Gauss-invariant original-link SU(2) strip, single extended character history and singleton second input. **Not** unrestricted nonlinear closure, interacting lattice gap, or 4D continuum mass gap. The full equation-level report, original-link quaternion checker, physical Fourier superoperator checker, passing logs, and SHA-256 manifest are supplied in the accompanying conversation archive \`three_independent_spin_audit_2026-11-04.zip\`.

## Model and exact character fusion

Take \(K=4(C_A+C_B+C_C)+2(D_{12}+D_{23})\), with \(D_{12}=\sum_aR_A^aL_B^a\), \(D_{23}=\sum_aR_B^aL_C^a\), where degree \(j\) represents SU(2) spin \(j/2\). For independent \(p,q,r\ge1\), let \(F_{p,q}=\chi_p(A)\chi_q(B)\chi_1(C)\) and \(G_r=\chi_r(B)\). The retained histories are \([1,3]\) and \([2]\); the output keeps history \([1,3]\).

Write \(Q=q(q+2)\), \(R=r(r+2)\), \(L_\ell=\ell(\ell+2)\), \(W_\ell=\chi_p(A)\chi_\ell(B)\chi_1(C)\), and \(\mathcal J=\{|q-r|,|q-r|+2,\ldots,q+r\}\). Set \(\alpha_\ell=(Q+R-L_\ell)/2\), \(t_\ell=(L_\ell+R-Q)/(2L_\ell)\) for \(\ell>0\), and \(t_0=0\). The **complete physical source identity** is
\[
\boxed{\Gamma_K(F_{p,q},G_r)=\sum_{\ell\in\mathcal J}
 [\alpha_\ell W_\ell-t_\ell(D_{12}+D_{23})W_\ell].}\tag{1}
\]
Proof: SU(2) fusion gives \(U_qU_r=\sum_{\ell\in\mathcal J}U_\ell\), and the radial Casimir polarization gives \((1-x^2)U_q'U_r'=\sum\alpha_\ell U_\ell\). Project \(U_qU_r'\) against \(U_\ell'\) with weight \((1-x^2)w(x)\), \(w(x)\propto\sqrt{1-x^2}\): by integration by parts its coefficient is \((R-\alpha_\ell)/L_\ell=t_\ell\). At \(\ell=0\) the derivative vanishes. The original-link cross-derivative supplies the minus sign. If \(q=r\), the zero-spin middle output is \(Q\chi_p(A)\chi_1(C)\), a *nonconstant physical* disconnected-minimal-support output retained at the original connected history.

## Direct Schatten-superoperator estimate

For fixed output \((p,\ell,1)\), let \(P=p(p+2)\), \(b_\ell=P+L_\ell+3\), \(d_\ell=2(p+1)(\ell+1)\), \(S_\ell=(\sqrt{PL_\ell}+\sqrt{3L_\ell})/4\). In **trace-expansion** Peter–Weyl coefficients, the matrix \(M_\ell\) satisfies
\[
(b_\ell\mathrm{id}+2\mathscr D_{12}+2\mathscr D_{23})M_\ell
 =\alpha_\ell I_{d_\ell}-t_\ell(\mathscr D_{12}+\mathscr D_{23})I_{d_\ell}.
\]
The actual operators act as \(\mathscr D_{12}(X)=-\sum_aJ_p^a X J_\ell^a\), \(\mathscr D_{23}(X)=-\sum_aJ_\ell^aXJ_1^a\) on their correct tensor factors. **The superoperators commute, not necessarily their ordinary matrix images**. Schatten row-column Cauchy yields \(\|\mathscr D_{12}X\|_1\le\sqrt{PL_\ell}\|X\|_1/4\) and \(\|\mathscr D_{23}X\|_1\le\sqrt{3L_\ell}\|X\|_1/4\). Since \(S_\ell\le b_\ell/4\), the full Neumann inverse is trace-norm convergent and
\[
\boxed{\|M_\ell\|_1\le d_\ell X_\ell,\quad
X_\ell=\frac{|\alpha_\ell|+|t_\ell|S_\ell}{b_\ell-2S_\ell}.}\tag{2}
\]
No inherited *general* coefficientwise tame theorem is invoked.

## Restricted first-moment family theorem

In the local-first \(L^{(1)}_{\kappa,\sigma}\) norm, for \(\kappa>0,\sigma\ge0\), the exact input norms are
\[
\|F_{p,q}\|_{L^{(1)}}=[2(p+1)(q+1)]^2[1+\max(p,q)]e^{3\kappa+\sigma(p+q+1)},
\quad \|G_r\|_{L^{(1)}}=(r+1)^3e^{\kappa+\sigma r}.
\]
The normalized nonlinear response \(R_{pqr}\) obeys, by (2),
\[
R_{pqr}\le\frac{e^{-\kappa}}{(r+1)^3}
\sum_{\ell\in\mathcal J}
 \left(\frac{\ell+1}{q+1}\right)^2
 \frac{1+\max(p,\ell)}{1+\max(p,q)}
 e^{\sigma(\ell-q-r)}X_\ell.\tag{3}
\]

**Theorem (all \(p,q,r\ge1\), specified character family only):**
\[
\boxed{R_{pqr}\le\frac{16e^{-\kappa}}{[1+\min(q,r)]^2}\le16e^{-\kappa}.}\tag{4}
\]
**Proof for all degrees.** By \(S_\ell\le b_\ell/4\), \(|R-Q|=|r-q|(q+r+2)\le\ell(q+r+2)\), and \(t_0=0\), uniformly
\[
X_\ell\le\frac{Q+R}{L_\ell+3}+\frac54+
\frac{q+r+2}{4(\ell+2)}.\tag{5}
\]
Also \((\ell+1)^2\le L_\ell+3\), \(\frac{1+\max(p,\ell)}{1+\max(p,q)}\le\max\{1,(\ell+1)/(q+1)\}\), and \(|\mathcal J|=1+\min(q,r)\). If \(q\ge r\), the moment ratio is at most 2 and the three terms in (5) *after multiplying by* \(((\ell+1)/(q+1))^2\) are at most \(2,5,1\). Each channel contributes at most 16 to (3), so \(R_{pqr}\le16e^{-\kappa}/(r+1)^2\). If \(r\ge q\), let \(t=(r+1)/(q+1)\ge1\). Moment ratio at most \(2t\); the three weighted terms are at most \(1+t^2,5t^2,t^2\), sum at most \(8t^2\). Each of \(q+1\) channels contributes at most \(16t^3\), hence \(R_{pqr}\le16e^{-\kappa}/(q+1)^2\). Combining proves (4).

This is **a first-moment same-grade estimate restricted to character-family input plus singleton character**, not general \(L^{(1)}\times L^{(1)}\to L^{(1)}\) continuity on all physical history families.

## Reproducibility and next gate

Companion archive verifiers passed: 100 symbolic CG/derivative/Gamma identities (\(q,r=1..10\)); 69 true physical Fourier superoperator inverse/Schatten checks covering 27 three-spin triples (\(p,q,r=1..3\)); 8,000 independent scalar bound cases; five exact original-link quaternion source identities including \((p,q,r)=(2,2,3)\). The repository lightweight regression checks character identities and the scalar estimate. These tests are not substitutes for the all-degree proof above.

**Next objective:** two *extended overlapping multi-face inputs* with independently variable spins and full history reconstruction, where earlier counterexamples may impose a moment loss. No proof of an interacting physical gap, source-certified Penrose regulator, or 4D continuum theory is claimed.