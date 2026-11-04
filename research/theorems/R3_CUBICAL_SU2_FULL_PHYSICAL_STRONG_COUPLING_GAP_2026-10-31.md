# R3-IR-589 — Full Gauss-invariant finite-volume strong-coupling gap on the refining cubical reference graph

Date 2026-10-31. Unlike earlier M5 small-basis Ritz computations, this is a spectral inequality on the **entire** gauge-invariant finite-graph Hilbert space for the distinct Kogut–Susskind cubic reference regulator of R3-IR-587.

Let a=1/n and let the finite open-boundary cubical graph G_n have F=3n²(n+1) plaquettes. On H_phys=L²(SU2^E)^{SU2^V}, define H_E=(g0²/2a)Σ_e(-Δ_e) with the standard SU2 Casimir j(j+1), and H_B=(2/g0²a)Σ_f[1−Tr(U_f)/2]. The magnetic potential is bounded, nonnegative and gauge invariant; the electric kinetic form is self-adjoint with compact resolvent, and restriction to the closed Gauss-invariant space preserves these properties.

**Exact free electric threshold:** SU2 Peter-Weyl spin networks give orthogonal eigenmodes of Σ_e(-Δ_e), with eigenvalue Σ_e j_e(j_e+1). At each vertex an invariant intertwiner forces the spin-carrying edge subgraph to have no leaf. For a simple cubic lattice graph, every nonempty finite leafless subgraph contains a cycle of length at least four. Every occupied edge has j≥1/2 and Casimir ≥3/4. Therefore every nonconstant gauge-invariant mode has sum Casimir at least 4(3/4)=3, attained by the trace of a fundamental elementary plaquette. Thus λ1(H_E|phys)=3g0²/(2a), λ0(H_E|phys)=0.

By min-max and H_B≥0, λ1(H)≥3g0²/(2a). For the constant normalized gauge-invariant trial function, ⟨1,H1⟩=⟨1,H_B1⟩=2F/(g0²a), since the Haar expectation of every nontrivial plaquette character is zero. Consequently λ0(H)≤2F/(g0²a), yielding the **full finite-graph spectral gap bound**
Δ_n=λ1(H)−λ0(H)≥3g0²/(2a)−2F/(g0²a).

In particular, Δ_n>0 whenever g0²>sqrt(4F/3). For n=2,4,8,16 the thresholds on g0² are approximately 6.92820323,17.88854382,48,131.93938002. Independent compactness and strictly-positive heat-kernel arguments also give uniqueness of the finite-graph ground state (strong continuity and positivity improving on gauge-invariant functions). This is a sufficient, not necessary, coupling condition; the exact finite-graph gap may be positive at other couplings as well.

**Continuum obstruction:** F~3n³, and the required g0² scales as n^(3/2), opposite to a controlled weak-bare-coupling limit. The bound provides NO positive lower bound uniform in a→0, volume, or physically renormalized coupling. The reference graph is cubical and is not the historical Penrose-prism Whitney regulator. No 3+1D continuum Yang–Mills construction or mass gap is proved.

Reproducible count/threshold audit: ChatGPT Library /The Singular Boundary/Source/cubical_su2_strong_coupling_finite_gap.py and cubical_su2_finite_strong_coupling_gap_2026-10-31.json. The analytic proof is this document, not a finite sampling argument. Remaining obligations: explicit compatible transfer-matrix proof and nontrivial continuum control; full R3-IR-584 31-state electric contraction remains open.