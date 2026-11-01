# R3-IR — Local Wilson Harnack refinement scaling

2026-10-31. Exact small-time SU2 heat-kernel calculation and conditional fixed-link refinement asymptotic.

Let S be the changed-link set, D_S=Δ_S V_-, B_S=Σ_(e∈S)1/a_e, and ℛ(s)=max SU2 heat-kernel k_s/min k_s for −Δ eigenvalues j(j+1). The spectator-conditioned Harnack inequality gives log R_orbit≤inf_(t>0)[2tD_S+2Σ_(e∈S)log ℛ(a_e t)]. By SU(2) heat kernel short-time geometry (round S3 radius 2; antipodal distance 2π), lim_(s→0) s log ℛ(s)=π².

For fixed finite S and fixed a_e>0 as D_S→∞, minimization yields **inf F(t)=4π√(D_S B_S)(1+o(1))**, with minimizing t∼π√(B_S/D_S). For M fixed equal-coefficient changed links, D_S∼c M b and b∼h⁻² with a∼1, the Harnack logarithmic **certificate** is of order M/h. This is not a lower bound on the actual Wilson vacuum orbit-density oscillation. If S or electric coefficients vary, additional uniformity hypotheses are needed for the asymptotic.

High-precision character-series checks at s=0.5,0.25,0.125,0.0625 yield s log[k_s(I)/k_s(−I)] = 7.697982,8.607279,9.151000,9.466781 approaching π²=9.869604. Results not Wilson vacuum measurements.

Full proof, executable 100-digit verifier and SHA256 manifest in /The Singular Boundary/Proof Audits/R3_IR_LOCAL_HARNACK_REFINEMENT_SCALING_2026-10-31.zip. Regulator uniform signed current, covariance and continuum Yang–Mills mass gap OPEN.