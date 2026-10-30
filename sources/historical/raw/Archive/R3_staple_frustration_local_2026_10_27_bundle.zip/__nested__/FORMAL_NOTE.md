# R3 — Rigorous local staple-frustration estimates: a solved planar case and the unresolved 3D boundary-minimum problem

Date: 27 October 2026. Study pertains to the verified direct-Z^5 Penrose rhombus disks and their three-step periodic prism products. **The arbitrary-support 3D nonlinear R3 theorem is not proved here.**

## Setting

For a finite oriented plaquette complex with normalized independent SU(2) Haar links, put `d(g)=1-(1/2)Tr g` and

\[S_R(U)=\sum_{p\in R}d(W_p),\quad d\mu_{R,\lambda}=Z_R(\lambda)^{-1}e^{-\lambda S_R(U)}\prod_e dU_e.\]

For retained link `e` with `m_e` incident retained plaquettes, hold all other link variables fixed. Reorienting each term using trace cyclicity gives `d(U_e A_{p,e})`. Let the corresponding unit-quaternion staple vector sum be `h_e`, with `H_e=||h_e||`. The **staple frustration** is `F_e=m_e-H_e`. It is independent of `U_e` but depends on all neighboring links.

The exactly proved heat-bath excess inequality from the preceding stage is

\[0\le \lambda\mathbb E[\sum_{p\ni e}d(W_p)-F_e\mid U_{\ne e}]\le3/2.\]

It does not bound `lambda E F_e` under the 3D measure, since opposing fixed staples give `H_e=0` and `F_e=m_e=2`.

## Theorem A — actual Gibbs-law exponential concentration on any *planar* free-boundary Penrose rhombus disk

Let the spatial complex be a simply connected open rhombus disk, with any retained face subset `R` and free Haar links. After ordinary spanning-tree gauge fixing, all independent plaquette holonomies are Haar independent; Wilson weighting makes the retained holonomies independent with law

\[d\nu_\lambda(g)=e^{-\lambda d(g)}q(\lambda)^{-1}\,dg,\quad q(\lambda)=2e^{-\lambda}I_1(\lambda)/\lambda.\]

The deterministic inequality `F_e <= sum_{p in R, p incident to e} d(W_p)` holds because `F_e` is the minimum of that sum over the variable `U_e`. The Wilson face integrals satisfy

\[\lambda \mathbb E_{\nu_\lambda}d(W)=\lambda(1-I_2(\lambda)/I_1(\lambda))\le3/2.\]

Furthermore, for `0<=theta<1`,

\[\mathbb E_{\mu_{R,\lambda}}e^{\theta\lambda F_e}
 \le\left(\frac{q((1-\theta)\lambda)}{q(\lambda)}\right)^{m_e}
 \le(1-\theta)^{-3m_e/2}.\]

The second inequality follows by integrating `-d log q(t)/dt = 1-I_2(t)/I_1(t) <=3/(2t)` between `(1-theta)lambda` and `lambda`.

Thus **for every volume and every lambda>0**,

\[\boxed{\lambda\mathbb E F_e\le\tfrac32m_e,\qquad
 \mathbb P\{\lambda F_e\ge t\}\le2^{3m_e/2}e^{-t/2}.}\]

In a rhombus disk `m_e<=2` for all retained link incidence, giving `lambda E F_e<=3` and tail `<=8 e^{-t/2}`. These are exact theorems for the genuine planar Penrose retained Wilson measure, with no Gaussian approximation or regularizer.

The same independence gives for any face subset `A\subset R`

\[\mathbb E e^{\theta\lambda\sum_{p\in A}d(W_p)}\le(1-\theta)^{-3|A|/2},\quad
 \lambda\sum_{p\in A}\mathbb E d(W_p)\le\tfrac32|A|.\]

**Scope limitation:** This fails as a proof for the 3D rhombus-prism model because spatial and temporal face holonomies no longer factorize under the full retained Gibbs measure. The connected Bianchi constraints and linked staple variables are precisely the difficult part.

## Theorem B — true 3D conditional concentration *above the exterior boundary minimum*

This holds on **any** finite four-edged-plaquette SU(2) complex of maximum link-face incidence `nu` without any planar independence or Gibbs uniqueness assumptions. Fix a block `B` of `k` link variables, exterior links `b`, and define `A(B)` as all retained faces involving a link of B. Let

\[S_B(u;b)=\sum_{p\in A(B)}d(W_p(u,b)),\qquad s_\star(b)=\min_{u\in SU(2)^k}S_B(u;b).\]

Every conditional Wilson integral is taken against *normalized product Haar on the k block links*. Assume `lambda>=1`.

For the SU(2) geodesic ball of angular radius `r<=1` its normalized Haar volume is at least `c_H r^3`, where `c_H=8/(3 pi^3)`. Center all k links at an actual minimizer of `S_B`. Parametrize their simultaneous perturbation as `u_e(t)=u_e^\star exp(t X_e)` with `||X_e||<=lambda^{-1/2}`. The first derivative of the total action vanishes at a minimizer. For every quadrilateral Wilson trace, its second directional derivative has magnitude at most `(sum_{e in face cap B} ||X_e||)^2`. Hence

\[\lambda(S_B(u;b)-s_\star(b))\le 2\nu k\]

throughout the product of radius-`lambda^{-1/2}` balls. Haar measure invariance and the quadratic Taylor formula give

\[\int e^{-\lambda(S_B-s_\star)}\,du\ge [c_H\lambda^{-3/2}e^{-2\nu}]^k.\]

Writing `h(lambda)=-log int exp[-lambda(S_B-s_star)]du`, we have `h(0)=0`, `h''(lambda)=-Var(S_B)<=0`, so `lambda h'(lambda)<=h(lambda)`. Therefore **for every fixed exterior b**,

\[\boxed{\lambda\mathbb E[S_B-s_\star(b)\mid b]\le
 k\big(\tfrac32\log\lambda+2\nu-\log c_H\big).}\]

The exponential Chernoff comparison with the half-coupling conditional partition function gives

\[\boxed{\mathbb P\big\{\lambda(S_B-s_\star(b))\ge
 3k\log\lambda+2k(2\nu-\log c_H)+2s\mid b\big\}\le e^{-s},\quad s\ge0.}\]

For the verified three-step Penrose prism geometry, every face has four edges and every link is in at most `nu=7` faces. Hence `2nu-log c_H = 16.4533604045365`, independent of the number of prisms.

The conditional tail estimate remains true **after averaging with the actual retained exterior Gibbs marginal** because its upper bound holds for every exterior b, but only for the difference `S_B-s_star(b)`.

### Exact local-energy decomposition

Taking an exterior Gibbs expectation in Theorem B gives

\[\boxed{\lambda\mathbb E_{\mu_R}S_B
\le k(\tfrac32\log\lambda+16.453360405)
+\lambda\mathbb E_{\nu_R}s_\star(b).}\]

If `A` is a prescribed retained neighborhood, choose B consisting of links in its face boundaries. Then `k<=4|A|` and `A\subseteq A(B)`. If `|A|<=c|Q|`, the first term is precisely the required `O(|Q|(1+log lambda))` **uniformly in ambient volume**. The second term, a randomly forced nonlinear boundary-minimum/compatibility defect, is NOT bounded by this argument.

To conclude the target R3-local energy bound it would suffice to prove the still-open estimate

\[\lambda\mathbb E_{\nu_R}s_\star(b)\le C|Q|(1+\log\lambda)\]

for this local choice of B. For the one-link block, `s_star(b)=F_e`, so this is exactly the original staple frustration problem; increasing the block size changes its form but does not remove it automatically.

### Why the missing step is not a technicality

In a fixed-exterior local heat bath with two opposite staples, `F_e=2` identically. No pointwise `O(log lambda/lambda)` control of `F_e` is possible. A proof for the full 3D Penrose Gibbs measure must show that such incompatible exteriors are sufficiently improbable, or must construct a correlated local transport with controlled Radon–Nikodym cost. An unconditional 3D tail for `F_e` has **not** been derived here; asserting one from the planar theorem or from bounded-degree geometry would be incorrect.

## Verified geometric sizes

The same direct-Z5 generator yields nested Penrose disks with (V,E,F) = (90,159,70), (148,269,122), (226,421,196), (377,714,338). The product with 3 periodic times gives 747, 1251, 1941, 3273 links; the maximum face incidence is 7 in every tested volume. The 2D link-face incidence is at most 2. Code: `verify.py` and `verify_block.py`; quantitative outputs: `certificate.json`, `conditional_block_certificate.json`, `penrose_planar_certificate.csv`.

## Relation to prior and external literature

Mack–Petkova and subsequent discussions refer to plaquette concentration on regular Wilson lattices. Those statements are **not** used as a theorem about Penrose rhombus-prism cavities: geometric and boundary hypotheses differ, and any transfer requires a new proof. The exact planar theorem and conditional block result here are self-contained.

## Research status / next proof obligation

- **PROVED** volume-uniform exponential distributional bound for staple frustration on planar Penrose disks under their exact retained Wilson measure.
- **PROVED** volume-uniform conditional Gibbs energy/tail estimate *above* the random exterior minimum in genuine 3D Penrose prisms.
- **UNPROVED** uniform control of the exterior Gibbs law of that minimum, equivalently a 3D local staple-frustration estimate.
- **UNPROVED** arbitrary-support nonlinear R3 insertion inequality and continuum Yang–Mills mass gap.

A defensible next approach is a boundary-to-interior repair/Peierls estimate on small prism collars, using actual nonabelian Bianchi words, with a bound on the exterior marginal of large `s_star(b)`; no theorem about that marginal is asserted in this document.
