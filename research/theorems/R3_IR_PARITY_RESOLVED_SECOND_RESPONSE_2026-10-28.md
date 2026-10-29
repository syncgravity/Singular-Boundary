# R3-IR — Parity-resolved second response and genuine Penrose seed calculation

**Status:** Finite regulator proofs only. No continuum mass gap, regulator-uniform response or Stage26 Hamiltonian identity is proved. No Monte Carlo performed.

For a simple even ground state Ω of H₀, reflection-odd bounded real multiplication observable A, and H(t)=H₀−tcA, define K=H₀−E₀, G=QK⁻¹Q, X=AΩ (odd), Y=GX (odd), S=QA²Ω (even), v=||X||², Z=GAY (even). Exact analytic perturbation of the finite ground state yields

**V''(0)=c²{4 Re⟨S,Z⟩+2⟨Y,(A²−v)Y⟩−8⟨X,Y⟩²}**, V(t)=Var_{Ω_t}(A).

Indeed Ω′=cY, Ω″=2c²Z−c²||Y||²Ω and μ′(0)=2c⟨X,Y⟩. The first source response V′(0)=0 by reflection; the second is generally not zero and has no fixed sign.

**Authentic three-rhombus spatial seed**: the canonical Z⁵ coordinates from the recovered history have 10 edges and a reflection fixing face 0 and exchanging edge-disjoint faces 1 and 2. In the true electric Hamiltonian H_E=aΣ_e(-Δ_e), for A=p₁−p₂ the finite-order Peter–Weyl character calculation gives v=1/2 and
4⟨S,Z⟩=11/(144a²), 2⟨Y,(A²−v)Y⟩=1/(12a²), −8⟨X,Y⟩²=−2/(9a²), hence **V″(0)=−c²/(16a²)**.
For fixed finite graph, bounded Wilson magnetic perturbations and the simple vacuum ensure analytic continuity. There exists a (not explicitly bounded) b*>0 so the second response remains negative for all sufficiently small symmetric positive magnetic b. This is not a strong-magnetic or continuum claim.

**Even-source genuine SU2 example:** On one open rhombus, H_b=4a(−Δ_class)+b(1−p) with p=χ₁/₂/2, the electric-limit second variance derivative is −1/(32a²). Consequently the first even-source three-point response is −b/(64a²)+O(b²) for weak positive magnetic coupling: parity does not annihilate generic even sources.

**Abstract sign obstruction:** On C³ take H₀=diag(0,d₁,d₂), R=diag(1,−1,1), and A=[[0,1,0],[1,0,q],[0,q,0]]. Then V″/c²=4q²/(d₁d₂)+2(q²−4)/d₁², which can be positive or negative.

For source-aligned α=3/2 geometric deformation, c=h^(−5/2). The earlier sufficient condition sup_{|t|≤τ}|V″(t)|=o(h^(−4)) would require the bracket in the displayed formula to be o(h) at zero, but the zero-point result by itself cannot control an interval. **This nonlinear, all-scale response bound remains open.**

Independent deterministic certificate: scripts/audit/verify_second_response.py, with 3-face incidence, 9-dimensional finite-order electric character calculation, one-rhombus reference, exact rational resolvent, and signed abstract witness. Detailed companion report and SHA256 manifest are available in the derived archival package. Original archives remain untouched.
