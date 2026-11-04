# Direct nested-history Casimir estimate in one face Peter–Weyl norm

**2026-11-04. Theorem scope:** corrected original-link SU(2) electric operator expressed on independent face holonomies of a finite open straight square strip. Full expanded proof, two independent executed tests, logs, SHA-256 manifest: accompanying conversation archive **p2_direct_face_nested_casimir_2026-11-04.zip**. This is **graded tame**, not same-grade closure, a nonlinear fixed point, an interacting gap or a continuum Yang–Mills theorem. Do **not** transfer the result by identifying inequivalent original-link and face PW projective norms.

Let \(K=4\sum_i C_i+2\sum_i\sum_a R_i^aL_{i+1}^a\) be the corrected original-link positive electric operator, \(Q\) global Haar-constant centering only, \(\Gamma_K=(fKg+gKf-K(fg))/2\), and \(\mathcal B=K^{-1}Q\Gamma_K\). SU(2) integer degree n is spin n/2. Define the **face trace-expansion nuclear** norm
\[
P_\sigma^{(r)}(f)=\sum_{\mathbf n}d_{\mathbf n}e^{\sigma\sum_i n_i}(1+\max_i n_i)^r\|A_{\mathbf n}\|_{S_1},
\quad d_{\mathbf n}=\prod_i(n_i+1),
\]
and the local-first history norm \(\|F\|_{L_{\kappa,\sigma}^{(r)}}=\sup_x\sum_{I\ni x}e^{\kappa|I|}P_\sigma^{(r)}(f_I)\), with \(\kappa>0,\sigma\ge0\), integers \(r\ge1\). The full output (including nonconstant disconnected-minimal-support channels) receives the connected union-history label.

## Independently available same-coordinate operator facts

1. SU(2) unitary Clebsch–Gordan recoupling and Schatten-1 block pinching give the **face** PW multiplication inequality. On every nonconstant output degree tuple c with \(D_{\mathbf c}=\sum_i c_i(c_i+2)\ge3\), the *actual original-link* matrix superoperator obeys \(\|K_{\mathbf c}^{-1}\|_{S_1\to S_1}\le2/D_{\mathbf c}\). Mixed shared-link superoperator images must not be treated as ordinary commuting matrices.
2. The previously directly derived all-width **single-pair** coefficientwise result (research/audits/WIDTH34_PAIRWISE_CROSSING_PW_2026-11-04.md) is
\[
P_\sigma^{(r)}(\mathcal B(f_I,g_J))
 \le (2+6|I\cap J|)P_\sigma^{(r)}(f_I)P_\sigma^{(r)}(g_J).
\]
It also supplies the directly proved anchored crossing/end-joining bound \(C_{\rm cross}(t)=8/(1-t)+24t/(1-t)^2\), \(t=e^{-\kappa}\).
3. On an original link e incident to at most two face variables, a fixed-degree original-link derivative is a sum of up to two left/right spin generators. Let \(w_e(\mathbf a)=\sum_{i\text{ incident to }e}a_i\). Then
\[
P_\sigma(\Gamma_K(f_\mathbf a,g_\mathbf b))
 \le\tfrac34\sum_e w_e(\mathbf a)w_e(\mathbf b)
 P_\sigma(f_\mathbf a)P_\sigma(g_\mathbf b).
\]
This is proved **in face coordinates** by generator norms \(\|J_{n/2}\|_{\rm op}\le n/2\), the three electric directions and the face PW product algebra. It is not imported by unproved norm transport.

## New source-collar / surviving-energy split

Fix an outer history I, inner \(J\subseteq I\), nonzero outer degree tuple a, inner tuple b, \(s=\max_i b_i\), \(D=\sum_i a_i(a_i+2)>0\), \(q_J=\sum_{i\in J}a_i(a_i+2)\), and \(J^+=\{i:\operatorname{dist}(i,J)\le1\}\).

**Original-link source collar:** on links incident to J, \(w_e(\mathbf b)\le2s\); four original edges per face imply \(\sum_e w_e(\mathbf a)w_e(\mathbf b)\le8s\sum_{i\in J^+}a_i\). Therefore the source multiplier is bounded by \(6s\sum_{i\in J^+}a_i\).

**Crucial energy distinction:** a shared original link can differentiate an outer face just beyond J, but CG **fusion** only modifies face degrees where both input functions have nonzero degree, hence **only inside J**. Thus all outer degrees outside *uncollared* J survive in every output, giving \(D_{\rm out}\ge D-q_J\). This was independently checked using the actual corrected original-link Fourier inverse, not free independent rotors.

**Good inner histories**, \(q_J\le D/2\): \(\|K_{\rm out}^{-1}\|\le4/D\). Multiplying the source bound gives \(24s D^{-1}\sum_{i\in J^+}a_i\). The output max-spin moment satisfies \((1+\max c_i)^r\le(1+\max a_i)^r(1+s)^r\); absorb s with one extra **inner** moment \((1+s)^{r+1}\). For nonnegative inner weights \(W_J\), put \(G_*=\sup_x\sum_{J\ni x}W_J\). The three-anchor collar bound
\[
\sum_{J:i\in J^+}t^{|J|}W_J\le3tG_*
\]
and \(\sum_i a_i\le D/3\) imply
\[
\|\mathcal B_{\rm good}(F,G)\|_{L^{(r)}}
 \le24t\|F\|_{L^{(r)}}\|G\|_{L^{(r+1)}}.
\]

**Exceptional inner histories**, \(q_J>D/2\): use the independent pairwise estimate, with factor \((2+6|J|)t^{|J|}\). Define \(H_\kappa=\sup_{m\ge1}(2+6m)t^{m/2}<\infty\). The Markov-energy charging inequality holds for any nonnegative W:
\[
\sum_{J:q_J>D/2}t^{|J|/2}W_J
\le\frac2D\sum_i a_i(a_i+2)\sum_{J\ni i}t^{|J|/2}W_J
\le2\sqrt t\,G_*.
\]
Therefore
\[
\|\mathcal B_{\rm exceptional}(F,G)\|_{L^{(r)}}
\le 2\sqrt t H_\kappa\,\|F\|_{L^{(r)}}\|G\|_{L^{(r)}}.
\]
When D=0 the outer function is constant, and the original-link Poisson source vanishes.

## Main results

**Direct all-width one-sided nested graded estimate**, uniform over *every finite strip length, nested interval length, all SU(2) degrees*:
\[
\boxed{\|\mathcal B_{\rm nest}^{G\subseteq F}(F,G)\|_{L^{(r)}}
\le24t\|F\|_{L^{(r)}}\|G\|_{L^{(r+1)}}
+2\sqrt tH_\kappa\|F\|_{L^{(r)}}\|G\|_{L^{(r)}}.}\tag{1}
\]

Sum both nested orientations (double-counting equal histories is safe) and the certified crossing/end-joining result. This proves the **direct graded all-history** estimate, still in the same face norm:
\[
\boxed{\begin{aligned}
\|\mathcal B_{\rm hist}(F,G)\|_{L^{(r)}}\le {}&
C_{\rm same}(\kappa)\|F\|_{L^{(r)}}\|G\|_{L^{(r)}}\\
&+24t\big[\|F\|_{L^{(r)}}\|G\|_{L^{(r+1)}}
+\|F\|_{L^{(r+1)}}\|G\|_{L^{(r)}}\big],
\end{aligned}}\tag{2}
\]
where \(C_{\rm same}=8/(1-t)+24t/(1-t)^2+4\sqrt tH_\kappa\). For \(\kappa=\log4\), \(t=1/4\), \(H_\kappa=4\), so **\(C_{\rm same}=88/3\)** and the extra moment coefficient is **6**.

The direct proof removes the **previously inherited unrestricted coefficientwise Poisson bound** for this finite straight-strip model; it does **not** remove the extra inner spin moment. Nor does the graded estimate imply an invariant fixed-grade Banach algebra, convergence of the source-generated score, physical \(\lambda=1\) positivity, Borel summability, OS reconstruction or 4D continuum Yang–Mills mass gap. All are distinct open obligations. A formal Gevrey/Borel-disk implication requires additional independently audited source-order spin caps and recurrence hypotheses.

## Reproducibility and provenance

The detailed companion archive includes:
- **108,513 exact-rational** face-energy/collar/exception/source-charge checks, widths 1–28.
- **16** non-character complex matrix nested inputs, **52 actual original-link Fourier inverse blocks**, both good and exceptional energy classes; full nonconstant output retained, source bound and inverse residuals verified.
- Detailed full report, two executable verifiers, logs and SHA-256 manifest. ZIP integrity checked.

**Next proof gate:** remove the extra max-spin moment by sharper energy/recoupling, or establish a rigorous summability/convergence mechanism for the generated graded nonlinear recurrence, with the complete physical history reconstruction.