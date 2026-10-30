import json
from pathlib import Path
import tempfile
import unittest
from unittest import mock
import stage9_m1_manager as m

SETTINGS = {'kind':'square','seed':101,'nt':20,'beta':3.5,'burn':1000,'thin':10}

class ManagerTests(unittest.TestCase):
    def test_missing_is_fresh(self):
        with tempfile.TemporaryDirectory() as td:
            self.assertIsNone(m.read_progress(Path(td),'square',101))

    def test_half_checkpoint_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            (Path(td)/'square_nt20_seed101.npz').write_bytes(b'x')
            with self.assertRaisesRegex(RuntimeError,'Half-written'):
                m.read_progress(Path(td),'square',101)

    def test_hash_validation(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td);g,p=m.paths(root,'square',101)
            g.write_bytes(b'test')
            p.write_text(json.dumps({'settings':SETTINGS,'completed_sweeps':5,'checkpoint_sha256':m.checksum(g)}))
            self.assertEqual(m.read_progress(root,'square',101,True)['completed_sweeps'],5)
            g.write_bytes(b'changed')
            with self.assertRaisesRegex(RuntimeError,'hash mismatch'):
                m.read_progress(root,'square',101,True)

    def test_reset_archive_only_checkpoint_files(self):
        with tempfile.TemporaryDirectory() as td:
            basedir=Path(td);(basedir/'checkpoints').mkdir()
            root=basedir/'checkpoints'
            (root/'square_nt20_seed101.npz').write_bytes(b'test')
            with mock.patch.object(m,'HERE',basedir):
                args=m.make_parser().parse_args(['reset'])
                m.cmd_reset(args)
                self.assertTrue((root/'square_nt20_seed101.npz').exists())
                args=m.make_parser().parse_args(['reset','--apply'])
                m.cmd_reset(args)
                self.assertFalse((root/'square_nt20_seed101.npz').exists())
                self.assertTrue(any(basedir.glob('retired_stage9_checkpoints_*/square_nt20_seed101.npz')))

    def test_reset_fails_with_unknown_file(self):
        with tempfile.TemporaryDirectory() as td:
            basedir=Path(td); root=basedir/'checkpoints';root.mkdir()
            (root/'notes.txt').write_text('do not remove')
            with mock.patch.object(m,'HERE',basedir):
                args=m.make_parser().parse_args(['reset','--mode','delete','--apply','--confirm','DELETE_OLD_STAGE9_CHECKPOINTS'])
                with self.assertRaisesRegex(RuntimeError,'Unexpected files'):
                    m.cmd_reset(args)
                self.assertTrue((root/'notes.txt').exists())

    def test_reset_delete_requires_confirm(self):
        with tempfile.TemporaryDirectory() as td:
            basedir=Path(td);root=basedir/'checkpoints';root.mkdir()
            (root/'square_nt20_seed101.npz').write_bytes(b'test')
            with mock.patch.object(m,'HERE',basedir):
                args=m.make_parser().parse_args(['reset','--mode','delete','--apply'])
                with self.assertRaisesRegex(RuntimeError,'Deletion refused'):
                    m.cmd_reset(args)
                self.assertTrue((root/'square_nt20_seed101.npz').exists())

    def test_concurrency_selection(self):
        parser=m.make_parser()
        args=parser.parse_args(['run','--workers','2','--chunk','10','--passes','1','--kinds','square','--seeds','101','211'])
        self.assertEqual(args.workers,2)
        self.assertEqual(len(m.select(args)),2)

    def test_selection_duplicate_seed(self):
        parser=m.make_parser()
        args=parser.parse_args(['run','--seeds','101','101'])
        with self.assertRaises(ValueError):m.select(args)

    def test_reset_deletes_known_only(self):
        with tempfile.TemporaryDirectory() as td:
            basedir=Path(td);root=basedir/'checkpoints';root.mkdir()
            cp=root/'square_nt20_seed101.npz';cp.write_bytes(b'x')
            (basedir/'stage7_checkpointed.py').write_text('safe')
            with mock.patch.object(m,'HERE',basedir):
                args=m.make_parser().parse_args(['reset','--mode','delete','--apply','--confirm','DELETE_OLD_STAGE9_CHECKPOINTS'])
                m.cmd_reset(args)
                self.assertFalse(cp.exists())
                self.assertTrue((basedir/'stage7_checkpointed.py').exists())

if __name__=='__main__':unittest.main()
