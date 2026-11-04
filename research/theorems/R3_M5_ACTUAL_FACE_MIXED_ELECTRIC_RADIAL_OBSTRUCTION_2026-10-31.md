# R3-IR-599 — Actual archived M5 face-4 mixed-electric carré-du-champ is not pointwise radial

Date 2026-10-31. Extends R3-IR-598 by interrogating actual archived candidate prism matrices, **not merely a toy 2×2 metric**.

Loaded `penrose_prism3d_candidate_matrices_2026-10-31.npz` and `penrose_prism3d_plaquette_incidence_2026-10-31.npz` from Library. Candidate M5 has 98 edges. In tree gauge, rooted gauge-transports are identity at the evaluation point but derivatives with respect to tree links are **not dropped**. Face 4 has oriented word (U_f=U_1 U_5 U_{26}^{-1} U_2^{-1}). Let (p_f=\mathrm{Re}(U_f)). For generators (T_a=\mathbf e_a/2), use left link derivatives (X_{e,a}p_f); for inverse incidence, derivative insertion is (-U_e^{-1}T_a). Let (K=(M5_{3D})^{-1}). Evaluate the bare fixed-K carré du champ (\Gamma(p_f,p_f)=\sum_{ee'a}K_{ee'}X_{e,a}p_f X_{e',a}p_f).

The two explicit configurations, with all unspecified links identity, are:
- (U_1=I, U_{26}=\mathbf i): (p_f=0), (\Gamma=40.29941845124068).
- (U_1=\mathbf j, U_{26}=\mathbf k): (p_f=0), (\Gamma=32.62609028239079).

The difference 7.67332816885 at equal face trace is an explicit **pointwise obstruction** to treating this mixed-metric kinetic coefficient as a function of the face class coordinate alone. Four face edges [1,5,26,2] and full 98×98 inverse Whitney K were used. Independent central-difference checks on every link-direction derivative for both configurations agree to at most 2.09e−14.

**Critical limitation:** This calculation uses the archived inverse-Whitney K and the specified tree-gauge left-link derivative convention. If the full physical Penrose rooted operator contains link-dependent transports, its gauge-covariant divergence form and link-dependent coefficients must be incorporated before identifying its true carré du champ. It also does **not** compute conditional (a_f(p)=\mathbb E_{\Omega^-}[\Gamma(p,p)\mid p_f=p]), drift (b_f), or score (c_f), because the nonlinear interacting deleted ground state is unknown. A pointwise obstruction does not preclude **conditional radial closure** after averaging. The preceding fixed-coefficient scalar radial estimates R3-IR-596–597 remain conditional, not verified properties of the Penrose vacuum.

Executable `audit_M5_actual_face_radial_coeff.py` and numerical audit `m5_actual_face4_pointwise_gamma_2026-10-31.json` preserved in ChatGPT Library `/The Singular Boundary/Source/`. No regulator-uniform interacting score or continuum Yang-Mills mass gap is proven.