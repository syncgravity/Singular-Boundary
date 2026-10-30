# Exact shared-edge spin-one obstruction to pointwise cap-biased cosh ordering

Date: 2026-10-30. R3-IR-406. Exact SU(2) Haar calculation in genuine original-link Wilson face geometry. It refutes a proposed **pointwise conditional stochastic-ordering shortcut**, NOT the averaged physical Wilson cap comparison.

## Face geometry and source

On a finite rhombus disk take a target face f and neighboring face g sharing a link x. With suitable based orientations, write W_f=x L and W_g=x^{-1} M, where L,M are SU(2) products of the other original links. At zero neighbor magnetic coupling, conditional on the environment y the positive physical ground state of the original-link Hamiltonian is uniform Haar in the magnetically private x; this is the exact archived private-link factorization.

Let p(U)=Tr_f(U)/2. Let the nonnegative central target-cap multiplier be k(W), with a0=int k(W)dW>0 and a1=int k(W)chi_1(W)dW. Here chi_1=4p^2-1 is the SU(2) integer spin-one character. For a sufficiently small identity-centered cap a1>0. Define the cap-biased conditional Haar average
E_k[F(x) | L,M] = [int k(xL) F(x)d x]/a0.
The unconditioned private-link Haar average is E_Haar.

## Theorem (SO-1): exact squared-neighbor contrast

For the fixed environmental holonomies L,M, let A=LM. Then

E_Haar[p(W_g)^2]=1/4,

E_k[p(W_g)^2 | L,M] = 1/4 + [a1/(12 a0)] chi_1(A),

so

boxed: E_k[p_g^2 | L,M] - E_Haar[p_g^2] = [a1/(12 a0)] chi_1(LM).  (SO-1)

Proof. The fundamental fusion rule is p(U)^2=(1+chi_1(U))/4. Substitute W=xL, so x^{-1}M=L W^{-1}M, and cyclicity gives chi_1(x^{-1}M)=chi_1(W^{-1}ML). Schur orthogonality for central k gives int k(W) chi_1(W^{-1}A)dW = (a1/3) chi_1(A). Since chi_1 is a class function, trace cyclicity permits A=LM or ML. Divide by a0 and by four. QED.

For A=I, chi_1(A)=3, so cap bias INCREASES the conditional second moment by a1/(4a0)>0.
For an SU(2) element A with p(A)=0 (trace zero), chi_1(A)=-1, and the same difference is -a1/(12a0)<0.

Both A=I and trace-zero A are allowed original-link environment configurations. Because the remaining link holonomies are genuine SU(2) variables, they occur in neighborhoods of positive Haar measure. Thus even with a genuinely positive identity-centered SU(2) cap observable, the **conditional** second-moment contrast has either sign.

## Local short-window cosh consequence

For a stationary private-link Brownian process with environment held at a chosen deterministic constant configuration (this frozen environment is a conditional test model, not the genuine interacting ground-state path distribution), set X_T=b int_0^T p(x_s^{-1}M) ds. The heat diffusion is continuous, so as T goes to zero, X_T/(bT) converges in L² to p(x_0^{-1}M). The cap-biased and ordinary reference expectations of cosh X_T therefore satisfy

E_k[cosh X_T]-E_Haar[cosh X_T]
= (b² T²/2) [a1/(12a0)] chi_1(A) + o(T²).

Consequently short-window conditional cosh ordering is REVERSED at trace-zero A, and favorable at identity A. This is a specific original-link Wilson geometry counterexample to any attempted proof by conditioning on environmental holonomies and asserting nonnegative cap-biased moment contrast for every configuration. It is NOT a counterexample to physical full-beta, full-coupling Gauss-projected Wilson cap survival; the actual environment must be integrated with the physical positive vacuum and gauge-seam weights.

## Analytical implication

The actual physical averaged comparison must exploit cancellation or suppression of unfavorable relative holonomy sectors. Neither centrality and nonnegativity of k nor positivity of the fundamental Wilson plaquette weight yields a pointwise lower ordering in the environment. The missing dynamical estimate may be recast as a bound on the genuine environment distribution of chi_1(LM) and its time-propagated generalization, which remains OPEN.

No physical full-coupling cap estimate, Penrose-uniform bound or Yang-Mills mass gap follows from this calculation.
