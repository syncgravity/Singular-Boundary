# PF-I16 isolated-rotor first-derivative hypothesis: perturbative obstruction

**Date:** 2026-11-11  
**Disposition:** the inherited estimate \(\|s_\beta'\|_\infty\le\beta\) is incompatible with the radial ground-state equation recorded in the PF-I16 refined-rotor dossier. All downstream estimates that use that constant must be treated as unverified until rederived.

## 1. The recorded equation

The refined-rotor dossier states, for the radius-two SU(2) class ground-state logarithm \(s_\beta(\theta)\), that \(q_\beta=s_\beta'\) satisfies
\[
q_\beta'+2\cot\theta\,q_\beta
=-4\big(q_\beta^2+\beta\cos\theta+\lambda_\beta\big),
\qquad 0<\theta<\pi,
\]
with regularity at both poles and
\[
\lambda_\beta
=-\frac{\int_0^\pi\sin^2\theta\,q_\beta(\theta)^2\,d\theta}
{\int_0^\pi\sin^2\theta\,d\theta}.
\]
The same dossier imports \(\|q_\beta\|_\infty\le\beta\) as a first-derivative hypothesis.

## 2. Linear response at zero coupling

At \(\beta=0\), the normalized ground state is constant, so \(q_0=0\) and \(\lambda_0=0\). The finite-volume compact-manifold Hamiltonian is an analytic family in \(\beta\); its ground eigenvalue is simple at zero coupling. Standard analytic perturbation therefore gives a differentiable ground-state branch and
\[
q_\beta=\beta q_1+o(\beta)
\quad\text{uniformly on }[0,\pi].
\]
The weighted-mean identity gives \(\lambda_\beta=O(\beta^2)\), hence \(\lambda'_0=0\). Differentiating the radial equation at \(\beta=0\) yields
\[
q_1'+2\cot\theta\,q_1=-4\cos\theta.
\]
Multiplying by \(\sin^2\theta\) and imposing regularity at \(\theta=0\),
\[
(\sin^2\theta\,q_1)'=-4\sin^2\theta\cos\theta,
\]
so
\[
\boxed{q_1(\theta)=-\frac43\sin\theta.}
\]
Consequently,
\[
\boxed{\lim_{\beta\downarrow0}
\frac{\|s_\beta'\|_\infty}{\beta}=\frac43.}
\]

This contradicts \(\|s_\beta'\|_\infty\le\beta\): for all sufficiently small positive \(\beta\), the ratio is strictly greater than one. The discrepancy is not a numerical rounding issue. It is already present in the exact first-order response of the stated differential equation.

## 3. Consequences for the PF-I16 ladder

The following downstream statements cannot currently be used with their published constants:

1. the isolated-face pulled-back Hessian blocks in the refined-rotor dossier;
2. the pointwise Kato–Bochner comparison constants derived from those blocks;
3. the derivative-flow rate and the \(1/40000\) smallness threshold;
4. the shared-link residual derivative bounds that use the same first-derivative estimate;
5. the revised third-order numerical prefactor that inherits these estimates.

The exact radial weighted-mean identity, the exact finite-graph dressing conjugation, the support bound \(25\), the universal incidence inventory \(d_e\le8\), the overlap-degree bound \(28\), and the rooted support count \(784^{k-1}\) are not invalidated by this finding. Nor is the independently audited four-factor mixed-derivative sign calculation.

## 4. Required repair

The first-derivative estimate must be rederived with the correct linear coefficient. At minimum, any valid small-coupling estimate must be consistent with
\[
\|s_\beta'\|_\infty
\ge \left(\frac43-o(1)\right)\beta.
\]
A candidate upper estimate may have the form
\[
\|s_\beta'\|_\infty\le\frac43\beta+C\beta^2,
\]
but the constant \(C\), its admissible coupling interval, and its compatibility with the radial endpoint conditions must be proved rather than assumed.

After obtaining a valid replacement, every pulled-back Hessian block, comparison-matrix row sum, curvature lower bound, derivative-flow decay rate, residual derivative constant, and third-order estimate must be recomputed. The previous numerical values are not to be retained by simply replacing \(\beta\) with \(4\beta/3\) unless each inequality is rederived.

## 5. Reproduction and status

The first-order equation is verified symbolically:
\[
q_1'+2\cot\theta\,q_1+4\cos\theta=0
\quad\text{for }q_1=-\tfrac43\sin\theta.
\]

This is an analytic perturbative obstruction, not a numerical approximation to the full rotor. It does not prove that the dressed PF-I16 route fails; it proves that its currently recorded first-derivative input and dependent constants have not been justified by the stated radial equation.

**Proof status:** local dressing identity — exact finite graph; four-factor mixed derivative signs — independently audited; isolated-rotor first-derivative input — contradicted as stated; downstream analytic PF-I16 constants — require rederivation; all-orders activity, physical normalization, continuum and mass gap — open.


## 6. Corrected radial estimate derived from the same ODE

The obstruction does not leave the rotor without a usable bound. The same ODE gives a simple global estimate for every \(\beta\ge0\), assuming the smooth regular ground-state branch recorded above.

At either pole, smooth radiality gives \(q(0)=q(\pi)=0\). Differentiate the radial equation:
\[
q''+2\cot\theta\,q'-2\csc^2\theta\,q
=-8qq'+4\beta\sin\theta.
\]
At an interior positive maximum of \(q\), \(q'=0\) and \(q''\le0\), whereas the equation gives
\[
q''=2\csc^2\theta\,q+4\beta\sin\theta>0,
\]
a contradiction. Thus \(q\le0\). At an interior negative minimum, \(q'=0\) and \(q''\ge0\), so
\[
q\ge-2\beta\sin^3\theta\ge-2\beta.
\]
Consequently
\[
\boxed{-2\beta\le q_\beta(\theta)\le0,\qquad
\|s_\beta'\|_\infty\le2\beta.}
\]
For negative coupling, the transformation \(\theta\mapsto\pi-\theta\) gives the same absolute bound.

This bound is consistent with, but not sharp at, the linear-response coefficient \(4/3\).

The weighted-mean identity gives \(-4\beta^2\le\lambda_\beta\le0\). Hence for \(h=q^2+\lambda_\beta\), \(\|h\|_\infty\le4\beta^2\). Repeating the endpoint-integral argument with this corrected bound gives
\[
\left|\frac{\cot\theta}{\sin^2\theta}J(\theta)\right|
\le\frac{4}{3}\beta^2.
\]
The radial and tangential Hessian eigenvalues therefore satisfy
\[
\|s_\beta''\|_\infty
\le\frac43\beta+\frac{80}{3}\beta^2,\qquad
\left\|\frac14\cot\theta\,q_\beta\right\|_\infty
\le\frac13\beta+\frac43\beta^2.
\]
Thus the corrected operator bound is
\[
\boxed{\|\nabla^2s_\beta\|_{\rm op}
\le\frac43\beta+\frac{80}{3}\beta^2.}
\]

For the PF-I16 allocation \(A_f\ge a_0/2\), \(\beta_f\le2b_0/a_0\), and \(a_e\le8A_f\), the corresponding *provisional corrected* face blocks are
\[
h_d\le\frac{32}{3}b_0+\frac{1280}{3}\frac{b_0^2}{a_0},
\qquad
h_o\le\frac{56}{3}b_0+\frac{1280}{3}\frac{b_0^2}{a_0}.
\]
Here the off-diagonal mixed term uses \(\|\nabla s_f\|\le2\beta_f\), not \(\beta_f\). The unweighted curvature row bound becomes
\[
\kappa_{\rm BE}\ge\frac{a_0}{2}
-\frac{3200}{3}b_0-\frac{81920}{3}\frac{b_0^2}{a_0},
\]
and the \(\mu=\log25\) derivative-flow comparison gives
\[
\lambda_{\log25}\ge\frac{a_0}{2}
-\frac{67712}{3}b_0
-\frac{1556480}{3}\frac{b_0^2}{a_0}.
\]
In particular \(b_0/a_0\le1/50000\) gives \(\kappa_{\rm BE}>0.4786a_0\) and \(\lambda_{\log25}>0.0483a_0\), **conditional on the remaining product-Hessian, Bochner and comparison arguments**.

The shared-link residual magnitude bound increases by a factor four to \(4160b_0^2/a_0\). The derivative estimates also change; under the same \(1/50000\) ratio, the direct substitution in the recorded residual derivative inequality gives the provisional bounds
\[
\|D_hR_e\|\le21514\frac{b_0^2}{\sqrt{a_0}},\quad
\Big(\sum_h\|D_hR_e\|^2\Big)^{1/2}
\le107570\frac{b_0^2}{\sqrt{a_0}},\quad
\sum_h\|D_hR_e\|\le537850\frac{b_0^2}{\sqrt{a_0}}.
\]
These are corrected algebraic consequences of the stated block/metric bounds, not an independent certification of the full PF-I16 derivative-flow theorem. The third-order numerical prefactor must be recomputed from these corrected residual and semigroup constants; its previous value remains withdrawn.

**Net result:** the false \(\beta\) first-derivative input has been replaced by a proved \(2\beta\) bound and a corrected radial Hessian estimate. The linear response shows that the leading coefficient \(4/3\) cannot be reduced to \(1\). The local analytic route survives, but its downstream constants and the all-orders activity problem remain open.
