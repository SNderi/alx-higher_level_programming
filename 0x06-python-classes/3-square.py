#!/usr/bin/python3
'''Square module with method area'''


class Square:
    '''Represents a square.
    Attributes:
        size (int): Length of square (default=0).
    Methods:
        area: Returns area of square'''

    def __init__(self, size=0):
        '''Initializes data.
        Args:
            size (int): Length of Square.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.'''

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        '''Finds current square area.
        Returns:
            Square area.'''

        return (self.__size * self.__size)
