# The Singular Boundary — Interior magnetic deletion through dual-bridge factorization

**Research date:** 2026-10-28. **Audit scope:** exact finite, gauge-invariant *nonlinear* SU(2) Wilson Hamiltonians on planar rhombus disks. This report proves a uniform single-face magnetic-deletion bound for every face possessing a private edge **or an incident magnetic dual-graph bridge**, including faces all four of whose edges are shared. It also quantifies the obstruction created by additional magnetic faces that close such bridges. The bound for fully cycle-surrounded Penrose bulk faces, a physical uniform mass gap, source-variance survival, and continuum construction remain **OPEN**. No Gaussian approximation is made in the nonlinear theorem.

## 1. Hamiltonian, link-face graph, and topology

Let a finite simply connected face-complete edge-to-edge rhombus disk have oriented links E, vertices V and magnetic faces F, each of four distinct edges, with each edge belonging to at most two magnetic faces. Work in the full Haar L²(SU(2)^E), with

H = ∑_{e∈E} a_e(−Δ_e) + ∑_{g∈F} b_g(1−p_g),
where p_g=(1/2) Re Tr W_g, a_e>0 and b_g>0, and −Δχ_{1/2}=3χ_{1/2}/4. The ground state is unique, strictly positive, and invariant under all vertex gauge transformations; thus it is physical. For a target face f, let H_f^-=H−b_f(1−p_f), Δ_f=E0(H)−E0(H_f^-), and A_f=∑_{e∈∂f}a_e.

Define the *magnetic edge-dual graph*: vertices are magnetic faces; connect distinct faces when they share a primal link. For every e∈∂f that lies on another magnetic face g, call the dual edge (f,g) a **bridge** when removing it disconnects the magnetic dual graph. An edge e private to f is called a *free portal* after deleting f.

**Topological criterion (BC).** At least one boundary edge e∈∂f is private to f, or its neighboring face g belongs, after deleting the target magnetic face f, to a magnetic edge-connected component containing **no other boundary edge of f**. For a face with no private links, this is equivalent to the presence of an incident dual-graph bridge. The chosen portal component can contain arbitrarily many faces; it need not itself be a leaf or a one-face system.

## 2. Factorization and conditional Haar lemma (exact, nonlinear)

Remove f's magnetic term and partition the *remaining* magnetic faces into their edge-sharing connected components F_1,…,F_k. Their link supports E_j=⋃_{g∈F_j}∂g are pairwise disjoint, since any shared link would join their faces. Every link not in any E_j belongs to a separate free electric-only tensor factor. This partition is by **links**, not vertices: components may share vertices without coupling any link Laplacian or magnetic term. Therefore H_f^- is exactly a tensor sum of independent Hamiltonians H_j on L²(SU(2)^{E_j}) and free-link electric Laplacians. Its strictly positive unique full-link ground state is the tensor product of the unique positive ground states of those factors.

Each component H_j is invariant under the complete local gauge group acting on its *own* edges, including at vertices shared with other components. By uniqueness, its probability law is invariant under these vertex gauge transformations. For any component edge e and either endpoint, such a transformation left- or right-multiplies U_e by arbitrary k∈SU(2). Therefore **the marginal law of every single component link U_e is exactly Haar**, irrespective of magnetic couplings, component size, or proximity to the boundary. A free link is Haar as well.

Under criterion (BC), choose an edge e₀∈∂f whose deleted-Hamiltonian component contains no other edge of ∂f. Its link variable U_{e₀} is Haar and is independent of *all the other boundary link variables of f*, because they live in different tensor factors. Thus the ordered product W_f is exactly Haar under the full deleted vacuum ν_f^-. In particular, its class trace p_f has density (2/π)√(1−p²) dp on [−1,1], with

E_- p_f^(2m+1)=0,  E_- p_f^(2m)=Catalan_m/4^m.

The stronger property, beyond the earlier center-flux Z₂ parity, is the **full Haar marginal of the missing-face holonomy**. It relies on an isolated portal *component*, not on a private edge. The marginal is not asserted Haar when all boundary portal edges belong to the same deleted magnetic component.

## 3. Theorem BD-1 — Uniform nonlinear bulk bridge magnetic-deletion bound

**Theorem.** For every finite nonlinear SU(2) Hamiltonian as above, and target face satisfying (BC), regardless of how many other faces are present or how large the other magnetic couplings are,

    0 <= Δ_f <= (3/(2√2)) √(A_f b_f).                 (BD-1)

**Complete variational proof.** Let Ω_f^- be the positive normalized deleted vacuum and κ>0. Multiply it by the strictly positive **gauge-invariant** central face factor gκ(W_f)=exp(κ p_f), normalizing Ψκ=gκΩ_f^-/||gκΩ_f^-||. Gauge invariance holds because p_f is a closed Wilson trace and Ω_f^- is Gauss invariant. The exact ground-state transform for H_f^- gives

 〈Ψκ,(H_f^-−E_f^-)Ψκ〉 = E_-[Γ(gκ)]/E_-[gκ²].

Every incident link contributes |∇_e p_f|²=(1−p_f²)/4. Hence Γ(gκ)=(A_f κ²/4)(1−p_f²)gκ². From section 2, **p_f has exact Haar law** under ν_f^-, so its gκ-tilted law is e^{2κ p} (2/π)√(1−p²)dp normalized. Put rκ=Eκ p. Haar integration by parts using Δp=−3p/4 yields Eκ(1−p²)=3 rκ/(2κ), and therefore kinetic increment 3A_f κ rκ/8 ≤ 3A_f κ/8.

For the magnetic part, Eκ(1−p)=1−rκ≤3/(4κ) for every κ>0. To prove this **globally**, write u=1−p∈[0,2]. Its tilted Haar law is proportional to e^(−2κu)u^(1/2)√(2−u)1_[0,2](u)du. Compare with a Gamma(shape=3/2, rate=2κ) random variable U. Multiplying the gamma density by the nonincreasing weight w(u)=√(2−u)1_[0,2](u) lowers the expectation of any increasing function; specifically E[U w(U)]/E[w(U)]≤E U=3/(4κ). This proves the magnetic estimate without a Bessel approximation.

Therefore

 Δ_f ≤ inf_{κ>0} [3A_f κ/8 + 3b_f/(4κ)]
     = (3/(2√2)) √(A_f b_f),

at κ=√(2b_f/A_f). QED. No additional cross-gradient or interaction terms are omitted: they vanish exactly from the deleted-ground-state transform, and the necessary weighted face law is exactly Haar by section 2. **All four links of f may be shared.**

## 4. Theorem BD-2 — Extreme-defect tail for dual-bridge interior faces

The existing exact single-face ground-state exponential-moment identity is

 E_{Ω_h} exp(s d_f) ≤ exp{ Δ_f /√(A_fb_f/8) · artanh[s√(A_f/(8b_f))] },  0≤s<√(8b_f/A_f).

Using BD-1 and choosing s=√(2b_f/A_f) gives

 **P_{Ω_h}(d_f≥δ) ≤ 3^(3/2) exp[−δ√(2b_f/A_f)].**  (BD-2)

If b_f≥β h^(−2), A_f≤4a*, δ_h=h^(3/4), then

 **P_{Ω_h}(d_f≥h^(3/4)) ≤ 3^(3/2) exp[−√(β/(2a*)) h^(−1/4)].**  (BD-3)

For any set of N_h faces satisfying (BC), the probability that at least one exceeds the threshold is at most N_h times the right side, with no independence assumption. If N_h≤C h^(−m), this tends to zero faster than any power of h. In particular **every face of a dual-tree rhombus disk** satisfies (BC), so the single-face extreme-defect estimate is simultaneous and uniform over arbitrary-size dual-tree families. Such trees need not constitute a fixed-positive-area, cycle-rich Penrose disk; no full-bulk conclusion is claimed.

## 5. Theorem BD-3 — Robust comparison when weak magnetic terms close dual bridges

Let H_0 contain the same electric terms and a subset of magnetic terms such that the selected f satisfies (BC). Restore a collection B of extra magnetic face terms W=∑_{g∈B}b_gd_g, with W≥0 and ||W||≤2B_sum, B_sum=∑_{g∈B}b_g. Denote the original H=H_0+W and the corresponding deleted Hamiltonians H_f^-=H_0^--b_f d_f+W if H_0 includes f, i.e. simply H_f^-=H_0-b_fd_f+W.

The min-max bounds E0(H_0+W)≤E0(H_0)+2B_sum and E0(H_0−b_fd_f+W)≥E0(H_0−b_fd_f) give

 **Δ_f(H) ≤ (3/(2√2))√(A_fb_f)+2B_sum.**  (BD-4)

This is an exact **nonlinear cycle-closing stability bound**, not a perturbation series. If B_sum=o(h^(−5/4)) with b_f≈h^(−2), it suffices to recover superpolynomial defect-tail exclusion at δ_h=h^(3/4) (with h-dependent rate), provided the positive h^(−1/4) exponent dominates the additive correction. In the physical Penrose bulk each removed full-strength magnetic term is generally Θ(h^(−2)), so BD-4 alone is **not** sufficient for cycle-rich full-lattice refinement. It quantifies exactly which magnetic loop-closing interactions must be controlled by a sharper comparison.

## 6. Theorem BD-4 — Exact nonlinear dual-cycle susceptibility gate

Let H_0 be a magnetic Hamiltonian containing f in which criterion (BC) holds. Let W=∑_{g∈B}b_gd_g≥0 be the magnetic interactions that close the relevant face-dual bridges in the complete model. For u∈[0,1] and t∈[0,b_f], put H(u,t)=H_0−b_fd_f+t d_f+uW, E(u,t)=E_0(H(u,t)), and denote its strictly positive physical ground state by Ω_{u,t}. At finite volume the ground energy is differentiable in both parameters and analytic on a neighborhood of each real (u,t). Denote by Q=1−|Ω><Ω|, K=H−E, and G=Q K^{-1}Q the physical reduced resolvent.

The exact mixed Hellmann–Feynman/Kato identity is

  ∂_u∂_t E(u,t) = −2 Re〈Qd_f Ω_{u,t}, G_{u,t} QW Ω_{u,t}〉.    (BD-5)

Although G≥0, this *cross* quadratic form is not known to have a fixed sign. Let Δ_f(u)=E(u,b_f)−E(u,0). Integrating the exact mixed identity twice yields

 **Δ_f(1) = Δ_f(0) −2∫₀¹du∫₀^{b_f}dt Re〈Qd_fΩ_{u,t},G_{u,t}QWΩ_{u,t}〉.**  (BD-6)

By BD-1, Δ_f(0)≤(3/(2√2))√(A_fb_f). Define the *negative cycle-closing susceptibility budget*

 N_f=2∫₀¹du∫₀^{b_f}dt [−Re〈Qd_fΩ_{u,t},G_{u,t}QWΩ_{u,t}〉]_+≥0.

Then the following **unconditional bound with an explicitly defined remainder** holds for the *complete nonlinear model*:

 **Δ_f(1) ≤ (3/(2√2))√(A_fb_f)+N_f.**     (BD-7)

If an independent argument established N_f=O(h^(−1) polylog(1/h)) at physical scaling, it would prove the desired bulk deletion bound. The weaker condition N_f=o(h^(−5/4)) would still be sufficient for stretched-exponential rarity of d_f≥h^(3/4) under the single-face Laplace bound. Neither bound on N_f is proved here. In particular, positive susceptibility on the diagonal does **not** imply positivity of the mixed response. The operator-norm comparison of BD-3 bounds N_f only through a coarse O(∑_{g∈B}b_g) replacement; physically strong magnetic cycle-closing terms require a better dynamical estimate.

**Interpretation:** the geometry separates into an exactly solvable nonlinear *bridge-deleted* reference and an exact **physical, mixed inverse-energy susceptibility** measuring the cost of reconnecting the magnetic dual cycles. This is not a Gaussian approximation, and the remainder is not assumed negligible.

## 7. Exact spatial fixtures and proof-integrity boundary

**Five-face interior star:** Take five unit square rhombi with face centers (0,0), (±1,0), (0,±1), keeping only their five magnetic faces. The center has all four boundary links shared, hence *no private edge*. The adjacent four neighbors have mutually edge-disjoint link sets; after deleting the center, the Hamiltonian splits into four nonlinear interacting one-plaquette subsystems. The missing center holonomy is exactly Haar and BD-1–BD-3 hold despite every center edge being shared. The square star is a rhombus-disk geometry fixture, not claimed to occur as that exact Euclidean shape in the Penrose tiling.

**Canonical three-face Penrose spatial seed:** Reconstruct the Z⁵ rhombus incidence from the source verifier. Its dual graph is a three-face path; all incidence dual links are bridges, so BD-1 applies to every face. This fixture is spatial only; it does not validate the original Stage 7/26 temporal action or Q14.

**Cycle-rich control:** A 3×3 full square-rhombus grid has a central face of degree four whose neighbors all remain connected through the surrounding ring after deletion. No incident dual edge is a bridge. The argument gives *no bound beyond the earlier universal Δ_f<b_f* for that center, and does not imply a uniform estimate for a complete, cycle-rich Penrose disk.

## 8. Classification and next obligation

**NEWLY PROVED FOR THE TRUE NONLINEAR SU(2) VACUUM:** the exact Haar missing-holonomy lemma when a removed magnetic face has an isolated magnetic component portal; the uniform square-root deletion-energy bound for interior dual-bridge faces; the resulting stretched-exponential true-vacuum defect tail; and stability under bounded additional magnetic loop-closing terms. This improves the preceding private-edge theorem in a genuinely non-boundary regime, with constants independent of other component sizes/couplings.

**NOT PROVED:** the analogous Haar or uniformly bounded conditional missing-face distribution for a face surrounded by dual cycles; control of loop-closing couplings Θ(h^(-2)) at the physical point; all-face sparse-defect rarity on a complete Penrose disk; connected Wilson-angle variance at fixed support; an all-sector mass gap, nonlinear quartic resolvent or continuum reconstruction. The next truly open object is the **negative mixed-resolvent susceptibility budget N_f in BD-7**, which exactly measures the energy cost of closing magnetic dual cycles; equivalently one needs control of the associated change in missing-face holonomy distribution. Center-flux Z₂ symmetry alone does not supply continuous SU(2) Haar averaging.

No Monte Carlo or historical binary modifications. All outputs in this package are independently derived for the declared finite model.