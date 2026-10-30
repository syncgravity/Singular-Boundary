# Stage 26 → R3 incidence bridge

Stage 26 calls `setup_geometry(kind,20,3.5)` from `stage22_shifted`, obtaining `lat['fi']` and `lat['sg']`. This script exports those actual plaquette-edge words **if** they are integer 2D arrays with ±1 orientation signs, without inventing graph endpoints, historical Q, or boundary links.

1. Copy `export_stage26_incidence.py` into `stage26_outer/` (alongside `stage26_outer.py`).
2. From `stage26_outer/`, run:

   ```sh
   python3 export_stage26_incidence.py --kind penrose --out penrose_stage26_full_incidence.json
   ```

3. **For a genuine R3 test**, identify the actual inserted face indices (`q.json` as `[12,13,...]`) and boundary-frozen edge indices (`fixed.json` as `[0,4,...]`) from the historical R3 definition, then rerun:

   ```sh
   python3 export_stage26_incidence.py --kind penrose --q q.json --fixed fixed.json --out penrose_r3_partition.json
   python3 audit_linear_repair.py penrose_r3_partition.json --out penrose_r3_linear_audit.json
   ```

The exporter is intentionally strict. If the Stage 22 arrays use packing/sentinels other than plain ±1 signed face-edge arrays, it stops with an error and the representation must be examined rather than silently guessed. The `edges` value is null because Stage 26 `fi`/`sg` alone do not provide vertex endpoints. The complete Stage26 lattice is **not** automatically the historical 12-prism R3 cavity. Rank audits on the full lattice can be substantial; restrict to a certified subcomplex for the R3 test.

Also upload `stage24_inner/deps_stage23/stage22_shifted.py` and the geometry modules it imports, particularly `setup_geometry` and the routine constructing `lat['fi']`/`lat['sg']`. We can then validate this exporter and derive a certified subcomplex and R3 insertion partition.
