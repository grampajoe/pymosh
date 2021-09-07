from pymosh.container import avi

import io
import unittest


class FakeRIFF(object):
    def __init__(self, contents):
        self._contents = contents

    def write(self, fh):
        fh.write(self._contents)


class TestAVI(unittest.TestCase):
    def test_init(self):
        """Should be able to create an index without a file."""
        index = avi.AVIFile()

        self.assertIsNotNone(index)

    def test_write(self):
        """Should write output to a file."""
        index = avi.AVIFile()
        index.riff = FakeRIFF(b'hello')

        fh = io.BytesIO()

        index.write(fh)

        self.assertEqual(fh.getvalue(), b'hello')
