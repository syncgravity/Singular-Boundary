# The Singular Boundary — Many-face nonlinear strong-field shared-edge theorem and a uniform Gaussian signed-source/time audit

**Date:** October 28, 2026. **Project:** R3-IR. **Research branch:** `audit/2026-10-28-independent-reconstruction`.

**Evidence status.** (i) New **fixed-finite-volume nonlinear SU(2) theorem**: for every fixed finite face-complete, simply connected, edge-connected rhombus disk, its exact physical ground-state strong-magnetic covariance between **every two** plaquettes has a strictly positive leading coefficient, controlled by the square root of the shared-edge kinetic matrix. (ii) New **arbitrary-size Gaussian tangent theorems**: even signed source weights have a cancellation-resistant two-sided variance at the expected scaling when all electric coefficients are equal; fixed-physical-time correlations disappear for all multiplicative normalizations with bounded nonzero equal-time variance. (iii) **Not proved:** uniform nonlinear strong-field expansion for F_h∼h^-2, equality to Stage7/26 action, any physical positive continuum mass gap, or full reconstruction. Original user archives not modified. No Monte Carlo.

## 1. Model and incidence on a true spatial rhombus disk

Let G be a finite embedded, simply connected, edge-connected rhombus disk, with F faces, E links and V vertices; fix local SU(2) gauge transformations at **every** vertex. Euler implies E−V+1=F. Choosing a maximal spanning tree leaves F independent SU(2) face-holonomy variables g_f, subject to simultaneous global conjugation. The reference measure on these variables is product Haar. The kinetic energy does **not** factorize: link derivatives on each shared edge couple its two adjacent face variables, with opposite incidence signs.

Let B be the F×E oriented face–edge incidence matrix, with four entries ±1 per face, and no more than two nonzero entries in each edge column. Each internal edge appears with opposite signs in its two face rows. Let a_e>0, and define

    M = B diag(a_e) B^T.

Since the face boundaries are linearly independent on a simply connected disk, M is positive definite. If the dual face-adjacency graph is connected, then M is an irreducible symmetric M-matrix: M_ff=Σ_{e∈∂f}a_e>0, M_fg=−a_shared<0 if faces f,g share an edge, and zero otherwise. Under uniform a_e=a, M=a(4I−A_dual) and 0<M≤8aI by Gershgorin.

The **nonlinear**, physical Wilson Hamiltonian is

    H_b = Σ_e a_e (−Δ_e) + b Σ_f d_f,
    d_f=1−p_f,  p_f=(1/2)ReTr W_f,  b>0,

on the gauge-invariant Hilbert space, with fundamental SU(2) Casimir 3/4. b is common to all faces. Its finite-volume positive normalized ground state is Ω_b. For each fixed graph all constants in the next limit may depend on F and M.

## 2. Theorem MF-1 — Fixed-F **nonlinear** SU(2) strong-magnetic covariance, all face pairs

For every fixed G as above, the strong-field limits hold:

    E0(b)/√b → (3/(2√2)) Tr √M,
    √b E_{Ω_b} d_f → (3√2/8)(√M)_ff,
    b Cov_{Ω_b}(d_f,d_g) → (3/16)[(√M)_fg]^2.          (MF-1)

The sign is unchanged when d_f is replaced by p_f in both covariance arguments. This is a theorem for the **nonlinear physical vacuum**, not a direct Gaussian substitution. The right-hand side is the covariance of its *proved* limiting oscillator. For f≠g with connected dual graph the coefficient is strictly positive, including nonadjacent face pairs.

**Proof with dependence made explicit.** (a) Maximal-tree gauge fixing is a smooth global group-coordinate parametrization modulo the residual simultaneous conjugation; its local kinetic principal symbol at g_f=I is M⊗I_3. Smoothness and strict positive a_e give a coercive elliptic form on the compact gauge-fixed configuration space. (b) In exponential coordinates g_f=exp(i x_f·σ/2), one has d_f=|x_f|²/8+O(|x_f|⁴). For fixed F, trial ψ_b=Z_b^(-1/2) exp(−κ√b Σ_f d_f), κ>0 fixed, gives E0(b)≤C_G√b from its gradients and magnetic expectation. This bound depends on the fixed graph. (c) With X=Σ_f d_f, the exact Γ(X)≤4a_max X and H_b≥b X produce, for fixed 0<t<1/√a_max and F_b(t)=E_{Ω_b}e^{t√b X},

    (1−a_max t²) F_b'(t) ≤ (E0(b)/√b) F_b(t).

Integrating yields uniformly in b at this **fixed graph**

    F_b(t)≤exp[(C_G/√a_max) artanh(t√a_max)].

Thus b^{1/2}X has uniform exponential moments. The rescaling y_f=b^{1/4}x_f has Gaussian-tight tails and uniform all-fixed-degree polynomial moments. (d) Unitarily transform the scaled physical quadratic forms b^{-1/2}H_b to the y coordinates, including Haar Jacobian; they converge on C_c^∞(R^{3F}) to

    H_∞=−Σ_fg M_fg ∇_{y_f}·∇_{y_g}+(1/8)Σ_f |y_f|²

on simultaneous-SO(3) invariants. The exterior-region mass is small by (c), and the rescaled local kinetic form supplies H¹_loc compactness; hence Rellich and matching variational liminf/limsup identify the unique normalized positive Gaussian oscillator vacuum (no assumption that Ω_b is Gaussian). It has color covariance Σ_y=√2√M. (e) By the moment bounds, the Taylor expansion

    b^{1/2}d_f=|y_f|²/8+O(b^{-1/2}|y_f|⁴)

converges in second moments. Wick's identity for three colors yields Cov(|y_f|²/8,|y_g|²/8)=(3/32)Σ_{y,fg}²=(3/16)[√M_fg]². This proves MF-1. Fixed-index excited energies likewise converge by the min–max principle at this **fixed** graph; the scalar physical oscillator first excitation is √(2λ_min(M))√b+o(√b). The constants are not uniform in F.

**Strict positivity at all distances.** For an irreducible symmetric M-matrix, (tI+M)^{-1} is entrywise strictly positive for every t>0. The functional-calculus integral

    √M=(1/π)∫_0^∞ t^{-1/2} M(tI+M)^{-1}dt

shows for f≠g

    (√M)_fg=−(1/π)∫_0^∞ t^{1/2}(tI+M)^{-1}_{fg}dt<0.

Therefore the square in MF-1 is positive for **every** pair of distinct faces on an edge-connected disk. This is a *leading-coefficient* assertion, not an all-b positive covariance theorem or a uniform-in-F lower bound for distant pairs.

## 3. Theorem MF-2 — Nonlinear fixed-graph signed sources and strict diagonal dominance of the asymptotic matrix

For a fixed graph and any real q=(q_f), the nonlinear strong-field limit of Q=Σ_f q_f d_f is

    lim_{b→∞} b Var_{Ω_b}(Q)=(3/16) q^T K q,
    K=(√M)∘(√M),                                      (MF-2)

where ∘ is entrywise (Hadamard) multiplication. Schur's theorem implies K is PSD; more is true when **all electric coefficients equal a**.

**Uniform signed coercivity of the limiting matrix, valid for every F.** Then M_ff=4a, M≤8aI, and (M²)_ff=(16+deg_dual(f))a²≤20a². The elementary scalar inequality

    √x ≥ x/√L + x(L−x)/(2L^(3/2))  for 0≤x≤L

holds by putting u=√(x/L) and factoring u−u²−u²(1−u²)/2 = u(u−1)²(u+2)/2≥0. Use functional calculus at L=8a and take diagonal entries to obtain

    (√M)_ff ≥ [4a + (32a²−20a²)/(16a)]/√(8a)
             = (19/4)√(a/8).

Hence K_ff≥361a/128. The identity Σ_g K_fg = (M)_ff=4a gives the exact offdiagonal row sum Σ_{g≠f}K_fg=4a−K_ff. Because K_fg≥0, the elementary inequality 2|q_fq_g|≤q_f²+q_g² implies

    q^T K q ≥ Σ_f[2K_ff−4a]q_f² ≥ (105a/64)Σ_f q_f²,
    q^T K q ≤ Σ_f (Σ_g K_fg)q_f² =4a Σ_f q_f².

Thus **for all real signed q and all sizes F**

    (315a/1024)Σ q_f² ≤ lim_{b→∞} b Var_{Ω_b}(Σ q_fd_f)
                     ≤ (3a/4)Σ q_f².                 (MF-3)

This shows that long-distance cross terms cannot cancel the leading signed-source variance in the **fixed-F then b→∞ order of limits**, uniformly in F at the level of coefficients. There is no claim that the nonlinear *remainders* are uniform in F.

## 4. Theorem MF-3 — Full shared-edge Gaussian tangent: sharp equal-time scaling, all signed tests

Independently of strong-field nonlinear remainder control, consider the exactly defined tangent oscillator on any finite disk:

    H^G_{h}=−Σ_fg M_fg ∇_{y_f}·∇_{y_g} + (b/8)Σ_f |y_f|²,
    b=β h^(-2), a_e=a,

with color covariance Σ=(2/b)^(1/2) √M. For arbitrary real |q_f|≤q_* and normalization α, the centered area-type source is

    A^G_{h,α}=(h^(2−α)/8)Σ_f q_f(|y_f|²−3Σ_ff).

Its **exact** variance is

    V^G_{h,α}=(3h^(6−2α)/(16β)) q^T K q.        (MF-4)

For Fh²≤A0 and Q_{2,h}=h²Σ_f q_f², the preceding sharp signed bound yields

    (315a/(1024β)) Q_{2,h} h^(4−2α)
     ≤ V^G_{h,α} ≤ (3a/(4β))Q_{2,h} h^(4−2α).  (MF-5)

If q arises from a fixed nonzero smooth real face test on positive physical area and 0<liminf Q_{2,h}≤limsup Q_{2,h}<∞, this is a **two-sided Θ(h^(4−2α)) bound** valid for signed q and for **any** growing rhombus-disk family, including Penrose disks. At the distinguished α=3/2, it is Θ(h). At α=2, it is Θ(1). It demonstrates absence of cancellation even between distant faces *in the tangent theory*.

## 5. Theorem MF-4 — Fixed-time Gaussian contact-only limit and multiplicative-normalization obstruction

The exact Euclidean two-point function is, for t≥0,

    C^G_{h,α}(t)=(3/32)h^(4−2α)
       Σ_{fg} q_fq_g[Σ e^(−t√(bM/2))]_{fg}².       (MF-6)

It is nonnegative even for signed q by the Schur product theorem. For any **fixed t>0**, use |q_f q_g|≤q_*² and the Frobenius norm:

    C^G_{h,α}(t)≤[3q_*² h^(4−2α)/(16b)] Tr[M e^(−2t√(bM/2))].

For each eigenvalue λ≥0 of M put u=√(bλ/2). Then λ e^(−2tu)=(2/b)u²e^(−2tu)≤(2/(b e²t²)). There are F eigenvalues, so

    0≤C^G_{h,α}(t) ≤ (3q_*²/(8β²e²t²)) (Fh²) h^(6−2α)
                      ≤ (3q_*²A0/(8β²e²t²)) h^(6−2α).  (MF-7)

No Cheeger spectral gap, Gaussian mean-field assumption beyond the **declared exact tangent model**, or eigenvalue-counting theorem is needed for this bound. It applies on full growing connected shared-edge face complexes.

**Sharp interpretive consequence.** If 0<liminf Q_{2,h} and Q_{2,h} bounded, then:

- α<2: V^G_{h,α}→0.
- α=2: 0<c≤V^G_{h,2}≤C but C^G_{h,2}(t)=O_t(h²)→0 for every fixed t>0. The equal-time covariance is nonzero, but fixed-physical-time covariance disappears: a *contact-time/UV-escape* source, not a nontrivial continuous Hilbert-vector Euclidean two-point limit.
- 2<α<3: V^G_{h,α}→∞ yet C^G_{h,α}(t)→0 for every t>0.
- α≥3: MF-7 alone does not force fixed-time decay, while V^G_{h,α}→∞.

**Therefore no purely multiplicative normalization α of this local quadratic-plaquette source yields both bounded nonzero equal-time variance and nonzero fixed-physical-time two-point correlation in this complete shared-edge Gaussian tangent theory.** This is a model-specific statement; it does NOT rule out distribution-valued composite fields, temporal smearing, subtractions/mixing, nor a different nonlinear interacting continuum limit. It shows the difficulty is not repaired simply by retaining shared electric edges in the tangent model.

## 6. Proof-integrity boundary and next nonlinear obligation

**Proved for actual nonlinear SU(2) vacuum on each fixed F:** MF-1 strong-magnetic covariance for all face pairs, strict positivity of pairwise leading coefficients, and MF-3 signed-source coefficient bounds for uniform electric coefficients. This generalizes the earlier two-face theorem at the same order of limits; it does **not** justify evaluating MF-1 at b_h=β/h² when F_h→∞.

**Proved only for explicit full shared-edge Gaussian tangent at arbitrary F_h:** MF-4/MF-5 signed variance two-sided bounds and MF-6/MF-7 time-decay; the obstruction to a single multiplicatively-renormalized continuous-time source.

**Not proved:** regulator-uniform nonlinear covariance comparison or error bound; its sign at fixed h for general magnetic couplings; positive lower spectral weight at fixed physical energy; regulator-uniform physical mass gap; quartic resolvent; Stage7/26 Hamiltonian identification; full continuum.

**Precisely needed next input:** a **quantitative many-face nonlinear remainder**, uniform for F_h≈h^-2 at b_h≈h^-2, controlling source four-point moments and Euclidean dynamics, or another direct interacting source-energy comparison that makes no Gaussian approximation. Strong-field convergence for every fixed F and uniform bounds for limiting coefficients are not such a remainder. One must keep the order of limits explicit.

## 7. Verification

`verify_many_face_gaussian.py` is an independently reproducible deterministic NumPy/SymPy/SciPy verifier of the authentic three-face, ten-edge spatial Penrose seed, the exact dual spectrum 4,4±√2, the scalar square-root lower bound, the uniform signed Gershgorin factor 105/64, test vectors on a complete growing rhombus grid, and the Euclidean time estimate. It checks finite algebra and constants, not the analytic nonlinear Γ-limit or Stage7/26 temporal Q14. No Monte Carlo and no historical file modifications.