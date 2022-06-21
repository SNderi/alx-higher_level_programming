#!/usr/bin/python3
'''Square module with object variable validation.'''


class Square:
    '''Represents a square with attribute validation.
    Attributes:
        size (int): Length of square (default=0).'''

    def __init__(self, size=0):
        '''Initializes data.
        Args:
            size (int): Length of Square
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.'''

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
