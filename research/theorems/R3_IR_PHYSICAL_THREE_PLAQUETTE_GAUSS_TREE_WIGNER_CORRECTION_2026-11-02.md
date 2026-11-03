# Physical three-plaquette Gauss-tree Wigner reconstruction (2026-11-02)

**Exact finite-graph correction.** A planar three-square SU(2) strip has ten original links, eight vertices, and three based cycle coordinates. Choose the seven-link spanning tree consisting of bottom horizontal edges b1,b2,b3 and vertical edges v0,v1,v2,v3; top chords t1,t2,t3 define A_j=P_(j−1) t_j P_j^−1, where P0=v0 and Pj=b1...bj vj. After tree fixing, A_j=t_j and residual simultaneous conjugation imposes the Gauss constraint.

With L_j and R_j the left/right SU(2) Lie derivatives and Q_j=L_j−R_j, the ten physical original-link derivative fields for each generator α are:
- chords t1,t2,t3: L1,L2,L3;
- verticals v0,v1,v2,v3: L1, −R1+L2, −R2+L3, −R3;
- bottom tree links b1,b2,b3: −R1+Q2+Q3, −R2+Q3, −R3.

The exact free electric operator is **K_phys=−Σ_(ten links e)Σ_α D_(e,α)^2**. In particular b1 differentiates multiple based face holonomies: the physical three-face operator is not the simple product of independent nearest-neighbor edge couplings used by the archive.

**Exact full degree-(1,1,1) magnetic calculation.** This block has 64 Wigner coefficients, of which 5 are residual-simultaneous-conjugation invariant. Choose basis p=trA1 trA2 trA3, u12=tr(A1A2)trA3, u23=tr(A2A3)trA1, u13=tr(A1A3)trA2, w=tr(A1A2A3). In coefficient-column convention the physical 5×5 invariant matrix is

    [[10,0,0,-2,0],
     [-1,8,0,1,0],
     [-1,0,8,1,0],
     [0,0,0,13,0],
     [0,-1,-1,-4,6]]

with **exact invariant spectrum {6,8,8,10,13}**. The eight-link outer Wilson trace w is correctly an eigenfunction with electric energy 6.

The most favorable sign-corrected extension of the archived nearest-neighbor ansatz, K_NN=4Σ_i Casimir_i+2Σ_(i=1,2)R_i·L_(i+1), gives instead the invariant matrix

    [[10,0,0,0,0],
     [-1,8,0,0,0],
     [-1,0,8,0,0],
     [0,0,0,10,0],
     [0,-1,-1,-2,6]]

with spectrum **{6,8,8,10,10}**. Although both give Kw=6w, their action on the gauge-invariant trace tr(A1 A3 A2) differs; the squared Euclidean norm of the full 64-coefficient difference is exactly 9. Thus **the nearest-neighbor ansatz fails even on the Gauss-invariant sector**, not merely on nonphysical magnetic coefficients.

**Dependency consequence:** The archived all-length commuting-coupling spin spectrum, all-length physical Wigner inverse and endpoint estimates, overlap and anchored polymer estimates, and nonlinear Wilson-character obstructions conditional on that ansatz cannot be asserted for the physical original-link strip until reconstructed afresh. Two-face norm inequalities and abstract results about the archived model are not automatically disproved. A different loop-coordinate choice requires a proven Gauss-preserving unitary equivalence.

The complete mathematical proof and exact SymPy six-index verifier, independent NumPy checker, passing logs, and SHA256 manifest are preserved in The Singular Boundary / Proof Audits Library. **No interacting lambda=1 gap or continuum Yang–Mills mass gap is established.**