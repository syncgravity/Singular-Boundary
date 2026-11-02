# Exact dressed face filtration and projected form witness — 2026-11-02

**Scope:** reduced original-link model A=XY, B=Y⁻¹Z, C=Z⁻¹W with independent Haar X,Y,Z,W; not a full four-link square-strip projected-form theorem.

The triangular Haar transformation to independent (A,B,C,Y) shows that weighting by ψ_b(Re A)^2 ψ_b(Re B)^2 ψ_b(Re C)^2 preserves independence of A,B,C and leaves spectator Y Haar. Thus conditional expectations onto A, onto (A,B), and onto (A,B,C) define explicit nested orthogonal projections, but a complete L² decomposition must also include the Y spectator sector.

With positive original-link Γ, the exact orientation identity is Γ_Y(a,b)=[Re(AB)−ab]/4, a=Re A, b=Re B. For the reduced-link K and S=s_b(a)+s_b(b)+s_b(c), L=K−2Γ(S,·) satisfies L a=3a/2−s'_b(a)(1−a²)−(s'_b(b)/2)(Re AB−ab). Conditional isotropy gives E[s'_b(b)(Re AB−ab)|A]=0, so (I−E[·|A])La=−(s'_b(b)/2)(Re AB−ab), which is nonzero for nonconstant local dressing.

Taking G=s'_b(b)(Re AB−ab), ⟨a,L G⟩=−(1/2)E[s'_b(b)^2(Re AB−ab)^2]. The Haar second moment is E[(Re AB−ab)^2]=3/16. For s'_b=b_coupling/3+O(b_coupling²), the form witness is −b_coupling²/96+O(b_coupling³), and squared off-sector norm of L a is b_coupling²/192+O(b_coupling³). Exact rational and symbolic checks passed.

The numeric factors belong to the reduced two-link-per-outer-face construction, not the physical square strip. This does not establish a relative off-diagonal Dirichlet-form bound, bounded tridiagonal operator, connected covariance decay, interacting gap or mass gap. Full proof, checker, log and SHA256 manifest are in Library /The Singular Boundary/Proof Audits.