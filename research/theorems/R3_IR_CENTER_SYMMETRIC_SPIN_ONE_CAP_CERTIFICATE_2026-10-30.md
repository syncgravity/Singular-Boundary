# R3-IR-421 — Center-symmetric SU(2) spin-one cap certificate

2026-10-30. Exact finite-volume SU(2) probability inequality, applicable to the physical deleted-target Wilson vacuum with dynamic boundary links. A sufficient criterion, NOT a proof that its Wilson hypothesis holds.

Write the central target holonomy as U with class angle theta in [0,pi], Tr(U)/2=cos(theta). The spin-one character is chi_1(U)=4 cos^2(theta)-1=3-4 sin^2(theta). Let B_a(I)={theta<a}, B_a(-I)={theta>pi-a} with 0<a<pi/2. These two caps are disjoint and are exchanged under U -> -U.

For any center-invariant probability distribution mu on SU(2), mu(B_a(I))=mu(B_a(-I)). Outside their union, sin^2(theta)>=sin^2(a). Since sin^2(theta)>=0 everywhere, Markov's inequality applied to nonnegative 3-chi_1=4sin^2(theta) yields

mu(B_a(I)) = (1/2)mu(B_a(I) union B_a(-I))
 >= (1/2)[1 - (3-E_mu chi_1)/(4 sin^2(a))]_+. (CC-1)

Here [x]_+=max(0,x). This is a rigorous SU(2) one-character *quantitative* certificate, not an assertion that positivity of E chi_1 alone suffices.

At the magnetically deleted target of a genuine original-link Wilson disk with free boundary, R3-IR-420 proves exact center invariance at all retained magnetic couplings, so (CC-1) applies to its actual vacuum distribution. In particular a sufficient condition for the previously targeted Haar-comparable cap survival

mu(B_a(I)) >= (1/2) Haar(B_a(I))

is
3 - <chi_1(W_f)> <=4 sin^2(a)[1 - Haar(B_a(I))].
This is only one convenient sufficient condition (because the lower bound CC-1 is stronger than 1/2 Haar cap in that regime); it is NOT necessary.

The SU(2) normalized class Haar density is (2/pi)sin^2(theta)dtheta; therefore
Haar(B_a(I))=[a - sin(2a)/2]/pi = (2/(3pi))a^3 + O(a^5).
For a~sqrt(h), the certificate requires 3-c_1=O(h) with a sufficiently small coefficient; a mere c_1>=0 or fixed c_1 close to 3 does not suffice uniformly as a ->0.

This refines the scope of R3-IR-419/420: center symmetry plus extremely strong spin-one concentration approaching 3 *at the cap's angular scale* can certify cap survival; generic positivity of spin one, or control of its eighth mixed response without this near-maximal quantitative conclusion, cannot.

No inequality of order 3-c_1 <= const*a² has been proved for the physical completed cage, and (CC-1) is vacuous for generic states where c_1 is O(1) away from 3. Neither a uniform Wilson cap lower bound nor a continuum Yang-Mills mass gap follows.
