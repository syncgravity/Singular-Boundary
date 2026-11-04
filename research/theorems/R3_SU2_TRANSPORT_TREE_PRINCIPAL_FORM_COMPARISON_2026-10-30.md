# R3-IR-533 — Explicit principal quadratic-form difference for two SU(2) transport trees (2026-10-30)

Graph: oriented triangle a:0->1, b:1->2, c:2->0 with root 0. Take rooted tree T1={a,b} and T2={a,c}. For a source derivative on c (source=2), the tree root-to-source transporter is V_c^(T1)=U_a U_b and V_c^(T2)=U_c^{-1}. The source derivative on a (source=0) has transporter identity for both trees. Let the real SPD edge matrix have K_aa=K_bb=K_cc=1 and K_ac=K_ca=0.3; other off-diagonal entries vanish.

At U_a=U_b=I and U_c=(sqrt(1/2),0,0,sqrt(1/2)) as a unit quaternion, choose derivative covectors of length one on a and c in a common root-frame x direction, with derivative on b zero. The electric first-order quadratic symbol Q_T=Σ K_ij (Ad V_i ξ_i)·(Ad V_j ξ_j) equals Q_T1=2.6 and Q_T2=2.0. Positivity follows because the smallest K eigenvalue is 0.7.

This is an **exact pointwise principal-symbol distinction** in common link coordinates, not merely a path-count distinction. It rules out coefficientwise equality and conjugation by scalar multiplication (which preserves the principal symbol). It does NOT rule out nontrivial unitary conjugacy involving transformations of coordinates or bundles, and the chosen covectors were not projected onto the gauge-invariant cotangent quotient. Physical spectral inequivalence is not established.

This test is deliberately on an independent graph: the archived 30-link M5 Whitney matrix is not mounted in the current runtime. No result on actual Penrose refinement scaling was added; the h^-2 scaling considered previously remains a scenario, not measured data.

Reproducer: research/scripts/validate_tree_principal_symbol.py.
