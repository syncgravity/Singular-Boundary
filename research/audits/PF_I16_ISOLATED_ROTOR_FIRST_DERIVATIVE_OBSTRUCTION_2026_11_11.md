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
