#!/usr/bin/python3
''' Module to search and append to a file '''


def append_after(filename="", search_string="", new_string=""):
    '''  inserts a line of text to a file, after each line
    containing a specific string 
    '''

    with open(filename, "r") as file:
        text = file.readlines()

    with open(filename, "w") as f:
        s = ""
        for line in text:
            s += line
            if search_string in line:
                s += new_string
        f.write(s)
