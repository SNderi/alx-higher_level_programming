#!/usr/bin/python3
'''Square module with # square drawer with spaces'''


class Square:
    '''Represents a square.
    Attributes:
        size (int): Length of square (default=0).
        position (int): Tuple of 2 positive integers (default=(0,0)).
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
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        '''position accessor.
        Returns:
            position'''
        return (self.__position)

    @position.setter
    def position(self, value):
        '''position mutator.
            Args:
                value (int): Tuple of 2 positive integers.
            Raises:
                TypeError: If value isn't a tuple of 2 positive integers.'''
        if not isinstance(value, tuple) and len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if not isinstance(value[0], int) and not isinstance[value[1], int]:
            raise TypeError('position must be a tuple of 2 positive integers')
        if value[0] < 0 and value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def __init__(self, size=0, position=(0, 0)):
        '''Initializes data.
        Args:
            size (int): Default length of Square.
            position (tuple): Tuple of 2 positive integers'''
        self.__size = size
        self.__position = position

    def area(self):
        '''Finds current square area.
        Returns:
            Square area.'''
        return (self.__size * self.__size)

    def my_print(self):
        '''Prints the square using #.'''
        if self.__size == 0:
            print()
            return
        for j in range(self.__position[1]):
            print()
        a = " " * self.__position[0]
        for i in range(self.__size):
            #for k in range(self.__position[0]):
                #print(" ", end="")
            print(a + '#' * self.__size)
