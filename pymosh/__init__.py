import sys

__all__ = ['index', 'avi', 'mpeg4', 'riff']

class VideoIndex(object):
    def __init__(self, filename):
        self.filename = filename
        self.index = None

        # Just do this for now
        import avi
        self.index = avi.AVIFile(filename)

    def __getattr__(self, index):
        return getattr(self.index, index)

    def __iter__(self):
        return iter(self.index)

def index(filename):
    return VideoIndex(filename)
