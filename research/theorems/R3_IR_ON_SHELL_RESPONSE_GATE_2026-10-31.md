# R3-IR — On-shell nonadiabatic response identity and independent-estimate gate

Date 2026-10-31. Exact finite-volume algebra conditional on the archived smooth positive SU(2) deleted-face Wilson ground state; **not a proof of regulator-uniform control**.

Set \(u=\arccos p_f\), \(A=A_f\), \(s=\partial_u\log\Psi\), and \(M(u)=\mathbb E_{\nu_u}[YV_-]\). The exact fiber equation and angular-transport theorem give, respectively,

\[U-E_0=\frac A4(s'+s^2+2\cot u\,s),\qquad U'=M+R.\]

Differentiating yields the **on-shell full-response identity**

\[\boxed{R(u)=\frac A4\left[s''+2(s+\cot u)s'-2\csc^2u\,s\right]-M(u).}\tag{OS-1}\]

Here \(R=\mathbb E_{\nu_u}[Yk]+2\operatorname{Cov}_{\nu_u}(k+V_-,Y\log\Phi)\), as previously derived. All identities hold at each interior angle, under the finite-volume smoothness assumptions; endpoint extension is interpreted by smooth SU(2) class-coordinate limits. This demonstrates that the combined kinetic-covariance response *exactly reproduces* the radial-score differential operator after subtracting the direct magnetic force. The cancellation is structural but supplies **no independent favorable sign**: bounding \([-R]_+\) by substituting (OS-1) amounts to bounding the unknown score and its derivatives, hence does not close the signed-current proof.

For the concrete smooth positive center-symmetric **engineered scalar radial state**, take \(\Psi_t(u)=Z_t^{-1/2}\exp(t\cos2u)\), \(t>0\), and define its scalar effective potential by the above radial equation. For this mathematical scalar model \(s_t=-2t\sin 2u\) and \(\mathfrak T_t=0\) on \([0,\pi/2]\) while the corresponding derivative \(U_t'\) can take either sign (e.g., \(t=2\)). This is not claimed to arise from an actual original-link magnetic-deleted Wilson Hamiltonian; it demonstrates that signs of effective energy derivatives and separate response terms are not sufficient as *necessary* criteria.

**Numerical algebra audit:** analytic differentiation of \(D_t=U_t-E_0\) compared against centered finite differences for \(t=0.2,0.5,1,2\) on 10,001 interior angles; maximum absolute residual 2.40e-6 at mesh step ~1.54e-4. This numerical check validates differentiation only, not any interacting-vacuum prediction.

**Next physically substantive obligation:** derive an independent one-sided estimate for the *actual combined response* \(R\), or for the radial flux, using the original-link Wilson eigen-equation beyond its scalar conditional projection—for example a new conditional elliptic inequality or a comparison principle for the normalized fiber state that is uniform over completed cages. The local bound \(|M(u)|\le B_f^{inc}\) can be \(O(h^{-2})\), and neither the Casimir/Fisher bound nor (OS-1) yields \(\sup_f\mathfrak T_{f,h}=o(h^{-1/4})\). Connected covariance and continuum Yang–Mills mass gap remain OPEN.