# R3-IR-441 — Wilson cap correlation with exterior through a boundary-shell resolvent

2026-10-30. Exact finite-volume response identity and Cauchy-Schwarz inequality for genuine original-link SU(2) Wilson ground states. No distance decay or continuum mass gap is claimed.

Let S be a finite set of original links containing the complete target face, and let T be a disjoint set of exterior links at arbitrary graph distance. Fix a retained magnetic face g that involves a link in T but none in S. Consider H(t)=H0+t b_g(1-p_g), with all other couplings retained; let Omega_t be the unique positive gauge-invariant ground state. Let O=k(W_f) depend only on S, and let E_t and R_t denote ground energy and reduced resolvent.

The exact first derivative is
d/dt <O>_t = 2b_g <Q_t O Omega_t,R_t Q_t p_g Omega_t>. (BR-1)

Define a source-specific transport kernel
K_t(O,p_g)=<Q_t O Omega_t,R_t Q_t p_g Omega_t>.
For any tau>0, spectral calculus gives the rigorously convergent heat representation
K_t(O,p_g)=int_0^infinity <Q_tO Omega_t,e^(-s(H(t)-E_t))Q_tp_g Omega_t> ds.
At each finite connected compact-link volume, the positive spectral gap above the unique ground state makes the integral finite, without asserting any uniform lower gap.

There is an exact temporal split at tau:
K_t=K_t^{short}(tau)+K_t^{long}(tau),
with integrals over [0,tau] and [tau,infinity]. Define
A_O=<QO Omega,RQO Omega>, A_p=<Qp Omega,RQp Omega>.
By reduced-resolvent Cauchy-Schwarz, |K_t|<=sqrt(A_O A_p); this bound does not encode graph distance.

For any s>=0, the heat-semigroup matrix element can be bounded by
|<QO Omega,e^(-s(H-E))Qp Omega>|
<= ||QO Omega|| ||Qp Omega||,
and for s>=tau,
|<QO Omega,e^(-s(H-E))Qp Omega>|
<= e^(-delta_t(s-tau))||QO Omega|| ||Qp Omega||,
where delta_t is the finite-volume excited-state gap. The resulting long-time upper bound still depends on 1/delta_t and is not a uniform mixing theorem.

For the short-time regime, spatial separation alone is insufficient for an instantaneous exact zero because the continuous-time electric heat semigroup and interacting potential generate nonzero correlations. Establishing a quantitative bound of the form
|K_t^{short}(tau)|<=C_Og exp[-c distance(S,g)]
requires a separate locality/commutator or cluster estimate, not supplied by the current Wilson input. Moreover, making the long-time term small uniformly requires independent infrared information, or a source-specific alternative.

Thus BR-1 is an exact distant-coupling response representation, and its decomposition identifies TWO independent estimates required to turn local coercivity into multiscale cap mixing: short-time off-diagonal dynamical locality and long-time decay on cap-correlated states. No such uniform estimates are proved here. Finite-volume gap existence is not the desired continuum mass gap.
