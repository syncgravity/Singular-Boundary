# The Singular Boundary — Cap-scale radial-current and shell-capacity transfer

**Date:** 2026-10-29. **Program:** R3 independent reconstruction. **Classification:** exact inequalities for the *true* finite interacting SU(2) magnetic-deleted vacuum; conditional Penrose-refinement consequences; and an explicit positive SU(2) class-rotor countermodel separating global and scale-local current. **OPEN:** model-specific uniform cap-scale current/shell Fisher estimates in the actual deleted Penrose vacuum, interior magnetic-deletion energy, full fixed-support covariance, physical mass gap, quartic resolvent, and continuum reconstruction.

## I. Exact nonlinear inputs and Haar normalization

On a finite simply connected face-complete rhombus disk with Gauss constraints at all vertices, delete the magnetic term of one interior face f from the SU(2) Wilson Hamiltonian. Let Omega_f^- be its unique normalized strictly positive ground state. The exact nonlinear fiber factorization and conditional-score Ward identity, previously derived without a transverse Born–Oppenheimer projection, give for the target face class angle u=arccos(p_f) in [0,pi]:

  dnu_f^-(u)=omega(u) psi(u)^2 du, omega(u)=(2/pi)sin²u,
  int_0^pi omega psi² = 1, psi(u)=psi(pi-u)>0,
  (log psi)'(u) = -(4/A_f) C_f(cos u)/sin u,

where A_f=sum_(e incident f) a_e and C_f is the actual conditional electric score current. At finite regulator psi is smooth and positive and log psi has finite total variation. Define H(a)=int_0^a omega(u)du=(a-sin(2a)/2)/pi, 0<a<pi/2. The event d_f<=1-cos a is exactly the center cap [0,a].

## II. Theorem CS-1: exact cap-scale one-sided current bound

Define the *truncated outward radial score variation*

  T_a = int_(a/2)^(pi/2) [(log psi)'(u)]_+ du
      = (4/A_f) int_(a/2)^(pi/2) [-C_f(cos u)]_+ / sin u du.

Set H_ring(a)=H(a)-H(a/2), W_out(a)=1/2-H(a). Then **without any inequality for the region u<a/2**, the exact nonlinear deleted-vacuum cap mass m(a)=int_0^a omega psi² obeys

  m(a) >= H_ring(a) e^(-2T_a) / [2(W_out(a)+H_ring(a)e^(-2T_a))].       (CS-1)

In particular, since 0<W_out<=1/2 and 0<H_ring<=1/2,

  m(a) >= (H_ring(a)/2) e^(-2T_a).                                      (CS-2)

**Proof.** For any v in I=[a/2,a] and x in O=[a,pi/2], the fundamental theorem gives log psi(x)-log psi(v)<=T_a. Therefore psi(x)^2<=e^(2T_a)psi(v)^2. Integrating x over O yields (1/2-m(a))<=e^(2T_a)W_out psi(v)^2. Integrating v over I yields H_ring(1/2-m(a))<=e^(2T_a)W_out m_I<=e^(2T_a)W_out m(a). Solve for m(a) to get CS-1. Since W_out+H_ring e^(-2T_a)<=1, CS-2 follows. No spectral gap, Gaussian replacement, monotone effective potential, pointwise vacuum-score bound or global current integral is used. All other physical modes remain inside psi by exact disintegration.

**Refinement.** At b_f~h^-2, the deleted flat-ball cutoff is delta=1/kappa_f=Theta(h), corresponding to a_f=arccos(1-1/kappa_f)=Theta(sqrt h). Thus H_ring(a_f)=Theta(h^(3/2)). From CS-2,

  m_f^-(d_f<=1/kappa_f) >= c h^(3/2) exp[-2 T_(a_f)].                (CS-3)

The previously proved all-bulk exponential trial estimate yields

  Delta_f <= C h^-1 [1+log(1/h)+T_(a_f)].                             (CS-4)

Hence T_(a_f)=O(log(1/h)) suffices for polynomial deleted-vacuum flat-ball mass and Delta_f=O(h^-1 log(1/h)); the still weaker T_(a_f)=o(h^-1/4) suffices for Delta_f=o(h^-5/4) and the previously derived fixed-area extreme-defect and Wilson–angle comparison conclusions. Both inputs on the actual refining Penrose vacuum remain OPEN.

**Strict improvement over the previous proof priority:** the previous global current budget was T_0=int_0^(pi/2)[(log psi)']_+. By construction 0<=T_a<=T_0, and the inequalities do not require any information about the possibly enormous score oscillations inside u<a/2.

## III. Theorem CS-2: two-scale exterior-current plus inner-shell Fisher criterion

An independent variant eliminates positive variation *inside the transition shell* and requires only its local square-root Fisher energy. Put

  T_out(a)=int_a^(pi/2)[(log psi)'(u)]_+ du,
  J_shell(a)=int_(a/2)^a omega(u)|psi'(u)|² du,
  K(a)=int_(a/2)^a omega(u)^(-1) du = (pi/2)[cot(a/2)-cot a].

**Claim.** The true deleted-vacuum cap mass obeys

  m(a) >= min{ H(a)/4,
              H_ring(a)[exp(-T_out(a))/sqrt(2)-sqrt(K(a)J_shell(a))]_+² }.   (CS-5)

In particular, if

  K(a)J_shell(a) <= exp(-2 T_out(a))/8,                                  (CS-6)

then

  m(a) >= [H_ring(a)/8] exp(-2T_out(a)).                                (CS-7)

**Proof.** If m(a)>=H(a)/4, CS-5 is immediate. Otherwise H(a)<=1/2 implies m(a)<1/8. By center symmetry the half-interval exterior mass is 1/2-m(a)>=3/8. For all x>=a, psi(x)<=e^(T_out)psi(a), hence psi(a)^2 >= (3/8)e^(-2T_out)/W_out >= (3/4)e^(-2T_out). We use the weaker psi(a)>=e^(-T_out)/sqrt(2). For u in [a/2,a], Cauchy–Schwarz gives psi(u)>=psi(a)-sqrt(J_shell K). Integrate the squared positive lower bound over the shell, which is a subset of the cap. Under CS-6, the bracket in CS-5 is at least e^(-T_out)/(2sqrt2), yielding CS-7. Finally H(a)/4 >= H_ring(a)e^(-2T_out)/8, so the same conclusion holds in the first case. No conditioning on a point of zero Haar capacity is performed: all Cauchy–Schwarz comparisons occur on an annulus at strictly positive radius.

As a->0, K(a)~pi/(2a), H_ring(a)~[7/(12pi)]a³ (since H(a)~2a³/(3pi)). Thus CS-6 asks only

  J_shell(a) <= c a exp(-2T_out(a)),                                    (CS-8)

with a concrete c from the exact K(a). This local Fisher estimate is *not implied* by the presently available global electric energy; it is a clearly separated new dynamical input. One sufficient pair for the Penrose objective is T_out(a_h)=o(h^-1/4) and K(a_h)J_shell(a_h)<=exp[-2T_out(a_h)]/8. These conditions are **not** proved in the nonlinear Penrose vacuum.

## IV. Theorem CS-3: global signed-current budget can diverge although cap mass is Haar and radial Fisher tends to zero

Let n>=4 be an integer, choose cap radius a_n=n^(-1/2), tiny radius eps_n=n^(-6), frequency N_n=n², amplitude c=1/5. Fix a smooth bump eta:[0,infinity)->[0,1], supported in (1/4,1/2) and identically 1 on [1/3,5/12]. For 0<=u<=pi/2 set

  q_n(u)=c eta(u/eps_n) sin(2pi N_n u/eps_n),
  psi_n(u)=Z_n^(-1/2)(1+q_n(u)),

extend psi_n by center symmetry psi_n(pi-u)=psi_n(u), and choose Z_n so that int omega psi_n²=1. The support is away from both group center points, making psi_n a smooth, strictly positive SU(2) class function. Define a smooth SU(2) rotor potential

  V_n(u)=k (psi_n''+2cot(u)psi_n')/psi_n + c_n,

where c_n makes V_n nonnegative. Then H_n=-k(partial_u²+2cot u partial_u)+V_n has psi_n as its exact unique normalized positive ground state, by the ground-state transform. This comparator is **not** the full nonlinear magnetic-deleted Penrose Hamiltonian.

Since eps_n<<a_n/2, T_(a_n)=0 **exactly** and T_out(a_n)=J_shell(a_n)=0. Meanwhile on the plateau the sine has at least floor(N_n/12)-1 complete cycles; each contributes positive log variation log[(1+c)/(1-c)]. Therefore

  T_0(psi_n) >= (floor(N_n/12)-1) log[(1+c)/(1-c)] = Omega(n²).

Its full radial Fisher energy satisfies

  J_n=int_0^pi omega|psi_n'|² <= C N_n² eps_n = O(n^-2)->0.

The pointwise ratio (1-c)²/Z_n <=psi_n²<=(1+c)²/Z_n is coarse, but the perturbation occupies angular volume O(eps_n³) entirely *inside* the center cap. Consequently Z_n=1+O(eps_n³), m_n(a_n)=H(a_n)+O(eps_n³), and

  m_n(a_n)/H(a_n)=1+O((eps_n/a_n)^3)=1+O(n^(-33/2)).

This exact countermodel proves that T_0=o(h^-1/4) is **not necessary** for the center-ball conclusion, even if J_n->0 and the state is a smooth strictly positive quantum ground state. The cap-scale criterion CS-1 correctly discards microscopic oscillations deep inside the cap.

## V. Interpretation, limits and next obligation

**New theorem:** CS-1 and CS-2 are exact consequences of the actual nonlinear deleted-vacuum marginal and its SU(2) center symmetry. They are compatible with slow collective modes and require no Born–Oppenheimer gap. CS-3 is an explicit independently solvable SU(2) rotor showing a strict improvement in the *sufficient criteria*.

**Still OPEN:** a uniform bound T_(a_f)=o(h^-1/4) in the true refining Penrose deleted vacuum, or the exterior-current/local-shell-Fisher pair CS-6; all-bulk deletion at O(h^-1 polylog), fixed-support connected Wilson–angle covariance, physical mass gap, nonlinear quartic resolvent and continuum reconstruction. The theorem neither constructs a continuum field nor asserts the desired small-ball property of the actual deleted vacuum. Do not promote surrogate lattices or comparator states to interacting Penrose evidence.
