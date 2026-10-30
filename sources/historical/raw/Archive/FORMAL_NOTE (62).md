# Weak-coupling obstruction to scale-independent SU(2) boundary-holonomy contraction

Date: 2026-10-27. Status: exact nonlinear transfer counterexample for a universal local mixing implication; NOT a no-go theorem for every Penrose relative energy-defect transfer.

## SU(2) Wilson transfer
Let G=SU(2), dg normalized Haar, d(g)=1-Tr(g)/2, q(lambda)=int exp(-lambda d(g))dg=e^{-lambda} 2I_1(lambda)/lambda. Define K_lambda(g)= exp(-lambda d(g))/q(lambda), which integrates to one. On a chain H_0,...,H_R, let H_0 be Haar and conditional transitions K_lambda(H_j^{-1}H_{j+1})dH_{j+1}. This is a strictly positive, non-Gaussian Wilson-type Gibbs distribution.

Let f(H)=Tr(H)/2. Since K_lambda is central, Schur's lemma implies integral K_lambda(g) g dg = a_lambda I_2. Character integral gives a_lambda = int K_lambda(g)f(g)dg = I_2(lambda)/I_1(lambda). Thus E[f(H_{j+1})|H_j]=a_lambda f(H_j), and E[f(H_R)|H_0]=a_lambda^R f(H_0). Fundamental-character correlation: E[f(H_0)f(H_R)] = (1/4)a_lambda^R because int f^2 dg=1/4. The asymptotic a_lambda = 1-3/(2lambda)+O(lambda^{-2}) implies for fixed R, a_lambda^R -> 1, and for R=o(lambda), a_lambda^R -> 1. A fixed factor q<1 per bounded-width layer independent of lambda therefore does not follow from Wilson positivity, bounded incidence or SU2 heat-bath alone. This is a counterexample to that *general proof mechanism*, not to contraction of a specially defined energy defect on the full Penrose complex.

## Required depth and shell-growth check
If a desired suppression a_lambda^R <= epsilon<1, then R >= (2lambda/3+O(1)) log(1/epsilon). If independent shell count grows as k_j~2^{dj}|Q| while local transfer contraction is a_lambda (approximately independent of j), the budget sum_j a_lambda^j k_j diverges geometrically for lambda large, since 2^d a_lambda>1. This does not rule out renormalized scale-dependent shell mechanisms or cancellations; it rules out proving their summability from the bare one-layer transfer factor.

## Correction to earlier request
A genuine relative cycle-defect variable Gamma need not be equivalent to f(H); this example does NOT disprove all possible Gamma contractions. Moreover a flat holonomy direction may be cost-free and its persistence irrelevant to a curvature-defect tail. To prove the desired Penrose statement would require an explicit definition of Gamma_j using actual 3D Penrose prism face–cell incidence and a separate uniform, shell-wise inequality Gamma_j <= a_j + b_j Gamma_{j+1}+T_j, with b_j decaying enough to counter shell growth. No such inequality is currently established. Current uploaded planar cycle catalogues do not contain a certified full 3D prism incidence matrix, so a claim of having checked arbitrary Penrose cavities would be unsupported.

## Independent next test
Construct face/cell coboundary for a finite extruded Penrose patch, identify harmonic/near-harmonic boundary modes and calculate the singular values of the (gauge-fixed) linearized boundary-to-boundary transfer, then separately test an energy-defect transfer after quotienting out neutral flat modes. Numerical spectral observations cannot by themselves supply a cutoff-uniform nonlinear Gibbs theorem.
