# R3-IR-549 — Full-metric conditional Fisher criterion for a uniform deleted-face center cap

Date 2026-10-30. **Conditional theorem, not a Penrose uniform estimate.**

## Statement

Let H_h=-L_h+V_h be a finite SU(2)-link Hamiltonian with self-adjoint positive elliptic electric carré du champ Γ_h, a smooth normalized strictly positive ground-state amplitude Ω_h, and a selected fundamental face f for which the exact pointwise radial closure of R3-IR-546 holds:

Γ_h(p,p)=κ_h(1-p²),  L_h p=-3κ_h p, κ_h>0, p=cos u, u∈[0,π].

Let the push-forward Ω_h² dμ under p have density w(p)ψ_h(p)², where w(p)=(2/π)sqrt(1-p²), and let

I_h(u)=E_{Ω_h² dμ}[ Γ_h(log Ω_h,log Ω_h) | p=cos u ].

Assume an absolutely continuous representative of log ψ_h on u∈(0,π) and finite conditional scores. Then the exact weak Ward identity from R3-IR-545 and radial closure imply

|d log ψ_h(cos u)/du| ≤ sqrt( I_h(u)/κ_h )   a.e.

Indeed (log ψ_h)'_p=j_h(p)/(κ_h(1-p²)), j_h=E_{Ω²}[Γ_h(p,log Ω)|p]. Conditional Cauchy–Schwarz gives |j_h|²≤κ_h(1-p²)I_h; |dp/du|=sin u, so the angular bound follows.

If B_h=∫_0^π sqrt(I_h(u)/κ_h)du <∞, then osc_u log ψ_h≤B_h, whence since ∫ψ_h² w dp=1, ψ_h(u)²≥exp(-2B_h) at a.e. u. Thus for every measurable radial event A, in particular a two-center cap C_delta,

**Pr_{Ω_h²}(A) ≥ exp(-2B_h) Pr_Haar(A).**

A uniform B_h≤B_* is a sufficient condition for a positive refinement-uniform multiplicative cap coefficient exp(-2B_*). In particular the stronger sup_u I_h(u)/κ_h≤J_* yields B_h≤π sqrt(J_*). Neither assumption is currently established for the actual interacting Penrose vacuum.

## Crucial distinction

The conditional I_h(u) uses the **full positive metric and all link gradients**. It does not arise from fixed-spectator coordinate conditioning; all cross-link kinetic couplings remain present. In the actual original M5 inverse Whitney matrix (SHA-256 d7bd716dcfa5ef640aabb824099ad614b4d64bfb781a3cbf4cc484bb8e902fbf), f0 edge IDs [1,4,13,0], incidence [1,1,-1,-1], κ0=2.362228738429273. The weighted coupling vector w^T K, w_i=s_i/2 on the face, has off-face l2 norm 0.6780854027243318. The row K_{13,j} has off-diagonal l2 norm 0.8350681872696013. The Schur kinetic constant for edge 13 is 1/M_ee=1.2855799879953353, while K_ee=1.6134216578087173. Discarding mixed terms is invalid.

## Stress test and research obligation

Normalized center-symmetric rotor Ωλ=Zλ^-1/2 exp(-λp²) has conditional Γ(logΩλ)=4λ²κ p²(1-p²), so ∫_0^π sqrt(I/κ)du=2λ; the inequality is pointwise saturated by the absolute angular derivative. The conditional Fisher criterion is sufficient but not necessary for a relative cap bound; this explicit family does not represent the physical Wilson Hamiltonian.

The remaining task is a genuine refinement-uniform Penrose estimate on B_h or a weaker **signed** one-sided radial current/oscillation, exploiting the local Wilson interaction and a controlled inverse-Whitney covariance/transport structure. Neither a global Dirichlet energy bound nor finite regulated protected-link spectral gap suffices by itself. The refinement matrices M_h and physical coupling normalization remain to be established. No continuum Yang–Mills mass gap follows.

Reproducer: research/scripts/audit_penrose_conditional_fisher.py. Original matrix in ChatGPT Library /The Singular Boundary/Source; binary data not committed to Git.
