from pymosh import Index

import unittest


class TestIndex(unittest.TestCase):
    """Tests for the Index class."""

    def test_init(self):
        """Should be able to create an instance without a file."""
        index = Index()

        self.assertIsNotNone(index)
