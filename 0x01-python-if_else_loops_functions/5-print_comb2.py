#!/usr/bin/python3
for n in range(0, 100):
    if n == 99:
        print("{:0=2d}\n".format(n), end=" ")
        continue
    print("{:0=2d},".format(n), end=" ")
