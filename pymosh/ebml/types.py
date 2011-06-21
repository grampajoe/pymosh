from pymosh.ebml.elements import Element, BaseElement
from pymosh.ebml.util import *
import os

# Element Types
class SignedInt(BaseElement):
    """A signed integer."""
    _type = 'SignedInt'

    def __init__(self, fh, header, length, position):
        super(SignedInt, self).__init__(fh, header, length, position)
        data = read(fh, length)
        self._value, = struct.unpack('!b', data[0])
        for c in data[1:]:
            n, = struct.unpack('!B', c)
            self._value <<= 8
            self._value += n

class UnsignedInt(BaseElement):
    """An unsigned integer."""
    _type = 'UnsignedInt'

    def __init__(self, fh, header, length, position):
        super(UnsignedInt, self).__init__(fh, header, length, position)
        data = read(fh, length)
        self._value = 0
        for c in data:
            n, = struct.unpack('!B', c)
            self._value <<= 8
            self._value += n

class Float(BaseElement):
    """A float."""
    _type = 'Float'

    def __init__(self, fh, header, length, position):
        super(Float, self).__init__(fh, header, length, position)
        data = read(fh, length)
        if len(data) == 4:
            self._value, = struct.unpack('!f', data)
        elif len(data) == 8:
            self._value, = struct.unpack('!d', data)

class String(BaseElement):
    """A string."""
    _type = 'String'

    def __init__(self, fh, header, length, position):
        super(String, self).__init__(fh, header, length, position)
        data = read(fh, length)
        self._value = data.encode('ascii')

class UTF8(BaseElement):
    """A UTF8 string."""
    _type = 'UTF8'

    def __init__(self, fh, header, length, position):
        super(UTF8, self).__init__(fh, header, length, position)
        data = read(fh, length)
        self._value = data.encode('utf8')

class Date(BaseElement):
    """A date."""
    _type = 'Date'

    def __init__(self, fh, header, length, position):
        super(Date, self).__init__(fh, header, length, position)
        data = read(fh, length)
        n, = struct.unpack('!q', data)
        self._value = n

class Master(BaseElement):
    """An EBML element with sub-elements."""
    _type = 'Master'

    def __init__(self, fh, header, length, position):
        super(Master, self).__init__(fh, header, length, position)

        self._children = []

        current = fh.tell()
        end = current + length
        while fh.tell() < end:
            ebml_id = read_id(fh)
            ebml_length = read_length(fh)
            elem = Element(fh, ebml_id, ebml_length, position)
            self._children.append(elem)

    def data(self):
        """Don't return any data for master elements."""
        return ''

    def __iter__(self):
        return self._children.__iter__()

class Binary(BaseElement):
    """Binary data."""
    _type = 'Binary'

    def __init__(self, fh, header, length, position):
        super(Binary, self).__init__(fh, header, length, position)
        fh.seek(length, os.SEEK_CUR)
