# Multiscale boundary-defect transfer: exact thermal bound and a conditional contraction criterion

Date: 2026-10-27. Status: conditional criterion only, NOT an arbitrary-support Penrose theorem.

## Local thermal-excess lemma
Let K be k adjustable links and S_K(U_K;v) include every plaquette touching K, with normalized Haar reference, at most Delta faces per link, bounded face length and beta_p <= c lambda. Let M(v)=min S_K. At a minimizer the first derivative of smooth S_K vanishes. On product geodesic balls radius c'/sqrt(lambda) about a minimizer the action is <= M+Ck (bounded Hessian row sums). The Haar volume is at least (c'' lambda^{-3/2})^k. Hence the conditional partition function Z(v)>=exp[-M-L], L=(3/2)k log(lambda)+Ck. For T=S_K-M >=0, for s>=0, P(T>=L+s |v)<=exp(-s). For any 0<t<1,
E[exp(t T)|v] <= exp(t L) (1+t/(1-t)) = exp(tL)/(1-t).
This bound is rigorous, conditional on any exterior v, with no insertion free energy assumed.

## Abstract multiscale transfer criterion
Suppose nonnegative boundary-defect variables X_0,...,X_R are associated with nested sigma fields F_0 superset F_1 superset ... superset F_R, and thermal variables T_j >=0 for j=0,...,R-1 are F_j measurable. Assume almost surely
X_j <= a_j + b_j X_{j+1} + T_j,
where a_j,b_j are deterministic nonnegative coefficients. Assume conditional mgf bounds for 0<=u<=t_*<1
E[exp(u T_j)|F_{j+1}] <= exp(u L_j)/(1-u)
with L_j=(3/2) k_j log lambda+C k_j, as follows from the local lemma when T_j really is a conditional full-sector action excess with the appropriate shell disintegration. Let B_0=1, B_j=prod_{i=0}^{j-1}b_i for j>=1. Then for any t>0 with t B_j<=t_* for all j,
E exp(t(X_0-B_R X_R)) <= exp(t sum_{j=0}^{R-1} B_j(a_j+L_j)) prod_{j=0}^{R-1}(1-t B_j)^{-1}.
Proof: expand the deterministic recursion; then integrate sequentially by conditional expectation for T_0, T_1,..., T_{R-1} using nested sigma fields. The inequality holds with X_0-B_R X_R <= sum_j B_j(a_j+T_j). Thus for s>=0:
P[X_0 > B_R X_R + sum_j B_j(a_j+L_j) + t^{-1} sum_j log(1/(1-t B_j)) + s] <= exp(-t s).

If X_R=0, sum_j B_j(a_j+k_j log lambda) <= C |Q| log lambda, and sum_j B_j <= C |Q|, this is the sought support-local absolute tail. It is a *criterion*, not an achieved estimate: the vital contraction inequality X_j <= a_j+b_j X_{j+1}+T_j is not verified for arbitrary Penrose Wilson buffers, nor are the weight budgets and outer boundary condition.

## Scaling diagnostic
If k_j ~ 2^{d j} |Q| and B_j <= C 2^{-sigma j}, sum_j B_j k_j uniformly finite only if sigma>d. In three-dimensional volume-growing shells d=3. For surface-like shell counts d=2. Mere bounded incidence provides no positive sigma; therefore the multiscale criterion is not closed by the previous geometric lemmas. This is a sufficient diagnostic, not a theorem that sigma>d is necessary for all possible approaches.

## Caution regarding independent data
The uploaded planar Penrose catalogue has no verified 3D prism face-cell incidence. No numeric Penrose-specific constants, scale-contraction coefficient, or absolute tail are certified here.

## Context
A preprint posted 2026-10-26, 'The continuum limit of three-dimensional SU(2) lattice Yang–Mills theory on a torus III: Regional renormalization and large-field control' (Hexagon 2610.00510v1) claims a regular cubic periodic torus result using reflection positivity and chessboard estimates; the preprint explicitly marks itself 'Primarily AI-generated text; Human understanding: no parts'. Even if its mathematical results are valid, they do not establish nonperiodic arbitrary-cavity Penrose bounds.
