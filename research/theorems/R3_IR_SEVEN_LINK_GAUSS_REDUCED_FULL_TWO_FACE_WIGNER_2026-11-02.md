# Seven-link Gauss-reduced complete two-face Wigner operator (2026-11-02)

**Supersedes archived two-face electric spectral formulas.** For two adjacent SU(2) plaquettes with seven original links, based holonomies A=H1 U, B=U^(-1) H2, and original-link generators T_a=i sigma_a/2, the shared-link derivative is D_a=R_a^A−L_a^B. Adding its Casimir and the three nonshared-link Casimirs for each face gives the **physically reconstructed two-face operator**

**K_phys=4L_A+4L_B+2 Σ_a R_a^A L_a^B.**

Maximal-tree gauge fixing leaves two independent based loop variables modulo residual simultaneous SU(2) conjugation. The induced Haar measure is product Haar; the operator commutes with that residual Gauss constraint.

On the full Wigner (n,m) matrix-coefficient block the right-A / left-B magnetic-index coupling is the ordinary Hermitian C=J_A dot J_B, hence **K_(n,m)=D I+2C**, D=n(n+2)+m(m+2). Exact SU(2) spin addition gives the **complete spectrum**

**E_(n,m;J)=3/4[n(n+2)+m(m+2)]+J(J+1)**,

J=|n−m|/2,...,(n+m)/2 in unit steps, with full-block multiplicity (n+1)(m+1)(2J+1). The fundamental mixed block has energies **9/2 and 13/2**, in agreement with the six-original-link outer Wilson loop, not the archived 11/2,15/2.

Wilson sector: a=Re A, b=Re B, w=Re(AB) obey Ka=3a, Kb=3b, Kw=9w/2; Γ(a,b)=(w−ab)/4 and K(ab)=13ab/2−w/2. In inverse-neighbor trace r=Re(A B^(-1))=2ab−w, K(ab)=11ab/2+r/2, K(r)=2ab+11r/2, and **K^(-1)Γ(a,b)=5ab/78−2r/39**.

The exact uncoupled-Wigner edge bound ||C||_(1→1)≤sqrt[n(n+2)m(m+2)]/4 survives the sign correction. Hence ||K_(n,m)^(-1)||_1≤2/D and ||K_(n,m)^(-1)C||_1≤1/6 on nonconstant **two-face** blocks, uniformly in degrees. Their physical all-length analogues require independent original-link rederivation.

The general 3+-face spectral formulas, anchored-polymer applications and all-length physical claims in prior reports **remain unvalidated** until the actual longer original-link geometry, maximal-tree loop basis and all derivative operators are checked. No interacting lambda=1 gap or continuum Yang–Mills mass gap follows.

A complete 126-line detailed proof report, independent exact SymPy magnetic-block verifier (all 49 degree pairs 0≤n,m≤6, including multiplicities and correct Wilson-sector Poisson response), passing log and SHA256 manifest are archived in The Singular Boundary / Proof Audits Library.