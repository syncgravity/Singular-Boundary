# PF-I16 — Exact one-link Haar marginal, interacting conditional Fisher/entropy bound, and mixing gate

**2026-11-08.** Source model: original PF-I11/PF-I15 finite accepted five-direction rhombus complexes. No cubic substitution. Full research report, executable one-rhombus verifier, logs, and hash manifest: Library `/The Singular Boundary/Proof Audits/PF_I16_CONDITIONAL_INFORMATION_2026_11_08.zip`. These are finite auxiliary Hamiltonian results; continuum Yang–Mills mass gap remains **OPEN**.

Let `H_G=sum_e a_e(-Delta_e)+sum_f b_f(1-Tr U_f/2)` on the finite SU(2) Gauss-invariant original-link space, `a_e>0,b_f>=0`, with strictly positive normalized ground state `Omega`, `dnu=Omega^2 dmu`. As established in PF-I16, `T_e=int |grad_e Omega|^2 dmu <= (2/a_e) sum_{f:e in boundary f}b_f`. An elementary source edge belongs to at most eight elementary five-direction rhombi.

**Exact Haar one-link marginal.** Invariance under the independent local SU(2) vertex gauge transformations, followed by integration over the other original links, forces `(pi_e)_*nu = Haar_SU2` for each edge e. This **does not** imply link independence.

**Exact conditional score / Fisher information.** Let `Y=U_{E\{e}}`, `m_e(Y)=int Omega(u,Y)^2du`, `rho_e(u|Y)=Omega(u,Y)^2/m_e(Y)`. Then `s_e=grad_u log rho_e=2grad_e log Omega` and
```math
E_nu |s_e|^2 =4T_e <= (8/a_e) sum_{f:e in boundary f} b_f <=64b_0/a_0
```
when `a_e>=a_0,b_f<=b_0`.

**New conditional information estimate.** SU(2) in the electric Casimir normalization `C_e chi_(1/2)=3/4 chi_(1/2)` is the round three-sphere of radius 2 (Ricci =1/2). Its Bakry–Émery log-Sobolev inequality is `Ent_Haar(phi^2)<=4 int|grad phi|^2` for `int phi^2=1`. Apply conditionally to `Omega(u,Y)/sqrt(m_e(Y))` and integrate in Y:
```math
I_nu(U_e;U_{-e})
=D_KL(nu || Haar_e tensor nu_{-e})
=E_Y D_KL(rho_e(.|Y) || Haar_e)
<=4T_e <=(8/a_e)sum_{f:e in boundary f}b_f <=64b_0/a_0.
```
Pinsker:
```math
||nu-Haar_e tensor nu_{-e}||_TV <=sqrt(2T_e)
<=sqrt((4/a_e)sum_{f:e in boundary f}b_f) <=sqrt(32 b_0/a_0).
```
These are *averaged* conditional-information statements in fixed original-link coordinates; they do not imply pointwise Dobrushin coefficients, a uniform conditional Poincare inequality, or approximate tensorization of the variance.

**Isolated authentic rhombus calibration.** For a four-link source rhombus with vacuum density `rho(U_f)` depending only on the class of the loop product, integrating any one link leaves all three other links independent Haar. Its one-versus-rest information is exactly `int rho log rho dHaar`. The Python character-Jacobi verifier (70 SU(2) characters, 1200-point angular quadrature) checked 7 magnetic couplings b = 0, 0.01, 0.1, 0.71, 1, 4, 16, and the log-Sobolev, Pinsker, and PF-I16 local variational inequalities. For b=.71: `T_e=0.0102353225`, `I_e=0.0271908835`, `TV=0.0988822952`. Computation verifies this one-rhombus calibration, not the full many-rhombus theorem.

**Next gate.** A uniform interacting gap would follow if *both* volume-uniform conditional variance tensorization and uniform one-fiber Poincare constants were established for the actual coupled Wilson vacua. Neither follows from the Fisher/information bound above. PF-I16's smooth positive non-Wilson countermodel has uniformly bounded local Fisher information but vanishing gap, showing why the implication cannot be assumed. Original J/observer time selection, physical energy scale, refining continuum, OS reconstruction, and physical Yang–Mills gap remain open.

No canonical claim gate changed; historical source graphs and archives untouched.