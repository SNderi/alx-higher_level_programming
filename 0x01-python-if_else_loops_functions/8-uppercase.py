#!/usr/bin/python3
def uppercase(str):
    for l in str:
        if ord(l) in range(65, 91) or ord(l) == 32:
            print("{:c}".format(ord(l)), end="")
        else:
            print("{:c}".format(ord(l)-32), end="")
