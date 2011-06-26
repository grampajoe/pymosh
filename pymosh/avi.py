import riff
import struct
import sys
from mpeg4 import is_iframe

class Stream(object):
    def __init__(self, num, stream_type):
        self.num = int(num)
        self.type = stream_type
        self.headers = {}
        self.chunks = []

    @staticmethod
    def from_header_list(num, header_list):
        stream = Stream(num, '')

        strh = header_list.find('strh')
        unpacked = struct.unpack('4s4sIIIIIIIIIIII', strh.data)
        stream.headers = {
            'type':                  unpacked[0],
            'handler':               unpacked[1],
            'flags':                 unpacked[2],
            'priority':              unpacked[3],
            'initial_frames':        unpacked[4],
            'scale':                 unpacked[5],
            'rate':                  unpacked[6],
            'start':                 unpacked[7],
            'suggested_buffer_size': unpacked[8],
            'quality':               unpacked[9],
            'sample_size':           unpacked[10],
        }
        stream.type = stream.headers['type']

        return stream

    def add_frame(self, chunk):
        self.chunks.append(chunk)

    def __getitem__(self, index):
        return self.chunks.__getitem__(index)

    def __iter__(self):
        return self.chunks.__iter__()

    def __len__(self):
        return len(self.chunks)

    def append(self, *args):
        return self.chunks.append(*args)

    def extend(self, *args):
        return self.chunks.extend(*args)

    def replace(self, chunks):
        self.chunks = chunks

class AVIFile(object):
    """A wrapper for AVI files."""
    def __init__(self, filename):
        self.riff = riff.RiffIndex(filename=filename)

        header = self.riff.find('LIST', 'hdrl')
        avih = header.find('avih')
        unpacked = struct.unpack('IIIIIIIIII4I', avih.data) 
        self.headers = {
                'micro_sec_per_frame':   unpacked[0],
                'max_bytes_per_sec':     unpacked[1],
                'flags':                 unpacked[3], # 2 is reserved/unused
                'total_frames':          unpacked[4],
                'inital_frames':         unpacked[5],
                'streams':               unpacked[6],
                'suggested_buffer_size': unpacked[7],
                'width':                 unpacked[8],
                'height':                unpacked[9], # Rest are reserved 
        }

        # Get stream info
        stream_lists = header.find_all('LIST', 'strl')
        self.streams = []
        for l in stream_lists:
            self.streams.append(Stream.from_header_list(len(self.streams), l))

        self.frame_order = []
        self.split_streams()

    def __iter__(self):
        return iter(self.streams)

    def add_frame_to_stream(self, chunk):
        stream_num = int(chunk.header[:2])
        if stream_num < len(self.streams):
            self.frame_order.append((stream_num, len(self.streams[stream_num])))
            self.streams[stream_num].add_frame(chunk)

    def split_streams(self):
        movi = self.riff.find('LIST', 'movi')
        for chunk in movi:
            self.add_frame_to_stream(chunk)

    def combine_streams(self):
        chunks = []
        for frame_record in self.frame_order:
            stream_num, frame_num = frame_record
            stream = self.streams[stream_num]
            frame = stream[frame_num]
            chunks.append(frame)
        return chunks

    def _video(self):
        return filter(lambda stream: stream.type == 'vids', self.streams)
    video = property(_video)

    def _audio(self):
        return filter(lambda stream: stream.type == 'auds', self.streams)
    audio = property(_audio)

    def rebuild(self):
        """Rebuild RIFF tree and index from streams."""
        movi = self.riff.find('LIST', 'movi')
        movi.chunks = self.combine_streams()
        self.rebuild_index()

    def rebuild_index(self):
        old_index = self.riff.find('idx1')
        movi = self.riff.find('LIST', 'movi')
        data = ''
        offset = 0
        flags = {
            'base':     0x00000000,
            'keyframe': 0x00000010,
        }
        for chunk in movi:
            length = len(chunk)
            frame_flags = flags['base']
            # If it's a video keyframe or audio frame, use keyframe flag
            if (chunk.header[2] == 'd' and is_iframe(chunk)) or (chunk.header[2] == 'w'):
                frame_flags |= flags['keyframe']
            data += struct.pack('<4sIII', chunk.header, frame_flags, offset,
                    length+8)
            offset += length + 8 + (length % 2)
        new_index = riff.RiffDataChunk('idx1', data)
        self.riff.find('RIFF').replace(old_index, new_index)

    def write(self, fh):
        self.riff.write(fh)
