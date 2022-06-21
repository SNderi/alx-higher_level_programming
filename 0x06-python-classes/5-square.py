#!/usr/bin/python3
'''Square module with # square drawer'''


class Square:
    '''Represents a square.
    Attributes:
        size (int): Length of square (default=0).
    Methods:
        area: Returns area of square.
        my_print: Draws square using #.'''

    @property
    def size(self):
        '''Size accessor.
        Returns:
            size.'''
        return (self.__size)

    @size.setter
    def size(self, value):
        '''Size mutator.
        Args:
            value (int): Length to set size to.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.'''

        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def __init__(self, size=0):
        '''Initializes data.
        Args:
            size (int): Default length of Square.'''
        self.__size = size

    def area(self):
        '''Finds current square area.
        Returns:
            Square area.'''
        return (self.__size * self.__size)

    def my_print(self):
        '''Prints the square using #.'''
        if self.__size == 0:
            print()
        for i in range(self.__size):
            print('#' * self.__size)
