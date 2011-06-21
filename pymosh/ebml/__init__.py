from pymosh.ebml.elements import Element
from pymosh.ebml.elements.generic import *
from pymosh.ebml.util import *
import struct

# Container class
class EBMLDocument(Master):
    def __init__(self, fh):
        self._children = self.parse(fh)

    def parse(self, fh):
        if isinstance(fh, basestring):
            fh = open(fh, 'rb')
        elif not isinstance(fh, file):
            raise Exception, 'Not a valid file.'

        # Get file length
        fh.seek(0, os.SEEK_END)
        total_length = fh.tell()
        fh.seek(0)

        tree = []

        while fh.tell() < total_length:
            ebml_id = read_id(fh)
            ebml_length = read_length(fh)
            elem = Element(fh, ebml_id, ebml_length, fh.tell())
            tree.append(elem)

        return tree

    def _ebml_int(self, n):
        """Encode an EBML-style unsigned integer for length descriptors."""
        data = ''
        while n:
            data = struct.pack('!B', n & 0b11111111) + data
            n >>= 8
        # Just use a whole byte to encode the length of the data
        data = struct.pack('!B', 0b10000000 >> len(data)) + data
        return data

    def write(self, fh):
        if isinstance(fh, basestring):
            fh = open(fh, 'wb')
        elif not isinstance(fh, file):
            raise Exception, 'Not a valid file.'

        def write_element(el):
            fh.write(el._header)
            fh.write(self._ebml_int(el._length))
            if el.has_children():
                for child in el:
                    write_element(child)
            else:
                fh.write(el[:])

        for child in self._children:
            write_element(child)
