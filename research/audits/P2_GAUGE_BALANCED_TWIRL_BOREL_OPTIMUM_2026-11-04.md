# P2: Gauge-balanced invariant intertwiners and optimization of the local Borel majorant

**2026-11-04.** Exact finite-strip SU(2) residual-gauge twirl theorem for every even history width, and exact optimization of the *previously derived* formal Borel-radius guarantee. Full expanded report, two independent executable exact verifiers, logs and SHA-256 manifest: accompanying conversation archive \`p2_gauge_balanced_borel_radius_2026-11-04.zip\`. These are **not** physical same-grade no-go, analytic continuation of the actual Borel transform, interacting vacuum, or a 4D continuum mass-gap theorem.

## 1. The earlier extremal matrix no-go has zero Gauss projection

With the corrected original-link electric operator represented in face holonomies, the earlier matrix-space same-grade obstruction used \(u(U)=U_{21}\) and \(\prod_i u(U_i)\). Under residual gauge conjugation by \(h_\theta=\operatorname{diag}(e^{i\theta/2},e^{-i\theta/2})\),
\[
u(h_\theta Uh_\theta^{-1})=e^{-i\theta}u(U).
\]
Thus \(\prod_{i=1}^N u(U_i)\) has torus weight \(-N\ne0\) and its **SU(2) gauge twirl is exactly zero** for all N≥1. The high-spin singleton \(u(U_j)^m\) also has zero Gauss projection. Projecting *each previous input* cannot produce a counterexample on the physical invariant subspace. Averaging their product instead of their separate inputs is not the gauge-invariant bilinear problem.

## 2. All even widths: a genuine invariant intertwined seed with no trace-nuclear loss

Let N=2k≥2. On \(V_N=(\mathbb C^2)^{\otimes N}\), define alternating computational states
\[
v=|+,-,+,-,\ldots,+,-\rangle,\quad
w=|-,+,-,+,\ldots,-,+\rangle,\quad X_N=|v\rangle\langle w|.
\]
The trace-expansion coefficient \(X_N\) represents an alternating product of \(U_{21}\) and \(U_{12}\) on N faces. It has \(\|X_N\|_{S_1}=1\). Define residual SU(2) Gauss averaging of the **coefficient** by
\[
\mathcal T_N(X)=\int_{SU(2)}g^{\otimes N}X(g^\dagger)^{\otimes N}\,dg.
\]
**Exact theorem (all even N):**
\[
\boxed{\|\mathcal T_N(X_N)\|_{S_1}=1.}
\]
The resulting function is invariant under simultaneous conjugation and remains entirely in face multidegree \((1,\ldots,1)\), so for every \(\sigma\ge0\) the dimension-weighted projective norm is retained **exactly**:
\[
P_\sigma(\mathcal T_N f_N)=P_\sigma(f_N)=2^N e^{\sigma N}.
\]

**Proof.** Under diagonal SU(2), decompose \(V_N=\bigoplus_{j=0}^k V_j\otimes M_j\) with integer total spin j. Both v,w have total magnetic quantum number zero, hence \(v=\bigoplus_j|j,0\rangle\otimes v_j\), \(w=\bigoplus_j|j,0\rangle\otimes w_j\). A common π rotation flips every spin and takes v to w up to a phase; in each fixed j, it acts on \(|j,0\rangle\) by a phase \(\zeta_j\) of modulus one, so \(w_j=\zeta_jv_j\). Schur averaging gives \(\mathcal T_N X_N=\bigoplus_j [I_{2j+1}/(2j+1)]\otimes |v_j\rangle\langle w_j|\). Its trace norm is \(\sum_j\|v_j\|\|w_j\|=\sum_j\|v_j\|^2=1\). QED. The proof is analytic and all-width; finite tests are independent regressions.

**Explicit two-face identity.** With \(A=a_0 I+i\sum_i a_i\sigma_i\), \(B=b_0 I+i\sum_i b_i\sigma_i\), twirling \(U_{21}(A)U_{12}(B)\) over SO(3) rotates the quaternion-vector components and yields
\[
\boxed{\mathcal T_2[U_{21}(A)U_{12}(B)]
=-\tfrac23\mathbf a\cdot\mathbf b
=\tfrac13\chi_1(AB)-\tfrac16\chi_1(A)\chi_1(B).}
\]
The Fourier matrix is \(P_{\rm swap}/3-I_4/6\), with eigenvalues \(1/6\) (multiplicity 3) and \(-1/2\) (multiplicity 1), giving nuclear norm exactly 1.

**Multiplicity check.** For even N, the squared projection of v onto total spin j is \(p_j=\mu_j/\binom N{N/2}\), where \(\mu_j=\binom N{N/2-j}-\binom N{N/2-j-1}\) (out-of-range term zero). The exact verifier forms the \(J^2\) matrix on the \(J_z=0\) sector, checks every spectral projector and spin-flip phase for N=2,4,6, and checks the integer multiplicity identity through N=200.

**Limit:** no physical same-grade bilinear divergence is claimed. One must test \(\mathcal B_{\rm hist}(\mathcal T_N f_N,G)\) with **separately gauge-invariant** high-spin inner inputs and the complete corrected original-link inverse.

## 3. The previous certified Borel radius is optimally tuned in κ

The previously derived direct graded history estimate and fundamental-source spin-order cap gave a local Borel radius guarantee
\[
R_{\rm cert}(t,\sigma)=\frac{3t e^{-\sigma}}{4K(t)},\
t=e^{-\kappa}\in(0,1),\
K(t)=2C(t)+192t,
\]
where
\[
C(t)=\frac8{1-t}+\frac{24t}{(1-t)^2}+4\sqrt t H(t),\
H(t)=\sup_{m\ge1}(2+6m)t^{m/2}.
\]
Since the m=1 term gives \(H(t)\ge8\sqrt t\), the guaranteed radius satisfies
\[
e^\sigma R_{\rm cert}(t,\sigma)\le r_0(t)
=\frac{3t(1-t)^2}{64(16t^3-32t^2+18t+1)}.
\]
The exact derivative
\[
r_0'(t)=\frac{3(t-1)(t+1)(4t-1)}
{64(16t^3-32t^2+18t+1)^2}
\]
is positive for t<1/4 and negative for t>1/4. At t=1/4, \(H(t)=4\) (achieved at m=1), so the bound is **attained**. Consequently
\[
\boxed{\sup_{\kappa>0}R_{\rm cert}(e^{-\kappa},\sigma)
=\frac9{5120}e^{-\sigma},\quad\kappa_{\rm optimum}=\log4.}
\]
This is an optimality statement **only for this particular certified norm-majorant with fixed operator constants**. It is **not an upper bound** for the actual Borel radius; sharpening the estimates could improve the guarantee.

## 4. The Gevrey norm bound alone cannot determine Borel continuation

Fix positive M,K and a unit vector v in any complex Banach space. Coefficients \(c_n^{(\phi)}=M^nK^{n-1}(n-1)!\,e^{-i(n-1)\phi}v\) obey the same Gevrey-1 majorant as the formal score. Their Borel transform is
\[
\widehat c_\phi(\xi)
=-\frac{e^{i\phi}}K v\log(1-MK e^{-i\phi}\xi),
\]
with a logarithmic singularity at \(\xi=e^{i\phi}/(MK)\). Choosing \(\phi=0\) places it on the positive ray. By contrast \(c_n=M^nK^{n-1}v\) is bounded by the same majorant but has the **entire** Borel transform \((e^{MK\xi}-1)v/K\). These are *logical comparison sequences*, **not** solutions of the actual SU(2) score recurrence. The coefficient bound alone neither proves nor rules out the required ray continuation/Laplace growth.

## Independent verification, research boundary

The companion archive includes two standalone verifiers with passing logs and file hashes. The first checks 24 exact signed-rotation matrices for the two-face Haar twirl, zero-torus-weight selection, exact symbolic radius derivative/maximum, and Borel comparison coefficient bounds. The second constructs total-spin \(J^2\) and spectral projectors for N=2,4,6, checks the twirled matrix nuclear decomposition exactly, and verifies 100 all-even-width SU(2) multiplicity formulas through N=200. All checks passed; ZIP integrity and SHA-256 manifest passed.

**Next:** true gauge-invariant high-spin *Poisson response* of the new balanced intertwined seeds (not just their input norms), then independent study of the **actual** Borel transform via analytic continuation or a Borel-plane nonlinear equation. No λ=1 interacting-vacuum or 4D continuum mass-gap result follows.