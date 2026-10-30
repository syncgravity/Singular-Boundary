import tempfile, unittest
from pathlib import Path
import numpy as np
from analyze_stage25 import inspect
class TestStage25(unittest.TestCase):
    def test_schema_and_burn_shift(self):
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp)/'result.npz';x=np.ones((1,1,2,4,2,9,4,4));x[:,:,1]+=0.02
            one=np.ones((1,1,2,4,2,20,4));err=np.zeros((1,1,2,4))
            np.savez(p,conditional=x,onepoint=one,direct_product=np.ones((1,1,9,4,4)),burns=[48,96],depths=[12,32],seconds=np.ones_like(err),cache_error=err,sweeps=[10010],offsets=[0])
            z=inspect(p)
            self.assertAlmostEqual(z['products'][0]['abs_burn_shift'],.02)
            self.assertEqual(z['inner_replicas'],4)
    def test_reject_cache(self):
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp)/'result.npz';x=np.ones((1,1,2,4,2,9,4,4));o=np.ones((1,1,2,4,2,20,4))
            np.savez(p,conditional=x,onepoint=o,direct_product=np.ones((1,1,9,4,4)),burns=[48,96],depths=[12,32],seconds=np.ones((1,1,2,4)),cache_error=np.ones((1,1,2,4))*1e-4,sweeps=[10010],offsets=[0])
            with self.assertRaises(ValueError):inspect(p)
if __name__=='__main__':unittest.main()
