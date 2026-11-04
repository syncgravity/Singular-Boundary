# Variable-high-spin recoupled PW matrices: a fixed-sector first-moment theorem

**2026-11-04 | Status: independently derived fixed-three-face sector theorem, numerical CG/Schatten regressions.** The exact detailed report, Python CG validator, execution log and SHA-256 hashes accompany this work in \`highspin_recoupled_audit_2026-11-04.zip\`. Not arbitrary history width, 3D continuum, λ=1 gap, or a Yang–Mills existence/mass-gap solution.

## Model and coefficient normalization

For finite open three-face SU(2) holonomies A,B,C use the original-link Gauss-invariant face realization
\[
K_3=4(C_A+C_B+C_C)+2D_{12}+2D_{23},\quad
D_{12}=\sum_aR_A^aL_B^a,\quad D_{23}=\sum_aR_B^aL_C^a .
\]
SU(2) degree n means spin n/2; put N=n(n+2), M=m(m+2). Write Fourier functions in **trace-expansion** form \(f=\sum_{\bf j}\operatorname{Tr}(A_{\bf j}\pi_{\bf j})\), with projective norm
\[
P_\sigma(f)=\sum_{\bf j}d_{\bf j}e^{\sigma|{\bf j}|}\|A_{\bf j}\|_{S_1},\
d_{\bf j}=\prod_e(j_e+1),\quad\sigma\ge0 .
\]
The local-first \(L^{(1)}\) norm puts \(1+\max_e j_e\) **inside** its anchor sum and attaches \(e^{\kappa|I|}\) to the connected history. For inputs with histories [1,2] and [2,3], the output keeps their union [1,3] and carries relative weight \(e^{-\kappa}\).

## Theorem A: arbitrary matrices in two coupled fixed-degree sectors

For arbitrary PW coefficient matrices F supported on (n,n,0), G supported on (0,m,m), n,m≥1, with these histories, the complete physical centered operation \(\mathcal B_{\rm hist}=K_3^{-1}Q\Gamma_K\) satisfies
\[
\boxed{\|\mathcal B_{\rm hist}(F,G)\|_{L^{(1)}}\le
3e^{-\kappa}\|F\|_{L^{(1)}}\|G\|_{L^{(1)}} .}\tag{A}
\]
The bound applies to all coefficient matrices in these sectors (and thus their residual-Gauss-invariant intertwiner subspaces), **not** only to characters. It is NOT an unrestricted bound for degrees (p,q) and (r,s), or for all history widths.

**Proof.** The two-face K in sector (n,n) is \(2N\,{\rm id}+2\mathscr D_{12}\). The direct Schatten row/column estimate \(\|\mathscr D_{12}\|_{S_1\to S_1}\le N/4\) yields \(P_\sigma(K_2 F)\le5N P_\sigma(F)/2\); similarly \(P_\sigma(K_2 G)\le5M P_\sigma(G)/2\). The input product has output sectors (n,ℓ,m), \(\ell=|n-m|,|n-m|+2,\ldots,n+m\). At each such sector the actual original-link coefficient **superoperators** obey
\[
\|\mathscr D_{12}\|_{S_1\to S_1}\le\tfrac14\sqrt{N\ell(\ell+2)},\quad
\|\mathscr D_{23}\|_{S_1\to S_1}\le\tfrac14\sqrt{M\ell(\ell+2)}.
\]
Writing \(b=N+\ell(\ell+2)+M\) and \(S\) for their summed bounds, AM-GM gives \(S\le b/4\), so the real physical inverse has norm
\[
\|K_3^{-1}\|_{S_1\to S_1}\le (b-2S)^{-1}\le2/b\le2/(N+M).
\]
These are direct trace-norm bounds, not an assumption of the full local-first tame theorem.

The projective matrix PW product inequality \(P_\sigma(fg)\le P_\sigma(f)P_\sigma(g)\) follows from rank-one nuclear atoms, unitary linkwise SU(2) Clebsch–Gordan recoupling, output dimension \(d_{\rm out}\le d_Fd_G\), and \(|{\bf j}_{\rm out}|\le|{\bf j}_F|+|{\bf j}_G|\). This also controls products with \(K_2F,K_2G\), since K preserves their input degree blocks.

Since both outer output degrees n,m are positive, the output has **no full Haar constant**; Q acts as the identity. The exact carré-du-champ polarization reads
\[
\mathcal B_{\rm hist}(F,G)=\tfrac12\left\{K_3^{-1}[(K_2F)G+F(K_2G)]-FG\right\}.
\]
Consequently \(P_\sigma(\mathcal B)\le\tfrac12[2(5/2)(N+M)/(N+M)+1]P_\sigma(F)P_\sigma(G)=3P_\sigma(F)P_\sigma(G)\). Every CG output has \(\ell\le n+m\) and hence \(1+\max(n,\ell,m)\le(1+n)(1+m)\), the product of input first moments. Multiplying by the exact history ratio \(e^{-\kappa}\) proves (A).

## Theorem B: full variable-high-spin recoupled Wilson trace family

For genuinely matrix-index-coupled Wilson words, not products of single-face characters,
\[
F_n=\chi_n(AB),\quad G_m=\chi_m(BC),\quad n,m\ge1,
\]
the shared-link operator acts as \(D_{12}F_n=-n(n+2)F_n/4\) (and similarly for G), so
\[
K_2F_n=\lambda_nF_n,\quad \lambda_n=\tfrac32n(n+2).
\]
Set \(H_{nm}=F_nG_m\). The exact physical nonlinear response is
\[
\boxed{\mathcal B_{\rm hist}(F_n,G_m)=
\tfrac12[(\lambda_n+\lambda_m)K_3^{-1}H_{nm}-H_{nm}] .}\tag{B}
\]
The same Schatten inverse bound sharpens (A) to
\[
\boxed{\|\mathcal B_{\rm hist}(F_n,G_m)\|_{L^{(1)}}\le
2e^{-\kappa}\|F_n\|_{L^{(1)}}\|G_m\|_{L^{(1)}} .}\tag{C}
\]
The trace-word coefficient is a dimension-(n+1)^2 permutation (swap), giving precisely
\(P_\sigma(F_n)=(n+1)^4e^{2\sigma n}\) and
\(\|F_n\|_{L^{(1)}}=e^{2\kappa}(n+1)^5e^{2\sigma n}\). **Do not replace** this trace-expansion norm with Haar-normalized Fourier coefficients.

## Exact all-spin low-energy middle-zero output

By SU(2) Schur orthogonality on middle B,
\[
P_{B,0}[F_nG_m]=\delta_{nm}\,\chi_n(AC^{-1})/(n+1).
\]
The resulting nonconstant physical outer-loop trace has \(K_3\)-energy \(2n(n+2)\). Applying (B) therefore gives the exact all-degree output
\[
\boxed{P_{B,0}\mathcal B_{\rm hist}(F_n,G_m)
=\delta_{nm}\,\chi_n(AC^{-1})/[4(n+1)] .}\tag{D}
\]
When n=1 and F,G are scaled by 1/2, this yields \(\operatorname{Re}(AC^{-1})/16\), confirming the previous exact fundamental-spin trace-word result. This is a physical disconnected-minimal-support channel retained on connected history [1,3], *not* a removable scalar or autonomous connected-support quotient.

## Independent regression / limits

The companion actual CG test explicitly constructs spin generators, every allowed middle-face Fourier coefficient of \(F_nG_m\), and the **correct left/right matrix superoperators**. For 9 nontrivial pairs n,m=1,2,3 it verifies noncommuting-group reconstruction, all inverse block residuals, Schatten norms, the first-moment ratio and the n=m projected output. All passed. Finite tests complement, rather than prove, the all-degree argument.

**Missing implication:** the fixed-sector restriction (n,n) vs (m,m) enforces an outer-spin energy barrier \(n(n+2)+m(m+2)\). More general PW matrices with unequal outer and middle degrees can lose this barrier under middle-spin fusion; no width-uniform or unrestricted first-grade closure follows. Next investigate **arbitrary external degrees and independently large middle degrees** for off-diagonal intertwiners, retaining all low-energy physical outputs and history information. The P0 3D regulator and the interacting continuum mass gap remain open.