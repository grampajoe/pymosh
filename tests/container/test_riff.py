from pymosh.container import riff

import unittest
import io


class TestRIFFIndex(unittest.TestCase):
    def test_init(self):
        """Should be able to create an index without a file."""
        index = riff.RiffIndex()

        self.assertIsNotNone(index)

    def test_write(self):
        """Should write to a file."""
        index = riff.RiffIndex()
        indexList = riff.RiffIndexList(header=b'RIFF', list_type=b'hdrl')
        chunkFile = io.BytesIO(b'TEST\x40\x00\x00\x00fart')
        chunk = riff.RiffIndexChunk(
            chunkFile, header=b'TEST', length=4, position=8)
        index.chunks = [indexList, chunk]

        expected = indexList.bytes() + chunk.bytes()

        fh = io.BytesIO()

        index.write(fh)

        self.assertEqual(fh.getvalue(), expected)


class TestRiffIndexList(unittest.TestCase):
    def test_bytes(self):
        """Should return a byte representation of the object."""
        indexList = riff.RiffIndexList(header=b'RIFF', list_type=b'hdrl')

        # Header, length of list_type as 4 bytes, list_type
        expected = b'RIFF\x04\x00\x00\x00hdrl'

        self.assertEqual(indexList.bytes(), expected)


class TestRiffIndexChunk(unittest.TestCase):
    def test_bytes(self):
        """Should return a byte representation of the object."""
        contents = io.BytesIO(b'TEST\x04\x00\x00\x00butt')

        # This chunk is the whole file
        expected = contents.getvalue()

        chunk = riff.RiffIndexChunk(contents, b'TEST', length=4, position=8)

        self.assertEqual(chunk.bytes(), expected)


class TestRiffDataChunk(unittest.TestCase):
    def test_bytes(self):
        """Should return a byte representation of the chunk."""
        chunk = riff.RiffDataChunk(header=b'TEST', data=b'fart')

        # 4 byte header, length of data, data
        expected = b'TEST\x04\x00\x00\x00fart'

        self.assertEqual(chunk.bytes(), expected)
