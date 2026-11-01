# R3-IR — Ground-state-weighted transport-orbit Poincaré inequality

2026-10-31. Exact finite-volume **conditional** SU(2) theorem. Let T_g be a smooth Haar-preserving transport action on a planar original-link disk, Ω>0 the deleted Wilson vacuum, and Y_a its orbit generators normalized to SU(2) Casimir first positive eigenvalue 3/4. Disintegrate Haar by transport orbits z; let w_z(g)=Ω(T_gz)²/∫Ω(T_hz)²dh and R_z=(max_g Ω(T_gz)²)/(min_g Ω(T_gz)²). Assume Σ_a|Y_a q|²≤C_Y Γ_0(q) with Γ_0=Σ_e a_e|∇_e q|².

For the *weighted orbit mean* m_z=∫w_zq_z dg, the sharp unweighted SU(2) Poincaré inequality and density comparison give

**∫w_z|q_z−m_z|²dg ≤ (4/3)R_z Σ_a∫w_z|Y_aq_z|²dg ≤ (4C_YR_z/3)∫w_z Γ_0(q_z)dg.**

Integrating orbitwise, if R_*=ess sup_z R_z<∞,

**||q−E_ν[q|orbit]||²_(L²ν) ≤ (4C_YR_*/3)∫Γ_0(q)dν.**

This is directly in the ground-state Dirichlet form, with no extensive E0−V_- offset. Its projection is the *weighted* conditional projection, not the unweighted Haar twirl. The orbit density ratio R_* is not controlled uniformly in the present Wilson proof. Smooth positive profiles Ω(g)∝exp(λ cosθ(g)) have R=e^(4|λ|), establishing that positivity, geometry and the Casimir alone do not bound R. They are not asserted to be Wilson vacua.

A radial SU(2) Gauss–Jacobi verifier checked 90 positive weighted class profiles, no inequality violations (maximum ratio to upper bound 1 within roundoff). This is an algebraic diagnostic, not an interacting Wilson-vacuum simulation. Full proof, executable checks and SHA256 archive retained in Library /The Singular Boundary/Proof Audits/R3_IR_WEIGHTED_ORBIT_POINCARE_GATE_2026-10-31.zip.

OPEN: regulator-uniform physical orbit-density control or alternate weighted coercivity; signed current sup_f T_(f,h)=o(h^(-1/4)), connected covariance, continuum Yang–Mills gap.