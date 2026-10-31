# Exact smooth center-depletion obstruction for the radial eigen-equation

Date: 2026-10-31. Status: exact SU(2) class-rotor countermodel, **not** the physical deleted-face Wilson ground state. This note tests whether positivity, center symmetry and a smooth Schrödinger ground-state eigen-equation alone control the signed current.

Let p(U)=Tr(U)/2, Δp=-3p/4 and Γ(p,p)=(1-p²)/4. For λ>0 take Ωλ=Zλ^(-1/2)exp(-λp²) and define qλ(p)=1/4[(1-p²)(-2λ+4λ²p²)+6λp²], Vλ=qλ-min qλ. Then Vλ≥0 is smooth and central and (-Δ+Vλ)Ωλ=(-min qλ)Ωλ. The positive ground-state transform proves it is the true simple positive ground state: ⟨φ,(H-E)φ⟩=∫Ωλ²|∇(φ/Ωλ)|²dHaar≥0.

The exact radial score current is Cλ(p)=a(p) ∂p log Ωλ=-(λ/2)p(1-p²), a(p)=(1-p²)/4; the positive one-sided current budget from p=1 to p=0 is Tλ=λ. For each fixed 0<δ<1, PΩλ(p≥1-δ)/PHaar(p≥1-δ) tends to 0 as λ→∞. Thus generic positivity, center symmetry, endpoint smoothness and the eigen-equation alone imply no uniform signed-current bound.

**Scope warning:** Vλ is a specially engineered one-rotor class potential, not the sum of neighboring Wilson plaquette potentials defining a complete deleted-face Penrose cage. This is a logical obstruction to general elliptic arguments, not a Wilson-vacuum counterexample, and proves no mass gap or continuum theorem. Wilson-specific conditional slice control remains OPEN. Related records: R3_IR_CENTER_SLICE_EIGEN_EQUATION_JET_2026-10-30.md and R3_IR_ROOT_INDEPENDENT_FACE_WARD_2026-10-31.md. Verifier, numerical quadratures and SHA-256 manifest preserved in Library `/The Singular Boundary/Proof Audits/R3_IR_CENTER_DEPLETION_2026-10-31.zip`.
