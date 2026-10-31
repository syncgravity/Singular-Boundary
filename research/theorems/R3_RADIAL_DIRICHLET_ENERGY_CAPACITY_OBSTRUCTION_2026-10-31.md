# R3-IR-595 — Radial SU(2) capacity obstruction to inferring one-sided score control from electric energy

Date: 2026-10-31. Continuation of the prior branch signed radial-score obligation R3-IR-289–292 and R3-IR-593–594. This is a rigorous synthetic counterexample to a proposed proof shortcut, not a simulation or estimate of the actual face-deleted nonlinear Yang–Mills vacuum.

## Construction and exact limit

Consider SU(2) conjugacy-class coordinate u∈[0,π], with normalized Haar radial measure (2/π)sin²u du. Let 0<δ<π/4, 0<ε<1. Put v=min(u,π-u), and define a center-symmetric smooth positive function

φ_{δ,ε}(u)=ε (0≤v≤δ); ε+(1−ε)S(v/δ−1) (δ<v<2δ); 1 (v≥2δ),

where S(t)=6t⁵−15t⁴+10t³, with zero first and second derivatives at endpoints. Normalize ψ=φ/√Z, Z=∫φ² dμ_Haar. Set δ_N=1/N, ε_N=exp(−√N), N≥8. Then Z_N→1 because the transition and depleted regions have Haar mass O(δ³).

The unweighted one-sided log-amplitude oscillation oriented from center toward equator is EXACTLY O_N=log(1/ε_N)=√N→∞. For a cap v≤δ_N, the normalized ν probability divided by the Haar probability is exactly ε_N²/Z_N=e^(−2√N)/Z_N→0.

The SU(2) radial electric Dirichlet form obeys

E(ψ)=∫|ψ'(u)|² dμ_Haar=(4/πZ)∫_δ^{2δ} sin²u [(1−ε)/δ]² [S'(u/δ−1)]² du
 ≤ (16/πZ)(1−ε)² δ ∫_0^1 [S'(t)]²dt
 = O(δ/Z)→0,

using sin²u≤4δ² on the transition. Thus there is no universal bound O≤F(E) with F finite as E→0 and no uniform positive Haar cap comparison obtainable from total Dirichlet-energy control alone.

For these functions E is an abstract SU(2) class-rotor quadratic form; it is not a physical candidate ground state of the fixed Penrose Hamiltonian. The example is compatible with positive smooth amplitudes and exact center symmetry. Its energy can be made arbitrarily small despite arbitrarily large one-sided log amplitude growth over a shrinking cap.

## Consequence

The remaining nonlinear Penrose face-deleted-vacuum problem needs additional *local* information: e.g. an appropriately dimension- and regulator-uniform elliptic Harnack inequality with controlled coefficients, a conditional score/flux estimate, or a microscopic capacity-sensitive input. The previous branch's proposed sufficient uniform current or oscillation estimates are not a consequence of the usual global electric kinetic expectation alone. Finite graph elliptic positivity does not provide the needed regulator-uniform Harnack constants by itself.

The prior branch's conditional Ward identity and the deduction from uniform one-sided oscillation to its magnetic-deletion spectral bound have NOT been independently re-proved from the original complete theorem package in this session; this report establishes only the abstract counterexample and its rigorously verified analytic behavior.

Reproducible executable `audit_radial_energy_noncoercivity_2026_10_31.py` and results `radial_energy_noncoercivity_2026-10-31.json` are in ChatGPT Library `/The Singular Boundary/Source/`.
