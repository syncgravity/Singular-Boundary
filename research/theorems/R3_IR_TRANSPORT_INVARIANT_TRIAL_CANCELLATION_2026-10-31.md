# Exact SU(2) transport-invariant trial cancellation

For any Haar-preserving original-link transport T preserving every retained plaquette trace and for any H¹ amplitude h invariant under T, the integrated signed electric-metric defect **vanishes exactly**:
\[
\int\nabla h(TU)^T[J_TAJ_T^T-A]\nabla h(TU)\,d\mu(U)=0.
\]
In particular all normalized positive trial amplitudes h=Z^{-1/2}F((p_g)_{g≠f}) have zero integrated signed defect for **every** tree–cotree choice, even when their pointwise defect densities have both signs and the maximum positive Jacobian eigenvalues differ.

Let B_T(h,k)=E(P_Th,P_Tk)−E(h,k). If d_abs is the uniform absolute normalized metric-distortion operator norm and h₀ is transport invariant, then for r=h−h₀,
\[
|B_T(h,h)|\le d_{abs}\{2\sqrt{E(h₀)E(r)}+E(r)\}.
\]
For the actual ground state Ω, Q_T=B_T(Ω,Ω)≥0; this controls Q_T only **conditionally** on an electric Sobolev approximation of Ω by invariant h₀. No such regulator-uniform approximation has been proved.

The 3×3 planar full-link checker verified 180 transport/configuration cases, maximum retained holonomy discrepancy 4.14e−15, trial invariance discrepancy 7.11e−15, and full Jacobian chain discrepancy 1.54e−7. Checks are algebraic, not physical vacuum measurements.

Complete proof, reproducible code, results and SHA256 manifest: Library `/The Singular Boundary/Proof Audits/R3_IR_TRANSPORT_INVARIANT_TRIAL_CANCELLATION_2026-10-31.zip`. Signed-current, covariance, and Yang–Mills mass gap remain OPEN.