from ebml.types import *

# Level 0

class Segment(Master):
        header='\x18\x53\x80\x67'


# Level 1

class SeekHead(Master):
        header='\x11\x4D\x9B\x74'

class Info(Master):
        header='\x15\x49\xA9\x66'

class Cluster(Master):
        header='\x1F\x43\xB6\x75'

class Tracks(Master):
        header='\x16\x54\xAE\x6B'

class Cues(Master):
        header='\x1C\x53\xBB\x6B'

class Attachments(Master):
        header='\x19\x41\xA4\x69'

class Chapters(Master):
        header='\x10\x43\xA7\x70'

class Tags(Master):
        header='\x12\x54\xC3\x67'


# Level 2

class Seek(Master):
        header='\x4D\xBB'

class SegmentUID(Binary):
        header='\x73\xA4'

class SegmentFilename(UTF8):
        header='\x73\x84'

class PrevUID(Binary):
        header='\x3C\xB9\x23'

class PrevFilename(UTF8):
        header='\x3C\x83\xAB'

class NextUID(Binary):
        header='\x3E\xB9\x23'

class NextFilename(UTF8):
        header='\x3E\x83\xBB'

class SegmentFamily(Binary):
        header='\x44\x44'

class ChapterTranslate(Master):
        header='\x69\x24'

class TimecodeScale(UnsignedInt):
        header='\x2A\xD7\xB1'

class Duration(Float):
        header='\x44\x89'

class DateUTC(Date):
        header='\x44\x61'

class Title(UTF8):
        header='\x7B\xA9'

class MuxingApp(UTF8):
        header='\x4D\x80'

class WritingApp(UTF8):
        header='\x57\x41'

class Timecode(UnsignedInt):
        header='\xE7'

class SilentTracks(Master):
        header='\x58\x54'

class Position(UnsignedInt):
        header='\xA7'

class PrevSize(UnsignedInt):
        header='\xAB'

class SimpleBlock(Binary):
        header='\xA3'

class BlockGroup(Master):
        header='\xA0'

class TrackEntry(Master):
        header='\xAE'

class CuePoint(Master):
        header='\xBB'

class AttachedFile(Master):
        header='\x61\xA7'

class EditionEntry(Master):
        header='\x45\xB9'

class Tag(Master):
        header='\x73\x73'


# Level 3

class SeekID(Binary):
        header='\x53\xAB'

class SeekPosition(UnsignedInt):
        header='\x53\xAC'

class ChapterTranslateEditionUID(UnsignedInt):
        header='\x69\xFC'

class ChapterTranslateCodec(UnsignedInt):
        header='\x69\xBF'

class ChapterTranslateID(Binary):
        header='\x69\xA5'

class SilentTrackNumber(UnsignedInt):
        header='\x58\xD7'

class Block(Binary):
        header='\xA1'

class BlockAdditions(Master):
        header='\x75\xA1'

class BlockDuration(UnsignedInt):
        header='\x9B'

class ReferencePriority(UnsignedInt):
        header='\xFA'

class ReferenceBlock(SignedInt):
        header='\xFB'

class CodecState(Binary):
        header='\xA4'

class Slices(Master):
        header='\x8E'

class TrackNumber(UnsignedInt):
        header='\xD7'

class TrackUID(UnsignedInt):
        header='\x73\xC5'

class TrackType(UnsignedInt):
        header='\x83'

class FlagEnabled(UnsignedInt):
        header='\xB9'

class FlagDefault(UnsignedInt):
        header='\x88'

class FlagForced(UnsignedInt):
        header='\x55\xAA'

class FlagLacing(UnsignedInt):
        header='\x9C'

class MinCache(UnsignedInt):
        header='\x6D\xE7'

class MaxCache(UnsignedInt):
        header='\x6D\xF8'

class DefaultDuration(UnsignedInt):
        header='\x23\xE3\x83'

class TrackTimecodeScale(Float):
        header='\x23\x31\x4F'

class MaxBlockAdditionID(UnsignedInt):
        header='\x55\xEE'

class Name(UTF8):
        header='\x53\x6E'

class Language(String):
        header='\x22\xB5\x9C'

class CodecID(String):
        header='\x86'

class CodecPrivate(Binary):
        header='\x63\xA2'

class CodecName(UTF8):
        header='\x25\x86\x88'

class AttachmentLink(UnsignedInt):
        header='\x74\x46'

class CodecDecodeAll(UnsignedInt):
        header='\xAA'

class TrackOverlay(UnsignedInt):
        header='\x6F\xAB'

class TrackTranslate(Master):
        header='\x66\x24'

class Video(Master):
        header='\xE0'

class Audio(Master):
        header='\xE1'

class TrackOperation(Master):
        header='\xE2'

class ContentEncodings(Master):
        header='\x6D\x80'

class CueTime(UnsignedInt):
        header='\xB3'

class CueTrackPositions(Master):
        header='\xB7'

class FileDescription(UTF8):
        header='\x46\x7E'

class FileName(UTF8):
        header='\x46\x6E'

class FileMimeType(String):
        header='\x46\x60'

class FileData(Binary):
        header='\x46\x5C'

class FileUID(UnsignedInt):
        header='\x46\xAE'

class EditionUID(UnsignedInt):
        header='\x45\xBC'

class EditionFlagHidden(UnsignedInt):
        header='\x45\xBD'

class EditionFlagDefault(UnsignedInt):
        header='\x45\xDB'

class EditionFlagOrdered(UnsignedInt):
        header='\x45\xDD'

class ChapterAtom(Master):
        header='\xB6'

class Targets(Master):
        header='\x63\xC0'

class SimpleTag(Master):
        header='\x67\xC8'


# Level 4

class BlockMore(Master):
        header='\xA6'

class TimeSlice(Master):
        header='\xE8'

class TrackTranslateEditionUID(UnsignedInt):
        header='\x66\xFC'

class TrackTranslateCodec(UnsignedInt):
        header='\x66\xBF'

class TrackTranslateTrackID(Binary):
        header='\x66\xA5'

class FlagInterlaced(UnsignedInt):
        header='\x9A'

class StereoMode(UnsignedInt):
        header='\x53\xB8'

class PixelWidth(UnsignedInt):
        header='\xB0'

class PixelHeight(UnsignedInt):
        header='\xBA'

class PixelCropBottom(UnsignedInt):
        header='\x54\xAA'

class PixelCropTop(UnsignedInt):
        header='\x54\xBB'

class PixelCropLeft(UnsignedInt):
        header='\x54\xCC'

class PixelCropRight(UnsignedInt):
        header='\x54\xDD'

class DisplayWidth(UnsignedInt):
        header='\x54\xB0'

class DisplayHeight(UnsignedInt):
        header='\x54\xBA'

class DisplayUnit(UnsignedInt):
        header='\x54\xB2'

class AspectRatioType(UnsignedInt):
        header='\x54\xB3'

class ColourSpace(Binary):
        header='\x2E\xB5\x24'

class SamplingFrequency(Float):
        header='\xB5'

class OutputSamplingFrequency(Float):
        header='\x78\xB5'

class Channels(UnsignedInt):
        header='\x9F'

class BitDepth(UnsignedInt):
        header='\x62\x64'

class TrackCombinePlanes(Master):
        header='\xE3'

class TrackJoinBlocks(Master):
        header='\xE9'

class ContentEncoding(Master):
        header='\x62\x40'

class CueTrack(UnsignedInt):
        header='\xF7'

class CueClusterPosition(UnsignedInt):
        header='\xF1'

class CueBlockNumber(UnsignedInt):
        header='\x53\x78'

class CueCodecState(UnsignedInt):
        header='\xEA'

class CueReference(Master):
        header='\xDB'

class ChapterUID(UnsignedInt):
        header='\x73\xC4'

class ChapterTimeStart(UnsignedInt):
        header='\x91'

class ChapterTimeEnd(UnsignedInt):
        header='\x92'

class ChapterFlagHidden(UnsignedInt):
        header='\x98'

class ChapterFlagEnabled(UnsignedInt):
        header='\x45\x98'

class ChapterSegmentUID(Binary):
        header='\x6E\x67'

class ChapterSegmentEditionUID(Binary):
        header='\x6E\xBC'

class ChapterPhysicalEquiv(UnsignedInt):
        header='\x63\xC3'

class ChapterTrack(Master):
        header='\x8F'

class ChapterDisplay(Master):
        header='\x80'

class ChapProcess(Master):
        header='\x69\x44'

class TargetTypeValue(UnsignedInt):
        header='\x68\xCA'

class TargetType(String):
        header='\x63\xCA'

class TagTrackUID(UnsignedInt):
        header='\x63\xC5'

class TagEditionUID(UnsignedInt):
        header='\x63\xC9'

class TagChapterUID(UnsignedInt):
        header='\x63\xC4'

class TagAttachmentUID(UnsignedInt):
        header='\x63\xC6'

class TagName(UTF8):
        header='\x45\xA3'

class TagLanguage(String):
        header='\x44\x7A'

class TagDefault(UnsignedInt):
        header='\x44\x84'

class TagString(UTF8):
        header='\x44\x87'

class TagBinary(Binary):
        header='\x44\x85'


# Level 5

class BlockAddID(UnsignedInt):
        header='\xEE'

class BlockAdditional(Binary):
        header='\xA5'

class LaceNumber(UnsignedInt):
        header='\xCC'

class TrackPlane(Master):
        header='\xE4'

class TrackJoinUID(UnsignedInt):
        header='\xED'

class ContentEncodingOrder(UnsignedInt):
        header='\x50\x31'

class ContentEncodingScope(UnsignedInt):
        header='\x50\x32'

class ContentEncodingType(UnsignedInt):
        header='\x50\x33'

class ContentCompression(Master):
        header='\x50\x34'

class ContentEncryption(Master):
        header='\x50\x35'

class CueRefTime(UnsignedInt):
        header='\x96'

class ChapterTrackNumber(UnsignedInt):
        header='\x89'

class ChapString(UTF8):
        header='\x85'

class ChapLanguage(String):
        header='\x43\x7C'

class ChapCountry(String):
        header='\x43\x7E'

class ChapProcessCodecID(UnsignedInt):
        header='\x69\x55'

class ChapProcessPrivate(Binary):
        header='\x45\x0D'

class ChapProcessCommand(Master):
        header='\x69\x11'


# Level 6

class TrackPlaneUID(UnsignedInt):
        header='\xE5'

class TrackPlaneType(UnsignedInt):
        header='\xE6'

class ContentCompAlgo(UnsignedInt):
        header='\x42\x54'

class ContentCompSettings(Binary):
        header='\x42\x55'

class ContentEncAlgo(UnsignedInt):
        header='\x47\xE1'

class ContentEncKeyID(Binary):
        header='\x47\xE2'

class ContentSignature(Binary):
        header='\x47\xE3'

class ContentSigKeyID(Binary):
        header='\x47\xE4'

class ContentSigAlgo(UnsignedInt):
        header='\x47\xE5'

class ContentSigHashAlgo(UnsignedInt):
        header='\x47\xE6'

class ChapProcessTime(UnsignedInt):
        header='\x69\x22'

class ChapProcessData(Binary):
        header='\x69\x33'
