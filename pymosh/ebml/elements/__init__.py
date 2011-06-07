import os

# EBML Element Classes

class BaseElement(object):
    """Base class for EBML elements.

    Element creation uses this class's __subclasses__ list to determine which
    type of element to create."""
    def __init__(self, fh, header, length, position):
        self._file = fh
        self._header = header
        self._length = length
        self._position = position

    def __getitem__(self, index):
        if self.has_children():
            return self._children[index]
        elif isinstance(index, slice):
            data = self._data()
            return data.__getitem__(index)
        elif index < self._length:
            current = self._file.tell()
            self._file.seek(self._position + index)
            data = self._file.read(1)
            self._file.seek(current)
            return data
        else:
            raise IndexError, 'Index out of range.'

    def _data(self):
        current = self._file.tell()
        self._file.seek(self._position)
        data = self._file.read(self._length)
        self._file.seek(current)
        return data

    def type(self):
        return self._type

    def value(self):
        if self.type() not in ('Master', 'Binary'):
            return self._value
        else:
            return None

    def has_children(self):
        return hasattr(self, '_children')

    def find(self, element_class):
        if self.__class__.__name__ == element_class:
            return self
        elif self.has_children():
            for child in self:
                el = child.find(element_class)
                if el != None:
                    return el
        return None

    def find_all(self, element_class):
        if self.__class__.__name__ == element_class:
            return [self]
        if self.has_children():
            elements = []
            for child in self:
                elements.extend(child.find_all(element_class))
            return elements
        return []

    @classmethod
    def is_element_for(self, header):
        try:
            return header == self.header
        except AttributeError:
            return False

class UndefinedElement(BaseElement):
    """An undefined element.

    Data is treated as binary and skipped."""
    header = ''

    def __init__(self, fh, header, length, position):
        super(UndefinedElement, self).__init__(fh, header, length, position)
        print "Caught undefined element '{3}', seeking to {0} ({1} bytes from {2}).".format(length +
                fh.tell(), length, fh.tell(), header.encode('hex'))
        fh.seek(length, os.SEEK_CUR)

def Element(fh, header, length, position):
    """Factory function for EBML elements."""
    # Types
    for cls in BaseElement.__subclasses__():
        # Elements
        for scls in cls.__subclasses__():
            if scls.is_element_for(header):
                return scls(fh, header, length, position)
    return UndefinedElement(fh, header, length, position)
