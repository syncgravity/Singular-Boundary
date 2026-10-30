import unittest,tempfile,json
from pathlib import Path
from stage17_measure import catalogue,digest
class Stage17SmokeTests(unittest.TestCase):
 def test_catalog_shapes(self):
  for kind in ('square','penrose'):
   p,i=catalogue(kind,2)
   self.assertEqual(p['idx'].shape[0],2)
   self.assertEqual(i.shape,(2,))
   self.assertTrue((p['r']>0).all())
 def test_catalog_full(self):
  for kind in ('square','penrose'):
   p,i=catalogue(kind,600)
   self.assertEqual(len(i),600)
 def test_hash(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d)/'a';p.write_bytes(b'abc')
   self.assertEqual(digest(p),'ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad')
if __name__=='__main__':unittest.main()
