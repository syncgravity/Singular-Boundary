# The Singular Boundary — Connected-bulk Wilson activation theorem and corner-sewing response

**Research date:** 2026-10-29. **R3 independent reconstruction.** This manuscript proves exact finite-volume geometric/analytic selection and full-coupling identities on a complete 3×3 *square-rhombus* disk. It does **not** establish the requested scale-uniform flat-holonomy mass for connected Penrose interiors, the physical mass gap, or continuum reconstruction. The 3×3 fixture is a valid rhombus-disk Wilson geometry but is not a Penrose inflation patch. It is used as a minimal connected control example, not as numerical evidence of a Penrose quantum vacuum.

## 1. Physical model and analytic coupling coordinates

Let the complete 3×3 square-rhombus disk have nine faces, 24 primal links, free boundary-link integration and Gauss invariance at **every** vertex. Let its central target face be `f=(0,0)`, with cardinal adjacent faces `N,E,S,W` and corner faces `NE,NW,SW,SE`. Delete only the target magnetic interaction. Independently vary each of the eight remaining full Wilson couplings:

\[
H(\mathbf r,\mathbf s)=\sum_ea_e(-\Delta_e)+\sum_{k\in\{N,E,S,W\}} r_kb_k(1-p_k)+\sum_{c\in\{NE,NW,SW,SE\}}s_cb_c(1-p_c).
\]

Here `p_k=ReTr W_k/2`, `a_e,b_k>0`, and \(0\le r_k,s_c\le1\) are dimensionless coupling fractions. The exact full-link Hamiltonian has a unique strictly positive ground state invariant under the physical gauge group; finite-volume real analytic perturbation theory applies in all eight coupling fractions. The physical state is obtained by restriction to the gauge-invariant subspace, and no regulator-uniform gap is assumed.

For spin \(j\in\{1,2,3,\ldots\}\), define \(c_j(\mathbf r,\mathbf s)=\langle\chi_j(W_f)\rangle_{\mathbf r,\mathbf s}\). The target center-flux symmetry ensures all half-odd-spin expectations vanish identically. Choose the previously established smooth positive central convolution cap source \(k_a=\phi_a*\phi_a^\vee\) with \(0\le k_a\le\nu_a1_{B_a}\), \(\alpha_a=\int\phi_a\), \(\nu_a=\int\phi_a^2\) and \(\alpha_a,\nu_a\asymp a^3\). Write \(F_a(\mathbf r,\mathbf s)=\langle k_a(W_f)\rangle_{\mathbf r,\mathbf s}\).

## 2. CB-1: exact support classification of all 256 magnetic activation subsets

Let \(A\) be any subset of the eight surrounding faces with nonzero magnetic coupling, with the others assigned zero. Recompute the connected components under **shared-primal-edge adjacency** of the retained magnetic faces. Any component meeting the four cyclic target edges along a single proper contiguous open arc has independent Haar group-valued arc holonomy, hence \(W_f\) itself is Haar, by the preceding open-arc theorem. If any cardinal neighboring face is inactive, an incident target edge is private and the Haar conclusion holds immediately.

For the 3×3 disk, the four cardinals form a four-vertex ring of potential contacts, and each active corner supplies exactly one link in the cycle connecting adjacent cardinals. Thus:

- If any cardinal is inactive, the target has a private edge and is exactly Haar.
- If all cardinals are active but at most two corners are active, every retained component meeting the target corresponds to a proper contiguous arc (a singleton, a pair or a triple of successive target edges). Consequently the target is exactly Haar.
- If all four cardinals and at least three corners are active, the component meets all four target edges. The open-arc theorem is **inapplicable**, and no claim of non-Haar marginal is implied.

The 256 activation subsets therefore contain **251 exactly Haar cases** and **five unresolved connected cases**, the latter being four sets of three corners plus the complete set of four corners. These statements are about *all positive values* of couplings on active faces, not perturbation theory. The deterministic verifier independently enumerates all 256 masks and the exact primal/shared-edge incidence.

## 3. CB-2: first possible Wilson-character response order on the complete disk

For each individual active surrounding face `k`, the finite disk has a primal boundary edge belonging to `k` alone. Multiplying that edge by the central `−I` flips \(p_k\to-p_k\), leaves every other face trace fixed and preserves all electric Laplacians. The Hamiltonians at \(t_k\) and \(-t_k\) are therefore unitarily equivalent up to a scalar shift \(2t_kb_k\), while \(\chi_j(W_f)\) is unchanged. Consequently **every** \(c_j\) and \(F_a\) is *even in each of the eight coupling coordinates separately*. Their Taylor expansions about the all-zero Hamiltonian contain only even powers in every variable.

Fix one cardinal face `k`. Setting its coupling \(r_k=0\) makes the link shared with \(f\) magnetically private, regardless of the other seven couplings. The remaining Hamiltonian commutes with that link's SU(2) Peter–Weyl spin projectors and the positive ground state has spin zero. Each insertion of \(b_kp_k\) in a Kato–Riesz expansion changes that link's spin by at most \(1/2\). A target spin-\(j\) Wilson character can couple ground-state perturbation orders \(m,n\) only when \(j\le(m+n)/2\). Therefore the Taylor expansion in \(r_k\) has **no term of degree below \(2j\)**, even with the other couplings arbitrary (within an analytic neighborhood of the chosen real values).

From CB-1, \(c_j\) vanishes identically whenever at most two corner variables are nonzero. Hence **every nonvanishing multivariate Taylor monomial** must contain at least **three distinct** corner coordinates. By independent center parity, every such corner contributes exponent \(\ge2\). Combining all four cardinal restrictions gives:

\[
\boxed{\text{Every nonzero monomial of }c_j\text{ has total degree }\ge4(2j)+3(2)=8j+6.}\tag{CB2}
\]

In the common-coupling specialization where all eight coupling fractions equal \(t\), the exact finite-volume selection law is

\[\boxed{c_j(t)=O_j(t^{8j+6})\quad(t\to0),\qquad j=1,2,3,\ldots.}\tag{CB3}\]

Thus spin 1 cannot appear before order 14, spin 2 before order 22, and spin 3 before order 30. These are **lower bounds on the first permitted order**, not claims that the corresponding coefficients are nonzero or have a favorable sign. For each fixed smooth central cap source, \(F_a(t)-\alpha_a^2=O_a(t^{14})\). The implicit perturbative constants need not be uniform in \(h\), and \(t=1\) lies far outside the generic finite-gap perturbative window when \(b\asymp h^{-2}\).

## 4. CB-3: exact full-coupling three-corner-plus-four-corner response decomposition

To isolate the **minimal connected obstruction** at physical coupling, set the four cardinal fractions to one and vary only the four corners: \(G_a(\mathbf s)=F_a(\mathbf1,\mathbf s)\). CB-1 gives \(G_a(s_S,0_{S^c})=\alpha_a^2\) whenever \(|S|\le2\); individual center parity makes \(G_a\) even in every corner fraction.

For a subset \(S\) of the corners, define \(\partial_S^2=\prod_{c\in S}\partial_{s_c}^2\). Apply the exact multivariate Newton/anchored inclusion-exclusion expansion, using the evenness of each coordinate to integrate its first-order finite difference twice. Terms of sizes one and two vanish. One obtains the **full physical-coupling identity**

\[
\boxed{
G_a(\mathbf1)-\alpha_a^2
=\sum_{\substack{S\subset\{NE,NW,SW,SE\}\\|S|=3,4}}
\int_{[0,1]^S}\left[\prod_{c\in S}(1-s_c)\right]
\partial_S^2G_a(\mathbf s_S,\mathbf0_{S^c})\,d\mathbf s_S .}\tag{CB4}
\]

There are exactly **four three-corner terms**, each corresponding to an eight-face connected minimal patch (the central face, all four cardinals and those three corners), plus one four-corner term in the complete nine-face patch. Every contribution is a gauge-invariant full-coupling nonlinear ground-state derivative. The identity holds without a refinement-uniform spectral gap, although controlling the derivatives uniformly remains unresolved.

Define the **adverse corner-sewing budget** as the sum of the corresponding weighted integrals with the negative part of each integrand. Positivity of the cap source gives

\[
\boxed{\Pr_{\Omega_f^-}(W_f\in B_a)\ge\frac{[\alpha_a^2-\mathcal N_a^{\rm sew}]_+}{\nu_a}.}\tag{CB5}
\]

Thus \(\mathcal N_{a_h}^{\rm sew}\le\alpha_{a_h}^2/2\) would suffice for polynomial near-flat mass at \(a_h\asymp\sqrt h\). **This bound is not established for the genuine connected Penrose deleted vacuum.** The main value of CB4 is a *minimal-geometric localization*: the first connected obstruction already appears on an eight-face patch with three corner couplings, not only on the complete nine-face ring.

## 5. CB-4: why positive-part response budgets may be unnecessarily strong

A smooth analytic *non-physical scalar comparator* makes the logical limitation explicit. Let \(r_i\) denote four neighbor fractions and \(s_i\) four corners. Put

\[
\widetilde F(\mathbf r,\mathbf s)
=\alpha_a^2\left[1+M\left(\prod_{i=1}^4r_i^2(1-r_i^2)\right)s_1^2s_2^2s_3^2\right],\quad M>0.
\]

It is strictly positive and even in every coupling; it is exactly \(\alpha_a^2\) if any cardinal coupling vanishes or fewer than three corners are active, and **returns to \(\alpha_a^2\) at the full endpoint** \(\mathbf r=\mathbf1\). Yet its eighth-order four-neighbor mixed derivative has a negative region of arbitrarily large amplitude relative to \(\alpha_a^2\) as \(M\) grows. For cap observables with \(\alpha_a^2\ll\nu_a\), a wide range of \(M\) remains compatible with the elementary probability bound \(\widetilde F\le\nu_a\). This comparator is not a Wilson quantum vacuum, but it proves that bounds obtained by separately taking positive or negative parts of mixed derivatives need not be **necessary** for Haar-order cap mass at the physical endpoint. The **signed total mixed response** is the exactly relevant quantity; one-sided budgets are sufficient but potentially overly restrictive.

## 6. Reproducibility and next real physical obligation

The two companion deterministic scripts enumerate all 256 activated square-rhombus subcomplexes; verify 24 primal links, each face's edge sharing, the 251/5 exact Haar/connected split, and spin thresholds 14,22,30,38 using exact integer arithmetic; confirm SU(2) Haar orthogonality by deterministic quadrature; and check CB4 exactly on nontrivial rational symbolic polynomials using SymPy. No Monte Carlo, physical SU(2) eight-face diagonalization, numerical Penrose-vacuum measurement, or continuum mass-gap claim is made.

**PROVED:** CB-1 support classification for the 3×3 disk; CB-2 spin/corner combined Taylor filtration; CB-3 signed full-coupling corner-sewing identity and its conditional cap inequality; CB-4 comparator showing why adverse-part budgets may be too strong.

**OPEN:** bound the **net signed** three-corner and four-corner responses or prove a polynomial cap lower bound directly for an actual, connected SU(2) Wilson magnetic-deleted ground state, including the minimal eight-face geometry; then control fully cycle-surrounded Penrose faces uniformly in refinement. Fixed-support centered covariance, nonzero finite-time response, uniform physical mass gap, quartic resolvent, and continuum reconstruction remain **OPEN**.
