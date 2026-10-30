# The Singular Boundary — Signed radial-current reduction for the nonlinear SU(2) deleted-face marginal

**Research date:** 2026-10-29. **Program:** R3 independent reconstruction. **Status:** an exact *true-interacting-deleted-vacuum* conditional-score/current theorem; an improved **conditional** all-bulk deletion criterion; and a sharp smooth positive SU(2) rotor countermodel showing that the previous positive-part fiber-energy budget is **not necessary** for Haar-order center-ball probability. **Not proved:** a Penrose-uniform bound on the new conditional current, actual bulk deletion tail, fixed-support nonlinear covariance, positive continuum mass gap, quartic resolvent or Stage7/26 source correspondence.

## 1. Exact nonlinear model

On a finite, simply connected, face-complete rhombus disk with all-vertex Gauss invariance, let

\[
H_f^- = \sum_e a_e(-\Delta_e)+\sum_{g\neq f}b_g(1-p_g),
\quad p_f=\frac12\mathrm{ReTr}\,W_f,
\quad A_f=\sum_{e\in\partial f}a_e>0,
\quad k_f=A_f/4.
\]

Let \(\Omega_f^-\) be the unique normalized strictly positive ground state. Push its density forward under \(p_f=\cos u\), \(0\le u\le\pi\). Write

\[
d\nu_f^-(u)=\omega_0(u)\psi_f(u)^2du,\qquad
\omega_0(u)=\frac2\pi\sin^2u,\quad
\int_0^\pi\omega_0\psi_f^2=1.
\]

The exact deleted-face center-flux symmetry gives \(\psi_f(\pi-u)=\psi_f(u)\). The previous full multichannel quantum fiber theorem, which retains all slow collective modes, yields the exact radial equation

\[
-k_f(\psi_f''+2\cot u\,\psi_f')+(\mathcal U_f(\cos u)-E_f^-)\psi_f=0.\tag{RC-1}
\]

Denote the fiber excess potential by \(V_f(u)=\mathcal U_f(\cos u)-E_f^-\). At each finite regulator the radial amplitude is smooth and positive, with its natural vanishing endpoint derivatives.

## 2. A hierarchy of three one-sided budgets

Define

\[
\begin{aligned}
\mathfrak O_f&=\sup_{0\le v\le u\le\pi/2}[\log\psi_f(u)-\log\psi_f(v)]_+,\\
\mathfrak T_f&=\int_0^{\pi/2}[\partial_u\log\psi_f(u)]_+\,du,\\
\mathfrak B_f&=\frac1{k_f}\int_0^{\pi/2}\sin u\cos u\,[V_f(u)]_+\,du.
\end{aligned}\tag{RC-2}
\]

The last is exactly the positive-part effective fiber-energy budget proved in the preceding one-sided report.

**Theorem RC-1 (exact signed-current sharpening).** In the actual nonlinear deleted vacuum,

\[
\boxed{0\le\mathfrak O_f\le\mathfrak T_f\le\mathfrak B_f.}\tag{RC-3}
\]

Moreover, define the *conditional vacuum-score current*, with all terms referring to the true deleted ground state,

\[
C_f(p)=\mathbb E_{\Omega_f^-}\!\left[
\sum_{e\in\partial f}a_e\nabla_ep_f\cdot\nabla_e\log\Omega_f^-
\ \middle|\ p_f=p\right].\tag{RC-4}
\]

Then the exact score transport formula is

\[
\boxed{\displaystyle
\mathfrak T_f=\frac1{k_f}\int_0^{\pi/2}
\frac{[-C_f(\cos u)]_+}{\sin u}\,du
=\frac4{A_f}\int_0^{\pi/2}\frac{[-C_f(\cos u)]_+}{\sin u}\,du.}\tag{RC-5}
\]

**Proof.** The exact previous marginal-score identity states

\[
 k_f(1-p^2)\frac{d}{dp}\log F_f(p)=2C_f(p),\qquad F_f(\cos u)=\psi_f(u)^2.
\]

Therefore \(\partial_u\log\psi_f(u)=-C_f(\cos u)/(k_f\sin u)\), giving RC-5. The first inequality RC-3 is the positive-variation bound for a continuously differentiable function. For the second, the exact Riccati equation for \(r=\psi_f'/\psi_f\) is

\[
(\sin^2u\,r)'=\frac{\sin^2u}{k_f}V_f(u)-\sin^2u\,r^2.
\]

The endpoint flux vanishes. Hence \([r(u)]_+\le[k_f\sin^2u]^{-1}\int_0^u\sin^2t\,[V_f(t)]_+dt\). Integrate over \(u\in[0,\pi/2]\), exchange integrals and use \(\int_t^{\pi/2}\csc^2u\,du=\cot t\). This gives \(\mathfrak T_f\le\mathfrak B_f\), without assuming monotonicity, Gaussianity, or an excitation gap. □

## 3. Sharpened true-deleted-vacuum center cap and magnetic deletion consequence

Let \(\alpha\in(0,\pi/2]\), \(m_H(\alpha)=(\alpha-\frac12\sin2\alpha)/\pi\), and \(m_f^-(\alpha)=\int_0^\alpha\omega_0\psi_f^2\). The center-even normalization and the one-sided comparison \(\psi(u)\le e^{\mathfrak O_f}\psi(v)\) for \(v\le u\le\pi/2\) yield the exact **nonlinear** lower bound

\[
\boxed{\displaystyle
m_f^-(\alpha)\ge e^{-2\mathfrak O_f}m_H(\alpha)
\ge e^{-2\mathfrak T_f}m_H(\alpha)
\ge e^{-2\mathfrak B_f}m_H(\alpha).}\tag{RC-6}
\]

The middle bound is strictly stronger in general than the last. Identical inequalities hold for the opposite SU(2) center cap. The formula works for angular cap \(\alpha=\arccos(1-\delta)\), for which \(m_H(\delta)\sim (4\sqrt2/(3\pi))\delta^{3/2}\).

Combine RC-6 with the **previously independently proved all-face variational magnetic-deletion inequality** (\(b_f>0,\ \kappa_f=\sqrt{2b_f/A_f}\ge1\)):

\[
\Delta_f=E_0(H)-E_0(H_f^-)
\le\frac{b_f}{\kappa_f}\left[2+\log\frac{2e^2\kappa_f}{m_f^-(d_f\le1/\kappa_f)}\right].
\]

Thus the **new sharpened conditional bound** is

\[
\boxed{\displaystyle
\Delta_f\le\sqrt{\frac{A_fb_f}{2}}\left[
2+\log\frac{2e^2\kappa_f}{m_H(1/\kappa_f)}+2\mathfrak T_f\right].}\tag{RC-7}
\]

Under declared Penrose coefficients \(0<A_-\le A_f\le A_+\) and \(\beta_-h^{-2}\le b_f\le\beta_+h^{-2}\), this gives \(\Delta_f\le Ch^{-1}[1+\log(1/h)+\mathfrak T_{f,h}]\). Therefore, **if independently proved**, either

* \(\sup_f\mathfrak T_{f,h}=O(\log(1/h))\) yields polynomial deleted-center mass;
* \(\sup_f\mathfrak T_{f,h}=o(h^{-1/4})\) yields \(\Delta_f=o(h^{-5/4})\), stretched-exponential exclusion of \(h^{3/4}\)-size defects throughout any fixed area and the previously established fixed-support Wilson–angle observable equivalence.

Both are conditional implications; neither bound on the actual nonlinear Penrose current has been proved. **The important improvement** is that bounding \(\mathfrak T\) is strictly weaker than bounding \(\mathfrak B\) at the same rate.

## 4. Exact smooth, positive SU(2) quantum ground-state countermodel: \(\mathfrak B\) can diverge while \(\mathfrak T\to0\)

Let \(n\ge2\) be an even integer, \(\epsilon_n=n^{-3/2}\), and define on SU(2) class angles

\[
\boxed{\displaystyle
\psi_n(u)=\frac{1+\epsilon_n\cos(2nu)}{\sqrt{1+\epsilon_n^2/2}}.}\tag{RC-8}
\]

For \(n\ge2\), exact SU(2) Haar character orthogonality gives \(\int\omega_0\cos(2nu)=0\) and \(\int\omega_0\cos^2(2nu)=1/2\), so the normalization is exact. \(\cos(2nu)=T_{2n}(\cos u)\) is a polynomial in the plaquette trace: the state is smooth, strictly positive, gauge-invariant and center-symmetric.

Fix any \(k>0\). Define the smooth class potential

\[
V_n^{\rm raw}(u)=k\frac{\psi_n''+2\cot u\,\psi_n'}{\psi_n},\quad
c_n=\frac{12k n^2\epsilon_n}{1-\epsilon_n},\quad
W_n=V_n^{\rm raw}+c_n.\tag{RC-9}
\]

Because \(|\cot u\sin(2nu)|\le2n\) on \([0,\pi]\), \(|V_n^{\rm raw}|\le c_n\), and hence \(0\le W_n\le2c_n=O(k\sqrt n)\). The genuine SU(2) *class rotor* Hamiltonian \(H_n=-k(\partial_u^2+2\cot u\,\partial_u)+W_n\) has \(H_n\psi_n=c_n\psi_n\). By positivity of \(\psi_n\) and the ground-state transform, this is its unique positive ground state. **The potential \(W_n\) is constructed, not the Wilson magnetic-deleted Penrose environment.** This is a countermodel to an inference from the abstract exact radial equation alone.

The exact one-sided quantities obey

\[
\boxed{\begin{aligned}
J_n&=\int\omega_0|\psi_n'|^2
=\frac{2n^2\epsilon_n^2}{1+\epsilon_n^2/2}\sim\frac2n,\\
\mathfrak O_n&=\log\frac{1+\epsilon_n}{1-\epsilon_n}\sim2n^{-3/2},\\
\mathfrak T_n&=\frac n2\log\frac{1+\epsilon_n}{1-\epsilon_n}\sim n^{-1/2},\\
\mathfrak B_n&\sim\frac2\pi n^{1/2}.
\end{aligned}}\tag{RC-10}
\]

Proof of \(\mathfrak B\): the leading term in \(V_n^{\rm raw}/k\) is \(-4n^2\epsilon_n\cos(2nu)\); the \(\cot u\) contribution has weighted integral \(O(n\epsilon_n)\). The period average of \([-\cos(2nu)]_+\) tends to \(1/\pi\) and \(\int_0^{\pi/2}\sin u\cos u\,du=1/2\). Thus \(\mathfrak B_n\sim2n^2\epsilon_n/\pi\). For the Fisher identity, \(\int\omega_0\sin^2(2nu)=1/2\). The current total positive log variation has \(n/2\) complete periods on the half-interval, each contributing \(\log[(1+\epsilon_n)/(1-\epsilon_n)]\).

For **every** center cap,

\[
\boxed{\frac{(1-\epsilon_n)^2}{1+\epsilon_n^2/2}
\le\frac{m_n^-(\alpha)}{m_H(\alpha)}
\le\frac{(1+\epsilon_n)^2}{1+\epsilon_n^2/2}.}\tag{RC-11}
\]

Therefore \(m_n^-(\alpha)/m_H(\alpha)=1+O(n^{-3/2})\) uniformly in cap radius, while \(J_n\to0\), \(\mathfrak T_n\to0\), and \(\mathfrak B_n\to\infty\). At refinement \(h=1/n\), the *previous* sufficient target \(\mathfrak B=o(h^{-1/4})\) fails dramatically (\(\mathfrak B\asymp h^{-1/2}\)), even though the small-ball conclusion is true and the *new* current target \(\mathfrak T=o(h^{-1/4})\) holds.

This establishes that the old positive-part potential budget is not logically necessary; high-frequency environmental energy oscillations may have cancelling radial effects. It does **not** establish any current bound for the actual magnetic-deleted Penrose vacuum.

## 5. Proof-priority correction and exact measurable input

The next independent nonlinear estimate can target the conditional *first-order score current* directly:

\[
\boxed{\displaystyle
\sup_{f\in D_R}\frac4{A_f}\int_0^{\pi/2}
\frac{[-\mathbb E_{\Omega^-}[\sum_{e\in\partial f}a_e\nabla_ep_f\cdot\nabla_e\log\Omega_f^-\mid p_f=\cos u]]_+}{\sin u}\,du
=o(h^{-1/4}).}\tag{RC-12}
\]

This **suffices** for the previously stated bulk consequences, retains all collective modes, uses only first-order conditional data, and is strictly less restrictive than the earlier one-sided \([\mathcal U-E]_+\) estimate. It remains open. A still weaker one-sided log-oscillation estimate \(\mathfrak O=o(h^{-1/4})\) also suffices but directly describes the marginal rather than its conditional quantum score.

No uniform physical Yang–Mills mass gap, quartic response, nontrivial field survival or continuum reconstruction is asserted.

## 6. Verification

Run `python verify_signed_radial_current.py`. The script checks six **exact, smooth positive SU(2) class rotor ground states** and all asymptotic hierarchies, the explicit nonnegative potential, the Haar center-ball probability ratio at \(\delta=1/n\), and the exact conditional-score radial current. It is a deterministic quadrature of the explicit comparator, **not** Monte Carlo and **not** a simulation of the growing nonlinear Penrose vacuum. The original Stage7/26 datasets remain untouched.
