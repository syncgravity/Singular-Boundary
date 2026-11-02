# R3-IR — Two-boundary Schur complement audit (2026-11-02)

Exact block identity for a positive bounded three-block operator L=[[A,U,0],[U*,D,V],[0,V*,C]]: eliminating D yields Schur off-diagonal −U D⁻¹ V. An analogous application to SU(2) requires domain and coercivity hypotheses not yet proved.

Conditional comparison theorem: for bounded block tridiagonal L=D0+V with diagonal blocks A_j≥κ>0, adjacent off-diagonal block norms ≤η, and 2η<κ, the inverse block satisfies ||(L⁻¹)_{i,j}||≤κ⁻¹ (2η/κ)^|i−j|/(1−2η/κ). Neumann expansion and nearest-neighbor propagation prove it.

For the finite-dimensional tridiagonal matrix A_n=I−t(S+Sᵀ), its end-to-end inverse entry equals t^(n−1)/d_n, d_0=d_1=1, d_n=d_(n−1)−t²d_(n−2). Exact Fraction checks through n=12 agree with numerical inversion and the bound; n=3 gives t²/(1−2t²).

**Important limitation:** the earlier SU(2) one-boundary gradient estimate does not furnish an off-diagonal bounded-operator norm η on a common orthogonal block decomposition. Thus this is a conditional mathematical comparison result, not physical connected-covariance decay or a Yang–Mills gap. Detailed audit, exact verifier, execution log and SHA256 manifest are in Library /The Singular Boundary/Proof Audits.