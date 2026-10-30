# The Singular Boundary — Local Wilson Frames: Two Obstructions, an All-Coupling Infrared Bound, and the Operator-Norm Repair

**Date:** October 26, 2026.  
**Mathematical status:** Theorems 1–5 proved under the assumptions below. The requested interacting, continuum-uniform R3/R2 coercivity theorem remains open. This note is an independent mathematical investigation; no Monte Carlo calculation is used.

## 0. Definitions and scope

Let `G=(V,E,F)` be a finite connected face-complete patch of a genuine Penrose rhombus tiling, with simple four-link faces and edge/face incidence at most two, and let `\mathcal H_G=L^2(SU(2)^E)^{SU(2)^V}`. Normalize the one-link Laplacian by `-\Delta\chi_j=j(j+1)\chi_j` and denote `p_f=\tfrac12\chi_{1/2}(W_f)`. The finite-volume Hamiltonian is

\[
H_G=\sum_e a_e(-\Delta_e)+\sum_f b_f(1-p_f),\qquad a_e>0,\ b_f\ge0.
\]

The full-link semigroup is positivity improving for finite `G`, hence the normalized ground state `\Omega>0` is unique and gauge invariant. Put `E_0=\inf\operatorname{spec} H_G`, `K=H_G-E_0`, `Q=1-|\Omega\rangle\langle\Omega|`, `P_s=\mathbf 1_{(0,s]}(K)` restricted to physical states, and `b_A=QA\Omega` for bounded gauge-invariant multiplier `A`.

A *bounded-diameter* local source has complete link support contained in a set of physical diameter at most `R`, independent of the size of `G`. Distances in the rhombus complex may equivalently be used at a fixed edge scale. On a torus, the contractible traces below are neutral under the \(\mathbb Z_2\) one-form center action. The main no-go proofs already hold on simply connected open patches.

## 1. Theorem 1 (strictly local sources fail on the full two-loop sector)

Take constant electric coefficients `a_e=a>0` and set *all* magnetic couplings to zero. There exist arbitrary large Penrose patches containing rhombi `f,g` with mutually disjoint edge sets and separation greater than any prescribed fixed `R`, accounting for face diameters. Let
\[
\psi_{fg}=\chi_{1/2}(W_f)\chi_{1/2}(W_g).
\]

Then `\psi_{fg}` is a normalized physical gauge-invariant, contractible/center-neutral excited eigenfunction, orthogonal to the constant vacuum `\Omega_E=1`, and
\[
H_E\psi_{fg}=6a\,\psi_{fg}. \tag{1}
\]

For **every** gauge-invariant multiplier `A_X` supported in a set of diameter at most `R`,
\[
\langle\psi_{fg},QA_X\Omega_E\rangle=0. \tag{2}
\]

**Proof.** Orthogonality and norm one follow by integrating the edge-disjoint face holonomies against product Haar measure: `\int\chi_{1/2}(U)dU=0` and `\int|\chi_{1/2}(U)|^2dU=1`. Every edge in the two face boundaries carries the fundamental Casimir `3/4`; there are eight such edges. Gauge invariance follows from taking closed holonomy traces. A bounded-diameter set cannot meet the edge supports of both separated faces. Integrate an edge variable on the unvisited face; every other factor is independent of it, so its fundamental character integrates to zero. Centering `A_X` by `Q` does not change the overlap because `\psi_{fg}\perp1`. QED.

**Consequence.** If `\eta\ge6a`, no set (even arbitrarily many) of diameter-`R` sources has a positive lower frame bound on the *whole* `\operatorname{Ran}P_\eta`, for sufficiently large patches. This refutes the proposed local-frame architecture **as an all-coupling theorem** (the class includes `b=0`). It does **not** exclude a frame for a restricted one-excitation sector, nor a more complicated construction at a specified strictly positive magnetic coupling.

**Multi-component extension.** If each source has at most `q` disconnected connected components, each of diameter at most `R`, place `q+1` edge-disjoint faces pairwise farther apart than `R` (with suitable margins). The normalized product of their fundamental traces has energy `3a(q+1)` and vanishing overlap with every such source. No bounded-component frame covers the full electric energy window `\eta\ge3a(q+1)` as volume grows.

### Corollary 1B (failure persists for arbitrarily small **strictly positive** magnetic couplings)

Fix one sufficiently large finite patch containing the separated rhombi from Theorem 1, and choose an energy cutoff `\eta>6a` not equal to an electric eigenvalue. Give every face a magnetic coefficient `b_f=\epsilon>0`. Suppose for each `\epsilon` we may select any finite family of diameter-`R` Wilson multipliers `A_i(\epsilon)` and weights `w_i(\epsilon)>0`, subject to a **uniform finite-patch source budget**
\[
\sum_iw_i(\epsilon)\,\|A_i(\epsilon)\|_\infty^2\le W_G<\infty.
\]
Then, as `\epsilon\downarrow0`, the lower frame constant on `\operatorname{Ran}P_{\eta}(H_\epsilon)` tends to zero. In particular, it cannot be bounded below by a positive constant *uniform over all positive couplings*.

**Proof.** On this fixed finite patch, `\|H_\epsilon-H_E\|\le2\epsilon|F|\to0`. The electric ground state is simple; spectral projection perturbation theory gives `\|\Omega_\epsilon-1\|_2\to0` after choosing the positive phase. Since `\eta` lies in the resolvent set of `H_E`, `P_\eta(H_\epsilon)\to P_\eta(H_E)` in operator norm. Normalize `\psi_\epsilon=P_\eta(H_\epsilon)\psi_{fg}/\|P_\eta(H_\epsilon)\psi_{fg}\|`, so `\psi_\epsilon\to\psi_{fg}`. Each diameter-`R` source has `\langle\psi_{fg},A_i(\epsilon)1\rangle=0` by Theorem 1, even if it depends on `\epsilon`. Consequently,
\[
|\langle\psi_\epsilon,A_i(\epsilon)\Omega_\epsilon\rangle|
\le\|A_i(\epsilon)\|_\infty
\big(\|\psi_\epsilon-\psi_{fg}\|+\|\Omega_\epsilon-1\|\big).
\]

Squaring, multiplying by weights, and summing bounds the frame quadratic form on `\psi_\epsilon` by `W_G` times a quantity tending to zero. QED.

This result **does not** exclude a frame constructed only along the prescribed continuum trajectory `b_f\sim h^{-2}`; that trajectory does not approach zero magnetic coupling. It does establish that strict positivity `b_f>0` is not enough to rescue an *arbitrary-coupling* theorem with bounded local sources.

### Corollary 1A (exponentially quasi-local tails do not repair this under a polynomial source budget)

At fixed edge scale, suppose that `A_i` has an approximation `A_i^{(r)}` supported in a radius-`r` ball about a center `x_i`, such that `\|A_i-A_i^{(r)}\|_{L^2(dU)}\le C_0e^{-\mu r}` with `C_0,\mu` uniform, and that the number/total positive weight of sources grows at most polynomially with the patch diameter `L`. Take `f,g` with separation `D\asymp L` and `r=(D-O(h))/3`, so no radius-`r` ball intersects both faces. Then
\[
\sum_iw_i|\langle\psi_{fg},QA_i\Omega_E\rangle|^2
\le C_0^2\Big(\sum_iw_i\Big)e^{-2\mu r}\longrightarrow0. \tag{3}
\]

The estimate uses only Haar `L^2` approximability and Cauchy–Schwarz. Thus the lower frame constant still fails in the free electric sector. The statement is not asserted for the interacting vacuum without first proving analogous approximation bounds there.

## 2. Theorem 2 (bare low-spin Wilson sources can collapse at strong magnetic coupling)

Take the single-rhombus open gauge complex with four equal electric couplings `a>0` and one magnetic coupling `b>0`. Let `p=\frac12\chi_{1/2}(W)\in[-1,1]`, and let `\Omega_{a,b}` be its positive ground state. Then
\[
\boxed{\operatorname{Var}_{\Omega_{a,b}}(p)\le
\min\{1,\ 4\sqrt{2}\sqrt{a/b}\}.} \tag{4}
\]

Thus the norm of the centered unrenormalized fundamental source `Qp\Omega_{a,b}` tends to zero as `b/a\to\infty`, *even on this fixed finite graph*. The theorem does **not** assert that an actual low-energy excitation remains in a fixed window during that limit; it shows failure of automatic source-norm normalization, not failure of a low-energy frame in an empty spectral window.

**Proof.** Gauge-fix three tree links, so physical class functions depend on `W\in SU(2)`. Test the Rayleigh quotient with the positive gauge-invariant function `\varphi_\lambda=e^{\lambda p}`. In the squared trial density `\varphi_\lambda^2dU`,
\[
m_\lambda:=\mathbb E_{\lambda}(1-p)=1-\frac{I_2(2\lambda)}{I_1(2\lambda)}\le\frac1\lambda. \tag{5}
\]

For completeness, write `r(x)=I_2(x)/I_1(x)`, which satisfies `r'=1-r^2-3r/x`. For `0<x\le2`, `1-r(x)\le1\le2/x`. For `x\ge2`, compare `r` with `\ell(x)=1-2/x`. At `x=2`, `r(2)>\ell(2)=0`; at a hypothetical crossing `r=\ell`, `r'-\ell'=1/x>0`, ruling out a crossing from above. Therefore `1-r(x)\le2/x`, proving (5).

In the SU(2) metric with fundamental Casimir `3/4`, `|\nabla p|^2=(1-p^2)/4\le(1-p)/2`. Each of the four link electric energies has the same expectation, so
\[
\frac{\langle\varphi_\lambda,H\varphi_\lambda\rangle}{\|\varphi_\lambda\|^2}
\le 2a\lambda^2m_\lambda+bm_\lambda
\le 2a\lambda+b/\lambda.
\]

Taking `\lambda=\sqrt{b/(2a)}` gives `E_0\le2\sqrt{2ab}`. Positivity of the electric energy implies `b\mathbb E_\Omega(1-p)\le E_0`. Finally, `\operatorname{Var}(p)\le\mathbb E(p-1)^2\le2\mathbb E(1-p)\le4\sqrt{2a/b}`. The universal variance bound `\operatorname{Var}(p)\le1` finishes the proof. QED.

Every fixed-degree polynomial `P(p)` with uniformly bounded Lipschitz constant also has `\operatorname{Var}(P(p))\le\mathrm{Lip}(P)^2\operatorname{Var}(p)\to0`. The observation does not establish continuum quantum convergence on large Penrose patches.

## 3. Theorem 3 (a genuinely interacting, non-extensive infrared estimate for finite multi-loop sources)

Return to arbitrary `G`, arbitrary nonnegative `b_f`, and arbitrary positive `a_e`. For each link set `B_e=\sum_{g:e\in\partial g} b_g`. Choose `q` rhombi `f_1,\ldots,f_q` with pairwise edge-disjoint boundary sets; their mutual separation can be arbitrarily large. Define the bounded center-neutral `q`-local Wilson multiplier
\[
A_{\mathcal F}=\prod_{k=1}^q p_{f_k},\qquad
S_{\mathcal F}=\bigcup_{k=1}^q\partial f_k,\qquad
\kappa_{\mathcal F}=\frac34\sum_{e\in S_{\mathcal F}}a_e.
\]

For every `0<s<\kappa_{\mathcal F}`,
\[
\boxed{\|P_sQA_{\mathcal F}\Omega\|^2\le
\min\left\{1,\frac{\big(\sum_{e\in S_{\mathcal F}}\sqrt{a_eB_e}\big)^2}{(\kappa_{\mathcal F}-s)^2}\right\}.} \tag{6}
\]

**Proof.** First prove `a_e\|\nabla_e\Omega\|_2^2\le B_e`: remove the link electric term and all nonnegative magnetic faces meeting it. In the remaining Hamiltonian the omitted link is a free variable. Replacing it with the constant wavefunction in a trial ground state costs precisely `B_e`, because Haar-averaged fundamental Wilson traces vanish. Positivity of the removed terms and the variational principle give the inequality. Next, for disjoint face edges `(-\Delta_e)A_{\mathcal F}=(3/4)A_{\mathcal F}` on `S_\mathcal F`, and `\|\nabla_e A_{\mathcal F}\|_\infty\le1/2`. The exact interacting ground-state product rule gives
\[
(K-\kappa_{\mathcal F})(A_{\mathcal F}\Omega)
=-2\sum_{e\in S_{\mathcal F}}a_e\nabla_e A_{\mathcal F}\cdot\nabla_e\Omega.
\]

Take `P_s` on both sides. **One must project before using the residual:** `(K-\kappa)QA\Omega` has an extra vacuum component in general, but `P_s` kills that component. Thus
\[
(\kappa-s)\|P_s QA_{\mathcal F}\Omega\|
\le\sum_{e\in S_\mathcal F} a_e\|\nabla_e\Omega\|_2
\le\sum_{e\in S_\mathcal F}\sqrt{a_eB_e}.
\]

Square and combine with `\|QA\Omega\|\le\|A\|_\infty\le1`. QED.

For equal `a_e=a` and `b_f\le b`, the uniform simplified bound is
\[
\boxed{\|P_s QA_{\mathcal F}\Omega\|^2\le
\min\{1,\frac{32q^2ab}{(3aq-s)^2}\},\quad 0<s<3aq.} \tag{7}
\]

**Important scope:** (6)–(7) are genuine *per-source* all-coupling infrared estimates with **no total-volume factor**. They are useful for small magnetic coupling. Under the prescribed `b_f\asymp h^{-2}` continuum coefficient trajectory, their right sides may become vacuous; this is NOT cutoff-uniform neutral-sector suppression.

## 4. Theorem 4 (a complete non-extensive frame on a restricted electric many-loop band)

Choose `N` pairwise edge-disjoint rhombi `f_1,...,f_N` and retain `a_e=a,b_f=0`. For every subset `S\subset\{1,...,N\}` with `|S|=q`, define
\[
\Psi_S=\prod_{i\in S}\chi_{1/2}(W_{f_i}).
\]

The vectors `\Psi_S` form an orthonormal family of gauge-invariant center-neutral eigenfunctions with energy `3aq`. Therefore
\[
\boxed{S_q:=\sum_{|S|=q}|\Psi_S\rangle\langle\Psi_S|
=P_{\mathcal E_q},\quad
\|S_q\|_{\rm op}=1,\quad
\mathrm{Tr}\,S_q=\binom Nq.} \tag{8}
\]

This is an **exact Parseval frame** for its q-loop excitation subspace, even though the number of sources is polynomially/extensively large. Each source uses exactly `q` elementary Wilson loops, but their components may have arbitrarily large mutual separation. This is not a frame for the entire electric low-energy Hilbert space, which also contains other spin networks; those can be added using the complete spin-network/Wilson-trace algebra.

The theorem exhibits the correct source-counting principle: use an **operator-norm Bessel/frame bound**, not a bound on the trace of the source Gramian, which necessarily grows with spectral multiplicity.

## 5. Theorem 5 (operator-norm frame/infrared criterion without an extensive trace)

For arbitrary finite-volume interacting `H`, let `b_i=QA_i\Omega` be Wilson sources with positive weights `w_i`, and suppose the formal frame operator `S=\sum_iw_i|b_i\rangle\langle b_i|` defines a bounded positive operator. Fix physical `\eta>0`, `p>0`, and uniform constants `c,C>0`. Suppose
\[
P_\eta S P_\eta\ge c P_\eta,\tag{O}
\]
\[
\|P_sSP_s\|_{\rm op}\le Cs^p\qquad(0<s\le\eta).\tag{IR-op}
\]

Then
\[
\boxed{\operatorname{gap}(H)\ge\min\{\eta,(c/C)^{1/p}\}.} \tag{9}
\]

**Proof.** If `P_s\ne0` for some `s\le\eta`, choose a normalized `\psi\in\operatorname{Ran}P_s`. Since `P_s\le P_\eta`, (O) gives `\langle\psi,S\psi\rangle\ge c`, while (IR-op) gives `\langle\psi,S\psi\rangle\le Cs^p`. Hence `s\ge(c/C)^{1/p}`. This excludes spectrum in the claimed open energy interval. QED.

Unlike the previous *trace* criterion, this formulation does **not** accumulate a source-counting factor. In the electric example (8), the source-operator norm is one although its trace is `\binom Nq`. However, (O)+(IR-op) with uniform constants is already a **mass-gap-strength premise**: there is no proof of it for interacting neutral Wilson sources at arbitrary continuum coupling. Its merit is to state the exact non-extensive operator estimate one would need, without misinterpreting per-source bounds as an all-sector theorem.

## 6. Consequences for the requested R3/R2 program

1. A **whole-spectrum** frame cannot consist only of individually fixed-diameter local sources: two distant contractible loops defeat it at `b=0`. Replace it by a graded *multilocal* family (products across separated regions), or explicitly restrict to a properly defined single-excitation sector and prove a separate many-excitation reduction.
2. The strongly magnetic one-face theorem shows why unrenormalized low-spin Wilson sources have no automatic nonzero variance at all couplings. Renormalization must be established from the interacting measure, not inferred from an energy-form upper bound.
3. The all-coupling per-source estimate (6) depends only on the selected faces and adjacent couplings. It **does not** establish physical-cutoff-uniform infrared suppression: at `b\asymp h^{-2}` the estimate loses its force. No claim to the continuum mass gap follows.
4. The q-loop reference frames (8) show how large spectral degeneracy can coexist with a bounded *operator-norm* frame. The corrected all-sector target is (O)+(IR-op), not a global trace bound with an extensive sum.
5. The remaining true mathematical problem is to derive from interacting Wilson dynamics an operator-norm estimate such as (IR-op) on a sufficient, appropriately renormalized multilocal source family, with lower observability (O), and to control the limiting continuum Hilbert space and physical time normalization (R2). Proving both would be a mass-gap theorem, not a routine completion of earlier Ward identities or C5 covariance.

**Literature context.** Thierry Lévy, *Wilson loops in the light of spin networks*, J. Geom. Phys. **52** (2004), 382–397, proves density of the full Wilson-loop trace algebra in finite-graph gauge-invariant continuous observables (DOI: 10.1016/j.geomphys.2004.04.003). This proves qualitative completeness, not (O) with uniform constants. D. A. Yarotsky, *Perturbations of ground states in weakly interacting quantum spin systems*, J. Math. Phys. **45** (2004), 2134–2152, gives a separate weak-interaction stability framework; it does not prove the arbitrary-coupling bounds (O) and (IR-op). The dissertation's geometric `J` and Penrose `C5` covariance do not currently yield the missing bounds. Literal Stage 26 action-level certification also remains conditional on access to `stage7_checkpointed.setup_geometry`.
