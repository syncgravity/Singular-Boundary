# R3-IR-528 — Strong-background non-tree link gap (2026-10-30)

**Conditional finite-model theorem.** Let e be outside the rooted transport tree of a connected open SU(2) graph. Let K=M^-1 be a fixed SPD inverse-Whitney matrix, D_j=Ad(V_j)X_j with V_j rooted-tree transports, and H0=(g2²/2)D* K D+V0 where the bounded real magnetic multiplication potential V0 is independent of U_e. Let P_e integrate Haar in U_e, R_e=I-P_e, and E0=inf spec H0.

Then P_e reduces H0 and, as quadratic forms,

**R_e(H0-E0)R_e >= [3g2²/(8M_ee)]R_e.**

Proof: Split electric derivatives into d_e and d_B. Schur square completion gives (d_e,d_B)*K(d_e,d_B)=(d_B+K_BB^-1 K_Be d_e)*K_BB(d_B+K_BB^-1 K_Be d_e) + (1/M_ee)|d_e|². Treating wavefunctions as Hilbert-valued functions of background links, the modified base derivatives are metric-compatible: K_BB^-1 K_Be d_e are skew-adjoint operators in the fiber SU(2)_e and the rooted coefficients are independent of U_e. The Hilbert-valued diamagnetic/Kato inequality bounds the first term below by the P-sector background kinetic energy acting on the scalar fiber norm ||psi(.,Y)||. V0 depends only on Y. Thus H0>=E_P+(g2²/(2M_ee))sum_a||X_e^a psi||², where E_P is the lowest P-sector energy. Restriction to P-sector yields E0=E_P. On R-sector the SU(2) Haar Poincare eigenvalue is 3/4, proving the gap. Operator-domain passage uses smooth density and quadratic-form closure.

If H_b=H0-bp_g activates the unique adjacent face g containing free link e, with 0<=b<gamma_e:=3g2²/(8M_ee), then E_b<=E0 (P-sector ground has Haar expectation p_g=0); consequently R_e(H_b-E_b)R_e >= (gamma_e-b)R_e. Projecting the ground-state eigenvalue equation gives ||R_e Omega_b||<=b/(gamma_e-b). Normalizing the P_e component produces an exact conditional-Haar link state, so Prob_Omega_b(C_g,delta)>=[c_delta-b/(gamma_e-b)]_+. This controls the *adjacent* face g, NOT the original deleted face 0, and it is additive, not uniform as delta->0.

Archived 30-link M5 matrix, g2²=1: (e,M_ee,gamma_e): (86,.213484466207,1.75656808509); (88,.453203129242,.827443536471); (372,.203825432189,1.83980966444); (26,.388929514047,.964184990997). With b=3/32000, b/(gamma_e-b) respectively 5.33739652e-5,1.13313621e-4,5.09589547e-5,9.72418336e-5. Floating-point numbers not interval-certified. Numerical check script: research/scripts/validate_m5_strong_background_local_gap.py.

Caveats: "strong background" permits arbitrary other plaquette couplings, NOT arbitrary *selected* b. Model depends on chosen rooted transport prescription; no physical refinement-uniform ratio b/gamma_e, deleted-face center cap, or continuum Yang-Mills mass gap proved.
