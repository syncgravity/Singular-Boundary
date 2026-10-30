"""Independent matching of vectorized large torus assembler to Stage 3 reference."""
import numpy as np
from stage7_large_torus import assemble_vectorized,exact_checks
from stage2_rational_torus import build_torus
from stage3_periodic_pilot import square_torus
from stage2_ym_calibration import assemble

def test_one(sp,nt=6):
 a=(sp['physical_area']/sp['F'])**.5
 old,co=assemble(sp,nt,3.5,a,a)
 new=assemble_vectorized(sp,nt,3.5,a)
 for key in ('fi','sg','beta','adj','degree'):
  assert np.array_equal(old[key],new[key]), key
 assert exact_checks(sp,new)['closure']
 print('exact implementation match:',sp['spatial_kind'],'V',sp['V'],'nt',nt)

if __name__=='__main__':
 test_one(build_torus(5))
 test_one(square_torus(13,14,61.70899448216604))
