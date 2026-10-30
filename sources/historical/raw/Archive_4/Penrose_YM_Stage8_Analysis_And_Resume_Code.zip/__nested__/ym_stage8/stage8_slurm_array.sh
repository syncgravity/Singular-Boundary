#!/usr/bin/env bash
#SBATCH --job-name=PenroseYM8
#SBATCH --array=0-7
#SBATCH --cpus-per-task=1
#SBATCH --mem=3G
#SBATCH --time=48:00:00
#SBATCH --output=stage8_%A_%a.log
set -euo pipefail
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 NUMBA_NUM_THREADS=1
SEEDS=(101 211 307 419)
IDX=${SLURM_ARRAY_TASK_ID:?Launch with sbatch --array=0-7}
KIND=square
if (( IDX >= 4 )); then KIND=penrose; fi
SEED=${SEEDS[$(( IDX % 4 ))]}
cd "$(dirname "$0")"
mkdir -p checkpoints
# Each array task owns a unique checkpoint and is safe to restart.
# Monitor convergence before accepting burn=1000 as sufficient.
while :; do
  python stage7_checkpointed.py --kind "$KIND" --seed "$SEED" --nt 20 \
    --beta 3.5 --burn 1000 --thin 10 --total-sweeps 10000 \
    --max-sweeps-this-run 100 --measure --checkpoint-root checkpoints
  COMPLETE=$(python - "$KIND" "$SEED" <<'PY'
import json,sys
from pathlib import Path
kind,seed=sys.argv[1:]
a=json.loads((Path('checkpoints')/f'{kind}_nt20_seed{seed}_progress.json').read_text())
print(a['completed_sweeps'])
PY
)
  if (( COMPLETE >= 10000 )); then break; fi
done
