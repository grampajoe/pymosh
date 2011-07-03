# mosh.py: pymosh example
#
# This example uses pymosh to perform "standard" datamoshing: removing
# every I-frame but the first to blend all the motion in an AVI video.
#
# Usage:
#   python mosh.py input_filename > output_filename

from pymosh import Index
from pymosh.mpeg4 import is_iframe
import sys

def mosh(filename):
    f = Index(filename)

    buf = [None] # So I can assign to the closed-over buffer
    def process_frame(frame):
        """Process a frame, holding onto one P-frame at a time, which is used to
        replace any I-frames encountered."""
        if buf[0] == None or not is_iframe(frame):
            buf[0] = frame
        else:
            frame = buf[0]
        return frame

    for stream in f.video:
        # Each I-frame is replaced by the following P-frame. Going
        # backwards makes this much less awkward. The first frame is kept
        # intact.
        newstream = map(process_frame, reversed(stream[1:])) + stream[:1]
        # Flip the frames back to the right order.
        newstream.reverse()
        stream.replace(newstream)

    # Call rebuild to recombine the modified streams and perform any other
    # maintenance the file format needs for clean output.
    f.rebuild()

    # Finally, write the modified file to stdout.
    f.write(sys.stdout)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "Usage: mosh.py filename"
        sys.exit(1)

    mosh(sys.argv[1])
