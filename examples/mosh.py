# mosh.py: pymosh example
#
# This example uses pymosh to perform "standard" datamoshing: removing
# every I-frame but the first to blend all the motion in the video.
#
# Usage:
#   python mosh.py input_filename > output_filename

from pymosh.avi import AVIFile
from pymosh.mpeg4 import is_iframe
import sys

def mosh(filename):
    f = AVIFile(filename)

    buf = [None] # So I can assign to the closed-over buffer
    def process_frame(frame):
        """Process a frame, holding onto one P-frame at a time, which is used to
        replace any I-frames encountered."""
        if buf[0] == None or not is_iframe(frame):
            buf[0] = frame
        else:
            frame = buf[0]
        return frame

    # Modify the streams in place so the file can be rewritten.
    for stream in f:
        if stream.type == 'vids':
            # Each I-frame is replaced by the following P-frame. Going
            # backwards makes this much less awkward. The first frame is kept
            # intact.
            newstream = map(process_frame, reversed(stream[1:])) + stream[:1]
            # Flip the frames back to the right order.
            newstream.reverse()
            stream.replace(newstream)

    # Call rebuild_riff to recombine the modified streams and replace the AVI
    # index.
    f.rebuild_riff()

    # Finally, write the modified file to stdout.
    f.write_data(sys.stdout)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "Usage: mosh.py filename"
        sys.exit(1)

    mosh(sys.argv[1])
