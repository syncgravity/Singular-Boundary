# Two overlapping extended Wilson histories: exact four-independent-spin SU(2) family bound

**2026-11-04. Status:** all-degree **restricted character-family** theorem on the corrected finite open three-face original-link, Gauss-invariant SU(2) system. NOT unrestricted local-first bilinear closure, convergence, interacting spectral gap, 3D regulator transport, or 4D continuum Yang–Mills mass gap. Detailed full-length report, exact quaternion/Fourier verifiers and SHA-256 manifest: accompanying conversation archive \`two_extended_histories_audit_2026-11-04.zip\`.

## Physical source and retained history

Use face holonomies A,B,C and the original-link electric generator
\[
K=4(C_A+C_B+C_C)+2D_{12}+2D_{23},\
D_{12}=\sum_aR_A^aL_B^a,\quad D_{23}=\sum_aR_B^aL_C^a.
\]
Take independent positive integer SU(2) degrees p,q,r,s (spin j/2 for degree j). Our **two extended** input histories are
\[
F_{p,q}=\chi_p(A)\chi_q(B)\ [I=[1,2]],\qquad
G_{r,s}=\chi_r(B)\chi_s(C)\ [J=[2,3]].
\]
Their union history is [1,3], face-overlap is one, and the exact spatial history-weight ratio is e^{-κ}. Let \(\mathcal J=\{|q-r|,|q-r|+2,\ldots,q+r\}\), \(W_\ell=\chi_p(A)\chi_\ell(B)\chi_s(C)\), \(Q=q(q+2)\), \(R=r(r+2)\), \(L_\ell=\ell(\ell+2)\). Define
\[
\alpha_\ell=(Q+R-L_\ell)/2,\quad
t_\ell=(L_\ell+R-Q)/(2L_\ell),\quad
u_\ell=(L_\ell+Q-R)/(2L_\ell)\quad(\ell>0),
\]
and t_0=u_0=0. The **complete** original-link carré-du-champ source is
\[
\boxed{\Gamma_K(F_{p,q},G_{r,s})=\sum_{\ell\in\mathcal J}
 [\alpha_\ell W_\ell-t_\ell D_{12}W_\ell-u_\ell D_{23}W_\ell].}\tag{1}
\]
The cross-link coefficients t and u are different: the first term differentiates \(\chi_q\chi_r'\) and the second \(\chi_q'\chi_r\). Derivation: SU(2) character fusion, radial one-face polarization, and Haar integration by parts. Independent exact *original-link quaternion* differentiation checks the identity including both physical shared-link terms. When q=r, the middle-spin-zero output \(Q\chi_p(A)\chi_s(C)\) is nonconstant, Gauss-invariant and of disconnected minimal link support; it is **retained**, not removed by Q (Haar centering).

## Actual trace-class Fourier inverse

In the output PW sector (p,ℓ,s), set \(P=p(p+2)\), \(T=s(s+2)\), \(b=P+L_\ell+T\), \(d=(p+1)(\ell+1)(s+1)\). The trace-expansion coefficient matrix \(M_\ell\) obeys
\[
(b\,\mathrm{id}+2\mathscr D_{12}+2\mathscr D_{23})M_\ell
 =\alpha_\ell I_d-t_\ell\mathscr D_{12}I_d-u_\ell\mathscr D_{23}I_d.
\]
The *correct* Fourier shared-link superoperators are \(\mathscr D_{12}(X)=-\sum_aJ_p^a X J_\ell^a\), \(\mathscr D_{23}(X)=-\sum_aJ_\ell^a X J_s^a\), tensor factors implicit. They commute as superoperators, not necessarily as ordinary matrices applied to I. For \(S_{12}=\sqrt{PL_\ell}/4\), \(S_{23}=\sqrt{TL_\ell}/4\), \(S=S_{12}+S_{23}\), Schatten row-column Cauchy gives operator trace-norm bounds S12 and S23. AM–GM yields \(S\le b/4\); the physical Neumann inverse therefore converges in trace norm:
\[
\boxed{\|M_\ell\|_1\le dX_\ell,\quad
X_\ell=\frac{|\alpha_\ell|+|t_\ell|S_{12}+|u_\ell|S_{23}}{b-2S}.}\tag{2}
\]
No previously inherited **general** coefficientwise PW tame estimate is used.

## All-spin first-moment bound for **two extended histories**

Define the local-first first-moment L^(1) norms at κ>0, σ≥0:
\[
\|F\|_{L^{(1)}}=[(p+1)(q+1)]^2[1+\max(p,q)]e^{2\kappa+\sigma(p+q)},
\]
\[
\|G\|_{L^{(1)}}=[(r+1)(s+1)]^2[1+\max(r,s)]e^{2\kappa+\sigma(r+s)}.
\]
The normalized response \(R_{pqrs}=\|\mathcal B_{\mathrm{hist}}(F,G)\|_{L^{(1)}}/[\|F\|_{L^{(1)}}\|G\|_{L^{(1)}}]\) obeys
\[
R_{pqrs}\le e^{-\kappa}\sum_{\ell\in\mathcal J}
 \frac{(\ell+1)^2}{(q+1)^2(r+1)^2}
 \frac{1+\max(p,\ell,s)}{[1+\max(p,q)][1+\max(r,s)]}
 e^{\sigma(\ell-q-r)}X_\ell.\tag{3}
\]
**Theorem.** For all independent p,q,r,s≥1, κ>0, σ≥0:
\[
\boxed{R_{pqrs}\le\frac{24e^{-\kappa}}{[1+\min(q,r)]^2}\le24e^{-\kappa}.}\tag{4}
\]
**Analytic proof for all degrees:** Put \(N=q+r+2\). For each permitted ℓ, \(\ell+1\le N\), \(|R-Q|=|r-q|N\le\ell N\), \(|\alpha_\ell|\le N^2\), and \(|t_\ell|\sqrt{L_\ell},|u_\ell|\sqrt{L_\ell}\le N\) (zero-spin derivatives vanish). Since \(b\ge L_\ell+6\ge(\ell+1)^2\), \(b-2S\ge b/2\), and \((\sqrt P+\sqrt T)/b\le\sqrt{2/b}\),
\[
X_\ell\le\left(2+\frac1{\sqrt2}\right)\frac{N^2}{(\ell+1)^2}
 <\frac{3N^2}{(\ell+1)^2}.\tag{5}
\]
Set \(a=q+1,b_*=r+1,A=1+\max(p,q)\ge a,B=1+\max(r,s)\ge b_*\). As ℓ≤q+r, \([1+\max(p,\ell,s)]/(AB)\le1/A+1/B\le1/a+1/b_*\). There are \(\min(a,b_*)\) output channels, and every exponential factor is ≤1. Thus
\[
R_{pqrs}\le3e^{-\kappa}\frac{\min(a,b_*)(a+b_*)^3}{a^3b_*^3}
\le\frac{24e^{-\kappa}}{\min(a,b_*)^2},
\]
where the final step assumes a≤b_* (or symmetrically reverses them) and uses \(a+b_*\le2\max(a,b_*)\). QED.

This establishes a same-grade \(L^{(1)}\times L^{(1)}\to L^{(1)}\) *inequality only for the specified two extended character histories*. A general bilinear map would need control of arbitrary spin-network intertwiners, linear combinations and multiple overlapping histories.

## Verification and corrections

- 49 exact SU(2) character fusion, radial Gamma and **both** distinct differentiated-product identities.
- 5 direct original-link quaternion source equalities on nontrivial (p,q,r,s).
- 36 physical Fourier superoperator inverse/Schatten checks on 16 full quadruples.
- 20,736 scalar all-family ratio and per-channel checks through degree 12.
- A first numerical script had mistakenly multiplied output by an extra dimension d; this was corrected **before accepting any ratios**. The final output uses \(d(1+\max)\|M_\ell\|_1\). The corrected verifier and exact hash are in the conversation ZIP.

The analytic inequality (4), not the finite test count, supports the all-degree theorem. P0 original-source chain custody, the 3D regulator, interacting spectrum and continuum physical gap remain open. **Next:** non-character (traceless/off-diagonal) PW coefficient matrices, arbitrary recoupled intertwiners and long-history overlap; investigate whether a fixed first-moment bound survives those genuinely less structured inputs.