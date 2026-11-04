# Exact three-face nested SU(2) Wilson family: two shared links, all middle-spin degrees

**2026-11-04 · finite physical original-link open straight three-face strip · family theorem.**
This result is **not** the unrestricted local-first tame theorem, interacting vacuum convergence, a regulator-uniform spectral theorem, or a Yang–Mills mass-gap proof. It uses the same trace-expansion matrix Peter–Weyl norm convention as the repository's preceding two-face nested-family audit. The complete executable quaternion and Fourier checks and their SHA-256 manifest are in the associated conversation research package.

## Physical model and source

Use face holonomies \(A,B,C\in SU(2)\) in the Gauss-invariant original-link finite open straight strip, with generators \(i\sigma_a/2\) and
\[
K=4(C_A+C_B+C_C)+2D_{12}+2D_{23},\qquad
D_{12}=\sum_a R_{A,a}L_{B,a},\quad D_{23}=\sum_a R_{B,a}L_{C,a}.
\]
The two **differential operators** commute because their actions on middle face \(B\) are respectively left and right invariant. Their ordinary Fourier coefficient matrices need **not** commute.

For any integer \(n\ge1\) take the genuinely nested physical inputs
\[
F_n=\chi_1(A)\chi_n(B)\chi_1(C),\quad G=\chi_1(B).
\]
Assign history [1,3] to \(F_n\), history [2] to \(G\), retaining [1,3] on output. Define \(W_l=\chi_1(A)\chi_l(B)\chi_1(C)\).
The SU(2) character identities and original-link carré du champ give exactly
\[
\Gamma_K(F_n,G)=-n W_{n+1}+(n+2)W_{n-1}
-\frac{(D_{12}+D_{23})(W_{n+1}-W_{n-1})}{n+1}.
\tag{1}
\]
Both output blocks have nontrivial outer face labels, so Haar centering \(Q\) does nothing. There are **only** two middle-spin degrees \(l=n\pm1\). The lower \(n=1\) channel is \(3W_0/6=\tfrac12\chi_1(A)\chi_1(C)\): a genuine disconnected-minimal-support *physical* mode, not a Haar constant. It must remain in the original connected history.

On any fixed degree triple \((1,l,1)\), \(l\ge1\), put \(b_l=l(l+2)+6\). Each shared-link differential operator satisfies
\[
D_{12}^2=-\tfrac12D_{12}+\tfrac{l(l+2)}{16}I,\qquad
D_{23}^2=-\tfrac12D_{23}+\tfrac{l(l+2)}{16}I.
\]
The response \(K^{-1}Q\Gamma\) is thus an exact linear combination of
\[
W_l,\quad D_{12}W_l,\quad D_{23}W_l,\quad D_{12}D_{23}W_l.
\tag{2}
\]
The coefficient vector is obtained by polynomial inversion of
\(b_l+2(D_{12}+D_{23})\) against
\(\alpha_l+\beta_l(D_{12}+D_{23})\), where
\[
(\alpha_{n+1},\beta_{n+1})=(-n,-1/(n+1)),\quad
(\alpha_{n-1},\beta_{n-1})=(n+2,+1/(n+1)).
\]
At \(n=1,l=2\), the exact upper response is
\[
-\tfrac7{104}W_2-\tfrac3{104}(D_{12}+D_{23})W_2+\tfrac1{104}D_{12}D_{23}W_2.
\]
At \(n=2,l=3\), it is
\[
-\tfrac{577}{6144}W_3-\tfrac{19}{2560}(D_{12}+D_{23})W_3+\tfrac1{640}D_{12}D_{23}W_3.
\]
Independent quaternion differentiation modulo all three SU(2) sphere relations verifies **the exact original-link equation** \(K\mathcal B(F_n,G)=\Gamma_K(F_n,G)\) at \(n=1,2\).

## Direct coefficientwise trace-class theorem

For the trace-expansion Peter–Weyl coefficient matrix \(M_l\) at degree \((1,l,1)\), the character \(W_l\) has identity coefficient of dimension \(d_l=4(l+1)\); the projective Fourier norm is \(d_l e^{\sigma(l+2)}\|M_l\|_1\), with *no silent change to Haar-normalized Fourier coefficients*.

For Hermitian angular momentum matrices \(J_A,J_B,J_C\), the differential operators act on coefficient matrices as **superoperators**, with the original-link orientation:
\[
\mathscr D_{12}(X)=-\sum_a J_A^a X J_B^a,\qquad
\mathscr D_{23}(X)=-\sum_a J_B^a X J_C^a
\]
(tensor identity factors implicit). They commute as superoperators, not as ordinary matrices \(\mathscr D_{12}(I)\) and \(\mathscr D_{23}(I)\).
By Schatten trace duality and the row-column Cauchy inequality,
\[
\|\mathscr D_{12}(X)\|_1,\ \|\mathscr D_{23}(X)\|_1\le
s_l\|X\|_1,\qquad s_l=\frac{\sqrt{3l(l+2)}}4.
\tag{3}
\]
As \(b_l>4s_l\), a Neumann inverse in **matrix trace norm** exists, giving for the exact output coefficient
\[
\boxed{\ \|M_l\|_1\le4(l+1)
\frac{|\alpha_l|+2|\beta_l|s_l}{l(l+2)+6-4s_l}\ }\qquad(l=n\pm1).
\tag{4}
\]
At \(l=0\), use the exact scalar response. This bound is **independent of any previously asserted unrestricted Peter–Weyl product algebra bound**.

## Local-first family inequality (all middle spins)

For \(\kappa>0,\sigma\ge0\) and the exact local-first norms \(L^{(r)}\),
\[
\|F_n\|_{L^{(1)}}=16(n+1)^3e^{3\kappa+\sigma(n+2)},\quad
\|G\|_{L^{(2)}}=16e^{\kappa+\sigma}.
\]
With \(m_l=\|M_l\|_1\) and max-spin moment \(1+\max(l,1)\), the **actual** ratio is
\[
R_n(\sigma,\kappa)=\frac{e^{-\kappa}}{256(n+1)^3}
\sum_{l=n\pm1}4(l+1)(1+\max(l,1))m_l\,e^{\sigma(l-n-1)}.
\tag{5}
\]
The lower channel factor is \(e^{-2\sigma}\); the upper factor is 1.

**Theorem:**
\[
\boxed{\,0<R_n(\sigma,\kappa)\le e^{-\kappa}/16
\quad\text{for all }n\ge1,\ \sigma\ge0,\ \kappa>0.\,}
\tag{6}
\]
**Proof:** For \(n\ge2\), bound \(s_l\le(l+1)/2\). Equation (4) gives
\(m_l\le4(l+1)A_l\), with
\[
A_l=\frac{|\alpha_l|+(l+1)/(n+1)}{l^2+4}.
\]
Substitution into (5), using \(e^{-2\sigma}\le1\), reduces (6) to
\[
(n+1)^3\ge
\frac{(n+2)^3[n+(n+2)/(n+1)]}{(n+1)^2+4}
+\frac{n^3[n+2+n/(n+1)]}{(n-1)^2+4}.
\]
After clearing positive denominators this is equivalent to
\[
P(n)=n^8+2n^7-2n^5+6n^4+32n^3-68n-55\ge0.
\]
Setting \(m=n-2\ge0\) yields
\[
P(m+2)=m^8+18m^7+140m^6+614m^5+1666m^4+
2912m^3+3312m^2+2268m+609>0.
\]
For \(n=1\), the exact lower matrix has trace norm \(m_0=2\); in the upper block \(s_2=\sqrt6/2<5/4\), giving \(m_2<3\) from (4). Therefore \(R_1<31e^{-\kappa}/512<e^{-\kappa}/16\).

**High-spin limit:** Because \(\operatorname{tr}\mathscr D_{12}(I)=\operatorname{tr}\mathscr D_{23}(I)=0\), trace duality yields the lower estimate
\[
\|M_l\|_1\ge
\frac{4(l+1)|\alpha_l|}{l(l+2)+6+4s_l}.
\]
Together with (4), this squeezes both \(m_{n+1}\) and \(m_{n-1}\) to 4 as \(n\to\infty\). Hence
\[
\boxed{\lim_{n\to\infty}n e^\kappa R_n(\sigma,\kappa)
=\frac{1+e^{-2\sigma}}{16}.}
\tag{7}
\]
The response decays as \(O(1/n)\) **for this family**, and this does not contradict archived high-spin no-go examples for different norms and input families.

## Verification, correction, and remaining gates

- Exact quaternion PDE/source checks at \(n=1,2\), in the corrected original-link model.
- Independent coefficient-matrix reconstruction of the full response at those same \(n\), evaluated on random noncommuting SU(2) configurations. The **mixed matrix factor is \(A@B\), not \(B@A\)**; the first implementation used the wrong order and was corrected before certification. Ordinary matrix factors need not commute even though their associated left/right differential superoperators do.
- Exact symbolic positivity proof for every integer \(n\ge2\); finite-spin trace-class comparisons through \(n=32\) are regressions, not the all-degree proof.
- Complete runnable scripts and exact-byte hashes are preserved in the companion archived ZIP. The repository's earlier two-face theorem and its physical trace norms were independently compared through \(n=14\); the trace norms agreed despite different matrix spectral representations.

**Missing:** a general coefficientwise bound when **two neighboring faces simultaneously carry arbitrary high spins**, all support/history widths, and a volume-uniform nonlinear convergence theorem. No \(z=1\) interacting physical gap, 3D regulator transport, or 4D Yang–Mills mass-gap proof follows.