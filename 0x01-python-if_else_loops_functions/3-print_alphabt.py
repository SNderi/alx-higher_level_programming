#!/usr/bin/python3
for l in range(97, 123):
    if l in (101, 113):
        continue
    print("{:c}".format(l), end="")
