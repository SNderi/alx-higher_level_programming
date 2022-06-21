#!/usr/bin/python3
'''Square module with object attribute initialization'''


class Square:
    '''Represents a square with no type/value verification
    Attributes:
        size (int): Length of square'''

    def __init__(self, size):
        '''Initialize data
        Args:
            size (int): Length of Square'''
        self.__size = size
