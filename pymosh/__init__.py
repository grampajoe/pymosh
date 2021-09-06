from .container import avi

__all__ = ['Index']


class Index(object):
    """Index is an index of video frame data."""

    def __init__(self, filename: str):
        self.filename = filename
        self.index = None

        # Assume AVI for now
        self.index = avi.AVIFile(filename)

    def __getattr__(self, index):
        return getattr(self.index, index)

    def __iter__(self):
        return iter(self.index)
