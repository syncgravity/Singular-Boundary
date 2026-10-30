# Exact curvature residual decomposition and local nonlinear action-excess tails

## Scope
Finite, bounded-incidence oriented spatial-temporal Wilson complexes with SU(2) link variables, normalized product Haar measure; coupling 0 <= beta_p <= c_+ lambda, lambda >= 2. No claim that arbitrary Penrose thin supports satisfy uniform stable filling or absolute plaquette large-field suppression.

## A. Algebraic curvature decomposition
On a finite gauge-fixed real vector space V, let D_0: V -> F_0 and D_Q:V -> F_Q denote weighted linearized undeleted and inserted curvature maps. With the Moore-Penrose inverse D_0^dagger, P=D_0^dagger D_0 is the orthogonal projection onto (ker D_0)^perp. Put A_Q=D_Q D_0^dagger and R_Q=D_Q (I-P). Then exactly D_Q=A_Q D_0+R_Q, and R_Q=0 iff ker D_0 subset ker D_Q. rank(R_Q)<=dim F_Q<=3|Q|. The norm of A_Q is not uniform without an additional stable filling/Poincare bound. This is a linearized identity, not a global nonabelian face-coordinate factorization.

If H_0=lambda D_0^* D_0+mu I (mu>0), its inverse splits with P_N=I-P as H_0^-1=mu^-1 P_N+ P H_0^-1 P. Because D_0P_N=0 and R_Q P=0, cross covariance vanishes exactly:
D_Q H_0^-1 D_Q^* = A_Q [D_0 H_0^-1 D_0^*] A_Q^* + mu^-1 R_Q R_Q^*.
Hence 0 <= first term <= lambda^-1 A_Q A_Q^*. There is no cutoff/infrared-uniform total curvature covariance if R_Q != 0 and mu -> 0. The residual rank <=3|Q|, but its spatial localization is not established.

## B. Local nonlinear Wilson action-excess tail
For arbitrary finite link subset K of size k, fix all outside links v. Let S_K(u;v) be the sum over plaquettes incident to K (including all spatial and temporal ones), and M_K(v)=min_u S_K(u;v). Define conditional Gibbs measure pi_v(du)= e^-S_K(u;v) du/Z_K(v).

Bounded incidence and bounded plaquette perimeter provide a second-derivative bound along product SU(2) geodesics <=C lambda sum_{e in K}|X_e|^2 at a minimizer; stationarity removes the first-order term. Integrate a product of Haar balls with radius c/sqrt(lambda) around a minimizer. Their volume >=(c' lambda^-3/2)^k and action <= M_K+Ck, so Z_K(v)>=exp[-M_K(v)-L_k], L_k= (3/2)k log(lambda)+Ck. Consequently for any s>=0:
pi_v(S_K-M_K >= L_k+s) <= e^-s.
Proof: numerator <=exp[-M_K-L_k-s] times Haar probability <=1, divide by lower normalization. Uniform over exterior v, cutoff h, and ambient volume. Averaging the conditional probability over the *actual* exterior marginal yields same inequality:
mu(S_K(U)-M_K(U_out)>= L_k+s) <= e^-s.
Also E[S_K-M_K|v] <= L_k from nonnegative relative entropy to Haar. These are unconditional, genuinely nonlinear *local excess* bounds and do NOT imply P(d_p>delta for all p in Q) without separately showing that that event forces S_K-M_K large. If M_K is of order lambda on frustrated exteriors, the event may have no excess penalty.

## C. Conditional contour implication (not unconditional)
For selected Q subset incident to K with beta_p>=c_-lambda, if on exterior configurations v in B one has M_K(v)<=m_*(v) and on event A_X all p in X subset Q satisfy d_p>delta, then S_K-M_K>=c_-lambda delta|X|-m_*(v). Therefore
mu(A_X intersection {M_K<=M_*}) <= exp[-c_-lambda delta|X|+M_*+L_k] (clamped by 1).
For arbitrary v, the decomposition mu(A_X) <= mu(M_K>M_*) + exp[-c_-lambda delta|X|+M_*+L_k] holds. The first term is uncontrolled. This precisely distinguishes local thermal large-field suppression from incompatible-background suppression.

## D. Nonlinear geometry caveat
The linear R_Q decomposition preserves infinitesimal constraints, not the nonlinear SU(2) Bianchi words globally. Exact Bianchi compatibility for the nonlinear tail theorem is automatic because integrations range over genuine SU(2) link variables. A uniform local nonlinear filling for arbitrary Penrose thin supports is not asserted.

## Status
Proved: finite-dimensional exact residual decomposition; sharp splitting of Gaussian curvature covariance into fillable and free curvature; conditional and unconditional local *action-excess* tails of Wilson Gibbs measure, uniform in exterior and ambient volume. Not proved: uniform bound on A_Q for all arbitrary supports; nonflat-background relative Hessian control; absolute Wilson large-field contour estimate; suppression of M_K under exterior Gibbs; arbitrary-support O(|Q|log lambda) insertion free-energy bound; R3/R2 mass gap.
