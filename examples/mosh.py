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
        if buf[0] == None:
            buf[0] = frame
        else:
            if is_iframe(frame):
                frame = buf[0]
            else:
                buf[0] = frame
        return frame

    # Modify the streams in place so the file can be rewritten.
    for i in range(len(f.streams)):
        stream = f.streams[i]
        if stream.type == 'vids':
            # Each I-frame is replaced by the following P-frame. Going
            # backwards makes this much less awkward. The first frame is kept
            # intact.
            f.streams[i] = map(process_frame, reversed(stream[1:])) + stream[:1]
            # Flip the frames back to the right order.
            f.streams[i].reverse()

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
