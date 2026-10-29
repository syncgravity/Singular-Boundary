# The Singular Boundary — Fixed-support spectral localization to sparse SU(2) curvature defects

**Date:** 2026-10-28. **Evidence classification:** finite genuine interacting SU(2) Wilson ground-state theorem under stated regional form-energy and exponential-moment hypotheses. This report establishes an exact **low-curvature/sparse-defect decomposition** for fixed physical supports, including an energy-weighted spectral comparison and quantitative physical bad-face-area bounds. It does NOT prove that the sparse-defect part vanishes, nonlinear–Gaussian vacuum convergence, fixed-energy source survival, a continuum physical mass gap, or the Stage 7/26 action correspondence. No Monte Carlo.

## 1. Exact model and inputs

Take a finite face-complete simply connected edge-to-edge rhombus disk. Every magnetic face has four edges; each edge belongs to at most two faces. On the Gauss-invariant physical subspace of L²(SU(2)^E,dHaar), use

H_h=Σ_e a_e(-Δ_e)+Σ_f b_fd_f,  d_f=1-p_f,  p_f=ReTr(W_f)/2,

with 0<a_e<=a_* and b_f>=β/h² for faces in the chosen fixed-physical-size interior region D. Let Ω_h>0 be the unique normalized ground state and K_h=H_h−E0. The local form comparison and exponential-moment theorem previously established on the branch imply, for Z_h=hΣ_{f∈D}d_f and every fixed integer r>=1,

sup_{0<h<=h0} E_{ν_h}[Z_h^r] <= M_r <∞, ν_h=Ω_h²dHaar.  (DL-1)

The interior collar and magnetic lower bound are required for uniform M_r. The q_f are any real signed weights with |q_f|<=q_* independent of refinement. All constants below may depend on a_*, β, q_*, region geometry, M_1,M_2 and the cutoff, not h or the ambient complete disk.

## 2. Exact global SU(2) angle and derivative bounds

Write u=arccos(p)∈[0,π] and d=1−cos(u). The intrinsic quadratic trace-angle is Q=u²/2. Define r=Q−d. Since 1−cos u >=2u²/π² for u∈[0,π], and Taylor's theorem gives 0<=r<=u⁴/24,

0<=r<=c_2 d²,  c_2=π⁴/96.  (DL-2)

In the fundamental SU(2) Casimir normalization |∇_ep|²=(1−p²)/4 for any incident edge. Consequently |∇_eu|²=1/4 almost everywhere, and

|∇_er|²=(u−sin u)²/4 <=u⁶/144 <= c_3 d³, c_3=π⁶/1152,  (DL-3)

while |∇_ed|²=(1−p²)/4 <=d/2. The principal class-angle is Lipschitz but not smooth at the center W=−I; these identities are valid almost everywhere as Sobolev-form identities. The **good cutoff source** below is smooth because it vanishes before the cut locus.

## 3. Good–bad decomposition and true-vacuum Hilbert norm bound

Choose 0<δ_h<=1/2 and any C^1 cutoff χ:[0,∞)->[0,1] satisfying χ=1 for x<=1, χ=0 for x>=2, and ||χ'||∞<=C_χ. If desired smooth it to C∞ preserving finite C_χ. Put

g_{δ,f}=r_f χ(d_f/δ),
s_{δ,f}=r_f[1−χ(d_f/δ)],
G_h=√h Σ_{f∈D}q_f g_{δ,f},  S_h=√h Σ_{f∈D}q_f s_{δ,f},
R_h=G_h+S_h=√hΣ q_fr_f.  (DL-4)

On the support of χ, d<=2δ and r<=c_2d²<=2c_2δ d. Thus deterministically

|G_h| <=2c_2 q_* δ h^(−1/2) Z_h.

By (DL-1),

||G_hΩ_h||² <=4c_2²q_*² M_2 δ²/h.  (DL-5)

Centering G by EνG only reduces its Hilbert norm. Hence **if δ=o(√h), the good source vanishes in actual nonlinear ground-state norm at fixed physical support**.

## 4. Genuine physical first spectral moment of the good part

By the product/chain rule, on d<=2δ,

|∇_e g_δ| <= |∇_e r| + (C_χ/δ)r|∇_ed|
              <= (√c_3 +√2 C_χ c_2)d^(3/2) = C_g d^(3/2),

and ∇g=0 for d>2δ. Thus |∇g|²<=4C_g²δ²d. Since no edge belongs to more than two faces,

Γ(G_h)=Σ_e a_e|∇_eG_h|² <=32a_*q_*² C_g² δ² Z_h. (DL-6)

The exact interacting ground-state transform gives

m_1(G_h)=〈G_hΩ_h,K_hG_hΩ_h〉=Eν Γ(G_h) <=32a_*q_*² C_g²M_1 δ². (DL-7)

This statement is in the **physical Gauss-invariant excitation sector**. Centering makes no difference to its positive-energy spectral moments. No Gaussian approximation, clustering assumption, or spectral gap enters.

For the complete remainder R_h, DL-3 and d³<=4d imply

m_1(R_h)<=32a_*q_*² c_3 M_1=O(1). (DL-8)

By the quadratic Hilbert inequality, m_1(S_h)<=2m_1(R_h)+2m_1(G_h)<=C. (DL-9)

## 5. Uniform comparison of energy-weighted *physical spectral measures*

For any gauge-invariant source B, let \tilde B=B−EνB and define the positive spectral measure μ_B(I)=||P_I(K_h)\tilde B Ω_h||² on (0,∞). Its energy-weighted counterpart is

σ_B(I)=∫_I E μ_B(dE)=||P_I(K_h)K_h^(1/2)BΩ_h||².

With x_g=K_h^(1/2)G_hΩ_h, x_s=K_h^(1/2)S_hΩ_h, the total-variation norm satisfies, for any bounded Borel |φ|<=1,

|〈x_s+x_g,φ(K)(x_s+x_g)〉−〈x_s,φ(K)x_s〉|
 <=2||x_g||||x_s||+||x_g||².

By DL-7 and DL-9, **uniformly over the entire physical spectrum**

||σ_{R_h}−σ_{S_h}||_TV <= C δ. (DL-10)

For every fixed positive energy cutoff ε>0, E^(-1)1_{E>=ε} is bounded by 1/ε, so

||μ_{R_h}−μ_{S_h}||_{TV, [ε,∞)} <= C δ/ε. (DL-11)

The Euclidean physical-energy-weighted response satisfies

sup_{t>=0}|−C'_{R_h}(t)+C'_{S_h}(t)| <= Cδ,  C_B(t)=〈\tilde BΩ,e^(−tK)\tilde BΩ〉. (DL-12)

**Important qualification:** DL-11 does not control the ordinary spectral measures near E=0 and DL-12 does not imply an unweighted Euclidean correlator comparison without a low-energy condition. This is the precise surviving infrared gate.

## 6. Bad-face area and optimal two-error tradeoff

Define N_bad=# {f∈D : d_f>δ}. Since 1_{d_f>δ}<=d_f/δ,

A_bad=h²N_bad <=(h/δ)Z_h. (DL-13)

Consequently ||A_bad||_{L^r(ν_h)}<=M_r^(1/r) h/δ for every fixed r>=1, and P(A_bad>=η)<=M_1 h/(ηδ). The exponential regional Laplace bound strengthens fixed-positive-area tails to exp(−cηδ/h³+C/h²) for δ/h→∞, with constants stated in the preceding regional exponential-tilt theorem.

The conditions δ>>h (vanishing expected bad physical area) and δ<<√h (vanishing good-source norm) are compatible. The power choice δ=h^γ with **1/2<γ<1** gives

||G_hΩ_h||=O(h^(γ−1/2)),  m_1(G_h)=O(h^(2γ)),
||A_bad||_{L^r}=O(h^(1−γ)),  ||σ_R−σ_S||_TV=O(h^γ).

Balancing the first and third errors chooses γ=3/4:

||G_hΩ_h||=O(h^(1/4)),  ||A_bad||_{L^r}=O(h^(1/4)),
m_1(G_h)=O(h^(3/2)),  ||σ_R−σ_S||_TV=O(h^(3/4)). (DL-14)

The pair of error rates is a consequence of the current prior moment bounds, **not a claim of optimality among all possible vacuum estimates**.

## 7. Why this is a partial solution and not a fixed-support equivalence theorem

For γ∈(1/2,1), the bad faces occupy vanishing physical area in every fixed L^r sense, and all source energy-weighted spectral strength at fixed support differs by o(1) from that of the bad contribution alone. Nonetheless, a coherent rare-defect branch could dominate the *centered* remainder variance. The earlier independently constructed positive gauge-invariant trial states have precisely this property without being interacting ground states. The current proof does not exclude such behavior in the actual vacuum, because it lacks a true-vacuum **connected covariance estimate for the bad contribution**:

Var_{Ω_h}(S_h)=hΣ_fg q_f q_g Cov_{Ω_h}(s_{δ,f},s_{δ,g}) = o(1) ?  OPEN.

The stronger connected-normalization problem, true fixed-time Wilson-field survival, quartic resolvent, all-excitation gap, and Stage7/26 source correspondence remain open. No mass gap is claimed.

## 8. Verification and integrity

`verify_sparse_defect_energy_localization.py` verifies exact polynomial SU(2) angle-gradient inequalities on the full class-angle interval with rigorous symbolic constants, the cutoff gradient estimate, incidence constants, power-law tradeoff, and exact 3-rhombus 10-edge spatial Penrose fixture. Also checks small finite genuine interacting SU(2) physical rotor spectral measures deterministically. The verifier does not prove the growing-volume vacuum nor rerun historical Q14, and does not use Monte Carlo. The report is self-contained given the previously proved uniform regional moments.