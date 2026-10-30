import unittest
from peeling_certificate import certify
class TestPeeling(unittest.TestCase):
    def test_disk(self):
        d={'faces':{'a':['x','y','z','w'],'b':['w','u','v','t']},'fill':['a','b']}
        r=certify(d);self.assertTrue(r['full_certificate']);self.assertEqual(r['peeled_count'],2)
    def test_closed_shell(self):
        d={'faces':{'a':['x','y'],'b':['x','y']},'fill':['a','b']}
        r=certify(d);self.assertFalse(r['full_certificate']);self.assertEqual(r['peeled_count'],0)
    def test_outside_face_blocks_peeling(self):
        d={'faces':{'a':['x','y'],'b':['x','y']},'fill':['a']}
        r=certify(d);self.assertFalse(r['full_certificate'])
    def test_full_linear_rank_does_not_imply_peeling(self):
        # Incidence rows [[1,1,0],[0,1,1],[1,0,1]] have determinant 2.
        # Every edge nevertheless belongs to two faces.
        d={"faces":{"a":["x","y"],"b":["y","z"],"c":["x","z"]},"fill":["a","b","c"]}
        r=certify(d);self.assertFalse(r["full_certificate"]);self.assertEqual(r["peeled_count"],0)
    def test_partial(self):
        d={'faces':{'a':['x','y'],'b':['x','y'],'c':['z']},'fill':['a','b','c']}
        r=certify(d);self.assertEqual(r['peeled_count'],1);self.assertEqual(r['unpeeled'],['a','b'])
if __name__=='__main__':unittest.main()
