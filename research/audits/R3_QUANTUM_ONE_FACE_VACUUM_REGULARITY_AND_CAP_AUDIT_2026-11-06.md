# Quantum one-face interacting SU(2) vacuum: curvature and classical-action cap audit
2026-11-06 · **One-face supporting theorem; P0–P5 open.**

For the gauge-invariant one-plaquette SU(2) rotor let x(U)=½Tr U, d=1−x, and H_b=−Δ_(round S³)+bd, b>0. The electric fundamental character eigenvalue is 3, matching the four unit-weight original links on an isolated plaquette after Gauss reduction. Let ψ_b be the unique positive normalized ground state and ν_b=ψ_b² Haar.

## Theorem A
For every b>0,

E₀(b)≤3√b, ν_b[d]≤3/√b, ν_b(d>δ)≤min(1,3/(δ√b)).

**Proof.** The gauge-invariant normalized trial φ_α∝exp(αx) satisfies ⟨x⟩=r=I₂(2α)/I₁(2α). Since Δx=−3x, ⟨φ_α,−Δφ_α⟩=(3α/2)r≤3α/2. The Bessel Riccati equation r'(t)=1−r(t)²−3r(t)/t (t=2α), with positivity at t=3 and a comparison against 1−3/t, proves 1−r≤3/t. Therefore trial energy ≤(3/2)(α+b/α). Choose α=√b, then use kinetic nonnegativity and Markov. □

## Theorem B — exact quantum-vacuum cap obstruction
Set A_h=8d/h. Fix M>0. There is C_M such that, for small h,

ν_b(A_h≤M)≤ C_M h(1+3√b).

Indeed this event is a geodesic round S³ cap of radius θ_h=arccos(1−Mh/8)=O_M(√h), whose normalized Haar volume v_h=O_M(h^(3/2)). Hölder and the compact S³ H¹→L⁶ Sobolev inequality give ν_b(cap)≤v_h^(2/3) C_S (1+∫|∇ψ_b|²)≤C_M h(1+3√b), since ∫|∇ψ_b|²≤E₀(b)≤3√b. □

Therefore if h(1+√b(h))→0 then **the bounded-classical-action event has vanishing probability even under the genuine interacting one-face *quantum ground-state measure***. As one illustrative scaling, b(h)=log²(1/h) meets this condition (corresponding to b=g⁻⁴ for the schematic one-face physical Hamiltonian (g²/h)K+(1/(g²h))d with g²=1/log(1/h)).

This is a **restricted countercalibration**, not a statement about coupled 3D SU(2) Wilson quantum vacuum, physical flowed renormalized curvature, or the Yang–Mills mass gap.

## Exact finite-basis verification
In the orthonormal SU(2) character basis χ_n, the Jacobi Hamiltonian has H_nn=n(n+2)+b and H_n,n+1=−b/2. At b=1,4,16,100,400,1600, truncated diagonalization confirms ground energy below the explicit trial bound and the curvature bound. For b(h)=log²(1/h) and M=4, the calculated quantum cap probabilities at h=10⁻²,10⁻³,10⁻⁴,10⁻⁵,10⁻⁶ are approximately 4.0180e−3, 2.43496e−4, 1.20399e−5, 5.36380e−7, 2.24111e−8. Exact finite-basis numerical tests do not substitute for the proofs above.

## Required next P2/T2 bridge
Define the genuinely coupled, gauge-invariant cubic interacting vacuum ν_(h,R), its coupling trajectory and a *renormalized flowed physical curvature observable* F_(h,R)(τ). Seek an actual vacuum moment/tightness estimate uniform in spatial h and volume R at fixed τ>0. Neither the classical bounded-action theorem nor these one-face quantum results establish that bound. Keep all P0–P5, Penrose/gravity and 4D spectral gaps OPEN.

Full derivation, executable SciPy verifier, log, and SHA-256 manifest are provided in the research ZIP attached to the conversation.
