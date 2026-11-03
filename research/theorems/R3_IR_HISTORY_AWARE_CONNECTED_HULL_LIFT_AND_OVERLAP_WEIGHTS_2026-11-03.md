# History-aware original-link SU(2) polymer lift: exact reconstruction, feedback, and overlap-weight absorption

**The Singular Boundary — independent physical-operator proof audit — November 3, 2026**

## Executive finding

A mathematically valid **history-aware connected-hull lift** exists for the corrected physical SU(2) original-link centered Poisson bilinear operation. It records the connected face interval that generated each contribution, **even when the resulting spin-network eigenfunction has disconnected minimal edge support**. The lift retains all physical output channels and intertwines *exactly* with reconstruction by summing history labels. The non-injective reconstruction map has a bilinearly stable kernel, unlike the invalidated projection that deletes disconnected-support physical states.

The prior exact all-width family of two shifted overlapping fundamental rectangles supplies a quantitative test. It has a genuine shared-singlet output coefficient `k/16`, but its **normalized history-labelled coefficient contribution** is bounded for every `k` if a positive hull exponent `κ>0` or a positive total-original-edge-degree exponent `σ>0` is used; even at `κ=σ=0`, a polynomial degree exponent `s>=1/2` controls this particular family. Its next-order connected feedback remains present and is tracked at the original union hull.

**Status:** These are exact algebraic and special-family all-width statements. The construction does **not** establish a general all-width bounded bilinear map, convergence of the nonlinear recurrence, a physical interacting gap at `λ=1`, or a continuum four-dimensional Yang–Mills mass gap.

## 1. A history-labelled, physical cylinder-function space

Let `G_t` be the planar one-row original-link square ladder with `t` faces and normalized Haar SU(2) measure on every physical link. For a nonempty contiguous face interval `I=[a,b]`, write `E(I)` for the `3|I|+1` original edges surrounding its constituent squares, including internal shared edges. Let `V(I)` be the vector space of **gauge-invariant** finite Peter–Weyl cylinder functions depending only on the link variables in `E(I)`. In particular, elements of `V(I)` may have strictly smaller *minimal* edge support, and that minimal support may be disconnected.

The history-labelled algebraic space is the **external** direct sum

\[
\boxed{\mathscr H_t:=\bigoplus_{I\subseteq[1,t]\ \mathrm{interval}}\bigl([I]\otimes V(I)\bigr).}\tag{1}
\]

The symbols `[I]` are formal provenance tags, **not** SU(2) representation labels. The same physical function can appear in different slots with different labels; no cancellation across labels is presumed. Let

\[
\boxed{\mathcal R\Big(\sum_I[I]\otimes f_I\Big):=\sum_I f_I}\tag{2}
\]

be **reconstruction**, which forgets provenance only after summing the complete family. The map is surjective onto gauge-invariant finite original-link cylinder functions assigned to some face hull, and is non-injective. On an infinite strip the same formulas are first understood for finite sums; any completed space would require separate absolute-convergence verification.

## 2. The physical Poisson operation has an exact history lift

Use the **actual original-link** positive free electric generator `K=−Σ_(e,a)∇_(e,a)^2`, constant-mode projection `Q`, and bilinear

\[
\mathcal B(f,g)=K^{-1}Q\Gamma_K(f,g),\qquad
\Gamma_K(f,g)=\sum_{e,a}(\nabla_{e,a}f)(\nabla_{e,a}g).
\]

The original-link support lemma from the prior exact audit states: `Γ_K(f,g)=0` if the input supports share no original edge; otherwise its cylinder support is contained in their union, and the centered free inverse `K^{-1}Q` **preserves that original-edge support** (all original-link spin-network Casimirs are diagonal).

For two face intervals `I,J` whose **actual physical edge supports** intersect, the assigned hull `T=I∪J` is a contiguous interval (two distinct square intervals can meet at a common vertical edge when adjacent). Thus `B(f_I,g_J) ∈ V(T)`. Define

\[
\boxed{
\mathcal B_{\rm hist}([I]\otimes f,[J]\otimes g)
:=[I\cup J]\otimes\mathcal B(f,g),
}\tag{3}
\]

and extend bilinearly over finite sums. For link-disjoint inputs the right side is zero. One may also set it to zero whenever the face intervals are separated by at least one **intervening** face, because such original-edge cylinder functions cannot share links.

**THEOREM 1 (exact reconstruction and stable null histories).** For all finite history families `F,G`,

\[
\boxed{\mathcal R\,\mathcal B_{\rm hist}(F,G)
=\mathcal B(\mathcal RF,\mathcal RG).}\tag{4}
\]

This is immediate from the bilinearity of the *physical* carré du champ and the linearity of `K^{-1}Q`, together with support preservation ensuring the history-tagged outputs are well-defined. In particular, for `N∈ker R`,

\[
\boxed{\mathcal B_{\rm hist}(N,G),\ \mathcal B_{\rm hist}(G,N)\in\ker\mathcal R.}\tag{5}
\]

Thus `ker R` is a (two-sided, **bilinear-operation**) ideal, and the quotient by **zero-reconstruction histories** recovers the physical Poisson operation. This is **not** the previously refuted quotient that throws away nonzero physical spin networks whose *minimal* original-link support is disconnected. The history lift remains faithful exactly because nothing physical is deleted.

**Formal-order reconstruction.** Given a finite history source `S`, the algebraic recurrence `F_1=S`, `F_n=Σ_(i=1)^(n-1) B_hist(F_i,F_(n-i))` (or any similarly finite quadratic formal-power-series recurrence) obeys `R F_1=R S`, `R F_n=Σ_i B(R F_i,R F_(n-i))` at every order by induction. This is an **identity of formal coefficients**, not a theorem of convergence of `Σ_n z^n F_n` at any nonzero `z`.

## 3. Exact positive overlap discount from connected hull labels

For real `κ>=0`, assign every history channel its face-hull weight `e^{κ|I|}`. For a nonzero linked pair with assigned union hull `T=I∪J`, the ratio of output to input face weights is **exactly**

\[
\boxed{
\frac{e^{\kappa|T|}}{e^{\kappa|I|}e^{\kappa|J|}}
=e^{-\kappa|I\cap J|}.
}\tag{6}
\]

The overlap `|I∩J|` counts shared **face labels**, not shared original edges. For adjacent face intervals the overlap count is zero even though the intervals meet along one physical link; no artificial gain is claimed there. For the shifted rectangles in the next section it equals the shared-face overlap length `k`.

For a fixed orthonormal original-link spin-network energy basis, denote the total original-edge Peter–Weyl degree `N_α=Σ_e n_e`. Clebsch–Gordan fusion gives `N_ν<=N_α+N_β` for every output channel of the physical original-link product (gradients preserve original-edge labels and the inverse is diagonal), so for `σ,s>=0`:

\[
\frac{e^{\sigma N_\nu}(1+N_\nu)^s}{e^{\sigma(N_\alpha+N_\beta)}(1+N_\alpha)^s(1+N_\beta)^s}\le1.
\tag{7}
\]

Equations (6)–(7) identify a **true overlap penalty** and submultiplicative degree weights. They do **not** bound the unweighted local recoupling/fusion coefficient sum for arbitrary spins and graphs; that remaining estimate is precisely where the all-width proof is open.

## 4. Full four-channel shifted-rectangle test with history and degree weights

The independently archived original-link SU(2) fusion theorem supplies the exact result for the two **connected input** rectangles

\[
F_k=\chi_1(W_{[1,k+1]}),\qquad G_k=\chi_1(W_{[2,k+2]}),\qquad k\ge1.
\]

Their history labels have widths `k+1,k+1`, their union hull is `T=[1,k+2]` of width `k+2`, and their face overlap has exactly `k` faces. Their total original-edge degrees are `N_F=N_G=2(k+2)`. The physical normalized output eigenchannels `Ψ_cd` (`c,d∈{0,2}`) have **physical original-edge** total degrees and electric energies

\[
N_{cd}=8+k(c+d),\qquad E_{cd}=6+k(c+d).
\tag{8}
\]

(For the two shared paths, each of `k` edges carries label `c` or `d`; the two exclusive end-plaquette paths contribute eight fundamental-spin edges.) The exact full physical Poisson response, with *the complete union history retained on every channel*, is

\[
\boxed{\begin{aligned}
\mathcal B_{\rm hist}([1,k+1]\otimes F_k,[2,k+2]\otimes G_k)
=[T]\otimes\Big[&\frac{k}{16}\Psi_{00}
+\frac{\sqrt3 k}{16(k+3)}(\Psi_{02}+\Psi_{20})\\
&-\frac{3k}{16(2k+3)}\Psi_{22}\Big].
\end{aligned}}\tag{9}
\]

The `Ψ_00` channel is the product `H_k` of the two **separated end-plaquette characters**. Its minimal physical support is disconnected, but its recorded history is the **connected** interval `T`. It has physical energy 6 and cannot be removed by constant centering.

Define the graded per-pair coefficient ratio in the historical norm with weights `e^{κ|I|}e^{σN}(1+N)^s`. Using (8)–(9) gives the **exact** all-width family expression

\[
\boxed{
\mathfrak R_k(\kappa,\sigma,s)
=e^{-\kappa k}\sum_{c,d\in\{0,2\}}
|b_{cd}(k)|\,e^{-\sigma(4-c-d)k}
\frac{\bigl(9+k(c+d)\bigr)^s}{(2k+5)^{2s}},
}\tag{10}
\]

where the absolute channel coefficients are

\[
|b_{00}|=\frac{k}{16},\quad
|b_{02}|=|b_{20}|=\frac{\sqrt3 k}{16(k+3)},\quad
|b_{22}|=\frac{3k}{16(2k+3)}.
\]

**THEOREM 2 (all-width restricted-family bounds).** For the complete four-channel history-labelled output, uniformly over integers `k>=1`:

* For `κ>0`, `σ>=0`, `s>=0`,
\[
\boxed{\sup_k\mathfrak R_k(\kappa,\sigma,s)
\le\frac{1}{16e\kappa}+\frac{\sqrt3}{8}+\frac3{32}.}\tag{11}
\]
* For `κ=0`, `σ>0`, `s>=0`,
\[
\boxed{\sup_k\mathfrak R_k(0,\sigma,s)
\le\frac{1}{64e\sigma}+\frac{\sqrt3}{8}+\frac3{32}.}\tag{12}
\]
* At `κ=σ=0`, the family is bounded if `s>=1/2`; in particular,
\[
\boxed{\sup_k\mathfrak R_k(0,0,1/2)
\le\frac3{16}+\frac{\sqrt3}{8}.}\tag{13}
\]
For `κ=σ=0` and `0<=s<1/2`, the `Ψ_00` term grows as `k^{1-2s}`. Hence `s>=1/2` is the sharp *polynomial-degree threshold for this family* (not a sufficiency theorem for arbitrary spin-network fusion).

**Proof.** Degree-weight submultiplicativity (7) makes the polynomial factor in (10) at most 1 for `s>=0`. Use `k/(k+3)<1`, `k/(2k+3)<1/2`, and `k e^{-ak}<=1/(ea)` for positive `a`. At `κ=0<σ`, the two `02` channels receive `e^{-2σk}`, the `00` channel receives `e^{-4σk}`, and the remaining `22` coefficient is already bounded. At `κ=σ=0,s=1/2`, the `00` contribution is `3k/[16(2k+5)]<3/32` and the other channels sum to less than `√3/8+3/32`, giving (13). For `s>1/2`, polynomial weights only further reduce the ratio. The lower bound from the `00` term proves the stated necessity threshold. `□`

These are **all-width exact-family** coefficient bounds, unlike the previous huge `H_m` dimension majorant, but they do not cover general overlapping spin networks or arbitrary histories.

## 5. Next-order nonlinear feedback is exactly preserved

Let `x=χ_1(A)` and `y=χ_1(B)` be the fundamental characters of the two separated end plaquettes, so `H_k=xy` and the original-link supports of `x` and `y` are disjoint. Let `u=χ_2(A)`. The prior exact local original-link identity is

\[
\boxed{\mathcal B(H_k,x)=y-\frac1{11}u\,y.}\tag{14}
\]

The physical response of the growing history component alone, at the next quadratic interaction with `x`, therefore equals

\[
\boxed{
\mathcal B\!\left(\frac{k}{16}H_k,x\right)
=\frac{k}{16}y-\frac{k}{176}u\,y.
}\tag{15}
\]

In the **history lift**, both outputs of (15) retain the union interval `T=[1,k+2]`, even though the first, `y`, depends on only the far-end plaquette. Reconstruction maps (15) back to the exact physical response, with no missing term. By contrast, a naive projection discarding the disconnected minimal-support state `H_k` would lose **both** terms of (15).

For the history representation, one should not project onto minimal connected supports or relabel (15) with the smaller minimal hull without tracking the resulting combinatorial and weighted-norm change. The history tag is a **provenance bookkeeping device**; it is not a claim that the physical eigenfunction actually depends on every original link in `T`.

## 6. What is not proved and next target

The history-labelled lift provides an **exact algebraic nonlinear model with physical reconstruction**, and the shift-rectangle test proves a finite coefficient bound when overlap, analytic-degree, or polynomial-degree weights compensate the real `k/16` channel growth. There is no projection/source defect, no loss of the separated channel, and no failure to retain next-order feedback.

It does **not** prove that the sum of physical SU(2) recoupling structure constants has an all-width estimate over **arbitrary** overlapping connected supports. The bilinear operator on the completed history space is not yet proved to be bounded, and the formal quadratic recurrence is not proved convergent. Furthermore, smallness at physical `λ=1`, an interacting thermodynamic gap, and the four-dimensional continuum Yang–Mills mass gap remain open.

**Next mathematical target:** derive a *history-labelled, all-width* fusion kernel estimate for connected original-link spin networks, tracking each independent shared path, the total edge degree, the number of allowed intertwiner channels, and the overlap budget from (6). A first test should extend the exact theta/two-path Wilson calculation to a uniformly bounded number of shared segments, followed by a constructive overlapping-interval incidence estimate compatible with the anchored norm. The current special-family calculation supplies exact benchmark coefficients but no general claim of closure.

## 7. Reproducibility

`verify_history_aware_hull_lift.py` tests (i) exact reconstruction for a two-history nonlinear input, (ii) original-link next-order feedback with separate retained labels, (iii) all four channel energies and edge-degree accounting for `1<=k<=2000`, and (iv) the positive hull/analytic and half-polynomial overlap budgets for `1<=k<=500`. It performs **29,000 exact-rational/combinatorial assertions and floating-point bound spot checks**; exact derivations above—not finite sampling—are the all-length proofs. The prior independently archived projector/fusion theorem provides the four-channel physical SU(2) normalization used as input, and the previous linked-cluster obstruction report provides (14). The checker records all tests and this report is accompanied by a passing execution log and a SHA-256 manifest.