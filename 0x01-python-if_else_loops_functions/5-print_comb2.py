#!/usr/bin/python3
for n in range(0, 100):
    if n == 99:
        print("{:0=2d}".format(n), end="\n")
        continue
    print("{:0=2d},".format(n), end=" ")
