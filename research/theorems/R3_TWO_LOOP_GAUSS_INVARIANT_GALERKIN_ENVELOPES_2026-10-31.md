# R3-IR-565 — Exact two-loop gauge-invariant Galerkin magnetic projection and electric-form envelopes

2026-10-31. On all six original prismatic candidate graphs, choose the two retained plaquettes sharing the deleted bottom face chord: adjacent horizontal loop A and vertical loop B. The archived signed incidence verifies their edge supports meet exactly at one chord edge, and each loop has edges absent from the other. Thus conditioning on all other edge Haar variables, independent unique Haar edge variables make their SU(2) holonomies **independent Haar variables**. No claim of independence under the interacting vacuum.

The four functions `1, χ_1/2(U_A), χ_1/2(U_B), χ_1/2(U_A)χ_1/2(U_B)`, where χ_1/2=Tr U, are gauge invariant, mutually orthonormal in product Haar, and belong to the finite graph's Gauss-law physical Hilbert space. Denote basis 00,10,01,11. With Wilson p_A=Tr U_A/2 and p_B=Tr U_B/2, their exact projected nonconstant magnetic Hamiltonian equals
```
[0     -bA/2 -bB/2   0   ]
[-bA/2   0      0   -bB/2]
[-bB/2   0      0   -bA/2]
[0     -bB/2 -bA/2   0   ].
```
All other retained plaquettes have at least one edge outside the union of these two loops, so their Wilson trace matrix elements vanish in this four-dimensional subspace under product Haar. The complete magnetic energy also includes the **additive identity constant** from Σ b_f(1−p_f), omitted above because it does not affect finite projected spectral differences.

The exact *unweighted derivative* quadratic form ∑_e,a⟨X_e^a φ_i,X_e^a φ_j⟩ is diag(0,3,3,6), since each elementary 4-edge fundamental SU(2) character carries Casimir 3/4 per edge and cross terms vanish by conditional Haar/representation orthogonality. The full rooted electric quadratic form is **not** that diagonal matrix: it contains all K_e,e' and transport rotations. However, since K=M1^-1 is positive definite and each transported edge derivative has unchanged norm, its actual four-dimensional matrix E satisfies the rigorous Loewner inequalities
  (g²/2)λmin(K)diag(0,3,3,6) ≤ E ≤ (g²/2)λmax(K)diag(0,3,3,6).
This is a spectral envelope, not a diagonal electric approximation. The finite Ritz eigenvalues of E+projected magnetic potential are bracketed, by matrix minimax, between the ordered eigenvalues of these two explicit 4×4 endpoints. **Ritz gaps are not bracketed by subtracting matched eigenvalues**; and even exact Ritz gaps are not full-operator mass gaps.

At g²=1, using action-normalized bA,bB and archived M1 data, the first two ordered Ritz eigenvalue intervals for the nonconstant magnetic convention are:

|M|λ0 lower|λ0 upper|λ1 lower|λ1 upper|
|---:|---:|---:|---:|---:|
|5|-16.928|-0.513|3.538|504.330|
|7|-25.325|-0.904|3.154|639.460|
|9|-36.074|-1.295|-5.285|969.655|
|11|-38.478|-1.347|5.951|1002.521|
|13|-41.613|-1.383|10.312|1197.269|
|15|-64.960|-2.834|-12.166|1402.392|

Intervals are too broad to certify physical finite-spectrum gaps. They nevertheless give exact *full-metric-compatible* bounds, preserve two distinct Wilson holonomies, and constitute an explicitly Gauss-law-invariant two-loop advance over the one-loop collapsed rotor R3-IR-564.

**Pending:** compute all individual electric off-diagonal Galerkin matrix elements using exact SU2 Haar tensor contractions (or certified high-accuracy quadrature) including rooted transport dependence; then expand the gauge-invariant spin-network basis with intertwiners and demonstrate spectral convergence of the full finite prism. No continuum Yang–Mills mass gap follows.

Executed audit and data are in ChatGPT Library `/The Singular Boundary/Source/audit_two_loop_gauge_galerkin.py` and `two_loop_gauge_galerkin_2026-10-31.json`. No binary arrays committed to Git.
