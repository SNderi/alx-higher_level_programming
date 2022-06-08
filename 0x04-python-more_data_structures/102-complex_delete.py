#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if value in a_dictionary.values():
        keys = list(a_dictionary.keys())
        values = list(a_dictionary.values())
        for val in values:
            if val == value:
                i = values.index(val)
                j = keys[i]
                a_dictionary.pop(j)
    return(a_dictionary)
