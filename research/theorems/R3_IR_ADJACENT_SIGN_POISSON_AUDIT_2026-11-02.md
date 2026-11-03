# The Singular Boundary — Adjacent-face sign and Poisson audit (2026-11-02)

## Scope and provenance
This audit continues the November 1 three-face quadratic-operator review. It uses the published exact reduced-chain identities, rather than asserting that a previously published full score recursion has been independently inspected. The original earlier two-face and three-face coefficient tables were not present in the available November 1 summary.

Put a=Re A, b=Re B, and r=Re(AB) for adjacent face holonomies, with the positive electric operator K satisfying

- K(a)=3a and K(b)=3b;
- K(ab)=(11/2)ab+(1/2)r;
- K(r)=(15/2)r;
- K(fg)=fKg+gKf-2Gamma(f,g).

Therefore Gamma(a,b)=(ab-r)/4. This fixes the direction of the earlier sign inconsistency.

## Exact Poisson inversion

The Haar-centered source Gamma(a,b)=(ab-r)/4 has unique centered solution within span{ab,r}:

X=(1/22)ab-(2/55)r.

Direct substitution: KX=(1/4)ab + ((1/44)-(3/11))r=(ab-r)/4.

The opposite-sign expression -X solves K(-X)=-Gamma(a,b), not the corrected equation.

## Implication for a second-order logarithmic-score recurrence

Under the explicit convention H=K+lambda V and Omega=exp(-S), for K=-div grad, the transformed ground-state equation is

K S + Gamma(S,S) = lambda V - E(lambda)

(the sign of the quadratic term follows by evaluating K exp(-S)/exp(-S) = -KS - Gamma(S,S) with the positive-Laplacian convention). More generally, if a chosen source recurrence has the form K S2 = c Gamma(a,b), its adjacent term is c X. In particular K S2 = 2q^2 Gamma(a,b) gives

S2,adj = q^2 [(1/11)ab-(4/55)r].

**Important:** the sign of S2,adj in the physical score cannot be stated until the score variable, potential convention and the complete recurrence are inspected. For the displayed Omega=exp(-S) and H=K+lambda V convention, the quadratic cross source in KS2 is **-2 Gamma(S1A,S1B)**, not +2, and the corresponding cross contribution is -2q² X. This audit reports both source-sign possibilities to avoid silently assigning a sign to an unpublished recurrence.

## Verification and limitations

A SymPy checker asserts K(X)=Gamma, K(2X)=2Gamma, and shows that -X fails K(X)=Gamma. It does not independently reconstruct the original-link quaternion derivative operator or verify the unavailable historical coefficient table. The complete quartic basis, three-face fourth-order inversion, analytic all-orders majorant, interacting gap and continuum Yang–Mills gap remain open.

## Next target

Retrieve the original two-face and three-face score recursion definitions and coefficient tables, inspect the exact score/Schrodinger convention, and substitute each reported coefficient directly into its Poisson equation. Once reconciled, construct the closed quartic invariant basis and invert the connected three-face fourth-order source.