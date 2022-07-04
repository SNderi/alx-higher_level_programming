#!/usr/bin/python3
''' Module Square inheriting from Rectangle '''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    ''' Represents a square
    Attr:
        size: length of square

    Methods:
        Area
    '''

    def __init__(self, size):
        ''' Initializes square dimension '''
        self.integer_validator('size', size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        ''' Finds square area.
        Overwrites the area() method from rectangle
        '''
        return self.__size * self.__size
