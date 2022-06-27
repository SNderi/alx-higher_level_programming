#!/usr/bin/python3
'''Module for a rectangle with string representation'''


class Rectangle:
    '''Represents a rectangle
    Attributes:
        width (int): Rectangle width size (Defaults to 0)
        height (int): Rectangle height size (Defaults to 0)
        number_of_instances (int): Keeps count of number of objects in existence
        print_symbol - Element to use to draw the rectangle

    Methods:
        area: Returns rectangle area
        perimeter: Returns rectangle perimeter
    '''
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        '''Initializes data
        Args:
            width (int): Rectangle width
            height (int): Rectangle height
        '''
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        '''Returns an informal and nicely printable string representation
        of a Rectangle instance, filled with the '#' character
        '''
        rect = ''
        if self.__height == 0 or self.__width == 0:
            return ''
        for i in range(self.__height):
            rect += str(self.print_symbol) * self.__width
            rect += '\n'
        return rect[:-1]

    def __repr__(self):
        '''Returns a string representation of a Rectangle instance
        that is able to recreate a new instance by using eval()
        '''
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        '''Rectangle decommissioning'''
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1

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

    def area(self):
        '''Returns Area of the rectangle'''
        return self.__width * self.__height

    def perimeter(self):
        '''Finds rectangle perimeter
        Returns:
            perimeter or 0 if height or width is 0
        '''
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__width + self.__height) * 2
