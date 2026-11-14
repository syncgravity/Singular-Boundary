# PF-I16 — Corrected face-map pullback and finite-product Kato–Bochner closure

**Review date:** 2026-11-13  
**Scope:** finite accepted-rhombus SU(2) graph; original-link product metric; isolated-face radial dressing; corrected reversible generator. This closes the finite-model metric-pullback and pointwise Kato–Bochner comparison sub-obligations under the explicit incidence and coupling hypotheses below. It does not establish a physical continuum theorem.

## 1. Corrected isolated-rotor bounds

For one isolated face, let \(q_\beta=s_\beta'\). The recorded radius-two SU(2) radial equation and regular endpoint conditions are
\[
q'+2\cot\theta\,q=-4(q^2+\beta\cos\theta+\lambda),\qquad
q(0)=q(\pi)=0,
\]
\[
\lambda=-\frac{\int_0^\pi\sin^2\theta\,q(\theta)^2\,d\theta}
{\int_0^\pi\sin^2\theta\,d\theta}.
\]
Differentiation gives
\[
q''+2\cot\theta\,q'-2\csc^2\theta\,q
=-8qq'+4\beta\sin\theta.
\]
At a positive interior maximum, \(q'=0\) and the equation gives
\(q''=2\csc^2\theta\,q+4\beta\sin\theta>0\), a contradiction. At a negative interior minimum,
\[
0\le q''=2\csc^2\theta\,q+4\beta\sin\theta,
\]
so \(q\ge-2\beta\sin^3\theta\ge-2\beta\). Hence
\[
-2\beta\le q\le0,\qquad \|s_\beta'\|_\infty\le2\beta.
\]

The weighted-mean identity gives \(-4\beta^2\le\lambda\le0\). Put
\(h=q^2+\lambda\) and \(J(\theta)=\int_0^\theta\sin^2u\,h(u)\,du\).
Then \(\|h\|_\infty\le4\beta^2\), \(J(\pi)=0\), and the nearer-endpoint estimate
\[
\left|\frac{\cot\theta}{\sin^2\theta}J(\theta)\right|
\le\frac43\beta^2
\]
follows from
\(\int_0^\theta\sin^2u\,du\le\sin^3\theta/(3\cos\theta)\) on the first hemisphere and the reflected estimate on the second. Integrating the radial equation yields
\[
q=-\frac43\beta\sin\theta-\frac{4J}{\sin^2\theta},
\qquad
q'=-\frac43\beta\cos\theta-4h
+8\frac{\cot\theta}{\sin^2\theta}J.
\]
Therefore
\[
\|s_\beta''\|_\infty\le\frac43\beta+\frac{80}{3}\beta^2,
\qquad
\left\|\frac14\cot\theta\,q\right\|_\infty
\le\frac13\beta+\frac43\beta^2,
\]
and
\[
\boxed{\|\nabla^2s_\beta\|_{\rm op}
\le\frac43\beta+\frac{80}{3}\beta^2.}
\]
These estimates hold for the smooth regular isolated-face ground-state branch. The linear response \(q_\beta/\beta\to-\frac43\sin\theta\) independently rules out the former unit-gradient constant.

## 2. Exact face-map metric pullback

For an oriented face word
\[
H_f=x_1x_2x_3x_4,\qquad x_i=U_i^{\epsilon_i},
\]
the differential in each original-link factor is an adjoint translate of the link tangent. Thus each one-factor differential \(d_iH_f\) is an isometry for the unscaled radius-two bi-invariant metrics. The independently audited suffix calculation gives, for distinct factors,
\[
(\nabla dH_f)(X_i,Y_j)=
\begin{cases}
+\frac12[\eta_i(X_i),\eta_j(Y_j)],&i<j,\\
-\frac12[\eta_i(X_i),\eta_j(Y_j)],&i>j,
\end{cases}
\]
and the same-factor covariant second derivative is zero. In the orthonormal radius-two basis the SU(2) bracket obeys
\(\|[X,Y]\|\le\|X\|\|Y\|\). Hence the mixed geometric term has norm at most
\(\frac12\|X_i\|\|Y_j\|\).

In the product metric
\[
\widetilde g=\bigoplus_e a_e^{-1}g_e,
\]
a unit vector in link block \(e\) has \(g_e\)-norm \(\sqrt{a_e}\). The covariant chain rule therefore gives, for one face,
\[
\|(\nabla^2(s_f\circ H_f))_{ee}\|_{\rm op}
\le a_e\|\nabla^2s_f\|_{\rm op},
\]
\[
\|(\nabla^2(s_f\circ H_f))_{eg}\|_{\rm op}
\le\sqrt{a_ea_g}
\left(\|\nabla^2s_f\|_{\rm op}
+\frac12\|\nabla s_f\|_\infty\right),\quad e\ne g.
\]
No additional metric factor is hidden in the face map: the adjoint transports are isometries, and all scaling is the displayed \(\sqrt{a_e}\) factor.

Use the source-uniform incidence hypothesis \(d_e\le8\) and the allocation
\[
A_f=\sum_{e\in\partial f}\frac{a_e}{d_e},\qquad
A_f\ge\frac{a_0}{2},\qquad a_e\le8A_f,\qquad
\beta_f=\frac{|b_f|}{A_f}\le\frac{2b_0}{a_0}.
\]
With \(\|\nabla s_f\|_\infty\le2\beta_f\), the preceding inequalities give the uniform per-face blocks
\[
\boxed{h_d=\frac{32}{3}b_0+\frac{1280}{3}\frac{b_0^2}{a_0}},
\qquad
\boxed{h_o=\frac{56}{3}b_0+\frac{1280}{3}\frac{b_0^2}{a_0}}.
\]
Indeed, the diagonal coefficient is \(8A_f(\frac43\beta_f+\frac{80}{3}\beta_f^2)\); the off-diagonal coefficient adds \(8A_f\beta_f\) from the half-bracket term.

## 3. Correct reversible generator and Kato–Bochner comparison

The exact ground-state transform fixes
\[
L_\Phi=-\Delta_{\widetilde g}
-2\nabla_{\nabla\Phi},\qquad
\mathscr G_\Phi=-L_\Phi
=\Delta_{\widetilde g}+2\nabla_{\nabla\Phi},
\qquad d\nu_\Phi\propto e^{2\Phi}dU.
\]
The vector Bochner identity is
\[
(\partial_t-\Delta^\nabla_{\widetilde g}
-2\nabla_{\nabla\Phi})\nabla P_tf
=-(\operatorname{Ric}^{\sharp}_{\widetilde g}
-2(\nabla^2\Phi)^\sharp)\nabla P_tf.
\]
Since the product connection preserves link tangent blocks and
\(\operatorname{Ric}^{\sharp}|_{T_e}=(a_e/2)I\), componentwise Kato gives
\[
(\partial_t-\mathscr G_\Phi)|D_eP_tf|
\le-\frac{a_0}{2}|D_eP_tf|
+2\sum_g\|(\nabla^2\Phi)_{eg}\|_{\rm op}|D_gP_tf|.
\]
At zeros this is the upper-Dini inequality obtained by regularizing
\(|W_e|\) as \((|W_e|^2+\varepsilon^2)^{1/2}\) and taking
\(\varepsilon\downarrow0\). The finite-product maximum principle then gives the cooperative system for \(U_e(t)=\sup_x|D_eP_tf(x)|\).

Each link is in at most eight faces, each face has three other links, and distinct links in one face are adjacent in the link-overlap graph. Thus the comparison matrix has
\[
A_{ee}\le16h_d,\qquad
A_{eg}\le2\,n_{eg}h_o,\qquad
\sum_g n_{eg}\le24.
\]
Its unweighted row sum is at most \(16h_d+48h_o\), while for
\(\mu=\log25\) its weighted row sum is at most
\(16h_d+1200h_o\). Substitution gives
\[
\kappa\ge\frac{a_0}{2}
-\frac{3200}{3}b_0-\frac{81920}{3}\frac{b_0^2}{a_0},
\]
\[
\lambda_{\log25}\ge\frac{a_0}{2}
-\frac{67712}{3}b_0-\frac{1556480}{3}\frac{b_0^2}{a_0}.
\]
At \(b_0/a_0\le1/50000\),
\[
\boxed{\kappa\ge0.478655744\,a_0>0,\qquad
\lambda_{\log25}\ge0.048379136\,a_0>0.}
\]
The exact rational arithmetic is reproduced by
[verify_pf_i16_corrected_rotor_constants.py](../verification/verify_pf_i16_corrected_rotor_constants.py).

The weighted cooperative comparison and Duhamel iteration now give the finite-graph derivative-flow theorem
\[
\boxed{
\|D_eP_tf\|_\infty
\le e^{-\lambda_{\log25}t}
\sum_g25^{-d(e,g)}\|D_gf\|_\infty.
}
\]
The positive unweighted curvature margin supplies the centered inverse. This closes the face-map metric pullback and finite-product Kato–Bochner sub-obligations under the stated source-incidence, coefficient-allocation, and weak-coupling hypotheses.

## 4. Consequences and strict boundary

The corrected two-point resolvent-decay estimate and the finite-order third- and fourth-order spatial-tree estimates may therefore use the derivative-flow bound as a proved finite accepted-graph input, uniform in graph volume under the stated hypotheses. The fourth-order cut interpolation is covered uniformly because every crossing-face Hessian block is multiplied by a coefficient \(s\in[0,1]\), so the same absolute block majorants apply throughout the interpolation.

This does **not** prove a cluster expansion for the full residual-interacting Hamiltonian. It does not establish the quantum Kotecký–Preiss criterion, the all-orders connected-resolvent theorem, stability of the true interacting Wilson vacuum, source-derived physical time, a refining physical three-dimensional regulator, continuum/OS reconstruction, or a positive physical Yang–Mills mass gap. The theorem is finite-model and source-normalization specific.
