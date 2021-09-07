from pymosh import Index

import io
import unittest


class FakeIndex(object):
    def __init__(self, contents):
        self._contents = contents

    def write(self, fh):
        fh.write(self._contents)


class TestIndex(unittest.TestCase):
    """Tests for the Index class."""

    def test_init(self):
        """Should be able to create an instance without a file."""
        index = Index()

        self.assertIsNotNone(index)

    def test_write(self):
        """Should write the container contents to a file."""
        index = Index()
        index.index = FakeIndex(b'hello')

        fh = io.BytesIO()

        index.write(fh)

        self.assertEqual(fh.getvalue(), b'hello')
