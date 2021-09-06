from pymosh.container import riff

import unittest


class TestRIFF(unittest.TestCase):
    def test_init(self):
        """Should be able to create an index without a file."""
        index = riff.RiffIndexChunk()

        self.assertIsNotNone(index)
