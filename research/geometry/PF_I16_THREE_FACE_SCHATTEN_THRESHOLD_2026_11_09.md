> **GEOMETRY ERRATUM (2026-11-09):** The particular *three opposite/adjacent coordinate-cube face* illustration below is **not** an authentic accepted cut-and-project motif. The two opposite ij faces cannot simultaneously pass strict PF-I11 perpendicular-triangle membership. **Do not use that cube illustration as source evidence.** The six-label trivalent spin-network topology and original-link strand lengths 3,3,1,1,1,1 **are nevertheless authenticated** by the distinct three-face witness [PF-I16 authenticated source motif and sharpened incidence](PF_I16_AUTHENTICATED_THREE_FACE_MOTIF_AND_SHARP_INCIDENCE_2026_11_09.md), present in all eight independently replayed original source sizes. The sharp abstract Schatten threshold p>3 remains valid for that authenticated motif. The source replay also improves genuine-face incidence from 8 to 2. This erratum supersedes the unaccepted cube example only, preserving the historical derivation for auditability.

# PF-I16 — Exact three-face Gauss-invariant Schatten threshold

**2026-11-09; new conditional source-motif theorem, NOT a mass-gap result.** Full proof, local original-Z5 incidence enumeration, exact SU(2) label verifier, cutoff logs and SHA-256 manifest: `/The Singular Boundary/Proof Audits/PF_I16_THREE_FACE_SCHATTEN_2026_11_09.zip`. This theorem concerns the original elementary-coordinate rhombus motif **if accepted by the cut-and-project window**. This acceptance has NOT been independently certified in each historical PF-I11 crop.

Take three unit Z5 elementary squares using directions i,j,k: the ij square at m, ik square at m, and parallel ij square at m+e_k. They have pairwise face-edge overlap graph f0—f1—f2 (f0 and f2 edge-disjoint), 8 original vertices, 10 original links, three independent cycles, and relative height levels 0,1,2,3 (compatible with the source 1–4 permitted heights after an appropriate base shift, but not itself acceptance-window proof).

Upon suppressing degree-two vertices **solely to label spin networks**, the graph has four trivalent vertices and six strands `(L,a,t,u,b,R)` with unit-link weights `(3,1,1,1,1,3)`. Gauge-invariant normalized spin networks are uniquely indexed by six nonnegative twice-spin labels satisfying triangle/parity constraints at `(L,a,t)`, `(L,a,u)`, `(R,b,t)`, `(R,b,u)`. The exact electric eigenvalue is
[
E_{L,a,t,u,b,R}=	frac14[3L(L+2)+a(a+2)+t(t+2)+u(u+2)+b(b+2)+3R(R+2)].
]
The all-zero state is the unique vacuum; the pure-electric gap is 3 at unit coefficients (PF-I15 cycle criterion).

**Theorem (sharp Schatten threshold).** On this fixed finite 3-face SU(2) Gauss-invariant Hilbert space,
[
oxed{K^{-1}P_0inmathcal S_piff p>3.}
]
For upper convergence: at max spin label r there are at most `(r+1)^6-r^6=O(r^5)` choices, and the electric energy is ≥`a0*r*(r+2)/4` with any original-link lower coefficient bound `a_e>=a0>0`. Hence `Tr'(K^-p)` bounded by `sum_r O(r^{5-2p})`, convergent when `p>3`.

For lower divergence: for dyadic even M select all six labels even in `[M,2M)`. They automatically satisfy every triangle and parity constraint, producing exactly `(M/2)^6` orthogonal gauge states. If original-link coefficients are bounded above by `a_*`, their energies are ≤`10a_* M(M+1)`. Their contribution to `Tr'(K^-p)` is at least `(M/2)^6/[10a_*M(M+1)]^p`, of order `M^{6-2p}`. Disjoint dyadic shells diverge at `p<=3`. Thus **K^-1 is NOT Hilbert–Schmidt** at three faces (`p=2`) despite the uniform electric gap and its L2 operator-norm inverse bound.

Reproducible six-spin enumeration for cutoffs N=4,8,12,16,20 yielded `Tr'(K^-2) = 1.599655530, 3.611335788, 6.485252300, 10.269933572, 14.981929375`. The checker verifies original five-coordinate face topology, gauge labels and dyadic shell counts. Numerical cutoffs are not used to prove divergence.

For comparison, the exact 1-cycle class-function sector has Schatten threshold p>1/2; the 2-cycle overlapping theta sector has p>3/2, so its inverse is Hilbert–Schmidt, consistent with the prior PF-I16 theorem.

**Interpretation:** The two-rhombus *Hilbert–Schmidt trace method* cannot be iterated indiscriminately to arbitrary connected source clusters. This does NOT prove unboundedness of the combined nonlinear operator `K^-1 P0 Gamma_K`, nor disprove its boundedness in a stronger analytic/spin-network norm; it does not address the interacting gap. The source-window verification of this exact 3-face motif and the all-orders nonlinear estimates are next obligations. Physical J/clock dynamics, source energy normalization, OS reconstruction, continuum and physical Yang–Mills mass gap remain OPEN. Canonical main/historical data unchanged.