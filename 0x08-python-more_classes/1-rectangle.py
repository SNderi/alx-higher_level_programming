#!/usr/bin/python3
'''Module for real definition of a rectangle'''


class Rectangle:
    '''Represents a rectangle
    Attributes:
        width (int): Rectangle width size (Defaults to 0)
        height (int): Rectangle height size (Defaults to 0)
    '''

    def __init__(self, width=0, height=0):
        '''Initializes data
        Args:
            width (int): Rectangle width
            height (int): Rectangle height
        '''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''Width accessor
        Returns:
            width
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''Width mutator.
        Args:
            value (int): Size to set width to.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than 0.
        '''
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        '''Height accessor
        Returns:
            height
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''Height mutator.
        Args:
            value (int): Size to set height to.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than 0.
        '''
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
