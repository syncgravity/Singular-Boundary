# The Singular Boundary — Exact regional vacuum exponential tilt and a nonlinear spectral-survival stress test

**Date:** 2026-10-28. **Branch:** `audit/2026-10-28-independent-reconstruction`. **Model scope:** exact finite Hamiltonian theorems for true SU(2) interacting ground states. Refinement estimates use the separately declared Penrose spatial coefficient and full-collar assumptions, **not** a source-verified Stage7/26 identity. The disconnected-plaquette family below is a separate nonlinear Wilson counterexample to an *inference from spectral moments*, not an example of the connected Penrose system. No mass gap or nontrivial continuum is proved.

## 1. Model and upstream dependencies

Work on a finite face-complete rhombus SU(2) link system with full vertex Gauss invariance. Each face has four distinct incident links, and each link is in at most two selected faces. Set

\[
H=\sum_e a_e(-\Delta_e)+\sum_f b_f(1-p_f),\quad p_f=\tfrac12\operatorname{ReTr}W_f,\quad d_f=1-p_f\in[0,2],\quad a_e\le a_*=a_{\max}.
\]

For a face set D, let S comprise its incident links, let C(D) comprise exterior faces sharing a link with S, and define H_out by deleting all S electric terms and magnetic terms on D∪C(D). Write E_out=inf spec(H_out), E0=inf spec(H), Delta_D=E0−E_out≥0, and assume b_f≥b_*>0 for f∈D. Let Ω>0 be the exact normalized full-link ground state, ν=Ω²dHaar, and X=Σ_{f∈D}d_f. The vacuum is gauge invariant. On each face, the exact Casimir gives

\[
|\nabla_e p_f|²=(1-p_f²)/4\le d_f/2,\quad
\Gamma(X)=\sum_e a_e|\nabla_e X|²\le4a_* X.
\]

The cut form comparison is

\[
H-E_0\ge b_*X-\Delta_D\quad\text{as quadratic forms}.
\]

These are earlier verified ER-1/AG-1 inputs. The exact vacuum IMS identity for any real smooth or Lipschitz multiplier f is

\[
\langle f\Omega,(H-E_0)f\Omega\rangle=\mathbb E_\nu\Gamma(f).
\]

## 2. Theorem RT-1 — An exact, sharp-threshold regional Laplace-transform bound

**Theorem.** For every finite Hamiltonian as above, and every real s satisfying 0≤s<√(b_*/a_*),

\[
\boxed{\mathbb E_\nu[e^{sX}]\le
\exp\left[\frac{\Delta_D}{\sqrt{a_*b_*}}\operatorname{artanh}\!\left(s\sqrt{\frac{a_*}{b_*}}\right)\right].}\tag{RT-1}
\]

**Proof.** On the finite compact link configuration space, f_s=e^{sX/2} is a smooth bounded positive multiplier. The form barrier and exact ground-state identity imply

\[
b_*\mathbb E[Xe^{sX}]-\Delta_D\mathbb E[e^{sX}]
\le\mathbb E\Gamma(e^{sX/2})
=\frac{s²}{4}\mathbb E[e^{sX}\Gamma(X)]
\le a_*s²\mathbb E[Xe^{sX}].
\]

Writing M(s)=E e^{sX} and M'(s)=E Xe^{sX}, rearrange to

\[(b_*-a_*s²)\frac{d}{ds}\log M(s)\le\Delta_D.\]

Integrating from 0, where M(0)=1, gives exactly RT-1. No cutoff approximation, independent plaquette factorization, curvature Hessian, spectral gap or Gaussian trial is used. The formula is a one-sided upper Laplace bound; it does **not** bound a centered moment-generating function.

## 3. Corollary RT-2 — Exponential exclusion above the *actual regional energy-budget scale*

Assume a fixed physical interior Penrose face region D_R with a complete collar, b_*≥β/h², a_e≤a_*, and Delta_D≤C_E/h³, with β,a_*,C_E positive constants independent of h. Put Z_h=h X, R=C_E/β and k=√(a_*/β). For every 0≤λ<1/k, substitute s=λ/h into RT-1 to obtain

\[
\boxed{\mathbb E e^{\lambda Z_h/h²}
\le\exp\left[\frac{R}{k h²}\operatorname{artanh}(k\lambda)\right].}\tag{RT-2}
\]

For every δ>0 and such λ, Chernoff yields

\[
\boxed{\nu_h(Z_h\ge R+\delta)\le
\exp\left\{-h^{-2}\left[\lambda(R+\delta)-\frac Rk\operatorname{artanh}(k\lambda)\right]\right\}.}\tag{RT-3}
\]

Since (artanh(kλ))/k=λ+O(λ³), choose any sufficiently small fixed λ=λ_δ>0 with

\[
\lambda_\delta\delta>\frac Rk[\operatorname{artanh}(k\lambda_\delta)-k\lambda_\delta].
\]

Then there exists c_δ>0 for which

\[
\boxed{\nu_h(Z_h\ge R+\delta)\le e^{-c_\delta/h²}.}\tag{RT-4}
\]

An explicit choice when R>0 is λδ=min{1/(2k),sqrt[9δ/(8Rk²)]}; since artanh(t)−t≤4t³/9 for t≤1/2, the bracket in RT-3 is at least λδ δ/2. If R=0, any 0<λδ<1/k works.

This tail threshold R is the regional **relative energy budget** Delta_D/b_* translated into Z units. The earlier AG-1 cutoff proof required an upper threshold 2L with L≥2Delta_D/b_*, i.e. at least 4R at the same declared budget. RT-4 sharpens that *upper tail threshold* to R+δ and gives an exponential h^-2 rate. It does **not** show the mean Z_h is near R, or that Z_h concentrates in a small neighborhood, or that the centered signed Wilson source variance vanishes. The true value Delta_D may be much smaller than its available upper bound C_E h^-3.

A separate direct moment recursion, valid for every integer k≥1, follows from the same form barrier with f=X^{k/2}:

\[
\boxed{b_*\mathbb E X^{k+1}\le\Delta_D\mathbb E X^k +a_* k²\mathbb E X^{k-1}.}\tag{RT-5}
\]

For b_*=β/h², after multiplying by h powers,

\[
\boxed{\mathbb E Z_h^{k+1}\le (h³\Delta_D/\beta)\mathbb E Z_h^k +(a_*k²/\beta)h^4\mathbb E Z_h^{k-1}.}\tag{RT-6}
\]

The nonnegative face sum is allowed to vanish; sqrt powers are approximated by smooth positive regularizations and controlled using Γ(X)≤4a_*X. These exact inequalities apply to the actual connected Penrose Hamiltonian under the stated hypotheses, independently of its unknown source covariance.

## 4. Theorem RT-3 — Exact SU(2) *nonlinear* one-plaquette strong-magnetic moment hierarchy

Now take a **separate** one-face SU(2) Wilson system with four electric links of coefficient a>0 and magnetic coefficient b>0. Its *gauge-invariant physical class-function operator* in p=(1/2)TrW is

\[H_{a,b}=-a(1-p²)\partial_p²+3ap\partial_p+b(1-p),\qquad\rho_0(p)=\frac2\pi\sqrt{1-p²}.\]

Its unique normalized positive ground state Ω_{a,b}, energy E0, and ν=ρ0 Ω² dp are *interacting* for b>0. A product-link variational trial gives E0≤3√(2ab). With d=1−p,

\[\Gamma(d)=a(1-p²)\le2ad,\qquad\Gamma(\sqrt d)=\frac a4(1+p)\le a/2.\]

For M_k=E d^k, M0=1, M1≤E0/b≤3√(2a/b). The exact barrier+IMS test f=d^{k/2} gives for k≥1,

\[\boxed{bM_{k+1}\le E0M_k+\frac{k² a}{2}M_{k-1}.}\tag{RT-7}\]

Thus for r=√(a/b), M_k≤C_k r^k with C0=1, C1=3√2, and C_{k+1}=3√2 C_k+(k²/2)C_{k-1}. In particular,

\[\boxed{E d²\le\frac{37a}{2b},\qquad \operatorname{Var}(d)\le\frac{37a}{2b}.}\tag{RT-8}\]

This yields an exact nonlinear Wilson strong-field *second moment* of order h² for b=β/h², without a Gaussian approximation or invoking prior AG-1.

A weighted local Fisher test with f=√d supplies

\[\mathbb E[dT]\le2E0\mathbb E d+4\mathbb E\Gamma(\sqrt d)\le38a,\qquad T=\sum_{e\in\partial f}a|\nabla_e\log\Omega|².\tag{RT-9}\]

Writing \(\mathcal L d=D+F\) with D=3ap and F=2Σ_ea∇_e logΩ·∇_e d, Cauchy yields E F²≤8a E[dT]≤304a², hence the *physical* second energy moment

\[\boxed{m_2(d)=\mathbb E[(\mathcal L d)²]\le626a².}\tag{RT-10}\]

For b≥72a, E p≥1/2. Stationarity and |E F|²≤4(E T)m1(d), E T≤E0, imply the independent first spectral moment lower bound

\[\boxed{\frac3{16\sqrt2}\frac{a^{3/2}}{\sqrt b}\le m_1(d)=a\mathbb E(1-p²)\le6\sqrt2\frac{a^{3/2}}{\sqrt b}.}\tag{RT-11}\]

Spectral Cauchy m1²≤Var(d)m2 and RT-8/RT-10 give the **matching exact variance order**

\[\boxed{\frac{9}{512\cdot626}\frac a b\le\operatorname{Var}_{\nu}(d)\le\frac{37}{2}\frac a b}\quad(b\ge72a).\tag{RT-12}
\]

All constants are intentionally conservative, and this is a rigorous theorem for the nonlinear one-face Wilson Hamiltonian.

## 5. Theorem RT-4 — Exact one-face third f-sum, matching the connected-model spectral scaling

For the same one-face physical class representation let T_a=−a[(1−p²)∂²−3p∂], C=[H,d]=−3ap+2a(1−p²)∂. The exact second commutator separates as

\[[C,[T_a,C]]=−6a³(5p²+1)+\rho_0^{-1}\partial_p[8a³\rho_0(1−p^4)\partial_p],\]

and the magnetic part is \([C,[b d,C]]=−8a²b p(1−p²)\). Consequently, with the *actual* interacting ground state Ω,

\[
\boxed{m_3^T(d)=3a³\mathbb E(5p²+1)+4a³\int\rho_0(1−p^4)(\Omega')²dp,}\tag{RT-13}
\]

\[\boxed{m_3^V(d)=4a² b\mathbb E[p(1−p²)].}\tag{RT-14}
\]

Since 1−p^4≤2(1−p²), E T≤E0, and E(1−p²)≤2E d≤2E0/b,

\[\boxed{0\le m_3(d)\le18a³+16a² E0\le18a³+48\sqrt2\,a^{5/2}\sqrt b.}\tag{RT-15}
\]

Thus b=β/h² gives m1(d)=Θ(h), m2(d)=O(1), m3(d)=O(h^-1) and Var(d)=Θ(h²), all for a **true interacting SU(2) ground state**, not Gaussian tangent dynamics.

## 6. Theorem RT-5 — Nonlinear Wilson ultraviolet-source escape on separated plaquettes

Take F_h independent, spatially separated Penrose-shaped rhombi, with F_h h²→A>0, each carrying its own physical one-face Hamiltonian H_{a,b} with b=β/h². The union is **not** the connected face-complete Penrose disk: there are no shared magnetic links or exterior couplings among components. The full Hamiltonian is a genuine finite SU(2) Wilson sum, its full Gauss projector factorizes, and its unique vacuum is the tensor product of the exact nonlinear one-plaquette vacua. For the centered gauge-invariant source

\[A_h=\sqrt h\sum_{j=1}^{F_h}(d_j-\mathbb E d_j),\]

all positive spectral moments are additive because each one-face excited state is orthogonal to its local vacuum. In particular,

\[\begin{aligned}
\boxed{\operatorname{Var}(A_h)=\Theta(h),}\qquad
\boxed{m_1(A_h)=\Theta(1),}\\
\boxed{m_2(A_h)=O(h^{-1}),}\qquad
\boxed{m_3(A_h)=O(h^{-2}).}
\end{aligned}\tag{RT-16}
\]

For **every fixed physical time** t≥0, positivity of the physical heat semigroup gives

\[0\le\langle A_h\Omega_h,e^{-tK_h}A_h\Omega_h\rangle\le\operatorname{Var}(A_h)=O(h)\to0.\tag{RT-17}\]

Meanwhile the first spectral moment stays bounded away from zero, so for every fixed physical energy cutoff Λ,

\[\boxed{\int_{(0,\Lambda]}E\,d\mu_h(E)\le\Lambda\operatorname{Var}(A_h)=O_\Lambda(h)\to0.}\tag{RT-18}
\]

This is a fully **nonlinear Wilson** demonstration that all the existing positive first/second/third spectral-moment scales, plus strong curvature control, can coexist with complete disappearance of the critically normalized source at fixed Euclidean times. It does **not** prove that the connected Penrose Hamiltonian behaves this way, and does **not** establish any regulator-uniform gap for this disconnected comparator. It refutes only the inference from the existing budgets to a fixed-time lower correlator.

## 7. Consequences, unresolved obligations, provenance

**New exact result on the actual connected finite SU(2) model:** RT-1/RT-4, a sharper exponential tail above the regional energy-budget cap, and the exact moment recursion RT-5/RT-6. This improves the threshold in the previous regional Agmon estimate without assuming a gap or source connected covariance.

**New exact nonlinear comparator:** strong-magnetic one-face moment hierarchy and bounded second moment RT-7 through RT-15; a product of independently gauged Wilson plaquettes has the same established moment orders as the proposed critically normalized connected-Penrose source, but its fixed-time correlator vanishes. It is not the connected Penrose vacuum and should not be promoted to it.

**Open:** actual connected-Penrose Wilson-source variance upper/lower classification; fixed-physical-time two-point survival (which may fail); physical full-sector regulator-uniform mass gap; nonlinear quartic resolvents; R2 continuum; original Stage 7/26 source provenance and temporal Q14 correspondence.

**Revised next independent proof task:** a genuinely *shared-edge* nonlinear comparison or conditional covariance/infrared spectral estimate; positive first and third moments or general regional exponential tails are insufficient. A lower fixed-time response would be one possible outcome for the selected source but is not a necessary mass-gap condition. In particular, all current sharp-threshold tails constrain total curvature, not its centered, source-weighted fluctuations.

**Verification:** `verify_regional_exponential_mgf.py` checks exact coefficient/rate algebra, exact SU(2) one-face commutator, rigorous moment bounds, the three-face Penrose **spatial** incidence and deterministic character-basis evaluations. There is no Monte Carlo and no modification of historical original files.