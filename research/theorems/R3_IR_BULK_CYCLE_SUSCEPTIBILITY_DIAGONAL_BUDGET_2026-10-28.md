# The Singular Boundary — Bulk cycle susceptibility: exact sum-rule bound and Gaussian submodularity

**Research date:** 2026-10-28. **Audit scope:** finite true nonlinear SU(2) Wilson Hamiltonians and, separately, the exact shared-edge Gaussian tangent Hamiltonian. **Evidence status:** CS-1 exact finite physical-sector nonlinear statement; CS-2 exact arbitrary-size Gaussian theorem; CS-3 exact finite two-level mathematical counterexample to inference from center parity/concavity alone. **Open:** the sign/size of SU(2) nonlinear connected mixed susceptibility at strong cycle-closing magnetic couplings, uniform bulk deletion energy, extreme-defect exclusion for all interior Penrose faces, full mass gap, nonlinear quartic resolvent, continuum construction. No Monte Carlo, no original research binaries modified.

## 1. SU(2) Wilson coupling rectangle and exact Hessian

Let H(u,t)=H_0-b_fd_f+t d_f+uW, 0<=t<=b_f=b, 0<=u<=1, where H_0 contains the target face f plus a bridge-compatible subset of the other magnetic faces, and W=sum_{g in cycle-closing B} b_g d_g >=0. The target face magnetic term is absent at t=0 and fully restored at t=b. Electric H_E=sum_e a_e(-Delta_e), fundamental Casimir 3/4, d_g=1-p_g in [0,2]. Every finite H(u,t) has a unique strictly positive physical vacuum Omega, even at the rectangle endpoints. Its ground energy E(u,t) is analytic locally in these real couplings. Define Q=I-|Omega><Omega|, K=H-E, G=QK^-1Q on the physical sector, and the reduced-resolvent form

  chi_{XY}(u,t)=Re <QX Omega,G QY Omega>.

Hellmann-Feynman/Kato derivatives give

  E_tt=-2 chi_dd <=0,   E_uu=-2 chi_WW <=0,
  E_ut=-2 chi_dW.

The Hessian matrix -D²E is PSD, since G is positive, so

  (E_ut)^2 <= (-E_tt)(-E_uu)            (CS-1a)

at every interior coupling. The target-face center-flux transformation of the previously proved BC theorem commutes with H(u,0) and reverses p_f for any u, hence <p_f>_{u,0}=0 and E_t(u,0)=<d_f>_{u,0}=1. The t-response is decreasing by concavity and, by the same center symmetry, <p_f>_{u,t}>=0 for t>=0. This is an exact nonlinear statement; it says nothing about the *cross* susceptibility chi_dW.

## 2. Integrated diagonal susceptibility budget — theorem CS-1

Define the nonnegative diagonal-response budgets

  A=integral_0^1 du integral_0^b dt [-E_tt(u,t)]
    =integral_0^1 du [<d_f>_{u,0}-<d_f>_{u,b}]
    =integral_0^1 du <p_f>_{u,b},

  B=integral_0^b dt integral_0^1 du [-E_uu(u,t)]
    =integral_0^b dt [<W>_{0,t}-<W>_{1,t}].

The exact center-flux sign and bounded trace give 0<=A<=1. Since W>=0 and W<=2 B_sum I with B_sum=sum_{g in B}b_g, 0<=B<=2b B_sum. This holds without an assumed physical gap, Gaussian approximation or sign of mixed response.

Integrate CS-1a and apply Cauchy-Schwarz on the coupling rectangle:

  |Delta_f(1)-Delta_f(0)|
    = |integral_0^1 du integral_0^b dt E_ut|
    <= integral sqrt[(-E_tt)(-E_uu)]
    <= sqrt(A B) <=sqrt(B) <=sqrt(2b B_sum).       (CS-1b)

Here Delta_f(u)=E(u,b)-E(u,0), and from the independently proved nonlinear dual-bridge theorem Delta_f(0)<=3 sqrt(A_f b)/(2 sqrt2). Therefore

  **Delta_f(1)<=3 sqrt(A_f b)/(2 sqrt2)+sqrt(B).**  (CS-1)

The B quantity is a *diagonal* cycle-closing response, involving only expectation differences of W at u=0 and u=1, with no inverse resolvent shown. An independent bound B=O(h^-2 polylog(1/h)^2) at b~h^-2 would imply the sought bulk deletion O(h^-1 polylog(1/h)). But B<=2b B_sum is O(h^-4) when at least one cycle-closing face has b_g~h^-2, and CS-1 alone does NOT close the original h^-5/4 gate. Unlike the earlier negative-part budget N_f, B controls absolute integrated mixed susceptibility, and may be too large even when the signed mixed susceptibility is favorable. This distinction is essential.

The identical theorem is valid for any finite Hermitian Hamiltonian linear in t,u with a nondegenerate ground state, provided the center symmetry gives E_t(u,0)=1 and p_f<=1; the SU(2) content is that the required center transformation is exact for every deleted bulk face.

## 3. Exact Gaussian all-coupling submodularity — theorem CS-2

For the *separate* harmonic (gauge-reduced tangent) model on any complete disk, let M=B_link diag(a_e) B_link^T>0, A_mat=M^(1/2) diag(b_f) M^(1/2), and

  E_G(b)= (3/(2 sqrt2)) Tr sqrt(A_mat).

For b_f>0 all faces, let v_f=M^(1/2)e_f and R_z=(A_mat+z I)^-1. Matrix functional calculus gives

  partial_{b_f} E_G=(3/(4 sqrt2)) v_f^T A_mat^(-1/2) v_f,
  **partial_{b_g} partial_{b_f} E_G
    =-(3/(4 sqrt2 pi)) integral_0^infty z^(-1/2)
                [v_f^T R_z v_g]^2 dz <=0.**           (CS-2)

This holds for f=g as well, and for all sizes and inhomogeneous electric/magnetic coefficients, not requiring a square-root of a 2x2 matrix. For a cycle-closing parameter u multiplying any sum W_G=sum_{g in B} b_g |y_g|^2/8 with b_g>=0, the mixed derivative E_{u,t}^G is a sum of nonpositive terms. Thus the *Gaussian* diagonal face response decreases when cycle-closing magnetic terms are restored, N_f^G=0, and

  **Delta_f^G(1)<=Delta_f^G(0)<=3 sqrt(A_f b)/(2 sqrt2).** (CS-3)

For couplings with zero entries, regularize b by eps>0 and take eps down to zero using continuity of Tr sqrt. The derivative formula is applied only on the strictly positive interior; the integrated submodularity persists at endpoints.

Proof of the integral identity: A_mat^(-1/2)=(1/pi) integral_0^infty z^(-1/2)(A_mat+z I)^(-1) dz. Differentiate the derivative partial_f E_G and use dR_z/db_g=-R_z v_g v_g^T R_z; its quadratic form gives the perfect square. This sign is an exact property of the Gaussian quadratic operator, NOT a physical SU(2) mixed-susceptibility bound.

## 4. A sharp obstruction to inferring that sign from center parity and positivity — theorem CS-3

Let sigma_x,sigma_z be Pauli matrices and g>0, t>0, u>=0. On C² set

  H_toy(u,t)=(g+u)(I-sigma_x)+t(I-sigma_z).

Both nonconstant operators multiplying u,t are positive semidefinite with norm 2, H_toy has a unique strictly positive ground state in the sigma_z basis, and T=sigma_x commutes with H_toy(u,0) while T sigma_z T=-sigma_z. Thus the model has the exact abstract analogue of the deleted SU(2) center-flux parity and the one-face positive response. Nevertheless,

  E_toy(u,t)=g+u+t-sqrt((g+u)^2+t^2),
  **partial_u partial_t E_toy = t(g+u)/[(g+u)^2+t^2]^(3/2)>0,**
  **chi_{dW}=-(1/2) E_ut<0,**
  **partial_u Delta_f(u)>0** for b=t>0.

The mixed sign is precisely opposite to Gaussian submodularity, even though the ground energy is separately concave, the Hamiltonian terms are positive and center-odd/center-even, and the vacuum is unique and positive. If the physical cycle-closing term is taken as u b(I-sigma_x) with u in [0,1], equivalently evaluate the expression above at original u=b, then at t=b and fixed g the complete deletion increment scales as (2-sqrt2)b, whereas at original u=0 it stays O(1). The construction is NOT a lattice SU(2) counterexample. It rigorously shows why parity, positive semigroup and general concavity alone cannot prove the desired SU(2) ferromagnetic sign; additional nonabelian representation geometry or a directly verified correlation inequality is necessary.

## 5. Exact nonlinear vs Gaussian proof obligations

The actual SU(2) bulk theorem would follow from a sufficient sign condition chi_{d_f,W}(u,t)>=0 throughout the coupling rectangle: then E_ut<=0, Delta_f(1)<=Delta_f(0), and the previously proved dual-bridge sqrt(A_f b_f) bound transfers to all cycle-rich faces. This sign condition is **UNPROVED** and may fail; CS-3 shows it cannot be justified from abstract inputs alone.

Alternatively the exact CS-1 bound reduces the problem to controlling the **diagonal** magnetic cycle-response budget B, ideally B=O(h^-2 polylog²), rather than the negative cross-resolvent susceptibility N_f. This is a sufficient criterion, NOT a result at physical coupling. Its rough universal bound B<=2b B_sum remains too large at b_g~h^-2. A narrower, energy-resolved nonlinear mixed-response bound may prove more realistic than either blanket sign or full B control.

Proved here: the finite SU(2) two-parameter positive-resolvent Gram inequality, the exact center-flux diagonal susceptibility sum rule 0<=A<=1, the integrated cycle comparison, and all-coupling/full-volume Gaussian submodularity with perfect-square resolvent integrand; the toy sign counterexample. Still OPEN: SU(2) strong-field cross sign, improvement of B, uniform bulk deletion, true Penrose extreme-defect probability, continuum gap and quartic resolvent. Q14/Stage26 temporal provenance still unverified.