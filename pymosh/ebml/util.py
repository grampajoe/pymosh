import os
import struct

# Utility Functions

def read(fh, length, position=None):
    """Read length bytes from the file, raising an exception if EOF is
    reached before length bytes."""
    if position != None:
        fh.seek(position)
    data = fh.read(length)
    if len(data) != length:
        raise Exception, 'Reached end of file unexpectedly.'
    return data

def read_variable_length(fh, position=None):
    """Read a UTF8-like sequence with a Length Descriptor.
    
    The number of 0s and the first 1 from the most significant end of the
    byte indicate the length of the data to be read."""
    data, = struct.unpack('!B', read(fh, 1, position))

    # Determine length of remaining data to be read
    length = 0
    while not data & 0b10000000:
        data <<= 1
        length += 1

    data = struct.pack('!B', data >> length)

    if length:
        data += read(fh, length)

    return data

def read_id(fh, position=None):
    """Read an EBML ID, which is just a string of bytes."""
    data = read_variable_length(fh, position)
    return data

def read_length(fh, position=None):
    """Read an EBML element length, which is a variable length integer."""
    data = read_variable_length(fh, position)
    length, = struct.unpack('!B', data[0])

    # Chop off the first 1
    length <<= len(data)-1
    length &= 0b01111111
    length >>= len(data)-1

    for c in data[1:]:
        n, = struct.unpack('!B', c)
        length <<= 8
        length += n

    return length
