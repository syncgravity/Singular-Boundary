# Penrose-specific collar coercivity: a deterministic good-boundary theorem, a genuine local Peierls estimate, and the unresolved full exterior law

**Date:** 2026-10-27. **Model:** actual SU(2) Wilson measure on direct-\(\mathbb Z^5\) Penrose rhombus spatial disks extruded through three periodic temporal intervals. All face words are exact nonabelian oriented holonomies. **Status:** the requested coercivity has been proved on an explicitly stated, nontrivial, gauge-invariant class of exterior boundary fields; a genuine *unconditional* exponential Gibbs suppression is proved for one specified obstructing exterior center defect. The full absolute tail for every configuration with large \(s_H\), the arbitrary-support R3 theorem, and the continuum mass gap remain **unproved**.

## 1. Precise setup and geometry

Write \(d(g)=1-\tfrac12\mathrm{Tr}(g)\in[0,2]\), normalized Haar on every SU(2) link, and
\[
 d\mu_{R,\lambda}(U)=Z_R^{-1}e^{-\lambda S_R(U)}\prod_{e}dU_e,\qquad S_R=\sum_{p\in R}d(W_p).
\]
For an adjustable link set \(J\), let \(A(J)=\{p\in R:\partial p\cap J\ne\emptyset\}\) and
\[
 s_J(U_{J^c})=\min_{u_J\in SU(2)^J}\sum_{p\in A(J)}d(W_p(u_J,U_{J^c})).
\]

For the 14-face overlapping temporal insertion \(Q\) from the original direct-Z5 anchor, let \(H\) consist of its 36 boundary links and \(K\) consist of \(H\) plus every link in a retained face touching \(H\). Exact canonical Z5 labels fix the same local geometry at spatial radii 5, 6.5, 8, 10:

- \(|Q|=14,\ |H|=36,\ |K|=125\).
- \(A(K)\) contains exactly **175 retained faces**.
- The exterior halo \(\partial A(K)\setminus K\) contains exactly **133 links** and has 87 endpoint vertices.
- Each quadrilateral has four links and maximum retained link-face incidence \(\nu\le7\).

The counts and face identities are machine-checked in `audit.py` and `verify_coercivity.py` against the actual oriented Penrose-prism construction; no abstract square-grid replacement is used.

## 2. Theorem A: explicit gauge-invariant good-boundary coercivity with \(\alpha=1\)

For \(0<\varepsilon\le1\) and \(\lambda\ge1\), define the **exterior good-halo event** \(G_{\varepsilon,\lambda}(K)\) as follows. There exist SU(2) vertex gauges \(g_v\) for vertices touched by the faces of \(A(K)\) such that, for **every exterior link** \(e\in\partial A(K)\setminus K\) (oriented from \(v\) to \(w\)),
\[
 \operatorname{dist}\big(U_e,g_vg_w^{-1}\big)\le \varepsilon\lambda^{-1/2}.
\]
Here `dist` is the bi-invariant geodesic angle on SU(2)=S³. This criterion is invariant under ordinary lattice gauge transformations. It imposes **no restriction on any link in K** and no restriction on distant exterior links that do not touch \(A(K)\).

**Theorem:** on this local boundary class,
\[
 \boxed{s_K(U_{K^c})\le \frac{8\varepsilon^2|A(K)|}{\lambda}.}
\]
**Proof:** choose the trial links \(U_{e}=g_vg_w^{-1}\) on all \(e\in K\). Conjugate every affected plaquette by its basepoint gauge. Every link factor is identity if it was in K; every remaining exterior factor has angle at most \(\varepsilon/\sqrt\lambda\). As each face has no more than four factors, the product angle is at most \(4\varepsilon/\sqrt\lambda\). The inequality \(d(W)\le\operatorname{dist}(W,I)^2/2\) gives at most \(8\varepsilon^2/\lambda\) per affected face. Minimize over K to conclude. **The trial is nonabelian and gauge covariant**, and no distant retained action enters the calculation.

Taking \(\varepsilon=1/4\) and the verified counts gives
\[
 \boxed{s_K\le\frac{87.5}{\lambda}=\frac{6.25|Q|}{\lambda}.}
\]
Because \(s_H\ge0\), this establishes the user's requested deterministic inequality **on this explicit exterior boundary class**:
\[
 \boxed{s_K\le (1-\alpha)s_H+6.25|Q|/\lambda,\qquad\alpha=1.}
\]

**Arbitrary bounded-degree Penrose prism Q:** for any insertion support of size \(q\), using \(H=\bigcup_{p\in Q}\partial p\), \(|H|\le4q\). The one-retained-face collar has \(|K|\le(1+3\nu)|H|\le88q\), and \(|A(K)|\le\nu|K|\le616q\) for \(\nu\le7\). On the corresponding local gauge-near-flat exterior class with \(\varepsilon=1/4\),
\[
 \boxed{s_K\le 308q/\lambda,\quad\alpha=1,\quad |K|\le88q.}
\]
Thus this is **not limited to the selected 14-face example** as a deterministic good-class theorem. The universal coefficients are much less sharp than the verified case.

## 3. Corollary: fully rigorous *joint* Peierls tail under the actual SU(2) Gibbs measure

Reuse the explicit finite SU(2) covering-net surgery \(T_\lambda\) from the preceding verified work, acting only on K, with exact unit branchwise Haar Jacobian and inverse multiplicity at most \((4097\lambda^{3/2})^{|K|}\). Its full-retained-action decrease obeys
\[
 \lambda[S_R(U)-S_R(T_\lambda U)]\ge\lambda[s_H-s_K]-2\nu|K|.
\]
On \(G_{\varepsilon,\lambda}(K)\cap\{\lambda s_H\ge t\}\), Theorem A gives a decrease of at least \(t-8\varepsilon^2|A(K)|-2\nu|K|\). Changing variables separately on the finite Haar-translation branches gives the **unconditional-in-ambient-volume joint-event bound**
\[
 \boxed{\mu_{R,\lambda}\{\lambda s_H\ge t,\ G_{\varepsilon,\lambda}(K)\}
 \le\min\{1,\exp[-t+8\varepsilon^2|A(K)|+|K|(\tfrac32\log\lambda+\log4097+2\nu)]\}.}
\]
For the actual Q14 Penrose collar and \(\varepsilon=1/4\):
\[
 \boxed{\mu_{R,\lambda}\{\lambda s_H\ge t,G\}
 \le\min\{1,\exp[-t+187.5\log\lambda+2877.251284694]\}.}
\]
For arbitrary Penrose prism insertion Q and the same \(\varepsilon\), its size bound becomes
\[
 \boxed{\mu_{R,\lambda}\{\lambda s_H\ge t,G\}\le
 \min\{1,\exp[-t+132q\log\lambda+2271.985q]\}.}
\]
This is a *valid Peierls tail for the large-frustration AND good-halo event*, not an unconditional tail for \(s_H\). In particular,
\[
 \mu_{R,\lambda}\{\lambda s_H\ge t\}\le\text{[displayed joint tail]}+\mu_{R,\lambda}(G^c),
\]
and **no adequate control of \(\mu(G^c)\) has been proved**. Since the radius defining G is a fixed multiple of the natural \(\lambda^{-1/2}\) fluctuation scale, its complement need not even vanish as \(\lambda\to\infty\); simple one-plaquette Gaussian scaling shows why a blanket \(o(1)\) claim would be unjustified. Thus the full requested absolute tail does **not** follow from Theorem A.

### Corollary: a genuine volume-uniform **restricted** retained-energy estimate

Because \(G_{\varepsilon,\lambda}(K)\) depends only on links outside K, and \(H\subset K\), it is measurable with respect to the exterior conditioning for the H-link heat bath. The previously proved conditional compact-Haar estimate gives
\[
 \lambda\mathbf E[(S_H-s_H)\mathbf1_G]\le |H|\bigl(\tfrac32\log\lambda+C_7\bigr),\qquad C_7=16.453360405.
\]
Integrating the proved *joint* tail gives
\[
 \lambda\mathbf E[s_H\mathbf1_G]\le8\varepsilon^2|A(K)|+|K|(\tfrac32\log\lambda+\log4097+14)+1.
\]
For the genuine Penrose Q14 collar with \(\varepsilon=1/4\), these combine to
\[
 \boxed{\lambda\mathbf E_{\mu_R}\left[\mathbf1_G\sum_{p\in A(H)}d(W_p)\right]
 \le241.5\log\lambda+3470.573\qquad(\lambda\ge1).}
\]
This is **unconditional as an estimate of the contribution of G to the true Gibbs expectation**, but it is *not* a bound for the complete expectation: the complementary contribution \(\mathbf E[S_H\mathbf1_{G^c}]\) is uncontrolled. It also does not imply a bound on \(\mathbf E[S_H\mid G]\) without a lower bound on \(\mu_R(G)\).

## 4. The good-boundary class is nontrivial: an exact obstructing Penrose mode

On the radius-5 patch, take spatial time-0 link \(e=19\) with Z5 endpoints
\[
 (-2,-1,0,0,-1),\quad (-1,-1,0,0,-1).
\]
It belongs to \(K\setminus H\) and is incident on exactly four **retained** faces. Two of these are temporal faces `229` and `264`, with original nonabelian words
\[
 W_{229}=U_{19}\,T_{512}\,U_{178}^{-1}\,T_{484}^{-1},\qquad
 W_{264}=U_{54}\,T_{512}\,U_{213}^{-1}\,T_{503}^{-1}.
\]
The only H-link in either word is the shared \(T_{512}\). Set every other link to identity and set \(U_{19}=-I\). Then for **every** allowed assignment of all 36 H-links,
\[
 d(W_{229})+d(W_{264})=d(-T_{512})+d(T_{512})=2.
\]
Therefore \(\boxed{s_H\ge2}\) for this explicit exterior configuration. Yet all links outside K are pure gauge (identity), so \(s_K=0\). Thus the proved coercivity on G includes genuinely large-frustration configurations, not only those with \(s_H=0\). The pair of face words and the transported Z5 edge endpoints are the same across radii 5, 6.5, 8, 10 (the numeric edge/face indices change). `nonabelian_witness.py` independently Tietze-eliminates 35 local face/link relators and obtains the residual exact word \(U_{19}=1\) from the two specified relators, verifying the nonabelian obstruction.

## 5. A genuinely unconditional Penrose Peierls estimate for one specified severe exterior defect

Fix \(0<\delta<\pi/8\). Define \(D_\delta\) as the local event that \(U_e\) is within geodesic angle \(\delta\) of \(-I\), and each of the 12 other links belonging to the four retained faces incident on e is within angle \(\delta\) of \(I\). This event depends on only **13 physical links** and is nonempty and open; its definition and size are identical by Z5 labels in all four nested patches. Its faces have noncommuting SU(2) words, but since \(-I\) is central, all four plaquette holonomies are within angle \(4\delta\) of \(-I\), giving \(\tfrac12\operatorname{Tr}W_p\le-\cos(4\delta)\).

The single-link center-flip \(T_e:U_e\mapsto -U_e\) preserves normalized Haar measure **bijectively** and changes every affected retained face by a central sign; all other retained faces are exactly invariant. The full retained-action decrease therefore obeys
\[
 S_R(U)-S_R(T_eU)=-2\sum_{p\ni e,\ p\in R}\tfrac12\operatorname{Tr}W_p
 \ge8\cos(4\delta),\quad U\in D_\delta.
\]
This gives the **unconditional, ambient-volume-independent Gibbs Peierls estimate**
\[
 \boxed{\mu_{R,\lambda}(D_\delta)\le\exp[-8\lambda\cos(4\delta)].}
\]
Independently, the temporal-face pair shows \(s_H\ge2-6\delta\) on this same event **regardless of how all H-links are subsequently optimized**. Thus \(D_\delta\subset\{\lambda s_H\ge(2-6\delta)\lambda\}\), and the displayed Gibbs bound rigorously suppresses a concrete high-frustration exterior mode. With \(\delta=0.05\), the thresholds are \(s_H\ge1.7\) and
\[
 \boxed{\mu_{R,\lambda}(D_{0.05})\le e^{-7.8405326227\lambda}.}
\]
This is a *real* Penrose-specific local repair, not an abstract four-letter Wilson counterexample. **It is not an absolute tail for the entire event \(\{s_H\ge t/\lambda\}\)**: high frustration may arise from many other configurations that do not satisfy the 13-link center-defect criteria.

## 6. Exact status and the missing next lemma

**PROVED:** local gauge-near-flat exterior coercivity for arbitrary Penrose plaquette supports with a one-face collar, with explicit \(\alpha=1\) and \(O(q/\lambda)\) additive cost; the corresponding *joint* Gibbs Peierls inequality; a strong, unconditional, single-defect Peierls suppression with exact Haar Jacobian one; a nonzero external-frustration Penrose witness, verified under four ambient volumes.

**NOT PROVED:** a Gibbs-probability estimate for the full exterior halo in a class broad enough to cover almost all large-\(s_H\) configurations, a coercive bounded-multiplicity surgery that acts successfully on *every* large-frustration exterior mode, the unconditional \(C^q(1+\lambda)^{aq}e^{-ct}\) tail for \(\lambda s_H\), the local retained-energy theorem for arbitrary Q, or a continuum mass gap.

The next noncircular task is to classify the complete finite-dimensional exterior modes of the 36-link, 62-face block and assign **each** mode a controlled energy-decreasing transformation while accounting for all retained crossing faces. Alternatively establish a local Wilson plaquette concentration theorem in the irregular Penrose prism setting. The present good-halo class is a strict and explicitly quantified partial result, not an unconditional solution.

## Reproduction

Run `python audit.py`, `python nonabelian_witness.py`, `python verify_coercivity.py`. All use the bundled unchanged direct-Z5 Penrose generator and incidence construction. `geometry_certificate.json` contains local counts, `nonabelian_single_link_witness.json` the exact Tietze proof, `certificate.json` the four-radius quaternion tests and explicit rates. `full_analytic_constants.json` contains constants for both fixed and arbitrary-support bounds.
