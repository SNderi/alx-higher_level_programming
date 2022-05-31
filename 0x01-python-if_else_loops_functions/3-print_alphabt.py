#!/usr/bin/python3
for num in range(97, 123):
    if num in (101, 113):
        continue
    print("{:c}".format(num), end="")
