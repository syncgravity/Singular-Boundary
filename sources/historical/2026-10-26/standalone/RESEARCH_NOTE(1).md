# R3 Penrose prism: incidence, partition-function, and frustration audit
28 October 2026. **Source-grounded scope:** the supplied `penrose_complete_catalogue.npz` holds 22,808 path records, 68,424 cycle records, `F=22808`, and graph hash `f67fc4455b37bf18f16c0a5ae90c7c3c5ccd49ca8b739fa1f5e43562b4581c21`. It is **not** an oriented vertex–edge–face cell complex; its `cidx` refers to indexed cycle/path data without the underlying edge endpoint map. Sample Stage 26 checkpoints contain observation arrays and source/catalogue hashes, not the missing face incidences. The dissertation tar archive contains PDFs, not a machine-readable R3 prism specification. Therefore we cannot honestly reconstruct *the original* Penrose prism or claim Penrose-specific frustration from these files.

## Relative partition functions
For normalized Wilson factors `w_lambda(H)=exp[-lambda(1 - tr(H)/2)]`, and a cavity action on the full integrated-link space, the exact identity is

`Z_C+Q / Z_C = E_C exp[-lambda D_Q]`, `D_Q=sum_{p in Q}(1-tr(H_p)/2)`.

For the near-flat event `A_t={D_Q <= t|Q|/lambda}`:

`Z_C+Q/Z_C >= exp(-t|Q|) P_C(A_t)`.

This is exact for all correlated Gibbs cavity measures. It reduces the desired polynomial/logarithmic comparison to a probability bound, **which is not presently proved for the Penrose prism**. If a cavity+Q family admits a local finite-to-one change of variables mapping a set of large Gibbs mass into `A_t`, then a valid proof must bound the Jacobian, action change, number of preimages, and exterior conditional mass. No such map is asserted here.

## Explicit geometry generator
`generate_r3_incidence.py` takes a user-supplied oriented *spatial cell complex* (vertices, directed edges, and cyclic oriented face words) and extrudes it over 3 temporal intervals / 4 time slices. Spatial faces `p:t:face` and temporal faces `r:t:edge` are written explicitly. The temporal face boundary for directed edge `u->v` is `s:t:e, t:t:v, -(s:t+1:e), -(t:t:u)`.

Boundary policy and insertion `q` **must be supplied explicitly**. No attempt is made to infer them from spectroscopy catalogues. The output includes each oriented face word, cavity Q partition, integrated/fixed edges, cavity degree, strict exclusive-edge test, and a mod-2 **central sector** consistency test. The central test asks whether all cavity faces can have central holonomy +I while all Q faces have -I, assuming fixed edges +I. Inconsistency is a genuine *discrete* obstruction for that imposed target; consistency is **not** evidence of a near-flat Gibbs event or sufficient condition for a logarithmic theorem. It does not test arbitrary noncentral SU(2) boundary holonomy, and cannot establish a positive frustration energy without continuous minimization.

The bundled one-spatial-plaquette example verifies code execution, **not** Penrose admissibility. Its four middle-interval temporal faces possess no strictly exclusive integrated edges. The mod-2 'all cavity +I, all Q -I' assignment is consistent for the *unfixed* control example.

## Run locally

```bash
python3 generate_r3_incidence.py control_spatial.json -o control_incidence.json
python3 generate_r3_incidence.py my_penrose_spatial.json -o penrose_three_step_incidence.json
```

Input schema is documented in the script. To recreate the exact R3 complex, supply (1) the original Penrose spatial *cell* graph with vertex IDs and oriented edge endpoints; (2) each spatial face as a closed oriented edge word; (3) the 3-step temporal identification convention, if different from trivial extrusion; (4) exactly which temporal/spatial faces comprise Q, and which preexisting terms are excluded from the cavity action; (5) which full spacetime edges are fixed, including boundary holonomy values if nonidentity; (6) any seam/topological identifications and coupling map. The generator supports trivial extrusion and identity-central consistency only. Modify or extend it if the original R3 complex uses nontrivial gluings or nonidentity boundary links. **Do not interpret its output as the original prism unless all these conventions match.**

## Near-term theorem test
Once source geometry is supplied: (a) verify each face word closes; (b) inspect Q/cavity edge incidence and fixed links; (c) search for local curvature redistribution over bounded collars; (d) prove either a comparison map or an *annealed* near-flat-event probability uniformly in ambient volume and lambda. Present results establish neither (c) nor (d) for the original Penrose prism. The uniform bound remains open.