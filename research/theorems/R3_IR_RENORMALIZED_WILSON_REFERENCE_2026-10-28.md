# R3-IR / R2 — Renormalized Wilson sources: a reference Gaussian continuum and interacting normalization obstruction

**Audit date:** 2026-10-28. **Evidence categories:** independently proved exact electric-reference statements; conditional interacting spectral obstruction; new construction is **not** a continuum interacting SU(2) gauge theory. Original historical data unchanged, no simulations. The paper's continuum *geometry and coefficient trajectory* are assumptions until cross-checked against all Stage 7/26 sources.

## Primary input, provenance and reused historical theorem

Previously proved `FORMAL_FRAME_AUDIT.md` (2026-10-26), Theorem F1, gives the first positive energy moment of a physical-area-smeared **fundamental** Wilson trace at the declared geometric coefficients. Existing `research/theorems/R3_IR_MESOSCOPIC_INTERIOR_CURVATURE_2026-10-28.md` (MI-3) and `research/theorems/R3_IR_MESOSCOPIC_WILSON_LOOP_DENSITY_2026-10-28.md` (LW-4) give mesoscopic area-averaged flatness, under specified assumptions. No novelty is claimed for those source results in isolation.

Assume a sequence of connected finite face-complete Penrose rhombus patches G_h, with physical edge h->0, all faces intersecting each fixed compact support interior to G_h, area A_f=h² σ_f, σ_f∈{σ_-=sin π/5,σ_+=sin 2π/5}. Face centers x_f and bounded on-site electric coefficients a_*≤a_e(h)≤a^* independent of h (true for the declared geometric dual-area prescription; **not** yet reverified as the literal Stage26 action). Each face contains four distinct links and any link at most two faces. Physical gauge-invariant Hilbert space is the Gauss-invariant subspace of L²(SU(2)^E). Write p_f=(1/2)Tr_{1/2} W_f, with real fundamental character, and κ_f=(3/4)Σ_{e∈∂f}a_e∈[3a_*,3a^*].

For smooth compactly supported real test function φ define

F_h^(α)[φ]=h^(−α)Σ_f A_f φ(x_f)(p_f−⟨p_f⟩_{Ω_h}),

where Ω_h is the normalized ground state at the specified magnetic couplings, or Ω_E=1 for the electric-only reference b_f=0. Keep α explicit; it is NOT yet a renormalized field dimension.

## Theorem RN-1 — a noncircular interacting normalization obstruction

Under declared geometric Wilson coefficients b_f(h)=4/(g₃² A_f), the ground-state transform and the historical F1 estimate yield

M1_h(F_h^(α)[φ]):=⟨F_h^(α)Ω_h,(H_h−E0)F_h^(α)Ω_h⟩ ≤ 2φ_g g₃² h^(2−2α) Σ_f A_f |φ(x_f)|²,

where φ_g=σ_+/σ_-=(1+√5)/2. For fixed test support the area sum is uniformly bounded.

If α<1 then M1_h→0. If the vacuum variance V_h=||F_h^(α) Ω_h||² satisfies liminf V_h>0, the physical Rayleigh principle implies gap(H_h)≤M1_h/V_h→0. Further, for each t≥0,

0≤V_h−C_h(t)≤t M1_h,

where C_h(t)=⟨F_h^(α)Ω_h,e^(−t(H_h−E0))F_h^(α)Ω_h⟩. Hence if V_h stays bounded and tends to v>0, C_h(t)→v for every fixed t. For every η>0, the positive spectral measure μ_h satisfies

μ_h((0,η])≥V_h−M1_h/η;

thus any finite weak spectral limit has all mass at zero energy. **This is a necessary condition, not an interacting gap proof nor proof that V_h is nonzero.** To have nonzero finite variance and a regulator-uniform positive gap in this source class, α≥1 is necessary, under these hypotheses.

## Theorem RN-2 — spatial flatness constrains α<1/2

If supp φ lies inside a fixed physical interior ball D_R for all sufficiently small h, and previous MI-3 applies with R fixed, then Σ_{f∈D_R}A_f E_{Ω_h} d_f=O(h). Let X_h=Σ_f A_f |φ(x_f)|d_f and C_φ(h)=Σ_f A_f|φ(x_f)|. The latter is bounded and 0≤X_h≤2C_φ(h). Since Σ_f A_f φ(x_f)p_f differs by a constant from −Σ_f A_f φ(x_f)d_f,

Var_{Ω_h}(Σ_f A_f φ(x_f)p_f) ≤ E X_h² ≤2 C_φ(h) E X_h=O(h).

Thus V_h(F_h^(α)[φ])=O(h^(1−2α)); in particular all α<1/2 yield a trivial zero-variance field in the interacting vacuum. At 1/2≤α<1 a positive limiting variance is not excluded by this spatial estimate, but RN-1 shows it cannot coexist with a uniform physical mass gap. The candidate α=1 has no variance bound adequate to conclude either triviality or nontriviality from the current inequalities.

## Theorem RN-3 — exact electric-reference spectral measures and nontrivial covariance

At b=0 the ground vector is Ω_E=1. Fundamental SU(2) Haar character orthogonality gives

⟨p_f⟩_0=0,   ⟨p_f p_g⟩_0=δ_fg/4,

for distinct simple faces, because a unique edge belonging to just one face kills the off-diagonal Haar integral. Moreover H_E p_f=κ_f p_f. Therefore for the critical source F_h^(1)[φ], the EXACT finite-regulator vacuum connected correlator is

C_h^E(φ,ψ;t)=1/(4h²) Σ_f A_f² φ(x_f)ψ(x_f) exp(−κ_f |t|),  t∈R.

Its exact positive excitation spectral measure for φ=ψ is

μ_{h,φ}^E=1/(4h²)Σ_f A_f² φ(x_f)² δ_{κ_f}.

Let the deterministic positive measures Λ_h=Σ_f (A_f²/h²) δ_{(x_f,κ_f)}=Σ_f A_f σ_f δ_{(x_f,κ_f)} on a compact physical support times [3a_*,3a^*]. They are uniformly bounded there. Every spatial-refinement sequence has a subsequence Λ_{h_j}⇀Λ. The spatial marginal of Λ obeys σ_- dx≤(π_x)_* Λ≤σ_+ dx on compact interior supports, by ordinary area quadrature on tilings. In particular the marginal is nonzero and Λ gives a nontrivial, positive definite limiting covariance

C_E(φ,ψ;t)=1/4 ∫ φ(x)ψ(x)e^(−κ|t|)dΛ(x,κ).

For nonzero real φ, its equal-time variance obeys

σ_- /4 ∫φ² dx ≤ C_E(φ,φ;0) ≤ σ_+/4 ∫φ² dx,

and all its spectral weight lies in the strictly positive electric band [3a_*,3a^*]. This yields a nontrivial **subsequential electric-reference** continuum covariance with common reference gap ≥3a_*. **No full-sequence uniqueness** is claimed without a local patch-frequency argument for the coefficients κ_f and shape variables.

## Theorem RN-4 — electric-reference Gaussian finite-dimensional distributions, not just two-point functions

In the stationary electric-reference Markov process (independent SU(2) link Brownian motions with Haar starting law), let p_f(t) be a face trace. Each finite-time random vector (p_f(t_1),...,p_f(t_m)) depends only on the four link Brownian paths on ∂f. These face vectors have a dependency graph of maximum degree four, because each edge belongs to at most two faces. Each source contribution to h^(−1)Σ_f A_f φ(x_f) p_f(t) has magnitude O(h) for compactly supported bounded φ, and the number of contributing faces is O(h^(−2)). For any fixed order q≥3, only connected q-tuples in that dependency graph have nonzero joint cumulants; there are O_q(h^(−2)) of them, and each cumulant is bounded by C_q h^q. Hence the q-th cumulant of any fixed linear combination of finitely many test functions and Euclidean times is O_q(h^(q−2))→0. The first cumulant is zero; the second cumulant has the exact limit RN-3. Moment convergence and the determinate Gaussian moment problem prove joint convergence in distribution to a centered Gaussian Euclidean field with covariance C_E above, along the same subsequence.

This is a **genuinely nonzero Gaussian spatially-white electric reference field** at physical time with spectrum contained in [3a_*,3a^*]. It is not the fully interacting Penrose Wilson continuum: at b_f=4/(g₃² A_f), link Brownian independence is lost, and neither Gaussianity, nonzero variance nor source convergence is established. The reference construction uses no Monte Carlo and is not a replacement for historical simulations.

## Immediate next noncircular gate

Obtain a regulator-uniform interacting variance *lower* bound (and preferably an upper bound) for h^(−1)Σ_f A_f φ(x_f)(p_f−⟨p_f⟩_h), or show an exact obstruction. The known first-moment bound alone cannot do so; nor can mesoscopic mean flatness imply a lower variance. Next establish physical-time multi-source convergence and source-inserted decay independently. Do not infer an interacting continuum from the Gaussian electric limit. An absolute-continuity/interacting comparison at magnetic b_f~h^(−2) needs its own nonperturbative theorem; naive electric-perturbation norm fails.

## Sources

- Historical `FORMAL_FRAME_AUDIT.md` (2026-10-26): theorem F1, first-moment bound, and electric spin-network reference; source-derived, not claimed as new here.
- `research/theorems/R3_IR_MESOSCOPIC_INTERIOR_CURVATURE_2026-10-28.md` and `research/theorems/R3_IR_MESOSCOPIC_WILSON_LOOP_DENSITY_2026-10-28.md`: regional mean curvature and vacuum mean-square flatness.
- J. Mazáč, *Patch frequencies in rhombic Penrose tilings*, Acta Cryst. A79 (2023), 399–411, DOI 10.1107/S2053273323004990, for possible eventual verification of unique local patch frequencies. The proof RN-3 uses only subsequential measure compactness and tiling area bounds, not this paper's detailed frequency claims.