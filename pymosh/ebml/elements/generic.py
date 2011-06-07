from ebml.types import *

# Generic EBML Elements

class EBML(Master):
    header = '\x1A\x45\xDF\xA3'

class EBMLVersion(UnsignedInt):
    header = '\x42\x86'
    default = 1

class EBMLReadVersion(UnsignedInt):
    header = '\x42\xF7'
    default = 1

class EBMLMaxIDLength(UnsignedInt):
    header = '\x42\xF2'
    default = 4

class EBMLMaxSizeLength(UnsignedInt):
    header = '\x42\xF3'
    default = 8

class DocType(String):
    header = '\x42\x82'
    level = 1
    default = ''

class DocTypeVersion(UnsignedInt):
    header = '\x42\x87'
    default = 1

class DocTypeReadVersion(UnsignedInt):
    header = '\x42\x85'
    default = 1

class Void(Binary):
    header = '\xEC'

class CRC32(Binary):
    header = '\xBF'
