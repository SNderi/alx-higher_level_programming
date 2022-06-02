#!/usr/bin/python3
import sys
if __name__ == "__main__":
    size = len(sys.argv) - 1
    if size == 1:
        print("{} argument:".format(size))
    elif size == 0:
        print("{} arguments.".format(size))
        break
    else:
        print("{} arguments:".format(size))
    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, argv[i]))

