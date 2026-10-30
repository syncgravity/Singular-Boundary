# Ground-state electric-energy control without off-block operator norms

Date 2026-10-30. Finite open SU2 disk, with independent deleted-face Haar coordinate and two-link fiber e,d. This theorem does not establish refinement-uniform center caps or a continuum mass gap.

Let H=H_E-sum_g b_g p_g, where b_g>=0, |p_g|<=1, product Haar is normalized, and H_E is the Friedrichs operator of a positive gauge-covariant inverse-Whitney electric quadratic form. Assume H_E >= c T, with T=sum_e(-Delta_e), c=g2_squared/(2 lambda_max(M))>0. Let Omega denote a normalized ground state and E0 its energy. The constant wavefunction is electric-zero and has zero expectation for each fundamental elementary plaquette trace on an open disk, hence E0<=0. Write B=sum_g b_g. Since V=-sum_g b_g p_g >=-B, the energy identity gives <Omega,H_E Omega> = E0-<Omega,V Omega> <= B.

Let P=P_e P_d be the product-link Haar average over the two links implementing the deleted-face conditional Haar fiber, R=I-P. Each nonconstant SU2 link representation has electric Casimir >=3/4, so the exact link Poincare estimate T >=(3/4)R holds as a quadratic form. Assuming the geometric fiber property Q_f P=0, we have ||Q_f Omega||<=||R Omega||. Therefore

||Q_f Omega|| <= min(1,sqrt(4B/(3c))) = min(1,sqrt(8 lambda_max(M) B/(3 g2_squared))).

No commutation of P with H_E, no bounded R H_E P, and no gap for the switched-off interacting environment is assumed. The price is dependence on the *total* magnetic strength B. At large volume or under physical 2+1 scaling b_f~h^-2, this bound generally becomes vacuous. It is not a replacement for a local Schur/Feshbach or ground-state-transform estimate and does not prove shrinking-center cap probability.

For the archived 11-face matrix lambda_max(M) approximately 1.104659344 and ten equal b_g=3/32000 at g2_squared=1, B=0.0009375 and c approximately 0.452628; the resulting bound is about 0.05255. These are double-precision illustrations, not interval-certified spectral constants. The general inequality is analytical.
