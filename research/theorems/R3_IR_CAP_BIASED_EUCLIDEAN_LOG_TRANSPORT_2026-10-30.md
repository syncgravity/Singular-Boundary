# Exact first-order cap-biased Euclidean transport identity for four-neighbor Wilson completion

**2026-10-30 | R3-IR | Classification:** exact finite-volume physical SU(2) Wilson identity and **conditional** cap-survival criterion. This is an alternative to the archived eighth mixed derivative, not a proof of the remaining signed comparison. No uniform mass gap is assumed or established.

## 1. Physical Hamiltonian and positive source

Use the genuine four-neighbor *magnetic-deleted target* setting of FN-1–FN-5: a finite edge-to-edge rhombus disk, target face \(f\) with its magnetic term absent, four distinct neighbors \(g_i\), and
\[
H(t)=H_{\rm rest}+\sum_{i=1}^4t_i b_i(1-p_i),\quad p_i=p_{g_i},\quad b_i\ge0,\quad t\in[0,1]^4.
\]
Work on the full original-link *Gauss-invariant* physical Hilbert space, not a gauge-fixed surrogate. Let \(O=k_a(W_f)\) be the positive bounded convolution cap observable from FN-4, supported on the target cap and satisfying \(0\le O\le\nu_a\,1_{\{W_f\in B_a\}}\) and \(\int_{SU(2)}k_a=\alpha_a^2>0\). Define
\[
F_{a,\beta}(t)=\frac{\operatorname{Tr}_{\rm phys}(Oe^{-\beta H(t)})}{\operatorname{Tr}_{\rm phys}(e^{-\beta H(t)})}
>0,\qquad F_a(t)=\lim_{\beta\to\infty}F_{a,\beta}(t)>0.
\]
At fixed finite \(\beta\), the physical Feynman–Kac loop measure with Gauss averaging at the time seam is positive. Set \(X_i=b_i\int_0^\beta p_i(U(\tau))\,d\tau\). Write \(\mathbf E_{\beta,t}\) for ordinary positive normalized path expectation and
\[
\mathbf E_{\beta,t}^{O}[Y]
:=\frac{\mathbf E_{\beta,t}[O(U(0))Y]}{\mathbf E_{\beta,t}[O(U(0))]}
\]
for cap-biased positive expectation. The latter is well defined since \(F_{a,\beta}>0\).

## 2. Exact first-order log transport

For every differentiable path \(t:[0,1]\to[0,1]^4\),
\[
\boxed{
\log\frac{F_{a,\beta}(t(1))}{F_{a,\beta}(t(0))}
=\int_0^1\sum_{i=1}^4\dot t_i(\lambda)
\left(\mathbf E_{\beta,t(\lambda)}^{O}X_i-
\mathbf E_{\beta,t(\lambda)}X_i\right)d\lambda.
}\tag{CT-1}
\]
**Proof.** On the positive physical Euclidean path measure, varying \(t_i\) changes its weight by the exponential factor \(\exp(t_i X_i-\beta t_i b_i)\). The scalar term cancels in normalized expectations. Differentiating \(\log\mathbf E_{\beta,t}O\) therefore gives
\[
\partial_{t_i}\log F_{a,\beta}(t)
=\frac{\operatorname{Cov}_{\beta,t}(O,X_i)}{F_{a,\beta}(t)}
=\mathbf E_{\beta,t}^{O}X_i-\mathbf E_{\beta,t}X_i.
\]
The path chain rule and integration prove CT-1. No spectral inverse, cluster decomposition, or sign claim is used. QED.

The identity holds along **any** path in the coupling cube, not only the diagonal. The scalar function \(\log F_{a,\beta}\) is the potential for the exact one-form on the right, so its closed-loop integral vanishes. This provides a consistency check on prospective approximations to the signed response.

## 3. Zero-temperature physical ground-state formulation

At fixed finite lattice each \(H(t)\) has a unique strictly positive physical ground state with a finite positive physical gap, but no gap bound uniform in \(h\) is assumed. The rank-one ground projector and its fixed-order derivatives are analytic in a neighborhood of each real point, and the physical heat-trace expectation converges locally with its first derivatives as \(\beta\to\infty\). Consequently along a fixed piecewise \(C^1\) path,
\[
\boxed{
\log\frac{F_a(t(1))}{F_a(t(0))}
=\lim_{\beta\to\infty}\int_0^1\sum_i\dot t_i
(\mathbf E_{\beta,t}^{O}X_i-\mathbf E_{\beta,t}X_i)\,d\lambda.
}\tag{CT-2}
\]
This is the limit of the **combined signed difference**, not an assertion that the individual integrated-plaquette expectations converge separately as \(\beta\to\infty\). Each may grow linearly with \(\beta\).

For a monotone diagonal completion \(t_i(\lambda)=\lambda\), define the finite lattice signed logarithmic response
\[
\mathcal A_{a,h}
:=\lim_{\beta\to\infty}\int_0^1
\sum_{i=1}^4
\left(\mathbf E_{\beta,\lambda\mathbf1}^{O}X_i
-\mathbf E_{\beta,\lambda\mathbf1}X_i\right)d\lambda.
\]
By the magnetic-private-link theorem FN-1, \(F_a(0)=\alpha_a^2\). Therefore
\[
\boxed{\quad F_a(\mathbf1)=\alpha_a^2e^{\mathcal A_{a,h}},
\qquad
\mathbb P_{\Omega_{\mathbf1}}(W_f\in B_a)
\ge\frac{\alpha_a^2}{\nu_a}\,e^{\mathcal A_{a,h}}.
\quad}\tag{CT-3}
\]
For any small-cap scaling \(a_h\asymp\sqrt h\), the previously required Haar-order lower bound would follow if, **as a new independently proved Wilson-specific hypothesis,**
\[
\boxed{\liminf_{h\downarrow0}\inf_{f\in D_R}\mathcal A_{a_h,h}>-\infty.}\tag{CT-4}
\]
For the precise FN-5 half-Haar criterion, the sufficient condition is \(\mathcal A_{a_h,h}\ge-\log2\). Neither is currently established.

## 4. Relationship to the eighth-order cumulant gate

CT-1 is a **first-order** transport identity that avoids dividing by an unknown spectral gap and does not take the absolute value of the eighth mixed response. It retains potentially beneficial cancellations between cap-biased and ordinary physical Wilson paths. The price is that the cap-biased expectation is normalized by the small positive cap observable \(F_{a,\beta}\), so a uniform lower bound or signed cancellation is still required; CT-4 is genuinely open.

The earlier eightfold derivative integral and this log-transport formula are two exact descriptions of the *same* full-coupling cap response. Neither implies a favorable sign for the other without additional Wilson-specific information. The formal order reduction does not prove stochastic domination, Euclidean mixing, or positive covariance. Any proposal to drop the negative portion of the path response must prove a Wilson-specific inequality, not rely on positivity of the underlying measure alone.

**Next proof task:** derive a signed lower bound on the cap-biased integrated-plaquette **difference** along the coupling completion path, with explicit \(h\), ambient-volume, and collar dependence; do so without importing the desired spectral gap. In particular test if local plaquette alignment or a valid correlation inequality survives the nonabelian shared-link geometry and the Gauss seam.

**Status:** CT-1–CT-3 exact fixed-finite-volume; CT-4 an OPEN sufficient hypothesis. Completed-cage signed current, cap-survival scaling, spectral gap and continuum reconstruction remain OPEN.
