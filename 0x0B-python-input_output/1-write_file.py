#!/usr/bin/python3
''' Module for writing to a file '''


def write_file(filename="", text=""):
    ''' Writes a string to a text file (UTF8) and
    returns the number of characters written
    '''
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
