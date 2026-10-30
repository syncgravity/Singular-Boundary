# Multiscale guard covariance and renormalized influence: formal audit

26 October 2026. The following are finite-dimensional theorems and a counterexample, not a proof of the full nonlinear Penrose R3 bound.

## A. Exact nonlinear block effective derivatives
Let X be interior links, Y retained guard links, with a local smooth chart on SU(2) per relevant link and S(X,Y) the complete Wilson action of a guarded block. Put Z(Y)=∫exp[-S(X,Y)]dX (normalized Haar), Φ(Y)=-log Z(Y). Derivatives (with fixed Haar integration domain and appropriate local charts) satisfy

  ∂i Φ = E_Y[∂i S],
  ∂i∂j Φ = E_Y[∂i∂j S] - Cov_Y(∂i S, ∂j S).

No Gaussian, small-field, or infinite-volume approximation is made. The first term is zero if no plaquette of the block touches both guard coordinates i,j, but the covariance can transmit influence through arbitrarily many interior plaquettes. Since every plaquette has bounded incidence and β≤cλ, mixed direct Hessian terms are O(λ) where present; absent a uniform conditional mixing inequality there is no distance decay for the second term. A Poincare inequality by itself gives |Cov(f,g)|≤ρ^{-1}(E||∇f||² E||∇g||²)^{1/2}, which has no spatial decay and may be O(λ²/ρ).

## B. Gaussian guard Schur complement, exact
For a positive definite gauge-fixed Hessian H partitioned into interior I and guards Y,

 H = [[H_II, H_IY], [H_YI,H_YY]],
 K = H_YY - H_YI H_II^{-1} H_IY.

The Gaussian effective action is 1/2 Y^T K Y, up to the constant (1/2)log det H_II. The covariance of retained variables is K^{-1}=(H^{-1})_YY. The large local piece H_YY is kept exactly; H_YI H_II^{-1} H_IY is the generated interaction. The identity itself does not make the normalized off-diagonal influence small.

## C. Exact scale covariance decomposition with localization estimates
For positive definite H≥μI, with ||H||≤M and finite interaction range one in the graph of matrix nonzero entries, choose times 0=t0<t1<...<tN=∞. Define
 C_j=∫_{t_j}^{t_{j+1}}exp(-tH)dt.

Then C_j≥0 and ∑C_j=H^{-1}. Thus a Gaussian A~N(0,H^{-1}) may be decomposed into independent shells with covariance C_j. This is a covariance decomposition, not automatically finite-range or a physical-mass estimate. For graph distance r=d(i,j), the Taylor polynomial of exp(-tH) of degree r-1 has zero ij entry. Hence
 |(exp(-tH))_{ij}|≤∑_{n≥r}(tM)^n/n! ≤ exp(tM)(tM)^r/r!.

Also |(exp(-tH))_{ij}|≤exp(-μt) from the operator norm. Combining and integrating gives
 |(C_j)_{ij}| ≤∫_{t_j}^{t_{j+1}} min{exp(-μt), exp(tM)(tM)^r/r!}dt.

The constants can deteriorate as μ→0, which is expected for unregulated gauge-potential modes. Shell curvature covariance is bounded as 0≤D C_j D*≤D H^{-1}D*≤λ^{-1}I whenever H≥λD*D. This upper curvature covariance does not establish guard influence contraction.

## D. Exact massless Gaussian obstruction
Consider the nearest-neighbor action on a one-dimensional chain,
 S(x)=(λ/2)∑_n(x_{n+1}-x_n)^2,
with endpoints pinned to remove its global zero mode. Retain x_{jb}=y_j, integrate the b−1 variables between each pair. Gaussian convolution, or minimization plus its Y-independent fluctuation determinant, gives exactly
 S_eff(y)=(λ/(2b))∑_j(y_{j+1}-y_j)^2 + constant.

For an interior retained coordinate j, the conditional law has mean (y_{j-1}+y_{j+1})/2 and variance b/(2λ). Its (Gaussian linear-mean) total neighbor influence is 1/2+1/2=1 at *every* b and λ. In the usual unbounded-coordinate total-variation Dobrushin definition (supremum over arbitrary neighbor configurations), each nonzero neighbor influence equals 1, an even stronger obstruction. Therefore exact Gaussian block integration, locality and cancellation of fluctuation determinants do not imply q<1 uniformly. With a guard pinning term κ y_j²/2 the normalized Hessian row influence becomes (2λ/b)/(2λ/b+κ)<1, but tends back to one if κb/λ→0.

This toy example is not a proof that the SU(2) gauge-invariant sector is gapless. It is a rigorous counterexample to an inference from *generic covariance decomposition* to strict guard contraction.

## E. Conditional Gaussian normalized influence criterion
Suppose K is a symmetric positive definite coarse Gaussian guard precision and B=diag(K_ii)>0 (scalar for simplicity); set T_ij= -K_ij/sqrt(K_ii K_jj) for i≠j, T_ii=0. If q= sup_i∑_{j≠i}|T_ij|<1, then K=B^{1/2}(I-T)B^{1/2} and
 K^-1=B^-1/2∑_{n≥0}T^n B^-1/2.

If T has graph interaction range R and diagonal entries K_ii≥k_min, then
 |(K^-1)_{ij}|≤(1/k_min) q^{ceil(d(i,j)/R)}/(1-q).

For block matrices, the same holds with operator-valued normalized off-diagonal blocks and an induced block-row norm. This is an actual proof of covariance decay *under independently verified q<1*, not a proof of q<1 for Wilson. A uniform bound on curvature covariance cannot replace that hypothesis.

## F. What has not been proved
1. Positive, gauge-fixed nonlinear Hessian and background control for every relevant Penrose coarse block.
2. Uniform conditional spatial decay of Cov_Y(∂iS,∂jS) in the exact nonlinear block.
3. A subtraction scheme that makes q<1 for the nonlinear guard action at all physical scales.
4. Nonlinear large-field and rare-background bounds, thin-support free-energy estimate, R3, or R2 mass gap.

## Sources
T. Balaban, *Propagators and renormalization transformations for lattice gauge theories. I*, CMP 95 (1984), 17–40, DOI 10.1007/BF01215753. T. Balaban, *Propagators for lattice Gauge theories in a background field*, CMP 99 (1985), 389–434, DOI 10.1007/BF01240355. These establish results in their respective lattice RG settings, not the missing Penrose transfer.
