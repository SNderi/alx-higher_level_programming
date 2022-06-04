#!/usr/bin/python3
def no_c(my_string):
    newl = []
    for letter in my_string:
        if letter not in ('c', 'C'):
            newl.append(letter)
    return (''.join(newl))
