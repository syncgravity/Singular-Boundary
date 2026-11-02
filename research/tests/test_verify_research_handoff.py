"""Adversarial and valid portable handoff fixtures. Run: python -m unittest discover -s research/tests -v"""
import hashlib
import json
import os
import stat
import tempfile
import unittest
import warnings
import zipfile
from pathlib import Path
from research.scripts.verify_research_handoff import verify_dir, verify_zip


def manifest(payload=b'data', name='data.txt'):
    return {'base': '/untrusted/original/path',
            'files': [{'path': name, 'bytes': len(payload),
                       'sha256': hashlib.sha256(payload).hexdigest()}]}


class HandoffVerifierTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def makezip(self, entries):
        dest = self.root / 'bundle.zip'
        with zipfile.ZipFile(dest, 'w') as z:
            for name, payload in entries:
                z.writestr(name, payload)
        return dest

    def test_valid_zip(self):
        verify_zip(self.makezip([('FILE_MANIFEST.json', json.dumps(manifest())), ('data.txt', b'data')]))

    def test_valid_directory(self):
        (self.root/'FILE_MANIFEST.json').write_text(json.dumps(manifest()))
        (self.root/'data.txt').write_bytes(b'data')
        verify_dir(self.root)

    def test_tampered_payload(self):
        with self.assertRaises(ValueError):
            verify_zip(self.makezip([('FILE_MANIFEST.json', json.dumps(manifest())), ('data.txt', b'evil')]))

    def test_missing_file(self):
        with self.assertRaises(FileNotFoundError):
            verify_zip(self.makezip([('FILE_MANIFEST.json', json.dumps(manifest()))]))

    def test_zip_traversal(self):
        with self.assertRaises(ValueError):
            verify_zip(self.makezip([('FILE_MANIFEST.json', json.dumps(manifest())), ('../bad', b'x'), ('data.txt', b'data')]))

    def test_manifest_traversal(self):
        with self.assertRaises(ValueError):
            verify_zip(self.makezip([('FILE_MANIFEST.json', json.dumps(manifest(name='../bad'))), ('data.txt', b'data')]))

    def test_duplicate_member(self):
        with warnings.catch_warnings():
            warnings.simplefilter('ignore', UserWarning)
            p = self.makezip([('FILE_MANIFEST.json', json.dumps(manifest())), ('data.txt', b'data'), ('data.txt', b'data')])
        with self.assertRaises(ValueError):
            verify_zip(p)

    def test_zip_symlink(self):
        s = zipfile.ZipInfo('data.txt')
        s.create_system = 3
        s.external_attr = (stat.S_IFLNK | 0o777) << 16
        with self.assertRaises(ValueError):
            verify_zip(self.makezip([('FILE_MANIFEST.json', json.dumps(manifest(payload=b'target'))), (s, b'target')]))

    def test_dir_symlink(self):
        (self.root/'FILE_MANIFEST.json').write_text(json.dumps(manifest()))
        (self.root/'target').write_bytes(b'data')
        os.symlink(self.root/'target', self.root/'data.txt')
        with self.assertRaises(ValueError):
            verify_dir(self.root)

    def test_malformed_manifest(self):
        with self.assertRaises(ValueError):
            verify_zip(self.makezip([('FILE_MANIFEST.json', json.dumps({'files': [{'path': 'data.txt', 'bytes': True, 'sha256': 'bad'}]})), ('data.txt', b'data')]))

    def test_prefixed_bundle(self):
        verify_zip(self.makezip([('package/FILE_MANIFEST.json', json.dumps(manifest())), ('package/data.txt', b'data')]))


if __name__ == '__main__':
    unittest.main()
