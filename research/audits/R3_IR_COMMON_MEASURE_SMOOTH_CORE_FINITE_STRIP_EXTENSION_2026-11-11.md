# R3-IR — Common-measure and smooth-core extension for the full-Hessian finite-strip estimate

**Date:** 2026-11-11  
**Status:** conditional finite-strip semigroup proposition; common-measure compatibility and operator-domain extension audited. No theorem/claim promotion.  
**Target:** draft PR #106, branch audit/r3-ir-h2-trace-to-k-2026-11-10.  
**Scope:** finite open SU(2) strip, product radius-two bi-invariant metric, isolated dressing regime |g|≤10^-3. This is not PF-I16, the Penrose route, a 3D regulator, or a continuum Yang–Mills result.

## 1. The measure is common

Let M_E=SU(2)^E, with finite link set E, product Haar measure dHaar, and
\[
S_g(U)=\sum_{f\in F}s_g(p_f(U)),\qquad
d\mu_g=Z_g^{-1}e^{2S_g}\,d\mathrm{Haar}.
\]
The finite product M_E is compact and connected. In the isolated dressing regime, the scalar fixed-point branch s_g is smooth (indeed analytic on the certified compact plaquette range), so S_g and the density of μ_g are smooth and strictly positive.

Set
\[
V=\nabla S_g,\qquad L=\Delta+2\nabla_V.
\]
With Δ=div∇, the divergence-form identity is
\[
Lh=e^{-2S_g}\operatorname{div}(e^{2S_g}\nabla h),
\]
and therefore, for smooth scalar h,k,
\[
\langle h,Lk\rangle_{\mu_g}
=-\int_M\langle\nabla h,\nabla k\rangle\,d\mu_g.
\]
Thus the scalar generator is symmetric and nonpositive in precisely the measure used by the conditional trace estimate.

The one-link conditional measure in the trace/Poincaré record is exactly the disintegration of this same measure:
\[
d\mu_g(U_e\mid U_{\ne e})
=Z_e(U_{\ne e})^{-1}
e^{2S_g(U_e,U_{\ne e})}\,dU_e.
\]
Consequently the conditional Poincaré inequality, its conditional-mean correction, and the weighted trace estimate are all integrated against μ_g, not a Haar or a different tilted measure.

The weighted gradient Bochner estimate is also compatible with μ_g. Its pointwise weighted Bakry–Émery inequality is an identity/inequality for L and the deterministic link weights; integrating its Γ₂ identity uses the symmetric measure just displayed. The ordered third-tensor, Hessian-of-dressing, and curvature estimates are pointwise coefficient bounds, so integrating their Cauchy–Schwarz consequences against μ_g introduces no measure change.

**Common-measure verdict:** the gradient, conditional trace, full-Hessian, and forcing estimates can be placed in one and the same L²(μ_g) space. The weight w_e=(6/5)^(2d(e,S)) is deterministic, positive, and independent of U; it does not alter the measure or the conditional law.

## 2. Tensor integration by parts: drift cancellation

For a covariant tensor Q, define the drifted rough operator
\[
L^{(r)}Q=\Delta^\nabla Q+2\nabla_VQ.
\]
Since the weighted divergence is
\[
\operatorname{div}_{\mu_g}X
=\operatorname{div}X+2\langle V,X\rangle,
\]
metric compatibility gives
\[
\int_M\langle Q,\Delta^\nabla Q\rangle\,d\mu_g
=-\int_M|\nabla Q|^2\,d\mu_g
-2\int_M\langle Q,\nabla_VQ\rangle\,d\mu_g.
\]
The last term is canceled exactly by the explicit drift:
\[
\boxed{\quad
\int_M\langle Q,L^{(r)}Q\rangle\,d\mu_g
=-\int_M|\nabla Q|^2\,d\mu_g.
\quad}
\]
This is the tensor integration-by-parts identity needed when the full ordered Hessian evolution is paired with H=∇²f_t. In particular, no uncontrolled div_μ(V) term remains. It would be incorrect to integrate the rough Laplacian alone against μ_g and discard its weighted-divergence correction; the cancellation uses the full drifted rough operator.

The deterministic weights commute with covariant differentiation on the product factors. Pairing link-indexed tensors with the one-output weight therefore preserves this identity componentwise.

## 3. The common one-output energy and its differential inequality

For f_t=P_tf, ∂_t f_t=Lf_t, put
\[
G_w(t)^2=\sum_e w_e\|\nabla_ef_t\|_{L^2(\mu_g)}^2,
\qquad
H_w(t)^2=\sum_{e,d}w_e
\|\nabla_d\nabla_ef_t\|_{L^2(\mu_g)}^2.
\]
Decompose the Hessian orthogonally, in the same weighted Hilbert space, into its diagonal pure-trace component and its complement:
\[
H_w^2=T_w^2+K_w^2,\qquad
T_w^2=\frac13\sum_e w_e\|\Delta_ef_t\|_2^2.
\]
The product SU(2) curvature estimate gives damping at least 1 on the mixed and diagonal trace-free sector K_w, while the pure diagonal trace has no direct curvature damping. The conditional one-link Poincaré estimate supplies
\[
\frac{d}{dt}T_w^2
\le -2c_{\rm tr}T_w^2+2\ell G_w^2
\]
for the coercive part, with the same μ_g, where
\[
c_{\rm tr}=\frac34e^{-49\pi/144}
=0.2575101249909138\ldots,\qquad
\ell=\frac{4c_{\rm tr}}{3}\left(\frac{49}{576}\right)^2
=0.00248473592666\ldots.
\]
The weighted Bochner estimate gives, in that same measure,
\[
\frac{d}{dt}G_w^2\le-2cG_w^2,\qquad c=\frac{11}{120}.
\]

The independently audited ordered third-dressing tensor, Hessian-of-dressing block, and symmetrized SU(2) Codazzi estimates give the conditional full-Hessian inequality
\[
\frac{d}{dt}H_w^2
\le -2K_w^2-2c_{\rm tr}T_w^2
+2\ell G_w^2+2C_HH_w^2+2C_GG_wH_w,
\]
where
\[
C_H<0.030426628227,\qquad
C_G=C_3+C_R<0.110094508039.
\]
Here C_3<0.049941327 includes the drift factor and one-output weight transfer, and C_R<0.060153181039 is the symmetrized curvature forcing bound. The constants are not estimates for arbitrary plaquette complexes; they use the stated finite straight-strip incidence and local dressing certificates.

Since c_tr<1,
\[
K_w^2+c_{\rm tr}T_w^2
\ge c_{\rm tr}(K_w^2+T_w^2)=c_{\rm tr}H_w^2.
\]
Adding the gradient and Hessian inequalities therefore yields
\[
\frac{d}{dt}(G_w^2+H_w^2)
\le-2aG_w^2-2bH_w^2+2C_GG_wH_w,
\]
with
\[
a=c-\ell=0.0891819307400\ldots,\qquad
b=c_{\rm tr}-C_H>0.2270834967645.
\]
The associated symmetric matrix is
\[
Q=\begin{pmatrix}a&-C_G/2\\-C_G/2&b\end{pmatrix}.
\]
Using the conservative upper constants above,
\[
C_G<0.110094508039
<2\sqrt{ab}=0.2846172495\ldots,
\]
and
\[
\lambda_{\rm cand}
=\frac{a+b-\sqrt{(a-b)^2+C_G^2}}2
>0.0699034.
\]
Thus, **provided the ordered evolution and local coefficient hypotheses in the preceding audit are satisfied**, the differential inequality implies
\[
\boxed{\quad
G_w(t)^2+H_w(t)^2
\le e^{-2\lambda_{\rm cand}t}
\big(G_w(0)^2+H_w(0)^2\big).
\quad}
\]
This is a finite-strip reference dressed-semigroup estimate in a one-output weighted L²(μ_g) norm. The inequality does not assert a volume-uniform interacting gap or a continuum limit.

## 4. Smooth core and semigroup realization

For each fixed finite link set E, M_E is a compact smooth manifold without boundary, and e^(2S_g) is smooth and strictly positive. The operator
\[
L=e^{-2S_g}\operatorname{div}(e^{2S_g}\nabla)
\]
is a uniformly elliptic second-order operator with smooth coefficients. Its nonpositive symmetric realization on L²(μ_g) is the Friedrichs realization of the closed Dirichlet form
\[
\mathcal E(u,v)=\int_M\langle\nabla u,\nabla v\rangle\,d\mu_g,
\qquad D(\mathcal E)=H^1(M).
\]
On a compact manifold with smooth positive density, C∞(M) is an operator core; elliptic regularity identifies D(L)=H²(M). The associated P_t=e^(tL) is a strongly continuous, self-adjoint contraction semigroup, smoothing for every t>0.

For f∈C∞(M), P_tf is smooth for t≥0, so the ordered differential identities, weighted integration by parts, and energy differentiations above are classical. For f∈H²(M), choose f_n∈C∞(M) with f_n→f in H². At fixed finite E, the deterministic positive weights are bounded above and below, and the weighted G_w+H_w norm is equivalent to the usual H² seminorm modulo constants. Strong continuity of the elliptic semigroup on D(L)=H², followed by lower semicontinuity (or direct convergence in the graph norm), passes the estimate to f∈H²(M).

For merely f∈L²(μ_g), smoothing gives P_sf∈H²(M) for every s>0, and hence
\[
G_w(t)^2+H_w(t)^2
\le e^{-2\lambda_{\rm cand}(t-s)}
\big(G_w(s)^2+H_w(s)^2\big),
\qquad t\ge s>0.
\]
No finite bound in terms of the initial L² norm alone is claimed at s=0. Constants lie in the kernel and are invisible to G_w,H_w; no mean-zero condition is needed for this derivative-seminorm contraction.

The decay rate is independent of the number of links **if** the stated local incidence and scalar dressing constants are uniform. Equivalence constants between weighted and unweighted Sobolev norms need not be uniform in strip length; the result is intentionally stated in the weighted norm.

## 5. Finite-strip resolvent consequence and its scope

For fixed finite E, compactness, connectedness, and uniform ellipticity imply that the kernel of L consists of constants and that the centered inverse
\[
R=(-L)^{-1}Q,\qquad Qh=h-\mu_g(h),
\]
is well-defined on centered L²(μ_g). If q∈H²(M), then the semigroup representation and the contraction above give
\[
\left(
\|\nabla Rq\|_{w,2}^2+
\|\nabla^2Rq\|_{w,2}^2
\right)^{1/2}
\le\frac1{\lambda_{\rm cand}}
\left(
\|\nabla q\|_{w,2}^2+
\|\nabla^2q\|_{w,2}^2
\right)^{1/2}.
\]
This resolvent corollary requires H² regularity of the source. It is not the earlier H¹-source Hessian resolvent estimate, and it does not replace or strengthen that separate result without an additional smoothing/duality argument. The existence of the finite-strip inverse here uses compact ellipticity; this paragraph does not supply a strip-length-uniform scalar L² spectral gap.

## 6. Audit verdict and remaining gates

**Verified at the level of compatibility and functional analysis, conditional on the cited coefficient audits:**

1. The conditional link laws are disintegrations of the same Gibbs measure μ_g that symmetrizes L.
2. The weighted gradient Bochner inequality, conditional trace/Poincaré inequality, and pointwise Hessian forcing bounds can all be integrated in L²(μ_g).
3. The drifted rough tensor operator has the required weighted integration-by-parts cancellation; no stray divergence term is omitted.
4. On each fixed finite strip, C∞ is a core, D(L)=H², and the smooth differential estimate extends to H² initial data and to positive-time smoothing from L².
5. The conservative candidate matrix has positive margin λ_cand>0.0699034.

**Still conditional / open:**

- The full ordered Hessian evolution, local third-tensor certificate, A=∇²S_g block bounds, and symmetrized SU(2) curvature contraction remain subject to the explicit hypotheses and conventions in the preceding 2026-11-11 audit; this document does not independently rederive those local geometric estimates.
- The conditional one-link Poincaré coefficient is a finite-strip bound under the isolated-dressing hypotheses; it is not a physical-coupling, volume-uniform interacting spectral gap.
- No nonlinear interacting fixed point, pointwise interacting Hessian bound, volume-uniform residual response, physical-coupling gap, 3D transfer, or continuum mass gap is proved.
- The provisional three-sector trace-to-K calculation remains paused and is not used.

**Decision:** this closes the common-measure and smooth-core/semigroup-extension audit for the *conditional finite-strip reference estimate*. It supports a conditional finite-strip semigroup proposition, not a promoted theorem or claim. Keep PR #106 draft and main unchanged.
