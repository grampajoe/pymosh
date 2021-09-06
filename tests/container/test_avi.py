from pymosh.container import avi

import unittest


class TestAVI(unittest.TestCase):
    def test_init(self):
        """Should be able to create an index without a file."""
        index = avi.AVIFile()

        self.assertIsNotNone(index)
