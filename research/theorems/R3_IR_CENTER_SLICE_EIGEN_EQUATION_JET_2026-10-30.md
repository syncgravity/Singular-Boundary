# Exact center derivative as a conditional slice of the Wilson eigen-equation

**Date:** 2026-10-30. **Status:** exact fixed-finite-volume endpoint identity, valid for complete magnetic cages in the actual positive Gauss-invariant SU(2) ground state. This is a reduction, not an estimate uniform in the Penrose regulator. It supplements the existing endpoint regularity theorem, not a replacement.

## Setting

Let \(H=T+V\) on \(SU(2)^E\), where \(T=\sum_e a_e(-\Delta_e)\), each \(a_e>0\), and \(V\) is a smooth gauge-invariant Wilson potential. Let \(H\Omega=E_0\Omega\) for the unique strictly positive, smooth, normalized and gauge-invariant ground state \(\Omega\). Fix a simple target plaquette \(f\), choose one original boundary link \(e\in\partial f\), and write the original coordinates as \((x,y)\), where \(x=U_e\) and \(y\) denotes every other link.

There is a smooth, Haar-preserving map \(x=x(W,y)\) for which the based target holonomy is \(W=W_f(x,y)\). At fixed \(y\), this map is a left/right group translation, with a possible inversion. Define
\[
F(W)=\int_{SU(2)^{E\setminus\{e\}}}\Omega(x(W,y),y)^2\,dy.
\]
Full vertex Gauss invariance makes \(F\) central, so \(F(W)=r(p)\), with \(p=\frac12\operatorname{Tr}W\), and \(r\) a positive smooth function on \([-1,1]\). This is precisely the target-trace density ratio to Haar in the ground-state Born measure. Put \(\psi=\sqrt r\).

## Theorem (CE-1): exact endpoint jet

At the group identity \(I\), where \(p=1\), the SU(2) fundamental Casimir normalization implies
\[
\boxed{
r'(1)=-\frac43(\Delta_W F)(I)
=-\frac83\int\left[
\Omega\,\Delta_e\Omega+|\nabla_e\Omega|^2
\right]_{x=x(I,y)}dy.
}\tag{CE-1}
\]
Consequently,
\[
\boxed{
\left.\partial_p\log\psi(p)\right|_{p=1}
=-\frac{4}{3r(1)}
\int\left[\Omega\,\Delta_e\Omega+
|\nabla_e\Omega|^2\right]_{x=x(I,y)}dy.
}\tag{CE-2}
\]
The same formulas hold at the opposite center \(W=-I\), with \(r'(-1)=\frac43(\Delta_WF)(-I)\) because \(\Delta_W p=-3p/4\) and \(p=-1\) there.

## Theorem (CE-2): conditional eigen-equation decomposition

Write
\[
H=a_e(-\Delta_e)+H_{\neg e}+V_e,
\]
where \(H_{\neg e}\) comprises all electric terms except \(e\) and all magnetic terms not incident to \(e\), while \(V_e\) is the sum of magnetic plaquette terms incident to \(e\). The differential operator \(H_{\neg e}\) differentiates the **original** link coordinates while \(x\) is held fixed; after evaluating \(x=x(I,y)\), it must not be treated as a Laplacian on a fixed-\(W\) slice.

The eigen-equation gives \(a_e\Delta_e\Omega=(H_{\neg e}+V_e-E_0)\Omega\). Therefore the endpoint coefficient is exactly
\[
\boxed{
\left.\partial_p\log\psi\right|_{p=1}
=-\frac{4}{3a_e r(1)}
\int\!\left[
\Omega(H_{\neg e}+V_e-E_0)\Omega
+a_e|\nabla_e\Omega|^2
\right]_{x=x(I,y)}dy.
}\tag{CE-3}
\]
The integral is finite and depends on the conditional **center slice** \(W_f=I\). Although \(V_e\) involves only the faces meeting \(e\), the \(H_{\neg e}\) term and the eigenvalue retain dependence on the entire interacting vacuum. No positivity/sign statement for the integral follows from the eigen-equation alone.

**Proof of CE-1–CE-3.** Because \(F\) is smooth and central, the group identity \(\Delta_Wp=-3p/4\), together with \(\nabla_Wp=0\) at \(W=\pm I\), yields \(\Delta_WF(I)=-3r'(1)/4\) and \(\Delta_WF(-I)=3r'(-1)/4\). Differentiation under the compact \(y\)-integral and the isometry of link translation/inversion give \(\Delta_W F=2\int(\Omega\Delta_e\Omega+|\nabla_e\Omega|^2)dy\) on each fixed-\(W\) slice. Half of \(\partial_p\log r\) is \(\partial_p\log\psi\); substituting the eigen-equation gives CE-3. QED.

## Consequence for the signed endpoint current

By the exact score Ward identity from the preceding records,
\[
\partial_u\log\psi(\cos u)
=-u\,\partial_p\log\psi(1)+O(u^3).
\]
Thus CE-3 identifies the actual coefficient of the linear center-angle drift. Its sign depends on the conditional sliced balance of the full kinetic and potential eigen-equation, not just on the incident magnetic potential \(V_e\). A uniform estimate of this slice functional, or a direct integrated one-sided estimate beyond the first jet, is required for \(\sup_{f\in D_R}\mathfrak T_{f,h}=o(h^{-1/4})\).

## Important limitations and proof strategy

1. Evaluating the full eigen-equation on \(W_f=I\) is **not** the same as conditioning an arbitrary nonnegative bulk energy on the event \(W_f=I\); that event has ambient Haar measure zero. CE-3 is a smooth trace identity on a geometric fiber, not a probabilistic estimate obtained by dividing by its event probability.
2. The term \(\Omega H_{\neg e}\Omega\) on the center slice cannot be integrated by parts as though the slice fixed the original edge \(x\). The coordinate \(x(I,y)\) changes with \(y\); ignoring this creates spurious sign conclusions.
3. A bound on the single endpoint jet alone would not control many sign changes of the score on a finite collar. A regulator-uniform **one-sided variation** or a quantified higher-derivative control is additionally required.
4. The local Harnack theorem bounds the amplitude ratio but not this conditional second-derivative slice at the needed scale. The present theorem does not close completed-cage current, covariance, or the continuum gap.

**Next obligation:** establish a center-collar control of the CE-3 conditional slice and its variation under \(p=\cos u\), keeping original link/target-fiber derivatives distinct and exploiting the actual nonlinear Wilson structure without inserting an assumed mass gap.
