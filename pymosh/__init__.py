from . import avi

__all__ = ['Index']


class Index(object):
    def __init__(self, filename):
        self.filename = filename
        self.index = None

        # Assume AVI for now
        self.index = avi.AVIFile(filename)

    def __getattr__(self, index):
        return getattr(self.index, index)

    def __iter__(self):
        return iter(self.index)
