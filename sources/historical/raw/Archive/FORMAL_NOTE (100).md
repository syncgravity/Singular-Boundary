# R3 — Explicit finite-net nonabelian Haar surgery on genuine Penrose prism collars

**Date:** 27 October 2026. **Scope:** the verified direct-\(\mathbb Z^5\) cut-and-project Penrose rhombus spatial disks, extruded through three periodic time intervals, and arbitrary finite bounded-incidence SU(2) Wilson complexes. This note constructs an **actual deterministic action-nonincreasing, bounded-multiplicity map**, with quantitative coercivity for **differences of collar minima**. An absolute Gibbs tail for the exterior minimum, the full arbitrary-support R3 inequality, and the Yang–Mills continuum mass gap are **still open**.

## I. Full interacting Wilson action and target

For retained plaquettes \(R\), independent normalized Haar links \(U\in SU(2)^{\mathcal E}\), and \(\lambda\ge1\), set
\[
 S_R(U)=\sum_{p\in R}d(W_p(U)),\qquad d(g)=1-\tfrac12\operatorname{Tr}(g)\in[0,2],\qquad
 d\mu_{R,\lambda}=Z_R^{-1}e^{-\lambda S_R(U)}\prod_e dU_e.
\]
Every face is a four-edge word, and every link appears in at most \(\nu\) retained faces. For a link set \(J\), let \(A(J)\) be the retained faces meeting \(J\) and
\[
 S_J(u_J;b)=\sum_{p\in A(J)}d(W_p(u_J,b)),\qquad
 s_J(b)=\min_{u_J}S_J(u_J;b).
\]
For nested \(H\subset K\), \(s_H\) is a function of \(U_{H^c}\), and \(s_K\) is a function of \(U_{K^c}\). **They are not monotone in the direction needed to control absolute frustration**, since \(A(K)\) contains additional plaquettes. In particular, \(s_H-s_K\) can be negative.

## II. An explicit finite covering of SU(2)

Identify \(SU(2)\) with the unit quaternions \(S^3\). Put \(n=\lceil6\sqrt\lambda\rceil\). For each dominant component \(j=0,1,2,3\), sign \(\varepsilon=\pm1\), and coordinates \(a,b,c\in\{-1,-1+2/n,\ldots,1\}\), normalize the vector that has \(\varepsilon\) in its \(j\)-th position and \((a,b,c)\) in the other positions. Also include the identity quaternion. Call this finite set \(\mathcal N_\lambda\).

For any unit quaternion \(q\), choose \(j\) maximizing \(|q_j|\). Since \(|q_j|\ge1/2\), ratios of the other three components to \(|q_j|\) belong to \([-1,1]\). Replacing these by their nearest grid values and normalizing gives Euclidean chord distance at most \(2\sqrt3/n\). The SU(2) geodesic distance is therefore at most \(\pi\sqrt3/n\le\lambda^{-1/2}\). Moreover,
\[
 \boxed{|\mathcal N_\lambda|\le8(n+1)^3+1\le4097\lambda^{3/2}.}
\]
The stated bound is analytic; numerical coverage tests are supplemental.

## III. Constructive deterministic map on all retained configurations

Fix nested local link blocks \(H\subset K\), \(k=|K|\). For a tuple \(g=(g_e)_{e\in K}\in\mathcal N_\lambda^K\), let
\[
 (T_gU)_e=\begin{cases}g_eU_e,&e\in K,\\U_e,&e\notin K.\end{cases}
\]
Define \(g_\star(U)\) to be the **first** tuple in a fixed enumeration minimizing \(S_R(T_gU)\), and \(T_\lambda U=T_{g_\star(U)}U\). This is a Borel, finite-branch map; possible equality boundaries may be assigned to the first branch. It is not necessary to differentiate across those boundaries, because each branch is a fixed Haar translation.

1. **Exactly local**: only links of \(K\) change. All retained faces disjoint from \(K\) remain exactly unchanged and cancel when computing the action difference.
2. **Exact branchwise Jacobian**: \(J(T_g)=1\) for product normalized Haar, independent of the input, \(\lambda\), and ambient volume.
3. **Total inverse multiplicity**: every image has at most \(\lvert\mathcal N_\lambda\rvert^k\le(4097\lambda^{3/2})^k\) inverse images across all branches, since each branch has the explicit inverse \(U_e=g_e^{-1}(T_gU)_e\).
4. **No action increase**: the identity element belongs to the net, so \(S_R(T_\lambda U)\le S_R(U)\) for every \(U\).

The exhaustive search has an exponentially large runtime in \(k\); the claims are **mathematical support and multiplicity complexity**, not a polynomial-time algorithm.

### Exact quantitative action-decrease inequality

Let \(u_K^*(b)\) be a minimum of \(S_K(\cdot;b)\) for exterior \(b=U_{K^c}\). Since left translating the original \(U_K\) by a net tuple gives a product net in \(SU(2)^K\), some candidate lies within geodesic distance \(\lambda^{-1/2}\) of \(u_K^*\) in every link coordinate. The first derivative of \(S_K\) vanishes at the minimum. For every quadrilateral, the second derivative along product geodesics of angular velocities \(X_e\) is bounded by \((\sum_{e\in\partial p\cap K}\|X_e\|)^2\); since each face has four edges and link incidence is at most \(\nu\), the Taylor remainder obeys
\[
 \lambda\bigl(S_K(T_{g}U)-s_K(b)\bigr)\le2\nu k.
\]
By minimality of \(g_\star\) the same bound holds with \(T_{g}\) replaced by \(T_\lambda\). Since \(S_K(U)\ge S_H(U)\ge s_H(U_{H^c})\), we conclude **for every configuration**
\[
 \boxed{\lambda\bigl[S_R(U)-S_R(T_\lambda U)\bigr]
 \ge\lambda\bigl[s_H(U_{H^c})-s_K(U_{K^c})\bigr]-2\nu k.}
\]
When the right-hand side is positive the map is strictly action decreasing. This is a genuine **full retained action** estimate, including every affected crossing plaquette.

### Gibbs probability bound from the actual map

On \(E_t=\{\lambda(s_H-s_K)\ge t\}\), change variables on each finite translation branch and use its explicit inverse. With no assumptions on the exterior marginal:
\[
 \boxed{\mu_{R,\lambda}(E_t)\le\min\left\{1,
 \exp\left[k\left(\tfrac32\log\lambda+\log4097+2\nu\right)-t\right]\right\}.}
\]
This re-proves a one-shell Peierls *increment* estimate by an **explicit bounded-multiplicity transformation**, unlike the previous compact-Haar ball integration proof.

## IV. A fully constructive *conditional* absolute-suppression criterion

Suppose a geometric/nonabelian **collar coercivity estimate** can additionally be demonstrated on every configuration of a bad event \(\{\lambda s_H\ge t\}\): for some \(\alpha>0\), \(\eta\ge0\),
\[
 \boxed{s_K(U_{K^c})\le(1-\alpha)s_H(U_{H^c})+\eta |Q|/\lambda.}
\]
If \(k\le A|Q|\), the **same explicit map**, with no additional Jacobian or transport construction, now satisfies the stronger action decrease
\[
 \lambda[S_R(U)-S_R(T_\lambda U)]\ge\alpha t-\eta|Q|-2\nu k,
\]
and therefore
\[
 \boxed{\mu_{R,\lambda}\{\lambda s_H\ge t\}
 \le\min\left\{1,\exp\left[-\alpha t+\eta|Q|+k(\tfrac32\log\lambda+\log4097+2\nu)\right]\right\}.}
\]
This is exactly the requested \(C^{|Q|}(1+\lambda)^{a|Q|}e^{-ct}\) form, with ambient-independent constants **if and only if the independent collar-coercivity obligation can be met**. Integrating this tail gives \(\lambda\mathbf E s_H\le\bigl[\eta|Q|+k(\tfrac32\log\lambda+\log4097+2\nu)+1\bigr]/\alpha\). This closes the previously proved local energy bound for any class in which coercivity is separately established.

**The coercivity hypothesis is NOT proved for arbitrary Penrose supports.** Because adding collar links also adds retained crossing plaquettes, \(s_K\) may exceed \(s_H\). It is not legitimate to replace \(s_K\) by zero or invoke this conditional criterion as an unconditional R3 theorem.

## V. A particularly simple exterior center-flip surgery

For the fixed verified 14-face Penrose temporal cavity, let \(H\) be its 36 incident links and \(K\) their 125-link retained-face collar. There are 89 genuine exterior links in \(K\setminus H\). For each such link \(e\), consider the SU(2) center transformation \(U_e\mapsto-U_e\), leaving every other link fixed. Since every incident quadrilateral contains the link once, this changes \(W_p\mapsto-W_p\) on exactly the incident retained faces. Writing \(c_p=\frac12\operatorname{Tr}W_p\), the **full** action decrease is exactly
\[
 \boxed{S_R(U)-S_R(\mathrm{flip}_e U)=-2\sum_{p\in R:p\ni e}c_p.}
\]
Choose the most decreasing one-link flip, or the identity if no flip decreases the action. This map has **exact Haar Jacobian one on each branch**, modifies **at most one exterior collar link**, and has total multiplicity at most \(1+89=90\), independent of \(\lambda\) and ambient volume. For four nested genuine Penrose patches, the exact Q14 collar remains 36/125/258 links at zero/one/two shells, with exactly 89 candidate exterior links at one shell. Explicit quaternion tests compute the full retained Wilson action before/after each map, including all crossing plaquettes. Random-Haar configurations give positive action decreases; flat configurations select identity. **The center flip has no proved lower bound proportional to \(s_H\)** and is a diagnostic/complementary surgery, not a solution to absolute frustration.

## VI. Obstruction to deriving absolute coercivity from locality and measure bounds alone

An abstract two-plaquette four-letter word system can have retained words \(Uxab\) and \(Ux ac\), where frozen exterior symbols are \(a=b=I,c=-I\). Its plaquette holonomies are opposite SU(2) elements, so
\[
 d(Ux)+d(-Ux)=2
\]
for every adjustable pair \(U,x\). Consequently \(s_{\{U\}}=s_{\{U,x\}}=2\) and **no action decrease of either adjustable-link surgery is possible**. All word lengths are four and the link set is bounded. This is an **abstract Wilson-word counterexample, not an embedded Penrose quadrilateral-prism manifold**; it demonstrates the extra exterior compatibility condition is logically essential and does not disprove a Penrose-specific theorem.

In the genuine Q14 Penrose cavity, signed integer incidence ranks computed over two distinct large prime fields indicate that nontrivial exterior compatibility directions persist at all three tested collar levels:

| Collar | Links | Affected retained faces | Additional exterior rank |
|---|---:|---:|---:|
| \(H_0\) | 36 | 62 | 24 |
| \(H_1\) | 125 | 175 | 46 |
| \(H_2\) | 258 | 335 | 63 |

These modular ranks are identical across surrounding radii (5, 6.5, 8 and 10). This is a finite-field numerical/certificate audit of the linearized constraint structure, not by itself a certified characteristic-zero rank or a nonlinear flat-completion theorem. In conjunction with the earlier nonabelian obstruction examples, it warns against assuming every outer boundary admits a fully flat local completion. They do not exclude a **Gibbs-typical** probabilistic coercivity estimate.

## VII. Reproduction and precise status

- `direct_cut_project.py`: unchanged certified Phase III acceptance-window \(\mathbb Z^5\) Penrose disk generator.
- `construct_surgery.py`: explicit quaternion net and full-action one-link translation audit.
- `cavity_audit.py`: fixed original 14-face temporal support and nested Penrose collar sizes, exact source-label preservation.
- `center_flip_audit.py`: exact one-exterior-link, Jacobian-one center-flip map and full retained action check.
- `rank_obstruction.py`: signed incidence exterior ranks with two distinct large primes.
- `abstract_no_go.py`: exact abstract-plaquette four-factor nonabelian obstruction.
- `certificate.json`, `cavity_certificate.json`, `center_flip_certificate.json`, `rank_certificate.json`, `abstract_no_go_certificate.json`: machine-readable results.

**PROVED**: explicit, measurable, piecewise product-Haar surgery on nested Penrose blocks; at most \(O(|Q|)\) changed links, unit branchwise Jacobian, \(\exp[O(|Q|\log\lambda)]\) inverse multiplicity, quantitative **full-action decrease for collar-minimum increments**. A more economical exactly-local center-flip action-decreasing map is also constructed on the actual Q14 exterior collar.

**NOT PROVED**: a positive absolute coercivity constant \(\alpha\) on the event \(\lambda s_H\ge t\), uniform across arbitrary Penrose supports, or an absolute 3D Gibbs tail for \(s_H\). Consequently, the desired general local retained-energy estimate, arbitrary-support R3 insertion theorem, and continuum Yang–Mills mass gap remain **open**.
