# Exact physical reduced-resolvent derivative for cap-biased Wilson transport

**2026-10-30. Status:** exact finite-volume SU(2) Wilson ground-state identity and a quantitative (generally inadequate) estimate. Neither a favorable sign nor a regulator-uniform cap lower bound is established. This derives a zero-temperature counterpart of the archived cap-biased Euclidean transport, with a diagnostic of its small-cap normalization.

## Setup and prior source

Use the genuine four-neighbor magnetic-deleted target Hamiltonian and positive cap observable from R3_IR_CAP_BIASED_EUCLIDEAN_LOG_TRANSPORT_2026-10-30.md:
\[
H(t)=H_{\rm rest}+\sum_{i=1}^4t_i b_i(1-p_i),\quad
O=k_a(W_f),\quad 0\le O\le\nu_a.
\]
Work throughout in the **full physical Gauss-invariant Hilbert space**. The unique positive normalized ground state is \(\Omega_t\), ground energy \(E_t\), and \(F_a(t)=\langle\Omega_t,O\Omega_t\rangle>0\). Set \(Q_t=1-|\Omega_t\rangle\langle\Omega_t|\), \(K_t=H(t)-E_t\), and
\[
R_t=(Q_tK_tQ_t)^{-1}\text{ on ran }Q_t,
\]
extended by zero on the ground state. This exists at every **fixed finite lattice**, where the physical gap \(\delta_t>0\). Let \(v_O=Q_t O\Omega_t\) and \(v_i=Q_t p_i\Omega_t\).

## Theorem (CR-1): exact real-time signed response

In the real positive ground-state gauge, analytic differentiation of the eigenvalue equation yields
\[
\boxed{\quad
\partial_{t_i}\Omega_t=b_i R_t v_i,\qquad
\partial_{t_i}F_a(t)=2b_i\langle v_O,R_t v_i\rangle.
\quad}\tag{CR-1}
\]
Thus
\[
\boxed{\quad
\partial_{t_i}\log F_a(t)=\frac{2b_i}{F_a(t)}
\langle v_O,R_t v_i\rangle.
\quad}\tag{CR-2}
\]
For a piecewise differentiable coupling path \(t(\lambda)\),
\[
\boxed{\quad
\log\frac{F_a(t(1))}{F_a(t(0))}
=\int_0^1\sum_i\dot t_i(\lambda)
\frac{2b_i}{F_a(t(\lambda))}
\langle v_O,R_t v_i\rangle\,d\lambda.
\quad}\tag{CR-3}
\]
The identity is exact in the physical interacting Wilson model and agrees with the zero-temperature limit of the earlier cap-biased Euclidean transport. It **does not** assert a sign for the mixed reduced-resolvent matrix element.

**Proof.** Differentiate \((H-E)\Omega=0\), project onto ran \(Q\), and use \(H_i'=b_i(1-p_i)\). With \(\langle\Omega,\partial_i\Omega\rangle=0\), obtain \(K\partial_i\Omega=-QH_i'\Omega=b_iQp_i\Omega\). Apply \(R\). Differentiate the ground-state expectation of fixed self-adjoint \(O\), and center \(O\) since \(R\Omega=0\). Divide by positive \(F_a\), then integrate the chain rule. QED.

## Theorem (CR-2): source-specific susceptibility bound and why it fails

Since \(R_t\) is positive on the physical orthogonal complement, its quadratic form obeys Cauchy--Schwarz:
\[
|\partial_{t_i}\log F_a|
\le\frac{2b_i}{F_a}
\sqrt{\langle v_O,R_tv_O\rangle
\langle v_i,R_tv_i\rangle}.
\tag{CR-4}
\]
As \(R_t\le\delta_t^{-1}Q_t\), and \(0\le O\le\nu_a\) implies \(O^2\le\nu_a O\), one further obtains
\[
\boxed{\quad
|\partial_{t_i}\log F_a(t)|
\le\frac{2b_i}{\delta_t}
\sqrt{\left(\frac{\nu_a}{F_a(t)}-1\right)
\,\mathrm{Var}_{\Omega_t^2}(p_i)}.
\quad}\tag{CR-5}
\]
The exact source-specific susceptibility form (CR-4) may be sharper if low-energy components of either \(O\Omega_t\) or \(p_i\Omega_t\) are suppressed. CR-5 explicitly displays the adverse **rare-cap factor** \(\sqrt{\nu_a/F_a}\), as well as \(1/\delta_t\). Thus this absolute-value gap-dependent inequality does not supply the uniform lower bound on the signed transport required for cap survival.

## Exact sign-sensitive gate

Define the signed physical susceptibility
\[
\mathcal S_{a,i}(t)=\langle Q_tO\Omega_t,R_tQ_tp_i\Omega_t\rangle.
\]
For diagonal completion \(t_i(\lambda)=\lambda\), the missing condition for a half-Haar baseline is exactly
\[
\boxed{\quad
\int_0^1\sum_{i=1}^4\frac{2b_i\,\mathcal S_{a,i}(\lambda\mathbf1)}
{F_a(\lambda\mathbf1)}\,d\lambda\ge-\log2.
\quad}\tag{CR-6}
\]
This is not claimed true. It identifies that **cross-source signed resolvent overlap**, rather than either diagonal susceptibility or the eighth-derivative absolute value, is the dynamical object to estimate. Positivity of \(R_t\) does not force a sign for the off-diagonal quadratic form \(\mathcal S_{a,i}\).

## Scope and dependency discipline

CR-1--CR-5 are consequences of finite-volume nondegenerate perturbation theory and the actual physical Hamiltonian. The half-Haar criterion CR-6 is conditional. The pre-existing R3_IR_PHYSICAL_SOURCE_RESPONSE_SPECTRAL_TRICHOTOMY_2026-10-28.md treats diagonal source susceptibilities and does not prove the missing off-diagonal sign. None of these statements yields the desired uniform current, source spectral gate, continuum field construction or mass gap.
