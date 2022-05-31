#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if ord(char) in range(65, 91) or ord(char) == 32:
            print("{:c}".format(ord(char)), end="")
        else:
            print("{:c}".format(ord(char)-32), end="")
