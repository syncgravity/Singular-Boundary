# Refinement-dependent Wilson truncation and localized cap response budget
Date: 2026-10-30
Status: exact finite-regulator inequality and conditional Penrose criterion. No quantitative uniform bounds proved.

For each finite SU(2) Penrose disk refinement h, deleted face f, put p=P_f Omega^-, q=Q_f Omega^-, K=H_f^--E_f^-, A=Q_f K Q_f on Ran Q_f and lambda_Q=inf spectrum(A)>0 at fixed regulator. With p smooth and source s=-Q_f T p in L2, the exact equation is Aq=s. Select finite retained gauge-invariant Wilson approximation p_N with P_f p_N=p_N, and let s_N=-Q_f T p_N, q_N=A^-1 s_N. For cap multiplication M_delta (norm <=1),
||M_delta q|| <= ||M_delta q_N||+||A^-1(s-s_N)||
<= ||M_delta A^-1 s_N|| + lambda_Q^-1 ||Q_f T(p-p_N)||.
This is an EXACT inequality for each finite regulator and its operator-domain approximants. It is not a uniform estimate because lambda_Q and source complexity can deteriorate.

A sufficient but unproved refinement criterion, uniformly for bulk faces f and delta_h comparable to h, is:
(i) inf_(h,f) ||P_f Omega^-|| >= c0>0;
(ii) sup_f ||M_delta_h A^-1 s_(N(h))|| = o(h^(3/4));
(iii) sup_f [lambda_Q^-1 ||Q_f T(p-p_(N(h)))||] = o(h^(3/4)).
Then by triangle ||M_delta Q Omega||=o(h^(3/4)), and the exact local Haar comparison gives m_f^-(delta_h)>=(c0²-o(1)) c_delta_h, with c_delta_h~constant h^(3/2). This suffices for the previously established logarithmic magnetic deletion comparison via exponential tilt. None of (i)-(iii) is established uniformly.

The H2 retained Wilson polynomial core at each finite regulator implies for any tolerance epsilon_h>0 and every face f there EXISTS some finite N(h,f) such that ||Q_fT(p-p_N)||<=epsilon_h lambda_Q. For finite many faces one can choose a maximum N(h) at fixed h. This diagonal selection is qualitative and does NOT prove (ii), nor bound N(h), Wilson word lengths, numerical constructibility, or source/response norms. In particular arbitrary nonconstructive N(h) does not constitute the sought continuum estimate.

A sharper cap-adapted approximation quantity is ||M_delta A^-1 Q_f T(p-p_N)||, which may be much smaller than lambda_Q^-1||Q_fT(p-p_N)||; requiring its o(h^(3/4)) is sufficient but verifying it requires exactly the localized dynamical estimate we lack. Avoid circularity.

All statements require the smooth finite volume coordinate and source operator assumptions already audited in R3_RETAINED_WILSON_GRAPH_CORE_2026-10-30.md. No polynomial Penrose cap proof, continuum construction, or mass gap claimed.
