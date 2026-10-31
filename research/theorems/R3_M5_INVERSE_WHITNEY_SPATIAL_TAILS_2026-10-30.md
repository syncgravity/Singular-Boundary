# R3-IR-554 — Verified spatial tails of the original M5 inverse Whitney metric; Poisson localization remains open

Date: 2026-10-30. This is a **kinetic-matrix localization result**, not a ground-state response/mass-gap theorem.

## Exact inverse-matrix decay lemma

Let M be any symmetric positive-definite edge mass matrix with spectrum [a,b], 0<a≤b, and let d_M(i,j) be the shortest path distance in its off-diagonal sparsity graph. Set rho=(b-a)/(b+a)<1 and c=2/(a+b). The uniformly convergent Neumann representation is

M^-1 = c sum_{k=0}^infinity (I-cM)^k.

For i≠j, (I-cM)^k_ij=0 for all k<d_M(i,j), because a length-k matrix product cannot connect vertices at distance >k. Furthermore ||I-cM||_2=rho. Thus

**|(M^-1)_ij| ≤ c sum_{k=d_M(i,j)}^infinity rho^k = rho^{d_M(i,j)}/a.**

This is a mathematically rigorous bound for a *sparse SPD* M, and it remains true on any sequence of refinements if a_h,b_h are known. To obtain a uniform exponential rate requires **uniform condition number** b_h/a_h; to sum the tails in norm also requires control of graph growth and geometry. It does not imply localization of the interacting ground-state Poisson resolvent A0,h^-1.

## Original M5 numerical audit

Source: original archived Whitney NPZ from ChatGPT Library /The Singular Boundary/Source, SHA256 d7bd716dcfa5ef640aabb824099ad614b4d64bfb781a3cbf4cc484bb8e902fbf. N=30, M has 66 nonzero off-diagonal unordered pairs of 435 (threshold 1e-12), whereas its inverse K=M^-1 has **all 435** off-diagonal entries nonzero above 1e-10. Eigenvalues a=0.14317414869400802, b=1.1046593441618966, giving rho=0.770523632337634.

Original K magnitudes binned by the **matrix sparsity graph**:
- distance 1: 132 ordered pairs, maximum |K| 2.14447223303
- distance 2: 230 ordered pairs, maximum |K| 0.65065352822
- distance 3: 258 ordered pairs, maximum |K| 0.05412938274
- distance 4: 186 ordered pairs, maximum |K| 0.00454112837
- distance 5: 64 ordered pairs, maximum |K| 0.0001203060311.

All 900 entries passed the Neumann spectral upper bound |K_ij|≤rho^d/a. These bounds are quite loose for the current condition number, and observed decay at one finite disk cannot be extrapolated as a theorem in h.

Using actual endpoint-sharing **line-graph distance** to the deleted face0 edge set [1,4,13,0] rather than the matrix sparsity graph, the off-face vector w^T K (w=s/2 on the face) has:
- 10 neighboring off-face links at distance 1: Euclidean norm 0.6708400401044,
- 16 off-face links at distance 2: Euclidean norm 0.0988607808008,
- total off-face Euclidean norm 0.6780854027243.
This measures *static radial kinetic mixing*, not the decay of the two interacting Poisson responses u1=−A0^-1W, u2=A0^-1[W A0^-1 W−mean].

## Why the remaining proof does NOT follow

A local forcing W and exponentially decaying entries of K=M^-1 do not by themselves imply exponential decay of the interacting Poisson solution A0^-1 W. The latter also depends on the stationary interacting ground state, its spectral gap or mixing properties, the nonlinear root transports, and the spatial dependence of the generator. To prove the needed uniform response one must provide dynamical sensitivity/mixing estimates (e.g. an appropriate commutator/influence bound and gap) with constants uniform on a **genuine M_h family**. No original refined Whitney matrices beyond the archived M5 were verified in this study, so no refinement scaling inference is justified.

## Reproducibility and storage

Executed source: research/scripts/audit_m5_inverse_metric_locality.py, backed by original Whitney NPZ and recovered original Penrose geometry in ChatGPT Library /The Singular Boundary/Source. Only text source and report are committed to Git. No binary NPZ in Git. The project-specific continuum mass-gap problem remains open.
