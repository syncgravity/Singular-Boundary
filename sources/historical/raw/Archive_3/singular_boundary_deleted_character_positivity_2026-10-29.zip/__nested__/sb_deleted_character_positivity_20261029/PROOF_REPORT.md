# The Singular Boundary — Character-positive deleted-face Haar-cap theorem and finite-spin certificate

**Date:** 2026-10-29. **Program:** R3 independent reconstruction; finite SU(2) Wilson Hamiltonians on simply connected planar Penrose rhombus disks. **Classification:** exact harmonic-analysis results for any positive center-even SU(2) class marginal, and a **conditional** physical nonlinear-vacuum consequence. **OPEN:** positivity or sufficiently small negative-character budget for the actual deleted ground state; the all-bulk magnetic deletion bound; continuum SU(2) mass gap.

## 1. Why this route differs from radial Fisher control

The exact magnetic-deleted ground state Ω^-_f of H^-_f=T+sum_{g≠f}b_g(1-p_g) has a positive, normalized gauge-invariant face-holonomy marginal F_{f,h}(U) dU relative to normalized SU(2) Haar. Residual global gauge invariance makes F central, and the exact deleted center-flux parity makes F(-U)=F(U). The earlier marginal capacity and radial orbit-current theorems gave sufficient—but unproved—rate conditions on the radial Fisher energy J_rad or signed current. Those conditions are not necessary: center-favoring distributions can have substantial Fisher energy and still have very large flat-cap probabilities. We derive a different gauge-invariant criterion in terms of the physically measurable Wilson characters.

Normalize SU(2) irreducible characters χ_j(U)=sin((2j+1)u)/sin u, with j=0,1/2,1,3/2,..., U=exp(iu n·σ), 0≤u≤π, dimension d_j=2j+1, and ∫χ_jχ_k dU=δ_jk. Define the exact deleted-vacuum coefficients

    c_j(f,h)=∫_{SU2}F_{f,h}(U)χ_j(U)dU = <χ_j(W_f)>_{Ω^-_f},   c_0=1.

They are gauge-invariant, real, and obey |c_j|≤d_j; center parity implies c_j=0 for half-odd-integer j. No sign of c_j for integer j>0 follows from parity or positivity of F alone.

## 2. Theorem CP-1: positive type gives a Haar-order flat-cap lower bound

Let B_a={U∈SU(2):u(U)<a}, with 0<a<π/2, and H(a)=Haar(B_a)=(a−sin(2a)/2)/π. Put A=B_{a/2}, q=1_A and k=q*q^∨, where q^∨(U)=q(U^{-1}), and convolution uses normalized Haar. Because the SU(2) bi-invariant geodesic distance is subadditive,

    0≤k(U)≤H(a/2) 1_{B_a}(U),
    ∫k=H(a/2)².

The convolution coefficients are exactly nonnegative:

    k(U)=sum_{j∈{0,1/2,...}} (b_j²/d_j) χ_j(U),
    b_j=∫_A χ_j(U)dU.

For any positive normalized *central* density F whose nontrivial coefficients c_j are nonnegative (equivalently, F is a continuous positive-definite class function), character orthogonality yields

    H(a/2) Pr_F(B_a) ≥ ∫F k
           =H(a/2)²+sum_{j>0} c_j b_j²/d_j ≥ H(a/2)².

Hence

    **Pr_F(B_a) ≥ H(a/2).**                                               (CP-1)

For the actual deleted-vacuum marginal, center parity means that only nonnegativity of **integer-spin** coefficients c_j, j=1,2,... is needed. No Gaussian approximation, spectral gap, spatial reflection symmetry, or control of the conditional wavefunction is used in the implication. The positivity premise itself is **OPEN** for cycle-rich nonlinear Wilson deleted vacua. Do not mistake the mathematical theorem for an SU(2)-specific proof of that premise.

At the required deficit threshold d=1-p≤h, take a_h=acos(1−h). Then B_{a_h} is exactly the flat cap, and B_{a_h/2} corresponds to deficit 1−sqrt(1−h/2). Since

    H(a_h/2) = (1/8+O(h)) H(a_h)
              = (sqrt(2)/(6π)+O(h)) h^(3/2),

CP-1 implies a **polynomial near-flat mass**. The earlier all-face exponential trial bound then gives Δ_f=O(h^-1 log(1/h)) under the declared Penrose bounds 0<a_-≤a_e≤a_+, β_-h^-2≤b_f≤β_+h^-2, closing the previously conditional extreme-defect and Wilson–angle remainder steps **if** the character sign premise is established uniformly. The physical gap is a separate obligation.

## 3. Theorem CP-2: exact negative-spin budget and finite character certificate

Let φ_a(U) be any real, nonnegative, central, smooth bump supported in B_{a/2}, 0≤φ_a≤1. Write

    A_a=∫φ_a dU>0,  N_a=∫φ_a² dU>0,
    β_j(a)=∫φ_a(U)χ_j(U)dU.

Define k_a=φ_a*φ_a^∨. Haar Cauchy gives

    0≤k_a≤N_a 1_{B_a},   ∫k_a=A_a²,
    k_a(U)=∑_{j≥0} β_j(a)²/d_j χ_j(U).

For the actual deleted-vacuum density F, define the measurable finite-spin *negative-character defect budget*

    Neg_J(F,a)=∑_{0<j≤J} [−c_j]_+ β_j(a)²/d_j.

The bound |c_j|≤d_j and Parseval give the exact finite-spin certificate

    **Pr_F(B_a) ≥ [A_a²−Neg_J(F,a)−Tail_J(a)]_+/N_a,**                 (CP-2)

    Tail_J(a)=∑_{j>J} β_j(a)² = N_a−∑_{j≤J} β_j(a)².

This holds with no sign hypothesis whatsoever and for all finite SU(2) class probability densities. For a center-even density, the half-integer-spin terms in Neg_J vanish identically. In particular, if the measured low-spin negative budget plus the deterministic high-spin tail is ≤A_a²/2, then

    **Pr_F(B_a) ≥ A_a²/(2N_a) ≍ a³.**                                    (CP-3)

At a=a_h≈sqrt(2h), this implies the required h^(3/2) lower bound. Thus character-positivity need not hold in *every* spin: small weighted negativity is allowed. This is a practical, quantitative proof gate in terms of gauge-invariant character expectations, not the inaccessible pointwise conditional vacuum score.

The exact Haar coefficients for the sharp indicator q=1_{B_r} are, for j>0,

    b_j(r)=1/π [ sin(2jr)/(2j) − sin((2j+2)r)/(2j+2) ];              (CP-4)
    b_0(r)=H(r).

All sums converge absolutely in CP-2: |c_j|≤d_j, and ∑β_j²=N_a. The sharp indicator can also be used in CP-2 with N_a=H(a/2), A_a=H(a/2) and the same Fourier tail, although smoothing gives a much better finite-spin cutoff.

## 4. Theorem CP-3: character cutoff J(h)=O(h^(−1/2−ε)) suffices, at arbitrary ε>0

Choose a fixed smooth radial bump φ(t), t≥0, equal to one for t≤1/4, zero for t≥1/2, nonnegative elsewhere, and set φ_a(U)=φ(u(U)/a). Smoothness at identity holds because φ is constant there. Uniform Haar-volume estimates for small a give A_a≍a³ and N_a≍a³. For every fixed integer m≥1, elliptic/scaling estimates on the round SU(2) 3-sphere give

    ||(−Δ)^(m/2) φ_a||²₂ ≤ C_m a^(3−2m).

The Casimir eigenvalue of χ_j is j(j+1), so character Parseval yields

    Tail_J(a) ≤ C_m a^(3−2m) / [J(J+1)]^m
              ≤ C'_m a³ (Ja)^(−2m)                         (J≥1).      (CP-5)

For any ε>0 choose m>3/(2ε) and J(a)≥C_{m,φ} a^(−1−ε). Then Tail_J(a)=o(a⁶)=o(A_a²). With a_h≈sqrt(2h), only integer-spin expectations through

    **J(h)=O(h^(−(1+ε)/2))**

need controlled negative budget to obtain the polynomial small ball. The hidden constant and sufficient refinement range may be large for small ε. This is a theorem about sufficiency, **not** an estimate of the actual SU(2) character expectations. It supplies a finite representation-theoretic target with arbitrarily small power overhead beyond the natural angular resolution j≈h^-1/2.

## 5. CP-4: why center parity and density positivity do not give the sign premise

For κ>0, consider the smooth, strictly positive, center-even SU(2) class density

    F_κ(U)=Z_κ^-1 exp(−κ p(U)²),

which is also the squared positive ground-state wavefunction of an explicitly constructible nonnegative center-symmetric class rotor potential. The spin-one character is χ_1(U)=4p²−1. Weighting Haar by a strictly decreasing function of p² reduces its mean p² below the Haar value 1/4, hence

    **c_1(F_κ)=4 E_{F_κ}(p²)−1<0.**

Thus *neither center symmetry, strict positivity, nor the positive-ground-state property alone* implies character positivity. The example is a separate rotor comparator, not a counterexample to the special magnetic-deleted Wilson Hamiltonian.

A further caution: SU(2) nonabelian surface representations can have signed contributions (e.g. Brydges–Giffen–Durhuus–Fröhlich, Nucl. Phys. B 275 (1986) 459–487), so no blanket positivity of all Wilson character expectations is assumed in this report. The exact magnetic-deleted Hamiltonian requires an independent positivity/negative-budget argument.

## 6. Deterministic verification, provenance and remaining tasks

`verify_character_minorization.py` checks the exact SU(2) Haar character integrals, the sharp indicator formula CP-4, smooth bump Fourier Parseval tails, positive finite-spin lower certificates, and negative c_1 for three strictly positive center-even rotor distributions. Its quadratures are deterministic; no Monte Carlo or nonlinear Penrose vacuum simulation was performed. The local Penrose Stage26 and Q14 data are not modified. The full SU(2) 3-face/10-edge fixture remains a separate geometric validation; this theorem is group-theoretic and independent of fixture size.

**PROVED:** CP-1 Haar-cap minorization from positive type, CP-2 exact weighted negative-spin finite certificate, CP-3 sharp near-cap representation cutoff up to arbitrarily small power, CP-4 strict positive even rotor sign obstruction.

**OPEN:** demonstrate nonnegative (or sufficiently weakly negative) *integer-spin* deleted-face Wilson character expectations up to J(h)=O(h^(−1/2−ε)) for all cycle-rich interior faces in the true nonlinear Penrose ground state. This would close the polynomial flat-cap and magnetic-deletion objectives, but not the full interacting mass gap, quartic resolvent, or continuum reconstruction.
