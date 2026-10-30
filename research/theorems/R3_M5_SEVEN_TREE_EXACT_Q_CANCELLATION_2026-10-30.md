# Exact 127-subset M5 seven-face tree electric regression and squarefree Q cancellation
Date: 2026-10-30. Status: complete exact rational algebra for truncated seven-active-face Hamiltonian. No all-orders Haar or physical mass gap claim.

Periodic M5 face indices S=(1,2,3,4,7,8,10). Their six primal shared edges: (1,3):3, (1,8):14, (2,3):2, (2,4):5, (7,8):8, (7,10):12. Graph is a tree. All link electric coefficients are a_e=1; physical SU2 Casimir j(j+1).

For each subset J of active faces, use basis vectors O_P=product over blocks B of P of half traces around the oriented simple boundary of the connected union B. Here P ranges over all partitions of J into blocks connected in the induced tree. Every boundary of a connected tree union has length 2|B|+2. All blocks contain only retained elementary faces.

Exact electric Fierz action: T O_P = d(P) O_P - (1/2) sum_{edges (g,k) crossing distinct blocks of P} O_(P with g/k blocks merged). The diagonal d(P)=(3/4)sum_B(2|B|+2) + (1/2)*number_of_crossing_edges. The formula includes all cross derivatives because distinct tree blocks share at most one primal edge per graph edge. Joining two blocks gives another connected retained-face union.

Define F_empty=1, F_J=R sum_(g in J) p_g F_(J minus g), R=(T on constants orthogonal)^-1. The subspace of retained connected-block Wilson products is T invariant and positive on all nonempty subsets; inversion can be performed by upper triangular rational elimination ordered by decreasing block count. Enumerating all 127 nonempty subsets and verifying each exact residual T F_J =sum_g p_g F_(J minus g) succeeds with Fraction arithmetic. Final seven-face basis contains 64 partitions, one for each selection of cuts of six tree edges. Final singleton-block coefficient is 58886977/206090632800; final fully joined block coefficient is 13607484139435318199/2995402808330596135600128000. All 64 coefficients are positive rationals.

In the deleted face conditional Haar coordinates, each O_P depends exclusively on retained plaquette holonomies (and their rooted transports), so Q_f O_P=0. Therefore Q_f F_S=0 exactly, and the parity-compatible probe O=(p_f²-1/4)prod_(g in S)p_g has exact overlap <O,F_S>=0. This supersedes the previous status 'amplitude not evaluated': seventh-order SQUAREFREE coefficient is evaluated and is zero. This result does NOT prove Q_f Omega=0 at arbitrary coupling, nor rule out repeated plaquette insertions and contributions from other active faces, and does not extend without proof to open Penrose disks. The continuum mass gap remains OPEN.

Executable exact-recurrence validator is in research/scripts/validate_m5_seven_tree_exact.py.
