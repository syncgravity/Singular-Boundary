# Exact target-score contraction and one-face Fisher bound in the physical Wilson vacuum

**Date:** 2026-10-30. **Status:** exact finite-volume identity and inequality for any cage, including completed; **not** a completed-cage signed-current or continuum mass-gap estimate.

## Setting

On the original-link space \(G=SU(2)^E\) with normalized Haar \(\mu\), take
\[
H=\sum_e a_e(-\Delta_e)+V,\qquad a_e>0,
\]
with bounded continuous gauge-invariant \(V\). The unique smooth strictly positive normalized ground state \(\Omega\) is invariant under the full original vertex Gauss group. Write \(\nu=\Omega^2\mu\). Choose a simple four-link target Wilson face \(f\) (its magnetic term may be deleted), let
\(p=\tfrac12\operatorname{Tr}W_f\in[-1,1]\) and \(A_f=\sum_{e\in\partial f}a_e\).
Let \(\Gamma(g,h)=\sum_e a_e\nabla_e g\cdot\nabla_e h\).
The SU(2) fundamental-link identities give
\[
\Gamma(p)=\kappa(p):=\tfrac{A_f}{4}(1-p^2),\qquad
\mathcal L_\mu p:=\sum_e a_e\Delta_e p=-\tfrac{3A_f}{4}p.
\]
Under \(\mu\), \(p\) has Haar class density
\(w(p)=\frac2\pi\sqrt{1-p^2}\) on \((-1,1)\).
Let \(\rho(p)dp=p_*\nu\) and \(r(p)=\rho(p)/w(p)>0\). Define \(\psi(p)=\sqrt{r(p)}\). All formulas below hold for \(-1<p<1\), and the integrated inequality extends across endpoints by finite energy.

## Exact score identity

Define the conditional signed score current
\[
J(p):=\mathbb E_\nu[\Gamma(p,\log\Omega)\mid p].
\]
Then
\[
\boxed{\quad \kappa(p)\,\partial_p\log r(p)=2J(p),\qquad
\kappa(p)\,\partial_p\log\psi(p)=J(p).\quad}\tag{S1}
\]
Equivalently, for \(p=\cos u\), \(0<u<\pi\),
\[
\boxed{\quad\partial_u\log\psi(\cos u)
=-\frac{4J(\cos u)}{A_f\sin u}.\quad}\tag{S2}
\]
Thus this \(J\) matches the signed current in the radial Ward identity when the earlier \(C_f\) is defined by the same conditional carré-du-champ. No sign conclusion is implied.

## Exact one-face Fisher contraction

Set
\[
I_f:=\int_{-1}^1\kappa(p)\left|\partial_p\log r(p)\right|^2\rho(p)\,dp.
\]
Then
\[
\boxed{\quad I_f
=4\int_{-1}^1\frac{J(p)^2}{\kappa(p)}\rho(p)\,dp
\le4\,\mathbb E_\nu\!\left[
\sum_{e\in\partial f}a_e|\nabla_e\log\Omega|^2\right].\quad}\tag{S3}
\]
This inequality is **local in the electric score energy on the right** and does not contain the full magnetic potential bound \(K=2b\sum c_q\) of the global heat-kernel estimate. It applies to completed cages at any finite coupling. The RHS may still scale badly with the regulator; no independent uniform bound of the required strength is shown.

More generally, for every \(C^1\) real test function \(g(p)\) with finite energy,
\[
\left|\mathbb E_\nu[g'(p)J(p)]\right|
\le \left(\mathbb E_\nu[\kappa(p)(g'(p))^2]\right)^{1/2}
\left(\mathbb E_\nu[T_f]\right)^{1/2},
\quad T_f=\sum_{e\in\partial f}a_e|\nabla_e\log\Omega|^2.
\tag{S4}
\]

## Proof

For a compactly supported smooth test \(\varphi\) on \((-1,1)\), symmetry of the Haar Laplacian and the identity \(\Gamma(\varphi(p),p)=\varphi'(p)\kappa(p)\) yield
\[
\int\varphi'(p)\kappa(p)\rho(p)dp
=-\mathbb E_\nu[\varphi(p)\mathcal L_\mu p]
-2\mathbb E_\nu[\varphi(p)\Gamma(p,\log\Omega)].
\]
Therefore, in distributions,
\[
(\kappa\rho)'=\rho\,\mathcal L_\mu p+2\rho J.
\]
The Haar pushforward satisfies \((\kappa w)'=w\,\mathcal L_\mu p\).
Subtracting after writing \(\rho=rw\) gives \(\kappa r'=2rJ\), proving (S1). Chain rule \(dp/du=-\sin u\) proves (S2).

Conditional Cauchy--Schwarz using \(\Gamma(p)=\kappa(p)\) gives pointwise
\[
|J(p)|^2\le\kappa(p)\,
\mathbb E_\nu[T_f\mid p].
\]
Multiply by \(4\rho(p)/\kappa(p)\), integrate, and obtain (S3). The same Cauchy--Schwarz argument gives (S4). QED.

## Why the signed center-cap gate remains open

The needed positive one-sided current integral
\[
\mathfrak T_f=\frac4{A_f}
\int_0^{\pi/2}\frac{[-J(\cos u)]_+}{\sin u}\,du
\]
equals the positive variation of \(\log\psi\) in the indicated orientation, **without the radial probability weight**. S3, in contrast, is a weighted \(L^2(\rho)\) score estimate. It does not imply a usable unweighted signed variation bound near a rare center cap, because \(\rho\) may be very small. Applying Cauchy--Schwarz across the cap introduces a factor involving \(\int( \kappa\rho)^{-1}dp\), which can diverge or scale sharply even for Haar density. An upper score-energy bound alone therefore cannot close the requested \(o(h^{-1/4})\) estimate.

**Research direction:** combine S1--S3 with a lower bound on the conditional radial density in a suitable collar, a signed comparison or reverse inequality, and the regional energy budget from the existing true-vacuum Agmon/score theorems; prove each uniform constant independently. Neither global heat-kernel positivity nor incomplete-cage Haar independence may be silently applied to completed cages.
