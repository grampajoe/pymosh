# sort.py: pymosh example
#
# This example sorts video frames by data size.
#
# Usage:
#   python sort.py input_filename > output_filename

import sys
from pymosh import Index


def avi_sort(filename):
    f = Index(filename)

    for stream in f.video:
        sorted_stream = sorted(stream, key=len, reverse=True)
        stream.replace(sorted_stream)

    f.rebuild()
    f.write(sys.stdout)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: {0} filename'.format(sys.argv[0]))

    avi_sort(sys.argv[1])
