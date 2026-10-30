# Q14: exact block-Gibbs exponential moment for the 225 staple-disagreement loops

**27 October 2026.** This extends the historical original Q14 construction recovered from `R3_uploaded_gaussian_audit_2026_10_27_bundle.zip`. The result below is a *conditional, centered* joint frustration estimate under the **fully interacting SU(2) Wilson cavity measure**. It is not an absolute Gibbs suppression theorem; the precise remaining random variable is the compatible boundary minimum.

## Exact finite-geometry audit

Using `direct_cut_project.py`, `cavity_audit.py`, `construct_surgery.py`, and the shelling rule from `verify_bianchi.py`, the script `block_audit.py` reconstructs the authentic Q14 at spatial radii 5, 6.5, 8, 10. At each radius: 14 inserted faces, 54 Bianchi-fill faces; the fractional face cover has 40 nonzero links and total weight 22. Their complete retained link stars contain 103 distinct retained faces (49 outside the fill set). Define their nonnegative fractional incidence coefficients

`c_p = sum_{e in C intersect boundary(p)} w_e`.

The **maximum c_p is exactly 5/2** on all four volumes. Let `K` be the union of all links in those 103 star faces: **|K|=192**. The complete retained action affected by changing K consists of **255 faces**, including 152 beyond the 103 stars. Every link in K meets at most **7** of these retained plaquettes. All four counts are verified directly by `block_audit.py` and exported in `block_certificate.json`.

## Theorem (conditional nonstationary Gibbs frustration tail)

Let `U` be distributed by the actual compact-SU(2) retained Wilson Gibbs measure at coupling `lambda>=0` on an arbitrarily large rhombus-prism cavity containing the stabilized Q14 collar. Split link coordinates into the fixed `K` block, `u`, and all other links, `v`. Let

`S_K(u,v) = sum_{p in R: boundary(p) intersects K} d(W_p(u,v))`.

The action of the remaining retained faces is independent of `u`. Let `m_K(v)=min_u S_K(u,v)`. For the 40 cover links put

`m_e(U_{not e}) = min_{U_e} sum_{p in R:p contains e} d(W_p)`, `M(u,v)=sum_{e in C}w_e m_e(U_{not e})`.

The exact incidence gives the **pointwise bound**

`0<=M(u,v) <= sum_{p in 103 star faces} c_p d(W_p(u,v)) <= (5/2) S_K(u,v)`.

For the full cavity conditional Gibbs law `mu(du | v) proportional exp(-lambda S_K(u,v)) du`, and every `0<=s<=2/5`,

`E_mu[ exp(s lambda ( M - (5/2) m_K(v) )) | v] <= b^(-1) (1+lambda)^288`,

where an explicit valid constant is

`b = exp(-1) (6 pi)^(-192) (2*7*192)^(-288)`.

**Proof:** The pointwise comparison implies

`exp(-lambda S_K+s lambda M) <= exp(-(1-(5/2)s)lambda S_K) <= exp(-(1-(5/2)s)lambda m_K)`.

The SU(2) geodesic-ball lower bound, using `|K|=192` and incidence `nu<=7`, is

`Z_K(v)=int exp(-lambda S_K(u,v))du >= b(1+lambda)^(-288) exp(-lambda m_K(v))`.

Dividing gives the claimed inequality. Nothing uses stationarity, independence of exterior links, Gaussian approximation, positivity of spin-network coefficients, or an insertion partition-function ratio. Because the conditional estimate holds for every `v`, averaging yields exactly the same bound under the *actual fully interacting Gibbs measure*.

In particular, at `s=1/5`, for every `t>=0`,

`P_mu[ lambda(M-(5/2)m_K(v)) >= t ] <= min{1, b^(-1)(1+lambda)^288 exp(-t/5)}`.

The logarithmic prefactor is volume-uniform; its numerical constant is deliberately conservative.

## Absolute target and precise remaining obstruction

For an absolute tail, conditional Markov gives

`P[lambda M>=t | v] <= min{1, b^(-1)(1+lambda)^288 exp(-s t+(5/2)s lambda m_K(v))}`.

Thus an absolute joint exponential moment would follow from a **uniform Gibbs estimate on the boundary-compatible minimum**:

`sup_Lambda E_{nu_Lambda} exp((5/2)s lambda m_K(v)) <= C(1+lambda)^a`.

This new condition is not proved here. The 192-link K and its 255 affected faces are an explicit bounded local block independent of spatial cutoff, but its boundary minimum may be large for frustrated exterior holonomies. In particular the above conditional theorem does **not** imply that the 225 loops have O(1/lambda) energy in expectation. A claim to that effect would be circular.

An alternative sufficient route is a Gibbs lower bound on the probability of `lambda m_K(v)<=c log(1+lambda)` combined with the conditional centered tail; an average bound on `m_K` alone would only control an average, not a full exponential moment.

## Replication and limitations

Run `OPENBLAS_NUM_THREADS=1 python block_audit.py` from this directory. Its result is saved in `block_certificate.json`. The extraction contains the original Q14 source. Numerical geometry checks cover radii 5,6.5,8,10; extending their stabilized local incidence to **every** larger arbitrary cut-and-project cavity requires the natural assumption that the fixed local patch and star incidences persist, rather than arbitrary modifications of the boundary through K. The bounded-block theorem itself applies whenever these local incidence counts hold.
