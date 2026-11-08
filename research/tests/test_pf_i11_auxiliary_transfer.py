import math,unittest
from verify_pf_i11_auxiliary_transfer import transfer

class AuxiliaryTransferTests(unittest.TestCase):
    def test_character_haar_orthonormality(self):
        q=transfer();self.assertLess(q['max_character_Haar_orthogonality_error'],1e-12)
    def test_finite_transfer_strict_positive(self):
        for beta in [0,.71,3.]:
            q=transfer(beta=beta)
            self.assertGreater(q['min_symmetric_mult_matrix_eigenvalue'],0)
            self.assertGreater(q['min_transfer_eigenvalue'],0)
            self.assertGreater(q['auxiliary_gap'],0)
    def test_noninteracting_gap_equals_casimir_scale(self):
        for eps in [.01,.1,1.]:
            q=transfer(beta=0,electric_scale=eps)
            self.assertAlmostEqual(q['auxiliary_gap'],.75*eps,places=10)
    def test_external_kinetic_scale_can_make_gap_arbitrarily_small(self):
        small=transfer(beta=0,electric_scale=1e-4)
        large=transfer(beta=0,electric_scale=1.)
        self.assertLess(small['auxiliary_gap'],1e-3)
        self.assertGreater(large['auxiliary_gap'],.7)

if __name__=='__main__':unittest.main()
