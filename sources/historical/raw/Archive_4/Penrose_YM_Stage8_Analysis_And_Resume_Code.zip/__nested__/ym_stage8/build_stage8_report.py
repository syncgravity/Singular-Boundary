import json
from pathlib import Path
from stage8_admission import audit
root=Path(__file__).parent
A=audit(root/'checkpoints',check_npz=False)
M=json.loads((root/'stage8_physical_matching.json').read_text())
counts={k:[r['sweeps'] for r in A['chains'] if r['kind']==k] for k in ('square','penrose')}
if any(v is None for v in counts.values()): raise AssertionError('missing counts')
status=[]
for k in ('square','penrose'):
 status.append(f"| {k} | {len(counts[k])} | {', '.join(str(x) for x in counts[k])} | {sum(r['production_samples'] for r in A['chains'] if r['kind']==k)} |")
req='\n'.join('| '+key.replace('_',' ')+' | '+('Passed (checkpoint existence only)' if value else 'Not established')+' |' for key,value in A['requirements'].items())
text=f'''# Stage 8: large independent-chain continuation and admission gate

**Status: incomplete thermalization; no physical mass or string tension extracted.** This is a computational progress and reproducibility report, not a continuum Yang–Mills measurement.

## Executed gauge-field continuation

From the verified Stage 7 20-slice M=55 rational Penrose torus (22,808 spatial vertices) and 151×151 square torus (22,801 vertices), both at beta_ref=3.5, we continued the exact checkpointed interacting Metropolis code using hashed seeds 101, 211, 307, 419. Each spacetime lattice has about 1.37 million SU(2) links. All checkpoint parameters are locked, and each completed segment checks the cached plaquettes against full recomputation.

| Geometry | Independently seeded checkpoints | Completed warm-up sweeps per seed (101, 211, 307, 419) | Post-burn samples |
|---|---:|---|---:|
{chr(10).join(status)}

The nominal burn-in cut is 1000 sweeps, so every completed step above is **thermalization**, not an equilibrium estimate. In particular, no 0++ correlator or torelon/string-tension measurement from these fields is admitted. Distinct seeds do not by themselves certify statistical independence or stationarity.

## Physical-separation screen

The archived deterministic 100-source measurement plans were compared using actual embedded path displacement. **{M['matched_distinct_r']} / {M['total_distinct_square_r']}** unique square source lengths have a Penrose length within {100*M['threshold']:.0f}%. This helps select common radial bins for future static potentials, but orientation distribution, renormalized matching and operator-overlap biases are not controlled by this test.

## Acceptance ledger

| Requirement | Current status |
|---|---|
{req}

These criteria must not be conflated. Establishing multiple restorable chains is engineering progress but **not** convergence-certified Yang–Mills spectroscopy. Prior Stage 5 square data did not resolve a stable scalar mass or string tension. Stage 6 conditional sampling reduced raw winding-product fluctuations in a pilot, but its inner/outer convergence was not certified. Neither historical result can fill in absent Stage 8 production data.

## Available deliverables and compute limits

The accompanying checkpoints contain actual 20-slice link and plaquette arrays plus RNG states, not fabricated observations. `stage8_campaign.py` resumes them; `stage8_admission.py` refuses a fit when the chain, measurement and statistical gates are absent. `stage8_slurm_array.sh` is a reproducible **example** for eight independent cluster jobs. The earlier runtime audit estimated approximately 33 hours for a four-seed 10k-sweep-per-chain campaign across both geometries, **before** full spectroscopy, convergence-driven extensions, multiple lattice spacings, and approximant/coupling matching. That full computation was not completed in this session.

**Scientific decision:** \\(m_{{0^{{++}}}}\\), \\(\\sigma\\), \\(m_{{0^{{++}}}}/\\sqrt{{\\sigma}}\\), and any continuum contrast remain **not determined**. A reliable physical extraction cannot be claimed without actual equilibrated correlator measurements and fits.
'''
(root/'STAGE_8_REPORT.md').write_text(text)
print('Wrote Stage 8 report')
