# Physical ten-link, three-plaquette Gauss reduction: nonlocal tree-link obstruction (2026-11-02)

**Supersedes prior all-length nearest-neighbor spectral claims as physical statements in this explicit based-loop coordinate gauge.** A horizontal row of three SU(2) squares has 8 vertices, 10 original links and 3 cycles. Choose root at bottom vertex B0 and maximal tree {b1,b2,b3,v0,v1,v2,v3}, with top horizontal chords h1,h2,h3. For P_i=b1…bi v_i (P0=v0), based loops are **A_i=P_(i−1) h_i P_i^(-1)**. In tree gauge, A_i=h_i, but varying bottom tree edges conjugates suffixes of loops.

Let R^i and L^i denote the standard right- and left-insertion derivative fields on A_i, G^i=L^i−R^i, and E(X)=−sum_(alpha=1)^3 X_alpha². Exactly differentiating each of ten original-link matrices gives the electric sum-of-squares

**K3=Σ_(i=1)^3 E(R^i)+E(L^1)+E(−R^1+L^2)+E(−R^2+L^3)+E(−R^3)+E(−R^1+G^2+G^3)+E(−R^2+G^3)+E(−R^3).**

The final three terms arise from bottom original tree links b1,b2,b3. In particular b1 induces −R1+G2+G3 and b2 induces −R2+G3; these are absent from the archived naive 4Σ L_i+2Σ R_i·L_(i+1) model. The reduced operator preserves simultaneous-conjugation Gauss invariance.

**Exact invariant-sector counterexample:** Let a1=Re A1, a3=Re A3, w13=Re(A1 A3). All are residual-gauge invariant. Fundamental SU(2) Fierz and original-link derivatives give
**K3(a1 a3)=6(a1 a3), K3(w13)=8w13−2a1a3.**
Therefore the invariant multidegree-(1,0,1) sector has genuine electric energies **6 and 8** (eigenfunctions a1a3 and w13−a1a3). The archived nearest-neighbor model predicts eigenvalue 6 throughout that sector, because n2=0. Hence it is **not the physical electric operator in this particular based-loop gauge**. This does not rule out a different gauge or loop-coordinate representation with equivalent but differently expressed dynamics.

The same original-link calculation confirms the six-original-link adjacent outer Wilson loop K Re(A1A2)=(9/2)Re(A1A2) and the eight-original-link three-face outer Wilson loop K Re(A1A2A3)=6 Re(A1A2A3). Full proof: 151-line Markdown report with graph, exact loop words, ten induced differential fields, Fierz calculation, Gauss caveats, dependency disposition and next research objective. Independent SymPy verifier differentiates every original link to second order on 36 rational SU(2) chord configurations and passes five additional perimeter configurations. Script, execution log, SHA-256 manifest and full report archived in The Singular Boundary / Proof Audits Library.

**Status:** Prior three-plus-face physical Wigner eigenvalue claims and any subsequent polymer conclusions relying on that nearest-neighbor electric generator require revalidation. The current theorem neither establishes a thermodynamic interacting λ=1 gap nor the continuum four-dimensional Yang–Mills mass gap.