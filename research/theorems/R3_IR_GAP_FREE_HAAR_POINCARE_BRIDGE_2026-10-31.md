# R3-IR — Gap-free SU(2) Haar comparison from one-link Wilson Fisher energy

Date 2026-10-31. Exact finite-volume theorem. No continuum mass gap or regulator-uniform current conclusion.

Let the positive normalized deleted-face Wilson ground state have relative radial class amplitude Ψ(u), with SU(2) Haar angular density ω(u)=2sin²u/π, ∫ωΨ²=1, and I_ang=∫ω|Ψ′|². For a target edge e incident at v set B_v=Σ_(k∋v) a_k⁻¹ and b_inc=Σ_(g≠f:e∈∂g)b_g.

**HP-1 (sharp class SU(2) Poincaré).** Var_ω(h)≤(1/3)∫ω|h′|². The first nontrivial class eigenfunction cos u has radial eigenvalue 3; higher eigenvalues are n(n+2).

**HP-2 (gap-free total variation).** Writing c=∫ωΨ and using normalization, 1−c²=Var_ω(Ψ)≤I_ang/3. Cauchy–Schwarz gives TV(Ψ²ω,ω)=½∫ω|Ψ²−1|≤√(1−c²)≤√(I_ang/3).

**HP-3 (local Wilson bound).** The archived one-link Ward bound I_ang≤4S_(0,e), and local gauge-charged coercivity gives S_(0,e)≤(3B_v/16)b_inc. Consequently

**TV(target face class marginal, SU2 Haar class law) ≤ min(1, ½√(B_v b_inc)).**

For the center cap p≥1−h, m_H(h)=[arccos(1−h)−(1−h)√(2h−h²)]/π∼4√2/(3π)h^(3/2), the probability is at least max(0,m_H(h)−½√(B_v b_inc)). Haar-order mass from this estimate requires B_v b_inc=o(h³). Candidate b_inc∼h⁻² with B_v∼1 makes it vacuous. Total-variation control alone also cannot bound unweighted signed log-current. This is an independent gap-free comparison, not the needed center-collar anti-depletion theorem.

10 deterministic positive radial test profiles (including 3 near-sharp eigenfunction perturbations); maximum positive Poincaré violation zero. Exact proof, verification code, JSON and SHA256 are in Library /The Singular Boundary/Proof Audits/R3_IR_GAP_FREE_HAAR_POINCARE_BRIDGE_2026-10-31.zip. Full signed-current, connected covariance and continuum mass gap remain OPEN.