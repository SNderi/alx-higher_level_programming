#!/usr/bin/python3
import sys
if __name__ == "__main__":
    size = len(argv) - 1
    if size == 1:
        print("{} argument:".format(size))
    elif size == 0:
        print("{} arguments.".format(size))
        break
    else:
        print("{} arguments:".format(size))
    for i in range(0, len(sys.argv)):
        if i > 0:
            print("{}: {}".format(i, sys.argv[i]))
